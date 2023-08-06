'''
# Terraform CDK dns Provider ~> 3.2

This repo builds and publishes the Terraform dns Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-dns](https://www.npmjs.com/package/@cdktf/provider-dns).

`npm install @cdktf/provider-dns`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-dns](https://pypi.org/project/cdktf-cdktf-provider-dns).

`pipenv install cdktf-cdktf-provider-dns`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Dns](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Dns).

`dotnet add package HashiCorp.Cdktf.Providers.Dns`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-dns](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-dns).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-dns</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-dns-go`](https://github.com/cdktf/cdktf-provider-dns-go) package.

`go get github.com/cdktf/cdktf-provider-dns-go/dns`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-dns).

## Versioning

This project is explicitly not tracking the Terraform dns Provider version 1:1. In fact, it always tracks `latest` of `~> 3.2` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform dns Provider](https://github.com/terraform-providers/terraform-provider-dns)
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
    "a_record_set",
    "aaaa_record_set",
    "cname_record",
    "data_dns_a_record_set",
    "data_dns_aaaa_record_set",
    "data_dns_cname_record_set",
    "data_dns_mx_record_set",
    "data_dns_ns_record_set",
    "data_dns_ptr_record_set",
    "data_dns_srv_record_set",
    "data_dns_txt_record_set",
    "mx_record_set",
    "ns_record_set",
    "provider",
    "ptr_record",
    "srv_record_set",
    "txt_record_set",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import a_record_set
from . import aaaa_record_set
from . import cname_record
from . import data_dns_a_record_set
from . import data_dns_aaaa_record_set
from . import data_dns_cname_record_set
from . import data_dns_mx_record_set
from . import data_dns_ns_record_set
from . import data_dns_ptr_record_set
from . import data_dns_srv_record_set
from . import data_dns_txt_record_set
from . import mx_record_set
from . import ns_record_set
from . import provider
from . import ptr_record
from . import srv_record_set
from . import txt_record_set
