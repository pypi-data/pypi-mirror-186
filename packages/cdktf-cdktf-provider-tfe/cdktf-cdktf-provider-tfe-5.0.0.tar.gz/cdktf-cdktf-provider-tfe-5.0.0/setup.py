import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-tfe",
    "version": "5.0.0",
    "description": "Prebuilt tfe Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-tfe.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-tfe.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_tfe",
        "cdktf_cdktf_provider_tfe._jsii",
        "cdktf_cdktf_provider_tfe.admin_organization_settings",
        "cdktf_cdktf_provider_tfe.agent_pool",
        "cdktf_cdktf_provider_tfe.agent_token",
        "cdktf_cdktf_provider_tfe.data_tfe_agent_pool",
        "cdktf_cdktf_provider_tfe.data_tfe_ip_ranges",
        "cdktf_cdktf_provider_tfe.data_tfe_oauth_client",
        "cdktf_cdktf_provider_tfe.data_tfe_organization",
        "cdktf_cdktf_provider_tfe.data_tfe_organization_members",
        "cdktf_cdktf_provider_tfe.data_tfe_organization_membership",
        "cdktf_cdktf_provider_tfe.data_tfe_organization_run_task",
        "cdktf_cdktf_provider_tfe.data_tfe_organizations",
        "cdktf_cdktf_provider_tfe.data_tfe_outputs",
        "cdktf_cdktf_provider_tfe.data_tfe_policy_set",
        "cdktf_cdktf_provider_tfe.data_tfe_slug",
        "cdktf_cdktf_provider_tfe.data_tfe_ssh_key",
        "cdktf_cdktf_provider_tfe.data_tfe_team",
        "cdktf_cdktf_provider_tfe.data_tfe_team_access",
        "cdktf_cdktf_provider_tfe.data_tfe_variable_set",
        "cdktf_cdktf_provider_tfe.data_tfe_variables",
        "cdktf_cdktf_provider_tfe.data_tfe_workspace",
        "cdktf_cdktf_provider_tfe.data_tfe_workspace_ids",
        "cdktf_cdktf_provider_tfe.data_tfe_workspace_run_task",
        "cdktf_cdktf_provider_tfe.notification_configuration",
        "cdktf_cdktf_provider_tfe.oauth_client",
        "cdktf_cdktf_provider_tfe.organization",
        "cdktf_cdktf_provider_tfe.organization_membership",
        "cdktf_cdktf_provider_tfe.organization_module_sharing",
        "cdktf_cdktf_provider_tfe.organization_run_task",
        "cdktf_cdktf_provider_tfe.organization_token",
        "cdktf_cdktf_provider_tfe.policy",
        "cdktf_cdktf_provider_tfe.policy_set",
        "cdktf_cdktf_provider_tfe.policy_set_parameter",
        "cdktf_cdktf_provider_tfe.project",
        "cdktf_cdktf_provider_tfe.provider",
        "cdktf_cdktf_provider_tfe.registry_module",
        "cdktf_cdktf_provider_tfe.run_trigger",
        "cdktf_cdktf_provider_tfe.sentinel_policy",
        "cdktf_cdktf_provider_tfe.ssh_key",
        "cdktf_cdktf_provider_tfe.team",
        "cdktf_cdktf_provider_tfe.team_access",
        "cdktf_cdktf_provider_tfe.team_member",
        "cdktf_cdktf_provider_tfe.team_members",
        "cdktf_cdktf_provider_tfe.team_organization_member",
        "cdktf_cdktf_provider_tfe.team_organization_members",
        "cdktf_cdktf_provider_tfe.team_token",
        "cdktf_cdktf_provider_tfe.terraform_version",
        "cdktf_cdktf_provider_tfe.variable",
        "cdktf_cdktf_provider_tfe.variable_set",
        "cdktf_cdktf_provider_tfe.workspace",
        "cdktf_cdktf_provider_tfe.workspace_policy_set",
        "cdktf_cdktf_provider_tfe.workspace_run_task",
        "cdktf_cdktf_provider_tfe.workspace_variable_set"
    ],
    "package_data": {
        "cdktf_cdktf_provider_tfe._jsii": [
            "provider-tfe@5.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_tfe": [
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
