'''
# `gitlab_project_approval_rule`

Refer to the Terraform Registory for docs: [`gitlab_project_approval_rule`](https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule).
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


class ProjectApprovalRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectApprovalRule.ProjectApprovalRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule gitlab_project_approval_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        approvals_required: jsii.Number,
        name: builtins.str,
        project: builtins.str,
        group_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        protected_branch_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        rule_type: typing.Optional[builtins.str] = None,
        user_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule gitlab_project_approval_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param approvals_required: The number of approvals required for this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#approvals_required ProjectApprovalRule#approvals_required}
        :param name: The name of the approval rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#name ProjectApprovalRule#name}
        :param project: The name or id of the project to add the approval rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#project ProjectApprovalRule#project}
        :param group_ids: A list of group IDs whose members can approve of the merge request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#group_ids ProjectApprovalRule#group_ids}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#id ProjectApprovalRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_branch_ids: A list of protected branch IDs (not branch names) for which the rule applies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#protected_branch_ids ProjectApprovalRule#protected_branch_ids}
        :param rule_type: String, defaults to 'regular'. The type of rule. ``any_approver`` is a pre-configured default rule with ``approvals_required`` at ``0``. Valid values are ``regular``, ``any_approver``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#rule_type ProjectApprovalRule#rule_type}
        :param user_ids: A list of specific User IDs to add to the list of approvers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#user_ids ProjectApprovalRule#user_ids}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6a866f18bd9c65c0fd1c1c17ccb181eb31fc8910316219f433e6de43e49f78)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectApprovalRuleConfig(
            approvals_required=approvals_required,
            name=name,
            project=project,
            group_ids=group_ids,
            id=id,
            protected_branch_ids=protected_branch_ids,
            rule_type=rule_type,
            user_ids=user_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetGroupIds")
    def reset_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupIds", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProtectedBranchIds")
    def reset_protected_branch_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedBranchIds", []))

    @jsii.member(jsii_name="resetRuleType")
    def reset_rule_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleType", []))

    @jsii.member(jsii_name="resetUserIds")
    def reset_user_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="approvalsRequiredInput")
    def approvals_required_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "approvalsRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdsInput")
    def group_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "groupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedBranchIdsInput")
    def protected_branch_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "protectedBranchIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleTypeInput")
    def rule_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdsInput")
    def user_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "userIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalsRequired")
    def approvals_required(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approvalsRequired"))

    @approvals_required.setter
    def approvals_required(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97af90fe14aa60c5938a63cf7a439480d5a316695add4a33661fee62c0dcdeee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalsRequired", value)

    @builtins.property
    @jsii.member(jsii_name="groupIds")
    def group_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "groupIds"))

    @group_ids.setter
    def group_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d14690bb978b8b8feb70e4b7e20d7df710fc2d947124f06165b028a7c54afa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupIds", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd2c83f3edca0d13beccb4e9b8e032121436d3bf931643c2c396d52a7193509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ad099b133e90c22fe598d0c90f3aa8bf1d6b294c006f9fe7db465012c8597d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f7cecb87b5db5b3d765ef8f7c825843640b2d612be6373303c392e8def5d40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="protectedBranchIds")
    def protected_branch_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "protectedBranchIds"))

    @protected_branch_ids.setter
    def protected_branch_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c37931131aba5e4c63ac4c53e35a6c98c3bafb3993bdb2252cdddedd0dc3778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedBranchIds", value)

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6353593ac80e5ff1e2c536823c051c9319d1ae4c3ebde778dd3ca55c672daabd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleType", value)

    @builtins.property
    @jsii.member(jsii_name="userIds")
    def user_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "userIds"))

    @user_ids.setter
    def user_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7de1face6b12d671eb5235deda919b4b97092eeb7a72a333cd723fd691839b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectApprovalRule.ProjectApprovalRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "approvals_required": "approvalsRequired",
        "name": "name",
        "project": "project",
        "group_ids": "groupIds",
        "id": "id",
        "protected_branch_ids": "protectedBranchIds",
        "rule_type": "ruleType",
        "user_ids": "userIds",
    },
)
class ProjectApprovalRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        approvals_required: jsii.Number,
        name: builtins.str,
        project: builtins.str,
        group_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        id: typing.Optional[builtins.str] = None,
        protected_branch_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        rule_type: typing.Optional[builtins.str] = None,
        user_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param approvals_required: The number of approvals required for this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#approvals_required ProjectApprovalRule#approvals_required}
        :param name: The name of the approval rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#name ProjectApprovalRule#name}
        :param project: The name or id of the project to add the approval rules. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#project ProjectApprovalRule#project}
        :param group_ids: A list of group IDs whose members can approve of the merge request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#group_ids ProjectApprovalRule#group_ids}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#id ProjectApprovalRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_branch_ids: A list of protected branch IDs (not branch names) for which the rule applies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#protected_branch_ids ProjectApprovalRule#protected_branch_ids}
        :param rule_type: String, defaults to 'regular'. The type of rule. ``any_approver`` is a pre-configured default rule with ``approvals_required`` at ``0``. Valid values are ``regular``, ``any_approver``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#rule_type ProjectApprovalRule#rule_type}
        :param user_ids: A list of specific User IDs to add to the list of approvers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#user_ids ProjectApprovalRule#user_ids}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee7f45e3ca72ce3c29a9e770de19e01d5c38ebdf734e3d68bae9542ca9b6c74d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument approvals_required", value=approvals_required, expected_type=type_hints["approvals_required"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument group_ids", value=group_ids, expected_type=type_hints["group_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument protected_branch_ids", value=protected_branch_ids, expected_type=type_hints["protected_branch_ids"])
            check_type(argname="argument rule_type", value=rule_type, expected_type=type_hints["rule_type"])
            check_type(argname="argument user_ids", value=user_ids, expected_type=type_hints["user_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approvals_required": approvals_required,
            "name": name,
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
        if group_ids is not None:
            self._values["group_ids"] = group_ids
        if id is not None:
            self._values["id"] = id
        if protected_branch_ids is not None:
            self._values["protected_branch_ids"] = protected_branch_ids
        if rule_type is not None:
            self._values["rule_type"] = rule_type
        if user_ids is not None:
            self._values["user_ids"] = user_ids

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
    def approvals_required(self) -> jsii.Number:
        '''The number of approvals required for this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#approvals_required ProjectApprovalRule#approvals_required}
        '''
        result = self._values.get("approvals_required")
        assert result is not None, "Required property 'approvals_required' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the approval rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#name ProjectApprovalRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or id of the project to add the approval rules.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#project ProjectApprovalRule#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of group IDs whose members can approve of the merge request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#group_ids ProjectApprovalRule#group_ids}
        '''
        result = self._values.get("group_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#id ProjectApprovalRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_branch_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of protected branch IDs (not branch names) for which the rule applies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#protected_branch_ids ProjectApprovalRule#protected_branch_ids}
        '''
        result = self._values.get("protected_branch_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def rule_type(self) -> typing.Optional[builtins.str]:
        '''String, defaults to 'regular'.

        The type of rule. ``any_approver`` is a pre-configured default rule with ``approvals_required`` at ``0``. Valid values are ``regular``, ``any_approver``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#rule_type ProjectApprovalRule#rule_type}
        '''
        result = self._values.get("rule_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of specific User IDs to add to the list of approvers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_approval_rule#user_ids ProjectApprovalRule#user_ids}
        '''
        result = self._values.get("user_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectApprovalRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectApprovalRule",
    "ProjectApprovalRuleConfig",
]

publication.publish()

def _typecheckingstub__bf6a866f18bd9c65c0fd1c1c17ccb181eb31fc8910316219f433e6de43e49f78(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    approvals_required: jsii.Number,
    name: builtins.str,
    project: builtins.str,
    group_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    id: typing.Optional[builtins.str] = None,
    protected_branch_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    rule_type: typing.Optional[builtins.str] = None,
    user_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
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

def _typecheckingstub__97af90fe14aa60c5938a63cf7a439480d5a316695add4a33661fee62c0dcdeee(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d14690bb978b8b8feb70e4b7e20d7df710fc2d947124f06165b028a7c54afa0(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd2c83f3edca0d13beccb4e9b8e032121436d3bf931643c2c396d52a7193509(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ad099b133e90c22fe598d0c90f3aa8bf1d6b294c006f9fe7db465012c8597d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f7cecb87b5db5b3d765ef8f7c825843640b2d612be6373303c392e8def5d40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c37931131aba5e4c63ac4c53e35a6c98c3bafb3993bdb2252cdddedd0dc3778(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6353593ac80e5ff1e2c536823c051c9319d1ae4c3ebde778dd3ca55c672daabd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7de1face6b12d671eb5235deda919b4b97092eeb7a72a333cd723fd691839b(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7f45e3ca72ce3c29a9e770de19e01d5c38ebdf734e3d68bae9542ca9b6c74d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    approvals_required: jsii.Number,
    name: builtins.str,
    project: builtins.str,
    group_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    id: typing.Optional[builtins.str] = None,
    protected_branch_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    rule_type: typing.Optional[builtins.str] = None,
    user_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass
