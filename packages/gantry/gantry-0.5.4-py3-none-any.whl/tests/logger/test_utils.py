import json
from io import StringIO

import mock
import pandas as pd
import pytest
import responses

from gantry.exceptions import (  # noqa
    GantryBatchCreationException,
    GantryLoggingException,
)
from gantry.logger.stores import APILogStore
from gantry.logger.utils import (
    JoinKey,
    _batch_success_msg,
    _build_batch_iterator,
    _build_success_msg,
    _concurrent_upload_multipart_batch,
    _is_empty,
    _is_not_empty,
    _log_exception,
    _put_block,
)


@pytest.mark.parametrize(
    ["test_obj", "expected_result"],
    [
        (pd.DataFrame(), True),
        (pd.DataFrame.from_dict({"A": [200, 201]}), False),
        ([1, 2, 3], False),
        ([], True),
        (None, True),
    ],
)
def test_is_empty(test_obj, expected_result):
    assert _is_empty(test_obj) is expected_result


@pytest.mark.parametrize(
    ["test_obj", "expected_result"],
    [
        (pd.DataFrame(), False),
        (pd.DataFrame.from_dict({"A": [200, 201]}), True),
        ([1, 2, 3], True),
        ([], False),
        (None, False),
    ],
)
def test_is_not_empty(test_obj, expected_result):
    assert _is_not_empty(test_obj) is expected_result


def test_log_exception():
    try:
        _log_exception(lambda: exec("raise(GantryLoggingException())"))()
    except Exception as e:
        pytest.fail(f"_log_exception() failed due to raising {e}")
    with pytest.raises(GantryBatchCreationException):
        _log_exception(lambda: exec("raise(GantryBatchCreationException())"))()
    try:
        _log_exception(lambda: exec("raise(Exception())"))()
    except Exception as e:
        pytest.fail(f"_log_exception() failed due to raising {e}")


def test_build_batch_iterator():
    event_list = [{1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}]
    # We should only have 3 batches created from the list.
    batch_iter = _build_batch_iterator(event_list, 2)
    iters = 0
    for _ in batch_iter:
        iters += 1
    assert iters == 3

    # We should still have all 5 lines in the file
    batch_iter = _build_batch_iterator(event_list, 2)
    result = "".join([part.decode("utf-8") for part in batch_iter])
    file = StringIO(result)

    for line in file.readlines():
        json.loads(line)

    file.seek(0)
    assert len(file.readlines()) == 5


def test_put_block():
    def custom_matcher(req):
        return (
            req.body == b"foobar",
            "Body doesn't match",
        )

    with responses.RequestsMock() as resp:
        resp.add(
            resp.PUT,
            url="http://foo/bar",
            headers={"ETag": "0123456789", "Content-Type": "application/json"},
            match=[custom_matcher],
        )
        res = _put_block("http://foo/bar", 10, b"foobar")
        assert res == {"ETag": "0123456789", "PartNumber": 10}


@mock.patch("gantry.logger.utils._put_block")
def test_concurrent_upload(mock_put_block):
    mock_put_block.side_effect = [
        {"ETag": "123", "PartNumber": 2},
        {"ETag": "456", "PartNumber": 1},
        {"ETag": "789", "PartNumber": 3},
    ]

    data = [{"1": "foo"}, {"2": "bar"}, {"3": "baz"}]
    signed_urls = ["http://foo", "http://bar", "http://baz"]

    ret = _concurrent_upload_multipart_batch(iter(data), signed_urls)
    assert ret == [
        {"ETag": "456", "PartNumber": 1},
        {"ETag": "123", "PartNumber": 2},
        {"ETag": "789", "PartNumber": 3},
    ]


@pytest.mark.parametrize(
    ["host", "application", "expected"],
    [
        (
            "https://staging.com/",
            "app",
            "Track your batch at https://staging.com/applications/app/jobs",
        ),
        (
            "https://staging.com",
            "app",
            "Track your batch at https://staging.com/applications/app/jobs",
        ),
        (
            "https://staging.com",
            "my app",
            "Track your batch at https://staging.com/applications/my%20app/jobs",
        ),
    ],
)
def test_build_success_msg(host, application, expected):
    assert _build_success_msg(host, application) == expected


@mock.patch("gantry.logger.utils._build_success_msg")
def test_batch_success_msg(mock_build_msg):
    log_store = mock.Mock(__class__=APILogStore)
    _batch_success_msg("12345", "app", log_store)
    mock_build_msg.assert_called_with(log_store._api_client._host, "app")


@pytest.mark.parametrize(
    ["dict_", "expected"],
    [
        ({"foo": "bar", "bar": "baz"}, "44258089824ec9db73fd592f418fbea1"),
        ({"bar": "baz", "foo": "bar"}, "44258089824ec9db73fd592f418fbea1"),
        ({"foo": "bar", "bar": 10}, "01debdea5ba523b44164d202fbbe42da"),
        ({"bar": None, "foo": "bar"}, "ade3188c2cfeae4234e0b7b042b74c35"),
        ({"foo": True, "bar": 10.4321}, "294ca280f5485b49fec1247e5b45d644"),
        ({"bar": [1, 2, 3], "foo": {"another": "dict"}}, "152874e4c1db6061d5a45ee38c3eace0"),
    ],
)
def test_join_key_from_dict(dict_, expected):
    assert JoinKey.from_dict(dict_) == expected


@pytest.mark.parametrize("dict_", [None, True, 10, "something"])
def test_join_key_from_dict_error(dict_):
    with pytest.raises(TypeError):
        _ = JoinKey.from_dict(dict_)
