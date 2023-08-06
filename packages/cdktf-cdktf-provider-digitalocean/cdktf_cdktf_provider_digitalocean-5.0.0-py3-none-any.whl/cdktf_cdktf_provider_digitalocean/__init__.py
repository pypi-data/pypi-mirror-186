'''
# Terraform CDK digitalocean Provider ~> 2.19

This repo builds and publishes the Terraform digitalocean Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-digitalocean](https://www.npmjs.com/package/@cdktf/provider-digitalocean).

`npm install @cdktf/provider-digitalocean`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-digitalocean](https://pypi.org/project/cdktf-cdktf-provider-digitalocean).

`pipenv install cdktf-cdktf-provider-digitalocean`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Digitalocean](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Digitalocean).

`dotnet add package HashiCorp.Cdktf.Providers.Digitalocean`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-digitalocean](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-digitalocean).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-digitalocean</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-digitalocean-go`](https://github.com/cdktf/cdktf-provider-digitalocean-go) package.

`go get github.com/cdktf/cdktf-provider-digitalocean-go/digitalocean`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-digitalocean).

## Versioning

This project is explicitly not tracking the Terraform digitalocean Provider version 1:1. In fact, it always tracks `latest` of `~> 2.19` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform digitalocean Provider](https://github.com/terraform-providers/terraform-provider-digitalocean)
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
    "app",
    "cdn",
    "certificate",
    "container_registry",
    "container_registry_docker_credentials",
    "custom_image",
    "data_digitalocean_account",
    "data_digitalocean_app",
    "data_digitalocean_certificate",
    "data_digitalocean_container_registry",
    "data_digitalocean_database_ca",
    "data_digitalocean_database_cluster",
    "data_digitalocean_database_replica",
    "data_digitalocean_domain",
    "data_digitalocean_domains",
    "data_digitalocean_droplet",
    "data_digitalocean_droplet_snapshot",
    "data_digitalocean_droplets",
    "data_digitalocean_firewall",
    "data_digitalocean_floating_ip",
    "data_digitalocean_image",
    "data_digitalocean_images",
    "data_digitalocean_kubernetes_cluster",
    "data_digitalocean_kubernetes_versions",
    "data_digitalocean_loadbalancer",
    "data_digitalocean_project",
    "data_digitalocean_projects",
    "data_digitalocean_record",
    "data_digitalocean_records",
    "data_digitalocean_region",
    "data_digitalocean_regions",
    "data_digitalocean_reserved_ip",
    "data_digitalocean_sizes",
    "data_digitalocean_spaces_bucket",
    "data_digitalocean_spaces_bucket_object",
    "data_digitalocean_spaces_bucket_objects",
    "data_digitalocean_spaces_buckets",
    "data_digitalocean_ssh_key",
    "data_digitalocean_ssh_keys",
    "data_digitalocean_tag",
    "data_digitalocean_tags",
    "data_digitalocean_volume",
    "data_digitalocean_volume_snapshot",
    "data_digitalocean_vpc",
    "database_cluster",
    "database_connection_pool",
    "database_db",
    "database_firewall",
    "database_replica",
    "database_user",
    "domain",
    "droplet",
    "droplet_snapshot",
    "firewall",
    "floating_ip",
    "floating_ip_assignment",
    "kubernetes_cluster",
    "kubernetes_node_pool",
    "loadbalancer",
    "monitor_alert",
    "project",
    "project_resources",
    "provider",
    "record",
    "reserved_ip",
    "reserved_ip_assignment",
    "spaces_bucket",
    "spaces_bucket_object",
    "spaces_bucket_policy",
    "ssh_key",
    "tag",
    "volume",
    "volume_attachment",
    "volume_snapshot",
    "vpc",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import app
from . import cdn
from . import certificate
from . import container_registry
from . import container_registry_docker_credentials
from . import custom_image
from . import data_digitalocean_account
from . import data_digitalocean_app
from . import data_digitalocean_certificate
from . import data_digitalocean_container_registry
from . import data_digitalocean_database_ca
from . import data_digitalocean_database_cluster
from . import data_digitalocean_database_replica
from . import data_digitalocean_domain
from . import data_digitalocean_domains
from . import data_digitalocean_droplet
from . import data_digitalocean_droplet_snapshot
from . import data_digitalocean_droplets
from . import data_digitalocean_firewall
from . import data_digitalocean_floating_ip
from . import data_digitalocean_image
from . import data_digitalocean_images
from . import data_digitalocean_kubernetes_cluster
from . import data_digitalocean_kubernetes_versions
from . import data_digitalocean_loadbalancer
from . import data_digitalocean_project
from . import data_digitalocean_projects
from . import data_digitalocean_record
from . import data_digitalocean_records
from . import data_digitalocean_region
from . import data_digitalocean_regions
from . import data_digitalocean_reserved_ip
from . import data_digitalocean_sizes
from . import data_digitalocean_spaces_bucket
from . import data_digitalocean_spaces_bucket_object
from . import data_digitalocean_spaces_bucket_objects
from . import data_digitalocean_spaces_buckets
from . import data_digitalocean_ssh_key
from . import data_digitalocean_ssh_keys
from . import data_digitalocean_tag
from . import data_digitalocean_tags
from . import data_digitalocean_volume
from . import data_digitalocean_volume_snapshot
from . import data_digitalocean_vpc
from . import database_cluster
from . import database_connection_pool
from . import database_db
from . import database_firewall
from . import database_replica
from . import database_user
from . import domain
from . import droplet
from . import droplet_snapshot
from . import firewall
from . import floating_ip
from . import floating_ip_assignment
from . import kubernetes_cluster
from . import kubernetes_node_pool
from . import loadbalancer
from . import monitor_alert
from . import project
from . import project_resources
from . import provider
from . import record
from . import reserved_ip
from . import reserved_ip_assignment
from . import spaces_bucket
from . import spaces_bucket_object
from . import spaces_bucket_policy
from . import ssh_key
from . import tag
from . import volume
from . import volume_attachment
from . import volume_snapshot
from . import vpc
