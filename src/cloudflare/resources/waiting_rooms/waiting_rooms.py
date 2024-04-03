# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .page import (
    Page,
    AsyncPage,
    PageWithRawResponse,
    AsyncPageWithRawResponse,
    PageWithStreamingResponse,
    AsyncPageWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .events import (
    Events,
    AsyncEvents,
    EventsWithRawResponse,
    AsyncEventsWithRawResponse,
    EventsWithStreamingResponse,
    AsyncEventsWithStreamingResponse,
)
from ...types import (
    WaitingRoom,
    WaitingRoomDeleteResponse,
    waiting_room_edit_params,
    waiting_room_create_params,
    waiting_room_delete_params,
    waiting_room_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from .statuses import (
    Statuses,
    AsyncStatuses,
    StatusesWithRawResponse,
    AsyncStatusesWithRawResponse,
    StatusesWithStreamingResponse,
    AsyncStatusesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from .events.events import Events, AsyncEvents
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["WaitingRooms", "AsyncWaitingRooms"]


class WaitingRooms(SyncAPIResource):
    @cached_property
    def page(self) -> Page:
        return Page(self._client)

    @cached_property
    def events(self) -> Events:
        return Events(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def statuses(self) -> Statuses:
        return Statuses(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> WaitingRoomsWithRawResponse:
        return WaitingRoomsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WaitingRoomsWithStreamingResponse:
        return WaitingRoomsWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_create_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_create_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Creates a new waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/waiting_rooms",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_create_params.WaitingRoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_update_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_update_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Updates a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_update_params.WaitingRoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoom]:
        """
        Lists waiting rooms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms",
            page=SyncSinglePage[WaitingRoom],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoom,
        )

    def delete(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoomDeleteResponse:
        """
        Deletes a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=maybe_transform(body, waiting_room_delete_params.WaitingRoomDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoomDeleteResponse], ResultWrapper[WaitingRoomDeleteResponse]),
        )

    def edit(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_edit_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_edit_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Patches a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_edit_params.WaitingRoomEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Fetches a single configured waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )


class AsyncWaitingRooms(AsyncAPIResource):
    @cached_property
    def page(self) -> AsyncPage:
        return AsyncPage(self._client)

    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def statuses(self) -> AsyncStatuses:
        return AsyncStatuses(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWaitingRoomsWithRawResponse:
        return AsyncWaitingRoomsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWaitingRoomsWithStreamingResponse:
        return AsyncWaitingRoomsWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_create_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_create_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Creates a new waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/waiting_rooms",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_create_params.WaitingRoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    async def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_update_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_update_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Updates a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_update_params.WaitingRoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoom, AsyncSinglePage[WaitingRoom]]:
        """
        Lists waiting rooms.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms",
            page=AsyncSinglePage[WaitingRoom],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoom,
        )

    async def delete(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoomDeleteResponse:
        """
        Deletes a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=await async_maybe_transform(body, waiting_room_delete_params.WaitingRoomDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoomDeleteResponse], ResultWrapper[WaitingRoomDeleteResponse]),
        )

    async def edit(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[waiting_room_edit_params.AdditionalRoute] | NotGiven = NOT_GIVEN,
        cookie_attributes: waiting_room_edit_params.CookieAttributes | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Patches a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                },
                waiting_room_edit_params.WaitingRoomEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    async def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Fetches a single configured waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )


class WaitingRoomsWithRawResponse:
    def __init__(self, waiting_rooms: WaitingRooms) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = to_raw_response_wrapper(
            waiting_rooms.create,
        )
        self.update = to_raw_response_wrapper(
            waiting_rooms.update,
        )
        self.list = to_raw_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = to_raw_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = to_raw_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = to_raw_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> PageWithRawResponse:
        return PageWithRawResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> StatusesWithRawResponse:
        return StatusesWithRawResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._waiting_rooms.settings)


class AsyncWaitingRoomsWithRawResponse:
    def __init__(self, waiting_rooms: AsyncWaitingRooms) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = async_to_raw_response_wrapper(
            waiting_rooms.create,
        )
        self.update = async_to_raw_response_wrapper(
            waiting_rooms.update,
        )
        self.list = async_to_raw_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = async_to_raw_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> AsyncPageWithRawResponse:
        return AsyncPageWithRawResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> AsyncStatusesWithRawResponse:
        return AsyncStatusesWithRawResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._waiting_rooms.settings)


class WaitingRoomsWithStreamingResponse:
    def __init__(self, waiting_rooms: WaitingRooms) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = to_streamed_response_wrapper(
            waiting_rooms.create,
        )
        self.update = to_streamed_response_wrapper(
            waiting_rooms.update,
        )
        self.list = to_streamed_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = to_streamed_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = to_streamed_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = to_streamed_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> PageWithStreamingResponse:
        return PageWithStreamingResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> StatusesWithStreamingResponse:
        return StatusesWithStreamingResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._waiting_rooms.settings)


class AsyncWaitingRoomsWithStreamingResponse:
    def __init__(self, waiting_rooms: AsyncWaitingRooms) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = async_to_streamed_response_wrapper(
            waiting_rooms.create,
        )
        self.update = async_to_streamed_response_wrapper(
            waiting_rooms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> AsyncPageWithStreamingResponse:
        return AsyncPageWithStreamingResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> AsyncStatusesWithStreamingResponse:
        return AsyncStatusesWithStreamingResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._waiting_rooms.settings)
