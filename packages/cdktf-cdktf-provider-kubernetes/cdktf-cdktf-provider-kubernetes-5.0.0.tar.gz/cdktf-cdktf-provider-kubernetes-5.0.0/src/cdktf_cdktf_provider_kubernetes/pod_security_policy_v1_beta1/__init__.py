'''
# `kubernetes_pod_security_policy_v1beta1`

Refer to the Terraform Registory for docs: [`kubernetes_pod_security_policy_v1beta1`](https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1).
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

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class PodSecurityPolicyV1Beta1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61f2510fa0377470e239932badf9a8b53b73406fa2ec64db50e62804e671ec1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PodSecurityPolicyV1Beta1Config(
            metadata=metadata,
            spec=spec,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        value = PodSecurityPolicyV1Beta1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[builtins.str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[builtins.str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[builtins.str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[builtins.str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        value = PodSecurityPolicyV1Beta1Spec(
            fs_group=fs_group,
            run_as_user=run_as_user,
            supplemental_groups=supplemental_groups,
            allowed_capabilities=allowed_capabilities,
            allowed_flex_volumes=allowed_flex_volumes,
            allowed_host_paths=allowed_host_paths,
            allowed_proc_mount_types=allowed_proc_mount_types,
            allowed_unsafe_sysctls=allowed_unsafe_sysctls,
            allow_privilege_escalation=allow_privilege_escalation,
            default_add_capabilities=default_add_capabilities,
            default_allow_privilege_escalation=default_allow_privilege_escalation,
            forbidden_sysctls=forbidden_sysctls,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_ports=host_ports,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            required_drop_capabilities=required_drop_capabilities,
            run_as_group=run_as_group,
            se_linux=se_linux,
            volumes=volumes,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "PodSecurityPolicyV1Beta1MetadataOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PodSecurityPolicyV1Beta1SpecOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Metadata"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Spec"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd08d1943f8bfab68ec30bad52e62c7a93c98767a9b83b0b7c7cddfa52ae4d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
        "spec": "spec",
        "id": "id",
    },
)
class PodSecurityPolicyV1Beta1Config(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PodSecurityPolicyV1Beta1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = PodSecurityPolicyV1Beta1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8229c65c03a3431dd32975349b420c928b0bc4d20b44baf7bc6da08595b2ff1a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def metadata(self) -> "PodSecurityPolicyV1Beta1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Metadata", result)

    @builtins.property
    def spec(self) -> "PodSecurityPolicyV1Beta1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PodSecurityPolicyV1Beta1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e6bac2e3459c0bef2f91a7d6faad54365f8615a741bf57a5a97447c48f8932)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1MetadataOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018aa2eaa4c4f5823616aff298bf49f26093d2ab4f1fed340d5c2a536de603c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a426bfa1e3bfc9c7bc82d5bd2e7d4e5721155ce33c85e8e34dd4cd0ad1c7999b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5612ce491f7eb3dc652ac21c77ac9694344dcfaf43af6aed83e3889dc93fbb76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5160e5195239e60395f2c9e1b2c8245007655460140782a653217598766bc980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Metadata]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b7337f78a18b871b49958d0ffecabf3f5be48094649e21043ea7b1e59ddb4df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "fs_group": "fsGroup",
        "run_as_user": "runAsUser",
        "supplemental_groups": "supplementalGroups",
        "allowed_capabilities": "allowedCapabilities",
        "allowed_flex_volumes": "allowedFlexVolumes",
        "allowed_host_paths": "allowedHostPaths",
        "allowed_proc_mount_types": "allowedProcMountTypes",
        "allowed_unsafe_sysctls": "allowedUnsafeSysctls",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "default_add_capabilities": "defaultAddCapabilities",
        "default_allow_privilege_escalation": "defaultAllowPrivilegeEscalation",
        "forbidden_sysctls": "forbiddenSysctls",
        "host_ipc": "hostIpc",
        "host_network": "hostNetwork",
        "host_pid": "hostPid",
        "host_ports": "hostPorts",
        "privileged": "privileged",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "required_drop_capabilities": "requiredDropCapabilities",
        "run_as_group": "runAsGroup",
        "se_linux": "seLinux",
        "volumes": "volumes",
    },
)
class PodSecurityPolicyV1Beta1Spec:
    def __init__(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[builtins.str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[builtins.str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[builtins.str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[builtins.str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        if isinstance(fs_group, dict):
            fs_group = PodSecurityPolicyV1Beta1SpecFsGroup(**fs_group)
        if isinstance(run_as_user, dict):
            run_as_user = PodSecurityPolicyV1Beta1SpecRunAsUser(**run_as_user)
        if isinstance(supplemental_groups, dict):
            supplemental_groups = PodSecurityPolicyV1Beta1SpecSupplementalGroups(**supplemental_groups)
        if isinstance(run_as_group, dict):
            run_as_group = PodSecurityPolicyV1Beta1SpecRunAsGroup(**run_as_group)
        if isinstance(se_linux, dict):
            se_linux = PodSecurityPolicyV1Beta1SpecSeLinux(**se_linux)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ca60debdad3c09a5d24eadd27d465dad7d16468a0356ebcef3eb814b75de041)
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument supplemental_groups", value=supplemental_groups, expected_type=type_hints["supplemental_groups"])
            check_type(argname="argument allowed_capabilities", value=allowed_capabilities, expected_type=type_hints["allowed_capabilities"])
            check_type(argname="argument allowed_flex_volumes", value=allowed_flex_volumes, expected_type=type_hints["allowed_flex_volumes"])
            check_type(argname="argument allowed_host_paths", value=allowed_host_paths, expected_type=type_hints["allowed_host_paths"])
            check_type(argname="argument allowed_proc_mount_types", value=allowed_proc_mount_types, expected_type=type_hints["allowed_proc_mount_types"])
            check_type(argname="argument allowed_unsafe_sysctls", value=allowed_unsafe_sysctls, expected_type=type_hints["allowed_unsafe_sysctls"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument default_add_capabilities", value=default_add_capabilities, expected_type=type_hints["default_add_capabilities"])
            check_type(argname="argument default_allow_privilege_escalation", value=default_allow_privilege_escalation, expected_type=type_hints["default_allow_privilege_escalation"])
            check_type(argname="argument forbidden_sysctls", value=forbidden_sysctls, expected_type=type_hints["forbidden_sysctls"])
            check_type(argname="argument host_ipc", value=host_ipc, expected_type=type_hints["host_ipc"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument host_pid", value=host_pid, expected_type=type_hints["host_pid"])
            check_type(argname="argument host_ports", value=host_ports, expected_type=type_hints["host_ports"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument required_drop_capabilities", value=required_drop_capabilities, expected_type=type_hints["required_drop_capabilities"])
            check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
            check_type(argname="argument se_linux", value=se_linux, expected_type=type_hints["se_linux"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fs_group": fs_group,
            "run_as_user": run_as_user,
            "supplemental_groups": supplemental_groups,
        }
        if allowed_capabilities is not None:
            self._values["allowed_capabilities"] = allowed_capabilities
        if allowed_flex_volumes is not None:
            self._values["allowed_flex_volumes"] = allowed_flex_volumes
        if allowed_host_paths is not None:
            self._values["allowed_host_paths"] = allowed_host_paths
        if allowed_proc_mount_types is not None:
            self._values["allowed_proc_mount_types"] = allowed_proc_mount_types
        if allowed_unsafe_sysctls is not None:
            self._values["allowed_unsafe_sysctls"] = allowed_unsafe_sysctls
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if default_add_capabilities is not None:
            self._values["default_add_capabilities"] = default_add_capabilities
        if default_allow_privilege_escalation is not None:
            self._values["default_allow_privilege_escalation"] = default_allow_privilege_escalation
        if forbidden_sysctls is not None:
            self._values["forbidden_sysctls"] = forbidden_sysctls
        if host_ipc is not None:
            self._values["host_ipc"] = host_ipc
        if host_network is not None:
            self._values["host_network"] = host_network
        if host_pid is not None:
            self._values["host_pid"] = host_pid
        if host_ports is not None:
            self._values["host_ports"] = host_ports
        if privileged is not None:
            self._values["privileged"] = privileged
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if required_drop_capabilities is not None:
            self._values["required_drop_capabilities"] = required_drop_capabilities
        if run_as_group is not None:
            self._values["run_as_group"] = run_as_group
        if se_linux is not None:
            self._values["se_linux"] = se_linux
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def fs_group(self) -> "PodSecurityPolicyV1Beta1SpecFsGroup":
        '''fs_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        '''
        result = self._values.get("fs_group")
        assert result is not None, "Required property 'fs_group' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroup", result)

    @builtins.property
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUser":
        '''run_as_user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        '''
        result = self._values.get("run_as_user")
        assert result is not None, "Required property 'run_as_user' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUser", result)

    @builtins.property
    def supplemental_groups(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroups":
        '''supplemental_groups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        '''
        result = self._values.get("supplemental_groups")
        assert result is not None, "Required property 'supplemental_groups' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroups", result)

    @builtins.property
    def allowed_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedCapabilities is a list of capabilities that can be requested to add to the container.

        Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        '''
        result = self._values.get("allowed_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_flex_volumes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]]:
        '''allowed_flex_volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        '''
        result = self._values.get("allowed_flex_volumes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]], result)

    @builtins.property
    def allowed_host_paths(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]]:
        '''allowed_host_paths block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        '''
        result = self._values.get("allowed_host_paths")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]], result)

    @builtins.property
    def allowed_proc_mount_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AllowedProcMountTypes is an allowlist of allowed ProcMountTypes.

        Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        '''
        result = self._values.get("allowed_proc_mount_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_unsafe_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection.

        Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        '''
        result = self._values.get("allowed_unsafe_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_add_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.

        You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        '''
        result = self._values.get("default_add_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        '''
        result = self._values.get("default_allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def forbidden_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.

        Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        '''
        result = self._values.get("forbidden_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host_ipc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostIPC determines if the policy allows the use of HostIPC in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        '''
        result = self._values.get("host_ipc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_pid(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''hostPID determines if the policy allows the use of HostPID in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        '''
        result = self._values.get("host_pid")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def host_ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]]:
        '''host_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        '''
        result = self._values.get("host_ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]], result)

    @builtins.property
    def privileged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''privileged determines if a pod can request to be run as privileged.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def read_only_root_filesystem(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.

        If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def required_drop_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''requiredDropCapabilities are the capabilities that will be dropped from the container.

        These are required to be dropped and cannot be added.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        '''
        result = self._values.get("required_drop_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def run_as_group(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        '''run_as_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        '''
        result = self._values.get("run_as_group")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], result)

    @builtins.property
    def se_linux(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        '''se_linux block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        '''
        result = self._values.get("se_linux")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''volumes is an allowlist of volume plugins.

        Empty indicates that no volumes may be used. To allow all volumes you may use '*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    jsii_struct_bases=[],
    name_mapping={"driver": "driver"},
)
class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes:
    def __init__(self, *, driver: builtins.str) -> None:
        '''
        :param driver: driver is the name of the Flexvolume driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef4f6d7a19ef3ad9cf37482f0d26ce79ea8e0093f02adcbd007a0abe0079713)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
        }

    @builtins.property
    def driver(self) -> builtins.str:
        '''driver is the name of the Flexvolume driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f26858da49ed7b4a1a53656057be34b2650491963844cdb4bdf8c401d15d738)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d58c540522eec969ef7a9f961bb9d35a3ac07d7f043150e9bdfe549b740020)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a39a6174616e81ad5b631e576dcaf1fedfe14412090346e5ebac85d72f5369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba61a563063fe713364ed47324630114483158256d2e82f950ba1d8be1bed719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1423ba05cc903369a5a2fb11d485a91cb23c9265ad615406c9915f1bd1823ca9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba5b0e10ac24f588823d011dfd5069afa055dc32f6878f0eb0963e1c33ced0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f00b081045bba47873db4486edddb9420668ea6879650547d89044b11973553f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a375fe78d2f8ba466ad1c9ff1a0ec18674cf4327d5a529f2fe9e06e905554e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff4b82a6c5fcc7a1b7880f2c4346613a7dcb80637d994a8fb58d983fe8ed0f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    jsii_struct_bases=[],
    name_mapping={"path_prefix": "pathPrefix", "read_only": "readOnly"},
)
class PodSecurityPolicyV1Beta1SpecAllowedHostPaths:
    def __init__(
        self,
        *,
        path_prefix: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path_prefix: pathPrefix is the path prefix that the host volume must match. It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path. Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        :param read_only: when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__998f3f2b014a818255d16645d7c61ea315e41d29d63855f95194fb398c0b64de)
            check_type(argname="argument path_prefix", value=path_prefix, expected_type=type_hints["path_prefix"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path_prefix": path_prefix,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path_prefix(self) -> builtins.str:
        '''pathPrefix is the path prefix that the host volume must match.

        It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path.

        Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        '''
        result = self._values.get("path_prefix")
        assert result is not None, "Required property 'path_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedHostPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8ff86b4b5a5e9d4c4b0fdd53c6c4fdd6dc2a8183856ac212e146e2f6ce022f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c705be7614c8c8566026c9a52e6d32b8243c1d8ec0d29c0bafd3e3b4cad4b70)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc25cd6eafa5f277404d521485e15e8fadaaee51f664f7f966bc6069112a2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e95978e2caea0557b83418776baca717087562e3f05b13d9af892e67ad0dd002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a67f3926dfb0405004ae340926bbf455154a8fc7fd61aa995768943b917ddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdd086bf86386802fe2ab8da20da2b8ee584c0096fd6be9d3cf6d1ff98c7a26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa98ecc83d9a4cbae57aac2b8545f479b0bc3acaabfdd3b57715dc8f700abb55)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixInput")
    def path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefix")
    def path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefix"))

    @path_prefix.setter
    def path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eec36cd786edf2ff893698b8a3f9a1ad987a57d534a9cdcf1095a1dd9100a36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cf2107c1cccbbf9fd2052c1115474e2b95db98f1f7be9037692107a017c5a69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de98712ef051bb85ae9e4f00f2ecb344fb4e1a2589899c7a3ae88dde394a0afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecFsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a82827e357a42316a4684b225c1223774728cfc864ccaa0a57f53f12ed4c706)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90059fba5c37a3d7bec0d620887b9350f9a491cc0888a6cd64f5ca8c06399266)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f9c56c7216efdc0d0b90745f0a57fb84c187b09a9af88bf691db404695c51ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7b04ea41d074571d1e3f168ffcfd8e753fb82c632fdc7ace64dc00d108070a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3883c20e5971592d021fb68150d31c9bba3b05ffa15f0db01fb5e0270052f6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecFsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b71a1457ca368e25163b617386364474f0f2f80239181c70897cfd21f009de9)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878707e9da84792f581a4e8f8ca933ae9e20136d82e703f3bf788b831cca2339)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c59507ce7a6786715b6192437d9bff5d0a54439bac2a9740c9c19c134ddc36)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6571bb54c06e3662c474fb696d80a38785f29c672ba2dfcf87513b2d57fb79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31b242e16c9c3337ed674178fdc7bec2cd1192ea511882905deb5329ea8e83b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99e11e2e467e5776ff093f27754e9f205dea0f16d99b8be3fc15ebe02e9508f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76aef7201eed3c1856c5420fe308090949067cef0714db4bf67010d2776f2306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992691f59b2c26b13cc5bb3fc31f780959cc3bbbbead5c2a54edc8a022641869)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9da8b57f7a6d89e047dcf59662c1fd5eb788db0c3520b6b19b5da963f31baa8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73838cf68b268c696737aa0a064835ad6f31cd47f54b075ea39bc8390836648b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3771175e1cc6f443163a29a021a938a056cf7eb393687a80aa68f55881745a64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPorts",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecHostPorts:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__098e254691f4d85dddc1b99e7b070eb14298d01dd578713e084fe998df3d93e6)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecHostPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecHostPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80409971d28d2bc2440e2f877313d8326df7cb954a8ddd1ae76834faf7c2ce18)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c450577b7747dad9bcf6e9d65310918a786b6894ea8ef307f60601cc65daaf7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecHostPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b64c56f237c3aa3c3fa990f0c0d521372299b4aac3c27d65630c82ccb16060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de6e0967415bd2fefad152b4419ec20f4445b6af7e9e6bc7463697d1e0cefe77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25f8bb371e0dfec97b269f1c4a961559138f358c629512a0e0ee392606fe648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e4e0cd301a072a38597a2735a8db87d3ce8e87a845b90f2ead80960f6a7ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecHostPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee13b4d56163ce571d7156c529f457ed7cbaa6b6e2f3ea7506322aed91aae620)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f2bbc425dd840a47e4921e5ea5f55d6e9034e36cf5665e84b757d795ebac06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8852ff8d682d8bb083e68eb4760f6d243275dd40030c1907b3a0e42d54e753e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f1b0923955ee0c7729ef810f6369601bfdbfc0d021d93f53bbc4330e4319b56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__721823cd3e87c26d5a8549a7a9027afa19e1bea73d3eeea9607f1582e62369dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedFlexVolumes")
    def put_allowed_flex_volumes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__687c22ca9b69cec3abd6a4c2de7db4366add9312dedad6bad49b9a81ed43778a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedFlexVolumes", [value]))

    @jsii.member(jsii_name="putAllowedHostPaths")
    def put_allowed_host_paths(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9806453dab0f6a679ddddcdd51aaa309ad519e6d86a2908dc80021b6368b8708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedHostPaths", [value]))

    @jsii.member(jsii_name="putFsGroup")
    def put_fs_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecFsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putFsGroup", [value]))

    @jsii.member(jsii_name="putHostPorts")
    def put_host_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3242c02e51e4598ca02f23eeb4bb96a9f69956005ff5545cba2e281ebf6aba67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostPorts", [value]))

    @jsii.member(jsii_name="putRunAsGroup")
    def put_run_as_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsGroup", [value]))

    @jsii.member(jsii_name="putRunAsUser")
    def put_run_as_user(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsUser(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsUser", [value]))

    @jsii.member(jsii_name="putSeLinux")
    def put_se_linux(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        value = PodSecurityPolicyV1Beta1SpecSeLinux(
            rule=rule, se_linux_options=se_linux_options
        )

        return typing.cast(None, jsii.invoke(self, "putSeLinux", [value]))

    @jsii.member(jsii_name="putSupplementalGroups")
    def put_supplemental_groups(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecSupplementalGroups(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putSupplementalGroups", [value]))

    @jsii.member(jsii_name="resetAllowedCapabilities")
    def reset_allowed_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCapabilities", []))

    @jsii.member(jsii_name="resetAllowedFlexVolumes")
    def reset_allowed_flex_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFlexVolumes", []))

    @jsii.member(jsii_name="resetAllowedHostPaths")
    def reset_allowed_host_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHostPaths", []))

    @jsii.member(jsii_name="resetAllowedProcMountTypes")
    def reset_allowed_proc_mount_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedProcMountTypes", []))

    @jsii.member(jsii_name="resetAllowedUnsafeSysctls")
    def reset_allowed_unsafe_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUnsafeSysctls", []))

    @jsii.member(jsii_name="resetAllowPrivilegeEscalation")
    def reset_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetDefaultAddCapabilities")
    def reset_default_add_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAddCapabilities", []))

    @jsii.member(jsii_name="resetDefaultAllowPrivilegeEscalation")
    def reset_default_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetForbiddenSysctls")
    def reset_forbidden_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForbiddenSysctls", []))

    @jsii.member(jsii_name="resetHostIpc")
    def reset_host_ipc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostIpc", []))

    @jsii.member(jsii_name="resetHostNetwork")
    def reset_host_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNetwork", []))

    @jsii.member(jsii_name="resetHostPid")
    def reset_host_pid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPid", []))

    @jsii.member(jsii_name="resetHostPorts")
    def reset_host_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPorts", []))

    @jsii.member(jsii_name="resetPrivileged")
    def reset_privileged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileged", []))

    @jsii.member(jsii_name="resetReadOnlyRootFilesystem")
    def reset_read_only_root_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnlyRootFilesystem", []))

    @jsii.member(jsii_name="resetRequiredDropCapabilities")
    def reset_required_drop_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredDropCapabilities", []))

    @jsii.member(jsii_name="resetRunAsGroup")
    def reset_run_as_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunAsGroup", []))

    @jsii.member(jsii_name="resetSeLinux")
    def reset_se_linux(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinux", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumes")
    def allowed_flex_volumes(
        self,
    ) -> PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, jsii.get(self, "allowedFlexVolumes"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPaths")
    def allowed_host_paths(self) -> PodSecurityPolicyV1Beta1SpecAllowedHostPathsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, jsii.get(self, "allowedHostPaths"))

    @builtins.property
    @jsii.member(jsii_name="fsGroup")
    def fs_group(self) -> PodSecurityPolicyV1Beta1SpecFsGroupOutputReference:
        return typing.cast(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference, jsii.get(self, "fsGroup"))

    @builtins.property
    @jsii.member(jsii_name="hostPorts")
    def host_ports(self) -> PodSecurityPolicyV1Beta1SpecHostPortsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecHostPortsList, jsii.get(self, "hostPorts"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroup")
    def run_as_group(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference", jsii.get(self, "runAsGroup"))

    @builtins.property
    @jsii.member(jsii_name="runAsUser")
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference", jsii.get(self, "runAsUser"))

    @builtins.property
    @jsii.member(jsii_name="seLinux")
    def se_linux(self) -> "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference", jsii.get(self, "seLinux"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroups")
    def supplemental_groups(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference", jsii.get(self, "supplementalGroups"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilitiesInput")
    def allowed_capabilities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumesInput")
    def allowed_flex_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "allowedFlexVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPathsInput")
    def allowed_host_paths_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "allowedHostPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypesInput")
    def allowed_proc_mount_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedProcMountTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctlsInput")
    def allowed_unsafe_sysctls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUnsafeSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalationInput")
    def allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilitiesInput")
    def default_add_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultAddCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalationInput")
    def default_allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "defaultAllowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctlsInput")
    def forbidden_sysctls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forbiddenSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsGroupInput")
    def fs_group_input(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "fsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIpcInput")
    def host_ipc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostIpcInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNetworkInput")
    def host_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPidInput")
    def host_pid_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "hostPidInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPortsInput")
    def host_ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "hostPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedInput")
    def privileged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "privilegedInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystemInput")
    def read_only_root_filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyRootFilesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilitiesInput")
    def required_drop_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiredDropCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroupInput")
    def run_as_group_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], jsii.get(self, "runAsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsUserInput")
    def run_as_user_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"], jsii.get(self, "runAsUserInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxInput")
    def se_linux_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], jsii.get(self, "seLinuxInput"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroupsInput")
    def supplemental_groups_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"], jsii.get(self, "supplementalGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilities")
    def allowed_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCapabilities"))

    @allowed_capabilities.setter
    def allowed_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb8130a6e0b4f6e40cce2d3c36e9a2e1022d2008c0b80b67f10bd0e901313dc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypes")
    def allowed_proc_mount_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedProcMountTypes"))

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414a0c08111bce40d1fff539192a2daabb0d7af189d4324af4a38784e7af5d4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedProcMountTypes", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUnsafeSysctls"))

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0f9d6f99ecb2aca3af7d1ddfaf5881c10bc8ca0f373bb9ac5dd5901ad19fd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUnsafeSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalation")
    def allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowPrivilegeEscalation"))

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ea8d9fbb29b158b18c988a427cb68bac25edc6c88b3747bfd320992efe3b99d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilities")
    def default_add_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultAddCapabilities"))

    @default_add_capabilities.setter
    def default_add_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d35f96179e3e65768e8cd4eb18e13228f9267c49e255a1d8919a4d5c04957ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAddCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalation")
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "defaultAllowPrivilegeEscalation"))

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90ceccfe3cf1faa06af14f05673717da5820fa3297795f265d7bf0712d9acea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAllowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctls")
    def forbidden_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "forbiddenSysctls"))

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2128288a96376dce55277e52cc21007cd86e53085faa18427b2fb94a45c39507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forbiddenSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="hostIpc")
    def host_ipc(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostIpc"))

    @host_ipc.setter
    def host_ipc(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58a39cc8be1c7c339dfda4bc24ecfbc090d973297ad60434af5eaff052b7ed0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostIpc", value)

    @builtins.property
    @jsii.member(jsii_name="hostNetwork")
    def host_network(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostNetwork"))

    @host_network.setter
    def host_network(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d19a307c6856ed2a7c847e40a88fa0b943a1ed06644f6e664e183918c4acd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="hostPid")
    def host_pid(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "hostPid"))

    @host_pid.setter
    def host_pid(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f1642f6f4389296eba07bb82954f80435ab284eb8c98223bde20e0431df258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPid", value)

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "privileged"))

    @privileged.setter
    def privileged(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f11275dba6bb295bdfae3ae14171a88bc33e8696c1680d52fd5d84bb20092d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileged", value)

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystem")
    def read_only_root_filesystem(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnlyRootFilesystem"))

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd3f1b91f53dae5cc8e122cf984db50bc7ee3905d55a4a19d6f545b72b9c1e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnlyRootFilesystem", value)

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilities")
    def required_drop_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiredDropCapabilities"))

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a96722272e885312b183c9fb61500f68d1e72e328a871d5258764f57b687f78b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredDropCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "volumes"))

    @volumes.setter
    def volumes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b722fe5e5f0943fa71e68f64ebbc80b4060b46cd477d989f31ba174c298244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Spec]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Spec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__309ca1d10718237e327db51142243cbfb9b70576eb25dc0ebb59c7d6c91d14bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0cabc0d7bd5374f93fc1efb12cc57e66c9ae5771e264f4242de7ed8b24b4d62)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsGroup values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa87626de12ac721d5c90fdd5e1e67390f53806b9d6aa8d692fa20202f567ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde501869f27985bbe53a5441b810cf14f0ed67821805b24c73349f152047d46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24732194e08d156afed254a449a61885cb5cc26f89aa6ca450fba530f63c96f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def59effcb0e9af25289c895dfca2c2f3c9f3c8982b4c6b13c3ff28b5cd18919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__798a7fd68c21166feb2050f5e3d4956abb1ac34adcc2b45d76bf87189a0b0d27)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6b0c5f0cda736dd7130dc6a45e4f75504fbfc787da28f265ff3b75dc8cc772)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a628de7dd16bbc620839e7e0590a5c1fa45f8abdf54d4af8ea14e330e755e8b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4828b26cfd7dad937acda0056b5d8dad0b93d1c50e98438ba4b94617beb52b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd52d6f6fbeb1dc230a345519bba841fd523c76740d15670c4beee71b3084d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed5ac02857482ae94cec4725dc8b6a3f11dda1580d65f20456cf5a7f381ee1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88ffc342b90deba429c2db0df70c519abe02b9466698ab2ad8b2010ab1998119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9b44052eb935e4d4e8090fd82a6a7faf9456f48100bb56cb5a75dbf1f2c1f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860179fc63bf193fead53c8c5d53c3f55970eb102121a030c049ac86a8c8488a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c92a00763dec6c70a4a8a187aa250e0537e3083285a1145083f43ed1b939c193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8486a28f6b0e225951ab8722d623536dd567bef5e69fc4e3c4861fa3db8f860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUser",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUser:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4efbd8dab5efafbde18545ffcb8c3d4aaf7a464606df09e6f74790c63c4188d2)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsUser values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26b9eb5912e52f1cca7c9f1dfce180eb3b81669f398e653500f949586f97f24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bb0a4de710f4f503f0fbdafb443f5a1d314c086536ee0f280e81100533c2d7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd03e8ec48309c31df2c7ea356d8da616b8c4f4d7eb0be37d91e061cc61ebd09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8646ef69fbc4c350c3221d144820c159d56344b88baef7217bff293e36a82a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUserRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa67717fc0729463be863bff2293d6486adf18bf1613bab27ea28515150e178)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUserRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ba736a4c4c27d923f39a8bf966a7246807104ccf4224dbe5275ba30bbc36bb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd4e88ea385368c6ae6c923b04e17f0343c06fd844ce6cd489734878f6e0781)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a733591285cc5dff5783a9a4a25250f506ac9b4ffbb6528b70fed3899d25e68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d9f63900c55711c97f7f069172f0c2d6dd0922d9c4f13818276da657fe1004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__312b182b75e831247e3be3c97c861616a32ab29f96dff1becb614a29313cac7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfdc6fc7c2283f30700aee5d011120661cc923de0af6f3351233e7e8f6d26d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a64685a1ced0f03351d2796c86d5542a4c7c47a30cb18107018ca75df379dd37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a18c9a13797f568433c14e5c3d2b0cfcd8e3aeee1eb6f01af5d2de1a59a4d10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db5337304a51d19d227aa65b5fc723689f4b806df6d76ae94db862fc7de3328b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a51f9ae393af3b6b1286fe56520c8ec7d97b22c0aeb50a7eca14349f4a4349bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinux",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "se_linux_options": "seLinuxOptions"},
)
class PodSecurityPolicyV1Beta1SpecSeLinux:
    def __init__(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ade509f970cc7cda00794f06cf1cac68e6f57fefdd1ded51e157fe20388e62a)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument se_linux_options", value=se_linux_options, expected_type=type_hints["se_linux_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if se_linux_options is not None:
            self._values["se_linux_options"] = se_linux_options

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable labels that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def se_linux_options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        '''se_linux_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        result = self._values.get("se_linux_options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinux(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee2042331765f33ad8da39c0dd0e1c34fe8050070cc19965cb16d2a37b09dea4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSeLinuxOptions")
    def put_se_linux_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d432c60bddab4b54e6a7fb175f803aeba74080099836eecf16dc00270560bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSeLinuxOptions", [value]))

    @jsii.member(jsii_name="resetSeLinuxOptions")
    def reset_se_linux_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinuxOptions", []))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptions")
    def se_linux_options(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList", jsii.get(self, "seLinuxOptions"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptionsInput")
    def se_linux_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], jsii.get(self, "seLinuxOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__015e573c4f8ee348ff02dce47b3e2faf0c68d1458be1564cf0c56dd11388f945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2da7f2855cd2fe9fde78f986dee84c723169fcae940662dae222c4de29a5c52d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "role": "role", "type": "type", "user": "user"},
)
class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions:
    def __init__(
        self,
        *,
        level: builtins.str,
        role: builtins.str,
        type: builtins.str,
        user: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.
        :param user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86cb06d13da55de6498e484bc01be857c48b2a81f5c0300d4c02220cbefce31)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "level": level,
            "role": role,
            "type": type,
            "user": user,
        }

    @builtins.property
    def level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.'''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d9fbcf8d2d2b03b840ae02f485a4fb0e25ad5f100db2c1725ac49295fe5422)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d38651311550fde0b96ec99ccf8f9fe5916678949f417a0f2f694ec1615c94)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4604f839d4acf2f77378c9ab5634526ac422998c6af86ece4804153b0c14f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348cd79d5dfdd7620b31cbb536e9d5640ba4bb70d37a6803b3d727da380218ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dffeaacea43665e452a97a5fc1c903839e6985ebeb136b74bc07209b2b8ad8c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c218895db160e3f89c582e4f65b9679eef1933a623e5e0a100bcd32a15120e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be310cfc7e76c5a88baf7f89bd35b72a89d6dc5413f124ab6a195be316cc1192)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8955a7bc1b92bbf521cdf13486ee41fbdc58ef9eea6796387fb8f917c952b1ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec3d8fb2344dcaec41ac3e04d9d2d67b9acc2d6dd0b17960aef78a537596b69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd18049887ce08eb3e1317a9499bd777aa9039954b47c36fd8116f86d71521b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55a8f9add063c13ba62e412dcead6649865c5e7fb34cd5ab5151598c675979f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a0aee5bf2f166d41293753cdd8bbf78f0be38f650ee6f8dbded4419bc30ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroups:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a826324ade1a8b56ed5d8c9d82eb245ec4125667a0fac6390cfd1ffc946ee2c5)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e0cca0463b065d95fc573482983e51c70329e852a76357297c2dfeebefe799c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69231e216264093fe06bbf88128b31c10f1ac4877a634a88647795f2c5a6dfc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdece2e6b8988b40805fcf1ddd7c3e211264e28f759bc7d3444ae180458081e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__241a478303384c4eb7214545f404ce9660559c67c0301a083a52e44387c570f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99465e44ac18739836c2313b57f82ba61330d1f11d75ffbb4b2aee5475cfadf)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__063e9f932d5216eb34fb042f78f57866bcd6bd17acef26a690692cfe81f2e9a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2136d6d2e324408498c53c7d2dbaf109271becdb0b65eeb45d387eb8cda55ede)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b6962003bffd660e04af215ec4eb39b3b4a74d2cddeb718dc3f153e21a1efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9424fcc7b59c27bb5f50c6d67104e5781acd0f05101369304144426b97ac0437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff785ec78b80bcb41502892b32b2c68ade4c67b3637b03653be886f611d3db41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__835b33f88488ba27e023e91208cd684c30aafa72d1b64c774f0b02a78a5da072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a6b8640eadfd3fbc9e37712c45786d5a236ba42d016ec7ad7308b00ebb166d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e9c709a3b7ccfbff41b3d03d9a77e07a03bf0cd9740af50a54e2aafe92a0e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07cbdbb6dc74512509d6f7dc1fd5f295b652c7b5147d61f6874b262464b3760a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc209649cef49104f36e4c2978aea783250c0b7317d98c17afba1b8eda941fc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PodSecurityPolicyV1Beta1",
    "PodSecurityPolicyV1Beta1Config",
    "PodSecurityPolicyV1Beta1Metadata",
    "PodSecurityPolicyV1Beta1MetadataOutputReference",
    "PodSecurityPolicyV1Beta1Spec",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroup",
    "PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroupRange",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecHostPorts",
    "PodSecurityPolicyV1Beta1SpecHostPortsList",
    "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
    "PodSecurityPolicyV1Beta1SpecOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroup",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUser",
    "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinux",
    "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
]

publication.publish()

def _typecheckingstub__f61f2510fa0377470e239932badf9a8b53b73406fa2ec64db50e62804e671ec1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[PodSecurityPolicyV1Beta1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[PodSecurityPolicyV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd08d1943f8bfab68ec30bad52e62c7a93c98767a9b83b0b7c7cddfa52ae4d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8229c65c03a3431dd32975349b420c928b0bc4d20b44baf7bc6da08595b2ff1a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[PodSecurityPolicyV1Beta1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[PodSecurityPolicyV1Beta1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e6bac2e3459c0bef2f91a7d6faad54365f8615a741bf57a5a97447c48f8932(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018aa2eaa4c4f5823616aff298bf49f26093d2ab4f1fed340d5c2a536de603c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a426bfa1e3bfc9c7bc82d5bd2e7d4e5721155ce33c85e8e34dd4cd0ad1c7999b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5612ce491f7eb3dc652ac21c77ac9694344dcfaf43af6aed83e3889dc93fbb76(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5160e5195239e60395f2c9e1b2c8245007655460140782a653217598766bc980(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7337f78a18b871b49958d0ffecabf3f5be48094649e21043ea7b1e59ddb4df(
    value: typing.Optional[PodSecurityPolicyV1Beta1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca60debdad3c09a5d24eadd27d465dad7d16468a0356ebcef3eb814b75de041(
    *,
    fs_group: typing.Union[PodSecurityPolicyV1Beta1SpecFsGroup, typing.Dict[builtins.str, typing.Any]],
    run_as_user: typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUser, typing.Dict[builtins.str, typing.Any]],
    supplemental_groups: typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroups, typing.Dict[builtins.str, typing.Any]],
    allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_flex_volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allowed_host_paths: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
    host_ipc: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_pid: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    host_ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    run_as_group: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    se_linux: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinux, typing.Dict[builtins.str, typing.Any]]] = None,
    volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef4f6d7a19ef3ad9cf37482f0d26ce79ea8e0093f02adcbd007a0abe0079713(
    *,
    driver: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f26858da49ed7b4a1a53656057be34b2650491963844cdb4bdf8c401d15d738(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d58c540522eec969ef7a9f961bb9d35a3ac07d7f043150e9bdfe549b740020(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a39a6174616e81ad5b631e576dcaf1fedfe14412090346e5ebac85d72f5369(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba61a563063fe713364ed47324630114483158256d2e82f950ba1d8be1bed719(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1423ba05cc903369a5a2fb11d485a91cb23c9265ad615406c9915f1bd1823ca9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba5b0e10ac24f588823d011dfd5069afa055dc32f6878f0eb0963e1c33ced0c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f00b081045bba47873db4486edddb9420668ea6879650547d89044b11973553f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a375fe78d2f8ba466ad1c9ff1a0ec18674cf4327d5a529f2fe9e06e905554e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff4b82a6c5fcc7a1b7880f2c4346613a7dcb80637d994a8fb58d983fe8ed0f58(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__998f3f2b014a818255d16645d7c61ea315e41d29d63855f95194fb398c0b64de(
    *,
    path_prefix: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ff86b4b5a5e9d4c4b0fdd53c6c4fdd6dc2a8183856ac212e146e2f6ce022f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c705be7614c8c8566026c9a52e6d32b8243c1d8ec0d29c0bafd3e3b4cad4b70(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc25cd6eafa5f277404d521485e15e8fadaaee51f664f7f966bc6069112a2f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95978e2caea0557b83418776baca717087562e3f05b13d9af892e67ad0dd002(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a67f3926dfb0405004ae340926bbf455154a8fc7fd61aa995768943b917ddd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdd086bf86386802fe2ab8da20da2b8ee584c0096fd6be9d3cf6d1ff98c7a26(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa98ecc83d9a4cbae57aac2b8545f479b0bc3acaabfdd3b57715dc8f700abb55(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eec36cd786edf2ff893698b8a3f9a1ad987a57d534a9cdcf1095a1dd9100a36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf2107c1cccbbf9fd2052c1115474e2b95db98f1f7be9037692107a017c5a69(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de98712ef051bb85ae9e4f00f2ecb344fb4e1a2589899c7a3ae88dde394a0afa(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a82827e357a42316a4684b225c1223774728cfc864ccaa0a57f53f12ed4c706(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90059fba5c37a3d7bec0d620887b9350f9a491cc0888a6cd64f5ca8c06399266(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9c56c7216efdc0d0b90745f0a57fb84c187b09a9af88bf691db404695c51ba(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b04ea41d074571d1e3f168ffcfd8e753fb82c632fdc7ace64dc00d108070a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3883c20e5971592d021fb68150d31c9bba3b05ffa15f0db01fb5e0270052f6f(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b71a1457ca368e25163b617386364474f0f2f80239181c70897cfd21f009de9(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878707e9da84792f581a4e8f8ca933ae9e20136d82e703f3bf788b831cca2339(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c59507ce7a6786715b6192437d9bff5d0a54439bac2a9740c9c19c134ddc36(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6571bb54c06e3662c474fb696d80a38785f29c672ba2dfcf87513b2d57fb79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31b242e16c9c3337ed674178fdc7bec2cd1192ea511882905deb5329ea8e83b9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99e11e2e467e5776ff093f27754e9f205dea0f16d99b8be3fc15ebe02e9508f1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76aef7201eed3c1856c5420fe308090949067cef0714db4bf67010d2776f2306(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992691f59b2c26b13cc5bb3fc31f780959cc3bbbbead5c2a54edc8a022641869(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da8b57f7a6d89e047dcf59662c1fd5eb788db0c3520b6b19b5da963f31baa8f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73838cf68b268c696737aa0a064835ad6f31cd47f54b075ea39bc8390836648b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3771175e1cc6f443163a29a021a938a056cf7eb393687a80aa68f55881745a64(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__098e254691f4d85dddc1b99e7b070eb14298d01dd578713e084fe998df3d93e6(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80409971d28d2bc2440e2f877313d8326df7cb954a8ddd1ae76834faf7c2ce18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c450577b7747dad9bcf6e9d65310918a786b6894ea8ef307f60601cc65daaf7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b64c56f237c3aa3c3fa990f0c0d521372299b4aac3c27d65630c82ccb16060(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6e0967415bd2fefad152b4419ec20f4445b6af7e9e6bc7463697d1e0cefe77(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25f8bb371e0dfec97b269f1c4a961559138f358c629512a0e0ee392606fe648(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e4e0cd301a072a38597a2735a8db87d3ce8e87a845b90f2ead80960f6a7ad1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee13b4d56163ce571d7156c529f457ed7cbaa6b6e2f3ea7506322aed91aae620(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f2bbc425dd840a47e4921e5ea5f55d6e9034e36cf5665e84b757d795ebac06(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8852ff8d682d8bb083e68eb4760f6d243275dd40030c1907b3a0e42d54e753e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f1b0923955ee0c7729ef810f6369601bfdbfc0d021d93f53bbc4330e4319b56(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__721823cd3e87c26d5a8549a7a9027afa19e1bea73d3eeea9607f1582e62369dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__687c22ca9b69cec3abd6a4c2de7db4366add9312dedad6bad49b9a81ed43778a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9806453dab0f6a679ddddcdd51aaa309ad519e6d86a2908dc80021b6368b8708(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3242c02e51e4598ca02f23eeb4bb96a9f69956005ff5545cba2e281ebf6aba67(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8130a6e0b4f6e40cce2d3c36e9a2e1022d2008c0b80b67f10bd0e901313dc6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414a0c08111bce40d1fff539192a2daabb0d7af189d4324af4a38784e7af5d4a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0f9d6f99ecb2aca3af7d1ddfaf5881c10bc8ca0f373bb9ac5dd5901ad19fd8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ea8d9fbb29b158b18c988a427cb68bac25edc6c88b3747bfd320992efe3b99d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d35f96179e3e65768e8cd4eb18e13228f9267c49e255a1d8919a4d5c04957ed(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ceccfe3cf1faa06af14f05673717da5820fa3297795f265d7bf0712d9acea8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2128288a96376dce55277e52cc21007cd86e53085faa18427b2fb94a45c39507(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a39cc8be1c7c339dfda4bc24ecfbc090d973297ad60434af5eaff052b7ed0e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d19a307c6856ed2a7c847e40a88fa0b943a1ed06644f6e664e183918c4acd8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f1642f6f4389296eba07bb82954f80435ab284eb8c98223bde20e0431df258(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f11275dba6bb295bdfae3ae14171a88bc33e8696c1680d52fd5d84bb20092d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd3f1b91f53dae5cc8e122cf984db50bc7ee3905d55a4a19d6f545b72b9c1e4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a96722272e885312b183c9fb61500f68d1e72e328a871d5258764f57b687f78b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b722fe5e5f0943fa71e68f64ebbc80b4060b46cd477d989f31ba174c298244(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309ca1d10718237e327db51142243cbfb9b70576eb25dc0ebb59c7d6c91d14bf(
    value: typing.Optional[PodSecurityPolicyV1Beta1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0cabc0d7bd5374f93fc1efb12cc57e66c9ae5771e264f4242de7ed8b24b4d62(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa87626de12ac721d5c90fdd5e1e67390f53806b9d6aa8d692fa20202f567ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde501869f27985bbe53a5441b810cf14f0ed67821805b24c73349f152047d46(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24732194e08d156afed254a449a61885cb5cc26f89aa6ca450fba530f63c96f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def59effcb0e9af25289c895dfca2c2f3c9f3c8982b4c6b13c3ff28b5cd18919(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798a7fd68c21166feb2050f5e3d4956abb1ac34adcc2b45d76bf87189a0b0d27(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6b0c5f0cda736dd7130dc6a45e4f75504fbfc787da28f265ff3b75dc8cc772(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a628de7dd16bbc620839e7e0590a5c1fa45f8abdf54d4af8ea14e330e755e8b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4828b26cfd7dad937acda0056b5d8dad0b93d1c50e98438ba4b94617beb52b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd52d6f6fbeb1dc230a345519bba841fd523c76740d15670c4beee71b3084d6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed5ac02857482ae94cec4725dc8b6a3f11dda1580d65f20456cf5a7f381ee1d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ffc342b90deba429c2db0df70c519abe02b9466698ab2ad8b2010ab1998119(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9b44052eb935e4d4e8090fd82a6a7faf9456f48100bb56cb5a75dbf1f2c1f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860179fc63bf193fead53c8c5d53c3f55970eb102121a030c049ac86a8c8488a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92a00763dec6c70a4a8a187aa250e0537e3083285a1145083f43ed1b939c193(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8486a28f6b0e225951ab8722d623536dd567bef5e69fc4e3c4861fa3db8f860(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4efbd8dab5efafbde18545ffcb8c3d4aaf7a464606df09e6f74790c63c4188d2(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26b9eb5912e52f1cca7c9f1dfce180eb3b81669f398e653500f949586f97f24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb0a4de710f4f503f0fbdafb443f5a1d314c086536ee0f280e81100533c2d7e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd03e8ec48309c31df2c7ea356d8da616b8c4f4d7eb0be37d91e061cc61ebd09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8646ef69fbc4c350c3221d144820c159d56344b88baef7217bff293e36a82a7d(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa67717fc0729463be863bff2293d6486adf18bf1613bab27ea28515150e178(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba736a4c4c27d923f39a8bf966a7246807104ccf4224dbe5275ba30bbc36bb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd4e88ea385368c6ae6c923b04e17f0343c06fd844ce6cd489734878f6e0781(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a733591285cc5dff5783a9a4a25250f506ac9b4ffbb6528b70fed3899d25e68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d9f63900c55711c97f7f069172f0c2d6dd0922d9c4f13818276da657fe1004(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__312b182b75e831247e3be3c97c861616a32ab29f96dff1becb614a29313cac7d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfdc6fc7c2283f30700aee5d011120661cc923de0af6f3351233e7e8f6d26d3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64685a1ced0f03351d2796c86d5542a4c7c47a30cb18107018ca75df379dd37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a18c9a13797f568433c14e5c3d2b0cfcd8e3aeee1eb6f01af5d2de1a59a4d10(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db5337304a51d19d227aa65b5fc723689f4b806df6d76ae94db862fc7de3328b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51f9ae393af3b6b1286fe56520c8ec7d97b22c0aeb50a7eca14349f4a4349bf(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ade509f970cc7cda00794f06cf1cac68e6f57fefdd1ded51e157fe20388e62a(
    *,
    rule: builtins.str,
    se_linux_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2042331765f33ad8da39c0dd0e1c34fe8050070cc19965cb16d2a37b09dea4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d432c60bddab4b54e6a7fb175f803aeba74080099836eecf16dc00270560bf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015e573c4f8ee348ff02dce47b3e2faf0c68d1458be1564cf0c56dd11388f945(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2da7f2855cd2fe9fde78f986dee84c723169fcae940662dae222c4de29a5c52d(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86cb06d13da55de6498e484bc01be857c48b2a81f5c0300d4c02220cbefce31(
    *,
    level: builtins.str,
    role: builtins.str,
    type: builtins.str,
    user: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d9fbcf8d2d2b03b840ae02f485a4fb0e25ad5f100db2c1725ac49295fe5422(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d38651311550fde0b96ec99ccf8f9fe5916678949f417a0f2f694ec1615c94(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4604f839d4acf2f77378c9ab5634526ac422998c6af86ece4804153b0c14f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348cd79d5dfdd7620b31cbb536e9d5640ba4bb70d37a6803b3d727da380218ee(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dffeaacea43665e452a97a5fc1c903839e6985ebeb136b74bc07209b2b8ad8c6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c218895db160e3f89c582e4f65b9679eef1933a623e5e0a100bcd32a15120e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be310cfc7e76c5a88baf7f89bd35b72a89d6dc5413f124ab6a195be316cc1192(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8955a7bc1b92bbf521cdf13486ee41fbdc58ef9eea6796387fb8f917c952b1ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec3d8fb2344dcaec41ac3e04d9d2d67b9acc2d6dd0b17960aef78a537596b69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd18049887ce08eb3e1317a9499bd777aa9039954b47c36fd8116f86d71521b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a8f9add063c13ba62e412dcead6649865c5e7fb34cd5ab5151598c675979f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a0aee5bf2f166d41293753cdd8bbf78f0be38f650ee6f8dbded4419bc30ae9(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a826324ade1a8b56ed5d8c9d82eb245ec4125667a0fac6390cfd1ffc946ee2c5(
    *,
    rule: builtins.str,
    range: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0cca0463b065d95fc573482983e51c70329e852a76357297c2dfeebefe799c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69231e216264093fe06bbf88128b31c10f1ac4877a634a88647795f2c5a6dfc5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdece2e6b8988b40805fcf1ddd7c3e211264e28f759bc7d3444ae180458081e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__241a478303384c4eb7214545f404ce9660559c67c0301a083a52e44387c570f1(
    value: typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99465e44ac18739836c2313b57f82ba61330d1f11d75ffbb4b2aee5475cfadf(
    *,
    max: jsii.Number,
    min: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__063e9f932d5216eb34fb042f78f57866bcd6bd17acef26a690692cfe81f2e9a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2136d6d2e324408498c53c7d2dbaf109271becdb0b65eeb45d387eb8cda55ede(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b6962003bffd660e04af215ec4eb39b3b4a74d2cddeb718dc3f153e21a1efe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9424fcc7b59c27bb5f50c6d67104e5781acd0f05101369304144426b97ac0437(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff785ec78b80bcb41502892b32b2c68ade4c67b3637b03653be886f611d3db41(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__835b33f88488ba27e023e91208cd684c30aafa72d1b64c774f0b02a78a5da072(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a6b8640eadfd3fbc9e37712c45786d5a236ba42d016ec7ad7308b00ebb166d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e9c709a3b7ccfbff41b3d03d9a77e07a03bf0cd9740af50a54e2aafe92a0e9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07cbdbb6dc74512509d6f7dc1fd5f295b652c7b5147d61f6874b262464b3760a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc209649cef49104f36e4c2978aea783250c0b7317d98c17afba1b8eda941fc8(
    value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
