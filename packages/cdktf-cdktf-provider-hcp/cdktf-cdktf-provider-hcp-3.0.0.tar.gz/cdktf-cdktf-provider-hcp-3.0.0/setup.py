import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-hcp",
    "version": "3.0.0",
    "description": "Prebuilt hcp Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-hcp.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-hcp.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_hcp",
        "cdktf_cdktf_provider_hcp._jsii",
        "cdktf_cdktf_provider_hcp.aws_network_peering",
        "cdktf_cdktf_provider_hcp.aws_transit_gateway_attachment",
        "cdktf_cdktf_provider_hcp.azure_peering_connection",
        "cdktf_cdktf_provider_hcp.boundary_cluster",
        "cdktf_cdktf_provider_hcp.consul_cluster",
        "cdktf_cdktf_provider_hcp.consul_cluster_root_token",
        "cdktf_cdktf_provider_hcp.consul_snapshot",
        "cdktf_cdktf_provider_hcp.data_hcp_aws_network_peering",
        "cdktf_cdktf_provider_hcp.data_hcp_aws_transit_gateway_attachment",
        "cdktf_cdktf_provider_hcp.data_hcp_azure_peering_connection",
        "cdktf_cdktf_provider_hcp.data_hcp_boundary_cluster",
        "cdktf_cdktf_provider_hcp.data_hcp_consul_agent_helm_config",
        "cdktf_cdktf_provider_hcp.data_hcp_consul_agent_kubernetes_secret",
        "cdktf_cdktf_provider_hcp.data_hcp_consul_cluster",
        "cdktf_cdktf_provider_hcp.data_hcp_consul_versions",
        "cdktf_cdktf_provider_hcp.data_hcp_hvn",
        "cdktf_cdktf_provider_hcp.data_hcp_hvn_peering_connection",
        "cdktf_cdktf_provider_hcp.data_hcp_hvn_route",
        "cdktf_cdktf_provider_hcp.data_hcp_packer_image",
        "cdktf_cdktf_provider_hcp.data_hcp_packer_image_iteration",
        "cdktf_cdktf_provider_hcp.data_hcp_packer_iteration",
        "cdktf_cdktf_provider_hcp.data_hcp_vault_cluster",
        "cdktf_cdktf_provider_hcp.hvn",
        "cdktf_cdktf_provider_hcp.hvn_peering_connection",
        "cdktf_cdktf_provider_hcp.hvn_route",
        "cdktf_cdktf_provider_hcp.provider",
        "cdktf_cdktf_provider_hcp.vault_cluster",
        "cdktf_cdktf_provider_hcp.vault_cluster_admin_token"
    ],
    "package_data": {
        "cdktf_cdktf_provider_hcp._jsii": [
            "provider-hcp@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_hcp": [
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
