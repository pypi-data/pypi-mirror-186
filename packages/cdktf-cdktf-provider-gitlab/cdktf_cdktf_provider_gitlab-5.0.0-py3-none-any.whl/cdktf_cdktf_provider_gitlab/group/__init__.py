'''
# `gitlab_group`

Refer to the Terraform Registory for docs: [`gitlab_group`](https://www.terraform.io/docs/providers/gitlab/r/group).
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


class Group(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.group.Group",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group gitlab_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        path: builtins.str,
        auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_branch_protection: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        emails_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extra_shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        lfs_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        membership_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mentions_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parent_id: typing.Optional[jsii.Number] = None,
        prevent_forking_outside_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_creation_level: typing.Optional[builtins.str] = None,
        request_access_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_two_factor_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
        share_with_group_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subgroup_creation_level: typing.Optional[builtins.str] = None,
        two_factor_grace_period: typing.Optional[jsii.Number] = None,
        visibility_level: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group gitlab_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#name Group#name}
        :param path: The path of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#path Group#path}
        :param auto_devops_enabled: Defaults to false. Default to Auto DevOps pipeline for all projects within this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#auto_devops_enabled Group#auto_devops_enabled}
        :param default_branch_protection: Defaults to 2. See https://docs.gitlab.com/ee/api/groups.html#options-for-default_branch_protection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#default_branch_protection Group#default_branch_protection}
        :param description: The description of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#description Group#description}
        :param emails_disabled: Defaults to false. Disable email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#emails_disabled Group#emails_disabled}
        :param extra_shared_runners_minutes_limit: Can be set by administrators only. Additional CI/CD minutes for this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#extra_shared_runners_minutes_limit Group#extra_shared_runners_minutes_limit}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#id Group#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lfs_enabled: Defaults to true. Enable/disable Large File Storage (LFS) for the projects in this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#lfs_enabled Group#lfs_enabled}
        :param membership_lock: Users cannot be added to projects in this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#membership_lock Group#membership_lock}
        :param mentions_disabled: Defaults to false. Disable the capability of a group from getting mentioned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#mentions_disabled Group#mentions_disabled}
        :param parent_id: Id of the parent group (creates a nested group). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#parent_id Group#parent_id}
        :param prevent_forking_outside_group: Defaults to false. When enabled, users can not fork projects from this group to external namespaces. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#prevent_forking_outside_group Group#prevent_forking_outside_group}
        :param project_creation_level: Defaults to maintainer. Determine if developers can create projects in the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#project_creation_level Group#project_creation_level}
        :param request_access_enabled: Defaults to false. Allow users to request member access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#request_access_enabled Group#request_access_enabled}
        :param require_two_factor_authentication: Defaults to false. Require all users in this group to setup Two-factor authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#require_two_factor_authentication Group#require_two_factor_authentication}
        :param shared_runners_minutes_limit: Can be set by administrators only. Maximum number of monthly CI/CD minutes for this group. Can be nil (default; inherit system default), 0 (unlimited), or > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#shared_runners_minutes_limit Group#shared_runners_minutes_limit}
        :param share_with_group_lock: Defaults to false. Prevent sharing a project with another group within this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#share_with_group_lock Group#share_with_group_lock}
        :param subgroup_creation_level: Defaults to owner. Allowed to create subgroups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#subgroup_creation_level Group#subgroup_creation_level}
        :param two_factor_grace_period: Defaults to 48. Time before Two-factor authentication is enforced (in hours). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#two_factor_grace_period Group#two_factor_grace_period}
        :param visibility_level: The group's visibility. Can be ``private``, ``internal``, or ``public``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#visibility_level Group#visibility_level}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba99799c3dfc0c212cdf9860e0ebe4109245373801789101a41d768bfb63c07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupConfig(
            name=name,
            path=path,
            auto_devops_enabled=auto_devops_enabled,
            default_branch_protection=default_branch_protection,
            description=description,
            emails_disabled=emails_disabled,
            extra_shared_runners_minutes_limit=extra_shared_runners_minutes_limit,
            id=id,
            lfs_enabled=lfs_enabled,
            membership_lock=membership_lock,
            mentions_disabled=mentions_disabled,
            parent_id=parent_id,
            prevent_forking_outside_group=prevent_forking_outside_group,
            project_creation_level=project_creation_level,
            request_access_enabled=request_access_enabled,
            require_two_factor_authentication=require_two_factor_authentication,
            shared_runners_minutes_limit=shared_runners_minutes_limit,
            share_with_group_lock=share_with_group_lock,
            subgroup_creation_level=subgroup_creation_level,
            two_factor_grace_period=two_factor_grace_period,
            visibility_level=visibility_level,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAutoDevopsEnabled")
    def reset_auto_devops_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDevopsEnabled", []))

    @jsii.member(jsii_name="resetDefaultBranchProtection")
    def reset_default_branch_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBranchProtection", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEmailsDisabled")
    def reset_emails_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailsDisabled", []))

    @jsii.member(jsii_name="resetExtraSharedRunnersMinutesLimit")
    def reset_extra_shared_runners_minutes_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraSharedRunnersMinutesLimit", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLfsEnabled")
    def reset_lfs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLfsEnabled", []))

    @jsii.member(jsii_name="resetMembershipLock")
    def reset_membership_lock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembershipLock", []))

    @jsii.member(jsii_name="resetMentionsDisabled")
    def reset_mentions_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMentionsDisabled", []))

    @jsii.member(jsii_name="resetParentId")
    def reset_parent_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentId", []))

    @jsii.member(jsii_name="resetPreventForkingOutsideGroup")
    def reset_prevent_forking_outside_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreventForkingOutsideGroup", []))

    @jsii.member(jsii_name="resetProjectCreationLevel")
    def reset_project_creation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectCreationLevel", []))

    @jsii.member(jsii_name="resetRequestAccessEnabled")
    def reset_request_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestAccessEnabled", []))

    @jsii.member(jsii_name="resetRequireTwoFactorAuthentication")
    def reset_require_two_factor_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireTwoFactorAuthentication", []))

    @jsii.member(jsii_name="resetSharedRunnersMinutesLimit")
    def reset_shared_runners_minutes_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedRunnersMinutesLimit", []))

    @jsii.member(jsii_name="resetShareWithGroupLock")
    def reset_share_with_group_lock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareWithGroupLock", []))

    @jsii.member(jsii_name="resetSubgroupCreationLevel")
    def reset_subgroup_creation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubgroupCreationLevel", []))

    @jsii.member(jsii_name="resetTwoFactorGracePeriod")
    def reset_two_factor_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTwoFactorGracePeriod", []))

    @jsii.member(jsii_name="resetVisibilityLevel")
    def reset_visibility_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibilityLevel", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="fullName")
    def full_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullName"))

    @builtins.property
    @jsii.member(jsii_name="fullPath")
    def full_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullPath"))

    @builtins.property
    @jsii.member(jsii_name="runnersToken")
    def runners_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runnersToken"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsEnabledInput")
    def auto_devops_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoDevopsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBranchProtectionInput")
    def default_branch_protection_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultBranchProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsDisabledInput")
    def emails_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "emailsDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="extraSharedRunnersMinutesLimitInput")
    def extra_shared_runners_minutes_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "extraSharedRunnersMinutesLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lfsEnabledInput")
    def lfs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "lfsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="membershipLockInput")
    def membership_lock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "membershipLockInput"))

    @builtins.property
    @jsii.member(jsii_name="mentionsDisabledInput")
    def mentions_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mentionsDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentIdInput")
    def parent_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="preventForkingOutsideGroupInput")
    def prevent_forking_outside_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "preventForkingOutsideGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="projectCreationLevelInput")
    def project_creation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectCreationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="requestAccessEnabledInput")
    def request_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requestAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="requireTwoFactorAuthenticationInput")
    def require_two_factor_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireTwoFactorAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedRunnersMinutesLimitInput")
    def shared_runners_minutes_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sharedRunnersMinutesLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="shareWithGroupLockInput")
    def share_with_group_lock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "shareWithGroupLockInput"))

    @builtins.property
    @jsii.member(jsii_name="subgroupCreationLevelInput")
    def subgroup_creation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subgroupCreationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="twoFactorGracePeriodInput")
    def two_factor_grace_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "twoFactorGracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityLevelInput")
    def visibility_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsEnabled")
    def auto_devops_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoDevopsEnabled"))

    @auto_devops_enabled.setter
    def auto_devops_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5ee5197e43d532cde3f273652c07112905095d2a6f1152af4a95c6019175c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDevopsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBranchProtection")
    def default_branch_protection(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultBranchProtection"))

    @default_branch_protection.setter
    def default_branch_protection(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f646129ff3b1ac94eb5501e160b860cbb3e843f10267e6a04e15d7814cdafbe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBranchProtection", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75058c67534df7bfbb41c981ca9fe3afcbbd097d46590b76fca8d8d0b37761a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="emailsDisabled")
    def emails_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "emailsDisabled"))

    @emails_disabled.setter
    def emails_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc5f0938cb8f5db381056424f8ccb159e80824608329ec5e561580bd6a5c9cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailsDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="extraSharedRunnersMinutesLimit")
    def extra_shared_runners_minutes_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "extraSharedRunnersMinutesLimit"))

    @extra_shared_runners_minutes_limit.setter
    def extra_shared_runners_minutes_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186e16f0071bd89da8cafd37afba2bb9cbe972375b25824705ccad4c94c20e06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraSharedRunnersMinutesLimit", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f527c7e04b91b3e7bf7660d3a5c08d27554b9f0ebce9bb4032da93059618a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lfsEnabled")
    def lfs_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "lfsEnabled"))

    @lfs_enabled.setter
    def lfs_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc16ededb6f38b6e437e96239bb840eae9b13730a79acd1a5d99c4aec64a20a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lfsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="membershipLock")
    def membership_lock(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "membershipLock"))

    @membership_lock.setter
    def membership_lock(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62648375b591a55aee7e12b34809299183acd6e2b72812e23ba582e52509783)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipLock", value)

    @builtins.property
    @jsii.member(jsii_name="mentionsDisabled")
    def mentions_disabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mentionsDisabled"))

    @mentions_disabled.setter
    def mentions_disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af60ddd8447ffb32fecca83476a5340d51db60bb2b71f3900068f5977ee8ff05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mentionsDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0bb14e6c07cf1a8841b8e273c6f66d252f8e373eb0c2fd9b8b56ea1093c9041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentId")
    def parent_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parentId"))

    @parent_id.setter
    def parent_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fcb463e1b0993fbe3f14f4c83b5aaf2d7df9133c1ab81663c61deb253d4e31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d6772179f5c1fabd99f58cbea49ded94499d31416518a02eb863f6ee637476)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="preventForkingOutsideGroup")
    def prevent_forking_outside_group(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "preventForkingOutsideGroup"))

    @prevent_forking_outside_group.setter
    def prevent_forking_outside_group(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70fbab9c6f08d8155eb21fd3f032cc519c3b189c6e8fc6f1538f947486c27ae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preventForkingOutsideGroup", value)

    @builtins.property
    @jsii.member(jsii_name="projectCreationLevel")
    def project_creation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectCreationLevel"))

    @project_creation_level.setter
    def project_creation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40f064449daebdd56116e7ae8f05437b22e235d31fed5df91af54fac8cf57584)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectCreationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="requestAccessEnabled")
    def request_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requestAccessEnabled"))

    @request_access_enabled.setter
    def request_access_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f91700aba15219c4f1bbc556e377633b4a649dbbb8407382a4992f215ced69e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="requireTwoFactorAuthentication")
    def require_two_factor_authentication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireTwoFactorAuthentication"))

    @require_two_factor_authentication.setter
    def require_two_factor_authentication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2fb1ebe02f044414605cb03da58f20f78839a6461b40c908b6ebe0affdc381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireTwoFactorAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="sharedRunnersMinutesLimit")
    def shared_runners_minutes_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sharedRunnersMinutesLimit"))

    @shared_runners_minutes_limit.setter
    def shared_runners_minutes_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d16b8dd1c124966d12c1dae51287669d9a65c697c8032580b0c084025d1e97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedRunnersMinutesLimit", value)

    @builtins.property
    @jsii.member(jsii_name="shareWithGroupLock")
    def share_with_group_lock(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "shareWithGroupLock"))

    @share_with_group_lock.setter
    def share_with_group_lock(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801deadad61e26b6e115bfd915cdc95cbb50b79391824f42de599f8513bd2faa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareWithGroupLock", value)

    @builtins.property
    @jsii.member(jsii_name="subgroupCreationLevel")
    def subgroup_creation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subgroupCreationLevel"))

    @subgroup_creation_level.setter
    def subgroup_creation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b1a536720055250a6c0d277303240e4c40d34655d16c329857c0181a095820)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subgroupCreationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="twoFactorGracePeriod")
    def two_factor_grace_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "twoFactorGracePeriod"))

    @two_factor_grace_period.setter
    def two_factor_grace_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be17fd058a0353a8216e9d840411aa6246fa3762369ac7003e066949b7d4019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "twoFactorGracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="visibilityLevel")
    def visibility_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibilityLevel"))

    @visibility_level.setter
    def visibility_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da56533c35403379cc486ca51558b7465c7715143e7439b1f43894cfe434c733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibilityLevel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.group.GroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "path": "path",
        "auto_devops_enabled": "autoDevopsEnabled",
        "default_branch_protection": "defaultBranchProtection",
        "description": "description",
        "emails_disabled": "emailsDisabled",
        "extra_shared_runners_minutes_limit": "extraSharedRunnersMinutesLimit",
        "id": "id",
        "lfs_enabled": "lfsEnabled",
        "membership_lock": "membershipLock",
        "mentions_disabled": "mentionsDisabled",
        "parent_id": "parentId",
        "prevent_forking_outside_group": "preventForkingOutsideGroup",
        "project_creation_level": "projectCreationLevel",
        "request_access_enabled": "requestAccessEnabled",
        "require_two_factor_authentication": "requireTwoFactorAuthentication",
        "shared_runners_minutes_limit": "sharedRunnersMinutesLimit",
        "share_with_group_lock": "shareWithGroupLock",
        "subgroup_creation_level": "subgroupCreationLevel",
        "two_factor_grace_period": "twoFactorGracePeriod",
        "visibility_level": "visibilityLevel",
    },
)
class GroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        path: builtins.str,
        auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_branch_protection: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        emails_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extra_shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        lfs_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        membership_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mentions_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        parent_id: typing.Optional[jsii.Number] = None,
        prevent_forking_outside_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_creation_level: typing.Optional[builtins.str] = None,
        request_access_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_two_factor_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
        share_with_group_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subgroup_creation_level: typing.Optional[builtins.str] = None,
        two_factor_grace_period: typing.Optional[jsii.Number] = None,
        visibility_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#name Group#name}
        :param path: The path of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#path Group#path}
        :param auto_devops_enabled: Defaults to false. Default to Auto DevOps pipeline for all projects within this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#auto_devops_enabled Group#auto_devops_enabled}
        :param default_branch_protection: Defaults to 2. See https://docs.gitlab.com/ee/api/groups.html#options-for-default_branch_protection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#default_branch_protection Group#default_branch_protection}
        :param description: The description of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#description Group#description}
        :param emails_disabled: Defaults to false. Disable email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#emails_disabled Group#emails_disabled}
        :param extra_shared_runners_minutes_limit: Can be set by administrators only. Additional CI/CD minutes for this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#extra_shared_runners_minutes_limit Group#extra_shared_runners_minutes_limit}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#id Group#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lfs_enabled: Defaults to true. Enable/disable Large File Storage (LFS) for the projects in this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#lfs_enabled Group#lfs_enabled}
        :param membership_lock: Users cannot be added to projects in this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#membership_lock Group#membership_lock}
        :param mentions_disabled: Defaults to false. Disable the capability of a group from getting mentioned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#mentions_disabled Group#mentions_disabled}
        :param parent_id: Id of the parent group (creates a nested group). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#parent_id Group#parent_id}
        :param prevent_forking_outside_group: Defaults to false. When enabled, users can not fork projects from this group to external namespaces. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#prevent_forking_outside_group Group#prevent_forking_outside_group}
        :param project_creation_level: Defaults to maintainer. Determine if developers can create projects in the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#project_creation_level Group#project_creation_level}
        :param request_access_enabled: Defaults to false. Allow users to request member access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#request_access_enabled Group#request_access_enabled}
        :param require_two_factor_authentication: Defaults to false. Require all users in this group to setup Two-factor authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#require_two_factor_authentication Group#require_two_factor_authentication}
        :param shared_runners_minutes_limit: Can be set by administrators only. Maximum number of monthly CI/CD minutes for this group. Can be nil (default; inherit system default), 0 (unlimited), or > 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#shared_runners_minutes_limit Group#shared_runners_minutes_limit}
        :param share_with_group_lock: Defaults to false. Prevent sharing a project with another group within this group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#share_with_group_lock Group#share_with_group_lock}
        :param subgroup_creation_level: Defaults to owner. Allowed to create subgroups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#subgroup_creation_level Group#subgroup_creation_level}
        :param two_factor_grace_period: Defaults to 48. Time before Two-factor authentication is enforced (in hours). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#two_factor_grace_period Group#two_factor_grace_period}
        :param visibility_level: The group's visibility. Can be ``private``, ``internal``, or ``public``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#visibility_level Group#visibility_level}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b46134b12f9e1fce1e34db566aea38b84df83b20de8e3094a6537f60b3321e3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument auto_devops_enabled", value=auto_devops_enabled, expected_type=type_hints["auto_devops_enabled"])
            check_type(argname="argument default_branch_protection", value=default_branch_protection, expected_type=type_hints["default_branch_protection"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument emails_disabled", value=emails_disabled, expected_type=type_hints["emails_disabled"])
            check_type(argname="argument extra_shared_runners_minutes_limit", value=extra_shared_runners_minutes_limit, expected_type=type_hints["extra_shared_runners_minutes_limit"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lfs_enabled", value=lfs_enabled, expected_type=type_hints["lfs_enabled"])
            check_type(argname="argument membership_lock", value=membership_lock, expected_type=type_hints["membership_lock"])
            check_type(argname="argument mentions_disabled", value=mentions_disabled, expected_type=type_hints["mentions_disabled"])
            check_type(argname="argument parent_id", value=parent_id, expected_type=type_hints["parent_id"])
            check_type(argname="argument prevent_forking_outside_group", value=prevent_forking_outside_group, expected_type=type_hints["prevent_forking_outside_group"])
            check_type(argname="argument project_creation_level", value=project_creation_level, expected_type=type_hints["project_creation_level"])
            check_type(argname="argument request_access_enabled", value=request_access_enabled, expected_type=type_hints["request_access_enabled"])
            check_type(argname="argument require_two_factor_authentication", value=require_two_factor_authentication, expected_type=type_hints["require_two_factor_authentication"])
            check_type(argname="argument shared_runners_minutes_limit", value=shared_runners_minutes_limit, expected_type=type_hints["shared_runners_minutes_limit"])
            check_type(argname="argument share_with_group_lock", value=share_with_group_lock, expected_type=type_hints["share_with_group_lock"])
            check_type(argname="argument subgroup_creation_level", value=subgroup_creation_level, expected_type=type_hints["subgroup_creation_level"])
            check_type(argname="argument two_factor_grace_period", value=two_factor_grace_period, expected_type=type_hints["two_factor_grace_period"])
            check_type(argname="argument visibility_level", value=visibility_level, expected_type=type_hints["visibility_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "path": path,
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
        if auto_devops_enabled is not None:
            self._values["auto_devops_enabled"] = auto_devops_enabled
        if default_branch_protection is not None:
            self._values["default_branch_protection"] = default_branch_protection
        if description is not None:
            self._values["description"] = description
        if emails_disabled is not None:
            self._values["emails_disabled"] = emails_disabled
        if extra_shared_runners_minutes_limit is not None:
            self._values["extra_shared_runners_minutes_limit"] = extra_shared_runners_minutes_limit
        if id is not None:
            self._values["id"] = id
        if lfs_enabled is not None:
            self._values["lfs_enabled"] = lfs_enabled
        if membership_lock is not None:
            self._values["membership_lock"] = membership_lock
        if mentions_disabled is not None:
            self._values["mentions_disabled"] = mentions_disabled
        if parent_id is not None:
            self._values["parent_id"] = parent_id
        if prevent_forking_outside_group is not None:
            self._values["prevent_forking_outside_group"] = prevent_forking_outside_group
        if project_creation_level is not None:
            self._values["project_creation_level"] = project_creation_level
        if request_access_enabled is not None:
            self._values["request_access_enabled"] = request_access_enabled
        if require_two_factor_authentication is not None:
            self._values["require_two_factor_authentication"] = require_two_factor_authentication
        if shared_runners_minutes_limit is not None:
            self._values["shared_runners_minutes_limit"] = shared_runners_minutes_limit
        if share_with_group_lock is not None:
            self._values["share_with_group_lock"] = share_with_group_lock
        if subgroup_creation_level is not None:
            self._values["subgroup_creation_level"] = subgroup_creation_level
        if two_factor_grace_period is not None:
            self._values["two_factor_grace_period"] = two_factor_grace_period
        if visibility_level is not None:
            self._values["visibility_level"] = visibility_level

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
    def name(self) -> builtins.str:
        '''The name of this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#name Group#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#path Group#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_devops_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Default to Auto DevOps pipeline for all projects within this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#auto_devops_enabled Group#auto_devops_enabled}
        '''
        result = self._values.get("auto_devops_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_branch_protection(self) -> typing.Optional[jsii.Number]:
        '''Defaults to 2. See https://docs.gitlab.com/ee/api/groups.html#options-for-default_branch_protection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#default_branch_protection Group#default_branch_protection}
        '''
        result = self._values.get("default_branch_protection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#description Group#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emails_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Disable email notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#emails_disabled Group#emails_disabled}
        '''
        result = self._values.get("emails_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def extra_shared_runners_minutes_limit(self) -> typing.Optional[jsii.Number]:
        '''Can be set by administrators only. Additional CI/CD minutes for this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#extra_shared_runners_minutes_limit Group#extra_shared_runners_minutes_limit}
        '''
        result = self._values.get("extra_shared_runners_minutes_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#id Group#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lfs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to true. Enable/disable Large File Storage (LFS) for the projects in this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#lfs_enabled Group#lfs_enabled}
        '''
        result = self._values.get("lfs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def membership_lock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Users cannot be added to projects in this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#membership_lock Group#membership_lock}
        '''
        result = self._values.get("membership_lock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def mentions_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Disable the capability of a group from getting mentioned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#mentions_disabled Group#mentions_disabled}
        '''
        result = self._values.get("mentions_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def parent_id(self) -> typing.Optional[jsii.Number]:
        '''Id of the parent group (creates a nested group).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#parent_id Group#parent_id}
        '''
        result = self._values.get("parent_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prevent_forking_outside_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. When enabled, users can not fork projects from this group to external namespaces.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#prevent_forking_outside_group Group#prevent_forking_outside_group}
        '''
        result = self._values.get("prevent_forking_outside_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def project_creation_level(self) -> typing.Optional[builtins.str]:
        '''Defaults to maintainer. Determine if developers can create projects in the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#project_creation_level Group#project_creation_level}
        '''
        result = self._values.get("project_creation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Allow users to request member access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#request_access_enabled Group#request_access_enabled}
        '''
        result = self._values.get("request_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_two_factor_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Require all users in this group to setup Two-factor authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#require_two_factor_authentication Group#require_two_factor_authentication}
        '''
        result = self._values.get("require_two_factor_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def shared_runners_minutes_limit(self) -> typing.Optional[jsii.Number]:
        '''Can be set by administrators only.

        Maximum number of monthly CI/CD minutes for this group. Can be nil (default; inherit system default), 0 (unlimited), or > 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#shared_runners_minutes_limit Group#shared_runners_minutes_limit}
        '''
        result = self._values.get("shared_runners_minutes_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def share_with_group_lock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to false. Prevent sharing a project with another group within this group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#share_with_group_lock Group#share_with_group_lock}
        '''
        result = self._values.get("share_with_group_lock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subgroup_creation_level(self) -> typing.Optional[builtins.str]:
        '''Defaults to owner. Allowed to create subgroups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#subgroup_creation_level Group#subgroup_creation_level}
        '''
        result = self._values.get("subgroup_creation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def two_factor_grace_period(self) -> typing.Optional[jsii.Number]:
        '''Defaults to 48. Time before Two-factor authentication is enforced (in hours).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#two_factor_grace_period Group#two_factor_grace_period}
        '''
        result = self._values.get("two_factor_grace_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def visibility_level(self) -> typing.Optional[builtins.str]:
        '''The group's visibility. Can be ``private``, ``internal``, or ``public``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group#visibility_level Group#visibility_level}
        '''
        result = self._values.get("visibility_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Group",
    "GroupConfig",
]

publication.publish()

def _typecheckingstub__2ba99799c3dfc0c212cdf9860e0ebe4109245373801789101a41d768bfb63c07(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    path: builtins.str,
    auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_branch_protection: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    emails_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extra_shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    lfs_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    membership_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mentions_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parent_id: typing.Optional[jsii.Number] = None,
    prevent_forking_outside_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_creation_level: typing.Optional[builtins.str] = None,
    request_access_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_two_factor_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
    share_with_group_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subgroup_creation_level: typing.Optional[builtins.str] = None,
    two_factor_grace_period: typing.Optional[jsii.Number] = None,
    visibility_level: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__cb5ee5197e43d532cde3f273652c07112905095d2a6f1152af4a95c6019175c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f646129ff3b1ac94eb5501e160b860cbb3e843f10267e6a04e15d7814cdafbe1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75058c67534df7bfbb41c981ca9fe3afcbbd097d46590b76fca8d8d0b37761a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abc5f0938cb8f5db381056424f8ccb159e80824608329ec5e561580bd6a5c9cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186e16f0071bd89da8cafd37afba2bb9cbe972375b25824705ccad4c94c20e06(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f527c7e04b91b3e7bf7660d3a5c08d27554b9f0ebce9bb4032da93059618a6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc16ededb6f38b6e437e96239bb840eae9b13730a79acd1a5d99c4aec64a20a2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62648375b591a55aee7e12b34809299183acd6e2b72812e23ba582e52509783(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af60ddd8447ffb32fecca83476a5340d51db60bb2b71f3900068f5977ee8ff05(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0bb14e6c07cf1a8841b8e273c6f66d252f8e373eb0c2fd9b8b56ea1093c9041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fcb463e1b0993fbe3f14f4c83b5aaf2d7df9133c1ab81663c61deb253d4e31(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d6772179f5c1fabd99f58cbea49ded94499d31416518a02eb863f6ee637476(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fbab9c6f08d8155eb21fd3f032cc519c3b189c6e8fc6f1538f947486c27ae5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f064449daebdd56116e7ae8f05437b22e235d31fed5df91af54fac8cf57584(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f91700aba15219c4f1bbc556e377633b4a649dbbb8407382a4992f215ced69e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2fb1ebe02f044414605cb03da58f20f78839a6461b40c908b6ebe0affdc381(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d16b8dd1c124966d12c1dae51287669d9a65c697c8032580b0c084025d1e97(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801deadad61e26b6e115bfd915cdc95cbb50b79391824f42de599f8513bd2faa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b1a536720055250a6c0d277303240e4c40d34655d16c329857c0181a095820(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be17fd058a0353a8216e9d840411aa6246fa3762369ac7003e066949b7d4019(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da56533c35403379cc486ca51558b7465c7715143e7439b1f43894cfe434c733(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b46134b12f9e1fce1e34db566aea38b84df83b20de8e3094a6537f60b3321e3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    path: builtins.str,
    auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_branch_protection: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    emails_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extra_shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    lfs_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    membership_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mentions_disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    parent_id: typing.Optional[jsii.Number] = None,
    prevent_forking_outside_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_creation_level: typing.Optional[builtins.str] = None,
    request_access_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_two_factor_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    shared_runners_minutes_limit: typing.Optional[jsii.Number] = None,
    share_with_group_lock: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subgroup_creation_level: typing.Optional[builtins.str] = None,
    two_factor_grace_period: typing.Optional[jsii.Number] = None,
    visibility_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
