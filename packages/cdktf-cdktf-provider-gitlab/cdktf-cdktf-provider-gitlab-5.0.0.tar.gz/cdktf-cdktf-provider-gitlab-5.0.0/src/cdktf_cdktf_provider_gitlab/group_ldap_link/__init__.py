'''
# `gitlab_group_ldap_link`

Refer to the Terraform Registory for docs: [`gitlab_group_ldap_link`](https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link).
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


class GroupLdapLink(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.groupLdapLink.GroupLdapLink",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link gitlab_group_ldap_link}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cn: builtins.str,
        group_id: builtins.str,
        ldap_provider: builtins.str,
        access_level: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group_access: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link gitlab_group_ldap_link} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cn: The CN of the LDAP group to link with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#cn GroupLdapLink#cn}
        :param group_id: The id of the GitLab group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_id GroupLdapLink#group_id}
        :param ldap_provider: The name of the LDAP provider as stored in the GitLab database. Note that this is NOT the value of the ``label`` attribute as shown in the web UI. In most cases this will be ``ldapmain`` but you may use the `LDAP check rake task <https://docs.gitlab.com/ee/administration/raketasks/ldap.html#check>`_ for receiving the LDAP server name: ``LDAP: ... Server: ldapmain`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#ldap_provider GroupLdapLink#ldap_provider}
        :param access_level: Minimum access level for members of the LDAP group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#access_level GroupLdapLink#access_level}
        :param force: If true, then delete and replace an existing LDAP link if one exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#force GroupLdapLink#force}
        :param group_access: Minimum access level for members of the LDAP group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_access GroupLdapLink#group_access}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#id GroupLdapLink#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9691e9e3a9a8cb94b4f96dea273d1cbdad288d5724c7487df05d6473eadea680)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupLdapLinkConfig(
            cn=cn,
            group_id=group_id,
            ldap_provider=ldap_provider,
            access_level=access_level,
            force=force,
            group_access=group_access,
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

    @jsii.member(jsii_name="resetAccessLevel")
    def reset_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevel", []))

    @jsii.member(jsii_name="resetForce")
    def reset_force(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForce", []))

    @jsii.member(jsii_name="resetGroupAccess")
    def reset_group_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupAccess", []))

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
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="cnInput")
    def cn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnInput"))

    @builtins.property
    @jsii.member(jsii_name="forceInput")
    def force_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceInput"))

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
    @jsii.member(jsii_name="ldapProviderInput")
    def ldap_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ldapProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7087e707e7ee69a3aa0e00359afb46eecd32746e1052e0f01e4c6975dd0470f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="cn")
    def cn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cn"))

    @cn.setter
    def cn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c18895ac4587b72dbae14a9e9cd34ba965f90cb13edcb28896ec5ff6448e8f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cn", value)

    @builtins.property
    @jsii.member(jsii_name="force")
    def force(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "force"))

    @force.setter
    def force(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d33637f26b88784fead2ed76ed157470fafb5e371667efd3729f8c3057a2533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "force", value)

    @builtins.property
    @jsii.member(jsii_name="groupAccess")
    def group_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupAccess"))

    @group_access.setter
    def group_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c03ef467cafb4f2305f98e16a909b0982b4a4b740fb206803ab179a361edc89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAccess", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f4bc74cf48c9f3995ba20076c29f3caa0cd419983df43bc7f205a72a3ef355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42bf4f354d281472acf98ad24c2f71bd919381df36335ce7746947d97675c4ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ldapProvider")
    def ldap_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapProvider"))

    @ldap_provider.setter
    def ldap_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240b28b5e00d4beb2e2b992e0d11e6f012653fbd89f3940cb7b9e939cdbaad95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ldapProvider", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.groupLdapLink.GroupLdapLinkConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cn": "cn",
        "group_id": "groupId",
        "ldap_provider": "ldapProvider",
        "access_level": "accessLevel",
        "force": "force",
        "group_access": "groupAccess",
        "id": "id",
    },
)
class GroupLdapLinkConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cn: builtins.str,
        group_id: builtins.str,
        ldap_provider: builtins.str,
        access_level: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group_access: typing.Optional[builtins.str] = None,
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
        :param cn: The CN of the LDAP group to link with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#cn GroupLdapLink#cn}
        :param group_id: The id of the GitLab group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_id GroupLdapLink#group_id}
        :param ldap_provider: The name of the LDAP provider as stored in the GitLab database. Note that this is NOT the value of the ``label`` attribute as shown in the web UI. In most cases this will be ``ldapmain`` but you may use the `LDAP check rake task <https://docs.gitlab.com/ee/administration/raketasks/ldap.html#check>`_ for receiving the LDAP server name: ``LDAP: ... Server: ldapmain`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#ldap_provider GroupLdapLink#ldap_provider}
        :param access_level: Minimum access level for members of the LDAP group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#access_level GroupLdapLink#access_level}
        :param force: If true, then delete and replace an existing LDAP link if one exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#force GroupLdapLink#force}
        :param group_access: Minimum access level for members of the LDAP group. Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_access GroupLdapLink#group_access}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#id GroupLdapLink#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da99af4c86522c6a2ac03e905fec1bfa19fe9e24fc49b21e5c79939a160c26ed)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cn", value=cn, expected_type=type_hints["cn"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument ldap_provider", value=ldap_provider, expected_type=type_hints["ldap_provider"])
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument group_access", value=group_access, expected_type=type_hints["group_access"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cn": cn,
            "group_id": group_id,
            "ldap_provider": ldap_provider,
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
        if access_level is not None:
            self._values["access_level"] = access_level
        if force is not None:
            self._values["force"] = force
        if group_access is not None:
            self._values["group_access"] = group_access
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
    def cn(self) -> builtins.str:
        '''The CN of the LDAP group to link with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#cn GroupLdapLink#cn}
        '''
        result = self._values.get("cn")
        assert result is not None, "Required property 'cn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The id of the GitLab group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_id GroupLdapLink#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ldap_provider(self) -> builtins.str:
        '''The name of the LDAP provider as stored in the GitLab database.

        Note that this is NOT the value of the ``label`` attribute as shown in the web UI. In most cases this will be ``ldapmain`` but you may use the `LDAP check rake task <https://docs.gitlab.com/ee/administration/raketasks/ldap.html#check>`_ for receiving the LDAP server name: ``LDAP: ... Server: ldapmain``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#ldap_provider GroupLdapLink#ldap_provider}
        '''
        result = self._values.get("ldap_provider")
        assert result is not None, "Required property 'ldap_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_level(self) -> typing.Optional[builtins.str]:
        '''Minimum access level for members of the LDAP group.

        Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#access_level GroupLdapLink#access_level}
        '''
        result = self._values.get("access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, then delete and replace an existing LDAP link if one exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#force GroupLdapLink#force}
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group_access(self) -> typing.Optional[builtins.str]:
        '''Minimum access level for members of the LDAP group.

        Valid values are: ``no one``, ``minimal``, ``guest``, ``reporter``, ``developer``, ``maintainer``, ``owner``, ``master``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#group_access GroupLdapLink#group_access}
        '''
        result = self._values.get("group_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_ldap_link#id GroupLdapLink#id}.

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
        return "GroupLdapLinkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupLdapLink",
    "GroupLdapLinkConfig",
]

publication.publish()

def _typecheckingstub__9691e9e3a9a8cb94b4f96dea273d1cbdad288d5724c7487df05d6473eadea680(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cn: builtins.str,
    group_id: builtins.str,
    ldap_provider: builtins.str,
    access_level: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group_access: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b7087e707e7ee69a3aa0e00359afb46eecd32746e1052e0f01e4c6975dd0470f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c18895ac4587b72dbae14a9e9cd34ba965f90cb13edcb28896ec5ff6448e8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d33637f26b88784fead2ed76ed157470fafb5e371667efd3729f8c3057a2533(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c03ef467cafb4f2305f98e16a909b0982b4a4b740fb206803ab179a361edc89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f4bc74cf48c9f3995ba20076c29f3caa0cd419983df43bc7f205a72a3ef355(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42bf4f354d281472acf98ad24c2f71bd919381df36335ce7746947d97675c4ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240b28b5e00d4beb2e2b992e0d11e6f012653fbd89f3940cb7b9e939cdbaad95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da99af4c86522c6a2ac03e905fec1bfa19fe9e24fc49b21e5c79939a160c26ed(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cn: builtins.str,
    group_id: builtins.str,
    ldap_provider: builtins.str,
    access_level: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group_access: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
