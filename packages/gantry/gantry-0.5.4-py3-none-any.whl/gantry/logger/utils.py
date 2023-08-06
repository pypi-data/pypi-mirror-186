import concurrent
import functools
import hashlib
import json
import logging
import os
import subprocess
import urllib
from itertools import islice
from typing import Any, Dict, Iterable, List, Union

import numpy as np
import pandas as pd
import requests
from typeguard import typechecked

from gantry.exceptions import GantryBatchCreationException, GantryLoggingException
from gantry.logger.stores import APILogStore, BaseLogStore
from gantry.serializers import EventEncoder

logger = logging.getLogger(__name__)


def _log_exception(func):
    """Handles all exceptions thrown by func, and logs them to prevent the
    func call from crashing.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except GantryLoggingException as le:
            # this is caused by a user error
            # log the error without the stacktrace
            logger.error("Error logging data to Gantry: %s", le)
        except GantryBatchCreationException as e:
            # Blocking exception for batch creation failure
            raise e
        except Exception as e:
            # make sure our logging errors don't cause exceptions in main program
            logger.exception("Internal exception in Gantry client: %s", e)

    return wrapper


def _is_empty(data: Union[List[Any], pd.DataFrame, Any] = None) -> bool:
    """
    Check whether input data is empty or not
    Returns True if data is None or empty, False if data size >= 1
    """
    if isinstance(data, pd.DataFrame):
        return data.empty
    elif isinstance(data, np.ndarray):
        return data.size == 0
    return True if not data else False


def _is_not_empty(data: Union[List[Any], pd.DataFrame, Any] = None) -> bool:
    return not _is_empty(data)


def _batch_fail_msg(batch_id):
    if batch_id:
        logger.info(f"Batch with id: {batch_id} FAILED")


def _check_sample_rate(sample_rate):
    assert sample_rate <= 1 and sample_rate >= 0


def _build_success_msg(host: str, application: str) -> str:
    return "Track your batch at {}applications/{}/jobs".format(
        host if host.endswith("/") else f"{host}/", urllib.parse.quote(application)
    )


def _batch_success_msg(batch_id, application, log_store: Union[APILogStore, BaseLogStore]):
    if batch_id:
        if isinstance(log_store, APILogStore):
            host = log_store._api_client._host
        else:
            host = "[YOUR_GANTRY_DASHBOARD]"

        logger.info(_build_success_msg(host, application))
        logger.info("Look for batch id: {}".format(batch_id))


def get_file_linecount(filepath):
    """
    'wc -l' will count the number of \n characters, but if the last line is missing the
    \n then it will miss it. So we add one if the last line is missing \n but is not empty.

    This needs to be a high performance function that works even for larger files.
    - https://stackoverflow.com/questions/845058
    - https://stackoverflow.com/questions/46258499
    """
    with open(filepath, "rb") as f:
        try:  # catch OSError in case of a one line file
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()

    line_count = int(subprocess.check_output(["wc", "-l", filepath]).split()[0])
    if len(last_line) > 0 and not last_line.endswith("\n"):
        line_count += 1
    return line_count


def _build_batch_iterator(iterable, batch_size):
    iterator = iter(iterable)
    batch = islice(iterator, batch_size)
    while batch:
        lines = "\n".join(map(lambda e: json.dumps(e, cls=EventEncoder), batch))
        batch = list(islice(iterator, batch_size))
        if batch:
            lines += "\n"
        yield lines.encode("utf-8")


def _put_block(url: str, part_num: int, block: bytes) -> dict:
    response = requests.put(url, data=block)
    etag = str(response.headers["ETag"])
    return {"ETag": etag, "PartNumber": part_num}


def _concurrent_upload_multipart_batch(
    data_batch_iterator: Iterable[bytes], signed_urls: List[str]
) -> List[dict]:
    """Uploads batches to presigned URLs concurrently using threads"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        logger.info("Starting multipart upload")
        futures = [
            executor.submit(_put_block, signed_urls[i], i + 1, block)
            for i, block in enumerate(data_batch_iterator)
        ]
        parts = [f.result() for f in concurrent.futures.as_completed(futures)]
        logger.info("Multipart upload complete")
        return sorted(parts, key=lambda d: d["PartNumber"])  # type: ignore


class JoinKey(str):
    @classmethod
    @typechecked
    def from_dict(cls, dict_: Dict) -> str:
        return hashlib.md5(
            json.dumps(dict_, sort_keys=True, cls=EventEncoder).encode("utf-8")
        ).hexdigest()
