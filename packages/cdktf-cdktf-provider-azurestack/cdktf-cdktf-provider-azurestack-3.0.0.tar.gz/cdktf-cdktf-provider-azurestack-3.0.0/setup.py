import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-azurestack",
    "version": "3.0.0",
    "description": "Prebuilt azurestack Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-azurestack.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-azurestack.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_azurestack",
        "cdktf_cdktf_provider_azurestack._jsii",
        "cdktf_cdktf_provider_azurestack.availability_set",
        "cdktf_cdktf_provider_azurestack.data_azurestack_availability_set",
        "cdktf_cdktf_provider_azurestack.data_azurestack_client_config",
        "cdktf_cdktf_provider_azurestack.data_azurestack_dns_zone",
        "cdktf_cdktf_provider_azurestack.data_azurestack_image",
        "cdktf_cdktf_provider_azurestack.data_azurestack_key_vault",
        "cdktf_cdktf_provider_azurestack.data_azurestack_key_vault_access_policy",
        "cdktf_cdktf_provider_azurestack.data_azurestack_key_vault_key",
        "cdktf_cdktf_provider_azurestack.data_azurestack_key_vault_secret",
        "cdktf_cdktf_provider_azurestack.data_azurestack_lb",
        "cdktf_cdktf_provider_azurestack.data_azurestack_lb_backend_address_pool",
        "cdktf_cdktf_provider_azurestack.data_azurestack_lb_rule",
        "cdktf_cdktf_provider_azurestack.data_azurestack_local_network_gateway",
        "cdktf_cdktf_provider_azurestack.data_azurestack_managed_disk",
        "cdktf_cdktf_provider_azurestack.data_azurestack_network_interface",
        "cdktf_cdktf_provider_azurestack.data_azurestack_network_security_group",
        "cdktf_cdktf_provider_azurestack.data_azurestack_platform_image",
        "cdktf_cdktf_provider_azurestack.data_azurestack_public_ip",
        "cdktf_cdktf_provider_azurestack.data_azurestack_public_ips",
        "cdktf_cdktf_provider_azurestack.data_azurestack_resource_group",
        "cdktf_cdktf_provider_azurestack.data_azurestack_resources",
        "cdktf_cdktf_provider_azurestack.data_azurestack_route_table",
        "cdktf_cdktf_provider_azurestack.data_azurestack_storage_account",
        "cdktf_cdktf_provider_azurestack.data_azurestack_storage_container",
        "cdktf_cdktf_provider_azurestack.data_azurestack_subnet",
        "cdktf_cdktf_provider_azurestack.data_azurestack_virtual_network",
        "cdktf_cdktf_provider_azurestack.data_azurestack_virtual_network_gateway",
        "cdktf_cdktf_provider_azurestack.data_azurestack_virtual_network_gateway_connection",
        "cdktf_cdktf_provider_azurestack.dns_a_record",
        "cdktf_cdktf_provider_azurestack.dns_aaaa_record",
        "cdktf_cdktf_provider_azurestack.dns_cname_record",
        "cdktf_cdktf_provider_azurestack.dns_mx_record",
        "cdktf_cdktf_provider_azurestack.dns_ns_record",
        "cdktf_cdktf_provider_azurestack.dns_ptr_record",
        "cdktf_cdktf_provider_azurestack.dns_srv_record",
        "cdktf_cdktf_provider_azurestack.dns_txt_record",
        "cdktf_cdktf_provider_azurestack.dns_zone",
        "cdktf_cdktf_provider_azurestack.image",
        "cdktf_cdktf_provider_azurestack.key_vault",
        "cdktf_cdktf_provider_azurestack.key_vault_access_policy",
        "cdktf_cdktf_provider_azurestack.key_vault_key",
        "cdktf_cdktf_provider_azurestack.key_vault_secret",
        "cdktf_cdktf_provider_azurestack.lb",
        "cdktf_cdktf_provider_azurestack.lb_backend_address_pool",
        "cdktf_cdktf_provider_azurestack.lb_nat_pool",
        "cdktf_cdktf_provider_azurestack.lb_nat_rule",
        "cdktf_cdktf_provider_azurestack.lb_probe",
        "cdktf_cdktf_provider_azurestack.lb_rule",
        "cdktf_cdktf_provider_azurestack.linux_virtual_machine",
        "cdktf_cdktf_provider_azurestack.linux_virtual_machine_scale_set",
        "cdktf_cdktf_provider_azurestack.local_network_gateway",
        "cdktf_cdktf_provider_azurestack.managed_disk",
        "cdktf_cdktf_provider_azurestack.network_interface",
        "cdktf_cdktf_provider_azurestack.network_interface_backend_address_pool_association",
        "cdktf_cdktf_provider_azurestack.network_security_group",
        "cdktf_cdktf_provider_azurestack.network_security_rule",
        "cdktf_cdktf_provider_azurestack.provider",
        "cdktf_cdktf_provider_azurestack.public_ip",
        "cdktf_cdktf_provider_azurestack.resource_group",
        "cdktf_cdktf_provider_azurestack.route",
        "cdktf_cdktf_provider_azurestack.route_table",
        "cdktf_cdktf_provider_azurestack.storage_account",
        "cdktf_cdktf_provider_azurestack.storage_blob",
        "cdktf_cdktf_provider_azurestack.storage_container",
        "cdktf_cdktf_provider_azurestack.subnet",
        "cdktf_cdktf_provider_azurestack.template_deployment",
        "cdktf_cdktf_provider_azurestack.virtual_machine",
        "cdktf_cdktf_provider_azurestack.virtual_machine_data_disk_attachment",
        "cdktf_cdktf_provider_azurestack.virtual_machine_extension",
        "cdktf_cdktf_provider_azurestack.virtual_machine_scale_set",
        "cdktf_cdktf_provider_azurestack.virtual_machine_scale_set_extension",
        "cdktf_cdktf_provider_azurestack.virtual_network",
        "cdktf_cdktf_provider_azurestack.virtual_network_gateway",
        "cdktf_cdktf_provider_azurestack.virtual_network_gateway_connection",
        "cdktf_cdktf_provider_azurestack.virtual_network_peering",
        "cdktf_cdktf_provider_azurestack.windows_virtual_machine",
        "cdktf_cdktf_provider_azurestack.windows_virtual_machine_scale_set"
    ],
    "package_data": {
        "cdktf_cdktf_provider_azurestack._jsii": [
            "provider-azurestack@3.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_azurestack": [
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
