"""Utils used by SaxoOpenAPIClient."""

import json
from datetime import datetime, timezone
from http import HTTPStatus
from typing import Dict, Optional
from urllib.parse import urlencode

import httpx
from loguru import logger
from pydantic import AnyHttpUrl, parse_obj_as

from .models import APIResponseError, HttpsUrl, OpenAPIAppConfig, StreamingMessage
from .version import VERSION


def configure_logger(log_sink: str, log_level: str) -> None:
    """Set defaults for log config."""
    logger.add(
        log_sink,
        format=(
            "{time:YYYY-MM-DD HH:mm:ss.SSS!UTC}Z {thread:12} {level:8} "
            "{module:15} {line:3} {function:25} {message}"
        ),
        level=log_level,
        enqueue=True,
    )


def make_default_session_headers() -> Dict:
    """Set default HTTP session."""
    headers: Dict[str, str] = {
        "accept": "application/json; charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": f"saxo-apy/{VERSION}",
        "connection": "keep-alive",
        "cache-control": "no-cache",
    }
    return headers


def unix_seconds_to_datetime(timestamp: int) -> datetime:
    """Convert unix seconds to human-readable timestamp."""
    return datetime.fromtimestamp(timestamp, tz=timezone.utc)


def validate_redirect_url(
    app_config: OpenAPIAppConfig, redirect_url: Optional[AnyHttpUrl]
) -> AnyHttpUrl:
    """Check if provided redirect URL for login is valid - or default to config."""
    if not redirect_url:
        logger.debug(
            "no redirect URL provided - defaulting to first localhost in config"
        )
        # defaults to first available localhost redirect for convenience
        _redirect_url: AnyHttpUrl = [
            url for url in app_config.redirect_urls if url.host == "localhost"
        ][0]
    else:
        assert redirect_url in app_config.redirect_urls, (
            f"redirect url {redirect_url} not available in app config "
            "- see client.available_redirect_urls"
        )
        _redirect_url = redirect_url
    return _redirect_url


def construct_auth_url(
    app_config: OpenAPIAppConfig, redirect_url: AnyHttpUrl, state: str
) -> HttpsUrl:
    """Parse app_config to generate auth URL."""
    auth_request_query_params = {
        "response_type": "code",
        "client_id": app_config.client_id,
        "state": state,
        "redirect_uri": redirect_url,
    }

    return parse_obj_as(
        HttpsUrl,
        app_config.auth_endpoint + "?" + urlencode(auth_request_query_params),
    )


def handle_api_response(response: httpx.Response) -> httpx.Response:
    """Handle response from OpenAPI."""
    s = response.status_code
    if "/sim" in str(response.request.url):
        env = "SIM"
    else:
        env = "LIVE"

    error_msg = None
    if s == HTTPStatus.BAD_REQUEST:
        error_msg = f"invalid request sent, please see error details: {response.text}"
    elif s == HTTPStatus.UNAUTHORIZED:
        error_msg = "access token missing, incorrect, or expired"
    elif s == HTTPStatus.FORBIDDEN:
        error_msg = (
            "you are not authorized to access this resource - check if you are "
            "logged in with write permissions and/or market data has been enabled"
        )
    elif s == HTTPStatus.NOT_FOUND:
        error_msg = f"requested resource not found: {response.request.url}"
    elif s == HTTPStatus.METHOD_NOT_ALLOWED:
        error_msg = (
            f"the requested method ({response.request.method}) is not valid for this "
            f"endpoint: {response.request.url}"
        )
    elif s in range(500, 505):
        error_msg = (
            "server error occurred, please ensure your request is correct "
            "and/or notify Saxo if this error persists"
        )

    if error_msg:
        raise APIResponseError(
            f"status: {s} - {HTTPStatus(s).name.replace('_', ' ')}\n"
            f"error: {error_msg}\n"
            f"client request id: {response.request.headers.get('x-request-id')}\n"
            f"server trace id: {response.headers.get('x-correlation')}\n"
            f"timestamp (UTC): {datetime.utcnow()} - env: {env}"
        )

    logger.success(
        "successfully performed API request with X-Request-Id: "
        f"{response.request.headers['x-request-id']}"
    )

    return response


def decode_streaming_message(message: bytes) -> StreamingMessage:
    """Decode streaming message byte and convert to dict."""
    logger.debug(f"received streaming message: {str(message)}")
    message_id = int.from_bytes(message[0:8], byteorder="little")
    ref_id_len = int(message[10])
    ref_id = message[11 : 11 + ref_id_len].decode()  # noqa
    format = int(message[11 + ref_id_len])
    if format != 0:
        raise RuntimeError(
            f"unsupported payload format received on streaming connection: {format}"
        )
    payload_size = int.from_bytes(
        message[12 + ref_id_len : 16 + ref_id_len], byteorder="little"  # noqa
    )
    payload = message[16 + ref_id_len : 16 + ref_id_len + payload_size].decode()  # noqa
    deserialized = json.loads(payload)
    return StreamingMessage(msg_id=message_id, ref_id=ref_id, data=deserialized)
