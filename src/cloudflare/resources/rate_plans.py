# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)
from ..types.rate_plans import RatePlanGetResponse

__all__ = ["RatePlans", "AsyncRatePlans"]


class RatePlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatePlansWithRawResponse:
        return RatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatePlansWithStreamingResponse:
        return RatePlansWithStreamingResponse(self)

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RatePlanGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatePlanGetResponse]], ResultWrapper[RatePlanGetResponse]),
        )


class AsyncRatePlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatePlansWithRawResponse:
        return AsyncRatePlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatePlansWithStreamingResponse:
        return AsyncRatePlansWithStreamingResponse(self)

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RatePlanGetResponse]:
        """
        Lists all rate plans the zone can subscribe to.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/available_rate_plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RatePlanGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatePlanGetResponse]], ResultWrapper[RatePlanGetResponse]),
        )


class RatePlansWithRawResponse:
    def __init__(self, rate_plans: RatePlans) -> None:
        self._rate_plans = rate_plans

        self.get = to_raw_response_wrapper(
            rate_plans.get,
        )


class AsyncRatePlansWithRawResponse:
    def __init__(self, rate_plans: AsyncRatePlans) -> None:
        self._rate_plans = rate_plans

        self.get = async_to_raw_response_wrapper(
            rate_plans.get,
        )


class RatePlansWithStreamingResponse:
    def __init__(self, rate_plans: RatePlans) -> None:
        self._rate_plans = rate_plans

        self.get = to_streamed_response_wrapper(
            rate_plans.get,
        )


class AsyncRatePlansWithStreamingResponse:
    def __init__(self, rate_plans: AsyncRatePlans) -> None:
        self._rate_plans = rate_plans

        self.get = async_to_streamed_response_wrapper(
            rate_plans.get,
        )
