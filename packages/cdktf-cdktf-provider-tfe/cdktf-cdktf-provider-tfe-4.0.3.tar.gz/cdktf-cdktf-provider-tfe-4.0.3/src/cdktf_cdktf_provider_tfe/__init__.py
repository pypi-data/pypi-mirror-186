'''
# Terraform CDK tfe Provider ~> 0.33

This repo builds and publishes the Terraform tfe Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-tfe](https://www.npmjs.com/package/@cdktf/provider-tfe).

`npm install @cdktf/provider-tfe`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-tfe](https://pypi.org/project/cdktf-cdktf-provider-tfe).

`pipenv install cdktf-cdktf-provider-tfe`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Tfe](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Tfe).

`dotnet add package HashiCorp.Cdktf.Providers.Tfe`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-tfe](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-tfe).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-tfe</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-tfe-go`](https://github.com/cdktf/cdktf-provider-tfe-go) package.

`go get github.com/cdktf/cdktf-provider-tfe-go/tfe`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-tfe).

## Versioning

This project is explicitly not tracking the Terraform tfe Provider version 1:1. In fact, it always tracks `latest` of `~> 0.33` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform tfe Provider](https://github.com/terraform-providers/terraform-provider-tfe)
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
    "admin_organization_settings",
    "agent_pool",
    "agent_token",
    "data_tfe_agent_pool",
    "data_tfe_ip_ranges",
    "data_tfe_oauth_client",
    "data_tfe_organization",
    "data_tfe_organization_members",
    "data_tfe_organization_membership",
    "data_tfe_organization_run_task",
    "data_tfe_organizations",
    "data_tfe_outputs",
    "data_tfe_policy_set",
    "data_tfe_slug",
    "data_tfe_ssh_key",
    "data_tfe_team",
    "data_tfe_team_access",
    "data_tfe_variable_set",
    "data_tfe_variables",
    "data_tfe_workspace",
    "data_tfe_workspace_ids",
    "data_tfe_workspace_run_task",
    "notification_configuration",
    "oauth_client",
    "organization",
    "organization_membership",
    "organization_module_sharing",
    "organization_run_task",
    "organization_token",
    "policy",
    "policy_set",
    "policy_set_parameter",
    "project",
    "provider",
    "registry_module",
    "run_trigger",
    "sentinel_policy",
    "ssh_key",
    "team",
    "team_access",
    "team_member",
    "team_members",
    "team_organization_member",
    "team_organization_members",
    "team_token",
    "terraform_version",
    "variable",
    "variable_set",
    "workspace",
    "workspace_policy_set",
    "workspace_run_task",
    "workspace_variable_set",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import admin_organization_settings
from . import agent_pool
from . import agent_token
from . import data_tfe_agent_pool
from . import data_tfe_ip_ranges
from . import data_tfe_oauth_client
from . import data_tfe_organization
from . import data_tfe_organization_members
from . import data_tfe_organization_membership
from . import data_tfe_organization_run_task
from . import data_tfe_organizations
from . import data_tfe_outputs
from . import data_tfe_policy_set
from . import data_tfe_slug
from . import data_tfe_ssh_key
from . import data_tfe_team
from . import data_tfe_team_access
from . import data_tfe_variable_set
from . import data_tfe_variables
from . import data_tfe_workspace
from . import data_tfe_workspace_ids
from . import data_tfe_workspace_run_task
from . import notification_configuration
from . import oauth_client
from . import organization
from . import organization_membership
from . import organization_module_sharing
from . import organization_run_task
from . import organization_token
from . import policy
from . import policy_set
from . import policy_set_parameter
from . import project
from . import provider
from . import registry_module
from . import run_trigger
from . import sentinel_policy
from . import ssh_key
from . import team
from . import team_access
from . import team_member
from . import team_members
from . import team_organization_member
from . import team_organization_members
from . import team_token
from . import terraform_version
from . import variable
from . import variable_set
from . import workspace
from . import workspace_policy_set
from . import workspace_run_task
from . import workspace_variable_set
