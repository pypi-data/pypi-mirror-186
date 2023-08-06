import json

import click
from click_aliases import ClickAliasedGroup

import gantry
from gantry.api_client import APIClient


@click.group(cls=ClickAliasedGroup)
def data_connector():
    """
    Use this to manage your data connectors with gantry.
    """
    pass


@data_connector.command(
    aliases=["create"],
    help="Creates a new data connector to your data source with Gantry.",
)
@click.option(
    "--name", type=click.STRING, required=True, help="A unique name of the data connector"
)
@click.option(
    "--connection-type",
    type=click.Choice(
        ["SNOWFLAKE", "BIGQUERY", "S3"],
        case_sensitive=False,
    ),
    required=True,
    help="Type of the source data connection",
)
@click.option(
    "--database-name", type=click.STRING, required=True, help="Name of the source database"
)
@click.option(
    "--secret-name",
    type=click.STRING,
    required=True,
    help="Name of the secret registered with Gantry",
)
@click.option(
    "--description", type=click.STRING, required=True, help="Description of the data connector"
)
@click.option(
    "--options",
    type=click.STRING,
    required=True,
    help="JSON string of the options for the data connector",
)
def create(
    name: str,
    connection_type: str,
    database_name: str,
    secret_name: str,
    description: str,
    options: str,
):
    gantry.init()
    api_client: APIClient = gantry.get_client().log_store._api_client
    request_body = {
        "name": name,
        "connection_type": connection_type,
        "database_name": database_name,
        "secret_name": secret_name,
        "description": description,
        "options": json.loads(options),
    }

    resp = api_client.request(
        "POST", "/api/v1/data-connectors/sources", json=request_body, raise_for_status=True
    )

    click.secho(
        f"--> A source data connector has been created.\n {json.dumps(resp['data'], indent=4)}"
    )


@data_connector.command(
    aliases=["list"],
    help="List data connectors registered with Gantry.",
)
def list():
    gantry.init()
    api_client: APIClient = gantry.get_client().log_store._api_client
    resp = api_client.request("GET", "/api/v1/data-connectors", raise_for_status=True)

    click.secho(f"--> A list of registered data connectors:\n {json.dumps(resp['data'], indent=4)}")


@data_connector.command(
    aliases=["delete"],
    help="Deletes a data connector.",
)
@click.option(
    "--name", type=click.STRING, required=True, help="A unique name of the data connector"
)
def delete(name: str):
    gantry.init()
    api_client: APIClient = gantry.get_client().log_store._api_client
    resp = api_client.request(
        "DELETE", f"/api/v1/data-connectors/sources/{name}", raise_for_status=True
    )

    click.secho(
        f"--> Deleted the source data connector {name}:\n {json.dumps(resp['data'], indent=4)}"
    )
