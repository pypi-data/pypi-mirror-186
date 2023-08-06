import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-hcs",
    "version": "3.0.0",
    "description": "Prebuilt hcs Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-hcs.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-hcs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_hcs",
        "cdktf_cdktf_provider_hcs._jsii",
        "cdktf_cdktf_provider_hcs.cluster",
        "cdktf_cdktf_provider_hcs.cluster_root_token",
        "cdktf_cdktf_provider_hcs.data_hcs_agent_helm_config",
        "cdktf_cdktf_provider_hcs.data_hcs_agent_kubernetes_secret",
        "cdktf_cdktf_provider_hcs.data_hcs_cluster",
        "cdktf_cdktf_provider_hcs.data_hcs_consul_versions",
        "cdktf_cdktf_provider_hcs.data_hcs_federation_token",
        "cdktf_cdktf_provider_hcs.data_hcs_plan_defaults",
        "cdktf_cdktf_provider_hcs.provider",
        "cdktf_cdktf_provider_hcs.snapshot"
    ],
    "package_data": {
        "cdktf_cdktf_provider_hcs._jsii": [
            "provider-hcs@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_hcs": [
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
