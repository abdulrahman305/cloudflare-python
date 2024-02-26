# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLInfoGetParams", "URLIDParam"]


class URLInfoGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    url: str

    url_id_param: URLIDParam


class URLIDParam(TypedDict, total=False):
    url_id: int
    """Submission ID(s) to filter submission results by."""
