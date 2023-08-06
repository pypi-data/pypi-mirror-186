'''
# `gitlab_pipeline_schedule`

Refer to the Terraform Registory for docs: [`gitlab_pipeline_schedule`](https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule).
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


class PipelineSchedule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.pipelineSchedule.PipelineSchedule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule gitlab_pipeline_schedule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cron: builtins.str,
        description: builtins.str,
        project: builtins.str,
        ref: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cron_timezone: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule gitlab_pipeline_schedule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cron: The cron (e.g. ``0 1 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron PipelineSchedule#cron}
        :param description: The description of the pipeline schedule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#description PipelineSchedule#description}
        :param project: The name or id of the project to add the schedule to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#project PipelineSchedule#project}
        :param ref: The branch/tag name to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#ref PipelineSchedule#ref}
        :param active: The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#active PipelineSchedule#active}
        :param cron_timezone: The timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron_timezone PipelineSchedule#cron_timezone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#id PipelineSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9484e102bd10cc60b49f7e2c5616a547ab9cbef887a79ef102d4b6a8eec622b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PipelineScheduleConfig(
            cron=cron,
            description=description,
            project=project,
            ref=ref,
            active=active,
            cron_timezone=cron_timezone,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetCronTimezone")
    def reset_cron_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCronTimezone", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="cronInput")
    def cron_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronInput"))

    @builtins.property
    @jsii.member(jsii_name="cronTimezoneInput")
    def cron_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f22bff0142c7fbc43e7c293ad15baae637b9dbbe5d1c8d51dfb6412135f8adf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="cron")
    def cron(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cron"))

    @cron.setter
    def cron(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9db34e928e292c57a088673cceb2772a68209e8702f237bc663349d07ca9daf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cron", value)

    @builtins.property
    @jsii.member(jsii_name="cronTimezone")
    def cron_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronTimezone"))

    @cron_timezone.setter
    def cron_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a07d1e6bff12c9df89eb6184c039f5803eb7691cae2b545fc94f0e1a710fa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e3c247d374c006f932db88c402ca18446cff9e565784a87383fb3f68b000d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48651672e0483b0735aee6c2d814248697dbbe02923f047d46881d23abe06cd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cd085a54e10acd91efe3e9c7007dbbe68dcc616a2cfa4d24df87e2d2c3ff1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5be2bdde69ad36e39274a88b8050758aeec812b747eb6565595740165585c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.pipelineSchedule.PipelineScheduleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cron": "cron",
        "description": "description",
        "project": "project",
        "ref": "ref",
        "active": "active",
        "cron_timezone": "cronTimezone",
        "id": "id",
    },
)
class PipelineScheduleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cron: builtins.str,
        description: builtins.str,
        project: builtins.str,
        ref: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cron_timezone: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cron: The cron (e.g. ``0 1 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron PipelineSchedule#cron}
        :param description: The description of the pipeline schedule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#description PipelineSchedule#description}
        :param project: The name or id of the project to add the schedule to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#project PipelineSchedule#project}
        :param ref: The branch/tag name to be triggered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#ref PipelineSchedule#ref}
        :param active: The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#active PipelineSchedule#active}
        :param cron_timezone: The timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron_timezone PipelineSchedule#cron_timezone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#id PipelineSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc8d96c9653945af7890ff3b1580e06d8f78e549bc0c291ddde5ac5a8183a40)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cron", value=cron, expected_type=type_hints["cron"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument cron_timezone", value=cron_timezone, expected_type=type_hints["cron_timezone"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cron": cron,
            "description": description,
            "project": project,
            "ref": ref,
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
        if active is not None:
            self._values["active"] = active
        if cron_timezone is not None:
            self._values["cron_timezone"] = cron_timezone
        if id is not None:
            self._values["id"] = id

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
    def cron(self) -> builtins.str:
        '''The cron (e.g. ``0 1 * * *``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron PipelineSchedule#cron}
        '''
        result = self._values.get("cron")
        assert result is not None, "Required property 'cron' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the pipeline schedule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#description PipelineSchedule#description}
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or id of the project to add the schedule to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#project PipelineSchedule#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ref(self) -> builtins.str:
        '''The branch/tag name to be triggered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#ref PipelineSchedule#ref}
        '''
        result = self._values.get("ref")
        assert result is not None, "Required property 'ref' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#active PipelineSchedule#active}
        '''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cron_timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#cron_timezone PipelineSchedule#cron_timezone}
        '''
        result = self._values.get("cron_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/pipeline_schedule#id PipelineSchedule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineScheduleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PipelineSchedule",
    "PipelineScheduleConfig",
]

publication.publish()

def _typecheckingstub__f9484e102bd10cc60b49f7e2c5616a547ab9cbef887a79ef102d4b6a8eec622b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cron: builtins.str,
    description: builtins.str,
    project: builtins.str,
    ref: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cron_timezone: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f22bff0142c7fbc43e7c293ad15baae637b9dbbe5d1c8d51dfb6412135f8adf5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9db34e928e292c57a088673cceb2772a68209e8702f237bc663349d07ca9daf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a07d1e6bff12c9df89eb6184c039f5803eb7691cae2b545fc94f0e1a710fa6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e3c247d374c006f932db88c402ca18446cff9e565784a87383fb3f68b000d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48651672e0483b0735aee6c2d814248697dbbe02923f047d46881d23abe06cd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cd085a54e10acd91efe3e9c7007dbbe68dcc616a2cfa4d24df87e2d2c3ff1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5be2bdde69ad36e39274a88b8050758aeec812b747eb6565595740165585c8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc8d96c9653945af7890ff3b1580e06d8f78e549bc0c291ddde5ac5a8183a40(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cron: builtins.str,
    description: builtins.str,
    project: builtins.str,
    ref: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cron_timezone: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
