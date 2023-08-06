import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-ionoscloud",
    "version": "5.0.0",
    "description": "Prebuilt ionoscloud Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-ionoscloud.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-ionoscloud.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_ionoscloud",
        "cdktf_cdktf_provider_ionoscloud._jsii",
        "cdktf_cdktf_provider_ionoscloud.application_loadbalancer",
        "cdktf_cdktf_provider_ionoscloud.application_loadbalancer_forwardingrule",
        "cdktf_cdktf_provider_ionoscloud.backup_unit",
        "cdktf_cdktf_provider_ionoscloud.certificate",
        "cdktf_cdktf_provider_ionoscloud.container_registry",
        "cdktf_cdktf_provider_ionoscloud.container_registry_token",
        "cdktf_cdktf_provider_ionoscloud.cube_server",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_application_loadbalancer",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_application_loadbalancer_forwardingrule",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_backup_unit",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_certificate",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_container_registry",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_container_registry_locations",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_container_registry_token",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_cube_server",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_datacenter",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_firewall",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_group",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_image",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_ipblock",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_ipfailover",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_k8_s_cluster",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_k8_s_node_pool",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_k8_s_node_pool_nodes",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_lan",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_location",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_mongo_cluster",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_mongo_user",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_natgateway",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_natgateway_rule",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_networkloadbalancer",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_networkloadbalancer_forwardingrule",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_nic",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_pg_backups",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_pg_cluster",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_pg_versions",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_private_crossconnect",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_resource",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_s3_key",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_server",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_servers",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_share",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_snapshot",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_target_group",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_template",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_user",
        "cdktf_cdktf_provider_ionoscloud.data_ionoscloud_volume",
        "cdktf_cdktf_provider_ionoscloud.datacenter",
        "cdktf_cdktf_provider_ionoscloud.firewall",
        "cdktf_cdktf_provider_ionoscloud.group",
        "cdktf_cdktf_provider_ionoscloud.ipblock",
        "cdktf_cdktf_provider_ionoscloud.ipfailover",
        "cdktf_cdktf_provider_ionoscloud.k8_s_cluster",
        "cdktf_cdktf_provider_ionoscloud.k8_s_node_pool",
        "cdktf_cdktf_provider_ionoscloud.lan",
        "cdktf_cdktf_provider_ionoscloud.loadbalancer",
        "cdktf_cdktf_provider_ionoscloud.mongo_cluster",
        "cdktf_cdktf_provider_ionoscloud.mongo_user",
        "cdktf_cdktf_provider_ionoscloud.natgateway",
        "cdktf_cdktf_provider_ionoscloud.natgateway_rule",
        "cdktf_cdktf_provider_ionoscloud.networkloadbalancer",
        "cdktf_cdktf_provider_ionoscloud.networkloadbalancer_forwardingrule",
        "cdktf_cdktf_provider_ionoscloud.nic",
        "cdktf_cdktf_provider_ionoscloud.pg_cluster",
        "cdktf_cdktf_provider_ionoscloud.private_crossconnect",
        "cdktf_cdktf_provider_ionoscloud.provider",
        "cdktf_cdktf_provider_ionoscloud.s3_key",
        "cdktf_cdktf_provider_ionoscloud.server",
        "cdktf_cdktf_provider_ionoscloud.share",
        "cdktf_cdktf_provider_ionoscloud.snapshot",
        "cdktf_cdktf_provider_ionoscloud.target_group",
        "cdktf_cdktf_provider_ionoscloud.user",
        "cdktf_cdktf_provider_ionoscloud.volume"
    ],
    "package_data": {
        "cdktf_cdktf_provider_ionoscloud._jsii": [
            "provider-ionoscloud@5.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_ionoscloud": [
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
