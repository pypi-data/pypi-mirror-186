'''
# Terraform CDK snowflake Provider  ~> 0.40

This repo builds and publishes the Terraform snowflake Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-snowflake](https://www.npmjs.com/package/@cdktf/provider-snowflake).

`npm install @cdktf/provider-snowflake`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-snowflake](https://pypi.org/project/cdktf-cdktf-provider-snowflake).

`pipenv install cdktf-cdktf-provider-snowflake`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Snowflake](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Snowflake).

`dotnet add package HashiCorp.Cdktf.Providers.Snowflake`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-snowflake](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-snowflake).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-snowflake</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-snowflake-go`](https://github.com/cdktf/cdktf-provider-snowflake-go) package.

`go get github.com/cdktf/cdktf-provider-snowflake-go/snowflake`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-snowflake).

## Versioning

This project is explicitly not tracking the Terraform snowflake Provider version 1:1. In fact, it always tracks `latest` of ` ~> 0.40` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform snowflake Provider](https://github.com/terraform-providers/terraform-provider-snowflake)
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
    "account_grant",
    "account_parameter",
    "api_integration",
    "data_snowflake_current_account",
    "data_snowflake_current_role",
    "data_snowflake_database",
    "data_snowflake_databases",
    "data_snowflake_external_functions",
    "data_snowflake_external_tables",
    "data_snowflake_file_formats",
    "data_snowflake_functions",
    "data_snowflake_grants",
    "data_snowflake_masking_policies",
    "data_snowflake_materialized_views",
    "data_snowflake_parameters",
    "data_snowflake_pipes",
    "data_snowflake_procedures",
    "data_snowflake_resource_monitors",
    "data_snowflake_role",
    "data_snowflake_roles",
    "data_snowflake_row_access_policies",
    "data_snowflake_schemas",
    "data_snowflake_sequences",
    "data_snowflake_stages",
    "data_snowflake_storage_integrations",
    "data_snowflake_streams",
    "data_snowflake_system_generate_scim_access_token",
    "data_snowflake_system_get_aws_sns_iam_policy",
    "data_snowflake_system_get_privatelink_config",
    "data_snowflake_system_get_snowflake_platform_info",
    "data_snowflake_tables",
    "data_snowflake_tasks",
    "data_snowflake_users",
    "data_snowflake_views",
    "data_snowflake_warehouses",
    "database",
    "database_grant",
    "external_function",
    "external_oauth_integration",
    "external_table",
    "external_table_grant",
    "failover_group",
    "file_format",
    "file_format_grant",
    "function_grant",
    "function_resource",
    "integration_grant",
    "managed_account",
    "masking_policy",
    "masking_policy_grant",
    "materialized_view",
    "materialized_view_grant",
    "network_policy",
    "network_policy_attachment",
    "notification_integration",
    "oauth_integration",
    "object_parameter",
    "pipe",
    "pipe_grant",
    "procedure",
    "procedure_grant",
    "provider",
    "resource_monitor",
    "resource_monitor_grant",
    "role",
    "role_grants",
    "role_ownership_grant",
    "row_access_policy",
    "row_access_policy_grant",
    "saml_integration",
    "schema",
    "schema_grant",
    "scim_integration",
    "sequence",
    "sequence_grant",
    "session_parameter",
    "share",
    "stage",
    "stage_grant",
    "storage_integration",
    "stream",
    "stream_grant",
    "table",
    "table_constraint",
    "table_grant",
    "tag",
    "tag_association",
    "tag_grant",
    "tag_masking_policy_association",
    "task",
    "task_grant",
    "user",
    "user_grant",
    "user_ownership_grant",
    "user_public_keys",
    "view",
    "view_grant",
    "warehouse",
    "warehouse_grant",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import account_grant
from . import account_parameter
from . import api_integration
from . import data_snowflake_current_account
from . import data_snowflake_current_role
from . import data_snowflake_database
from . import data_snowflake_databases
from . import data_snowflake_external_functions
from . import data_snowflake_external_tables
from . import data_snowflake_file_formats
from . import data_snowflake_functions
from . import data_snowflake_grants
from . import data_snowflake_masking_policies
from . import data_snowflake_materialized_views
from . import data_snowflake_parameters
from . import data_snowflake_pipes
from . import data_snowflake_procedures
from . import data_snowflake_resource_monitors
from . import data_snowflake_role
from . import data_snowflake_roles
from . import data_snowflake_row_access_policies
from . import data_snowflake_schemas
from . import data_snowflake_sequences
from . import data_snowflake_stages
from . import data_snowflake_storage_integrations
from . import data_snowflake_streams
from . import data_snowflake_system_generate_scim_access_token
from . import data_snowflake_system_get_aws_sns_iam_policy
from . import data_snowflake_system_get_privatelink_config
from . import data_snowflake_system_get_snowflake_platform_info
from . import data_snowflake_tables
from . import data_snowflake_tasks
from . import data_snowflake_users
from . import data_snowflake_views
from . import data_snowflake_warehouses
from . import database
from . import database_grant
from . import external_function
from . import external_oauth_integration
from . import external_table
from . import external_table_grant
from . import failover_group
from . import file_format
from . import file_format_grant
from . import function_grant
from . import function_resource
from . import integration_grant
from . import managed_account
from . import masking_policy
from . import masking_policy_grant
from . import materialized_view
from . import materialized_view_grant
from . import network_policy
from . import network_policy_attachment
from . import notification_integration
from . import oauth_integration
from . import object_parameter
from . import pipe
from . import pipe_grant
from . import procedure
from . import procedure_grant
from . import provider
from . import resource_monitor
from . import resource_monitor_grant
from . import role
from . import role_grants
from . import role_ownership_grant
from . import row_access_policy
from . import row_access_policy_grant
from . import saml_integration
from . import schema
from . import schema_grant
from . import scim_integration
from . import sequence
from . import sequence_grant
from . import session_parameter
from . import share
from . import stage
from . import stage_grant
from . import storage_integration
from . import stream
from . import stream_grant
from . import table
from . import table_constraint
from . import table_grant
from . import tag
from . import tag_association
from . import tag_grant
from . import tag_masking_policy_association
from . import task
from . import task_grant
from . import user
from . import user_grant
from . import user_ownership_grant
from . import user_public_keys
from . import view
from . import view_grant
from . import warehouse
from . import warehouse_grant
