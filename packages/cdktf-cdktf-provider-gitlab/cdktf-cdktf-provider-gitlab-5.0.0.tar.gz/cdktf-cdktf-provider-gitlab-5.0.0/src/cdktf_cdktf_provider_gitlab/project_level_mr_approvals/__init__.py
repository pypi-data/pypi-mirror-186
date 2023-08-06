'''
# `gitlab_project_level_mr_approvals`

Refer to the Terraform Registory for docs: [`gitlab_project_level_mr_approvals`](https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals).
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


class ProjectLevelMrApprovals(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectLevelMrApprovals.ProjectLevelMrApprovals",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals gitlab_project_level_mr_approvals}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        project_id: jsii.Number,
        disable_overriding_approvers_per_merge_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        merge_requests_author_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_disable_committers_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_password_to_approve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reset_approvals_on_push: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals gitlab_project_level_mr_approvals} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project_id: The ID of the project to change MR approval configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#project_id ProjectLevelMrApprovals#project_id}
        :param disable_overriding_approvers_per_merge_request: By default, users are able to edit the approval rules in merge requests. If set to true,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#disable_overriding_approvers_per_merge_request ProjectLevelMrApprovals#disable_overriding_approvers_per_merge_request}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#id ProjectLevelMrApprovals#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param merge_requests_author_approval: Set to ``true`` if you want to allow merge request authors to self-approve merge requests. Authors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_author_approval ProjectLevelMrApprovals#merge_requests_author_approval}
        :param merge_requests_disable_committers_approval: Set to ``true`` if you want to prevent approval of merge requests by merge request committers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_disable_committers_approval ProjectLevelMrApprovals#merge_requests_disable_committers_approval}
        :param require_password_to_approve: Set to ``true`` if you want to require authentication when approving a merge request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#require_password_to_approve ProjectLevelMrApprovals#require_password_to_approve}
        :param reset_approvals_on_push: Set to ``true`` if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#reset_approvals_on_push ProjectLevelMrApprovals#reset_approvals_on_push}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93fdb6897b7725a52d98bb78a6233c818c518e0885406fadd57636b1d6db0fe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectLevelMrApprovalsConfig(
            project_id=project_id,
            disable_overriding_approvers_per_merge_request=disable_overriding_approvers_per_merge_request,
            id=id,
            merge_requests_author_approval=merge_requests_author_approval,
            merge_requests_disable_committers_approval=merge_requests_disable_committers_approval,
            require_password_to_approve=require_password_to_approve,
            reset_approvals_on_push=reset_approvals_on_push,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDisableOverridingApproversPerMergeRequest")
    def reset_disable_overriding_approvers_per_merge_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableOverridingApproversPerMergeRequest", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMergeRequestsAuthorApproval")
    def reset_merge_requests_author_approval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsAuthorApproval", []))

    @jsii.member(jsii_name="resetMergeRequestsDisableCommittersApproval")
    def reset_merge_requests_disable_committers_approval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsDisableCommittersApproval", []))

    @jsii.member(jsii_name="resetRequirePasswordToApprove")
    def reset_require_password_to_approve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePasswordToApprove", []))

    @jsii.member(jsii_name="resetResetApprovalsOnPush")
    def reset_reset_approvals_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetApprovalsOnPush", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="disableOverridingApproversPerMergeRequestInput")
    def disable_overriding_approvers_per_merge_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableOverridingApproversPerMergeRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsAuthorApprovalInput")
    def merge_requests_author_approval_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mergeRequestsAuthorApprovalInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsDisableCommittersApprovalInput")
    def merge_requests_disable_committers_approval_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mergeRequestsDisableCommittersApprovalInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePasswordToApproveInput")
    def require_password_to_approve_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requirePasswordToApproveInput"))

    @builtins.property
    @jsii.member(jsii_name="resetApprovalsOnPushInput")
    def reset_approvals_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "resetApprovalsOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="disableOverridingApproversPerMergeRequest")
    def disable_overriding_approvers_per_merge_request(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableOverridingApproversPerMergeRequest"))

    @disable_overriding_approvers_per_merge_request.setter
    def disable_overriding_approvers_per_merge_request(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2286ece47db3e1e20ce1e9b3dc1ec37c963949187b280335aa57ecccb5afb31c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableOverridingApproversPerMergeRequest", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee74604c9db376fb4cb696aeb4023cc59db6ad3d81e854890527851b82c6e61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsAuthorApproval")
    def merge_requests_author_approval(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mergeRequestsAuthorApproval"))

    @merge_requests_author_approval.setter
    def merge_requests_author_approval(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__266a585f02173e581990dcaff224edf56b18dc5eed498b9bc1ff745b23d36ea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsAuthorApproval", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsDisableCommittersApproval")
    def merge_requests_disable_committers_approval(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mergeRequestsDisableCommittersApproval"))

    @merge_requests_disable_committers_approval.setter
    def merge_requests_disable_committers_approval(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58da984f481ad697b30d9dfce0d0510087b4060612c927cf8b52fffd6d699cb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsDisableCommittersApproval", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03b1823e6a20d5400dc7efe79b71e580dbb98227f52cfdce2f52485db730a1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="requirePasswordToApprove")
    def require_password_to_approve(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requirePasswordToApprove"))

    @require_password_to_approve.setter
    def require_password_to_approve(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297f81ed357b658e08a3dd1f74425f088e2d584cba719b93a0194fd00f2d0a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePasswordToApprove", value)

    @builtins.property
    @jsii.member(jsii_name="resetApprovalsOnPush")
    def reset_approvals_on_push(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "resetApprovalsOnPush"))

    @reset_approvals_on_push.setter
    def reset_approvals_on_push(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e59412d574984f05924965c5da9ee1f61744322ba9bb9303e3666891602ae11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resetApprovalsOnPush", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectLevelMrApprovals.ProjectLevelMrApprovalsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project_id": "projectId",
        "disable_overriding_approvers_per_merge_request": "disableOverridingApproversPerMergeRequest",
        "id": "id",
        "merge_requests_author_approval": "mergeRequestsAuthorApproval",
        "merge_requests_disable_committers_approval": "mergeRequestsDisableCommittersApproval",
        "require_password_to_approve": "requirePasswordToApprove",
        "reset_approvals_on_push": "resetApprovalsOnPush",
    },
)
class ProjectLevelMrApprovalsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        project_id: jsii.Number,
        disable_overriding_approvers_per_merge_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        merge_requests_author_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_disable_committers_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_password_to_approve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reset_approvals_on_push: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project_id: The ID of the project to change MR approval configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#project_id ProjectLevelMrApprovals#project_id}
        :param disable_overriding_approvers_per_merge_request: By default, users are able to edit the approval rules in merge requests. If set to true,. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#disable_overriding_approvers_per_merge_request ProjectLevelMrApprovals#disable_overriding_approvers_per_merge_request}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#id ProjectLevelMrApprovals#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param merge_requests_author_approval: Set to ``true`` if you want to allow merge request authors to self-approve merge requests. Authors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_author_approval ProjectLevelMrApprovals#merge_requests_author_approval}
        :param merge_requests_disable_committers_approval: Set to ``true`` if you want to prevent approval of merge requests by merge request committers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_disable_committers_approval ProjectLevelMrApprovals#merge_requests_disable_committers_approval}
        :param require_password_to_approve: Set to ``true`` if you want to require authentication when approving a merge request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#require_password_to_approve ProjectLevelMrApprovals#require_password_to_approve}
        :param reset_approvals_on_push: Set to ``true`` if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#reset_approvals_on_push ProjectLevelMrApprovals#reset_approvals_on_push}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50f7e2214f9825e69d980ec18e907583b948d2045332afadb6734e47160ebea)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument disable_overriding_approvers_per_merge_request", value=disable_overriding_approvers_per_merge_request, expected_type=type_hints["disable_overriding_approvers_per_merge_request"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument merge_requests_author_approval", value=merge_requests_author_approval, expected_type=type_hints["merge_requests_author_approval"])
            check_type(argname="argument merge_requests_disable_committers_approval", value=merge_requests_disable_committers_approval, expected_type=type_hints["merge_requests_disable_committers_approval"])
            check_type(argname="argument require_password_to_approve", value=require_password_to_approve, expected_type=type_hints["require_password_to_approve"])
            check_type(argname="argument reset_approvals_on_push", value=reset_approvals_on_push, expected_type=type_hints["reset_approvals_on_push"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if disable_overriding_approvers_per_merge_request is not None:
            self._values["disable_overriding_approvers_per_merge_request"] = disable_overriding_approvers_per_merge_request
        if id is not None:
            self._values["id"] = id
        if merge_requests_author_approval is not None:
            self._values["merge_requests_author_approval"] = merge_requests_author_approval
        if merge_requests_disable_committers_approval is not None:
            self._values["merge_requests_disable_committers_approval"] = merge_requests_disable_committers_approval
        if require_password_to_approve is not None:
            self._values["require_password_to_approve"] = require_password_to_approve
        if reset_approvals_on_push is not None:
            self._values["reset_approvals_on_push"] = reset_approvals_on_push

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
    def project_id(self) -> jsii.Number:
        '''The ID of the project to change MR approval configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#project_id ProjectLevelMrApprovals#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def disable_overriding_approvers_per_merge_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''By default, users are able to edit the approval rules in merge requests. If set to true,.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#disable_overriding_approvers_per_merge_request ProjectLevelMrApprovals#disable_overriding_approvers_per_merge_request}
        '''
        result = self._values.get("disable_overriding_approvers_per_merge_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#id ProjectLevelMrApprovals#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_requests_author_approval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to ``true`` if you want to allow merge request authors to self-approve merge requests. Authors.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_author_approval ProjectLevelMrApprovals#merge_requests_author_approval}
        '''
        result = self._values.get("merge_requests_author_approval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def merge_requests_disable_committers_approval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to ``true`` if you want to prevent approval of merge requests by merge request committers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#merge_requests_disable_committers_approval ProjectLevelMrApprovals#merge_requests_disable_committers_approval}
        '''
        result = self._values.get("merge_requests_disable_committers_approval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_password_to_approve(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to ``true`` if you want to require authentication when approving a merge request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#require_password_to_approve ProjectLevelMrApprovals#require_password_to_approve}
        '''
        result = self._values.get("require_password_to_approve")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def reset_approvals_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to ``true`` if you want to remove all approvals in a merge request when new commits are pushed to its source branch.

        Default is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_level_mr_approvals#reset_approvals_on_push ProjectLevelMrApprovals#reset_approvals_on_push}
        '''
        result = self._values.get("reset_approvals_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectLevelMrApprovalsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectLevelMrApprovals",
    "ProjectLevelMrApprovalsConfig",
]

publication.publish()

def _typecheckingstub__c93fdb6897b7725a52d98bb78a6233c818c518e0885406fadd57636b1d6db0fe(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    project_id: jsii.Number,
    disable_overriding_approvers_per_merge_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    merge_requests_author_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_disable_committers_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_password_to_approve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reset_approvals_on_push: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__2286ece47db3e1e20ce1e9b3dc1ec37c963949187b280335aa57ecccb5afb31c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee74604c9db376fb4cb696aeb4023cc59db6ad3d81e854890527851b82c6e61a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__266a585f02173e581990dcaff224edf56b18dc5eed498b9bc1ff745b23d36ea7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58da984f481ad697b30d9dfce0d0510087b4060612c927cf8b52fffd6d699cb4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03b1823e6a20d5400dc7efe79b71e580dbb98227f52cfdce2f52485db730a1d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297f81ed357b658e08a3dd1f74425f088e2d584cba719b93a0194fd00f2d0a73(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e59412d574984f05924965c5da9ee1f61744322ba9bb9303e3666891602ae11(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50f7e2214f9825e69d980ec18e907583b948d2045332afadb6734e47160ebea(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    project_id: jsii.Number,
    disable_overriding_approvers_per_merge_request: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    merge_requests_author_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_disable_committers_approval: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_password_to_approve: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reset_approvals_on_push: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
