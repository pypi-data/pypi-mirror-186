import pytest
import mock
from gantry.dataset import main
from gantry.exceptions import ClientNotInitialized
from .conftest import USER_EMAIL, AWS_REGION, BUCKET_NAME


@pytest.mark.parametrize(
    ["method", "params"],
    [
        ("create_dataset", {"name": "dataset_name"}),
        ("get_dataset", {"name": "dataset_name"}),
        ("list_dataset_commits", {"name": "dataset_name"}),
        ("list_datasets", {}),
    ],
)
def test_uninit_client_main(method, params):
    """Test all public methods from dataset module
    fail if client is not initialized
    """
    with mock.patch("gantry.dataset.main._DATASET", None):
        with pytest.raises(ClientNotInitialized):
            getattr(main, method)(**params)


@pytest.mark.parametrize("backend", ["", "/some/file", "tcp://other/protocol"])
def test_global_init_error(backend):
    """Test invalide backend"""
    with pytest.raises(ValueError):
        main.init(email=USER_EMAIL, backend=backend)


@pytest.mark.parametrize("valid_backend", ["http", "https"])
def test_no_api_key_provided(valid_backend):
    with mock.patch.dict("os.environ", {"GANTRY_API_KEY": ""}):
        with pytest.raises(ValueError):
            main.init(email=USER_EMAIL, backend=valid_backend, api_key=None)


def test_init():
    """Test init"""
    passed_api_key = "some_key"
    with mock.patch.dict("os.environ", {"GANTRY_API_KEY": passed_api_key}):
        main.init(
            email=USER_EMAIL,
            backend="https://gantry.datasettest",
            bucket_name=BUCKET_NAME,
            aws_region=AWS_REGION,
        )
        assert main._DATASET._api_client._host == "https://gantry.datasettest"
        assert main._DATASET._api_client._api_key == passed_api_key
        assert main._DATASET.email == USER_EMAIL
        assert main._DATASET.bucket_name == BUCKET_NAME
        assert main._DATASET.aws_region == AWS_REGION


def test_init_default():
    """Test init client with default values"""
    main.init(email=USER_EMAIL, backend="https://foo/bar", api_key="ABCD1234")
    assert main._DATASET._api_client._host == "https://foo/bar"
    assert main._DATASET._api_client._api_key == "ABCD1234"
    assert main._DATASET.email == USER_EMAIL
    assert not main._DATASET.aws_region and not main._DATASET.bucket_name


@pytest.mark.parametrize(
    ["method", "params"],
    [
        ("create_dataset", {"name": "dataset_name"}),
        ("get_dataset", {"name": "dataset_name"}),
        ("list_dataset_commits", {"name": "dataset_name"}),
        ("list_datasets", {}),
    ],
)
def test_dataset_methods(method, params):
    """Test all public methods from gantry module or gantry.main module
    resolve in the global _DATASET methods
    """
    m = mock.Mock()
    with mock.patch("gantry.dataset.main._DATASET", m):
        getattr(main, method)(**params)
        getattr(m, method).assert_called_once_with(**params)
