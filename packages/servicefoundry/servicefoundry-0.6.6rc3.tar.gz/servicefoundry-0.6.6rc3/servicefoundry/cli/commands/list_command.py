import logging

import rich_click as click

from servicefoundry.cli.config import CliConfig
from servicefoundry.cli.console import console
from servicefoundry.cli.const import (
    COMMAND_CLS,
    ENABLE_AUTHORIZE_COMMANDS,
    ENABLE_CLUSTER_COMMANDS,
    ENABLE_SECRETS_COMMANDS,
    GROUP_CLS,
)
from servicefoundry.cli.display_util import print_json, print_list
from servicefoundry.cli.util import handle_exception_wrapper
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.lib.dao import deployment as deployment_lib
from servicefoundry.lib.dao import workspace as workspace_lib
from servicefoundry.lib.messages import (
    PROMPT_NO_DEPLOYMENTS,
    PROMPT_NO_SERVICES,
    PROMPT_NO_WORKSPACES,
)
from servicefoundry.lib.model.entity import (
    Cluster,
    NewDeployment,
    Secret,
    SecretGroup,
    Workspace,
)

logger = logging.getLogger(__name__)

# TODO (chiragjn): --json should disable all non json console prints


@click.group(name="list", cls=GROUP_CLS)
def list_command():
    # TODO (chiragjn): Figure out a way to update supported resources based on ENABLE_* flags
    """
    Servicefoundry list resources
    """


@click.command(name="cluster", cls=COMMAND_CLS, help="List Clusters")
@handle_exception_wrapper
def list_cluster():
    tfs_client = ServiceFoundryServiceClient()
    clusters = tfs_client.list_cluster()
    if CliConfig.get("json"):
        print_json(data=clusters)
    else:
        print_list("Clusters", clusters, Cluster.list_display_columns)


@click.command(name="workspace", cls=COMMAND_CLS, help="List Workspaces")
@click.option("-A", "--all", is_flag=True, default=False)
@click.option("-c", "--cluster", type=click.STRING, default=None, help="cluster name")
@click.option("--non-interactive", is_flag=True, default=False)
@handle_exception_wrapper
def list_workspace(all, cluster, non_interactive):
    # Tests:
    # - Set Context -> list workspace -> Should get workspaces in set cluster
    # - Set Context -> list workspace -c 'cluster_name' -> Should get workspaces in given cluster
    # - Set Context -> list workspace -c 'invalid_cluster_name' -> Should give error invalid cluster
    # - Set Context -> list workspace -A -> Should give all workspaces across all clusters
    # - No Context -> list workspace -c 'cluster_name' -> Should get workspaces in given cluster
    # - No Context -> list workspace -c 'invalid_cluster_name' -> Should give error invalid cluster
    # - No Context -> list workspace -A -> Should give all workspaces across all clusters
    # ? No Context -> list workspace -> Should list workspaces if there is only cluster or ask for cluster name
    workspaces = workspace_lib.list_workspaces(
        cluster_name_or_id=cluster,
        all_=all,
        non_interactive=non_interactive,
    )
    if not workspaces:
        console.print(PROMPT_NO_WORKSPACES)
    else:
        workspaces.sort(key=lambda w: (w.fqn, w.createdAt))
    # TODO (chiragjn): Display columns here need to show cluster name!
    workspaces = [w.to_dict() for w in workspaces]
    if CliConfig.get("json"):
        print_json(data=workspaces)
    else:
        print_list(
            "Workspaces",
            workspaces,
            columns=Workspace.list_display_columns,
        )


@click.command(name="deployment", cls=COMMAND_CLS, help="List Deployments")
@click.option(
    "-w", "--workspace", type=click.STRING, default=None, help="workspace fqn"
)
@handle_exception_wrapper
def list_deployments(workspace):
    deployments = deployment_lib.list_deployments(
        workspace_fqn=workspace,
    )
    if not deployments:
        console.print(PROMPT_NO_DEPLOYMENTS)
    else:
        deployments.sort(key=lambda s: (s.fqn))

    deployments = [s.to_dict() for s in deployments]
    if CliConfig.get("json"):
        print_json(data=deployments)
    else:
        # TODO (chiragjn): Display columns here need to show workspace and cluster name!
        print_list(
            "Deployments",
            deployments,
            columns=NewDeployment.list_display_columns,
        )


@click.command(name="secret-group", cls=COMMAND_CLS, help="List Secret Groups")
@handle_exception_wrapper
def list_secret_group():
    tfs_client = ServiceFoundryServiceClient()
    response = tfs_client.get_secret_groups()
    print_list("Secret Groups", response, columns=SecretGroup.list_display_columns)


@click.command(name="secret", cls=COMMAND_CLS, help="List Secrets in a Secret Group")
@click.argument("secret_group_id")
@handle_exception_wrapper
def list_secret(secret_group_id):
    tfs_client = ServiceFoundryServiceClient()
    response = tfs_client.get_secrets_in_group(secret_group_id)
    print_list("Secrets", response, columns=Secret.list_display_columns)


@click.command(
    name="authorize", cls=COMMAND_CLS, help="List authorization for a resource id."
)
@click.argument("resource_type", type=click.Choice(["workspace"], case_sensitive=False))
@click.argument("resource_id")
@handle_exception_wrapper
def list_authorize(resource_type, resource_id):
    tfs_client = ServiceFoundryServiceClient()
    response = tfs_client.get_authorization_for_resource(resource_type, resource_id)
    print_list(f"Auth for {resource_type}: {resource_id}", response)


def get_list_command():
    # list_command.add_command(list_workspace)
    list_command.add_command(list_deployments)

    # if ENABLE_AUTHORIZE_COMMANDS:
    #     list_command.add_command(list_authorize)
    # if ENABLE_CLUSTER_COMMANDS:
    #     list_command.add_command(list_cluster)
    # if ENABLE_SECRETS_COMMANDS:
    #     list_command.add_command(list_secret)
    #     list_command.add_command(list_secret_group)

    return list_command
