import binascii
import hashlib
import hmac
import json
from datetime import datetime
from typing import Optional
from urllib.parse import quote, unquote

import requests


class SbercloudAuthRequests:
    """Implements authentication mechanism with access key+secret key in accordance with:
    https://support.hc.sbercloud.ru/devg/apisign/api-sign-algorithm.html
    """

    ENCODING = "utf-8"
    ALGORITHM = "SDK-HMAC-SHA256"
    TIMESTAMP_FORMAT = "%Y%m%dT%H%M%SZ"

    def __init__(
        self, endpoint: str, access_key_id: str, secret_key: str, base_path: str = ""
    ) -> None:
        """Initializes a new instance of requests class.

        Args:
            endpoint: Represents endpoint of a specific service
                (listed at https://support.hc.sbercloud.ru/en-us/endpoint/index.html).
            base_path: Prefix for all request path's that will be sent via this instance.
            access_key_id: Access key from Sbercloud credentials.
            secret_key: Secret key from Sbercloud credentials.
        """
        self.endpoint = endpoint
        self.base_path = base_path
        self.access_key_id = access_key_id
        self.secret_key = secret_key

    def get(self, path: str, query: Optional[dict] = None) -> requests.Response:
        return self._send_request("GET", path, query, data=None)

    def delete(self, path: str, query: Optional[dict] = None) -> requests.Response:
        return self._send_request("DELETE", path, query, data=None)

    def post(
        self, path: str, query: Optional[dict] = None, data: Optional[dict] = None
    ) -> requests.Response:
        return self._send_request("POST", path, query, data)

    def _send_request(
        self, method: str, path: str, query: Optional[dict], data: Optional[dict]
    ) -> requests.Response:
        if self.base_path:
            path = self.base_path + path

        timestamp = datetime.strftime(datetime.utcnow(), self.TIMESTAMP_FORMAT)
        headers = self._build_original_headers(timestamp)

        content = ""
        if data:
            # At the moment we support json content only
            content = json.dumps(data)
            headers["Content-Type"] = "application/json"
        body = content.encode(self.ENCODING)

        signed_headers = self._build_signed_headers(headers)
        canonical_request = self._build_canonical_request(
            method, path, query, body, headers, signed_headers
        )
        signature = self._build_signature(timestamp, canonical_request)
        headers["Authorization"] = self._build_authorization_header(signature, signed_headers)

        query_string = "?" + self._build_canonical_query_string(query) if query else ""
        url = f"https://{self.endpoint}{path}{query_string}"

        response = requests.request(method, url, headers=headers, data=body)
        if response.status_code < 200 or response.status_code >= 300:
            raise AssertionError(
                f"Request to url={url} failed: status={response.status_code} "
                f"response={response.text})"
            )
        return response

    def _build_original_headers(self, timestamp: str) -> dict[str, str]:
        return {
            "X-Sdk-Date": timestamp,
            "host": self.endpoint,
        }

    def _build_signed_headers(self, headers: dict[str, str]) -> list[str]:
        return sorted(header_name.lower() for header_name in headers)

    def _build_canonical_request(
        self,
        method: str,
        path: str,
        query: Optional[dict],
        body: bytes,
        headers: dict[str, str],
        signed_headers: list[str],
    ) -> str:
        canonical_headers = self._build_canonical_headers(headers, signed_headers)
        body_hash = self._calc_sha256_hash(body)
        canonical_url = self._build_canonical_url(path)
        canonical_query_string = self._build_canonical_query_string(query)

        return "\n".join(
            [
                method.upper(),
                canonical_url,
                canonical_query_string,
                canonical_headers,
                ";".join(signed_headers),
                body_hash,
            ]
        )

    def _build_canonical_headers(self, headers: dict[str, str], signed_headers: list[str]) -> str:
        normalized_headers = {}
        for key, value in headers.items():
            normalized_key = key.lower()
            normalized_value = value.strip()
            normalized_headers[normalized_key] = normalized_value
            # Re-encode header in request itself (iso-8859-1 comes from HTTP 1.1 standard)
            headers[key] = normalized_value.encode(self.ENCODING).decode("iso-8859-1")

        # Join headers in the same order as they are sorted in signed_headers list
        joined_headers = "\n".join(f"{key}:{normalized_headers[key]}" for key in signed_headers)
        return joined_headers + "\n"

    def _calc_sha256_hash(self, value: bytes) -> str:
        sha256 = hashlib.sha256()
        sha256.update(value)
        return sha256.hexdigest()

    def _build_canonical_url(self, path: str) -> str:
        path_parts = unquote(path).split("/")
        canonical_url = "/".join(quote(path_part) for path_part in path_parts)

        if not canonical_url.endswith("/"):
            canonical_url += "/"
        return canonical_url

    def _build_canonical_query_string(self, query: Optional[dict]) -> str:
        if not query:
            return ""

        key_value_pairs = []
        for key in sorted(query.keys()):
            # NOTE: we do not support list values, as they are not used in API at the moment
            encoded_key = quote(key)
            encoded_value = quote(str(query[key]))
            key_value_pairs.append(f"{encoded_key}={encoded_value}")
        return "&".join(key_value_pairs)

    def _build_signature(self, timestamp: str, canonical_request: str) -> str:
        canonical_request_hash = self._calc_sha256_hash(canonical_request.encode(self.ENCODING))
        string_to_sign = f"{self.ALGORITHM}\n{timestamp}\n{canonical_request_hash}"

        hmac_digest = hmac.new(
            key=self.secret_key.encode(self.ENCODING),
            msg=string_to_sign.encode(self.ENCODING),
            digestmod=hashlib.sha256,
        ).digest()
        signature = binascii.hexlify(hmac_digest).decode()

        return signature

    def _build_authorization_header(self, signature: str, signed_headers: list[str]) -> str:
        joined_signed_headers = ";".join(signed_headers)
        return f"{self.ALGORITHM} Access={self.access_key_id}, SignedHeaders={joined_signed_headers}, Signature={signature}"
