import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-snowflake",
    "version": "4.0.4",
    "description": "Prebuilt snowflake Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-snowflake.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-snowflake.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_snowflake",
        "cdktf_cdktf_provider_snowflake._jsii",
        "cdktf_cdktf_provider_snowflake.account_grant",
        "cdktf_cdktf_provider_snowflake.account_parameter",
        "cdktf_cdktf_provider_snowflake.api_integration",
        "cdktf_cdktf_provider_snowflake.data_snowflake_current_account",
        "cdktf_cdktf_provider_snowflake.data_snowflake_current_role",
        "cdktf_cdktf_provider_snowflake.data_snowflake_database",
        "cdktf_cdktf_provider_snowflake.data_snowflake_databases",
        "cdktf_cdktf_provider_snowflake.data_snowflake_external_functions",
        "cdktf_cdktf_provider_snowflake.data_snowflake_external_tables",
        "cdktf_cdktf_provider_snowflake.data_snowflake_file_formats",
        "cdktf_cdktf_provider_snowflake.data_snowflake_functions",
        "cdktf_cdktf_provider_snowflake.data_snowflake_grants",
        "cdktf_cdktf_provider_snowflake.data_snowflake_masking_policies",
        "cdktf_cdktf_provider_snowflake.data_snowflake_materialized_views",
        "cdktf_cdktf_provider_snowflake.data_snowflake_parameters",
        "cdktf_cdktf_provider_snowflake.data_snowflake_pipes",
        "cdktf_cdktf_provider_snowflake.data_snowflake_procedures",
        "cdktf_cdktf_provider_snowflake.data_snowflake_resource_monitors",
        "cdktf_cdktf_provider_snowflake.data_snowflake_role",
        "cdktf_cdktf_provider_snowflake.data_snowflake_roles",
        "cdktf_cdktf_provider_snowflake.data_snowflake_row_access_policies",
        "cdktf_cdktf_provider_snowflake.data_snowflake_schemas",
        "cdktf_cdktf_provider_snowflake.data_snowflake_sequences",
        "cdktf_cdktf_provider_snowflake.data_snowflake_stages",
        "cdktf_cdktf_provider_snowflake.data_snowflake_storage_integrations",
        "cdktf_cdktf_provider_snowflake.data_snowflake_streams",
        "cdktf_cdktf_provider_snowflake.data_snowflake_system_generate_scim_access_token",
        "cdktf_cdktf_provider_snowflake.data_snowflake_system_get_aws_sns_iam_policy",
        "cdktf_cdktf_provider_snowflake.data_snowflake_system_get_privatelink_config",
        "cdktf_cdktf_provider_snowflake.data_snowflake_system_get_snowflake_platform_info",
        "cdktf_cdktf_provider_snowflake.data_snowflake_tables",
        "cdktf_cdktf_provider_snowflake.data_snowflake_tasks",
        "cdktf_cdktf_provider_snowflake.data_snowflake_users",
        "cdktf_cdktf_provider_snowflake.data_snowflake_views",
        "cdktf_cdktf_provider_snowflake.data_snowflake_warehouses",
        "cdktf_cdktf_provider_snowflake.database",
        "cdktf_cdktf_provider_snowflake.database_grant",
        "cdktf_cdktf_provider_snowflake.external_function",
        "cdktf_cdktf_provider_snowflake.external_oauth_integration",
        "cdktf_cdktf_provider_snowflake.external_table",
        "cdktf_cdktf_provider_snowflake.external_table_grant",
        "cdktf_cdktf_provider_snowflake.failover_group",
        "cdktf_cdktf_provider_snowflake.file_format",
        "cdktf_cdktf_provider_snowflake.file_format_grant",
        "cdktf_cdktf_provider_snowflake.function_grant",
        "cdktf_cdktf_provider_snowflake.function_resource",
        "cdktf_cdktf_provider_snowflake.integration_grant",
        "cdktf_cdktf_provider_snowflake.managed_account",
        "cdktf_cdktf_provider_snowflake.masking_policy",
        "cdktf_cdktf_provider_snowflake.masking_policy_grant",
        "cdktf_cdktf_provider_snowflake.materialized_view",
        "cdktf_cdktf_provider_snowflake.materialized_view_grant",
        "cdktf_cdktf_provider_snowflake.network_policy",
        "cdktf_cdktf_provider_snowflake.network_policy_attachment",
        "cdktf_cdktf_provider_snowflake.notification_integration",
        "cdktf_cdktf_provider_snowflake.oauth_integration",
        "cdktf_cdktf_provider_snowflake.object_parameter",
        "cdktf_cdktf_provider_snowflake.pipe",
        "cdktf_cdktf_provider_snowflake.pipe_grant",
        "cdktf_cdktf_provider_snowflake.procedure",
        "cdktf_cdktf_provider_snowflake.procedure_grant",
        "cdktf_cdktf_provider_snowflake.provider",
        "cdktf_cdktf_provider_snowflake.resource_monitor",
        "cdktf_cdktf_provider_snowflake.resource_monitor_grant",
        "cdktf_cdktf_provider_snowflake.role",
        "cdktf_cdktf_provider_snowflake.role_grants",
        "cdktf_cdktf_provider_snowflake.role_ownership_grant",
        "cdktf_cdktf_provider_snowflake.row_access_policy",
        "cdktf_cdktf_provider_snowflake.row_access_policy_grant",
        "cdktf_cdktf_provider_snowflake.saml_integration",
        "cdktf_cdktf_provider_snowflake.schema",
        "cdktf_cdktf_provider_snowflake.schema_grant",
        "cdktf_cdktf_provider_snowflake.scim_integration",
        "cdktf_cdktf_provider_snowflake.sequence",
        "cdktf_cdktf_provider_snowflake.sequence_grant",
        "cdktf_cdktf_provider_snowflake.session_parameter",
        "cdktf_cdktf_provider_snowflake.share",
        "cdktf_cdktf_provider_snowflake.stage",
        "cdktf_cdktf_provider_snowflake.stage_grant",
        "cdktf_cdktf_provider_snowflake.storage_integration",
        "cdktf_cdktf_provider_snowflake.stream",
        "cdktf_cdktf_provider_snowflake.stream_grant",
        "cdktf_cdktf_provider_snowflake.table",
        "cdktf_cdktf_provider_snowflake.table_constraint",
        "cdktf_cdktf_provider_snowflake.table_grant",
        "cdktf_cdktf_provider_snowflake.tag",
        "cdktf_cdktf_provider_snowflake.tag_association",
        "cdktf_cdktf_provider_snowflake.tag_grant",
        "cdktf_cdktf_provider_snowflake.tag_masking_policy_association",
        "cdktf_cdktf_provider_snowflake.task",
        "cdktf_cdktf_provider_snowflake.task_grant",
        "cdktf_cdktf_provider_snowflake.user",
        "cdktf_cdktf_provider_snowflake.user_grant",
        "cdktf_cdktf_provider_snowflake.user_ownership_grant",
        "cdktf_cdktf_provider_snowflake.user_public_keys",
        "cdktf_cdktf_provider_snowflake.view",
        "cdktf_cdktf_provider_snowflake.view_grant",
        "cdktf_cdktf_provider_snowflake.warehouse",
        "cdktf_cdktf_provider_snowflake.warehouse_grant"
    ],
    "package_data": {
        "cdktf_cdktf_provider_snowflake._jsii": [
            "provider-snowflake@4.0.4.jsii.tgz"
        ],
        "cdktf_cdktf_provider_snowflake": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.14.0, <0.15.0",
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
