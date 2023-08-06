import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-opc",
    "version": "3.0.0",
    "description": "Prebuilt opc Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-opc.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-opc.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_opc",
        "cdktf_cdktf_provider_opc._jsii",
        "cdktf_cdktf_provider_opc.compute_acl",
        "cdktf_cdktf_provider_opc.compute_image_list",
        "cdktf_cdktf_provider_opc.compute_image_list_entry",
        "cdktf_cdktf_provider_opc.compute_instance",
        "cdktf_cdktf_provider_opc.compute_ip_address_association",
        "cdktf_cdktf_provider_opc.compute_ip_address_prefix_set",
        "cdktf_cdktf_provider_opc.compute_ip_address_reservation",
        "cdktf_cdktf_provider_opc.compute_ip_association",
        "cdktf_cdktf_provider_opc.compute_ip_network",
        "cdktf_cdktf_provider_opc.compute_ip_network_exchange",
        "cdktf_cdktf_provider_opc.compute_ip_reservation",
        "cdktf_cdktf_provider_opc.compute_machine_image",
        "cdktf_cdktf_provider_opc.compute_orchestrated_instance",
        "cdktf_cdktf_provider_opc.compute_route",
        "cdktf_cdktf_provider_opc.compute_sec_rule",
        "cdktf_cdktf_provider_opc.compute_security_application",
        "cdktf_cdktf_provider_opc.compute_security_association",
        "cdktf_cdktf_provider_opc.compute_security_ip_list",
        "cdktf_cdktf_provider_opc.compute_security_list",
        "cdktf_cdktf_provider_opc.compute_security_protocol",
        "cdktf_cdktf_provider_opc.compute_security_rule",
        "cdktf_cdktf_provider_opc.compute_snapshot",
        "cdktf_cdktf_provider_opc.compute_ssh_key",
        "cdktf_cdktf_provider_opc.compute_storage_attachment",
        "cdktf_cdktf_provider_opc.compute_storage_volume",
        "cdktf_cdktf_provider_opc.compute_storage_volume_snapshot",
        "cdktf_cdktf_provider_opc.compute_vnic_set",
        "cdktf_cdktf_provider_opc.compute_vpn_endpoint_v2",
        "cdktf_cdktf_provider_opc.data_opc_compute_image_list_entry",
        "cdktf_cdktf_provider_opc.data_opc_compute_ip_address_reservation",
        "cdktf_cdktf_provider_opc.data_opc_compute_ip_reservation",
        "cdktf_cdktf_provider_opc.data_opc_compute_machine_image",
        "cdktf_cdktf_provider_opc.data_opc_compute_network_interface",
        "cdktf_cdktf_provider_opc.data_opc_compute_ssh_key",
        "cdktf_cdktf_provider_opc.data_opc_compute_storage_volume_snapshot",
        "cdktf_cdktf_provider_opc.data_opc_compute_vnic",
        "cdktf_cdktf_provider_opc.lbaas_certificate",
        "cdktf_cdktf_provider_opc.lbaas_listener",
        "cdktf_cdktf_provider_opc.lbaas_load_balancer",
        "cdktf_cdktf_provider_opc.lbaas_policy",
        "cdktf_cdktf_provider_opc.lbaas_server_pool",
        "cdktf_cdktf_provider_opc.provider",
        "cdktf_cdktf_provider_opc.storage_container",
        "cdktf_cdktf_provider_opc.storage_object"
    ],
    "package_data": {
        "cdktf_cdktf_provider_opc._jsii": [
            "provider-opc@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_opc": [
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
