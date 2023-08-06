'''
# Terraform CDK opc Provider ~> 1.4

This repo builds and publishes the Terraform opc Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-opc](https://www.npmjs.com/package/@cdktf/provider-opc).

`npm install @cdktf/provider-opc`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-opc](https://pypi.org/project/cdktf-cdktf-provider-opc).

`pipenv install cdktf-cdktf-provider-opc`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Opc](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Opc).

`dotnet add package HashiCorp.Cdktf.Providers.Opc`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-opc](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-opc).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-opc</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-opc-go`](https://github.com/cdktf/cdktf-provider-opc-go) package.

`go get github.com/cdktf/cdktf-provider-opc-go/opc`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-opc).

## Versioning

This project is explicitly not tracking the Terraform opc Provider version 1:1. In fact, it always tracks `latest` of `~> 1.4` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform opc Provider](https://github.com/terraform-providers/terraform-provider-opc)
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
    "compute_acl",
    "compute_image_list",
    "compute_image_list_entry",
    "compute_instance",
    "compute_ip_address_association",
    "compute_ip_address_prefix_set",
    "compute_ip_address_reservation",
    "compute_ip_association",
    "compute_ip_network",
    "compute_ip_network_exchange",
    "compute_ip_reservation",
    "compute_machine_image",
    "compute_orchestrated_instance",
    "compute_route",
    "compute_sec_rule",
    "compute_security_application",
    "compute_security_association",
    "compute_security_ip_list",
    "compute_security_list",
    "compute_security_protocol",
    "compute_security_rule",
    "compute_snapshot",
    "compute_ssh_key",
    "compute_storage_attachment",
    "compute_storage_volume",
    "compute_storage_volume_snapshot",
    "compute_vnic_set",
    "compute_vpn_endpoint_v2",
    "data_opc_compute_image_list_entry",
    "data_opc_compute_ip_address_reservation",
    "data_opc_compute_ip_reservation",
    "data_opc_compute_machine_image",
    "data_opc_compute_network_interface",
    "data_opc_compute_ssh_key",
    "data_opc_compute_storage_volume_snapshot",
    "data_opc_compute_vnic",
    "lbaas_certificate",
    "lbaas_listener",
    "lbaas_load_balancer",
    "lbaas_policy",
    "lbaas_server_pool",
    "provider",
    "storage_container",
    "storage_object",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import compute_acl
from . import compute_image_list
from . import compute_image_list_entry
from . import compute_instance
from . import compute_ip_address_association
from . import compute_ip_address_prefix_set
from . import compute_ip_address_reservation
from . import compute_ip_association
from . import compute_ip_network
from . import compute_ip_network_exchange
from . import compute_ip_reservation
from . import compute_machine_image
from . import compute_orchestrated_instance
from . import compute_route
from . import compute_sec_rule
from . import compute_security_application
from . import compute_security_association
from . import compute_security_ip_list
from . import compute_security_list
from . import compute_security_protocol
from . import compute_security_rule
from . import compute_snapshot
from . import compute_ssh_key
from . import compute_storage_attachment
from . import compute_storage_volume
from . import compute_storage_volume_snapshot
from . import compute_vnic_set
from . import compute_vpn_endpoint_v2
from . import data_opc_compute_image_list_entry
from . import data_opc_compute_ip_address_reservation
from . import data_opc_compute_ip_reservation
from . import data_opc_compute_machine_image
from . import data_opc_compute_network_interface
from . import data_opc_compute_ssh_key
from . import data_opc_compute_storage_volume_snapshot
from . import data_opc_compute_vnic
from . import lbaas_certificate
from . import lbaas_listener
from . import lbaas_load_balancer
from . import lbaas_policy
from . import lbaas_server_pool
from . import provider
from . import storage_container
from . import storage_object
