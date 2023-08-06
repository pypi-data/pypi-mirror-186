'''
# `gitlab_project_protected_environment`

Refer to the Terraform Registory for docs: [`gitlab_project_protected_environment`](https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class ProjectProtectedEnvironment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectProtectedEnvironment.ProjectProtectedEnvironment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment gitlab_project_protected_environment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        deploy_access_levels: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectProtectedEnvironmentDeployAccessLevels", typing.Dict[builtins.str, typing.Any]]]],
        environment: builtins.str,
        project: builtins.str,
        id: typing.Optional[builtins.str] = None,
        required_approval_count: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment gitlab_project_protected_environment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param deploy_access_levels: deploy_access_levels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#deploy_access_levels ProjectProtectedEnvironment#deploy_access_levels}
        :param environment: The name of the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#environment ProjectProtectedEnvironment#environment}
        :param project: The ID or full path of the project which the protected environment is created against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#project ProjectProtectedEnvironment#project}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#id ProjectProtectedEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param required_approval_count: The number of approvals required to deploy to this environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#required_approval_count ProjectProtectedEnvironment#required_approval_count}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4e2d8c459953a985f206eca27f73a12df2bfd52f7a32966bdd9827002065dd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectProtectedEnvironmentConfig(
            deploy_access_levels=deploy_access_levels,
            environment=environment,
            project=project,
            id=id,
            required_approval_count=required_approval_count,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeployAccessLevels")
    def put_deploy_access_levels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectProtectedEnvironmentDeployAccessLevels", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67451726529357dc5808ff52d06e2ce54647a35a61ed1ca4982748c5cbf70ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployAccessLevels", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRequiredApprovalCount")
    def reset_required_approval_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredApprovalCount", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="deployAccessLevels")
    def deploy_access_levels(
        self,
    ) -> "ProjectProtectedEnvironmentDeployAccessLevelsList":
        return typing.cast("ProjectProtectedEnvironmentDeployAccessLevelsList", jsii.get(self, "deployAccessLevels"))

    @builtins.property
    @jsii.member(jsii_name="deployAccessLevelsInput")
    def deploy_access_levels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectProtectedEnvironmentDeployAccessLevels"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectProtectedEnvironmentDeployAccessLevels"]]], jsii.get(self, "deployAccessLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredApprovalCountInput")
    def required_approval_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requiredApprovalCountInput"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__944749d49f3aa110b14bfbd832e118a4aa0757d22c8f2ac22e79cc92ecf3bf63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eb97f9d36f02ee80ee3b8308ead25039456ff4d73f87898b473b9f95399441d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b4182a6980c0c06c26eb65d600fb786d31e18adbd0fe8379a7190bf40cd779)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="requiredApprovalCount")
    def required_approval_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requiredApprovalCount"))

    @required_approval_count.setter
    def required_approval_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8298e5777186e69780ae1b0cde3917d48b24665d4b8fc0cf72723aa207a2b6c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredApprovalCount", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectProtectedEnvironment.ProjectProtectedEnvironmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "deploy_access_levels": "deployAccessLevels",
        "environment": "environment",
        "project": "project",
        "id": "id",
        "required_approval_count": "requiredApprovalCount",
    },
)
class ProjectProtectedEnvironmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        deploy_access_levels: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ProjectProtectedEnvironmentDeployAccessLevels", typing.Dict[builtins.str, typing.Any]]]],
        environment: builtins.str,
        project: builtins.str,
        id: typing.Optional[builtins.str] = None,
        required_approval_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param deploy_access_levels: deploy_access_levels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#deploy_access_levels ProjectProtectedEnvironment#deploy_access_levels}
        :param environment: The name of the environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#environment ProjectProtectedEnvironment#environment}
        :param project: The ID or full path of the project which the protected environment is created against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#project ProjectProtectedEnvironment#project}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#id ProjectProtectedEnvironment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param required_approval_count: The number of approvals required to deploy to this environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#required_approval_count ProjectProtectedEnvironment#required_approval_count}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66951fd875db7a4ca321f49b4534580ff863549f237945b60fa64a17474bbd3a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument deploy_access_levels", value=deploy_access_levels, expected_type=type_hints["deploy_access_levels"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument required_approval_count", value=required_approval_count, expected_type=type_hints["required_approval_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deploy_access_levels": deploy_access_levels,
            "environment": environment,
            "project": project,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id
        if required_approval_count is not None:
            self._values["required_approval_count"] = required_approval_count

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def deploy_access_levels(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectProtectedEnvironmentDeployAccessLevels"]]:
        '''deploy_access_levels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#deploy_access_levels ProjectProtectedEnvironment#deploy_access_levels}
        '''
        result = self._values.get("deploy_access_levels")
        assert result is not None, "Required property 'deploy_access_levels' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ProjectProtectedEnvironmentDeployAccessLevels"]], result)

    @builtins.property
    def environment(self) -> builtins.str:
        '''The name of the environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#environment ProjectProtectedEnvironment#environment}
        '''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The ID or full path of the project which the protected environment is created against.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#project ProjectProtectedEnvironment#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#id ProjectProtectedEnvironment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required_approval_count(self) -> typing.Optional[jsii.Number]:
        '''The number of approvals required to deploy to this environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#required_approval_count ProjectProtectedEnvironment#required_approval_count}
        '''
        result = self._values.get("required_approval_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectProtectedEnvironmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectProtectedEnvironment.ProjectProtectedEnvironmentDeployAccessLevels",
    jsii_struct_bases=[],
    name_mapping={
        "access_level": "accessLevel",
        "group_id": "groupId",
        "user_id": "userId",
    },
)
class ProjectProtectedEnvironmentDeployAccessLevels:
    def __init__(
        self,
        *,
        access_level: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[jsii.Number] = None,
        user_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param access_level: Levels of access required to deploy to this protected environment. Valid values are ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#access_level ProjectProtectedEnvironment#access_level}
        :param group_id: The ID of the group allowed to deploy to this protected environment. The project must be shared with the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#group_id ProjectProtectedEnvironment#group_id}
        :param user_id: The ID of the user allowed to deploy to this protected environment. The user must be a member of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#user_id ProjectProtectedEnvironment#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c8f5cc4bfd2017180fa82b990922973cf7b2053d1dddf4c0f0fb28d3fa2e12)
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_level is not None:
            self._values["access_level"] = access_level
        if group_id is not None:
            self._values["group_id"] = group_id
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def access_level(self) -> typing.Optional[builtins.str]:
        '''Levels of access required to deploy to this protected environment. Valid values are ``developer``, ``maintainer``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#access_level ProjectProtectedEnvironment#access_level}
        '''
        result = self._values.get("access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the group allowed to deploy to this protected environment.

        The project must be shared with the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#group_id ProjectProtectedEnvironment#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the user allowed to deploy to this protected environment.

        The user must be a member of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_protected_environment#user_id ProjectProtectedEnvironment#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectProtectedEnvironmentDeployAccessLevels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectProtectedEnvironmentDeployAccessLevelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectProtectedEnvironment.ProjectProtectedEnvironmentDeployAccessLevelsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea666d1a92e969228b5c79a075806457bcb2bc7c55bafaecd3e2aa14c47db852)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ProjectProtectedEnvironmentDeployAccessLevelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c640651262159ff935cdceeba5ee614177cb576d87f25b14b67ac891562384)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectProtectedEnvironmentDeployAccessLevelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ad826e0a9a837857d2ad3d913d9910acf5421f0a2cc0707b8c885188eaba6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6cceafe613df26483282d204509ba65632679e0facde40c7bf038514e758f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53dcef2f6bac715665239ea7742246f30bb82f96c017e96d6c6538bd7a6b4d09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectProtectedEnvironmentDeployAccessLevels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectProtectedEnvironmentDeployAccessLevels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectProtectedEnvironmentDeployAccessLevels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7d96f0046eeda0acfe31fc94a0d19e24282d0ba7045fd47f45f6b60d41b6a34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectProtectedEnvironmentDeployAccessLevelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectProtectedEnvironment.ProjectProtectedEnvironmentDeployAccessLevelsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe8327715e969945890fe9a3490333f2c2567c98ab352afb7dd940f937933d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessLevel")
    def reset_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevel", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevelDescription")
    def access_level_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevelDescription"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d45e75be923c3ab3b2c69a5ec604eb933af947b2387af3797acba73b2532e30d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbeb1c98021a9b4db0a56dbabca887ccf6fbd1db90ee1ce7394047beee7c8a11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47baf8191cadbf3e759284ab309750f46981caacad0033168896d8423ff2977b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeef85011c620205c8757d157716207dd8c98347d9dc5d51fd7205c415d60f28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ProjectProtectedEnvironment",
    "ProjectProtectedEnvironmentConfig",
    "ProjectProtectedEnvironmentDeployAccessLevels",
    "ProjectProtectedEnvironmentDeployAccessLevelsList",
    "ProjectProtectedEnvironmentDeployAccessLevelsOutputReference",
]

publication.publish()

def _typecheckingstub__9e4e2d8c459953a985f206eca27f73a12df2bfd52f7a32966bdd9827002065dd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    deploy_access_levels: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, typing.Dict[builtins.str, typing.Any]]]],
    environment: builtins.str,
    project: builtins.str,
    id: typing.Optional[builtins.str] = None,
    required_approval_count: typing.Optional[jsii.Number] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67451726529357dc5808ff52d06e2ce54647a35a61ed1ca4982748c5cbf70ab2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__944749d49f3aa110b14bfbd832e118a4aa0757d22c8f2ac22e79cc92ecf3bf63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb97f9d36f02ee80ee3b8308ead25039456ff4d73f87898b473b9f95399441d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b4182a6980c0c06c26eb65d600fb786d31e18adbd0fe8379a7190bf40cd779(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8298e5777186e69780ae1b0cde3917d48b24665d4b8fc0cf72723aa207a2b6c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66951fd875db7a4ca321f49b4534580ff863549f237945b60fa64a17474bbd3a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    deploy_access_levels: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, typing.Dict[builtins.str, typing.Any]]]],
    environment: builtins.str,
    project: builtins.str,
    id: typing.Optional[builtins.str] = None,
    required_approval_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c8f5cc4bfd2017180fa82b990922973cf7b2053d1dddf4c0f0fb28d3fa2e12(
    *,
    access_level: typing.Optional[builtins.str] = None,
    group_id: typing.Optional[jsii.Number] = None,
    user_id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea666d1a92e969228b5c79a075806457bcb2bc7c55bafaecd3e2aa14c47db852(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c640651262159ff935cdceeba5ee614177cb576d87f25b14b67ac891562384(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ad826e0a9a837857d2ad3d913d9910acf5421f0a2cc0707b8c885188eaba6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6cceafe613df26483282d204509ba65632679e0facde40c7bf038514e758f7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53dcef2f6bac715665239ea7742246f30bb82f96c017e96d6c6538bd7a6b4d09(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d96f0046eeda0acfe31fc94a0d19e24282d0ba7045fd47f45f6b60d41b6a34(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ProjectProtectedEnvironmentDeployAccessLevels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe8327715e969945890fe9a3490333f2c2567c98ab352afb7dd940f937933d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d45e75be923c3ab3b2c69a5ec604eb933af947b2387af3797acba73b2532e30d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbeb1c98021a9b4db0a56dbabca887ccf6fbd1db90ee1ce7394047beee7c8a11(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47baf8191cadbf3e759284ab309750f46981caacad0033168896d8423ff2977b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeef85011c620205c8757d157716207dd8c98347d9dc5d51fd7205c415d60f28(
    value: typing.Optional[typing.Union[ProjectProtectedEnvironmentDeployAccessLevels, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
