use std::{marker::PhantomData, time::Duration};

use reqwest::{header::HeaderValue, Method, StatusCode};
use serde::{de::DeserializeOwned, Deserialize, Serialize};

use crate::{
    signature::{signature, SignatureParams},
    timestamp::Timestamp,
    HttpClient, HttpClientError, HttpClientResult,
};

const USER_AGENT: &str = "openapi-sdk";
const REQUEST_TIMEOUT: Duration = Duration::from_secs(30);
const RETRY_COUNT: usize = 5;
const RETRY_INITIAL_DELAY: Duration = Duration::from_millis(100);
const RETRY_FACTOR: f32 = 2.0;

#[derive(Deserialize)]
struct OpenApiResponse<T> {
    code: i32,
    message: String,
    data: Option<T>,
}

/// A request builder
pub struct RequestBuilder<T, Q, R> {
    client: HttpClient,
    method: Method,
    path: String,
    body: Option<T>,
    query_params: Option<Q>,
    mark_resp: PhantomData<R>,
}

impl RequestBuilder<(), (), ()> {
    pub(crate) fn new(client: HttpClient, method: Method, path: impl Into<String>) -> Self {
        Self {
            client,
            method,
            path: path.into(),
            body: None,
            query_params: None,
            mark_resp: PhantomData,
        }
    }
}

impl<T, Q, R> RequestBuilder<T, Q, R> {
    /// Set the request body
    #[must_use]
    pub fn body<T2>(self, body: T2) -> RequestBuilder<T2, Q, R>
    where
        T2: Serialize + Send + Sync + 'static,
    {
        RequestBuilder {
            client: self.client,
            method: self.method,
            path: self.path,
            body: Some(body),
            query_params: self.query_params,
            mark_resp: self.mark_resp,
        }
    }

    /// Set the query string
    #[must_use]
    pub fn query_params<Q2>(self, params: Q2) -> RequestBuilder<T, Q2, R>
    where
        Q2: Serialize + Send + Sync + 'static,
    {
        RequestBuilder {
            client: self.client,
            method: self.method,
            path: self.path,
            body: self.body,
            query_params: Some(params),
            mark_resp: self.mark_resp,
        }
    }

    /// Set the response body type
    #[must_use]
    pub fn response<R2>(self) -> RequestBuilder<T, Q, R2>
    where
        R2: DeserializeOwned + Send + 'static,
    {
        RequestBuilder {
            client: self.client,
            method: self.method,
            path: self.path,
            body: self.body,
            query_params: self.query_params,
            mark_resp: PhantomData,
        }
    }
}

impl<T, Q, R> RequestBuilder<T, Q, R>
where
    T: Serialize + Send + 'static,
    Q: Serialize + Send + 'static,
    R: DeserializeOwned + Send + 'static,
{
    async fn do_send(&self) -> HttpClientResult<R> {
        let HttpClient {
            http_cli,
            config,
            default_headers,
        } = &self.client;
        let now = Timestamp::now();
        let app_key_value =
            HeaderValue::from_str(&config.app_key).map_err(|_| HttpClientError::InvalidApiKey)?;
        let access_token_value = HeaderValue::from_str(&config.access_token)
            .map_err(|_| HttpClientError::InvalidAccessToken)?;

        let mut request_builder = http_cli
            .request(
                self.method.clone(),
                &format!("{}{}", config.http_url, self.path),
            )
            .headers(default_headers.clone())
            .header("User-Agent", USER_AGENT)
            .header("X-Api-Key", app_key_value)
            .header("Authorization", access_token_value)
            .header("X-Timestamp", now.to_string())
            .header("Content-Type", "application/json; charset=utf-8");

        // set the request body
        if let Some(body) = &self.body {
            request_builder = request_builder
                .body(serde_json::to_string(body).map_err(HttpClientError::SerializeRequestBody)?);
        }

        let mut request = request_builder.build().expect("invalid request");

        // set the query string
        if let Some(query_params) = &self.query_params {
            let query_string = crate::qs::to_string(&query_params)?;
            request.url_mut().set_query(Some(&query_string));
        }

        // signature the request
        let sign = signature(SignatureParams {
            request: &request,
            app_key: &config.app_key,
            access_token: Some(&config.access_token),
            app_secret: &config.app_secret,
            timestamp: now,
        });
        request.headers_mut().insert(
            "X-Api-Signature",
            HeaderValue::from_maybe_shared(sign).expect("valid signature"),
        );

        tracing::debug!(method = %request.method(), url = %request.url(), "http request");

        // send request
        let (status, text) = tokio::time::timeout(REQUEST_TIMEOUT, async move {
            let resp = http_cli.execute(request).await?;
            let status = resp.status();
            let text = resp.text().await.map_err(HttpClientError::from)?;
            Ok::<_, HttpClientError>((status, text))
        })
        .await
        .map_err(|_| HttpClientError::RequestTimeout)??;

        tracing::debug!(body = text.as_str(), "http response");

        match serde_json::from_str::<OpenApiResponse<R>>(&text) {
            Ok(resp) if resp.code == 0 => resp.data.ok_or(HttpClientError::UnexpectedResponse),
            Ok(resp) => Err(HttpClientError::OpenApi {
                code: resp.code,
                message: resp.message,
            }),
            Err(err) if status == StatusCode::OK => {
                Err(HttpClientError::DeserializeResponseBody(err))
            }
            Err(_) => Err(HttpClientError::BadStatus(status)),
        }
    }

    /// Send request and get the response
    #[tracing::instrument(level = "debug", skip(self))]
    pub async fn send(self) -> HttpClientResult<R> {
        match self.do_send().await {
            Ok(resp) => Ok(resp),
            Err(HttpClientError::BadStatus(StatusCode::TOO_MANY_REQUESTS)) => {
                let mut retry_delay = RETRY_INITIAL_DELAY;

                for _ in 0..RETRY_COUNT {
                    tokio::time::sleep(retry_delay).await;

                    match self.do_send().await {
                        Ok(resp) => return Ok(resp),
                        Err(HttpClientError::BadStatus(StatusCode::TOO_MANY_REQUESTS)) => {
                            retry_delay =
                                Duration::from_secs_f32(retry_delay.as_secs_f32() * RETRY_FACTOR);
                            continue;
                        }
                        Err(err) => return Err(err),
                    }
                }

                Err(HttpClientError::BadStatus(StatusCode::TOO_MANY_REQUESTS))
            }
            Err(err) => Err(err),
        }
    }
}
