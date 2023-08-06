'''
# Terraform CDK kubernetes Provider ~> 2.0

This repo builds and publishes the Terraform kubernetes Provider bindings for [CDK for Terraform](https://cdk.tf).

## Available Packages

### NPM

The npm package is available at [https://www.npmjs.com/package/@cdktf/provider-kubernetes](https://www.npmjs.com/package/@cdktf/provider-kubernetes).

`npm install @cdktf/provider-kubernetes`

### PyPI

The PyPI package is available at [https://pypi.org/project/cdktf-cdktf-provider-kubernetes](https://pypi.org/project/cdktf-cdktf-provider-kubernetes).

`pipenv install cdktf-cdktf-provider-kubernetes`

### Nuget

The Nuget package is available at [https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Kubernetes](https://www.nuget.org/packages/HashiCorp.Cdktf.Providers.Kubernetes).

`dotnet add package HashiCorp.Cdktf.Providers.Kubernetes`

### Maven

The Maven package is available at [https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-kubernetes](https://mvnrepository.com/artifact/com.hashicorp/cdktf-provider-kubernetes).

```
<dependency>
    <groupId>com.hashicorp</groupId>
    <artifactId>cdktf-provider-kubernetes</artifactId>
    <version>[REPLACE WITH DESIRED VERSION]</version>
</dependency>
```

### Go

The go package is generated into the [`github.com/cdktf/cdktf-provider-kubernetes-go`](https://github.com/cdktf/cdktf-provider-kubernetes-go) package.

`go get github.com/cdktf/cdktf-provider-kubernetes-go/kubernetes`

## Docs

Find auto-generated docs for this provider here: [./API.md](./API.md)
You can also visit a hosted version of the documentation on [constructs.dev](https://constructs.dev/packages/@cdktf/provider-kubernetes).

## Versioning

This project is explicitly not tracking the Terraform kubernetes Provider version 1:1. In fact, it always tracks `latest` of `~> 2.0` with every release. If there are scenarios where you explicitly have to pin your provider version, you can do so by generating the [provider constructs manually](https://cdk.tf/imports).

These are the upstream dependencies:

* [Terraform CDK](https://cdk.tf)
* [Terraform kubernetes Provider](https://github.com/terraform-providers/terraform-provider-kubernetes)
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
    "annotations",
    "api_service",
    "api_service_v1",
    "certificate_signing_request",
    "certificate_signing_request_v1",
    "cluster_role",
    "cluster_role_binding",
    "cluster_role_binding_v1",
    "cluster_role_v1",
    "config_map",
    "config_map_v1",
    "config_map_v1_data",
    "cron_job",
    "cron_job_v1",
    "csi_driver",
    "csi_driver_v1",
    "daemon_set_v1",
    "daemonset",
    "data_kubernetes_all_namespaces",
    "data_kubernetes_config_map",
    "data_kubernetes_config_map_v1",
    "data_kubernetes_endpoints_v1",
    "data_kubernetes_ingress",
    "data_kubernetes_ingress_v1",
    "data_kubernetes_mutating_webhook_configuration_v1",
    "data_kubernetes_namespace",
    "data_kubernetes_namespace_v1",
    "data_kubernetes_persistent_volume_claim",
    "data_kubernetes_persistent_volume_claim_v1",
    "data_kubernetes_pod",
    "data_kubernetes_pod_v1",
    "data_kubernetes_resource",
    "data_kubernetes_secret",
    "data_kubernetes_secret_v1",
    "data_kubernetes_service",
    "data_kubernetes_service_account",
    "data_kubernetes_service_account_v1",
    "data_kubernetes_service_v1",
    "data_kubernetes_storage_class",
    "data_kubernetes_storage_class_v1",
    "default_service_account",
    "default_service_account_v1",
    "deployment",
    "deployment_v1",
    "endpoints",
    "endpoints_v1",
    "env",
    "horizontal_pod_autoscaler",
    "horizontal_pod_autoscaler_v1",
    "horizontal_pod_autoscaler_v2",
    "horizontal_pod_autoscaler_v2_beta2",
    "ingress",
    "ingress_class",
    "ingress_class_v1",
    "ingress_v1",
    "job",
    "job_v1",
    "labels",
    "limit_range",
    "limit_range_v1",
    "manifest",
    "mutating_webhook_configuration",
    "mutating_webhook_configuration_v1",
    "namespace",
    "namespace_v1",
    "network_policy",
    "network_policy_v1",
    "persistent_volume",
    "persistent_volume_claim",
    "persistent_volume_claim_v1",
    "persistent_volume_v1",
    "pod",
    "pod_disruption_budget",
    "pod_disruption_budget_v1",
    "pod_security_policy",
    "pod_security_policy_v1_beta1",
    "pod_v1",
    "priority_class",
    "priority_class_v1",
    "provider",
    "replication_controller",
    "replication_controller_v1",
    "resource_quota",
    "resource_quota_v1",
    "role",
    "role_binding",
    "role_binding_v1",
    "role_v1",
    "secret",
    "secret_v1",
    "service",
    "service_account",
    "service_account_v1",
    "service_v1",
    "stateful_set",
    "stateful_set_v1",
    "storage_class",
    "storage_class_v1",
    "validating_webhook_configuration",
    "validating_webhook_configuration_v1",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import annotations
from . import api_service
from . import api_service_v1
from . import certificate_signing_request
from . import certificate_signing_request_v1
from . import cluster_role
from . import cluster_role_binding
from . import cluster_role_binding_v1
from . import cluster_role_v1
from . import config_map
from . import config_map_v1
from . import config_map_v1_data
from . import cron_job
from . import cron_job_v1
from . import csi_driver
from . import csi_driver_v1
from . import daemon_set_v1
from . import daemonset
from . import data_kubernetes_all_namespaces
from . import data_kubernetes_config_map
from . import data_kubernetes_config_map_v1
from . import data_kubernetes_endpoints_v1
from . import data_kubernetes_ingress
from . import data_kubernetes_ingress_v1
from . import data_kubernetes_mutating_webhook_configuration_v1
from . import data_kubernetes_namespace
from . import data_kubernetes_namespace_v1
from . import data_kubernetes_persistent_volume_claim
from . import data_kubernetes_persistent_volume_claim_v1
from . import data_kubernetes_pod
from . import data_kubernetes_pod_v1
from . import data_kubernetes_resource
from . import data_kubernetes_secret
from . import data_kubernetes_secret_v1
from . import data_kubernetes_service
from . import data_kubernetes_service_account
from . import data_kubernetes_service_account_v1
from . import data_kubernetes_service_v1
from . import data_kubernetes_storage_class
from . import data_kubernetes_storage_class_v1
from . import default_service_account
from . import default_service_account_v1
from . import deployment
from . import deployment_v1
from . import endpoints
from . import endpoints_v1
from . import env
from . import horizontal_pod_autoscaler
from . import horizontal_pod_autoscaler_v1
from . import horizontal_pod_autoscaler_v2
from . import horizontal_pod_autoscaler_v2_beta2
from . import ingress
from . import ingress_class
from . import ingress_class_v1
from . import ingress_v1
from . import job
from . import job_v1
from . import labels
from . import limit_range
from . import limit_range_v1
from . import manifest
from . import mutating_webhook_configuration
from . import mutating_webhook_configuration_v1
from . import namespace
from . import namespace_v1
from . import network_policy
from . import network_policy_v1
from . import persistent_volume
from . import persistent_volume_claim
from . import persistent_volume_claim_v1
from . import persistent_volume_v1
from . import pod
from . import pod_disruption_budget
from . import pod_disruption_budget_v1
from . import pod_security_policy
from . import pod_security_policy_v1_beta1
from . import pod_v1
from . import priority_class
from . import priority_class_v1
from . import provider
from . import replication_controller
from . import replication_controller_v1
from . import resource_quota
from . import resource_quota_v1
from . import role
from . import role_binding
from . import role_binding_v1
from . import role_v1
from . import secret
from . import secret_v1
from . import service
from . import service_account
from . import service_account_v1
from . import service_v1
from . import stateful_set
from . import stateful_set_v1
from . import storage_class
from . import storage_class_v1
from . import validating_webhook_configuration
from . import validating_webhook_configuration_v1
