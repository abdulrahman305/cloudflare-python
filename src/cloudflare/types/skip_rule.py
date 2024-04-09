# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .shared import UnnamedSchemaRef70f2c6ccd8a405358ac7ef8fc3d6751c
from .._models import BaseModel

__all__ = ["SkipRule", "ActionParameters"]


class ActionParameters(BaseModel):
    phases: Optional[
        List[
            Literal[
                "ddos_l4",
                "ddos_l7",
                "http_config_settings",
                "http_custom_errors",
                "http_log_custom_fields",
                "http_ratelimit",
                "http_request_cache_settings",
                "http_request_dynamic_redirect",
                "http_request_firewall_custom",
                "http_request_firewall_managed",
                "http_request_late_transform",
                "http_request_origin",
                "http_request_redirect",
                "http_request_sanitize",
                "http_request_sbfm",
                "http_request_select_configuration",
                "http_request_transform",
                "http_response_compression",
                "http_response_firewall_managed",
                "http_response_headers_transform",
                "magic_transit",
                "magic_transit_ids_managed",
                "magic_transit_managed",
            ]
        ]
    ] = None
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: Optional[
        List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    ] = None
    """A list of legacy security products to skip the execution of."""

    rules: Optional[Dict[str, List[str]]] = None
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Optional[Literal["current"]] = None
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: Optional[List[str]] = None
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class SkipRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["skip"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[ActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[UnnamedSchemaRef70f2c6ccd8a405358ac7ef8fc3d6751c] = None
    """An object configuring the rule's logging behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule ID by default)."""
