from typing import Optional

from gantry.alerts.main import _init as alerts_init
from gantry.logger.main import LOGGING_LEVEL_T
from gantry.logger.main import _init as logger_init
from gantry.logger.main import (
    get_client,
    log_file,
    log_record,
    log_records,
    ping,
    ready,
    setup_logger,
)
from gantry.logger.utils import JoinKey
from gantry.query.main import _init as query_init
from gantry.utils import compute_feedback_id

__all__ = [
    "init",
    "log_record",
    "log_records",
    "log_file",
    "ping",
    "ready",
    "get_client",
    "setup_logger",
    "compute_feedback_id",
    "JoinKey",
]


def init(
    api_key: Optional[str] = None,
    logging_level: Optional[LOGGING_LEVEL_T] = None,
    environment: Optional[str] = None,
    send_in_background: Optional[bool] = None,
):
    """
    Initialize gantry services. Initialization should happen before any interaction with Gantry
    (whether is ingesting data or performing queries).

    After initialization, the SDK logging module, query module and alerts module
    will be enabled.

    Example:

    .. code-block:: python

       import gantry
       gantry.init(api_key="foobar")


    Args:
        api_key (optional, str): The Gantry API Key. You can also set this parameter by setting
            the env variable GANTRY_API_KEY.
        logging_level (optional, str): Set logging level for Gantry system logging.
            You can also set this parameter by setting the env variable GANTRY_LOGGING_LEVEL.
            Options are: DEBUG, INFO, WARNING, CRITICAL or ERROR.
            If not specified, it defaults to INFO.
        environment (optional, str): Set the value for the environment label attached
            to data instrumented. You can also set this parameter by setting the env
            variable GANTRY_ENVIRONMENT. If not provided, it defaults to "dev".
        send_in_background (optional, bool): set whether Gantry logging methods should
            run synchronously or not. You can also set this value by setting
            the env variable GANTRY_SEND_IN_BACKGROUND.
            If not provided, it defaults to True unless running in an AWS lambda.

    """
    logger_init(api_key, logging_level, environment, send_in_background)
    query_init(api_key)
    alerts_init(api_key)
