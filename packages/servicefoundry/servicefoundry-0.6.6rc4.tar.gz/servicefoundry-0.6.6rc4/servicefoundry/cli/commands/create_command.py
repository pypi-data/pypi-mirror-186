import logging

import rich_click as click

from servicefoundry.cli.const import COMMAND_CLS, GROUP_CLS
from servicefoundry.cli.display_util import print_obj
from servicefoundry.cli.util import handle_exception_wrapper
from servicefoundry.lib.dao import workspace as workspace_lib

logger = logging.getLogger(__name__)

WORKSPACE_DISPLAY_FIELDS = [
    "id",
    "name",
    "namespace",
    "status",
    "clusterId",
    "createdBy",
    "createdAt",
    "updatedAt",
]
DEPLOYMENT_DISPLAY_FIELDS = [
    "id",
    "serviceId",
    "domain",
    "deployedBy",
    "createdAt",
    "updatedAt",
]


@click.group(name="create", cls=GROUP_CLS)
def create_command():
    # TODO (chiragjn): Figure out a way to update supported resources based on ENABLE_* flags
    """
    Create servicefoundry resources

    \b
    Supported resources:
    - Workspace
    """
    pass


@click.command(name="workspace", cls=COMMAND_CLS, help="Create a new Workspace")
@click.argument("name", type=click.STRING)
@click.option(
    "-c",
    "--cluster",
    type=click.STRING,
    default=None,
    help="cluster to create this workspace in",
)
@click.option("--non-interactive", is_flag=True, default=False)
@handle_exception_wrapper
def create_workspace(name, cluster, non_interactive):
    workspace = workspace_lib.create_workspace(
        name=name,
        cluster_name_or_id=cluster,
        non_interactive=non_interactive,
    )
    print_obj("Workspace", workspace.to_dict())


def get_create_command():
    create_command.add_command(create_workspace)
    return create_command
