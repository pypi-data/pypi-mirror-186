'''
# `kubernetes_network_policy_v1`

Refer to the Terraform Registory for docs: [`kubernetes_network_policy_v1`](https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1).
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


class NetworkPolicyV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1 kubernetes_network_policy_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["NetworkPolicyV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["NetworkPolicyV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1 kubernetes_network_policy_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#metadata NetworkPolicyV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#spec NetworkPolicyV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#id NetworkPolicyV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b7b86e54ae53d35fdfae40080196fe5a92f59490992e842294b2dd60944889)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkPolicyV1Config(
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
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the network policy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#annotations NetworkPolicyV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#generate_name NetworkPolicyV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the network policy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#labels NetworkPolicyV1#labels}
        :param name: Name of the network policy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#name NetworkPolicyV1#name}
        :param namespace: Namespace defines the space within which name of the network policy must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace NetworkPolicyV1#namespace}
        '''
        value = NetworkPolicyV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
            namespace=namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        pod_selector: typing.Union["NetworkPolicyV1SpecPodSelector", typing.Dict[builtins.str, typing.Any]],
        policy_types: typing.Sequence[builtins.str],
        egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngress", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param pod_selector: pod_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        :param policy_types: List of rule types that the NetworkPolicy relates to. Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an Egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#policy_types NetworkPolicyV1#policy_types}
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#egress NetworkPolicyV1#egress}
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ingress NetworkPolicyV1#ingress}
        '''
        value = NetworkPolicyV1Spec(
            pod_selector=pod_selector,
            policy_types=policy_types,
            egress=egress,
            ingress=ingress,
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
    def metadata(self) -> "NetworkPolicyV1MetadataOutputReference":
        return typing.cast("NetworkPolicyV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "NetworkPolicyV1SpecOutputReference":
        return typing.cast("NetworkPolicyV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["NetworkPolicyV1Metadata"]:
        return typing.cast(typing.Optional["NetworkPolicyV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["NetworkPolicyV1Spec"]:
        return typing.cast(typing.Optional["NetworkPolicyV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2303d0a4bb3134565d46eced1374406f23ed6ee377611f5b70f4ca76dd3439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1Config",
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
class NetworkPolicyV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["NetworkPolicyV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["NetworkPolicyV1Spec", typing.Dict[builtins.str, typing.Any]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#metadata NetworkPolicyV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#spec NetworkPolicyV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#id NetworkPolicyV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = NetworkPolicyV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = NetworkPolicyV1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f39d84ebee8210cecb79db63d90da2ff790eba0177d152447a865571b5bbacc)
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
    def metadata(self) -> "NetworkPolicyV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#metadata NetworkPolicyV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("NetworkPolicyV1Metadata", result)

    @builtins.property
    def spec(self) -> "NetworkPolicyV1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#spec NetworkPolicyV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("NetworkPolicyV1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#id NetworkPolicyV1#id}.

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
        return "NetworkPolicyV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class NetworkPolicyV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the network policy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#annotations NetworkPolicyV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#generate_name NetworkPolicyV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the network policy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#labels NetworkPolicyV1#labels}
        :param name: Name of the network policy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#name NetworkPolicyV1#name}
        :param namespace: Namespace defines the space within which name of the network policy must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace NetworkPolicyV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dbd7932168ed8b6c476b3e7c63d26cd8bb2f1c46d5301fc5088cc5d21e01d64)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the network policy that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#annotations NetworkPolicyV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#generate_name NetworkPolicyV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the network policy.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#labels NetworkPolicyV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the network policy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#name NetworkPolicyV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the network policy must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace NetworkPolicyV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71e3449a3b6e3b8fefca683f9846457adcf023d3839154410ff5e5535dc77b7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetGenerateName")
    def reset_generate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateName", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
    @jsii.member(jsii_name="generateNameInput")
    def generate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generateNameInput"))

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
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e317c65d6ae508c52252ec76895e104af1dd05c16d52a5aae0de6283808fced4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d21cbcca7706c3c212a0fcc34bc9f95850763f99602c7284eca747ed74b7f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d60c7b116b18c5dc9afd11d9cf4b8207301c99061de8c94d45ea506831cbaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e5ecc406facd61a58bec22b95dc1e98d6a9bd48d79eb334437101a2384ca26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0b748e4e10631b87c3eacf649e8df9dc702657eafcef42df6b303859197484)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1Metadata]:
        return typing.cast(typing.Optional[NetworkPolicyV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkPolicyV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baba8a679141c3fc86d3501a67e818f0ff331d02176150094d3c01e05d359108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "pod_selector": "podSelector",
        "policy_types": "policyTypes",
        "egress": "egress",
        "ingress": "ingress",
    },
)
class NetworkPolicyV1Spec:
    def __init__(
        self,
        *,
        pod_selector: typing.Union["NetworkPolicyV1SpecPodSelector", typing.Dict[builtins.str, typing.Any]],
        policy_types: typing.Sequence[builtins.str],
        egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngress", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param pod_selector: pod_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        :param policy_types: List of rule types that the NetworkPolicy relates to. Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an Egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#policy_types NetworkPolicyV1#policy_types}
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#egress NetworkPolicyV1#egress}
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ingress NetworkPolicyV1#ingress}
        '''
        if isinstance(pod_selector, dict):
            pod_selector = NetworkPolicyV1SpecPodSelector(**pod_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29223fb2544a7988e76e7d1576e8b1d7498fac8d2c86c8d6604d3078ddc4faab)
            check_type(argname="argument pod_selector", value=pod_selector, expected_type=type_hints["pod_selector"])
            check_type(argname="argument policy_types", value=policy_types, expected_type=type_hints["policy_types"])
            check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pod_selector": pod_selector,
            "policy_types": policy_types,
        }
        if egress is not None:
            self._values["egress"] = egress
        if ingress is not None:
            self._values["ingress"] = ingress

    @builtins.property
    def pod_selector(self) -> "NetworkPolicyV1SpecPodSelector":
        '''pod_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        '''
        result = self._values.get("pod_selector")
        assert result is not None, "Required property 'pod_selector' is missing"
        return typing.cast("NetworkPolicyV1SpecPodSelector", result)

    @builtins.property
    def policy_types(self) -> typing.List[builtins.str]:
        '''List of rule types that the NetworkPolicy relates to.

        Valid options are ["Ingress"], ["Egress"], or ["Ingress", "Egress"]. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ "Egress" ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include "Egress" (since such a policy would not include an Egress section and would otherwise default to just [ "Ingress" ]). This field is beta-level in 1.8

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#policy_types NetworkPolicyV1#policy_types}
        '''
        result = self._values.get("policy_types")
        assert result is not None, "Required property 'policy_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def egress(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgress"]]]:
        '''egress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#egress NetworkPolicyV1#egress}
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgress"]]], result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngress"]]]:
        '''ingress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ingress NetworkPolicyV1#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngress"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgress",
    jsii_struct_bases=[],
    name_mapping={"ports": "ports", "to": "to"},
)
class NetworkPolicyV1SpecEgress:
    def __init__(
        self,
        *,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        to: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressTo", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ports NetworkPolicyV1#ports}
        :param to: to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#to NetworkPolicyV1#to}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0af20920ad9effe66406c4506e3419cfadfd30aaba5d4dc63f2e76672cef9b10)
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ports is not None:
            self._values["ports"] = ports
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ports NetworkPolicyV1#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressPorts"]]], result)

    @builtins.property
    def to(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressTo"]]]:
        '''to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#to NetworkPolicyV1#to}
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressTo"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecEgressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89e6364dd05f4f9ec69f6fff543d7b8c3875f7973c3b01036167361014167595)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkPolicyV1SpecEgressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878d4f6ff5777f92e6fc82d1cd2fd9daf01704625cb8114a358091db9d9f86f4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecEgressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf424889457b9bc1d0adde4e0bf9de80da072bff211589a36f5a90a475a7580)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2078dcd09dfbd11f3bb15cbf686225e3b9dabdd7bd44b5205ae26e26431a6f2e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8d752c7b04c37feb3a1824330efd030a5d8c17d493dfb8d67e1bc263d033726)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf15caecd59ec69576d1757f6270e2067a4a108e690d6caf4b9135f64239d73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d79a169a023bc3def522aee37f55058bf6b289f56e97ccbd511a7d2d3b650c73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressPorts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96bd8fcef166718003c41bc788258b97e7fe28403f7cd1e0f1eb754d5c5c671a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="putTo")
    def put_to(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressTo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e169a56f5c5fb0a9c882f5654806fa83a7526b60b1e77fe7b851fc3e47409517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTo", [value]))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @jsii.member(jsii_name="resetTo")
    def reset_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTo", []))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "NetworkPolicyV1SpecEgressPortsList":
        return typing.cast("NetworkPolicyV1SpecEgressPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> "NetworkPolicyV1SpecEgressToList":
        return typing.cast("NetworkPolicyV1SpecEgressToList", jsii.get(self, "to"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="toInput")
    def to_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressTo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressTo"]]], jsii.get(self, "toInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecEgress, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecEgress, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgress, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485277436e087e10005914ae0043920c6b2ef6a33b978f77697d75f93bca6260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressPorts",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class NetworkPolicyV1SpecEgressPorts:
    def __init__(
        self,
        *,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#port NetworkPolicyV1#port}
        :param protocol: The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#protocol NetworkPolicyV1#protocol}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb44922464edfdbea4937d1b68e6bb30db7e287f3be682ec3b71e2355c879ff4)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''The port on the given protocol.

        This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#port NetworkPolicyV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#protocol NetworkPolicyV1#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecEgressPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressPortsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ad63e230c998473005cdda986ec4880ed0dc181fe30434c1a4f9fbd5a69b33f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecEgressPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed3c18618855339e98d2efe659eb7f2f79c5643a9ca25d8b1c7e3acca564280)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecEgressPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c053522a755f7b1df4dcd4ad33565d8a196ee2c3ed277c483b6b1fb0e828193f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__521839b2f983866fc524a0222ec29bb8478efd00b6062f9dcd7ad263ec62df02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b346c292bef0b4f22f3b8da4cd8c67f8bef7bae506d747671d2f9843e9d095be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6dc0419b7ce91f885dc71ff05fe725b9e592d65ffca703abf81cd87591a4168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressPortsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__045c726cfe31ecf45e3b25aa27ef63671c8bd2df68ee0f9519c086c49729c774)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d6ad25b174f2ba7ffe94563b284c746f53b0c4c5585ef54edbeee39f158bb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec2a12173be7e2e7bac05aefdb7cc423bbfc8855072f62431379effbdd1de4cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecEgressPorts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecEgressPorts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressPorts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9d535361c34ec6c3d3c58e0dd3ce8872444026c2728f8d52cb54d73f46b3f0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressTo",
    jsii_struct_bases=[],
    name_mapping={
        "ip_block": "ipBlock",
        "namespace_selector": "namespaceSelector",
        "pod_selector": "podSelector",
    },
)
class NetworkPolicyV1SpecEgressTo:
    def __init__(
        self,
        *,
        ip_block: typing.Optional[typing.Union["NetworkPolicyV1SpecEgressToIpBlock", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace_selector: typing.Optional[typing.Union["NetworkPolicyV1SpecEgressToNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_selector: typing.Optional[typing.Union["NetworkPolicyV1SpecEgressToPodSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ip_block: ip_block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ip_block NetworkPolicyV1#ip_block}
        :param namespace_selector: namespace_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace_selector NetworkPolicyV1#namespace_selector}
        :param pod_selector: pod_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        '''
        if isinstance(ip_block, dict):
            ip_block = NetworkPolicyV1SpecEgressToIpBlock(**ip_block)
        if isinstance(namespace_selector, dict):
            namespace_selector = NetworkPolicyV1SpecEgressToNamespaceSelector(**namespace_selector)
        if isinstance(pod_selector, dict):
            pod_selector = NetworkPolicyV1SpecEgressToPodSelector(**pod_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33896808258e17a78ff1961a3180b922b10ba5a61e62cdaee2ae33bc09b3324f)
            check_type(argname="argument ip_block", value=ip_block, expected_type=type_hints["ip_block"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument pod_selector", value=pod_selector, expected_type=type_hints["pod_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_block is not None:
            self._values["ip_block"] = ip_block
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if pod_selector is not None:
            self._values["pod_selector"] = pod_selector

    @builtins.property
    def ip_block(self) -> typing.Optional["NetworkPolicyV1SpecEgressToIpBlock"]:
        '''ip_block block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ip_block NetworkPolicyV1#ip_block}
        '''
        result = self._values.get("ip_block")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecEgressToIpBlock"], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["NetworkPolicyV1SpecEgressToNamespaceSelector"]:
        '''namespace_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace_selector NetworkPolicyV1#namespace_selector}
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecEgressToNamespaceSelector"], result)

    @builtins.property
    def pod_selector(self) -> typing.Optional["NetworkPolicyV1SpecEgressToPodSelector"]:
        '''pod_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        '''
        result = self._values.get("pod_selector")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecEgressToPodSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToIpBlock",
    jsii_struct_bases=[],
    name_mapping={"cidr": "cidr", "except_": "except"},
)
class NetworkPolicyV1SpecEgressToIpBlock:
    def __init__(
        self,
        *,
        cidr: typing.Optional[builtins.str] = None,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cidr: CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        :param except_: Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd0c381d05638efd170ab88eacafaf71ab04a06c760f42f5110574965bc84ad)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument except_", value=except_, expected_type=type_hints["except_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cidr is not None:
            self._values["cidr"] = cidr
        if except_ is not None:
            self._values["except_"] = except_

    @builtins.property
    def cidr(self) -> typing.Optional[builtins.str]:
        '''CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        '''
        result = self._values.get("cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def except_(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        result = self._values.get("except_")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressToIpBlock(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecEgressToIpBlockOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToIpBlockOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0bc7d56fb8655270de53c8363b94354f16e77e99b46ed2e9e29704aa618f273)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCidr")
    def reset_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidr", []))

    @jsii.member(jsii_name="resetExcept")
    def reset_except(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcept", []))

    @builtins.property
    @jsii.member(jsii_name="cidrInput")
    def cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptInput")
    def except_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exceptInput"))

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd87bd4b81eae047790a81fff8207483b2f85af40dd0faac610e50722511f12f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value)

    @builtins.property
    @jsii.member(jsii_name="except")
    def except_(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "except"))

    @except_.setter
    def except_(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d13b080e3828731d407c89bffcf3b09ac62c2bf4c8161c2e4ab7d17678eca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "except", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1SpecEgressToIpBlock]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecEgressToIpBlock], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecEgressToIpBlock],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9b2c8c1cbeb16c8dfd7503c02b652448569f6097b3f7d81d08522193429e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1501d61756887c6e4df1793f261bee21f2987db75dba1a32f0caf20c1166719f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkPolicyV1SpecEgressToOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d430fccb81872a2a6c02a850c51bddbbe190f5402c8ca1bb4e10206bce8fa38b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecEgressToOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e747b67d0a83b125b6183bfb23fddf4738dc4da41fa7d6290e5f4c3abd8982da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6431580bbe6bd646cfaa0efb219a7d2f830e9c2213d8840fcfacc4c01a346fc3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc478e88f2d86c53e139bbb3d1ce25a1e8e521644ce0fa6ff00ed073a0570ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressTo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressTo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressTo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e95f19ca5482600755b1a6f14f546f9d7a0263e2fa9aa50c08ff88bea424ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class NetworkPolicyV1SpecEgressToNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46224dafa402025c8bd584cef3af3e69184fb63f1b4acf16f4a4021d545da01a)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressToNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef0f920abd5d300cd269c5ce12c7f5b13e08e5106ee72703a587848b6ffab05)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__384a004a613b58257a5ef20609b9ce3530a566dc825cf805d303034efb79d27d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481ead2bc8318d1fe08a9ea8d762e200c64a3ef06d8a4c1645c746b696c2f22a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aecfe6439dcad01031389aaeb110969502e16fc30a0e1416e49cb114f428dd2f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0064403e2ab901ab4b2df85a77465decc3a5981f33bafd341c8d6463325331f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0ce12ecb55b160df58d414274c6cd09f601682344b3526d369d6600ae759c5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af4df2dfa51db8e459af9d444403095d2a5d1c78c1eaaa2ecf86d345ea5d4857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a63cccde366ff68a5fdf17dd6d1c782573e6e22ddd315ab07840b46f96fe6ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc2c2fed806267976019a9bddb7a9441773f57d859043d17a27c9a28c00924f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f84cd4624799231a88e3f8ecba5e058d39edc0aaf10477c7a1056a55ae8b7905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c260a386875145ad353490d6a52eb618b5ea005696d03a30ccc7113588e44cb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cccb6e2e6474d8043a93aa69446f50197c36c1cb2ec91b76cb971eae7736c1f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToNamespaceSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToNamespaceSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b2447005d16bbd9f96edefe948983b6266c5d9968e93dba3aeebbcec3d068eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a97c89b6eb397e6554791499002803d591913726d51732c79f4301b466fe68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsList:
        return typing.cast(NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f612d83ab6c08a9bbf76806bfbab78a9244c11950f4137ee3cd415ae17a1e30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f6d865437d95f37973c39312bd15602451477434bda8cb5473c473c97c9a2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1dd682ba4989b8d835ac1daa4b1ffef594d1a530b44910575c3830afb1930b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpBlock")
    def put_ip_block(
        self,
        *,
        cidr: typing.Optional[builtins.str] = None,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cidr: CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        :param except_: Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        value = NetworkPolicyV1SpecEgressToIpBlock(cidr=cidr, except_=except_)

        return typing.cast(None, jsii.invoke(self, "putIpBlock", [value]))

    @jsii.member(jsii_name="putNamespaceSelector")
    def put_namespace_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        value = NetworkPolicyV1SpecEgressToNamespaceSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putNamespaceSelector", [value]))

    @jsii.member(jsii_name="putPodSelector")
    def put_pod_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        value = NetworkPolicyV1SpecEgressToPodSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putPodSelector", [value]))

    @jsii.member(jsii_name="resetIpBlock")
    def reset_ip_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpBlock", []))

    @jsii.member(jsii_name="resetNamespaceSelector")
    def reset_namespace_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceSelector", []))

    @jsii.member(jsii_name="resetPodSelector")
    def reset_pod_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodSelector", []))

    @builtins.property
    @jsii.member(jsii_name="ipBlock")
    def ip_block(self) -> NetworkPolicyV1SpecEgressToIpBlockOutputReference:
        return typing.cast(NetworkPolicyV1SpecEgressToIpBlockOutputReference, jsii.get(self, "ipBlock"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelector")
    def namespace_selector(
        self,
    ) -> NetworkPolicyV1SpecEgressToNamespaceSelectorOutputReference:
        return typing.cast(NetworkPolicyV1SpecEgressToNamespaceSelectorOutputReference, jsii.get(self, "namespaceSelector"))

    @builtins.property
    @jsii.member(jsii_name="podSelector")
    def pod_selector(self) -> "NetworkPolicyV1SpecEgressToPodSelectorOutputReference":
        return typing.cast("NetworkPolicyV1SpecEgressToPodSelectorOutputReference", jsii.get(self, "podSelector"))

    @builtins.property
    @jsii.member(jsii_name="ipBlockInput")
    def ip_block_input(self) -> typing.Optional[NetworkPolicyV1SpecEgressToIpBlock]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecEgressToIpBlock], jsii.get(self, "ipBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelectorInput")
    def namespace_selector_input(
        self,
    ) -> typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector], jsii.get(self, "namespaceSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="podSelectorInput")
    def pod_selector_input(
        self,
    ) -> typing.Optional["NetworkPolicyV1SpecEgressToPodSelector"]:
        return typing.cast(typing.Optional["NetworkPolicyV1SpecEgressToPodSelector"], jsii.get(self, "podSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecEgressTo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecEgressTo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressTo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f87049f066c57f65d058283b699c03fbcf881e872e1b0197e6bafea5c97450ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToPodSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class NetworkPolicyV1SpecEgressToPodSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97aae9f32f785ae89f2fd92709ad034d6736cf8769d3779f37bede980d1d7982)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressToPodSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__960c00ce6264ce404ff93cee04b985fe75ed3b730fdfb3263943788afbc9381c)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee203134c1848e6986e543c5dd36237de488e61909a4d0925cde8612ecceefa6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7350daa58d818acd608a70850af008f7b4ee9504dd34987bfcdfa26709ef4c22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ad71dd0a95e6937bd48092e18b785b78896dff14cd3a5db00a9bd255a800e27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0794ffb7b0cddfbf37885dbfb6fcb39a7ef57f9e4ad1b0c48c16238a25351509)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef9abeabc57be6244de846b62a5cb94596410b4c0c03082357581eb56ed33ce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174725a32b0b6cd16320b903019934af79c4bbe1371c70e9114135cfb93e8b92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94588a001d50fef9fd207299d917fc4ce008f42f891141789c29a28f6697f0e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536d7e1a50629f41b9a4adf5610f06164171627dcb4e22f1496291c263d437f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95244a386dd02467abdf01161dfcf33ea79774bf3e1711ddd519504e79cfa322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8f0f9e29101579c7d84bc35174493eb2b763a4315390bf10f8d06b7449beb0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__625827e6acce481bfa7da4156af8c2d2389f8549ed75f6745f48142a3939c19e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecEgressToPodSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecEgressToPodSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0804bf3ec041c35e9e1b1d0f63cb3795665dd8e5a8ed9b62e629f8bf436dcccd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fe913db8f9cce33410ef1a961133e9356bfac4c28fef2892abad88e85dcf130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsList:
        return typing.cast(NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c86383d7314c5f1131fc77b0699dd4d392c330e52564326c7bafae8677dabf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1SpecEgressToPodSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecEgressToPodSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecEgressToPodSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed9ac3ed3addcde8fa648291d27976d5b5fc3d4200c0ad95cc896812489ff05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngress",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "ports": "ports"},
)
class NetworkPolicyV1SpecIngress:
    def __init__(
        self,
        *,
        from_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressFrom", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param from_: from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#from NetworkPolicyV1#from}
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ports NetworkPolicyV1#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50edd96f967af9de07cfcc1f5ceb575f69bab759b36101a6f796fc034a6cd8b9)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def from_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFrom"]]]:
        '''from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#from NetworkPolicyV1#from}
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFrom"]]], result)

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ports NetworkPolicyV1#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressPorts"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFrom",
    jsii_struct_bases=[],
    name_mapping={
        "ip_block": "ipBlock",
        "namespace_selector": "namespaceSelector",
        "pod_selector": "podSelector",
    },
)
class NetworkPolicyV1SpecIngressFrom:
    def __init__(
        self,
        *,
        ip_block: typing.Optional[typing.Union["NetworkPolicyV1SpecIngressFromIpBlock", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace_selector: typing.Optional[typing.Union["NetworkPolicyV1SpecIngressFromNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        pod_selector: typing.Optional[typing.Union["NetworkPolicyV1SpecIngressFromPodSelector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ip_block: ip_block block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ip_block NetworkPolicyV1#ip_block}
        :param namespace_selector: namespace_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace_selector NetworkPolicyV1#namespace_selector}
        :param pod_selector: pod_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        '''
        if isinstance(ip_block, dict):
            ip_block = NetworkPolicyV1SpecIngressFromIpBlock(**ip_block)
        if isinstance(namespace_selector, dict):
            namespace_selector = NetworkPolicyV1SpecIngressFromNamespaceSelector(**namespace_selector)
        if isinstance(pod_selector, dict):
            pod_selector = NetworkPolicyV1SpecIngressFromPodSelector(**pod_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3ac358d5681d3d0250f2a2413d170a2b1c684bdde04a6a342ac5f8839e7aa0)
            check_type(argname="argument ip_block", value=ip_block, expected_type=type_hints["ip_block"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument pod_selector", value=pod_selector, expected_type=type_hints["pod_selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_block is not None:
            self._values["ip_block"] = ip_block
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if pod_selector is not None:
            self._values["pod_selector"] = pod_selector

    @builtins.property
    def ip_block(self) -> typing.Optional["NetworkPolicyV1SpecIngressFromIpBlock"]:
        '''ip_block block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#ip_block NetworkPolicyV1#ip_block}
        '''
        result = self._values.get("ip_block")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecIngressFromIpBlock"], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["NetworkPolicyV1SpecIngressFromNamespaceSelector"]:
        '''namespace_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#namespace_selector NetworkPolicyV1#namespace_selector}
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecIngressFromNamespaceSelector"], result)

    @builtins.property
    def pod_selector(
        self,
    ) -> typing.Optional["NetworkPolicyV1SpecIngressFromPodSelector"]:
        '''pod_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#pod_selector NetworkPolicyV1#pod_selector}
        '''
        result = self._values.get("pod_selector")
        return typing.cast(typing.Optional["NetworkPolicyV1SpecIngressFromPodSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromIpBlock",
    jsii_struct_bases=[],
    name_mapping={"cidr": "cidr", "except_": "except"},
)
class NetworkPolicyV1SpecIngressFromIpBlock:
    def __init__(
        self,
        *,
        cidr: typing.Optional[builtins.str] = None,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cidr: CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        :param except_: Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7f39010bc2c4af44f386380f07179a66ba71feb59c4653a6fc504078fd4f5b)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument except_", value=except_, expected_type=type_hints["except_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cidr is not None:
            self._values["cidr"] = cidr
        if except_ is not None:
            self._values["except_"] = except_

    @builtins.property
    def cidr(self) -> typing.Optional[builtins.str]:
        '''CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        '''
        result = self._values.get("cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def except_(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        result = self._values.get("except_")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFromIpBlock(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecIngressFromIpBlockOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromIpBlockOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fa75c559d99b09358c74fb31e3ad929a30927b186a06627b432146887224f75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCidr")
    def reset_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidr", []))

    @jsii.member(jsii_name="resetExcept")
    def reset_except(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcept", []))

    @builtins.property
    @jsii.member(jsii_name="cidrInput")
    def cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptInput")
    def except_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exceptInput"))

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11dfd603d28e5bce63620093b97ea0a4ea4044be6d5b8c99f9fb67a38eae7ab4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value)

    @builtins.property
    @jsii.member(jsii_name="except")
    def except_(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "except"))

    @except_.setter
    def except_(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3d1522ff3fbe86721473f160a356b05bec59b62692741895d9fadd5219ceda7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "except", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7679c736e69d4c5f55009fda8298d49741221d4302ec829bb1ae2200b4edf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__389fc6fbcc9d28a45f0086392567c2405b9d6e1c42fba32b15dd312281d6827e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecIngressFromOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdc023da3a86937f307ae5756d9e0e2167fd38547fa018372b2fd5ade4f4a50b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecIngressFromOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d8b8a609d989d09009a3dd760b2dd40fda993edf99865a954f05b1df57032c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__59f2de7a95e6c267e95167aa0b6b5d2a106c04afb4578fac5e65b863c7891647)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7be04a87ecf2eaa5b6d7b8692b438f6452684af248bcdb194d513e22ed15868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3179b867d78c06adfa05e6f93b27109e80affdd722e0eec051a5333540009a28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class NetworkPolicyV1SpecIngressFromNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f912c554476427886bdfa002515e66720f0473d340467929cb210b3ec7e9022b)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFromNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bb7acaa26abbefab2713444dc157cc3480fc6e3a0c7605fd658a81a53d09b53)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fac96aa2ef338f6c5ac09d34f7a7a94d349f46929b3b7a9148f2929f446f856)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7739f42c0411846d6aa5d550f4b93500a99db6a34d2b4a751af7205959f7faf6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6eed9a2d5524c6aa232355142b4527f3a029f40d977615318b802d403be6ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d46527ac3a5eb43ada249a199c9d986c620da27521babedcebb63c8f78bd9cad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89324153501243b4017f15c1ff32c4c11c2ef48fa6cfb5bd69dc5bee47c63f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1549662ed020ad548d3a6675786f701e803d9bf4f86f2ecda46e81fd7b5b8ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b697eb22919f6c224cc53488b5adf9ba7d1616c967eb59cf04fee2d171b96e4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__105a4e274261595631507501772acbada864351c7fcfb2c68f7365c3f2088f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88e01ecf020427b46d440e51ab7f32657b40a99daff0b324dbb4ac8d72756422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0094fc700b6dac5871474a8f6bade01bb261d599c217415b4049cca39e8555e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571f9e3753947c69336bf8248f1f4cb97bc547d50ddd611d14ef0300e713dd79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromNamespaceSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromNamespaceSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab728f3b7c0d5382d8e0a1da7b15657b6878acc52b9e4d5c55fb660707d0b75b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c1b480717e98f1840335d9a1bba08e6192b3e56d24f32cb32631c0c650f94c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsList:
        return typing.cast(NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673e380cd61368c857f1b89130ae794edec510e1d7cd37de2d58047692b7b82a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25bb7825800168a437e822ee289cd184f5cd70ada2a19c96e64627409da0ef13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__88f27558403e3ec11322d2e51308bed0fe6692a4f0fdafdce67b89a4a5859316)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpBlock")
    def put_ip_block(
        self,
        *,
        cidr: typing.Optional[builtins.str] = None,
        except_: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cidr: CIDR is a string representing the IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#cidr NetworkPolicyV1#cidr}
        :param except_: Except is a slice of CIDRs that should not be included within an IP Block Valid examples are "192.168.1.1/24" or "2001:db9::/64" Except values will be rejected if they are outside the CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#except NetworkPolicyV1#except}
        '''
        value = NetworkPolicyV1SpecIngressFromIpBlock(cidr=cidr, except_=except_)

        return typing.cast(None, jsii.invoke(self, "putIpBlock", [value]))

    @jsii.member(jsii_name="putNamespaceSelector")
    def put_namespace_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        value = NetworkPolicyV1SpecIngressFromNamespaceSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putNamespaceSelector", [value]))

    @jsii.member(jsii_name="putPodSelector")
    def put_pod_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        value = NetworkPolicyV1SpecIngressFromPodSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putPodSelector", [value]))

    @jsii.member(jsii_name="resetIpBlock")
    def reset_ip_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpBlock", []))

    @jsii.member(jsii_name="resetNamespaceSelector")
    def reset_namespace_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceSelector", []))

    @jsii.member(jsii_name="resetPodSelector")
    def reset_pod_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodSelector", []))

    @builtins.property
    @jsii.member(jsii_name="ipBlock")
    def ip_block(self) -> NetworkPolicyV1SpecIngressFromIpBlockOutputReference:
        return typing.cast(NetworkPolicyV1SpecIngressFromIpBlockOutputReference, jsii.get(self, "ipBlock"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelector")
    def namespace_selector(
        self,
    ) -> NetworkPolicyV1SpecIngressFromNamespaceSelectorOutputReference:
        return typing.cast(NetworkPolicyV1SpecIngressFromNamespaceSelectorOutputReference, jsii.get(self, "namespaceSelector"))

    @builtins.property
    @jsii.member(jsii_name="podSelector")
    def pod_selector(
        self,
    ) -> "NetworkPolicyV1SpecIngressFromPodSelectorOutputReference":
        return typing.cast("NetworkPolicyV1SpecIngressFromPodSelectorOutputReference", jsii.get(self, "podSelector"))

    @builtins.property
    @jsii.member(jsii_name="ipBlockInput")
    def ip_block_input(self) -> typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock], jsii.get(self, "ipBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelectorInput")
    def namespace_selector_input(
        self,
    ) -> typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector], jsii.get(self, "namespaceSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="podSelectorInput")
    def pod_selector_input(
        self,
    ) -> typing.Optional["NetworkPolicyV1SpecIngressFromPodSelector"]:
        return typing.cast(typing.Optional["NetworkPolicyV1SpecIngressFromPodSelector"], jsii.get(self, "podSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFrom, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFrom, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFrom, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8abdb3d63c3f295537782c7b2be852d11a5674f5d6ca27de37df14dd290366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromPodSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class NetworkPolicyV1SpecIngressFromPodSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8646ba3cb0d995a5faf3971e79eca281ea33e1d1d3426e8672ee915cf242c4f7)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFromPodSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b30be4504b05b763e09cd67436505017b287da978720c8d2a710e6b72b61c2)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ed470864d6b61b556564ded7e663655907e7a45002ae9701c6fd15db449d889)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd49872a7bfb18cd3592b07a091ac874073eb53bf1cc6b7d36317df310d32f7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4acccef614d053e0c4f4b4b034a219a10aee478119f1843750bffb902bd2eed0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96935bf34406626022660fac316b3bb1f1dd0b765e2dc59e0fe85bffdf8dc7de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d23445bcb63526887e9bc7134f1aa20479a5c7970a88143fe492d86298e2aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df94fe0a5a9aa7d799601e707dea75103fb6614522f7d343922ca0438ca5c6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84d39346170594cf6e572f30b21727ef07d1544420569e1d7d481e410f1e4b75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edde2693920a73e92e376ea4609d423f03b1125c3e99538e6c7e0e39be2d59e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58aee245f9b80d4ab1ab90ce6d927d7e01d5697ee55b4fb0729b24ad5ba5edf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c2090b443d2804416d3936da8a5baafb79e30a236a277db5bb7ebdfb8d6bd7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a658e8e0bd880192d4db75d58918281bfb766780f0b2892ebc2401fae250d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressFromPodSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressFromPodSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__783dc45068e3d17d8b451b934ba3146ce6b70404de71f838fb38c3870547b056)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7466d90ee3c741384353d7cc321a59573cfefd985d316d0c0616a28294139f13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsList:
        return typing.cast(NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a076b9f03bb3cf2011d58ac2cc0c795169b35e32906b973ac04e03e9cd84064d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkPolicyV1SpecIngressFromPodSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecIngressFromPodSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecIngressFromPodSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47dd3ac05cca2ccd63dd0015f2934d00805cb324db7bf56a20b0f3b346d943a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5c59af62e9812b812f5817c926cdccccc8d51f52ee590eed28d57f54849378a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkPolicyV1SpecIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd2626839f8458f027ce30ef348a66dcdbf024dedb7adcce9b6a3a972a45cbd7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527825d00f62895e648c383eed7c662d303e967aae725a4487fdeef52c7c1950)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2ac93d00eda513d7c96347d8ea34892cc0a86e624a3879b1fcc0ad9e82334e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4719eb9f9b8a365a4f8c597619adc6ba66835d1efd5d8e742802d0d852246d3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1361eb87f68530ccc569a0a8c59ace577e156d3bbb2eae9d56466a4242412092)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a90a3f229e8e828a4ccef336691672225a88ab33b3d98523c39c4ca5039e1db0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFrom")
    def put_from(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFrom, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff80dd1cb97d15e21738072e3b9f07d398023bb2a171a6a718fb3d3162a59c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFrom", [value]))

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecIngressPorts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2e47d0c77662ae4af7b94a8490cce7630a01df5b9a204e1191286fcfe7a826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> NetworkPolicyV1SpecIngressFromList:
        return typing.cast(NetworkPolicyV1SpecIngressFromList, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "NetworkPolicyV1SpecIngressPortsList":
        return typing.cast("NetworkPolicyV1SpecIngressPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecIngressPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecIngress, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecIngress, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngress, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5117a82945eae468d0bf22f9c13d6d0b72bdd3374e2e301cc0b85a6dad63f482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressPorts",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class NetworkPolicyV1SpecIngressPorts:
    def __init__(
        self,
        *,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#port NetworkPolicyV1#port}
        :param protocol: The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#protocol NetworkPolicyV1#protocol}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8979415a5336b7e9b982a9e6ef599ee12d071160dec7f5edf2d07b1a9b38f8f)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''The port on the given protocol.

        This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#port NetworkPolicyV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#protocol NetworkPolicyV1#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecIngressPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecIngressPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressPortsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa3b7a04a02eb8bd5dfe5a5e73c27ba9d9e33a4282e75e80aeb7367c64c51bbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecIngressPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe2ed56a0e205da6d0288c44b6fe77190d7fb8671c8bae42531974bc8a85b6f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecIngressPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32652f9d8b3424d0a37896cab5cb670d87400e9d17b827f57db5d5a82e105fc0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6be764e18c6cba2d92cd822a0a8a13285ae3fe6e92d6bd9b40630aed3f73cd87)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ac5e48d99508ac137c384395932c37c059afabc6e2979375b108f24d9204f55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8bb5459823b948515f1310385f574ac2750411bc7b6edf8b33645b1c8c9a1c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecIngressPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecIngressPortsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc987e62bdb064fe2e4af21e073381d9c49ab88590ee1d6ccece03fd0133b40e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b8ee37fac7b157ddd432ccda9ef15478e8c238b702cb3fa71d8d3e24936f70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2dc5ca00ea25fb252147fa72edf96e497d639052f31aa19233b9cabcca25b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecIngressPorts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecIngressPorts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressPorts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d47d6e598f220351c5f2106ccc5257976be5a21744e613ba0c9875cca066f63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f44c2724524b520c27d08f2cd92cec799a6a5e968292306ed5780397fa1f3f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEgress")
    def put_egress(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgress, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ec9ee17a4e262974ef4a1811aebb7ef3e0c9c2421f11e00f1c28e208caa4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEgress", [value]))

    @jsii.member(jsii_name="putIngress")
    def put_ingress(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngress, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e3c68ffcc78ae767a98b4b1498e17addd35976974e231404f30732d7393b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIngress", [value]))

    @jsii.member(jsii_name="putPodSelector")
    def put_pod_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        value = NetworkPolicyV1SpecPodSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putPodSelector", [value]))

    @jsii.member(jsii_name="resetEgress")
    def reset_egress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgress", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @builtins.property
    @jsii.member(jsii_name="egress")
    def egress(self) -> NetworkPolicyV1SpecEgressList:
        return typing.cast(NetworkPolicyV1SpecEgressList, jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> NetworkPolicyV1SpecIngressList:
        return typing.cast(NetworkPolicyV1SpecIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="podSelector")
    def pod_selector(self) -> "NetworkPolicyV1SpecPodSelectorOutputReference":
        return typing.cast("NetworkPolicyV1SpecPodSelectorOutputReference", jsii.get(self, "podSelector"))

    @builtins.property
    @jsii.member(jsii_name="egressInput")
    def egress_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]], jsii.get(self, "egressInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="podSelectorInput")
    def pod_selector_input(self) -> typing.Optional["NetworkPolicyV1SpecPodSelector"]:
        return typing.cast(typing.Optional["NetworkPolicyV1SpecPodSelector"], jsii.get(self, "podSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypesInput")
    def policy_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policyTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypes")
    def policy_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policyTypes"))

    @policy_types.setter
    def policy_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fb2e0893b9dee6a404c0dabeec90bb59ae09347ca01465f26b520f091edd10c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1Spec]:
        return typing.cast(typing.Optional[NetworkPolicyV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkPolicyV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58f5917e0725236cc605a23e2741ebb5cf9212b66ab36558a12662d5fc82fc8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecPodSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class NetworkPolicyV1SpecPodSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkPolicyV1SpecPodSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430996a3ed9ce01809c792abf7b6e735041d6d35b91c8fa9ba8e9134ded404cd)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecPodSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_expressions NetworkPolicyV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkPolicyV1SpecPodSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#match_labels NetworkPolicyV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecPodSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecPodSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class NetworkPolicyV1SpecPodSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8846775cadd063011a75d016bc6dcd5ac8cecf004a9dbdf363138869db8bc8fb)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#key NetworkPolicyV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#operator NetworkPolicyV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/network_policy_v1#values NetworkPolicyV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPolicyV1SpecPodSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkPolicyV1SpecPodSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecPodSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8ec1ab55b45d3df2397ada8389ce2f1b92e22993cc6cbc7fd7e857b167d9d70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkPolicyV1SpecPodSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d2a20395a400e1fbae4396edb28901e5f7ca740246fdc656dd0784066e3a8d8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkPolicyV1SpecPodSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c0a518400c90589329283ed20f6459e801a32f45a387621c607e561e851de0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8f6ccc73e006f9016f32113340ae9b43536a0234eff041a3d3ec88db945016f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44eed26a08faacd24f5de9205b8869ff99c870455d9ec26ad27166eb4e14bfa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ae9ae7565b216a1252244675e01c42f78bc78725d99ce89a1fb90b87d7122b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecPodSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecPodSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57b6d42d1e2e6c7d2c8d54bd7450db5624a1023cb9bbf4900bc1d3b31670b4f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3ca784c0935f6e5e7b5a4af6b62ad31d696d7f4c3ec98fa806812a8d96bd34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e67a880a713d6cdaf3d4d837e7b4d3a49fedf01683e2deb4e524c7cdc60e2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6ff7e613b3a78757649027545ef66832123a49aab5ecb4a37f01cd518219aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a0747f993cf0658c825c1d9e95fd8fec2db456c64a0f0335e1566a073eb52e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkPolicyV1SpecPodSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.networkPolicyV1.NetworkPolicyV1SpecPodSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ffbdd7fa8a029987f26744c0d25371112df3cf9791e51694eb75048f01e872e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88398fe75d5b3eb66dee6d96ef008e520b769cb4807a0cfeffc6d80b98728931)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(self) -> NetworkPolicyV1SpecPodSelectorMatchExpressionsList:
        return typing.cast(NetworkPolicyV1SpecPodSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fb0992afba2f67c8e3698fba06b6e08904adbf8a7fb1157ba667def608cd08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkPolicyV1SpecPodSelector]:
        return typing.cast(typing.Optional[NetworkPolicyV1SpecPodSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkPolicyV1SpecPodSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01257b3b357f550237c875ffc307733c1560dd56c7ee40719c3d7e04b8b04b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkPolicyV1",
    "NetworkPolicyV1Config",
    "NetworkPolicyV1Metadata",
    "NetworkPolicyV1MetadataOutputReference",
    "NetworkPolicyV1Spec",
    "NetworkPolicyV1SpecEgress",
    "NetworkPolicyV1SpecEgressList",
    "NetworkPolicyV1SpecEgressOutputReference",
    "NetworkPolicyV1SpecEgressPorts",
    "NetworkPolicyV1SpecEgressPortsList",
    "NetworkPolicyV1SpecEgressPortsOutputReference",
    "NetworkPolicyV1SpecEgressTo",
    "NetworkPolicyV1SpecEgressToIpBlock",
    "NetworkPolicyV1SpecEgressToIpBlockOutputReference",
    "NetworkPolicyV1SpecEgressToList",
    "NetworkPolicyV1SpecEgressToNamespaceSelector",
    "NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions",
    "NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsList",
    "NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressionsOutputReference",
    "NetworkPolicyV1SpecEgressToNamespaceSelectorOutputReference",
    "NetworkPolicyV1SpecEgressToOutputReference",
    "NetworkPolicyV1SpecEgressToPodSelector",
    "NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions",
    "NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsList",
    "NetworkPolicyV1SpecEgressToPodSelectorMatchExpressionsOutputReference",
    "NetworkPolicyV1SpecEgressToPodSelectorOutputReference",
    "NetworkPolicyV1SpecIngress",
    "NetworkPolicyV1SpecIngressFrom",
    "NetworkPolicyV1SpecIngressFromIpBlock",
    "NetworkPolicyV1SpecIngressFromIpBlockOutputReference",
    "NetworkPolicyV1SpecIngressFromList",
    "NetworkPolicyV1SpecIngressFromNamespaceSelector",
    "NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions",
    "NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsList",
    "NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressionsOutputReference",
    "NetworkPolicyV1SpecIngressFromNamespaceSelectorOutputReference",
    "NetworkPolicyV1SpecIngressFromOutputReference",
    "NetworkPolicyV1SpecIngressFromPodSelector",
    "NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions",
    "NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsList",
    "NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressionsOutputReference",
    "NetworkPolicyV1SpecIngressFromPodSelectorOutputReference",
    "NetworkPolicyV1SpecIngressList",
    "NetworkPolicyV1SpecIngressOutputReference",
    "NetworkPolicyV1SpecIngressPorts",
    "NetworkPolicyV1SpecIngressPortsList",
    "NetworkPolicyV1SpecIngressPortsOutputReference",
    "NetworkPolicyV1SpecOutputReference",
    "NetworkPolicyV1SpecPodSelector",
    "NetworkPolicyV1SpecPodSelectorMatchExpressions",
    "NetworkPolicyV1SpecPodSelectorMatchExpressionsList",
    "NetworkPolicyV1SpecPodSelectorMatchExpressionsOutputReference",
    "NetworkPolicyV1SpecPodSelectorOutputReference",
]

publication.publish()

def _typecheckingstub__17b7b86e54ae53d35fdfae40080196fe5a92f59490992e842294b2dd60944889(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[NetworkPolicyV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[NetworkPolicyV1Spec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__9b2303d0a4bb3134565d46eced1374406f23ed6ee377611f5b70f4ca76dd3439(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f39d84ebee8210cecb79db63d90da2ff790eba0177d152447a865571b5bbacc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[NetworkPolicyV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[NetworkPolicyV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dbd7932168ed8b6c476b3e7c63d26cd8bb2f1c46d5301fc5088cc5d21e01d64(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e3449a3b6e3b8fefca683f9846457adcf023d3839154410ff5e5535dc77b7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e317c65d6ae508c52252ec76895e104af1dd05c16d52a5aae0de6283808fced4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d21cbcca7706c3c212a0fcc34bc9f95850763f99602c7284eca747ed74b7f1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d60c7b116b18c5dc9afd11d9cf4b8207301c99061de8c94d45ea506831cbaa(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e5ecc406facd61a58bec22b95dc1e98d6a9bd48d79eb334437101a2384ca26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0b748e4e10631b87c3eacf649e8df9dc702657eafcef42df6b303859197484(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baba8a679141c3fc86d3501a67e818f0ff331d02176150094d3c01e05d359108(
    value: typing.Optional[NetworkPolicyV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29223fb2544a7988e76e7d1576e8b1d7498fac8d2c86c8d6604d3078ddc4faab(
    *,
    pod_selector: typing.Union[NetworkPolicyV1SpecPodSelector, typing.Dict[builtins.str, typing.Any]],
    policy_types: typing.Sequence[builtins.str],
    egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgress, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngress, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0af20920ad9effe66406c4506e3419cfadfd30aaba5d4dc63f2e76672cef9b10(
    *,
    ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    to: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressTo, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e6364dd05f4f9ec69f6fff543d7b8c3875f7973c3b01036167361014167595(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878d4f6ff5777f92e6fc82d1cd2fd9daf01704625cb8114a358091db9d9f86f4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf424889457b9bc1d0adde4e0bf9de80da072bff211589a36f5a90a475a7580(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2078dcd09dfbd11f3bb15cbf686225e3b9dabdd7bd44b5205ae26e26431a6f2e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d752c7b04c37feb3a1824330efd030a5d8c17d493dfb8d67e1bc263d033726(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf15caecd59ec69576d1757f6270e2067a4a108e690d6caf4b9135f64239d73(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgress]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79a169a023bc3def522aee37f55058bf6b289f56e97ccbd511a7d2d3b650c73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96bd8fcef166718003c41bc788258b97e7fe28403f7cd1e0f1eb754d5c5c671a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e169a56f5c5fb0a9c882f5654806fa83a7526b60b1e77fe7b851fc3e47409517(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressTo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485277436e087e10005914ae0043920c6b2ef6a33b978f77697d75f93bca6260(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgress, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb44922464edfdbea4937d1b68e6bb30db7e287f3be682ec3b71e2355c879ff4(
    *,
    port: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad63e230c998473005cdda986ec4880ed0dc181fe30434c1a4f9fbd5a69b33f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed3c18618855339e98d2efe659eb7f2f79c5643a9ca25d8b1c7e3acca564280(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c053522a755f7b1df4dcd4ad33565d8a196ee2c3ed277c483b6b1fb0e828193f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521839b2f983866fc524a0222ec29bb8478efd00b6062f9dcd7ad263ec62df02(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b346c292bef0b4f22f3b8da4cd8c67f8bef7bae506d747671d2f9843e9d095be(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6dc0419b7ce91f885dc71ff05fe725b9e592d65ffca703abf81cd87591a4168(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045c726cfe31ecf45e3b25aa27ef63671c8bd2df68ee0f9519c086c49729c774(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d6ad25b174f2ba7ffe94563b284c746f53b0c4c5585ef54edbeee39f158bb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2a12173be7e2e7bac05aefdb7cc423bbfc8855072f62431379effbdd1de4cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d535361c34ec6c3d3c58e0dd3ce8872444026c2728f8d52cb54d73f46b3f0f(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressPorts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33896808258e17a78ff1961a3180b922b10ba5a61e62cdaee2ae33bc09b3324f(
    *,
    ip_block: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToIpBlock, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace_selector: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_selector: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToPodSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd0c381d05638efd170ab88eacafaf71ab04a06c760f42f5110574965bc84ad(
    *,
    cidr: typing.Optional[builtins.str] = None,
    except_: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0bc7d56fb8655270de53c8363b94354f16e77e99b46ed2e9e29704aa618f273(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd87bd4b81eae047790a81fff8207483b2f85af40dd0faac610e50722511f12f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d13b080e3828731d407c89bffcf3b09ac62c2bf4c8161c2e4ab7d17678eca4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9b2c8c1cbeb16c8dfd7503c02b652448569f6097b3f7d81d08522193429e09(
    value: typing.Optional[NetworkPolicyV1SpecEgressToIpBlock],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1501d61756887c6e4df1793f261bee21f2987db75dba1a32f0caf20c1166719f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d430fccb81872a2a6c02a850c51bddbbe190f5402c8ca1bb4e10206bce8fa38b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e747b67d0a83b125b6183bfb23fddf4738dc4da41fa7d6290e5f4c3abd8982da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6431580bbe6bd646cfaa0efb219a7d2f830e9c2213d8840fcfacc4c01a346fc3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc478e88f2d86c53e139bbb3d1ce25a1e8e521644ce0fa6ff00ed073a0570ee2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e95f19ca5482600755b1a6f14f546f9d7a0263e2fa9aa50c08ff88bea424ac(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressTo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46224dafa402025c8bd584cef3af3e69184fb63f1b4acf16f4a4021d545da01a(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef0f920abd5d300cd269c5ce12c7f5b13e08e5106ee72703a587848b6ffab05(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384a004a613b58257a5ef20609b9ce3530a566dc825cf805d303034efb79d27d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481ead2bc8318d1fe08a9ea8d762e200c64a3ef06d8a4c1645c746b696c2f22a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecfe6439dcad01031389aaeb110969502e16fc30a0e1416e49cb114f428dd2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0064403e2ab901ab4b2df85a77465decc3a5981f33bafd341c8d6463325331f9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ce12ecb55b160df58d414274c6cd09f601682344b3526d369d6600ae759c5a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af4df2dfa51db8e459af9d444403095d2a5d1c78c1eaaa2ecf86d345ea5d4857(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a63cccde366ff68a5fdf17dd6d1c782573e6e22ddd315ab07840b46f96fe6ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc2c2fed806267976019a9bddb7a9441773f57d859043d17a27c9a28c00924f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f84cd4624799231a88e3f8ecba5e058d39edc0aaf10477c7a1056a55ae8b7905(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c260a386875145ad353490d6a52eb618b5ea005696d03a30ccc7113588e44cb0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cccb6e2e6474d8043a93aa69446f50197c36c1cb2ec91b76cb971eae7736c1f7(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b2447005d16bbd9f96edefe948983b6266c5d9968e93dba3aeebbcec3d068eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a97c89b6eb397e6554791499002803d591913726d51732c79f4301b466fe68(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f612d83ab6c08a9bbf76806bfbab78a9244c11950f4137ee3cd415ae17a1e30(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f6d865437d95f37973c39312bd15602451477434bda8cb5473c473c97c9a2f(
    value: typing.Optional[NetworkPolicyV1SpecEgressToNamespaceSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1dd682ba4989b8d835ac1daa4b1ffef594d1a530b44910575c3830afb1930b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f87049f066c57f65d058283b699c03fbcf881e872e1b0197e6bafea5c97450ca(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressTo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97aae9f32f785ae89f2fd92709ad034d6736cf8769d3779f37bede980d1d7982(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960c00ce6264ce404ff93cee04b985fe75ed3b730fdfb3263943788afbc9381c(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee203134c1848e6986e543c5dd36237de488e61909a4d0925cde8612ecceefa6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7350daa58d818acd608a70850af008f7b4ee9504dd34987bfcdfa26709ef4c22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad71dd0a95e6937bd48092e18b785b78896dff14cd3a5db00a9bd255a800e27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0794ffb7b0cddfbf37885dbfb6fcb39a7ef57f9e4ad1b0c48c16238a25351509(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9abeabc57be6244de846b62a5cb94596410b4c0c03082357581eb56ed33ce1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174725a32b0b6cd16320b903019934af79c4bbe1371c70e9114135cfb93e8b92(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94588a001d50fef9fd207299d917fc4ce008f42f891141789c29a28f6697f0e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536d7e1a50629f41b9a4adf5610f06164171627dcb4e22f1496291c263d437f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95244a386dd02467abdf01161dfcf33ea79774bf3e1711ddd519504e79cfa322(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f0f9e29101579c7d84bc35174493eb2b763a4315390bf10f8d06b7449beb0c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625827e6acce481bfa7da4156af8c2d2389f8549ed75f6745f48142a3939c19e(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0804bf3ec041c35e9e1b1d0f63cb3795665dd8e5a8ed9b62e629f8bf436dcccd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe913db8f9cce33410ef1a961133e9356bfac4c28fef2892abad88e85dcf130(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgressToPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c86383d7314c5f1131fc77b0699dd4d392c330e52564326c7bafae8677dabf9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed9ac3ed3addcde8fa648291d27976d5b5fc3d4200c0ad95cc896812489ff05(
    value: typing.Optional[NetworkPolicyV1SpecEgressToPodSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50edd96f967af9de07cfcc1f5ceb575f69bab759b36101a6f796fc034a6cd8b9(
    *,
    from_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFrom, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3ac358d5681d3d0250f2a2413d170a2b1c684bdde04a6a342ac5f8839e7aa0(
    *,
    ip_block: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromIpBlock, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace_selector: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    pod_selector: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromPodSelector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7f39010bc2c4af44f386380f07179a66ba71feb59c4653a6fc504078fd4f5b(
    *,
    cidr: typing.Optional[builtins.str] = None,
    except_: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa75c559d99b09358c74fb31e3ad929a30927b186a06627b432146887224f75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11dfd603d28e5bce63620093b97ea0a4ea4044be6d5b8c99f9fb67a38eae7ab4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d1522ff3fbe86721473f160a356b05bec59b62692741895d9fadd5219ceda7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7679c736e69d4c5f55009fda8298d49741221d4302ec829bb1ae2200b4edf0(
    value: typing.Optional[NetworkPolicyV1SpecIngressFromIpBlock],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389fc6fbcc9d28a45f0086392567c2405b9d6e1c42fba32b15dd312281d6827e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdc023da3a86937f307ae5756d9e0e2167fd38547fa018372b2fd5ade4f4a50b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d8b8a609d989d09009a3dd760b2dd40fda993edf99865a954f05b1df57032c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f2de7a95e6c267e95167aa0b6b5d2a106c04afb4578fac5e65b863c7891647(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7be04a87ecf2eaa5b6d7b8692b438f6452684af248bcdb194d513e22ed15868(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3179b867d78c06adfa05e6f93b27109e80affdd722e0eec051a5333540009a28(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFrom]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f912c554476427886bdfa002515e66720f0473d340467929cb210b3ec7e9022b(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb7acaa26abbefab2713444dc157cc3480fc6e3a0c7605fd658a81a53d09b53(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fac96aa2ef338f6c5ac09d34f7a7a94d349f46929b3b7a9148f2929f446f856(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7739f42c0411846d6aa5d550f4b93500a99db6a34d2b4a751af7205959f7faf6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6eed9a2d5524c6aa232355142b4527f3a029f40d977615318b802d403be6ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46527ac3a5eb43ada249a199c9d986c620da27521babedcebb63c8f78bd9cad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89324153501243b4017f15c1ff32c4c11c2ef48fa6cfb5bd69dc5bee47c63f1a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1549662ed020ad548d3a6675786f701e803d9bf4f86f2ecda46e81fd7b5b8ac6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b697eb22919f6c224cc53488b5adf9ba7d1616c967eb59cf04fee2d171b96e4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105a4e274261595631507501772acbada864351c7fcfb2c68f7365c3f2088f79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e01ecf020427b46d440e51ab7f32657b40a99daff0b324dbb4ac8d72756422(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0094fc700b6dac5871474a8f6bade01bb261d599c217415b4049cca39e8555e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571f9e3753947c69336bf8248f1f4cb97bc547d50ddd611d14ef0300e713dd79(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab728f3b7c0d5382d8e0a1da7b15657b6878acc52b9e4d5c55fb660707d0b75b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c1b480717e98f1840335d9a1bba08e6192b3e56d24f32cb32631c0c650f94c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673e380cd61368c857f1b89130ae794edec510e1d7cd37de2d58047692b7b82a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25bb7825800168a437e822ee289cd184f5cd70ada2a19c96e64627409da0ef13(
    value: typing.Optional[NetworkPolicyV1SpecIngressFromNamespaceSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f27558403e3ec11322d2e51308bed0fe6692a4f0fdafdce67b89a4a5859316(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8abdb3d63c3f295537782c7b2be852d11a5674f5d6ca27de37df14dd290366(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFrom, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8646ba3cb0d995a5faf3971e79eca281ea33e1d1d3426e8672ee915cf242c4f7(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b30be4504b05b763e09cd67436505017b287da978720c8d2a710e6b72b61c2(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed470864d6b61b556564ded7e663655907e7a45002ae9701c6fd15db449d889(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd49872a7bfb18cd3592b07a091ac874073eb53bf1cc6b7d36317df310d32f7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acccef614d053e0c4f4b4b034a219a10aee478119f1843750bffb902bd2eed0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96935bf34406626022660fac316b3bb1f1dd0b765e2dc59e0fe85bffdf8dc7de(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d23445bcb63526887e9bc7134f1aa20479a5c7970a88143fe492d86298e2aff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df94fe0a5a9aa7d799601e707dea75103fb6614522f7d343922ca0438ca5c6a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d39346170594cf6e572f30b21727ef07d1544420569e1d7d481e410f1e4b75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edde2693920a73e92e376ea4609d423f03b1125c3e99538e6c7e0e39be2d59e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58aee245f9b80d4ab1ab90ce6d927d7e01d5697ee55b4fb0729b24ad5ba5edf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2090b443d2804416d3936da8a5baafb79e30a236a277db5bb7ebdfb8d6bd7e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a658e8e0bd880192d4db75d58918281bfb766780f0b2892ebc2401fae250d11(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783dc45068e3d17d8b451b934ba3146ce6b70404de71f838fb38c3870547b056(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7466d90ee3c741384353d7cc321a59573cfefd985d316d0c0616a28294139f13(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFromPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a076b9f03bb3cf2011d58ac2cc0c795169b35e32906b973ac04e03e9cd84064d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47dd3ac05cca2ccd63dd0015f2934d00805cb324db7bf56a20b0f3b346d943a4(
    value: typing.Optional[NetworkPolicyV1SpecIngressFromPodSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c59af62e9812b812f5817c926cdccccc8d51f52ee590eed28d57f54849378a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd2626839f8458f027ce30ef348a66dcdbf024dedb7adcce9b6a3a972a45cbd7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527825d00f62895e648c383eed7c662d303e967aae725a4487fdeef52c7c1950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ac93d00eda513d7c96347d8ea34892cc0a86e624a3879b1fcc0ad9e82334e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4719eb9f9b8a365a4f8c597619adc6ba66835d1efd5d8e742802d0d852246d3b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1361eb87f68530ccc569a0a8c59ace577e156d3bbb2eae9d56466a4242412092(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngress]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90a3f229e8e828a4ccef336691672225a88ab33b3d98523c39c4ca5039e1db0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff80dd1cb97d15e21738072e3b9f07d398023bb2a171a6a718fb3d3162a59c4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressFrom, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2e47d0c77662ae4af7b94a8490cce7630a01df5b9a204e1191286fcfe7a826(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngressPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5117a82945eae468d0bf22f9c13d6d0b72bdd3374e2e301cc0b85a6dad63f482(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngress, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8979415a5336b7e9b982a9e6ef599ee12d071160dec7f5edf2d07b1a9b38f8f(
    *,
    port: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3b7a04a02eb8bd5dfe5a5e73c27ba9d9e33a4282e75e80aeb7367c64c51bbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe2ed56a0e205da6d0288c44b6fe77190d7fb8671c8bae42531974bc8a85b6f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32652f9d8b3424d0a37896cab5cb670d87400e9d17b827f57db5d5a82e105fc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be764e18c6cba2d92cd822a0a8a13285ae3fe6e92d6bd9b40630aed3f73cd87(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac5e48d99508ac137c384395932c37c059afabc6e2979375b108f24d9204f55(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bb5459823b948515f1310385f574ac2750411bc7b6edf8b33645b1c8c9a1c5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecIngressPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc987e62bdb064fe2e4af21e073381d9c49ab88590ee1d6ccece03fd0133b40e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b8ee37fac7b157ddd432ccda9ef15478e8c238b702cb3fa71d8d3e24936f70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2dc5ca00ea25fb252147fa72edf96e497d639052f31aa19233b9cabcca25b47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d47d6e598f220351c5f2106ccc5257976be5a21744e613ba0c9875cca066f63(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecIngressPorts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f44c2724524b520c27d08f2cd92cec799a6a5e968292306ed5780397fa1f3f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ec9ee17a4e262974ef4a1811aebb7ef3e0c9c2421f11e00f1c28e208caa4be(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecEgress, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e3c68ffcc78ae767a98b4b1498e17addd35976974e231404f30732d7393b34(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecIngress, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fb2e0893b9dee6a404c0dabeec90bb59ae09347ca01465f26b520f091edd10c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58f5917e0725236cc605a23e2741ebb5cf9212b66ab36558a12662d5fc82fc8b(
    value: typing.Optional[NetworkPolicyV1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430996a3ed9ce01809c792abf7b6e735041d6d35b91c8fa9ba8e9134ded404cd(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8846775cadd063011a75d016bc6dcd5ac8cecf004a9dbdf363138869db8bc8fb(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ec1ab55b45d3df2397ada8389ce2f1b92e22993cc6cbc7fd7e857b167d9d70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d2a20395a400e1fbae4396edb28901e5f7ca740246fdc656dd0784066e3a8d8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c0a518400c90589329283ed20f6459e801a32f45a387621c607e561e851de0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f6ccc73e006f9016f32113340ae9b43536a0234eff041a3d3ec88db945016f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44eed26a08faacd24f5de9205b8869ff99c870455d9ec26ad27166eb4e14bfa7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ae9ae7565b216a1252244675e01c42f78bc78725d99ce89a1fb90b87d7122b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkPolicyV1SpecPodSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b6d42d1e2e6c7d2c8d54bd7450db5624a1023cb9bbf4900bc1d3b31670b4f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3ca784c0935f6e5e7b5a4af6b62ad31d696d7f4c3ec98fa806812a8d96bd34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e67a880a713d6cdaf3d4d837e7b4d3a49fedf01683e2deb4e524c7cdc60e2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6ff7e613b3a78757649027545ef66832123a49aab5ecb4a37f01cd518219aa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a0747f993cf0658c825c1d9e95fd8fec2db456c64a0f0335e1566a073eb52e(
    value: typing.Optional[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ffbdd7fa8a029987f26744c0d25371112df3cf9791e51694eb75048f01e872e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88398fe75d5b3eb66dee6d96ef008e520b769cb4807a0cfeffc6d80b98728931(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkPolicyV1SpecPodSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fb0992afba2f67c8e3698fba06b6e08904adbf8a7fb1157ba667def608cd08(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01257b3b357f550237c875ffc307733c1560dd56c7ee40719c3d7e04b8b04b4(
    value: typing.Optional[NetworkPolicyV1SpecPodSelector],
) -> None:
    """Type checking stubs"""
    pass
