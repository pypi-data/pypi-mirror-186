from ratio.http.response import Response
from typing import Literal


def redirect(
    url: str, type_: Literal["temporary", "permanent", "301", "302"] = "temporary"
) -> Response:
    is_permanent_redirect = type_ in {"permanent", "301"}
    allow_method_change = type_ in {"301", "302"}

    return Response.redirect(url, is_permanent_redirect, allow_method_change)
