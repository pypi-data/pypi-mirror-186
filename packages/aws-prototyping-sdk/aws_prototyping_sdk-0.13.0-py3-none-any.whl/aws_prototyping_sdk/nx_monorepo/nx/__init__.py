import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ..._jsii import *


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.NamedInputs",
    jsii_struct_bases=[],
    name_mapping={},
)
class NamedInputs:
    def __init__(self) -> None:
        '''Named inputs config.

        :see: https://nx.dev/reference/nx-json#inputs-&-namedinputs
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamedInputs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.ProjectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "implicit_dependencies": "implicitDependencies",
        "included_scripts": "includedScripts",
        "named_inputs": "namedInputs",
        "tags": "tags",
        "targets": "targets",
    },
)
class ProjectConfig:
    def __init__(
        self,
        *,
        implicit_dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        included_scripts: typing.Optional[typing.Sequence[builtins.str]] = None,
        named_inputs: typing.Optional[typing.Union[NamedInputs, typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        targets: typing.Optional[typing.Mapping[builtins.str, typing.Union["ProjectTarget", typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param implicit_dependencies: Implicit dependencies.
        :param included_scripts: Explicit list of scripts for Nx to include.
        :param named_inputs: Named inputs.
        :param tags: Project tag annotations.
        :param targets: Targets configuration.
        '''
        if isinstance(named_inputs, dict):
            named_inputs = NamedInputs(**named_inputs)
        if __debug__:
            def stub(
                *,
                implicit_dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
                included_scripts: typing.Optional[typing.Sequence[builtins.str]] = None,
                named_inputs: typing.Optional[typing.Union[NamedInputs, typing.Dict[str, typing.Any]]] = None,
                tags: typing.Optional[typing.Sequence[builtins.str]] = None,
                targets: typing.Optional[typing.Mapping[builtins.str, typing.Union[ProjectTarget, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument implicit_dependencies", value=implicit_dependencies, expected_type=type_hints["implicit_dependencies"])
            check_type(argname="argument included_scripts", value=included_scripts, expected_type=type_hints["included_scripts"])
            check_type(argname="argument named_inputs", value=named_inputs, expected_type=type_hints["named_inputs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if implicit_dependencies is not None:
            self._values["implicit_dependencies"] = implicit_dependencies
        if included_scripts is not None:
            self._values["included_scripts"] = included_scripts
        if named_inputs is not None:
            self._values["named_inputs"] = named_inputs
        if tags is not None:
            self._values["tags"] = tags
        if targets is not None:
            self._values["targets"] = targets

    @builtins.property
    def implicit_dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Implicit dependencies.

        :see: https://nx.dev/reference/project-configuration#implicitdependencies
        '''
        result = self._values.get("implicit_dependencies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def included_scripts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit list of scripts for Nx to include.

        :see: https://nx.dev/reference/project-configuration#ignoring-package.json-scripts
        '''
        result = self._values.get("included_scripts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def named_inputs(self) -> typing.Optional[NamedInputs]:
        '''Named inputs.

        :see: https://nx.dev/reference/nx-json#inputs-&-namedinputs
        '''
        result = self._values.get("named_inputs")
        return typing.cast(typing.Optional[NamedInputs], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Project tag annotations.

        :see: https://nx.dev/reference/project-configuration#tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def targets(self) -> typing.Optional[typing.Mapping[builtins.str, "ProjectTarget"]]:
        '''Targets configuration.

        :see: https://nx.dev/reference/project-configuration
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "ProjectTarget"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.ProjectTarget",
    jsii_struct_bases=[],
    name_mapping={"depends_on": "dependsOn", "inputs": "inputs", "outputs": "outputs"},
)
class ProjectTarget:
    def __init__(
        self,
        *,
        depends_on: typing.Optional[typing.Sequence[typing.Union["TargetDependency", typing.Dict[str, typing.Any]]]] = None,
        inputs: typing.Optional[typing.Sequence[builtins.str]] = None,
        outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Project Target.

        :param depends_on: List of Target Dependencies.
        :param inputs: List of inputs to hash for cache key, relative to the root of the monorepo. note: must start with leading /
        :param outputs: List of outputs to cache, relative to the root of the monorepo. note: must start with leading /
        '''
        if __debug__:
            def stub(
                *,
                depends_on: typing.Optional[typing.Sequence[typing.Union[TargetDependency, typing.Dict[str, typing.Any]]]] = None,
                inputs: typing.Optional[typing.Sequence[builtins.str]] = None,
                outputs: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if inputs is not None:
            self._values["inputs"] = inputs
        if outputs is not None:
            self._values["outputs"] = outputs

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List["TargetDependency"]]:
        '''List of Target Dependencies.'''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List["TargetDependency"]], result)

    @builtins.property
    def inputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of inputs to hash for cache key, relative to the root of the monorepo.

        note: must start with leading /
        '''
        result = self._values.get("inputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outputs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of outputs to cache, relative to the root of the monorepo.

        note: must start with leading /
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.TargetDefaults",
    jsii_struct_bases=[],
    name_mapping={},
)
class TargetDefaults:
    def __init__(self) -> None:
        '''Target defaults config.

        :see: https://nx.dev/reference/nx-json#target-defaults
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.TargetDependency",
    jsii_struct_bases=[],
    name_mapping={"projects": "projects", "target": "target"},
)
class TargetDependency:
    def __init__(
        self,
        *,
        projects: "TargetDependencyProject",
        target: builtins.str,
    ) -> None:
        '''Represents an NX Target Dependency.

        :param projects: Target dependencies.
        :param target: Projen target i.e: build, test, etc.
        '''
        if __debug__:
            def stub(
                *,
                projects: TargetDependencyProject,
                target: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument projects", value=projects, expected_type=type_hints["projects"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "projects": projects,
            "target": target,
        }

    @builtins.property
    def projects(self) -> "TargetDependencyProject":
        '''Target dependencies.'''
        result = self._values.get("projects")
        assert result is not None, "Required property 'projects' is missing"
        return typing.cast("TargetDependencyProject", result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Projen target i.e: build, test, etc.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetDependency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.TargetDependencyProject")
class TargetDependencyProject(enum.Enum):
    '''Supported enums for a TargetDependency.'''

    SELF = "SELF"
    '''Only rely on the package where the target is called.

    This is usually done for test like targets where you only want to run unit
    tests on the target packages without testing all dependent packages.
    '''
    DEPENDENCIES = "DEPENDENCIES"
    '''Target relies on executing the target against all dependencies first.

    This is usually done for build like targets where you want to build all
    dependant projects first.
    '''


@jsii.data_type(
    jsii_type="aws-prototyping-sdk.nx_monorepo.Nx.WorkspaceConfig",
    jsii_struct_bases=[],
    name_mapping={
        "affected_branch": "affectedBranch",
        "cacheable_operations": "cacheableOperations",
        "implicit_dependencies": "implicitDependencies",
        "named_inputs": "namedInputs",
        "nx_cloud_read_only_access_token": "nxCloudReadOnlyAccessToken",
        "nx_ignore": "nxIgnore",
        "target_defaults": "targetDefaults",
        "target_dependencies": "targetDependencies",
    },
)
class WorkspaceConfig:
    def __init__(
        self,
        *,
        affected_branch: typing.Optional[builtins.str] = None,
        cacheable_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        implicit_dependencies: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
        named_inputs: typing.Optional[typing.Union[NamedInputs, typing.Dict[str, typing.Any]]] = None,
        nx_cloud_read_only_access_token: typing.Optional[builtins.str] = None,
        nx_ignore: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_defaults: typing.Optional[typing.Union[TargetDefaults, typing.Dict[str, typing.Any]]] = None,
        target_dependencies: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[TargetDependency, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''NX workspace configurations.

        :param affected_branch: Affected branch. Default: mainline
        :param cacheable_operations: Defines the list of targets/operations that are cached by Nx. Default: ["build", "test"]
        :param implicit_dependencies: Configuration for Implicit Dependencies.
        :param named_inputs: Named inputs.
        :param nx_cloud_read_only_access_token: Read only access token if enabling nx cloud.
        :param nx_ignore: List of patterns to include in the .nxignore file.
        :param target_defaults: Target defaults.
        :param target_dependencies: Configuration for TargetDependencies.

        :see: https://nx.dev/configuration/packagejson
        '''
        if isinstance(named_inputs, dict):
            named_inputs = NamedInputs(**named_inputs)
        if isinstance(target_defaults, dict):
            target_defaults = TargetDefaults(**target_defaults)
        if __debug__:
            def stub(
                *,
                affected_branch: typing.Optional[builtins.str] = None,
                cacheable_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
                implicit_dependencies: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[builtins.str]]] = None,
                named_inputs: typing.Optional[typing.Union[NamedInputs, typing.Dict[str, typing.Any]]] = None,
                nx_cloud_read_only_access_token: typing.Optional[builtins.str] = None,
                nx_ignore: typing.Optional[typing.Sequence[builtins.str]] = None,
                target_defaults: typing.Optional[typing.Union[TargetDefaults, typing.Dict[str, typing.Any]]] = None,
                target_dependencies: typing.Optional[typing.Mapping[builtins.str, typing.Sequence[typing.Union[TargetDependency, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument affected_branch", value=affected_branch, expected_type=type_hints["affected_branch"])
            check_type(argname="argument cacheable_operations", value=cacheable_operations, expected_type=type_hints["cacheable_operations"])
            check_type(argname="argument implicit_dependencies", value=implicit_dependencies, expected_type=type_hints["implicit_dependencies"])
            check_type(argname="argument named_inputs", value=named_inputs, expected_type=type_hints["named_inputs"])
            check_type(argname="argument nx_cloud_read_only_access_token", value=nx_cloud_read_only_access_token, expected_type=type_hints["nx_cloud_read_only_access_token"])
            check_type(argname="argument nx_ignore", value=nx_ignore, expected_type=type_hints["nx_ignore"])
            check_type(argname="argument target_defaults", value=target_defaults, expected_type=type_hints["target_defaults"])
            check_type(argname="argument target_dependencies", value=target_dependencies, expected_type=type_hints["target_dependencies"])
        self._values: typing.Dict[str, typing.Any] = {}
        if affected_branch is not None:
            self._values["affected_branch"] = affected_branch
        if cacheable_operations is not None:
            self._values["cacheable_operations"] = cacheable_operations
        if implicit_dependencies is not None:
            self._values["implicit_dependencies"] = implicit_dependencies
        if named_inputs is not None:
            self._values["named_inputs"] = named_inputs
        if nx_cloud_read_only_access_token is not None:
            self._values["nx_cloud_read_only_access_token"] = nx_cloud_read_only_access_token
        if nx_ignore is not None:
            self._values["nx_ignore"] = nx_ignore
        if target_defaults is not None:
            self._values["target_defaults"] = target_defaults
        if target_dependencies is not None:
            self._values["target_dependencies"] = target_dependencies

    @builtins.property
    def affected_branch(self) -> typing.Optional[builtins.str]:
        '''Affected branch.

        :default: mainline
        '''
        result = self._values.get("affected_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cacheable_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Defines the list of targets/operations that are cached by Nx.

        :default: ["build", "test"]

        :see: https://nx.dev/reference/nx-json#tasks-runner-options
        '''
        result = self._values.get("cacheable_operations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def implicit_dependencies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        '''Configuration for Implicit Dependencies.

        :see: https://nx.dev/configuration/packagejson#implicitdependencies
        '''
        result = self._values.get("implicit_dependencies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

    @builtins.property
    def named_inputs(self) -> typing.Optional[NamedInputs]:
        '''Named inputs.

        :see: https://nx.dev/reference/nx-json#inputs-&-namedinputs
        '''
        result = self._values.get("named_inputs")
        return typing.cast(typing.Optional[NamedInputs], result)

    @builtins.property
    def nx_cloud_read_only_access_token(self) -> typing.Optional[builtins.str]:
        '''Read only access token if enabling nx cloud.'''
        result = self._values.get("nx_cloud_read_only_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nx_ignore(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of patterns to include in the .nxignore file.

        :see: https://nx.dev/configuration/packagejson#nxignore
        '''
        result = self._values.get("nx_ignore")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_defaults(self) -> typing.Optional[TargetDefaults]:
        '''Target defaults.

        :see: https://nx.dev/reference/nx-json#target-defaults
        '''
        result = self._values.get("target_defaults")
        return typing.cast(typing.Optional[TargetDefaults], result)

    @builtins.property
    def target_dependencies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.List[TargetDependency]]]:
        '''Configuration for TargetDependencies.

        :see: https://nx.dev/configuration/packagejson#target-dependencies
        '''
        result = self._values.get("target_dependencies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.List[TargetDependency]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NamedInputs",
    "ProjectConfig",
    "ProjectTarget",
    "TargetDefaults",
    "TargetDependency",
    "TargetDependencyProject",
    "WorkspaceConfig",
]

publication.publish()
