import functools
import hashlib
import io
import json
import logging
import os
import shutil
import uuid
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import IO, Any, Callable, Dict, List, Optional, Union

import datasets
import jinja2
import pandas as pd
import yaml
from typeguard import typechecked

from gantry.api_client import APIClient
from gantry.dataset import constants
from gantry.exceptions import (
    DatasetCommitNotFoundError,
    DatasetDeletedException,
    DatasetHeadOutOfDateException,
    DatasetNotFoundError,
    GantryRequestException,
)
from gantry.utils import (
    download_file_from_url,
    get_files_checksum,
    list_all_files,
    parse_s3_path,
    upload_file_to_url,
)

logger = logging.getLogger(__name__)

BATCH_SIZE = 5


def _ensure_not_deleted(func: Callable) -> Callable:
    """
    Decorator to ensure we do not perform an operation on a deleted dataset, and instead warn the
    user that the dataset is deleted.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        resp = self._api_client.request(
            "GET",
            f"/api/v1/datasets/{self.dataset_name}",
            raise_for_status=True,
        )
        dataset_info = resp["data"]

        if dataset_info["disabled"]:
            raise DatasetDeletedException("This dataset has been deleted!")

        return func(self, *args, **kwargs)

    return wrapper


def _ensure_dataset_exists_locally(func: Callable) -> Callable:
    """
    Decorator to ensure dataset exists locally, if not will warn the user to download the dataset.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not Path(self._get_file_path(constants.DATASET_MANIFEST_FILE)).exists():
            raise DatasetNotFoundError(
                f"Can't find dataset {self.dataset_name} locally, please run pull()"
                f"to download the dataset into your local workspace."
            )

        return func(self, *args, **kwargs)

    return wrapper


