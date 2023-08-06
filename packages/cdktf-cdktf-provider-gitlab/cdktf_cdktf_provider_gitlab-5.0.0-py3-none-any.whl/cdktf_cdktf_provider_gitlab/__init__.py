'''
# Terraform CDK gitlab Provider ~> 3.14

This repo builds and publishes the Terraform gitlab Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-gitlab](https://www.npmjs.com/package/@cdktf/provider-gitlab).

`npm install @cdktf/provider-gitlab`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-gitlab](https://pypi.org/project/cdktf-cdktf-provider-gitlab).

`pipenv install cdktf-cdktf-provider-gitlab`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Gitlab](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Gitlab).

`dotnet add package HashiCorp.Cdktf.Providers.Gitlab`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-gitlab](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-gitlab).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-gitlab</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-gitlab-go`](https://github.com/cdktf/cdktf-provider-gitlab-go) package.

`go get github.com/cdktf/cdktf-provider-gitlab-go/gitlab`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-gitlab).

## Versioning

This project is explicitly not tracking the Terraform gitlab Provider version 1:1. In fact, it always tracks `latest` of `~> 3.14` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform gitlab Provider](https://github.com/terraform-providers/terraform-provider-gitlab)
* [Terraform Engine](https://terraform.io)

If there are breaking changes (backward incompatible) in any of the above, the major version of this project will be bumped.

## Features / Issues / Bugs

Please report bugs and issues to the [terraform cdk](https://cdk.tf) project:

* [Create bug report](https://cdk.tf/bug)
* [Create feature request](https://cdk.tf/feature)

## Contributing

### projen

This is mostly based on [projen](https://github.com/eladb/projen), which takes care of generating the entire repository.

### cdktf-provider-project based on projen

There's a custom [project builder](https://github.com/hashicorp/cdktf-provider-project) which encapsulate the common settings for all `cdktf` providers.

### Provider Version

The provider version can be adjusted in [./.projenrc.js](./.projenrc.js).

### Repository Management

The repository is managed by [Repository Manager](https://github.com/hashicorp/cdktf-repository-manager/)
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

from ._jsii import *

__all__ = [
    "application_settings",
    "branch",
    "branch_protection",
    "cluster_agent",
    "cluster_agent_token",
    "data_gitlab_branch",
    "data_gitlab_cluster_agent",
    "data_gitlab_cluster_agents",
    "data_gitlab_current_user",
    "data_gitlab_group",
    "data_gitlab_group_hook",
    "data_gitlab_group_hooks",
    "data_gitlab_group_membership",
    "data_gitlab_group_subgroups",
    "data_gitlab_group_variable",
    "data_gitlab_group_variables",
    "data_gitlab_groups",
    "data_gitlab_instance_deploy_keys",
    "data_gitlab_instance_variable",
    "data_gitlab_instance_variables",
    "data_gitlab_project",
    "data_gitlab_project_branches",
    "data_gitlab_project_hook",
    "data_gitlab_project_hooks",
    "data_gitlab_project_issue",
    "data_gitlab_project_issues",
    "data_gitlab_project_membership",
    "data_gitlab_project_milestone",
    "data_gitlab_project_milestones",
    "data_gitlab_project_protected_branch",
    "data_gitlab_project_protected_branches",
    "data_gitlab_project_tag",
    "data_gitlab_project_tags",
    "data_gitlab_project_variable",
    "data_gitlab_project_variables",
    "data_gitlab_projects",
    "data_gitlab_release_link",
    "data_gitlab_release_links",
    "data_gitlab_repository_file",
    "data_gitlab_repository_tree",
    "data_gitlab_user",
    "data_gitlab_user_sshkeys",
    "data_gitlab_users",
    "deploy_key",
    "deploy_key_enable",
    "deploy_token",
    "group",
    "group_access_token",
    "group_badge",
    "group_cluster",
    "group_custom_attribute",
    "group_hook",
    "group_label",
    "group_ldap_link",
    "group_membership",
    "group_project_file_template",
    "group_saml_link",
    "group_share_group",
    "group_variable",
    "instance_cluster",
    "instance_variable",
    "label",
    "managed_license",
    "personal_access_token",
    "pipeline_schedule",
    "pipeline_schedule_variable",
    "pipeline_trigger",
    "project",
    "project_access_token",
    "project_approval_rule",
    "project_badge",
    "project_cluster",
    "project_custom_attribute",
    "project_environment",
    "project_freeze_period",
    "project_hook",
    "project_issue",
    "project_issue_board",
    "project_level_mr_approvals",
    "project_membership",
    "project_milestone",
    "project_mirror",
    "project_protected_environment",
    "project_runner_enablement",
    "project_share_group",
    "project_tag",
    "project_variable",
    "provider",
    "release_link",
    "repository_file",
    "runner",
    "service_emails_on_push",
    "service_external_wiki",
    "service_github",
    "service_jira",
    "service_microsoft_teams",
    "service_pipelines_email",
    "service_slack",
    "system_hook",
    "tag_protection",
    "topic",
    "user",
    "user_custom_attribute",
    "user_gpgkey",
    "user_sshkey",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import application_settings
from . import branch
from . import branch_protection
from . import cluster_agent
from . import cluster_agent_token
from . import data_gitlab_branch
from . import data_gitlab_cluster_agent
from . import data_gitlab_cluster_agents
from . import data_gitlab_current_user
from . import data_gitlab_group
from . import data_gitlab_group_hook
from . import data_gitlab_group_hooks
from . import data_gitlab_group_membership
from . import data_gitlab_group_subgroups
from . import data_gitlab_group_variable
from . import data_gitlab_group_variables
from . import data_gitlab_groups
from . import data_gitlab_instance_deploy_keys
from . import data_gitlab_instance_variable
from . import data_gitlab_instance_variables
from . import data_gitlab_project
from . import data_gitlab_project_branches
from . import data_gitlab_project_hook
from . import data_gitlab_project_hooks
from . import data_gitlab_project_issue
from . import data_gitlab_project_issues
from . import data_gitlab_project_membership
from . import data_gitlab_project_milestone
from . import data_gitlab_project_milestones
from . import data_gitlab_project_protected_branch
from . import data_gitlab_project_protected_branches
from . import data_gitlab_project_tag
from . import data_gitlab_project_tags
from . import data_gitlab_project_variable
from . import data_gitlab_project_variables
from . import data_gitlab_projects
from . import data_gitlab_release_link
from . import data_gitlab_release_links
from . import data_gitlab_repository_file
from . import data_gitlab_repository_tree
from . import data_gitlab_user
from . import data_gitlab_user_sshkeys
from . import data_gitlab_users
from . import deploy_key
from . import deploy_key_enable
from . import deploy_token
from . import group
from . import group_access_token
from . import group_badge
from . import group_cluster
from . import group_custom_attribute
from . import group_hook
from . import group_label
from . import group_ldap_link
from . import group_membership
from . import group_project_file_template
from . import group_saml_link
from . import group_share_group
from . import group_variable
from . import instance_cluster
from . import instance_variable
from . import label
from . import managed_license
from . import personal_access_token
from . import pipeline_schedule
from . import pipeline_schedule_variable
from . import pipeline_trigger
from . import project
from . import project_access_token
from . import project_approval_rule
from . import project_badge
from . import project_cluster
from . import project_custom_attribute
from . import project_environment
from . import project_freeze_period
from . import project_hook
from . import project_issue
from . import project_issue_board
from . import project_level_mr_approvals
from . import project_membership
from . import project_milestone
from . import project_mirror
from . import project_protected_environment
from . import project_runner_enablement
from . import project_share_group
from . import project_tag
from . import project_variable
from . import provider
from . import release_link
from . import repository_file
from . import runner
from . import service_emails_on_push
from . import service_external_wiki
from . import service_github
from . import service_jira
from . import service_microsoft_teams
from . import service_pipelines_email
from . import service_slack
from . import system_hook
from . import tag_protection
from . import topic
from . import user
from . import user_custom_attribute
from . import user_gpgkey
from . import user_sshkey
