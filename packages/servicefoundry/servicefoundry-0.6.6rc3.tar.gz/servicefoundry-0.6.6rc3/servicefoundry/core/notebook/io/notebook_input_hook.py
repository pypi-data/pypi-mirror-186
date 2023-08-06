import questionary
from questionary import Choice

from servicefoundry.cli.console import console
from servicefoundry.cli.io.cli_input_hook import MSG_CREATE_NEW_SPACE
from servicefoundry.io.input_hook import InputHook
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)


class NotebookInputHook(InputHook):
    def confirm(self, prompt, default=False):
        raise NotImplementedError()

    def ask_file_path(self, param):
        raise NotImplementedError()

    def ask_python_file(self, param):
        raise NotImplementedError()

    def __init__(self, tfs_client: ServiceFoundryServiceClient):
        super().__init__(tfs_client)

    def ask_string(self, param):
        return questionary.text(param.prompt, default=param.default).ask()

    def ask_number(self, param):
        while True:
            value = questionary.text(param.prompt, default=str(param.default)).ask()
            if value.isdigit():
                return int(value)
            else:
                print("Not an integer Value. Try again")

    def ask_option(self, param):
        return questionary.select(param.prompt, choices=param.options).ask()

    def ask_workspace(self, param):
        tfs_client = ServiceFoundryServiceClient()
        space_choices = self.get_workspace_choices()  # TODO: unresolved reference!
        space_choices.append(
            Choice(title=MSG_CREATE_NEW_SPACE, value=MSG_CREATE_NEW_SPACE)
        )
        space = questionary.select(param.prompt, choices=space_choices).ask()

        if space == MSG_CREATE_NEW_SPACE:
            cluster = tfs_client.session.get_cluster()
            if not cluster:
                raise Exception(
                    "No default cluster set to create workspace. "
                    "Use `sfy use cluster` to pick and set a default cluster"
                )
            new_space_name = questionary.text(
                "Please provide a name for your workspace"
            ).ask()
            console.print("Please wait while your workspace is being created. ")
            response = tfs_client.create_workspace(
                cluster_id=cluster["id"], name=new_space_name
            )
            console.print(f"Done, created new workspace with name {new_space_name!r}")
            space = response["workspace"]

        return space["fqn"]
