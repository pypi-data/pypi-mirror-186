import json

import mock
import responses
from click.testing import CliRunner
from responses import matchers

from gantry.cli.data_connector import create, delete, list

UNITTEST_HOST = "http://unittest"
DATA_CONNECTOR_NAME = "test_data_connector"
DATA_CONNECTOR_1_ID = "0db220e0-f568-4295-be48-67095fa57f34"
DATA_CONNECTOR_2_ID = "9e09947e-fb18-4ce3-bd17-7c386a3c9980"
DATABASE_NAME = "test_database"
CONNECTION_TYPE = "SNOWFLAKE"
DESCRIPTION = "Data connector to log records from my snowflake database"
SECRET_NAME = "test_secret"
OPTIONS = '{"schema_name": "PUBLIC","table_name": "GANTRY_EVENTS"}'


def test_create_data_connector():
    runner = CliRunner()
    cli_args = [
        "--name",
        DATA_CONNECTOR_NAME,
        "--database-name",
        DATABASE_NAME,
        "--connection-type",
        CONNECTION_TYPE,
        "--secret-name",
        SECRET_NAME,
        "--description",
        DESCRIPTION,
        "--options",
        OPTIONS,
    ]

    with responses.RequestsMock() as resp:
        resp.add(
            resp.POST,
            f"{UNITTEST_HOST}/api/v1/data-connectors/sources",
            json={
                "response": "ok",
                "data": {
                    "connection_type": CONNECTION_TYPE,
                    "created_at": "2023-01-18T00:18:01.000000",
                    "database_name": DATABASE_NAME,
                    "description": DESCRIPTION,
                    "id": DATA_CONNECTOR_1_ID,
                    "name": DATABASE_NAME,
                    "options": {"schema_name": "PUBLIC", "table_name": "GANTRY_EVENTS"},
                    "secret_name": SECRET_NAME,
                    "type": "SOURCE",
                    "updated_at": "2023-01-18T00:18:01.000000",
                },
            },
            headers={"Content-Type": "application/json"},
            match=[
                matchers.json_params_matcher(
                    {
                        "name": DATA_CONNECTOR_NAME,
                        "database_name": DATABASE_NAME,
                        "connection_type": CONNECTION_TYPE,
                        "secret_name": SECRET_NAME,
                        "description": DESCRIPTION,
                        "options": json.loads(OPTIONS),
                    }
                )
            ],
        )

        result = runner.invoke(
            create,
            cli_args,
            env={"GANTRY_API_KEY": "test", "GANTRY_LOGS_LOCATION": UNITTEST_HOST},
        )

        assert result.exit_code == 0
        assert "--> A source data connector has been created" in result.output


def test_create_data_connector_input_validation_failure():
    """
    Tests that invalid connection type throws an error
    """
    runner = CliRunner()
    cli_args = [
        "--name",
        DATA_CONNECTOR_NAME,
        "--database-name",
        DATABASE_NAME,
        "--connection-type",
        "NOT_VALID_TYPE",
        "--secret-name",
        SECRET_NAME,
        "--description",
        DESCRIPTION,
        "--options",
        OPTIONS,
    ]

    result = runner.invoke(
        create,
        cli_args,
        env={"GANTRY_API_KEY": "test", "GANTRY_LOGS_LOCATION": UNITTEST_HOST},
    )

    assert result.exit_code == 2
    assert "Error: Invalid value for '--connection-type': 'NOT_VALID_TYPE'" in result.output


@mock.patch("gantry.cli.data_connector.APIClient.request")
def test_create_data_connector_api_failure(mock_api_client: mock.Mock):
    """
    Tests that invalid connection type throws an error
    """
    mock_api_client.return_value = {"response": "error", "error": "some error"}

    runner = CliRunner()
    cli_args = [
        "--name",
        DATA_CONNECTOR_NAME,
        "--database-name",
        DATABASE_NAME,
        "--connection-type",
        CONNECTION_TYPE,
        "--secret-name",
        SECRET_NAME,
        "--description",
        DESCRIPTION,
        "--options",
        OPTIONS,
    ]

    result = runner.invoke(
        create,
        cli_args,
        env={"GANTRY_API_KEY": "test", "GANTRY_LOGS_LOCATION": UNITTEST_HOST},
    )

    assert result.exit_code == 1


def test_list_data_connectors():
    """
    Tests that correct message displays when list command returns data connectors
    """
    runner = CliRunner()

    with responses.RequestsMock() as resp:
        resp.add(
            resp.GET,
            f"{UNITTEST_HOST}/api/v1/data-connectors",
            json={
                "response": "ok",
                "data": [
                    {
                        "connection_type": CONNECTION_TYPE,
                        "created_at": "2023-01-18T00:18:01.000000",
                        "database_name": DATABASE_NAME,
                        "description": DESCRIPTION,
                        "id": DATA_CONNECTOR_1_ID,
                        "name": DATABASE_NAME,
                        "options": {"schema_name": "PUBLIC", "table_name": "GANTRY_EVENTS"},
                        "secret_name": SECRET_NAME,
                        "type": "SOURCE",
                        "updated_at": "2023-01-18T00:18:01.000000",
                    },
                    {
                        "connection_type": CONNECTION_TYPE,
                        "created_at": "2023-01-18T00:18:01.000000",
                        "database_name": DATABASE_NAME,
                        "description": DESCRIPTION,
                        "id": DATA_CONNECTOR_2_ID,
                        "name": DATABASE_NAME,
                        "options": {"schema_name": "PUBLIC", "table_name": "GANTRY_EVENTS_2"},
                        "secret_name": SECRET_NAME,
                        "type": "SOURCE",
                        "updated_at": "2023-01-18T00:18:01.000000",
                    },
                ],
            },
            headers={"Content-Type": "application/json"},
        )

        result = runner.invoke(
            list,
            env={"GANTRY_API_KEY": "test", "GANTRY_LOGS_LOCATION": UNITTEST_HOST},
        )

        assert result.exit_code == 0
        assert "--> A list of registered data connectors" in result.output
        assert DATA_CONNECTOR_1_ID in result.output
        assert DATA_CONNECTOR_2_ID in result.output


def test_delete_data_connector():
    """ """
    runner = CliRunner()
    cli_args = ["--name", DATA_CONNECTOR_NAME]

    with responses.RequestsMock() as resp:
        resp.add(
            resp.DELETE,
            f"{UNITTEST_HOST}/api/v1/data-connectors/sources/{DATA_CONNECTOR_NAME}",
            json={
                "response": "ok",
                "data": {
                    "connection_type": CONNECTION_TYPE,
                    "created_at": "2023-01-18T00:18:01.000000",
                    "database_name": DATABASE_NAME,
                    "description": DESCRIPTION,
                    "id": DATA_CONNECTOR_1_ID,
                    "name": DATABASE_NAME,
                    "options": {"schema_name": "PUBLIC", "table_name": "GANTRY_EVENTS"},
                    "secret_name": SECRET_NAME,
                    "type": "SOURCE",
                    "updated_at": "2023-01-18T00:18:01.000000",
                },
            },
            headers={"Content-Type": "application/json"},
        )

        result = runner.invoke(
            delete,
            cli_args,
            env={"GANTRY_API_KEY": "test", "GANTRY_LOGS_LOCATION": UNITTEST_HOST},
        )

        assert result.exit_code == 0
        assert "--> Deleted the source data connector" in result.output
        assert DATA_CONNECTOR_1_ID in result.output
