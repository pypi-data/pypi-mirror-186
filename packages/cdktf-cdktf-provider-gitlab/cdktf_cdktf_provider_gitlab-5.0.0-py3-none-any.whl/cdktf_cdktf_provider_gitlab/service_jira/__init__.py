'''
# `gitlab_service_jira`

Refer to the Terraform Registory for docs: [`gitlab_service_jira`](https://www.terraform.io/docs/providers/gitlab/r/service_jira).
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


class ServiceJira(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.serviceJira.ServiceJira",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira gitlab_service_jira}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        password: builtins.str,
        project: builtins.str,
        url: builtins.str,
        username: builtins.str,
        api_url: typing.Optional[builtins.str] = None,
        comment_on_event_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        commit_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        jira_issue_transition_id: typing.Optional[builtins.str] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_key: typing.Optional[builtins.str] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira gitlab_service_jira} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param password: The password of the user created to be used with GitLab/JIRA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#password ServiceJira#password}
        :param project: ID of the project you want to activate integration on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project ServiceJira#project}
        :param url: The URL to the JIRA project which is being linked to this GitLab project. For example, https://jira.example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#url ServiceJira#url}
        :param username: The username of the user created to be used with GitLab/JIRA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#username ServiceJira#username}
        :param api_url: The base URL to the Jira instance API. Web URL value is used if not set. For example, https://jira-api.example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#api_url ServiceJira#api_url}
        :param comment_on_event_enabled: Enable comments inside Jira issues on each GitLab event (commit / merge request). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#comment_on_event_enabled ServiceJira#comment_on_event_enabled}
        :param commit_events: Enable notifications for commit events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#commit_events ServiceJira#commit_events}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#id ServiceJira#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Enable notifications for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#issues_events ServiceJira#issues_events}
        :param jira_issue_transition_id: The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration > Issues > Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2. *Note**: importing this field is only supported since GitLab 15.2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#jira_issue_transition_id ServiceJira#jira_issue_transition_id}
        :param job_events: Enable notifications for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#job_events ServiceJira#job_events}
        :param merge_requests_events: Enable notifications for merge request events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#merge_requests_events ServiceJira#merge_requests_events}
        :param note_events: Enable notifications for note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#note_events ServiceJira#note_events}
        :param pipeline_events: Enable notifications for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#pipeline_events ServiceJira#pipeline_events}
        :param project_key: The short identifier for your JIRA project, all uppercase, e.g., PROJ. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project_key ServiceJira#project_key}
        :param push_events: Enable notifications for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#push_events ServiceJira#push_events}
        :param tag_push_events: Enable notifications for tag_push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#tag_push_events ServiceJira#tag_push_events}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86aa6319e4e2ba83a10c1a2d0e6ce7b4ca5b29fd14dcd3d12774a410fb23a7db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceJiraConfig(
            password=password,
            project=project,
            url=url,
            username=username,
            api_url=api_url,
            comment_on_event_enabled=comment_on_event_enabled,
            commit_events=commit_events,
            id=id,
            issues_events=issues_events,
            jira_issue_transition_id=jira_issue_transition_id,
            job_events=job_events,
            merge_requests_events=merge_requests_events,
            note_events=note_events,
            pipeline_events=pipeline_events,
            project_key=project_key,
            push_events=push_events,
            tag_push_events=tag_push_events,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetApiUrl")
    def reset_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUrl", []))

    @jsii.member(jsii_name="resetCommentOnEventEnabled")
    def reset_comment_on_event_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommentOnEventEnabled", []))

    @jsii.member(jsii_name="resetCommitEvents")
    def reset_commit_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitEvents", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuesEvents")
    def reset_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesEvents", []))

    @jsii.member(jsii_name="resetJiraIssueTransitionId")
    def reset_jira_issue_transition_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJiraIssueTransitionId", []))

    @jsii.member(jsii_name="resetJobEvents")
    def reset_job_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobEvents", []))

    @jsii.member(jsii_name="resetMergeRequestsEvents")
    def reset_merge_requests_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsEvents", []))

    @jsii.member(jsii_name="resetNoteEvents")
    def reset_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoteEvents", []))

    @jsii.member(jsii_name="resetPipelineEvents")
    def reset_pipeline_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineEvents", []))

    @jsii.member(jsii_name="resetProjectKey")
    def reset_project_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectKey", []))

    @jsii.member(jsii_name="resetPushEvents")
    def reset_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEvents", []))

    @jsii.member(jsii_name="resetTagPushEvents")
    def reset_tag_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPushEvents", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "active"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="apiUrlInput")
    def api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="commentOnEventEnabledInput")
    def comment_on_event_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "commentOnEventEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="commitEventsInput")
    def commit_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "commitEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesEventsInput")
    def issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "issuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="jiraIssueTransitionIdInput")
    def jira_issue_transition_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jiraIssueTransitionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jobEventsInput")
    def job_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "jobEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEventsInput")
    def merge_requests_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mergeRequestsEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="noteEventsInput")
    def note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineEventsInput")
    def pipeline_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pipelineEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="projectKeyInput")
    def project_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEventsInput")
    def push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPushEventsInput")
    def tag_push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tagPushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUrl")
    def api_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiUrl"))

    @api_url.setter
    def api_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df5da237ad58254784f7d0b9fe7e47b5c309261ca1fe943f7f1226d80acfbee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="commentOnEventEnabled")
    def comment_on_event_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "commentOnEventEnabled"))

    @comment_on_event_enabled.setter
    def comment_on_event_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30df50b39e929792d68bf4274141458bc6cf3f97178c0eca5baf7b4aa919b5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commentOnEventEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="commitEvents")
    def commit_events(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "commitEvents"))

    @commit_events.setter
    def commit_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50a799744161ce615ed9752e4293cc21fafd52c2edd63ccc4e3760f8b6777e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitEvents", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f41fda6394e0a35951c6ce8c4852d0a793359c55f5e5ce6904c0c5b9569169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issuesEvents")
    def issues_events(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "issuesEvents"))

    @issues_events.setter
    def issues_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c02a56d60f6e7d005df92ef0c92f42425a0ea709ad0aa30769eea7215a353bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="jiraIssueTransitionId")
    def jira_issue_transition_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jiraIssueTransitionId"))

    @jira_issue_transition_id.setter
    def jira_issue_transition_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ad7d744d3cd7278ee2fc1146f60b1706b85120620ff49867cc6279b594ca75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jiraIssueTransitionId", value)

    @builtins.property
    @jsii.member(jsii_name="jobEvents")
    def job_events(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "jobEvents"))

    @job_events.setter
    def job_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f9cd924d1f8c533df981970d686192bd5ca573cd70aac6d4d14a3f6c7880ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobEvents", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEvents")
    def merge_requests_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mergeRequestsEvents"))

    @merge_requests_events.setter
    def merge_requests_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564575ec8b91a860799ecffb6d56bb2dd951d783fbaba4e616c01bb90ac801f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsEvents", value)

    @builtins.property
    @jsii.member(jsii_name="noteEvents")
    def note_events(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noteEvents"))

    @note_events.setter
    def note_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff5ffdadae9c01c00b92909f3c4d1a77f49c588d19af500817d1a21249bce65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e96faf3ab6fbc714477ccdf4bfe16af7a39dc44c0b3259f1b364a5a3e1e835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineEvents")
    def pipeline_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "pipelineEvents"))

    @pipeline_events.setter
    def pipeline_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa5614b4dac682a3295f61c22ced69a4157b7efa610f8e512b8339880b3ca97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineEvents", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5a11b263ec1299d8e0875ade65209bdb76f5243ec50316c948f0a749c53c822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="projectKey")
    def project_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectKey"))

    @project_key.setter
    def project_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381a8d552b32fe27d8adcc5e404ab33efaabba1ad09105c4a5b035091819a053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectKey", value)

    @builtins.property
    @jsii.member(jsii_name="pushEvents")
    def push_events(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "pushEvents"))

    @push_events.setter
    def push_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__493eceb9c2e2befc6662108c9676123807e31fc81b8a2a37e4145d4074c973fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="tagPushEvents")
    def tag_push_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tagPushEvents"))

    @tag_push_events.setter
    def tag_push_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a501cdaa6d7a3d9b7e2275525ccdbc3b4846837007f38b354266cae426981bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2d9e14960bb5c0c7c9bd8c48444eedb51d3fc798d96116bbdcb9ef448a9621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0757c7ea8c28108bd39e69ddd10e4829f475461fd38e46f23ffcc6a0f30f201a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.serviceJira.ServiceJiraConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "password": "password",
        "project": "project",
        "url": "url",
        "username": "username",
        "api_url": "apiUrl",
        "comment_on_event_enabled": "commentOnEventEnabled",
        "commit_events": "commitEvents",
        "id": "id",
        "issues_events": "issuesEvents",
        "jira_issue_transition_id": "jiraIssueTransitionId",
        "job_events": "jobEvents",
        "merge_requests_events": "mergeRequestsEvents",
        "note_events": "noteEvents",
        "pipeline_events": "pipelineEvents",
        "project_key": "projectKey",
        "push_events": "pushEvents",
        "tag_push_events": "tagPushEvents",
    },
)
class ServiceJiraConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        password: builtins.str,
        project: builtins.str,
        url: builtins.str,
        username: builtins.str,
        api_url: typing.Optional[builtins.str] = None,
        comment_on_event_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        commit_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        jira_issue_transition_id: typing.Optional[builtins.str] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        project_key: typing.Optional[builtins.str] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param password: The password of the user created to be used with GitLab/JIRA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#password ServiceJira#password}
        :param project: ID of the project you want to activate integration on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project ServiceJira#project}
        :param url: The URL to the JIRA project which is being linked to this GitLab project. For example, https://jira.example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#url ServiceJira#url}
        :param username: The username of the user created to be used with GitLab/JIRA. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#username ServiceJira#username}
        :param api_url: The base URL to the Jira instance API. Web URL value is used if not set. For example, https://jira-api.example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#api_url ServiceJira#api_url}
        :param comment_on_event_enabled: Enable comments inside Jira issues on each GitLab event (commit / merge request). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#comment_on_event_enabled ServiceJira#comment_on_event_enabled}
        :param commit_events: Enable notifications for commit events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#commit_events ServiceJira#commit_events}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#id ServiceJira#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Enable notifications for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#issues_events ServiceJira#issues_events}
        :param jira_issue_transition_id: The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration > Issues > Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2. *Note**: importing this field is only supported since GitLab 15.2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#jira_issue_transition_id ServiceJira#jira_issue_transition_id}
        :param job_events: Enable notifications for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#job_events ServiceJira#job_events}
        :param merge_requests_events: Enable notifications for merge request events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#merge_requests_events ServiceJira#merge_requests_events}
        :param note_events: Enable notifications for note events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#note_events ServiceJira#note_events}
        :param pipeline_events: Enable notifications for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#pipeline_events ServiceJira#pipeline_events}
        :param project_key: The short identifier for your JIRA project, all uppercase, e.g., PROJ. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project_key ServiceJira#project_key}
        :param push_events: Enable notifications for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#push_events ServiceJira#push_events}
        :param tag_push_events: Enable notifications for tag_push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#tag_push_events ServiceJira#tag_push_events}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b126cddc07e63985584ed9325c10c57833061e6962b3ece3124c2ba5a0c2d10f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument api_url", value=api_url, expected_type=type_hints["api_url"])
            check_type(argname="argument comment_on_event_enabled", value=comment_on_event_enabled, expected_type=type_hints["comment_on_event_enabled"])
            check_type(argname="argument commit_events", value=commit_events, expected_type=type_hints["commit_events"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issues_events", value=issues_events, expected_type=type_hints["issues_events"])
            check_type(argname="argument jira_issue_transition_id", value=jira_issue_transition_id, expected_type=type_hints["jira_issue_transition_id"])
            check_type(argname="argument job_events", value=job_events, expected_type=type_hints["job_events"])
            check_type(argname="argument merge_requests_events", value=merge_requests_events, expected_type=type_hints["merge_requests_events"])
            check_type(argname="argument note_events", value=note_events, expected_type=type_hints["note_events"])
            check_type(argname="argument pipeline_events", value=pipeline_events, expected_type=type_hints["pipeline_events"])
            check_type(argname="argument project_key", value=project_key, expected_type=type_hints["project_key"])
            check_type(argname="argument push_events", value=push_events, expected_type=type_hints["push_events"])
            check_type(argname="argument tag_push_events", value=tag_push_events, expected_type=type_hints["tag_push_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "project": project,
            "url": url,
            "username": username,
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
        if api_url is not None:
            self._values["api_url"] = api_url
        if comment_on_event_enabled is not None:
            self._values["comment_on_event_enabled"] = comment_on_event_enabled
        if commit_events is not None:
            self._values["commit_events"] = commit_events
        if id is not None:
            self._values["id"] = id
        if issues_events is not None:
            self._values["issues_events"] = issues_events
        if jira_issue_transition_id is not None:
            self._values["jira_issue_transition_id"] = jira_issue_transition_id
        if job_events is not None:
            self._values["job_events"] = job_events
        if merge_requests_events is not None:
            self._values["merge_requests_events"] = merge_requests_events
        if note_events is not None:
            self._values["note_events"] = note_events
        if pipeline_events is not None:
            self._values["pipeline_events"] = pipeline_events
        if project_key is not None:
            self._values["project_key"] = project_key
        if push_events is not None:
            self._values["push_events"] = push_events
        if tag_push_events is not None:
            self._values["tag_push_events"] = tag_push_events

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
    def password(self) -> builtins.str:
        '''The password of the user created to be used with GitLab/JIRA.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#password ServiceJira#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''ID of the project you want to activate integration on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project ServiceJira#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL to the JIRA project which is being linked to this GitLab project. For example, https://jira.example.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#url ServiceJira#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The username of the user created to be used with GitLab/JIRA.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#username ServiceJira#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_url(self) -> typing.Optional[builtins.str]:
        '''The base URL to the Jira instance API. Web URL value is used if not set. For example, https://jira-api.example.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#api_url ServiceJira#api_url}
        '''
        result = self._values.get("api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment_on_event_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable comments inside Jira issues on each GitLab event (commit / merge request).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#comment_on_event_enabled ServiceJira#comment_on_event_enabled}
        '''
        result = self._values.get("comment_on_event_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def commit_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for commit events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#commit_events ServiceJira#commit_events}
        '''
        result = self._values.get("commit_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#id ServiceJira#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#issues_events ServiceJira#issues_events}
        '''
        result = self._values.get("issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def jira_issue_transition_id(self) -> typing.Optional[builtins.str]:
        '''The ID of a transition that moves issues to a closed state.

        You can find this number under the JIRA workflow administration (Administration > Issues > Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2. *Note**: importing this field is only supported since GitLab 15.2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#jira_issue_transition_id ServiceJira#jira_issue_transition_id}
        '''
        result = self._values.get("jira_issue_transition_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for job events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#job_events ServiceJira#job_events}
        '''
        result = self._values.get("job_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def merge_requests_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for merge request events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#merge_requests_events ServiceJira#merge_requests_events}
        '''
        result = self._values.get("merge_requests_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for note events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#note_events ServiceJira#note_events}
        '''
        result = self._values.get("note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def pipeline_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for pipeline events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#pipeline_events ServiceJira#pipeline_events}
        '''
        result = self._values.get("pipeline_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def project_key(self) -> typing.Optional[builtins.str]:
        '''The short identifier for your JIRA project, all uppercase, e.g., PROJ.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#project_key ServiceJira#project_key}
        '''
        result = self._values.get("project_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#push_events ServiceJira#push_events}
        '''
        result = self._values.get("push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tag_push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notifications for tag_push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/service_jira#tag_push_events ServiceJira#tag_push_events}
        '''
        result = self._values.get("tag_push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceJiraConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ServiceJira",
    "ServiceJiraConfig",
]

publication.publish()

def _typecheckingstub__86aa6319e4e2ba83a10c1a2d0e6ce7b4ca5b29fd14dcd3d12774a410fb23a7db(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    password: builtins.str,
    project: builtins.str,
    url: builtins.str,
    username: builtins.str,
    api_url: typing.Optional[builtins.str] = None,
    comment_on_event_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    commit_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    jira_issue_transition_id: typing.Optional[builtins.str] = None,
    job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_key: typing.Optional[builtins.str] = None,
    push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__3df5da237ad58254784f7d0b9fe7e47b5c309261ca1fe943f7f1226d80acfbee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30df50b39e929792d68bf4274141458bc6cf3f97178c0eca5baf7b4aa919b5b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50a799744161ce615ed9752e4293cc21fafd52c2edd63ccc4e3760f8b6777e6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f41fda6394e0a35951c6ce8c4852d0a793359c55f5e5ce6904c0c5b9569169(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c02a56d60f6e7d005df92ef0c92f42425a0ea709ad0aa30769eea7215a353bd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ad7d744d3cd7278ee2fc1146f60b1706b85120620ff49867cc6279b594ca75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f9cd924d1f8c533df981970d686192bd5ca573cd70aac6d4d14a3f6c7880ee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564575ec8b91a860799ecffb6d56bb2dd951d783fbaba4e616c01bb90ac801f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff5ffdadae9c01c00b92909f3c4d1a77f49c588d19af500817d1a21249bce65c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e96faf3ab6fbc714477ccdf4bfe16af7a39dc44c0b3259f1b364a5a3e1e835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa5614b4dac682a3295f61c22ced69a4157b7efa610f8e512b8339880b3ca97(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5a11b263ec1299d8e0875ade65209bdb76f5243ec50316c948f0a749c53c822(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381a8d552b32fe27d8adcc5e404ab33efaabba1ad09105c4a5b035091819a053(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493eceb9c2e2befc6662108c9676123807e31fc81b8a2a37e4145d4074c973fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a501cdaa6d7a3d9b7e2275525ccdbc3b4846837007f38b354266cae426981bbf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2d9e14960bb5c0c7c9bd8c48444eedb51d3fc798d96116bbdcb9ef448a9621(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0757c7ea8c28108bd39e69ddd10e4829f475461fd38e46f23ffcc6a0f30f201a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b126cddc07e63985584ed9325c10c57833061e6962b3ece3124c2ba5a0c2d10f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    password: builtins.str,
    project: builtins.str,
    url: builtins.str,
    username: builtins.str,
    api_url: typing.Optional[builtins.str] = None,
    comment_on_event_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    commit_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    jira_issue_transition_id: typing.Optional[builtins.str] = None,
    job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    project_key: typing.Optional[builtins.str] = None,
    push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
