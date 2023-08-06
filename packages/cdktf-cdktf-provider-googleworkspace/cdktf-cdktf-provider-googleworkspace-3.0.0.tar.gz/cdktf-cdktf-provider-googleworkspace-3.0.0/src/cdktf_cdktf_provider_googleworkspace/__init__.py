'''
# Terraform CDK googleworkspace Provider ~> 0.7

This repo builds and publishes the Terraform googleworkspace Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-googleworkspace](https://www.npmjs.com/package/@cdktf/provider-googleworkspace).

`npm install @cdktf/provider-googleworkspace`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-googleworkspace](https://pypi.org/project/cdktf-cdktf-provider-googleworkspace).

`pipenv install cdktf-cdktf-provider-googleworkspace`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Googleworkspace](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Googleworkspace).

`dotnet add package HashiCorp.Cdktf.Providers.Googleworkspace`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-googleworkspace](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-googleworkspace).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-googleworkspace</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-googleworkspace-go`](https://github.com/cdktf/cdktf-provider-googleworkspace-go) package.

`go get github.com/cdktf/cdktf-provider-googleworkspace-go/googleworkspace`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-googleworkspace).

## Versioning

This project is explicitly not tracking the Terraform googleworkspace Provider version 1:1. In fact, it always tracks `latest` of `~> 0.7` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform googleworkspace Provider](https://github.com/terraform-providers/terraform-provider-googleworkspace)
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
    "chrome_policy",
    "data_googleworkspace_chrome_policy_schema",
    "data_googleworkspace_domain",
    "data_googleworkspace_domain_alias",
    "data_googleworkspace_group",
    "data_googleworkspace_group_member",
    "data_googleworkspace_group_members",
    "data_googleworkspace_group_settings",
    "data_googleworkspace_groups",
    "data_googleworkspace_org_unit",
    "data_googleworkspace_privileges",
    "data_googleworkspace_role",
    "data_googleworkspace_schema",
    "data_googleworkspace_user",
    "data_googleworkspace_users",
    "domain",
    "domain_alias",
    "gmail_send_as_alias",
    "group",
    "group_member",
    "group_members",
    "group_settings",
    "org_unit",
    "provider",
    "role",
    "role_assignment",
    "schema",
    "user",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import chrome_policy
from . import data_googleworkspace_chrome_policy_schema
from . import data_googleworkspace_domain
from . import data_googleworkspace_domain_alias
from . import data_googleworkspace_group
from . import data_googleworkspace_group_member
from . import data_googleworkspace_group_members
from . import data_googleworkspace_group_settings
from . import data_googleworkspace_groups
from . import data_googleworkspace_org_unit
from . import data_googleworkspace_privileges
from . import data_googleworkspace_role
from . import data_googleworkspace_schema
from . import data_googleworkspace_user
from . import data_googleworkspace_users
from . import domain
from . import domain_alias
from . import gmail_send_as_alias
from . import group
from . import group_member
from . import group_members
from . import group_settings
from . import org_unit
from . import provider
from . import role
from . import role_assignment
from . import schema
from . import user
