'''
# `gitlab_project_freeze_period`

Refer to the Terraform Registory for docs: [`gitlab_project_freeze_period`](https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period).
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


class ProjectFreezePeriod(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectFreezePeriod.ProjectFreezePeriod",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period gitlab_project_freeze_period}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        freeze_end: builtins.str,
        freeze_start: builtins.str,
        project_id: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period gitlab_project_freeze_period} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param freeze_end: End of the Freeze Period in cron format (e.g. ``0 2 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_end ProjectFreezePeriod#freeze_end}
        :param freeze_start: Start of the Freeze Period in cron format (e.g. ``0 1 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_start ProjectFreezePeriod#freeze_start}
        :param project_id: The id of the project to add the schedule to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#project_id ProjectFreezePeriod#project_id}
        :param cron_timezone: The timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#cron_timezone ProjectFreezePeriod#cron_timezone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#id ProjectFreezePeriod#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57eecec7135a9ffb1396f09f7bba01322e40c885144536d29188859e041317d0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectFreezePeriodConfig(
            freeze_end=freeze_end,
            freeze_start=freeze_start,
            project_id=project_id,
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
    @jsii.member(jsii_name="cronTimezoneInput")
    def cron_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="freezeEndInput")
    def freeze_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "freezeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="freezeStartInput")
    def freeze_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "freezeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cronTimezone")
    def cron_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronTimezone"))

    @cron_timezone.setter
    def cron_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860cb161b8aaca9319534e1e73969c4105c9437fc082f6328733c03ddef96da4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="freezeEnd")
    def freeze_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "freezeEnd"))

    @freeze_end.setter
    def freeze_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcdafa0a0852e687059085745e55336e0f524bca5d9b3764878b6fc6379875b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "freezeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="freezeStart")
    def freeze_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "freezeStart"))

    @freeze_start.setter
    def freeze_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62066c3ce2feb37c093f9142d055565863f5a24e53dfe2f7be4fda74429d7699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "freezeStart", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__180a9fa80e650529a6f25e6aab2465c66ebe9b7a256e9b0c424da9e1a6ec066c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3c5bf8e1b467873e76da21c0d552fac685f617b01136f17fd1f4684c8ee276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectFreezePeriod.ProjectFreezePeriodConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "freeze_end": "freezeEnd",
        "freeze_start": "freezeStart",
        "project_id": "projectId",
        "cron_timezone": "cronTimezone",
        "id": "id",
    },
)
class ProjectFreezePeriodConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        freeze_end: builtins.str,
        freeze_start: builtins.str,
        project_id: builtins.str,
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
        :param freeze_end: End of the Freeze Period in cron format (e.g. ``0 2 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_end ProjectFreezePeriod#freeze_end}
        :param freeze_start: Start of the Freeze Period in cron format (e.g. ``0 1 * * *``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_start ProjectFreezePeriod#freeze_start}
        :param project_id: The id of the project to add the schedule to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#project_id ProjectFreezePeriod#project_id}
        :param cron_timezone: The timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#cron_timezone ProjectFreezePeriod#cron_timezone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#id ProjectFreezePeriod#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c216c0d8efb05eb5dd9d5088bc6a6c54959830b59647cf886e65398d23f955a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument freeze_end", value=freeze_end, expected_type=type_hints["freeze_end"])
            check_type(argname="argument freeze_start", value=freeze_start, expected_type=type_hints["freeze_start"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument cron_timezone", value=cron_timezone, expected_type=type_hints["cron_timezone"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "freeze_end": freeze_end,
            "freeze_start": freeze_start,
            "project_id": project_id,
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
    def freeze_end(self) -> builtins.str:
        '''End of the Freeze Period in cron format (e.g. ``0 2 * * *``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_end ProjectFreezePeriod#freeze_end}
        '''
        result = self._values.get("freeze_end")
        assert result is not None, "Required property 'freeze_end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def freeze_start(self) -> builtins.str:
        '''Start of the Freeze Period in cron format (e.g. ``0 1 * * *``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#freeze_start ProjectFreezePeriod#freeze_start}
        '''
        result = self._values.get("freeze_start")
        assert result is not None, "Required property 'freeze_start' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The id of the project to add the schedule to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#project_id ProjectFreezePeriod#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cron_timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#cron_timezone ProjectFreezePeriod#cron_timezone}
        '''
        result = self._values.get("cron_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_freeze_period#id ProjectFreezePeriod#id}.

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
        return "ProjectFreezePeriodConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectFreezePeriod",
    "ProjectFreezePeriodConfig",
]

publication.publish()

def _typecheckingstub__57eecec7135a9ffb1396f09f7bba01322e40c885144536d29188859e041317d0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    freeze_end: builtins.str,
    freeze_start: builtins.str,
    project_id: builtins.str,
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

def _typecheckingstub__860cb161b8aaca9319534e1e73969c4105c9437fc082f6328733c03ddef96da4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdafa0a0852e687059085745e55336e0f524bca5d9b3764878b6fc6379875b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62066c3ce2feb37c093f9142d055565863f5a24e53dfe2f7be4fda74429d7699(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__180a9fa80e650529a6f25e6aab2465c66ebe9b7a256e9b0c424da9e1a6ec066c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3c5bf8e1b467873e76da21c0d552fac685f617b01136f17fd1f4684c8ee276(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c216c0d8efb05eb5dd9d5088bc6a6c54959830b59647cf886e65398d23f955a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    freeze_end: builtins.str,
    freeze_start: builtins.str,
    project_id: builtins.str,
    cron_timezone: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
