'''
# `gitlab_project_variable`

Refer to the Terraform Registory for docs: [`gitlab_project_variable`](https://www.terraform.io/docs/providers/gitlab/r/project_variable).
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


class ProjectVariable(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectVariable.ProjectVariable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable gitlab_project_variable}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        key: builtins.str,
        project: builtins.str,
        value: builtins.str,
        environment_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        masked: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        protected: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        variable_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable gitlab_project_variable} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param key: The name of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#key ProjectVariable#key}
        :param project: The name or id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#project ProjectVariable#project}
        :param value: The value of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#value ProjectVariable#value}
        :param environment_scope: The environment scope of the variable. Defaults to all environment (``*``). Note that in Community Editions of Gitlab, values other than ``*`` will cause inconsistent plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#environment_scope ProjectVariable#environment_scope}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#id ProjectVariable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param masked: If set to ``true``, the value of the variable will be hidden in job logs. The value must meet the `masking requirements <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#masked ProjectVariable#masked}
        :param protected: If set to ``true``, the variable will be passed only to pipelines running on protected branches and tags. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#protected ProjectVariable#protected}
        :param variable_type: The type of a variable. Valid values are: ``env_var``, ``file``. Default is ``env_var``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#variable_type ProjectVariable#variable_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba36e6cae0b6f75c25ff019eb03c933de8f32adca3dc43ef3badc2d5418a512)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectVariableConfig(
            key=key,
            project=project,
            value=value,
            environment_scope=environment_scope,
            id=id,
            masked=masked,
            protected=protected,
            variable_type=variable_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEnvironmentScope")
    def reset_environment_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentScope", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMasked")
    def reset_masked(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasked", []))

    @jsii.member(jsii_name="resetProtected")
    def reset_protected(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtected", []))

    @jsii.member(jsii_name="resetVariableType")
    def reset_variable_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariableType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="environmentScopeInput")
    def environment_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="maskedInput")
    def masked_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "maskedInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedInput")
    def protected_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "protectedInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="variableTypeInput")
    def variable_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentScope")
    def environment_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentScope"))

    @environment_scope.setter
    def environment_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f036c737cd52a286ed4c62ce0040a00f07e9d7d4fc7e95f1ae845795d85aea49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentScope", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef0af27c431e1954a47f96910551e3dc07aa93af4c4b0c81e2032a282e1d8583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eeade47e05d9534c93d8adbce4a8841ee3ea38499655d56a8a6ad133fe9a6fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="masked")
    def masked(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "masked"))

    @masked.setter
    def masked(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce4b1e9571b8228468fb2f3d7d1e623210e6f66428ce0bb45cf02dab8dcc23a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masked", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c7b64c08a6fe4cd9efead43ce911b110cb426305b08efa77209d24ed572e06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="protected")
    def protected(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "protected"))

    @protected.setter
    def protected(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1065a81d44dd6c76119eff1fca89afdeb4d2eac2ad8e0b5227c15dd57061e8a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protected", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05605a51ec857c968029a7b97a1a113a287fec901195cf94b4399082b6a2881c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="variableType")
    def variable_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variableType"))

    @variable_type.setter
    def variable_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64fee082ae862656a35c8767aa7fefc49221b17e62129ec32d72124b253fefb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variableType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectVariable.ProjectVariableConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "key": "key",
        "project": "project",
        "value": "value",
        "environment_scope": "environmentScope",
        "id": "id",
        "masked": "masked",
        "protected": "protected",
        "variable_type": "variableType",
    },
)
class ProjectVariableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        key: builtins.str,
        project: builtins.str,
        value: builtins.str,
        environment_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        masked: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        protected: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param key: The name of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#key ProjectVariable#key}
        :param project: The name or id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#project ProjectVariable#project}
        :param value: The value of the variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#value ProjectVariable#value}
        :param environment_scope: The environment scope of the variable. Defaults to all environment (``*``). Note that in Community Editions of Gitlab, values other than ``*`` will cause inconsistent plans. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#environment_scope ProjectVariable#environment_scope}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#id ProjectVariable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param masked: If set to ``true``, the value of the variable will be hidden in job logs. The value must meet the `masking requirements <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#masked ProjectVariable#masked}
        :param protected: If set to ``true``, the variable will be passed only to pipelines running on protected branches and tags. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#protected ProjectVariable#protected}
        :param variable_type: The type of a variable. Valid values are: ``env_var``, ``file``. Default is ``env_var``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#variable_type ProjectVariable#variable_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1515fcfc1160edca023ea3bf55c5ed4b0851c79d4664c3aeaafd91dc0407ca6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument environment_scope", value=environment_scope, expected_type=type_hints["environment_scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument masked", value=masked, expected_type=type_hints["masked"])
            check_type(argname="argument protected", value=protected, expected_type=type_hints["protected"])
            check_type(argname="argument variable_type", value=variable_type, expected_type=type_hints["variable_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "project": project,
            "value": value,
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
        if environment_scope is not None:
            self._values["environment_scope"] = environment_scope
        if id is not None:
            self._values["id"] = id
        if masked is not None:
            self._values["masked"] = masked
        if protected is not None:
            self._values["protected"] = protected
        if variable_type is not None:
            self._values["variable_type"] = variable_type

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
    def key(self) -> builtins.str:
        '''The name of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#key ProjectVariable#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or id of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#project ProjectVariable#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#value ProjectVariable#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_scope(self) -> typing.Optional[builtins.str]:
        '''The environment scope of the variable.

        Defaults to all environment (``*``). Note that in Community Editions of Gitlab, values other than ``*`` will cause inconsistent plans.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#environment_scope ProjectVariable#environment_scope}
        '''
        result = self._values.get("environment_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#id ProjectVariable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def masked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to ``true``, the value of the variable will be hidden in job logs.

        The value must meet the `masking requirements <https://docs.gitlab.com/ee/ci/variables/#masked-variables>`_. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#masked ProjectVariable#masked}
        '''
        result = self._values.get("masked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If set to ``true``, the variable will be passed only to pipelines running on protected branches and tags.

        Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#protected ProjectVariable#protected}
        '''
        result = self._values.get("protected")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''The type of a variable. Valid values are: ``env_var``, ``file``. Default is ``env_var``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_variable#variable_type ProjectVariable#variable_type}
        '''
        result = self._values.get("variable_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectVariableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectVariable",
    "ProjectVariableConfig",
]

publication.publish()

def _typecheckingstub__dba36e6cae0b6f75c25ff019eb03c933de8f32adca3dc43ef3badc2d5418a512(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    key: builtins.str,
    project: builtins.str,
    value: builtins.str,
    environment_scope: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    masked: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    protected: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    variable_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f036c737cd52a286ed4c62ce0040a00f07e9d7d4fc7e95f1ae845795d85aea49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef0af27c431e1954a47f96910551e3dc07aa93af4c4b0c81e2032a282e1d8583(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eeade47e05d9534c93d8adbce4a8841ee3ea38499655d56a8a6ad133fe9a6fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce4b1e9571b8228468fb2f3d7d1e623210e6f66428ce0bb45cf02dab8dcc23a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c7b64c08a6fe4cd9efead43ce911b110cb426305b08efa77209d24ed572e06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1065a81d44dd6c76119eff1fca89afdeb4d2eac2ad8e0b5227c15dd57061e8a2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05605a51ec857c968029a7b97a1a113a287fec901195cf94b4399082b6a2881c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64fee082ae862656a35c8767aa7fefc49221b17e62129ec32d72124b253fefb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1515fcfc1160edca023ea3bf55c5ed4b0851c79d4664c3aeaafd91dc0407ca6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    key: builtins.str,
    project: builtins.str,
    value: builtins.str,
    environment_scope: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    masked: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    protected: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
