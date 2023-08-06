import logging

import rich_click as click

from servicefoundry.cli.config import CliConfig
from servicefoundry.cli.const import COMMAND_CLS, ENABLE_CLUSTER_COMMANDS, GROUP_CLS
from servicefoundry.cli.display_util import print_json, print_obj
from servicefoundry.cli.util import handle_exception_wrapper
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.lib.dao import workspace as workspace_lib
from servicefoundry.lib.model.entity import Cluster, Workspace

logger = logging.getLogger(__name__)

# TODO (chiragjn): --json should disable all non json console prints


@click.group(name="get", cls=GROUP_CLS)
def get_command():
    # TODO (chiragjn): Figure out a way to update supported resources based on ENABLE_* flags
    """
    Get servicefoundry resources

    \b
    Supported resources:
    - Workspace
    - Service
    - Deployment
    """
    pass


@click.command(name="cluster", cls=COMMAND_CLS, help="Get Cluster metadata")
@click.argument("cluster_id")
@handle_exception_wrapper
def get_cluster(cluster_id):
    tfs_client = ServiceFoundryServiceClient()
    cluster = tfs_client.get_cluster(cluster_id)
    if CliConfig.get("json"):
        print_json(data=cluster)
    else:
        print_obj("Cluster", cluster, columns=Cluster.get_display_columns)


@click.command(name="workspace", cls=COMMAND_CLS, help="Get Workspace metadata")
@click.argument("name", type=click.STRING)
@click.option(
    "-c",
    "--cluster",
    type=click.STRING,
    default=None,
    help="cluster to find this workspace in",
)
@click.option("--non-interactive", is_flag=True, default=False)
@handle_exception_wrapper
def get_workspace(name, cluster, non_interactive):
    workspace = workspace_lib.get_workspace(
        name_or_id=name,
        cluster_name_or_id=cluster,
        non_interactive=non_interactive,
    )
    if CliConfig.get("json"):
        print_json(data=workspace.to_dict())
    else:
        print_obj(
            "Workspace", workspace.to_dict(), columns=Workspace.get_display_columns
        )


def get_get_command():
    get_command.add_command(get_workspace)
    if ENABLE_CLUSTER_COMMANDS:
        get_command.add_command(get_cluster)
    return get_command
