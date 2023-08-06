"""
Exposes top-level aliases for using the alerts client.
"""

import os
from typing import Dict, List, Optional, Union
from urllib.parse import urlparse
from uuid import UUID

from gantry.alerts import globals
from gantry.alerts.client import GantryAlerts
from gantry.alerts.globals import _alerts_alias, validate_init
from gantry.api_client import APIClient
from gantry.const import PROD_API_URL


def _init(api_key: Optional[str] = None):
    backend = os.environ.get("GANTRY_LOGS_LOCATION", PROD_API_URL)
    parsed_origin = urlparse(backend)
    if parsed_origin.scheme not in ("http", "https"):
        raise ValueError(
            "Invalid backend. http or https backends " + "supported. Got {}".format(backend)
        )

    api_key = os.environ.get("GANTRY_API_KEY") if api_key is None else api_key

    if not api_key:
        raise ValueError(
            """
            No API key provided. Please pass the api_key parameter or set the GANTRY_API_KEY
            environment variable.
            """
        )

    api_client = APIClient(backend, api_key)
    globals._Alerts = GantryAlerts(api_client)  # type: ignore[union-attr]


@_alerts_alias
def get_alerts(
    application_name: str,
    triggered: bool = False,
    triggered_from: Optional[str] = None,
    triggered_to: Optional[str] = None,
) -> List[Dict]:
    validate_init()
    return globals._Alerts.get_alerts(**locals())  # type: ignore[union-attr]


@_alerts_alias
def create_alert(
    application_name: str,
    alert_name: str,
    alert_checks: List[Dict],
    evaluation_window: str,
    evaluation_delay: str,
    tags: Optional[Dict[str, str]] = None,
) -> str:
    validate_init()
    return globals._Alerts.create_alert(**locals())  # type: ignore[union-attr, return-value]


@_alerts_alias
def update_alert(
    application_name: str,
    alert_id: Union[str, UUID],
    alert_name: str,
    alert_checks: List[Dict],
    evaluation_window: str,
    evaluation_delay: str,
    tags: Optional[Dict[str, str]] = None,
) -> str:
    validate_init()
    return globals._Alerts.update_alert(**locals())  # type: ignore[union-attr, return-value]


@_alerts_alias
def create_slack_notification(
    alert_id: str,
    notification_name: str,
    slack_webhook_url: str,
    notify_daily: bool,
    daily_notification_time: Optional[str] = None,
) -> str:
    validate_init()
    return globals._Alerts.create_slack_notification(  # type: ignore[union-attr, return-value]
        **locals()
    )


@_alerts_alias
def get_slack_notifications() -> List[Dict]:
    validate_init()
    return globals._Alerts.get_slack_notifications()  # type: ignore[union-attr]


@_alerts_alias
def delete_alert(alert_id: Union[str, UUID]) -> None:
    validate_init()
    return globals._Alerts.delete_alert(**locals())  # type: ignore[union-attr, return-value]


@_alerts_alias
def delete_slack_notification(
    alert_id: Union[str, UUID], slack_notification_id: Union[str, UUID]
) -> None:
    validate_init()
    return globals._Alerts.delete_slack_notification(  # type: ignore[union-attr, return-value]
        **locals()
    )
