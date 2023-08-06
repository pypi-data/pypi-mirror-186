import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-kubernetes",
    "version": "5.0.0",
    "description": "Prebuilt kubernetes Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-kubernetes.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-kubernetes.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_kubernetes",
        "cdktf_cdktf_provider_kubernetes._jsii",
        "cdktf_cdktf_provider_kubernetes.annotations",
        "cdktf_cdktf_provider_kubernetes.api_service",
        "cdktf_cdktf_provider_kubernetes.api_service_v1",
        "cdktf_cdktf_provider_kubernetes.certificate_signing_request",
        "cdktf_cdktf_provider_kubernetes.certificate_signing_request_v1",
        "cdktf_cdktf_provider_kubernetes.cluster_role",
        "cdktf_cdktf_provider_kubernetes.cluster_role_binding",
        "cdktf_cdktf_provider_kubernetes.cluster_role_binding_v1",
        "cdktf_cdktf_provider_kubernetes.cluster_role_v1",
        "cdktf_cdktf_provider_kubernetes.config_map",
        "cdktf_cdktf_provider_kubernetes.config_map_v1",
        "cdktf_cdktf_provider_kubernetes.config_map_v1_data",
        "cdktf_cdktf_provider_kubernetes.cron_job",
        "cdktf_cdktf_provider_kubernetes.cron_job_v1",
        "cdktf_cdktf_provider_kubernetes.csi_driver",
        "cdktf_cdktf_provider_kubernetes.csi_driver_v1",
        "cdktf_cdktf_provider_kubernetes.daemon_set_v1",
        "cdktf_cdktf_provider_kubernetes.daemonset",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_all_namespaces",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_config_map",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_config_map_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_endpoints_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_ingress",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_ingress_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_mutating_webhook_configuration_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_namespace",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_namespace_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_persistent_volume_claim",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_persistent_volume_claim_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_pod",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_pod_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_resource",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_secret",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_secret_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_service",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_service_account",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_service_account_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_service_v1",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_storage_class",
        "cdktf_cdktf_provider_kubernetes.data_kubernetes_storage_class_v1",
        "cdktf_cdktf_provider_kubernetes.default_service_account",
        "cdktf_cdktf_provider_kubernetes.default_service_account_v1",
        "cdktf_cdktf_provider_kubernetes.deployment",
        "cdktf_cdktf_provider_kubernetes.deployment_v1",
        "cdktf_cdktf_provider_kubernetes.endpoints",
        "cdktf_cdktf_provider_kubernetes.endpoints_v1",
        "cdktf_cdktf_provider_kubernetes.env",
        "cdktf_cdktf_provider_kubernetes.horizontal_pod_autoscaler",
        "cdktf_cdktf_provider_kubernetes.horizontal_pod_autoscaler_v1",
        "cdktf_cdktf_provider_kubernetes.horizontal_pod_autoscaler_v2",
        "cdktf_cdktf_provider_kubernetes.horizontal_pod_autoscaler_v2_beta2",
        "cdktf_cdktf_provider_kubernetes.ingress",
        "cdktf_cdktf_provider_kubernetes.ingress_class",
        "cdktf_cdktf_provider_kubernetes.ingress_class_v1",
        "cdktf_cdktf_provider_kubernetes.ingress_v1",
        "cdktf_cdktf_provider_kubernetes.job",
        "cdktf_cdktf_provider_kubernetes.job_v1",
        "cdktf_cdktf_provider_kubernetes.labels",
        "cdktf_cdktf_provider_kubernetes.limit_range",
        "cdktf_cdktf_provider_kubernetes.limit_range_v1",
        "cdktf_cdktf_provider_kubernetes.manifest",
        "cdktf_cdktf_provider_kubernetes.mutating_webhook_configuration",
        "cdktf_cdktf_provider_kubernetes.mutating_webhook_configuration_v1",
        "cdktf_cdktf_provider_kubernetes.namespace",
        "cdktf_cdktf_provider_kubernetes.namespace_v1",
        "cdktf_cdktf_provider_kubernetes.network_policy",
        "cdktf_cdktf_provider_kubernetes.network_policy_v1",
        "cdktf_cdktf_provider_kubernetes.persistent_volume",
        "cdktf_cdktf_provider_kubernetes.persistent_volume_claim",
        "cdktf_cdktf_provider_kubernetes.persistent_volume_claim_v1",
        "cdktf_cdktf_provider_kubernetes.persistent_volume_v1",
        "cdktf_cdktf_provider_kubernetes.pod",
        "cdktf_cdktf_provider_kubernetes.pod_disruption_budget",
        "cdktf_cdktf_provider_kubernetes.pod_disruption_budget_v1",
        "cdktf_cdktf_provider_kubernetes.pod_security_policy",
        "cdktf_cdktf_provider_kubernetes.pod_security_policy_v1_beta1",
        "cdktf_cdktf_provider_kubernetes.pod_v1",
        "cdktf_cdktf_provider_kubernetes.priority_class",
        "cdktf_cdktf_provider_kubernetes.priority_class_v1",
        "cdktf_cdktf_provider_kubernetes.provider",
        "cdktf_cdktf_provider_kubernetes.replication_controller",
        "cdktf_cdktf_provider_kubernetes.replication_controller_v1",
        "cdktf_cdktf_provider_kubernetes.resource_quota",
        "cdktf_cdktf_provider_kubernetes.resource_quota_v1",
        "cdktf_cdktf_provider_kubernetes.role",
        "cdktf_cdktf_provider_kubernetes.role_binding",
        "cdktf_cdktf_provider_kubernetes.role_binding_v1",
        "cdktf_cdktf_provider_kubernetes.role_v1",
        "cdktf_cdktf_provider_kubernetes.secret",
        "cdktf_cdktf_provider_kubernetes.secret_v1",
        "cdktf_cdktf_provider_kubernetes.service",
        "cdktf_cdktf_provider_kubernetes.service_account",
        "cdktf_cdktf_provider_kubernetes.service_account_v1",
        "cdktf_cdktf_provider_kubernetes.service_v1",
        "cdktf_cdktf_provider_kubernetes.stateful_set",
        "cdktf_cdktf_provider_kubernetes.stateful_set_v1",
        "cdktf_cdktf_provider_kubernetes.storage_class",
        "cdktf_cdktf_provider_kubernetes.storage_class_v1",
        "cdktf_cdktf_provider_kubernetes.validating_webhook_configuration",
        "cdktf_cdktf_provider_kubernetes.validating_webhook_configuration_v1"
    ],
    "package_data": {
        "cdktf_cdktf_provider_kubernetes._jsii": [
            "provider-kubernetes@5.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_kubernetes": [
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
