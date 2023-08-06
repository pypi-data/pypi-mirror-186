'''
# Terraform CDK nomad Provider ~> 1.4

This repo builds and publishes the Terraform nomad Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-nomad](https://www.npmjs.com/package/@cdktf/provider-nomad).

`npm install @cdktf/provider-nomad`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-nomad](https://pypi.org/project/cdktf-cdktf-provider-nomad).

`pipenv install cdktf-cdktf-provider-nomad`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Nomad](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Nomad).

`dotnet add package HashiCorp.Cdktf.Providers.Nomad`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-nomad](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-nomad).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-nomad</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-nomad-go`](https://github.com/cdktf/cdktf-provider-nomad-go) package.

`go get github.com/cdktf/cdktf-provider-nomad-go/nomad`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-nomad).

## Versioning

This project is explicitly not tracking the Terraform nomad Provider version 1:1. In fact, it always tracks `latest` of `~> 1.4` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform nomad Provider](https://github.com/terraform-providers/terraform-provider-nomad)
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
    "acl_policy",
    "acl_role",
    "acl_token",
    "data_nomad_acl_policies",
    "data_nomad_acl_policy",
    "data_nomad_acl_role",
    "data_nomad_acl_roles",
    "data_nomad_acl_token",
    "data_nomad_acl_tokens",
    "data_nomad_datacenters",
    "data_nomad_deployments",
    "data_nomad_job",
    "data_nomad_job_parser",
    "data_nomad_namespace",
    "data_nomad_namespaces",
    "data_nomad_plugin",
    "data_nomad_plugins",
    "data_nomad_regions",
    "data_nomad_scaling_policies",
    "data_nomad_scaling_policy",
    "data_nomad_scheduler_config",
    "data_nomad_volumes",
    "external_volume",
    "job",
    "namespace",
    "provider",
    "quota_specification",
    "scheduler_config",
    "sentinel_policy",
    "volume",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import acl_policy
from . import acl_role
from . import acl_token
from . import data_nomad_acl_policies
from . import data_nomad_acl_policy
from . import data_nomad_acl_role
from . import data_nomad_acl_roles
from . import data_nomad_acl_token
from . import data_nomad_acl_tokens
from . import data_nomad_datacenters
from . import data_nomad_deployments
from . import data_nomad_job
from . import data_nomad_job_parser
from . import data_nomad_namespace
from . import data_nomad_namespaces
from . import data_nomad_plugin
from . import data_nomad_plugins
from . import data_nomad_regions
from . import data_nomad_scaling_policies
from . import data_nomad_scaling_policy
from . import data_nomad_scheduler_config
from . import data_nomad_volumes
from . import external_volume
from . import job
from . import namespace
from . import provider
from . import quota_specification
from . import scheduler_config
from . import sentinel_policy
from . import volume
