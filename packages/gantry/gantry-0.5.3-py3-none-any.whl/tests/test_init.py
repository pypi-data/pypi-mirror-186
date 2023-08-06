import mock

from gantry import init


@mock.patch("gantry.logger_init")
@mock.patch("gantry.query_init")
@mock.patch("gantry.alerts_init")
def test_init(mock_alers_init, mock_query_init, mock_logger_init):
    init("foobar", "INFO", "dev", False)

    mock_alers_init.assert_called_once_with("foobar")
    mock_query_init.assert_called_once_with("foobar")
    mock_logger_init.assert_called_once_with("foobar", "INFO", "dev", False)
