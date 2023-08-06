'''
# `gitlab_group_share_group`

Refer to the Terraform Registory for docs: [`gitlab_group_share_group`](https://www.terraform.io/docs/providers/gitlab/r/group_share_group).
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


class GroupShareGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.groupShareGroup.GroupShareGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group gitlab_group_share_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        group_access: builtins.str,
        group_id: builtins.str,
        share_group_id: jsii.Number,
        expires_at: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group gitlab_group_share_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_access: The access level to grant the group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_access GroupShareGroup#group_access}
        :param group_id: The id of the main group to be shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_id GroupShareGroup#group_id}
        :param share_group_id: The id of the additional group with which the main group will be shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#share_group_id GroupShareGroup#share_group_id}
        :param expires_at: Share expiration date. Format: ``YYYY-MM-DD``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#expires_at GroupShareGroup#expires_at}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#id GroupShareGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6715aead6778f3752dfac2c258708e5ccf5e095185812d5b8664b91c600fab54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupShareGroupConfig(
            group_access=group_access,
            group_id=group_id,
            share_group_id=share_group_id,
            expires_at=expires_at,
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

    @jsii.member(jsii_name="resetExpiresAt")
    def reset_expires_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiresAt", []))

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
    @jsii.member(jsii_name="expiresAtInput")
    def expires_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresAtInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAccessInput")
    def group_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="shareGroupIdInput")
    def share_group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shareGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresAt"))

    @expires_at.setter
    def expires_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd758f2f3b303c2fce70ee5fc299f5d914495523ba01f8878a91e197cf62a01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresAt", value)

    @builtins.property
    @jsii.member(jsii_name="groupAccess")
    def group_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAccess"))

    @group_access.setter
    def group_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c614ea5e6df12efa66861ffd497474c367ef3a70552059238ef05b3888a9915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAccess", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6373c88802040272db70a6bfa47d3c49435af641f028e644b3417b688fa81aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab37bfe5704ddb0f8997adcea9f22084781c75579f2e25f4c8b156cdebf0cdf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="shareGroupId")
    def share_group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shareGroupId"))

    @share_group_id.setter
    def share_group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02cf25ebd06e851a26b38bcd08af2b7501f24e5feadfdf72452d16458c8f67b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareGroupId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.groupShareGroup.GroupShareGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_access": "groupAccess",
        "group_id": "groupId",
        "share_group_id": "shareGroupId",
        "expires_at": "expiresAt",
        "id": "id",
    },
)
class GroupShareGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_access: builtins.str,
        group_id: builtins.str,
        share_group_id: jsii.Number,
        expires_at: typing.Optional[builtins.str] = None,
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
        :param group_access: The access level to grant the group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_access GroupShareGroup#group_access}
        :param group_id: The id of the main group to be shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_id GroupShareGroup#group_id}
        :param share_group_id: The id of the additional group with which the main group will be shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#share_group_id GroupShareGroup#share_group_id}
        :param expires_at: Share expiration date. Format: ``YYYY-MM-DD``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#expires_at GroupShareGroup#expires_at}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#id GroupShareGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99aa2f6274d4575c3ff2c15b7e905531b53c98790f9917f1189bba87e4820efd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_access", value=group_access, expected_type=type_hints["group_access"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument share_group_id", value=share_group_id, expected_type=type_hints["share_group_id"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_access": group_access,
            "group_id": group_id,
            "share_group_id": share_group_id,
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
        if expires_at is not None:
            self._values["expires_at"] = expires_at
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
    def group_access(self) -> builtins.str:
        '''The access level to grant the group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_access GroupShareGroup#group_access}
        '''
        result = self._values.get("group_access")
        assert result is not None, "Required property 'group_access' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The id of the main group to be shared.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#group_id GroupShareGroup#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_group_id(self) -> jsii.Number:
        '''The id of the additional group with which the main group will be shared.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#share_group_id GroupShareGroup#share_group_id}
        '''
        result = self._values.get("share_group_id")
        assert result is not None, "Required property 'share_group_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''Share expiration date. Format: ``YYYY-MM-DD``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#expires_at GroupShareGroup#expires_at}
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_share_group#id GroupShareGroup#id}.

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
        return "GroupShareGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupShareGroup",
    "GroupShareGroupConfig",
]

publication.publish()

def _typecheckingstub__6715aead6778f3752dfac2c258708e5ccf5e095185812d5b8664b91c600fab54(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    group_access: builtins.str,
    group_id: builtins.str,
    share_group_id: jsii.Number,
    expires_at: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4cd758f2f3b303c2fce70ee5fc299f5d914495523ba01f8878a91e197cf62a01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c614ea5e6df12efa66861ffd497474c367ef3a70552059238ef05b3888a9915(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6373c88802040272db70a6bfa47d3c49435af641f028e644b3417b688fa81aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab37bfe5704ddb0f8997adcea9f22084781c75579f2e25f4c8b156cdebf0cdf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02cf25ebd06e851a26b38bcd08af2b7501f24e5feadfdf72452d16458c8f67b5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99aa2f6274d4575c3ff2c15b7e905531b53c98790f9917f1189bba87e4820efd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    group_access: builtins.str,
    group_id: builtins.str,
    share_group_id: jsii.Number,
    expires_at: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
