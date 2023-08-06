'''
# Terraform CDK azurestack Provider ~> 1.0

This repo builds and publishes the Terraform azurestack Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-azurestack](https://www.npmjs.com/package/@cdktf/provider-azurestack).

`npm install @cdktf/provider-azurestack`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-azurestack](https://pypi.org/project/cdktf-cdktf-provider-azurestack).

`pipenv install cdktf-cdktf-provider-azurestack`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Azurestack](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Azurestack).

`dotnet add package HashiCorp.Cdktf.Providers.Azurestack`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-azurestack](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-azurestack).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-azurestack</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-azurestack-go`](https://github.com/cdktf/cdktf-provider-azurestack-go) package.

`go get github.com/cdktf/cdktf-provider-azurestack-go/azurestack`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-azurestack).

## Versioning

This project is explicitly not tracking the Terraform azurestack Provider version 1:1. In fact, it always tracks `latest` of `~> 1.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform azurestack Provider](https://github.com/terraform-providers/terraform-provider-azurestack)
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
    "availability_set",
    "data_azurestack_availability_set",
    "data_azurestack_client_config",
    "data_azurestack_dns_zone",
    "data_azurestack_image",
    "data_azurestack_key_vault",
    "data_azurestack_key_vault_access_policy",
    "data_azurestack_key_vault_key",
    "data_azurestack_key_vault_secret",
    "data_azurestack_lb",
    "data_azurestack_lb_backend_address_pool",
    "data_azurestack_lb_rule",
    "data_azurestack_local_network_gateway",
    "data_azurestack_managed_disk",
    "data_azurestack_network_interface",
    "data_azurestack_network_security_group",
    "data_azurestack_platform_image",
    "data_azurestack_public_ip",
    "data_azurestack_public_ips",
    "data_azurestack_resource_group",
    "data_azurestack_resources",
    "data_azurestack_route_table",
    "data_azurestack_storage_account",
    "data_azurestack_storage_container",
    "data_azurestack_subnet",
    "data_azurestack_virtual_network",
    "data_azurestack_virtual_network_gateway",
    "data_azurestack_virtual_network_gateway_connection",
    "dns_a_record",
    "dns_aaaa_record",
    "dns_cname_record",
    "dns_mx_record",
    "dns_ns_record",
    "dns_ptr_record",
    "dns_srv_record",
    "dns_txt_record",
    "dns_zone",
    "image",
    "key_vault",
    "key_vault_access_policy",
    "key_vault_key",
    "key_vault_secret",
    "lb",
    "lb_backend_address_pool",
    "lb_nat_pool",
    "lb_nat_rule",
    "lb_probe",
    "lb_rule",
    "linux_virtual_machine",
    "linux_virtual_machine_scale_set",
    "local_network_gateway",
    "managed_disk",
    "network_interface",
    "network_interface_backend_address_pool_association",
    "network_security_group",
    "network_security_rule",
    "provider",
    "public_ip",
    "resource_group",
    "route",
    "route_table",
    "storage_account",
    "storage_blob",
    "storage_container",
    "subnet",
    "template_deployment",
    "virtual_machine",
    "virtual_machine_data_disk_attachment",
    "virtual_machine_extension",
    "virtual_machine_scale_set",
    "virtual_machine_scale_set_extension",
    "virtual_network",
    "virtual_network_gateway",
    "virtual_network_gateway_connection",
    "virtual_network_peering",
    "windows_virtual_machine",
    "windows_virtual_machine_scale_set",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import availability_set
from . import data_azurestack_availability_set
from . import data_azurestack_client_config
from . import data_azurestack_dns_zone
from . import data_azurestack_image
from . import data_azurestack_key_vault
from . import data_azurestack_key_vault_access_policy
from . import data_azurestack_key_vault_key
from . import data_azurestack_key_vault_secret
from . import data_azurestack_lb
from . import data_azurestack_lb_backend_address_pool
from . import data_azurestack_lb_rule
from . import data_azurestack_local_network_gateway
from . import data_azurestack_managed_disk
from . import data_azurestack_network_interface
from . import data_azurestack_network_security_group
from . import data_azurestack_platform_image
from . import data_azurestack_public_ip
from . import data_azurestack_public_ips
from . import data_azurestack_resource_group
from . import data_azurestack_resources
from . import data_azurestack_route_table
from . import data_azurestack_storage_account
from . import data_azurestack_storage_container
from . import data_azurestack_subnet
from . import data_azurestack_virtual_network
from . import data_azurestack_virtual_network_gateway
from . import data_azurestack_virtual_network_gateway_connection
from . import dns_a_record
from . import dns_aaaa_record
from . import dns_cname_record
from . import dns_mx_record
from . import dns_ns_record
from . import dns_ptr_record
from . import dns_srv_record
from . import dns_txt_record
from . import dns_zone
from . import image
from . import key_vault
from . import key_vault_access_policy
from . import key_vault_key
from . import key_vault_secret
from . import lb
from . import lb_backend_address_pool
from . import lb_nat_pool
from . import lb_nat_rule
from . import lb_probe
from . import lb_rule
from . import linux_virtual_machine
from . import linux_virtual_machine_scale_set
from . import local_network_gateway
from . import managed_disk
from . import network_interface
from . import network_interface_backend_address_pool_association
from . import network_security_group
from . import network_security_rule
from . import provider
from . import public_ip
from . import resource_group
from . import route
from . import route_table
from . import storage_account
from . import storage_blob
from . import storage_container
from . import subnet
from . import template_deployment
from . import virtual_machine
from . import virtual_machine_data_disk_attachment
from . import virtual_machine_extension
from . import virtual_machine_scale_set
from . import virtual_machine_scale_set_extension
from . import virtual_network
from . import virtual_network_gateway
from . import virtual_network_gateway_connection
from . import virtual_network_peering
from . import windows_virtual_machine
from . import windows_virtual_machine_scale_set
