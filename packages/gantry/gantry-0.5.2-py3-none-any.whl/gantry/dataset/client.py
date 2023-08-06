import logging
import pathlib
from typing import Any, Dict, List, Optional

from typeguard import typechecked

from gantry.api_client import APIClient
from gantry.dataset.gantry_dataset import GantryDataset
from gantry.exceptions import DatasetNotFoundError, GantryRequestException

logger = logging.getLogger(__name__)


class GantryDatasetClient:
    def __init__(
        self,
        api_client: APIClient,
        email: str,
        bucket_name: Optional[str] = None,
        aws_region: Optional[str] = None,
        workspace: str = str(pathlib.Path().absolute()),
    ):
        self._api_client = api_client
        self.email = email
        self.bucket_name = bucket_name
        self.aws_region = aws_region
        self.workspace = workspace

    @typechecked
    def create_dataset(self, name: str, model_name: Optional[str] = None) -> GantryDataset:
        """
        Create dataset

        Args:
            name (str): dataset name
            model_name (Optional[str], optional): gantry application name which will be used to set
                dataset schema if provided.

        Returns:
            GantryDataset
        """
        data = {
            "name": name,
            "email": self.email,
        }

        if model_name:
            res = self._api_client.request(
                "GET", f"/api/v1/applications/{model_name}/schemas", raise_for_status=True
            )
            data["model_id"] = res["data"]["id"]

        if self.bucket_name and self.aws_region:
            data.update(
                {
                    "bucket_name": self.bucket_name,
                    "aws_region": self.aws_region,
                }
            )
        elif not (not self.bucket_name and not self.aws_region):
            raise NotImplementedError(
                "Both bucket name and region need to be set if you want\
                 to use your own bucket."
            )

        res = self._api_client.request("POST", "/api/v1/datasets", json=data, raise_for_status=True)

        return GantryDataset(
            api_client=self._api_client,
            user_email=self.email,
            dataset_name=res["data"]["name"],
            dataset_id=res["data"]["id"],
            bucket_name=res["data"]["bucket_name"],
            aws_region=res["data"]["aws_region"],
            dataset_s3_prefix=f"{res['data']['organization_id']}/{res['data']['s3_prefix']}",
            workspace=self.workspace,
        )

    @typechecked
    def get_dataset(self, name: str) -> GantryDataset:
        """
        Get dataset object

        Args:
            name (str): dataset name

        Returns:
            GantryDataset
        """
        try:
            res = self._api_client.request("GET", f"/api/v1/datasets/{name}", raise_for_status=True)
        except GantryRequestException as e:
            if e.status_code == 404:
                raise DatasetNotFoundError(f'Could not find dataset with name "{name}"') from e
            raise

        if res["data"]["disabled"]:
            logger.warning("This dataset is marked as deleted")

        return GantryDataset(
            api_client=self._api_client,
            user_email=self.email,
            dataset_name=res["data"]["name"],
            dataset_id=res["data"]["id"],
            bucket_name=res["data"]["bucket_name"],
            aws_region=res["data"]["aws_region"],
            dataset_s3_prefix=f"{res['data']['organization_id']}/{res['data']['s3_prefix']}",
            workspace=self.workspace,
        )

    @typechecked
    def list_dataset_commits(self, name: str) -> List[Dict[str, Any]]:
        """
        Show dataset commit history

        Args:
            name (str): dataset name

        Returns:
            list of commit info
        """
        dataset = self.get_dataset(name)

        return dataset.list_commits()

    @typechecked
    def list_datasets(self, include_deleted: bool = False) -> List[Dict[str, Any]]:
        """
        List datasets

        Args:
            include_deleted (bool): whether to return deleted datasets, defaults to false

        Returns:
            List of dataset information
        """
        res = self._api_client.request(
            "GET",
            "/api/v1/datasets",
            raise_for_status=True,
            params={"include_deleted": include_deleted},
        )

        return [self._prune_dataset_info(dataset_info) for dataset_info in res["data"]]

    @typechecked
    def delete_dataset(self, name: str):
        """
        Delete dataset

        Args:
            name (str): dataset name

        Returns:
            none
        """
        dataset = self.get_dataset(name)

        return dataset.delete()

    def ping(self) -> bool:
        """
        Pings the API client server to check if it is alive.
        Returns True if alive, False if there is an error during ping process.
        """
        try:
            # Cannot use /healthz/* endpoints as those will be answered by nginx
            # need to use /.
            # See https://linear.app/gantry/issue/ENG-2978/revisit-ping-in-sdk
            self._api_client.request("GET", "/api/ping", raise_for_status=True)
            return True
        except Exception as e:
            logger.error(f"Error during ping: {e}")
            return False

    def ready(self) -> bool:
        """
        Checks whether the API is ready to receive traffic with the provided API Key.
        """
        try:
            self._api_client.request("GET", "/api/v1/auth-ping", raise_for_status=True)
            return True
        except Exception as e:
            logger.error(f"Error during api key check: {e}")
            return False

    @staticmethod
    def _prune_dataset_info(dataset_info):
        return {
            "name": dataset_info["name"],
            "dataset_id": dataset_info["id"],
            "created_at": dataset_info["created_at"],
        }
