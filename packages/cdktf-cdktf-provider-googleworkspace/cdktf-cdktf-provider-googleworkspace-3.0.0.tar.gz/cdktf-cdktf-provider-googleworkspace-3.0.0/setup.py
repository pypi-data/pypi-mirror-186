import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-googleworkspace",
    "version": "3.0.0",
    "description": "Prebuilt googleworkspace Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-googleworkspace.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-googleworkspace.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_googleworkspace",
        "cdktf_cdktf_provider_googleworkspace._jsii",
        "cdktf_cdktf_provider_googleworkspace.chrome_policy",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_chrome_policy_schema",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_domain",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_domain_alias",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_group",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_group_member",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_group_members",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_group_settings",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_groups",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_org_unit",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_privileges",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_role",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_schema",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_user",
        "cdktf_cdktf_provider_googleworkspace.data_googleworkspace_users",
        "cdktf_cdktf_provider_googleworkspace.domain",
        "cdktf_cdktf_provider_googleworkspace.domain_alias",
        "cdktf_cdktf_provider_googleworkspace.gmail_send_as_alias",
        "cdktf_cdktf_provider_googleworkspace.group",
        "cdktf_cdktf_provider_googleworkspace.group_member",
        "cdktf_cdktf_provider_googleworkspace.group_members",
        "cdktf_cdktf_provider_googleworkspace.group_settings",
        "cdktf_cdktf_provider_googleworkspace.org_unit",
        "cdktf_cdktf_provider_googleworkspace.provider",
        "cdktf_cdktf_provider_googleworkspace.role",
        "cdktf_cdktf_provider_googleworkspace.role_assignment",
        "cdktf_cdktf_provider_googleworkspace.schema",
        "cdktf_cdktf_provider_googleworkspace.user"
    ],
    "package_data": {
        "cdktf_cdktf_provider_googleworkspace._jsii": [
            "provider-googleworkspace@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_googleworkspace": [
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
