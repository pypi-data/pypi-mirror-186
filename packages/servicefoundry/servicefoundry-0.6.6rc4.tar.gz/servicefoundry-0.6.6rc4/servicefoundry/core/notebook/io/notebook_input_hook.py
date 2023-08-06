import questionary

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
