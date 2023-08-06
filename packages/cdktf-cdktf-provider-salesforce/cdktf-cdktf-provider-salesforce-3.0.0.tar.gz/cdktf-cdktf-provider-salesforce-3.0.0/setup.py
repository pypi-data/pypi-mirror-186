import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-salesforce",
    "version": "3.0.0",
    "description": "Prebuilt salesforce Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-salesforce.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-salesforce.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_salesforce",
        "cdktf_cdktf_provider_salesforce._jsii",
        "cdktf_cdktf_provider_salesforce.data_salesforce_profile",
        "cdktf_cdktf_provider_salesforce.data_salesforce_user_license",
        "cdktf_cdktf_provider_salesforce.profile",
        "cdktf_cdktf_provider_salesforce.provider",
        "cdktf_cdktf_provider_salesforce.user",
        "cdktf_cdktf_provider_salesforce.user_role"
    ],
    "package_data": {
        "cdktf_cdktf_provider_salesforce._jsii": [
            "provider-salesforce@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_salesforce": [
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