def _warn_when_local_changes(func: Callable) -> Callable:
    """
    Decorator to ensure there are no local changes in the dataset. If there are, will return None
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        localdiff = self.get_diff()
        if (
            localdiff[constants.DELETED_FILES]
            or localdiff[constants.MODIFIED_FILES]
            or localdiff[constants.NEW_FILES]
        ) and not kwargs.get("forced", False):
            logger.warning(
                "Local changes detected! Please run stash() to stash your local changes, "
                "or run this function again with forced=True"
            )
            return None

        return func(self, *args, **kwargs)

    return wrapper


@dataclass
class DatasetFileInfo:
    file_name: str
    url: str
    version_id: Optional[str] = None
    sha256: Optional[str] = None

    def to_jsonl(self):
        if not self.file_name or not self.url or not self.version_id or not self.sha256:
            raise ValueError(
                f"Failed to create file info jsonl: {json.dumps(asdict(self))}. \
                    Incomplete dataset file info line! "
            )

        return f"{json.dumps(asdict(self))}\n"


class GantryDataset:
    def __init__(
        self,
        api_client: APIClient,
        dataset_name: str,
        user_email: str,
        dataset_id: uuid.UUID,
        bucket_name: str,
        aws_region: str,
        dataset_s3_prefix: str,
        workspace: str,
    ):
        self.dataset_name = dataset_name
        self.user_email = user_email
        self.workspace = workspace
        self._api_client = api_client
        self._dataset_id = dataset_id
        self._bucket_name = bucket_name
        self._dataset_s3_prefix = dataset_s3_prefix
        self._aws_region = aws_region

    def list_commits(self) -> List[Dict[str, Any]]:
        """
        Get dataset commits history

        Returns:
            List[Dict[str, Any]]: dataset commits sorted from latest to earliest.
        """
        response = self._api_client.request(
            "GET", f"/api/v1/datasets/{self._dataset_id}/commits", raise_for_status=True
        )
        return [self._prune_commit_info(commit_info) for commit_info in response["data"]]

    @_ensure_dataset_exists_locally
    def get_diff(self) -> Dict[str, List[str]]:
        """
        Get local changes which hasn't been committed
        Return:
            {
                "new_files": List[str],
                "modified_files": List[str],
                "deleted_files": List[str],
            }
        """

        diff = self._get_diff()
        return {
            constants.NEW_FILES: [f for f, _ in diff[constants.NEW_FILES]],
            constants.MODIFIED_FILES: [f for f, _ in diff[constants.MODIFIED_FILES]],
            constants.DELETED_FILES: [f for f, _ in diff[constants.DELETED_FILES]],
        }

    @typechecked
    @_ensure_dataset_exists_locally
    @_ensure_not_deleted
    def commit(self, message: str) -> Dict[str, Any]:
        """
        This method will compute the difference between the current commit and the local directory,
        upload new files and modified files to dataset repo. After that we will update
        .gantry_artifact.jsonl with the latest dataset info and create a new commit. HEAD file
        will also be updated using the latest commit information.

        Args:
            message (str): commit message, can't be empty
        Returns:
            Commit info
        """
        commit_id = uuid.uuid4()
        diff = self._get_diff_for_commit(commit_id)

        if (
            not diff[constants.NEW_FILES]
            and not diff[constants.MODIFIED_FILES]
            and not diff[constants.DELETED_FILES]
        ):
            logger.warning("No local changes to commit!")
            return self._get_current_commit()

        # Check that HEAD is up to date
        resp = self._api_client.request(
            "GET", f"/api/v1/datasets/{self._dataset_id}/commits", raise_for_status=True
        )
        latest_commit_id = resp["data"][0]["id"]

        with open(self._get_file_path(constants.DATASET_HEAD_FILE), "r") as f:
            current_commit = json.load(f)

            if current_commit["id"] != latest_commit_id:
                raise DatasetHeadOutOfDateException

        diff[constants.NEW_FILES] = self._upload_files(diff[constants.NEW_FILES])
        diff[constants.MODIFIED_FILES] = self._upload_files(diff[constants.MODIFIED_FILES])

        self._backup_file(constants.DATASET_MANIFEST_FILE)
        self._update_manifest_file(diff)

        result = self._upload_files(
            [
                DatasetFileInfo(
                    file_name=constants.DATASET_MANIFEST_FILE,
                    url=self._get_s3_url(constants.DATASET_MANIFEST_FILE),
                )
            ]
        )
        version_id = result[0].version_id
        try:
            resp = self._api_client.request(
                "POST",
                f"/api/v1/datasets/{self._dataset_id}/commits",
                json={
                    "message": message,
                    "metadata_s3_file_version": version_id,
                    "parent_commit_id": self._get_current_commit()["id"],
                    "commit_id": commit_id,
                    "email": self.user_email,
                },
                raise_for_status=True,
            )
            os.remove(
                self._get_file_path(f"{constants.DATASET_MANIFEST_FILE}{constants.BACKUP_SUFFIX}")
            )
        except GantryRequestException as e:
            self._recover_file(constants.DATASET_MANIFEST_FILE)
            if (
                e.status_code == 400
                and 'Details: {"error":"Parent commit out of date!","response":"error"}'
                in e.args[0]
            ):
                raise DatasetHeadOutOfDateException
            raise e

        commit_info = resp["data"]
        self._update_head(commit_info)

        return self._prune_commit_info(commit_info)

    @typechecked
    @_ensure_not_deleted
    def add_file(
        self,
        file: IO,
        filename: Optional[str] = None,
        commit_message: Optional[str] = None,
        parent_commit_id: Optional[Union[uuid.UUID, str]] = None,
    ) -> Dict[str, Any]:
        """
        This method will upload a file (such as a file opened with ``open()``) to the dataset in a
        new commit. Does not rely on the user having the dataset synced, nor does it cause the
        dataset to sync after the upload.

        Args:
            file (IO): the file to be uploaded
            filename (str, Optional): the name of the file to be uploaded. Defaults to the local
                filename of the file
            commit_message (str, Optional): the commit message that will be associated with the
                upload of the file. Defaults to a generic message if not set
        Returns:
            Commit info
        """
        # TODO: require specification of parent commit
        if filename:
            name = filename
        else:
            name = os.path.basename(file.name)

        return self._add_single_file(file, name, commit_message, parent_commit_id)

    @typechecked
    @_ensure_not_deleted
    def add_tabular_file(
        self,
        file: IO,
        filename: Optional[str] = None,
        commit_message: Optional[str] = None,
        parent_commit_id: Optional[Union[uuid.UUID, str]] = None,
    ) -> Dict[str, Any]:
        """
        This method will upload a csv file (such as a csv file opened with ``open()``) to the
        tabular_manifests of the dataset in a new commit. Does not rely on the user having the
        dataset synced, nor does it cause the dataset to sync after the upload.

        Args:
            file (IO): the csv file to be uploaded
            filename (str, Optional): the name of the file to be uploaded. Defaults to the local
                filename of the file. Name must end with '.csv'
            commit_message (str, Optional): the commit message that will be associated with the
                upload of the file. Defaults to a generic message if not set
        Returns:
            Commit info
        """
        # TODO: require specification of parent commit
        if filename:
            name = filename
        else:
            name = os.path.basename(file.name)

        if name[-4:] != ".csv":
            raise ValueError(f"filename must end with '.csv'! Got filename: {name}")

        return self._add_single_file(file, name, commit_message, parent_commit_id)

    @typechecked
    @_ensure_not_deleted
    def add_dataframe(
        self,
        dataframe: pd.DataFrame,
        csvname: Optional[str] = None,
        commit_message: Optional[str] = None,
        parent_commit_id: Optional[Union[uuid.UUID, str]] = None,
    ) -> Dict[str, Any]:
        """
        This method will upload a pandas DataFrame as a new commit in the form of a csv. Does not
        rely on the user having the dataset synced, nor does it cause the dataset to sync after the
        upload.

        Args:
            dataframe (pd.DataFrame): the dataframe to be uploaded
            csvname (str, Optional): the name for the csv that will be uploaded. Defaults to
                dataframe-[md5 hash].csv
            commit_message (str, Optional): the commit message that will be associated with the
                upload of the file. Defaults to a generic message if not set
        Returns:
            Commit info
        """
        # TODO: require specification of parent commit
        if csvname:
            if csvname[-4:] == ".csv":
                name = csvname
            else:
                name = f"{csvname}.csv"
        else:
            hash = hashlib.md5(pd.util.hash_pandas_object(dataframe).values).hexdigest()
            name = f"dataframe-{hash}.csv"

        file = io.StringIO()
        dataframe.to_csv(file)
        file.seek(0)

        return self._add_single_file(file, name, commit_message, parent_commit_id)

    @typechecked
    @_ensure_not_deleted
    @_warn_when_local_changes
    def rollback(
        self, commit_id: Union[str, uuid.UUID], forced: bool = False
    ) -> Optional[Dict[str, Any]]:
        """
        Roll back the dataset to a previous version based on commit id, then pull the newly created
        commit to the local folder. If there are local changes, will instead do nothing and return
        None

        Args:
            commit_id (str): target commit id
            forced (bool): whether to ignore the presence of any local changes
        Returns:
            commit info (optional): commit info if rollback was successsful. None if there were
                local changes
        """
        target_commit = self._get_commit(commit_id)

        resp = self._api_client.request(
            "POST",
            f"/api/v1/datasets/{self._dataset_id}/commits",
            json={
                "message": f"Rollback dataset to commit: {target_commit['id']}",
                "metadata_s3_file_version": target_commit["metadata_s3_file_version"],
                "parent_commit_id": self._get_current_commit()["id"],
                "email": self.user_email,
            },
            raise_for_status=True,
        )

        commit_info = resp["data"]
        self.pull(commit_info["id"], forced=True)

        return self._prune_commit_info(commit_info)

    @typechecked
    @_ensure_not_deleted
    @_warn_when_local_changes
    def pull(
        self, commit_id: Optional[Union[str, uuid.UUID]] = None, forced: bool = False
    ) -> Optional[Dict[str, Any]]:
        """
        Sync local dataset folder based on a commit id. If commit_id was not provided, will sync
        based on the latest commit. Will not allow a pull if there are local changes, to avoid
        accidentally losing changes

        Args:
            commit_id (str, optional): target commit id. Defaults to None.
            forced (bool): whether to ignore the presence of any local changes
        Returns:
            commit info (optional): commit info if pull was successful. None if there were local
                changes
        """

        target_commit = (
            self._get_commit(commit_id=commit_id) if commit_id else self._get_latest_commit()
        )

        version_id = target_commit[constants.METADATA_S3_FILE_VERSION]

        self._download_files(
            [
                DatasetFileInfo(
                    file_name=constants.DATASET_MANIFEST_FILE,
                    url=self._get_s3_url(constants.DATASET_MANIFEST_FILE),
                    version_id=version_id,
                )
            ]
        )

        diff = self._get_diff_for_pull()
        self._download_files(diff[constants.MODIFIED_FILES])  # Overwrite modified files
        self._download_files(diff[constants.DELETED_FILES])  # redownload deleted files

        # delete new added files
        for f in diff[constants.NEW_FILES]:
            os.remove(self._get_file_path(f.file_name))

        self._update_head(target_commit)
        if not os.path.exists(self._get_file_path(constants.STASH_FOLDER)):
            os.mkdir(self._get_file_path(constants.STASH_FOLDER))

        return self._prune_commit_info(target_commit)

    def stash(self) -> None:
        """
        Stashes local changes
        """
        # deletes existing stash
        if os.path.exists(self._get_file_path(constants.DATASET_STASH_FILE)):
            with open(self._get_file_path(constants.DATASET_STASH_FILE)) as stashfile:
                old_stash = json.load(stashfile)
            for file in old_stash[constants.MODIFIED_FILES] + old_stash[constants.NEW_FILES]:
                os.remove(self._get_file_path(f"{constants.STASH_FOLDER}/{file}"))

        # creates new stash
        local_diff = self.get_diff()
        with open(self._get_file_path(constants.DATASET_STASH_FILE), "w+") as stashfile:
            json.dump(local_diff, stashfile)

        # stash files
        for file in local_diff[constants.MODIFIED_FILES]:
            self._stash_file(file)
        for file in local_diff[constants.NEW_FILES]:
            self._stash_file(file)

        # re-sync to current commit
        diff = self._get_diff_for_pull()
        logger.warning(diff)
        self._download_files(diff[constants.MODIFIED_FILES])  # overwrite modified files
        self._download_files(diff[constants.DELETED_FILES])  # redownload deleted files

        # delete new added files
        for file in diff[constants.NEW_FILES]:
            os.remove(self._get_file_path(file.file_name))

    def restore(self) -> None:
        """
        Restores changes from stash
        """
        if not os.path.exists(self._get_file_path(constants.DATASET_STASH_FILE)):
            logger.warning("No stashed files were found!")
            return

        diff = {}
        with open(self._get_file_path(constants.DATASET_STASH_FILE)) as stashfile:
            diff = json.load(stashfile)
        os.remove(self._get_file_path(constants.DATASET_STASH_FILE))
        if not diff:
            return

        for file in diff[constants.MODIFIED_FILES]:
            self._restore_stash_file(file)
        for file in diff[constants.NEW_FILES]:
            self._restore_stash_file(file)
        for file in diff[constants.DELETED_FILES]:
            os.remove(self._get_file_path(file))

    def delete(self):
        """
        Deletes the dataset (currently it is just marked as deleted)
        """
        self._api_client.request(
            "DELETE",
            f"/api/v1/datasets/{self._dataset_id}",
            raise_for_status=True,
        )
        logger.info(f"Dataset {self.dataset_name} has been deleted")
        return

    @typechecked
    def _get_commit(self, commit_id: Union[str, uuid.UUID]) -> Dict[str, Any]:
        """
        Get commit details

        Args:
            commit_id (str): commit id
        Returns:
            Commit information
        """
        try:
            resp = self._api_client.request(
                "GET",
                f"/api/v1/datasets/{self._dataset_id}/commits/{commit_id}",
                raise_for_status=True,
            )
        except GantryRequestException as e:
            if e.status_code == 404:
                raise DatasetCommitNotFoundError(
                    f"Could not find dataset commit with id {commit_id}"
                ) from e
            raise
        return resp["data"]

    def _get_latest_commit(self) -> Dict[str, Any]:
        """
        Get latest commit details

        Returns:
            Commit information
        """
        resp = self._api_client.request(
            "GET", f"/api/v1/datasets/{self._dataset_id}/commits", raise_for_status=True
        )
        return resp["data"][0]  # return latest commit

    def _update_manifest_file(self, diff: Dict[str, List[DatasetFileInfo]]):
        new_files = {f.file_name: f for f in diff[constants.NEW_FILES]}
        modified_files = {f.file_name: f for f in diff[constants.MODIFIED_FILES]}
        deleted_files = {f.file_name: f for f in diff[constants.DELETED_FILES]}

        with open(
            self._get_file_path(f"{constants.DATASET_MANIFEST_FILE}{constants.NEW_SUFFIX}"), "w"
        ) as new_gantry_manifest:
            with open(
                self._get_file_path(constants.DATASET_MANIFEST_FILE), "r"
            ) as cur_gantry_manifest:
                for line in cur_gantry_manifest:
                    cur_file_info = json.loads(line)
                    cur_file_name = cur_file_info[constants.FILE_NAME]

                    if cur_file_name in modified_files:  # update modified files
                        new_gantry_manifest.write(modified_files[cur_file_name].to_jsonl())
                    elif cur_file_name in deleted_files:  # remove deleted files
                        continue
                    else:  # keep unchanged files
                        new_gantry_manifest.write(line)

            for _, file_info in new_files.items():
                new_gantry_manifest.write(file_info.to_jsonl())  # add new added files

        os.replace(
            self._get_file_path(f"{constants.DATASET_MANIFEST_FILE}{constants.NEW_SUFFIX}"),
            self._get_file_path(constants.DATASET_MANIFEST_FILE),
        )

    def _get_diff_for_commit(self, commit_id: uuid.UUID):
        repo_diff = self._get_diff()
        commit_diff = {}

        # generate new url for new files
        commit_diff[constants.NEW_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url=self._get_s3_url(file_name, commit_id),
                sha256=checksum,
            )
            for file_name, checksum in repo_diff[constants.NEW_FILES]
        ]
        # generate new url for modified files
        commit_diff[constants.MODIFIED_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url=self._get_s3_url(file_name, commit_id),
                sha256=checksum,
            )
            for file_name, checksum in repo_diff[constants.MODIFIED_FILES]
        ]
        # don't need url for deleted files
        commit_diff[constants.DELETED_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url="",
                sha256=checksum,
            )
            for file_name, checksum in repo_diff[constants.DELETED_FILES]
        ]

        return commit_diff

    def _get_diff_for_pull(self):
        repo_diff = self._get_diff()
        sync_diff = {}

        commit_snapshot = {}
        with open(self._get_file_path(constants.DATASET_MANIFEST_FILE)) as cur_gantry_manifest:
            for line in cur_gantry_manifest:
                file_info = json.loads(line)
                commit_snapshot[file_info[constants.FILE_NAME]] = file_info

        # don't need url for new files and use checksum for empty string
        sync_diff[constants.NEW_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url="",
                sha256=constants.EMPTY_STR_SHA256,
            )
            for file_name, _ in repo_diff[constants.NEW_FILES]
        ]
        # retrieve url for modified files
        sync_diff[constants.MODIFIED_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url=commit_snapshot[file_name][constants.URL],
                sha256=commit_snapshot[file_name][constants.SHA256],
                version_id=commit_snapshot[file_name][constants.VERSION_ID],
            )
            for file_name, _ in repo_diff[constants.MODIFIED_FILES]
        ]
        # retrieve url for deleted files
        sync_diff[constants.DELETED_FILES] = [
            DatasetFileInfo(
                file_name=file_name,
                url=commit_snapshot[file_name][constants.URL],
                sha256=commit_snapshot[file_name][constants.SHA256],
                version_id=commit_snapshot[file_name][constants.VERSION_ID],
            )
            for file_name, _ in repo_diff[constants.DELETED_FILES]
        ]

        return sync_diff

    def _get_diff(self):
        """
        Generate local diff.

        Args:
            return_local_info (bool): if true return local file info for modified files else
            return file info in dataset repo

        Returns:
            {
                "new_files": List[Tuple(str,str)],
                "modified_files": List[Tuple(str,str)],
                "deleted_files": List[Tuple(str,str)],
            }
        """
        repo_diff = defaultdict(list)

        commit_snapshot = {}
        with open(self._get_file_path(constants.DATASET_MANIFEST_FILE)) as cur_gantry_manifest:
            for line in cur_gantry_manifest:
                file_info = json.loads(line)
                commit_snapshot[file_info[constants.FILE_NAME]] = file_info

        local_files = get_files_checksum(Path(self.workspace) / self.dataset_name)

        # TODO:// Simplify the following logic to make it easier to maintain
        for file_name, checksum in local_files.items():
            if file_name.startswith(constants.GANTRY_FOLDER):  # skip .dataset_metadata folder
                continue
            elif file_name.startswith(constants.STASH_FOLDER):  # skip stash folder
                continue
            elif file_name not in commit_snapshot:  # new added file
                repo_diff[constants.NEW_FILES].append((file_name, checksum))
            elif checksum != commit_snapshot[file_name].get(
                constants.SHA256
            ):  # if file_name in current_snapshot --> check if it has been modified
                repo_diff[constants.MODIFIED_FILES].append((file_name, checksum))

        for file_name in commit_snapshot:
            if file_name not in local_files:
                repo_diff[constants.DELETED_FILES].append((file_name, constants.EMPTY_STR_SHA256))

        return repo_diff

    def _add_single_file(
        self,
        file: IO,
        filename: str,
        commit_msg: Optional[str],
        parent_commit_id: Optional[Union[uuid.UUID, str]],
    ):
        if parent_commit_id is not None:
            if str(parent_commit_id) != self._get_latest_commit()["id"]:
                raise DatasetHeadOutOfDateException()

        if commit_msg is None:
            commit_msg = f"Uploaded {filename} to dataset"

        data = {
            "email": self.user_email,
            "commit_msg": commit_msg,
        }
        files = {
            "file": (filename, file),
        }

        resp = self._api_client.request(
            "POST",
            f"/api/v1/datasets/{self._dataset_id}/file",
            files=files,
            data=data,
            raise_for_status=True,
        )

        commit_info = resp["data"]
        return self._prune_commit_info(commit_info)

    def _get_file_path(self, file_name: str) -> str:
        return os.path.join(self.workspace, self.dataset_name, file_name)

    def _get_s3_url(self, file_name: str, commit_id: Optional[uuid.UUID] = None) -> str:
        if commit_id:
            return (
                f"s3://{self._bucket_name}/{self._dataset_s3_prefix}/"
                f"{self.dataset_name}/{commit_id}/{file_name}"
            )
        else:
            return (
                f"s3://{self._bucket_name}/{self._dataset_s3_prefix}/"
                f"{self.dataset_name}/{file_name}"
            )

    def _get_obj_key(self, s3_url: str) -> str:
        _, obj_key = parse_s3_path(s3_url)
        return obj_key

    def _update_head(self, commit_info: Dict[str, Any]):
        with open(self._get_file_path(constants.DATASET_HEAD_FILE), "w") as f:
            json.dump(commit_info, f)

    def _get_current_commit(self) -> Dict[str, Any]:
        with open(self._get_file_path(constants.DATASET_HEAD_FILE), "r") as f:
            return json.load(f)

    def _backup_file(self, file_path: str):
        # make a copy of the original file
        shutil.copyfile(
            self._get_file_path(file_path),
            self._get_file_path(f"{file_path}{constants.BACKUP_SUFFIX}"),
        )

    def _recover_file(self, file_path: str):
        # recover the file from a backup copy
        os.replace(
            self._get_file_path(f"{file_path}{constants.BACKUP_SUFFIX}"),
            self._get_file_path(file_path),
        )

    def _stash_file(self, file_path: str):
        # move file to stash folder
        os.replace(
            self._get_file_path(file_path),
            self._get_file_path(f"{constants.STASH_FOLDER}/{file_path}"),
        )

    def _restore_stash_file(self, file_path: str):
        # recover file from stash folder
        os.replace(
            self._get_file_path(f"{constants.STASH_FOLDER}/{file_path}"),
            self._get_file_path(file_path),
        )

    def _download_files(self, file_list: List[DatasetFileInfo]):
        """
        download file to the specific path

        Args:
            file_list (List[DatasetFileInfo]):
        """
        for i in range(0, len(file_list), BATCH_SIZE):
            batch = file_list[i : i + BATCH_SIZE]
            resp = self._api_client.request(
                "POST",
                f"/api/v1/datasets/{self._dataset_id}/presign/getobject",
                json={
                    "obj_infos": [
                        {
                            constants.OBJ_KEY: self._get_obj_key(item.url),
                            constants.VERSION_ID: item.version_id,
                        }
                        for item in batch
                    ],
                },
                raise_for_status=True,
            )
            presigned_urls = resp["data"]

            for item in batch:
                local_path = self._get_file_path(item.file_name)
                presigned_url = presigned_urls[self._get_obj_key(item.url)]
                download_file_from_url(presigned_url=presigned_url, local_path=Path(local_path))

    def _upload_files(self, file_list: List[DatasetFileInfo]):
        """
        download file to the specific path

        Args:
            file_list (List[DatasetFileInfo]):
        Returns:
            List[DatasetFileInfo]
        """
        for i in range(0, len(file_list), BATCH_SIZE):
            batch = file_list[i : i + BATCH_SIZE]
            resp = self._api_client.request(
                "POST",
                f"/api/v1/datasets/{self._dataset_id}/presign/putobject",
                json={"obj_keys": [self._get_obj_key(f.url) for f in batch]},
                raise_for_status=True,
            )
            presigned_urls = resp["data"]

            for item in batch:
                local_path = self._get_file_path(item.file_name)
                presigned_url = presigned_urls[self._get_obj_key(item.url)]
                version_id = upload_file_to_url(
                    presigned_url=presigned_url, local_path=Path(local_path)
                )
                item.version_id = version_id
                logger.info(f"successfully upload: {item.file_name}")

        return file_list

    def _extract_feature_type(self) -> Dict[str, Any]:
        """
        Read feature type from dataset_config and convert them to huggingface feature type
        Returns:
            A key value pair of Dict where key is the column name and value is huggingface
            feature type
        """
        columns = dict()
        config = yaml.safe_load(
            (Path(self.workspace) / self.dataset_name / constants.DATASET_CONFIG_FILE).open(
                mode="r"
            )
        )

        if constants.DATASET_FEATURES_KEY in config:
            for feature_name, feature_dtype in config[constants.DATASET_FEATURES_KEY].items():
                columns[feature_name] = constants.GANTRY_2_HF_DTYPE[feature_dtype]

        if constants.DATASET_FEEDBACK_KEY in config:
            for feature_name, feature_dtype in config[constants.DATASET_FEEDBACK_KEY].items():
                columns[feature_name] = constants.GANTRY_2_HF_DTYPE[feature_dtype]

        return columns

    def get_huggingface_dataset(self):
        """
        Create a huggingface dataset based on the local dataset files

        This method will create a huggingface load script based on the dataset config and
        then load the dataset into huggingface pyarrow dataset.
        """

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")
            )
        )

        template = env.get_template("load_script_template.py.jinja")

        training_files = [
            str(p)
            for p in list_all_files(
                Path(self.workspace) / self.dataset_name / constants.TABULAR_MANIFESTS
            )
        ]

        content = template.render(
            training_file_list=training_files,
            dataset_version="1.0.0",  # Format should be x.y.z with {{x,y,z}} being digits
            dataset_name=self.dataset_name,
            features=self._extract_feature_type(),
        )

        hf_loading_script = (
            Path(self.workspace)
            / self.dataset_name
            / constants.HF_FOLDER
            / f"{self.dataset_name}.py"
        )
        os.makedirs(hf_loading_script.parent, exist_ok=True)
        with hf_loading_script.open("w") as f:
            f.write(content)

        return datasets.load_dataset(str(hf_loading_script))

    def _prune_commit_info(self, commit_info):
        return {
            "commit_id": commit_info["id"],
            "dataset": self.dataset_name,
            "message": commit_info["message"],
            # TODO:// uncomment the following line once we add sdk support for user version
            # "user_version": commit_info["user_version"],
            "created_at": commit_info["created_at"],
            "created_by": commit_info["created_by"],
            "is_latest_commit": commit_info["is_latest_commit"],
        }
