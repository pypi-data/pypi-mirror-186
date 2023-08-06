import warnings

from pydantic import Field, constr, root_validator

from servicefoundry.auto_gen import models
from servicefoundry.lib.model.entity import Deployment
from servicefoundry.logger import logger
from servicefoundry.v2.lib.deploy import deploy_component

_TOP_LEVEL_COMMAND_DEPRECATION_MESSAGE = """
==================== DEPRECATION WARNING ====================
`command` has been deprecated and will be removed in future.
Please use `command` argument of `Image` or `DockerFileBuild` or `PythonBuild` instead.
E.g.
    {cls_name}(..., image=Image(..., command=...))
    OR {cls_name}(..., image=Build(..., build_spec=DockerFileBuild(..., command=...)))
    OR {cls_name}(..., image=Build(..., build_spec=PythonBuild(..., command=...)))

These are equivalent to `image.command` and `image.build_spec.command in yaml spec

E.g.

```
name: "{name}"
image:
  type: "image"
  command: ...
```

OR

```
name: "{name}"
image:
  type: "build"
  build_spec:
    type: "tfy-python-buildpack" # or "dockerfile"
    command: ...
```

============================================================
"""


def _warn_top_level_command_use(cls, values):
    command = values.get("command")
    image = values.get("image")
    if command and image:
        _message = _TOP_LEVEL_COMMAND_DEPRECATION_MESSAGE.format(
            cls_name=cls.__name__, name=values.get("name") or "NAME_NOT_FOUND"
        )
        logger.warning(_message)
        warnings.warn(_message, category=DeprecationWarning, stacklevel=2)
        if image.type == "image":
            values["image"].command = command
        elif image.type == "build":
            values["image"].build_spec.command = command
        values.pop("command")
    return values


class Service(models.Service):
    type: constr(regex=r"service") = "service"
    resources: models.Resources = Field(default_factory=models.Resources)

    class Config:
        extra = "forbid"

    _patch_command = root_validator(allow_reuse=True)(_warn_top_level_command_use)

    def deploy(self, workspace_fqn: str, wait: bool = True) -> Deployment:
        return deploy_component(component=self, workspace_fqn=workspace_fqn, wait=wait)


class Job(models.Job):
    type: constr(regex=r"job") = "job"
    resources: models.Resources = Field(default_factory=models.Resources)

    class Config:
        extra = "forbid"

    _patch_command = root_validator(allow_reuse=True)(_warn_top_level_command_use)

    def deploy(self, workspace_fqn: str, wait: bool = True) -> Deployment:
        return deploy_component(component=self, workspace_fqn=workspace_fqn, wait=wait)


class Notebook(models.Notebook):
    type: constr(regex=r"notebook") = "notebook"
    resources: models.Resources = Field(default_factory=models.Resources)

    class Config:
        extra = "forbid"

    def deploy(self, workspace_fqn: str) -> Deployment:
        return deploy_component(component=self, workspace_fqn=workspace_fqn)


class ModelDeployment(models.ModelDeployment):
    type: constr(regex=r"model-deployment") = "model-deployment"
    resources: models.Resources = Field(default_factory=models.Resources)

    class Config:
        extra = "forbid"

    def deploy(self, workspace_fqn: str, wait: bool = True) -> Deployment:
        return deploy_component(component=self, workspace_fqn=workspace_fqn, wait=wait)


class Application(models.Application):
    class Config:
        extra = "forbid"

    def deploy(self, workspace_fqn: str, wait: bool = True) -> Deployment:
        return deploy_component(
            component=self.__root__, workspace_fqn=workspace_fqn, wait=wait
        )
