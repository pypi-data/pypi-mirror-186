import functools
import inspect
import logging
import os
from typing import Optional
from urllib.parse import urlparse

from gantry.api_client import APIClient
from gantry.const import PROD_API_URL
from gantry.dataset.client import GantryDatasetClient
from gantry.exceptions import ClientNotInitialized

_DATASET: Optional[GantryDatasetClient] = None
logger_obj = logging.getLogger(__name__)


def _dataset_client_alias(f):
    doc = "Alias for :meth:`gantry.dataset.client.GantryDatasetClient.{}`".format(f.__name__)
    orig_doc = inspect.getdoc(getattr(GantryDatasetClient, f.__name__))

    if orig_doc:
        doc += "\n\n{}".format(orig_doc)

    f.__doc__ = doc

    # This decorator also checks that the _CLIENT
    # has been initialized
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if _DATASET is None:
            raise ClientNotInitialized()

        return f(*args, **kwargs)

    return wrapper


def init(
    email: str,
    backend: str = PROD_API_URL,
    workspace: str = ".",
    api_key: Optional[str] = None,
    bucket_name: Optional[str] = None,
    aws_region: Optional[str] = None,
):
    """
    Initialize the dataset functionality. Initialization should happen before any dataset operation.

    Example:

    .. code-block:: python

       import gantry.dataset as gdataset

       gdataset.init(api_key="foobar", email="someuser@gmail.com")

    Args:
        email (str): User email
        backend (str): The backend URL. Defaults to the Gantry production URL.
        workspace(str): dataset workspace
        api_key (str): The API key. Users can fetch the API key from the dashboard.
        bucket_name (str): Provide bucket name if you want to use your own bucket. If not provided
                        we will use a gantry managed bucket.
        aws_region (str): Provide bucket region if you want to use your own bucket. If not provided
                        we will use a gantry managed bucket.
    """
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

    global _DATASET

    api_client = APIClient(backend, api_key)
    _DATASET = GantryDatasetClient(
        api_client=api_client,
        bucket_name=bucket_name,
        aws_region=aws_region,
        email=email,
        workspace=workspace,
    )  # type: ignore[union-attr]

    if not _DATASET.ping():
        logger_obj.warning(
            "Gantry services not reachable. Check provided URL "
            f"[{backend}] is pointing to the correct address"
        )
        return

    if not _DATASET.ready():
        logger_obj.warning("Gantry services won't receive traffic. Check if API Key is valid")


@_dataset_client_alias
def create_dataset(*args, **kwargs):
    return _DATASET.create_dataset(*args, **kwargs)


@_dataset_client_alias
def get_dataset(*args, **kwargs):
    return _DATASET.get_dataset(*args, **kwargs)


@_dataset_client_alias
def list_dataset_commits(*args, **kwargs):
    return _DATASET.list_dataset_commits(*args, **kwargs)


@_dataset_client_alias
def list_datasets(*args, **kwargs):
    return _DATASET.list_datasets(*args, **kwargs)


@_dataset_client_alias
def delete_dataset(*args, **kwargs):
    return _DATASET.delete_dataset(*args, **kwargs)
