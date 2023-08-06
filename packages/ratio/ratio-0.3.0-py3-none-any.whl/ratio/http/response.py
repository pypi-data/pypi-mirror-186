from http import HTTPStatus
from typing import Self, TypedDict, NotRequired


class ResponseData(TypedDict):
    code: int
    message: NotRequired[str]
    headers: NotRequired[dict[str, str | list[str]]]


class Response:
    """Generic response class for all default responses"""

    code: int
    message: str
    __headers: dict[str, str | list[str]]
    __success: bool

    def __init__(self, data: ResponseData) -> None:
        code = data["code"]

        try:
            assert 100 < code < 600
        except AssertionError:
            code = 500

        self.code = code
        self.message = data.get("message", "")
        self.__headers = data.get("headers", {})

    # Reason for ignoring type: Self is actually valid. In new version of Mypy this will be supported.
    @classmethod
    def from_http_status(cls, status: HTTPStatus) -> Self:  # type: ignore
        return cls({"code": status.value, "message": status.phrase})

    @property
    def success(self) -> bool:
        return 200 <= self.code <= 299

    @property
    def headers(self) -> list[tuple[bytes, bytes]]:
        normalized_headers = {
            key: (value if isinstance(value, list) else [value])
            for key, value in self.__headers.items()
        }

        return [
            (header.encode("utf-8"), value.encode("utf-8"))
            for header in normalized_headers
            for value in normalized_headers[header]
        ]

    @classmethod
    def redirect(cls, url: str, is_permanent: bool = False, allow_method_change: bool = False) -> Self:  # type: ignore
        status = (
            HTTPStatus.PERMANENT_REDIRECT
            if is_permanent is True and allow_method_change is False
            else HTTPStatus.MOVED_PERMANENTLY
            if is_permanent is True and allow_method_change is True
            else HTTPStatus.FOUND
            if is_permanent is False and allow_method_change is True
            else HTTPStatus.TEMPORARY_REDIRECT
        )

        return cls({"code": status.value, "headers": {"Location": url}})
