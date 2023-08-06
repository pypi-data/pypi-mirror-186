import datetime
import os
import warnings
from typing import Dict, List, Optional, Union
from urllib.parse import urlparse

from gantry.api_client import APIClient
from gantry.const import PROD_API_URL
from gantry.query import globals
from gantry.query.client import GantryQuery
from gantry.query.core.dataframe import GantryDataFrame  # noqa
from gantry.query.globals import _query_alias, validate_init


def init(api_key: Optional[str] = None):
    """
    Initialize the Query functionality. Initialization should happen before any Query call.

    WARNING: this method will be deprecated soon, Use global `init` to intialize query
    functionality, as shown below.

    Example:

    .. code-block:: python

       import gantry.query as gquery

       gquery.init(api_key="foobar")

    Args:
        api_key (str): The API key. Users can fetch the API key from the dashboard.
    """
    warnings.warn(
        "This initialization method will be deprecated soon, use global gantry.init instead"
    )
    _init(api_key)


def _init(api_key: Optional[str] = None):
    backend = os.environ.get("GANTRY_LOGS_LOCATION", PROD_API_URL)
    parsed_origin = urlparse(backend)
    if parsed_origin.scheme not in ("http", "https"):
        raise ValueError(
            "Invalid backend. http or https backends " + "supported. Got {}".format(backend)
        )

    # Check environment if api_key is not provided
    api_key = os.environ.get("GANTRY_API_KEY") if api_key is None else api_key

    if not api_key:
        raise ValueError(
            """
            No API key provided. Please pass the api_key parameter or set the GANTRY_API_KEY
            environment variable.
            """
        )

    api_client = APIClient(backend, api_key)
    globals._Query = GantryQuery(api_client)  # type: ignore[union-attr]


@_query_alias
def list_applications() -> List[str]:
    validate_init()
    return globals._Query.list_applications()  # type: ignore[union-attr]


@_query_alias
def create_view(
    application: str,
    name: str,
    version: Optional[str] = None,
    tag_filters: Optional[Dict[str, str]] = None,
    data_filters: Optional[List[Dict]] = None,
    duration: Optional[datetime.timedelta] = None,
    start_time: Optional[datetime.datetime] = None,
    end_time: Optional[datetime.datetime] = None,
) -> None:
    validate_init()
    return globals._Query.create_view(**locals())  # type: ignore[union-attr,return-value]


@_query_alias
def list_application_versions(application: str) -> List[str]:
    validate_init()
    return globals._Query.list_application_versions(**locals())  # type: ignore[union-attr]


@_query_alias
def list_application_environments(application: str) -> List[str]:
    validate_init()
    return globals._Query.list_application_environments(**locals())  # type: ignore[union-attr]


@_query_alias
def query(
    application: str,
    start_time: Optional[Union[str, datetime.datetime]] = None,
    end_time: Optional[Union[str, datetime.datetime]] = None,
    version: Optional[Union[int, str]] = None,
    environment: Optional[str] = None,
    filters: Optional[List[Dict]] = None,
    view: Optional[str] = None,
    tags: Optional[dict] = None,
    batch_id: Optional[str] = None,
) -> GantryDataFrame:
    validate_init()
    return globals._Query.query(**locals())  # type: ignore[union-attr]


@_query_alias
def list_application_views(
    application: str,
    version: Optional[Union[str, int]] = None,
    environment: Optional[str] = None,
) -> List[str]:
    validate_init()
    return globals._Query.list_application_views(**locals())  # type: ignore[union-attr]


@_query_alias
def list_application_batches(
    application: str,
    version: Optional[Union[str, int]] = None,
) -> List[dict]:
    validate_init()
    return globals._Query.list_application_batches(**locals())  # type: ignore[union-attr]


@_query_alias
def print_application_info(application: str):
    validate_init()
    return globals._Query.print_application_info(**locals())  # type: ignore[union-attr]
