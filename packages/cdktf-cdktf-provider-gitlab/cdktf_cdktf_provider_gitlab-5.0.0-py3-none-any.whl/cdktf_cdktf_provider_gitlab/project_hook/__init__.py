'''
# `gitlab_project_hook`

Refer to the Terraform Registory for docs: [`gitlab_project_hook`](https://www.terraform.io/docs/providers/gitlab/r/project_hook).
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


class ProjectHook(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectHook.ProjectHook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook gitlab_project_hook}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        project: builtins.str,
        url: builtins.str,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deployment_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        push_events_branch_filter: typing.Optional[builtins.str] = None,
        releases_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook gitlab_project_hook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project: The name or id of the project to add the hook to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#project ProjectHook#project}
        :param url: The url of the hook to invoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#url ProjectHook#url}
        :param confidential_issues_events: Invoke the hook for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_issues_events ProjectHook#confidential_issues_events}
        :param confidential_note_events: Invoke the hook for confidential notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_note_events ProjectHook#confidential_note_events}
        :param deployment_events: Invoke the hook for deployment events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#deployment_events ProjectHook#deployment_events}
        :param enable_ssl_verification: Enable ssl verification when invoking the hook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#enable_ssl_verification ProjectHook#enable_ssl_verification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#id ProjectHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Invoke the hook for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#issues_events ProjectHook#issues_events}
        :param job_events: Invoke the hook for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#job_events ProjectHook#job_events}
        :param merge_requests_events: Invoke the hook for merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#merge_requests_events ProjectHook#merge_requests_events}
        :param note_events: Invoke the hook for notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#note_events ProjectHook#note_events}
        :param pipeline_events: Invoke the hook for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#pipeline_events ProjectHook#pipeline_events}
        :param push_events: Invoke the hook for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events ProjectHook#push_events}
        :param push_events_branch_filter: Invoke the hook for push events on matching branches only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events_branch_filter ProjectHook#push_events_branch_filter}
        :param releases_events: Invoke the hook for releases events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#releases_events ProjectHook#releases_events}
        :param tag_push_events: Invoke the hook for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#tag_push_events ProjectHook#tag_push_events}
        :param token: A token to present when invoking the hook. The token is not available for imported resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#token ProjectHook#token}
        :param wiki_page_events: Invoke the hook for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#wiki_page_events ProjectHook#wiki_page_events}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72fed472f7a30421e32f07c4230f793374dd7436dc25ca6ab9fed7552ac63e4a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectHookConfig(
            project=project,
            url=url,
            confidential_issues_events=confidential_issues_events,
            confidential_note_events=confidential_note_events,
            deployment_events=deployment_events,
            enable_ssl_verification=enable_ssl_verification,
            id=id,
            issues_events=issues_events,
            job_events=job_events,
            merge_requests_events=merge_requests_events,
            note_events=note_events,
            pipeline_events=pipeline_events,
            push_events=push_events,
            push_events_branch_filter=push_events_branch_filter,
            releases_events=releases_events,
            tag_push_events=tag_push_events,
            token=token,
            wiki_page_events=wiki_page_events,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConfidentialIssuesEvents")
    def reset_confidential_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialIssuesEvents", []))

    @jsii.member(jsii_name="resetConfidentialNoteEvents")
    def reset_confidential_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialNoteEvents", []))

    @jsii.member(jsii_name="resetDeploymentEvents")
    def reset_deployment_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentEvents", []))

    @jsii.member(jsii_name="resetEnableSslVerification")
    def reset_enable_ssl_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSslVerification", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuesEvents")
    def reset_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesEvents", []))

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

    @jsii.member(jsii_name="resetPushEvents")
    def reset_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEvents", []))

    @jsii.member(jsii_name="resetPushEventsBranchFilter")
    def reset_push_events_branch_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEventsBranchFilter", []))

    @jsii.member(jsii_name="resetReleasesEvents")
    def reset_releases_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReleasesEvents", []))

    @jsii.member(jsii_name="resetTagPushEvents")
    def reset_tag_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPushEvents", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWikiPageEvents")
    def reset_wiki_page_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiPageEvents", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="hookId")
    def hook_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hookId"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEventsInput")
    def confidential_issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "confidentialIssuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEventsInput")
    def confidential_note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "confidentialNoteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentEventsInput")
    def deployment_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deploymentEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSslVerificationInput")
    def enable_ssl_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableSslVerificationInput"))

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
    @jsii.member(jsii_name="pushEventsBranchFilterInput")
    def push_events_branch_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pushEventsBranchFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEventsInput")
    def push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="releasesEventsInput")
    def releases_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "releasesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPushEventsInput")
    def tag_push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tagPushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiPageEventsInput")
    def wiki_page_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "wikiPageEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEvents")
    def confidential_issues_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "confidentialIssuesEvents"))

    @confidential_issues_events.setter
    def confidential_issues_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bdfce50b64928f5871f86ad1415760d489902d8f7306b556159f79d00f9684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialIssuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEvents")
    def confidential_note_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "confidentialNoteEvents"))

    @confidential_note_events.setter
    def confidential_note_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__008b6ec2242dbcd5d9dd391d22f6ec9141b91459283742c4d41dee12e0d55102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialNoteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentEvents")
    def deployment_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deploymentEvents"))

    @deployment_events.setter
    def deployment_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923cd4ebc70fe527799849151ae208b76bf3ce1177f45e8e4d3292b67f0a901f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentEvents", value)

    @builtins.property
    @jsii.member(jsii_name="enableSslVerification")
    def enable_ssl_verification(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableSslVerification"))

    @enable_ssl_verification.setter
    def enable_ssl_verification(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db29091d16cefb74d612c55748ecdee2d8f2a1733f50bfa5994a2c0dd87a70d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSslVerification", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5716938bc1b138c329e7f1cb3592cc03bc7c0d271cd8860344ae8725ef6b423)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f121b9cee4f8c2bcf43c0c9d1748d3acf87e43b514e4860575bb57365b9802dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesEvents", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__45b2bff45f7c23e2613626b7efe151a23c0846e7be8bc9a324e4c5416aa8caca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82421a2fdbc4947756d3e8c33ac2618709f7e3857d56f57ceb5c6fdd969a2508)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14caf0458a3030ba6a569454594985454886ec489c8a29b9ef4d568f9af4488b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteEvents", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__05a2bf14e62a4ec30d7ad368da94eecef67d9ac02e26d807900930a6ffabb0fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineEvents", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a19d03693d1820daece223c69380fe52efcbbcb03421d31c0899b945804e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__b27f6e76bac8d4f0e7367e86c05044ac4d482498cf9faa77653ef8fac619eabb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="pushEventsBranchFilter")
    def push_events_branch_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pushEventsBranchFilter"))

    @push_events_branch_filter.setter
    def push_events_branch_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3baf49253b6d574883cb74547e2ccf937639406d62403b62ef4c5a11c5fad0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEventsBranchFilter", value)

    @builtins.property
    @jsii.member(jsii_name="releasesEvents")
    def releases_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "releasesEvents"))

    @releases_events.setter
    def releases_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4b44e2f83a6e414fe06016d72e35129fc9b15184e5d22a765a7d963de2224f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releasesEvents", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__fe983f44c6e6bfaa26f27d7c3075bb66c2fd6d43e6c2399b9b4ec8030f790f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc3dc59afde08dfe1e272eea957123ca21d11c99f4d284ad9110558164a0b1ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a5f930bf1b842734539c9db4dd671563b4d7d2659c3199ba63ff423ee60f8ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="wikiPageEvents")
    def wiki_page_events(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wikiPageEvents"))

    @wiki_page_events.setter
    def wiki_page_events(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74050b2811c49873f24daeb55862dc3d1c18bf917aa86316868955c7bc510b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiPageEvents", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectHook.ProjectHookConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project": "project",
        "url": "url",
        "confidential_issues_events": "confidentialIssuesEvents",
        "confidential_note_events": "confidentialNoteEvents",
        "deployment_events": "deploymentEvents",
        "enable_ssl_verification": "enableSslVerification",
        "id": "id",
        "issues_events": "issuesEvents",
        "job_events": "jobEvents",
        "merge_requests_events": "mergeRequestsEvents",
        "note_events": "noteEvents",
        "pipeline_events": "pipelineEvents",
        "push_events": "pushEvents",
        "push_events_branch_filter": "pushEventsBranchFilter",
        "releases_events": "releasesEvents",
        "tag_push_events": "tagPushEvents",
        "token": "token",
        "wiki_page_events": "wikiPageEvents",
    },
)
class ProjectHookConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        project: builtins.str,
        url: builtins.str,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        deployment_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        push_events_branch_filter: typing.Optional[builtins.str] = None,
        releases_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project: The name or id of the project to add the hook to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#project ProjectHook#project}
        :param url: The url of the hook to invoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#url ProjectHook#url}
        :param confidential_issues_events: Invoke the hook for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_issues_events ProjectHook#confidential_issues_events}
        :param confidential_note_events: Invoke the hook for confidential notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_note_events ProjectHook#confidential_note_events}
        :param deployment_events: Invoke the hook for deployment events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#deployment_events ProjectHook#deployment_events}
        :param enable_ssl_verification: Enable ssl verification when invoking the hook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#enable_ssl_verification ProjectHook#enable_ssl_verification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#id ProjectHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Invoke the hook for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#issues_events ProjectHook#issues_events}
        :param job_events: Invoke the hook for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#job_events ProjectHook#job_events}
        :param merge_requests_events: Invoke the hook for merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#merge_requests_events ProjectHook#merge_requests_events}
        :param note_events: Invoke the hook for notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#note_events ProjectHook#note_events}
        :param pipeline_events: Invoke the hook for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#pipeline_events ProjectHook#pipeline_events}
        :param push_events: Invoke the hook for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events ProjectHook#push_events}
        :param push_events_branch_filter: Invoke the hook for push events on matching branches only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events_branch_filter ProjectHook#push_events_branch_filter}
        :param releases_events: Invoke the hook for releases events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#releases_events ProjectHook#releases_events}
        :param tag_push_events: Invoke the hook for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#tag_push_events ProjectHook#tag_push_events}
        :param token: A token to present when invoking the hook. The token is not available for imported resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#token ProjectHook#token}
        :param wiki_page_events: Invoke the hook for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#wiki_page_events ProjectHook#wiki_page_events}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f59033c88363f228172052503a71ad7ecf9c4cfcf0aaf04454f5f1af3ba119)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument confidential_issues_events", value=confidential_issues_events, expected_type=type_hints["confidential_issues_events"])
            check_type(argname="argument confidential_note_events", value=confidential_note_events, expected_type=type_hints["confidential_note_events"])
            check_type(argname="argument deployment_events", value=deployment_events, expected_type=type_hints["deployment_events"])
            check_type(argname="argument enable_ssl_verification", value=enable_ssl_verification, expected_type=type_hints["enable_ssl_verification"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issues_events", value=issues_events, expected_type=type_hints["issues_events"])
            check_type(argname="argument job_events", value=job_events, expected_type=type_hints["job_events"])
            check_type(argname="argument merge_requests_events", value=merge_requests_events, expected_type=type_hints["merge_requests_events"])
            check_type(argname="argument note_events", value=note_events, expected_type=type_hints["note_events"])
            check_type(argname="argument pipeline_events", value=pipeline_events, expected_type=type_hints["pipeline_events"])
            check_type(argname="argument push_events", value=push_events, expected_type=type_hints["push_events"])
            check_type(argname="argument push_events_branch_filter", value=push_events_branch_filter, expected_type=type_hints["push_events_branch_filter"])
            check_type(argname="argument releases_events", value=releases_events, expected_type=type_hints["releases_events"])
            check_type(argname="argument tag_push_events", value=tag_push_events, expected_type=type_hints["tag_push_events"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument wiki_page_events", value=wiki_page_events, expected_type=type_hints["wiki_page_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project": project,
            "url": url,
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
        if confidential_issues_events is not None:
            self._values["confidential_issues_events"] = confidential_issues_events
        if confidential_note_events is not None:
            self._values["confidential_note_events"] = confidential_note_events
        if deployment_events is not None:
            self._values["deployment_events"] = deployment_events
        if enable_ssl_verification is not None:
            self._values["enable_ssl_verification"] = enable_ssl_verification
        if id is not None:
            self._values["id"] = id
        if issues_events is not None:
            self._values["issues_events"] = issues_events
        if job_events is not None:
            self._values["job_events"] = job_events
        if merge_requests_events is not None:
            self._values["merge_requests_events"] = merge_requests_events
        if note_events is not None:
            self._values["note_events"] = note_events
        if pipeline_events is not None:
            self._values["pipeline_events"] = pipeline_events
        if push_events is not None:
            self._values["push_events"] = push_events
        if push_events_branch_filter is not None:
            self._values["push_events_branch_filter"] = push_events_branch_filter
        if releases_events is not None:
            self._values["releases_events"] = releases_events
        if tag_push_events is not None:
            self._values["tag_push_events"] = tag_push_events
        if token is not None:
            self._values["token"] = token
        if wiki_page_events is not None:
            self._values["wiki_page_events"] = wiki_page_events

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
    def project(self) -> builtins.str:
        '''The name or id of the project to add the hook to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#project ProjectHook#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The url of the hook to invoke.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#url ProjectHook#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def confidential_issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for confidential issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_issues_events ProjectHook#confidential_issues_events}
        '''
        result = self._values.get("confidential_issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def confidential_note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for confidential notes events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#confidential_note_events ProjectHook#confidential_note_events}
        '''
        result = self._values.get("confidential_note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def deployment_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for deployment events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#deployment_events ProjectHook#deployment_events}
        '''
        result = self._values.get("deployment_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_ssl_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable ssl verification when invoking the hook.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#enable_ssl_verification ProjectHook#enable_ssl_verification}
        '''
        result = self._values.get("enable_ssl_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#id ProjectHook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#issues_events ProjectHook#issues_events}
        '''
        result = self._values.get("issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def job_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for job events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#job_events ProjectHook#job_events}
        '''
        result = self._values.get("job_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def merge_requests_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for merge requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#merge_requests_events ProjectHook#merge_requests_events}
        '''
        result = self._values.get("merge_requests_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for notes events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#note_events ProjectHook#note_events}
        '''
        result = self._values.get("note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def pipeline_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for pipeline events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#pipeline_events ProjectHook#pipeline_events}
        '''
        result = self._values.get("pipeline_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events ProjectHook#push_events}
        '''
        result = self._values.get("push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def push_events_branch_filter(self) -> typing.Optional[builtins.str]:
        '''Invoke the hook for push events on matching branches only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#push_events_branch_filter ProjectHook#push_events_branch_filter}
        '''
        result = self._values.get("push_events_branch_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def releases_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for releases events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#releases_events ProjectHook#releases_events}
        '''
        result = self._values.get("releases_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tag_push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for tag push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#tag_push_events ProjectHook#tag_push_events}
        '''
        result = self._values.get("tag_push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''A token to present when invoking the hook. The token is not available for imported resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#token ProjectHook#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_page_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Invoke the hook for wiki page events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_hook#wiki_page_events ProjectHook#wiki_page_events}
        '''
        result = self._values.get("wiki_page_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectHookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProjectHook",
    "ProjectHookConfig",
]

publication.publish()

def _typecheckingstub__72fed472f7a30421e32f07c4230f793374dd7436dc25ca6ab9fed7552ac63e4a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    project: builtins.str,
    url: builtins.str,
    confidential_issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    confidential_note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deployment_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    push_events_branch_filter: typing.Optional[builtins.str] = None,
    releases_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token: typing.Optional[builtins.str] = None,
    wiki_page_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__d0bdfce50b64928f5871f86ad1415760d489902d8f7306b556159f79d00f9684(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008b6ec2242dbcd5d9dd391d22f6ec9141b91459283742c4d41dee12e0d55102(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923cd4ebc70fe527799849151ae208b76bf3ce1177f45e8e4d3292b67f0a901f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db29091d16cefb74d612c55748ecdee2d8f2a1733f50bfa5994a2c0dd87a70d3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5716938bc1b138c329e7f1cb3592cc03bc7c0d271cd8860344ae8725ef6b423(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f121b9cee4f8c2bcf43c0c9d1748d3acf87e43b514e4860575bb57365b9802dd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b2bff45f7c23e2613626b7efe151a23c0846e7be8bc9a324e4c5416aa8caca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82421a2fdbc4947756d3e8c33ac2618709f7e3857d56f57ceb5c6fdd969a2508(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14caf0458a3030ba6a569454594985454886ec489c8a29b9ef4d568f9af4488b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a2bf14e62a4ec30d7ad368da94eecef67d9ac02e26d807900930a6ffabb0fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a19d03693d1820daece223c69380fe52efcbbcb03421d31c0899b945804e9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27f6e76bac8d4f0e7367e86c05044ac4d482498cf9faa77653ef8fac619eabb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3baf49253b6d574883cb74547e2ccf937639406d62403b62ef4c5a11c5fad0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4b44e2f83a6e414fe06016d72e35129fc9b15184e5d22a765a7d963de2224f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe983f44c6e6bfaa26f27d7c3075bb66c2fd6d43e6c2399b9b4ec8030f790f8e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc3dc59afde08dfe1e272eea957123ca21d11c99f4d284ad9110558164a0b1ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5f930bf1b842734539c9db4dd671563b4d7d2659c3199ba63ff423ee60f8ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74050b2811c49873f24daeb55862dc3d1c18bf917aa86316868955c7bc510b37(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f59033c88363f228172052503a71ad7ecf9c4cfcf0aaf04454f5f1af3ba119(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    project: builtins.str,
    url: builtins.str,
    confidential_issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    confidential_note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    deployment_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    issues_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    job_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    merge_requests_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    note_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pipeline_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    push_events_branch_filter: typing.Optional[builtins.str] = None,
    releases_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tag_push_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token: typing.Optional[builtins.str] = None,
    wiki_page_events: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
