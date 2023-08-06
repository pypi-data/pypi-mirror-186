import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-gitlab",
    "version": "5.0.0",
    "description": "Prebuilt gitlab Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-gitlab.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-gitlab.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_gitlab",
        "cdktf_cdktf_provider_gitlab._jsii",
        "cdktf_cdktf_provider_gitlab.application_settings",
        "cdktf_cdktf_provider_gitlab.branch",
        "cdktf_cdktf_provider_gitlab.branch_protection",
        "cdktf_cdktf_provider_gitlab.cluster_agent",
        "cdktf_cdktf_provider_gitlab.cluster_agent_token",
        "cdktf_cdktf_provider_gitlab.data_gitlab_branch",
        "cdktf_cdktf_provider_gitlab.data_gitlab_cluster_agent",
        "cdktf_cdktf_provider_gitlab.data_gitlab_cluster_agents",
        "cdktf_cdktf_provider_gitlab.data_gitlab_current_user",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_hook",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_hooks",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_membership",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_subgroups",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_variable",
        "cdktf_cdktf_provider_gitlab.data_gitlab_group_variables",
        "cdktf_cdktf_provider_gitlab.data_gitlab_groups",
        "cdktf_cdktf_provider_gitlab.data_gitlab_instance_deploy_keys",
        "cdktf_cdktf_provider_gitlab.data_gitlab_instance_variable",
        "cdktf_cdktf_provider_gitlab.data_gitlab_instance_variables",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_branches",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_hook",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_hooks",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_issue",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_issues",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_membership",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_milestone",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_milestones",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_protected_branch",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_protected_branches",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_tag",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_tags",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_variable",
        "cdktf_cdktf_provider_gitlab.data_gitlab_project_variables",
        "cdktf_cdktf_provider_gitlab.data_gitlab_projects",
        "cdktf_cdktf_provider_gitlab.data_gitlab_release_link",
        "cdktf_cdktf_provider_gitlab.data_gitlab_release_links",
        "cdktf_cdktf_provider_gitlab.data_gitlab_repository_file",
        "cdktf_cdktf_provider_gitlab.data_gitlab_repository_tree",
        "cdktf_cdktf_provider_gitlab.data_gitlab_user",
        "cdktf_cdktf_provider_gitlab.data_gitlab_user_sshkeys",
        "cdktf_cdktf_provider_gitlab.data_gitlab_users",
        "cdktf_cdktf_provider_gitlab.deploy_key",
        "cdktf_cdktf_provider_gitlab.deploy_key_enable",
        "cdktf_cdktf_provider_gitlab.deploy_token",
        "cdktf_cdktf_provider_gitlab.group",
        "cdktf_cdktf_provider_gitlab.group_access_token",
        "cdktf_cdktf_provider_gitlab.group_badge",
        "cdktf_cdktf_provider_gitlab.group_cluster",
        "cdktf_cdktf_provider_gitlab.group_custom_attribute",
        "cdktf_cdktf_provider_gitlab.group_hook",
        "cdktf_cdktf_provider_gitlab.group_label",
        "cdktf_cdktf_provider_gitlab.group_ldap_link",
        "cdktf_cdktf_provider_gitlab.group_membership",
        "cdktf_cdktf_provider_gitlab.group_project_file_template",
        "cdktf_cdktf_provider_gitlab.group_saml_link",
        "cdktf_cdktf_provider_gitlab.group_share_group",
        "cdktf_cdktf_provider_gitlab.group_variable",
        "cdktf_cdktf_provider_gitlab.instance_cluster",
        "cdktf_cdktf_provider_gitlab.instance_variable",
        "cdktf_cdktf_provider_gitlab.label",
        "cdktf_cdktf_provider_gitlab.managed_license",
        "cdktf_cdktf_provider_gitlab.personal_access_token",
        "cdktf_cdktf_provider_gitlab.pipeline_schedule",
        "cdktf_cdktf_provider_gitlab.pipeline_schedule_variable",
        "cdktf_cdktf_provider_gitlab.pipeline_trigger",
        "cdktf_cdktf_provider_gitlab.project",
        "cdktf_cdktf_provider_gitlab.project_access_token",
        "cdktf_cdktf_provider_gitlab.project_approval_rule",
        "cdktf_cdktf_provider_gitlab.project_badge",
        "cdktf_cdktf_provider_gitlab.project_cluster",
        "cdktf_cdktf_provider_gitlab.project_custom_attribute",
        "cdktf_cdktf_provider_gitlab.project_environment",
        "cdktf_cdktf_provider_gitlab.project_freeze_period",
        "cdktf_cdktf_provider_gitlab.project_hook",
        "cdktf_cdktf_provider_gitlab.project_issue",
        "cdktf_cdktf_provider_gitlab.project_issue_board",
        "cdktf_cdktf_provider_gitlab.project_level_mr_approvals",
        "cdktf_cdktf_provider_gitlab.project_membership",
        "cdktf_cdktf_provider_gitlab.project_milestone",
        "cdktf_cdktf_provider_gitlab.project_mirror",
        "cdktf_cdktf_provider_gitlab.project_protected_environment",
        "cdktf_cdktf_provider_gitlab.project_runner_enablement",
        "cdktf_cdktf_provider_gitlab.project_share_group",
        "cdktf_cdktf_provider_gitlab.project_tag",
        "cdktf_cdktf_provider_gitlab.project_variable",
        "cdktf_cdktf_provider_gitlab.provider",
        "cdktf_cdktf_provider_gitlab.release_link",
        "cdktf_cdktf_provider_gitlab.repository_file",
        "cdktf_cdktf_provider_gitlab.runner",
        "cdktf_cdktf_provider_gitlab.service_emails_on_push",
        "cdktf_cdktf_provider_gitlab.service_external_wiki",
        "cdktf_cdktf_provider_gitlab.service_github",
        "cdktf_cdktf_provider_gitlab.service_jira",
        "cdktf_cdktf_provider_gitlab.service_microsoft_teams",
        "cdktf_cdktf_provider_gitlab.service_pipelines_email",
        "cdktf_cdktf_provider_gitlab.service_slack",
        "cdktf_cdktf_provider_gitlab.system_hook",
        "cdktf_cdktf_provider_gitlab.tag_protection",
        "cdktf_cdktf_provider_gitlab.topic",
        "cdktf_cdktf_provider_gitlab.user",
        "cdktf_cdktf_provider_gitlab.user_custom_attribute",
        "cdktf_cdktf_provider_gitlab.user_gpgkey",
        "cdktf_cdktf_provider_gitlab.user_sshkey"
    ],
    "package_data": {
        "cdktf_cdktf_provider_gitlab._jsii": [
            "provider-gitlab@5.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_gitlab": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.15.0, <0.16.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.73.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
