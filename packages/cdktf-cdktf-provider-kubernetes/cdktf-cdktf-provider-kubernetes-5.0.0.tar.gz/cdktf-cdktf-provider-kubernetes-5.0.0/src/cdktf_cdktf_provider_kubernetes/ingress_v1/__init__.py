'''
# `kubernetes_ingress_v1`

Refer to the Terraform Registory for docs: [`kubernetes_ingress_v1`](https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1).
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


class IngressV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1 kubernetes_ingress_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["IngressV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1 kubernetes_ingress_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c906024ebb2917b40aa4b415615e01f82dfe593b0fb2fb9bd04170155a63e24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IngressV1Config(
            metadata=metadata,
            spec=spec,
            id=id,
            wait_for_load_balancer=wait_for_load_balancer,
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        value = IngressV1Metadata(
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
        default_backend: typing.Optional[typing.Union["IngressV1SpecDefaultBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_backend: default_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        value = IngressV1Spec(
            default_backend=default_backend,
            ingress_class_name=ingress_class_name,
            rule=rule,
            tls=tls,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetWaitForLoadBalancer")
    def reset_wait_for_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForLoadBalancer", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "IngressV1MetadataOutputReference":
        return typing.cast("IngressV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "IngressV1SpecOutputReference":
        return typing.cast("IngressV1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "IngressV1StatusList":
        return typing.cast("IngressV1StatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["IngressV1Metadata"]:
        return typing.cast(typing.Optional["IngressV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["IngressV1Spec"]:
        return typing.cast(typing.Optional["IngressV1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForLoadBalancerInput")
    def wait_for_load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForLoadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c38d3556ec643facfb08bd45f8a5010eef2402a7bbfae7c20ce6d2ae4fe9406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="waitForLoadBalancer")
    def wait_for_load_balancer(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForLoadBalancer"))

    @wait_for_load_balancer.setter
    def wait_for_load_balancer(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18e589a552b007274dc1be966db9ea1a5a61099700dfcdcaaefea90f95d3537c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLoadBalancer", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1Config",
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
        "wait_for_load_balancer": "waitForLoadBalancer",
    },
)
class IngressV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["IngressV1Metadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressV1Spec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = IngressV1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = IngressV1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf63d53e98f6209c118910104409793a0f869e7eb79464ba34555d69c4f2412a)
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
            check_type(argname="argument wait_for_load_balancer", value=wait_for_load_balancer, expected_type=type_hints["wait_for_load_balancer"])
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
        if wait_for_load_balancer is not None:
            self._values["wait_for_load_balancer"] = wait_for_load_balancer

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
    def metadata(self) -> "IngressV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#metadata IngressV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("IngressV1Metadata", result)

    @builtins.property
    def spec(self) -> "IngressV1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#spec IngressV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("IngressV1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#id IngressV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_load_balancer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#wait_for_load_balancer IngressV1#wait_for_load_balancer}
        '''
        result = self._values.get("wait_for_load_balancer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class IngressV1Metadata:
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc98afd4bc3156d01361dc929cc5a7a73a825754b39a76da76fa788a21d9e83)
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
        '''An unstructured key value map stored with the ingress that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#annotations IngressV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#generate_name IngressV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the ingress.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#labels IngressV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the ingress must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#namespace IngressV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c89b7f06e8bbfa73d95b207b61b802c869e985045f1b2cd52f5f8a5a57b58dc5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__363d5d09211b9c504b5646e2958205a6517707e367bc68f7305289dff69daad4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871a4a76d11535f748649ac20d97b115db8737760cc87c0ea932bd9814f06577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e678690cd1e1703c49aa8ded17e5cbf3bf248ddc438465ff96477607678cb627)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35020cc2235fe398a8033b6e664fdf78feca1e47c775f0abdfd664c00388346f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adecf7f34fe3aa1251c67fd84b404aae95a9f7e8b9394a99707efc5596eaef63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Metadata]:
        return typing.cast(typing.Optional[IngressV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa9c31fc6e3183426016ae58660377e947d810b1d9b2faf65c21f37ff63bd8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "default_backend": "defaultBackend",
        "ingress_class_name": "ingressClassName",
        "rule": "rule",
        "tls": "tls",
    },
)
class IngressV1Spec:
    def __init__(
        self,
        *,
        default_backend: typing.Optional[typing.Union["IngressV1SpecDefaultBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default_backend: default_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        if isinstance(default_backend, dict):
            default_backend = IngressV1SpecDefaultBackend(**default_backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f135a737d6b6269cc4bad1c464aabb55630f8ed90fcb3beeb413a6bae5c7d44b)
            check_type(argname="argument default_backend", value=default_backend, expected_type=type_hints["default_backend"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_backend is not None:
            self._values["default_backend"] = default_backend
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if rule is not None:
            self._values["rule"] = rule
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def default_backend(self) -> typing.Optional["IngressV1SpecDefaultBackend"]:
        '''default_backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#default_backend IngressV1#default_backend}
        '''
        result = self._values.get("default_backend")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackend"], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''IngressClassName is the name of the IngressClass cluster resource.

        The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#ingress_class_name IngressV1#ingress_class_name}
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#rule IngressV1#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#tls IngressV1#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackend",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "service": "service"},
)
class IngressV1SpecDefaultBackend:
    def __init__(
        self,
        *,
        resource: typing.Optional[typing.Union["IngressV1SpecDefaultBackendResource", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["IngressV1SpecDefaultBackendService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        if isinstance(resource, dict):
            resource = IngressV1SpecDefaultBackendResource(**resource)
        if isinstance(service, dict):
            service = IngressV1SpecDefaultBackendService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8d246346bee7a8d927238cfc191b9c751f7403151f5933a5f657127dfc8f58)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource is not None:
            self._values["resource"] = resource
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def resource(self) -> typing.Optional["IngressV1SpecDefaultBackendResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendResource"], result)

    @builtins.property
    def service(self) -> typing.Optional["IngressV1SpecDefaultBackendService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35e93f1123f82b9d1445387cac5645ee06cd6adeb3a00a2b02e9c95688381526)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        value = IngressV1SpecDefaultBackendResource(
            api_group=api_group, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecDefaultBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        value = IngressV1SpecDefaultBackendService(name=name, port=port)

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> "IngressV1SpecDefaultBackendResourceOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "IngressV1SpecDefaultBackendServiceOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional["IngressV1SpecDefaultBackendResource"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional["IngressV1SpecDefaultBackendService"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackend]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5f8c560b1dc8337e45a443e736bce48bff61a8888ac14c5e2912c695803b71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendResource",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class IngressV1SpecDefaultBackendResource:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186ab9d837f46b0dfd676cf18f5734040dc21755721743da9551c8b2cfaeddcf)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_group": api_group,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''APIGroup is the group for the resource being referenced.

        If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7eed59ed7313e9c64884d0dc4b427c302014862dd6c282ffcde11504cefbf78b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0c9607dbe28a42c4b3af13c498b6266f9da9ab38c967ed2c2e6067df8a6416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1caff48385507b21b8971ba316644494d18747c99f1ca6439fcf61a27cb7c018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f11d64104b4bff4bd50af019aa6e5bd6d3a5fe7d1ff36bdff8b0f856deeec25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendResource]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f93a1c8ceb3d300efb9ea6523be36d8855f0ec492853630c15dcecc19c16d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "port": "port"},
)
class IngressV1SpecDefaultBackendService:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecDefaultBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        if isinstance(port, dict):
            port = IngressV1SpecDefaultBackendServicePort(**port)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5418fdbc4702da4008a9eeddb18ce9d19e527f09567f19aeaacb28b7cc4bb73b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> "IngressV1SpecDefaultBackendServicePort":
        '''port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast("IngressV1SpecDefaultBackendServicePort", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c84f2ec3458317ffac9660907f83d16a26c16badf155326ded672d1d795f838)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        value = IngressV1SpecDefaultBackendServicePort(name=name, number=number)

        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "IngressV1SpecDefaultBackendServicePortOutputReference":
        return typing.cast("IngressV1SpecDefaultBackendServicePortOutputReference", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional["IngressV1SpecDefaultBackendServicePort"]:
        return typing.cast(typing.Optional["IngressV1SpecDefaultBackendServicePort"], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b23dd6a7dcdc02f7ab0f6da9123bda8702170cc8937bcfd6bbca000d172f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendService]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__505efffc431df1c9c9cfc450b53e3d2bcabe5f5055c9232088ffb5c697fef06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendServicePort",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "number": "number"},
)
class IngressV1SpecDefaultBackendServicePort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99d732cf89605de87bc88e4499bea6367e652c8fbba0b97a9ebdb388e8bf26d7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''Specifies the numerical port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecDefaultBackendServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecDefaultBackendServicePortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecDefaultBackendServicePortOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18cdfd02dd8b4588e107a9e3013f668302cf17ecf8245ab9a128c5359595066b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae0d7c42c0db876196b4f9c1aed3c432d2cb6ec27463605a5cff08094c33ed1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "number"))

    @number.setter
    def number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3219bd18b34f7b3470b9e8cd64407702ec6cb1ea06e6558c171968f3eaf1f60f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecDefaultBackendServicePort]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackendServicePort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecDefaultBackendServicePort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ef19c8cc2ba61f57563fffac23ca68e5e9d3b82cc15b836a33488e1f266767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7eac9a4a9df131d0864032f0f7796d397234e32854749ddd0d808d2983b6d12a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultBackend")
    def put_default_backend(
        self,
        *,
        resource: typing.Optional[typing.Union[IngressV1SpecDefaultBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[IngressV1SpecDefaultBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        value = IngressV1SpecDefaultBackend(resource=resource, service=service)

        return typing.cast(None, jsii.invoke(self, "putDefaultBackend", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3569eca26641df64c2f282b7db1def5a58cb4a02becda38125c22d59f2e40012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecTls", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02ce6e879cbe1e017a8f8d37addfb0380a1f435bcf977eff24cdc8d46a477018)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetDefaultBackend")
    def reset_default_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBackend", []))

    @jsii.member(jsii_name="resetIngressClassName")
    def reset_ingress_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressClassName", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="defaultBackend")
    def default_backend(self) -> IngressV1SpecDefaultBackendOutputReference:
        return typing.cast(IngressV1SpecDefaultBackendOutputReference, jsii.get(self, "defaultBackend"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "IngressV1SpecRuleList":
        return typing.cast("IngressV1SpecRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "IngressV1SpecTlsList":
        return typing.cast("IngressV1SpecTlsList", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="defaultBackendInput")
    def default_backend_input(self) -> typing.Optional[IngressV1SpecDefaultBackend]:
        return typing.cast(typing.Optional[IngressV1SpecDefaultBackend], jsii.get(self, "defaultBackendInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassNameInput")
    def ingress_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingressClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecTls"]]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassName")
    def ingress_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingressClassName"))

    @ingress_class_name.setter
    def ingress_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07696d4f2fe41441d9c919551ec6b4933edcc7a2ba51a9cb1aee81c217f64883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressClassName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Spec]:
        return typing.cast(typing.Optional[IngressV1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Spec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43333428ac69830ce13d9454f9029d17020625b12c1ac5fefd0c70a5565e9ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRule",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "http": "http"},
)
class IngressV1SpecRule:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        http: typing.Optional[typing.Union["IngressV1SpecRuleHttp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue. Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#host IngressV1#host}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#http IngressV1#http}
        '''
        if isinstance(http, dict):
            http = IngressV1SpecRuleHttp(**http)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__161adce870403a7dfee95ba04fd0daaa515c870443b196bb151dc096773775bf)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if http is not None:
            self._values["http"] = http

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host is the fully qualified domain name of a network host, as defined by RFC 3986.

        Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to
        the IP in the Spec of the parent Ingress.
        2. The ``:`` delimiter is not respected because ports are not allowed.
        Currently the port of an Ingress is implicitly :80 for http and
        :443 for https.
        Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.

        Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#host IngressV1#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http(self) -> typing.Optional["IngressV1SpecRuleHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#http IngressV1#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttp",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class IngressV1SpecRuleHttp:
    def __init__(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5403d0999a4f97b23974b2a5e46d63d3027335852b76c915edfa036e747c52e0)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11eeadd7c9ba973c8fbddc46e45f234e304ea2c45a3f3bcf3307c7c83609f2d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressV1SpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322a9278fbeda1e205ff002508092eb7955ab39470242ea6d9b14c53e5587fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "IngressV1SpecRuleHttpPathList":
        return typing.cast("IngressV1SpecRuleHttpPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressV1SpecRuleHttpPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecRuleHttp]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1SpecRuleHttp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d4023f941ec08ebe0c364c2a95ca182613f0dd40cd0ac483cdb43f4da93982)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPath",
    jsii_struct_bases=[],
    name_mapping={"backend": "backend", "path": "path", "path_type": "pathType"},
)
class IngressV1SpecRuleHttpPath:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        path_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#backend IngressV1#backend}
        :param path: Path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        :param path_type: PathType determines the interpretation of the Path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is done on a path element by element basis. A path element refers is the list of labels in the path split by the '/' separator. A request is a match for path p if every p is an element-wise prefix of p of the request path. Note that if the last element of the path is a substring of the last element in request path, it is not a match (e.g. /foo/bar matches /foo/bar/baz, but does not match /foo/barbaz). ImplementationSpecific: Interpretation of the Path matching is up to the IngressClass. Implementations can treat this as a separate PathType or treat it identically to Prefix or Exact path types. Implementations are required to support all path types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path_type IngressV1#path_type}
        '''
        if isinstance(backend, dict):
            backend = IngressV1SpecRuleHttpPathBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318858710f2074f6663608b99ea18ec593f47c41c694cc0c2f4b78e305955d25)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument path_type", value=path_type, expected_type=type_hints["path_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if path is not None:
            self._values["path"] = path
        if path_type is not None:
            self._values["path_type"] = path_type

    @builtins.property
    def backend(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#backend IngressV1#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackend"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is matched against the path of an incoming request.

        Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_type(self) -> typing.Optional[builtins.str]:
        '''PathType determines the interpretation of the Path matching.

        PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is
        done on a path element by element basis. A path element refers is the
        list of labels in the path split by the '/' separator. A request is a
        match for path p if every p is an element-wise prefix of p of the
        request path. Note that if the last element of the path is a substring
        of the last element in request path, it is not a match (e.g. /foo/bar
        matches /foo/bar/baz, but does not match /foo/barbaz).
        ImplementationSpecific: Interpretation of the Path matching is up to
        the IngressClass. Implementations can treat this as a separate PathType
        or treat it identically to Prefix or Exact path types.
        Implementations are required to support all path types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path_type IngressV1#path_type}
        '''
        result = self._values.get("path_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackend",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "service": "service"},
)
class IngressV1SpecRuleHttpPathBackend:
    def __init__(
        self,
        *,
        resource: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackendResource", typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union["IngressV1SpecRuleHttpPathBackendService", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        if isinstance(resource, dict):
            resource = IngressV1SpecRuleHttpPathBackendResource(**resource)
        if isinstance(service, dict):
            service = IngressV1SpecRuleHttpPathBackendService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15de79e1524fa215bee3f4959cfcfe62412143c53a7ccac16a9e2ace8fc1fd0d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource is not None:
            self._values["resource"] = resource
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def resource(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackendResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendResource"], result)

    @builtins.property
    def service(self) -> typing.Optional["IngressV1SpecRuleHttpPathBackendService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendService"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__912745f5feb88ae395aef6fc362bb7f822fa155136e6c36d0b9e047286df7629)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        value = IngressV1SpecRuleHttpPathBackendResource(
            api_group=api_group, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecRuleHttpPathBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        value = IngressV1SpecRuleHttpPathBackendService(name=name, port=port)

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> "IngressV1SpecRuleHttpPathBackendResourceOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "IngressV1SpecRuleHttpPathBackendServiceOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendResource"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendService"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1SpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__936c7a2b554e923d738867ad8bdddbe53f2d1b118cc5c10b333b02c9259a6368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendResource",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class IngressV1SpecRuleHttpPathBackendResource:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c8b364ce625eab4bb92ae8363d017c511c9df769ac9a5073e27b7b076228c3)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_group": api_group,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''APIGroup is the group for the resource being referenced.

        If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#api_group IngressV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#kind IngressV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendResourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendResourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e73c8a8e9d52c2dfcb86fc1d60ec37a5a206d562a911062c56a4a065ab0b229)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022a3c53c3a6e19a4e4df8a50a4fa188ad7c0aa3ba29b20034fff98084668955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7973ce78c73746bf4a4f5304d97150fa8d1932982703339d7e049836c23fc65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b621a3c312d49e6710e1db30cf594636296623f3a0e5b9bf0c43f78bf8b3135)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendResource]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb8123d2f414177a62c0656eec02516c41ef3cf39f0f2873d0a9356fe7867d91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendService",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "port": "port"},
)
class IngressV1SpecRuleHttpPathBackendService:
    def __init__(
        self,
        *,
        name: builtins.str,
        port: typing.Union["IngressV1SpecRuleHttpPathBackendServicePort", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param port: port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        if isinstance(port, dict):
            port = IngressV1SpecRuleHttpPathBackendServicePort(**port)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93c04ee4260742d65e1cbec29c0a8191345eaac52ebf84d2175f65d2d09ce955)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "port": port,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> "IngressV1SpecRuleHttpPathBackendServicePort":
        '''port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#port IngressV1#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast("IngressV1SpecRuleHttpPathBackendServicePort", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5de6e218db218f8843ee412ae409b191aa1dae0218c15bbc17c27177f3ba1ce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPort")
    def put_port(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        value = IngressV1SpecRuleHttpPathBackendServicePort(name=name, number=number)

        return typing.cast(None, jsii.invoke(self, "putPort", [value]))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> "IngressV1SpecRuleHttpPathBackendServicePortOutputReference":
        return typing.cast("IngressV1SpecRuleHttpPathBackendServicePortOutputReference", jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(
        self,
    ) -> typing.Optional["IngressV1SpecRuleHttpPathBackendServicePort"]:
        return typing.cast(typing.Optional["IngressV1SpecRuleHttpPathBackendServicePort"], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e94ee297473ee6552424f856380c947351433c3736fce0b5694e5f5f2fa7e8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendService]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2767169520a9f5f5b8a84798c4f7e80e1f8d991cf77f9580648e415a218baf33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServicePort",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "number": "number"},
)
class IngressV1SpecRuleHttpPathBackendServicePort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Specifies the name of the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        :param number: Specifies the numerical port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19fced465f6d72e454b4168f951a099a6d425d59d6b78ff369ba0fccd19fb801)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#name IngressV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''Specifies the numerical port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#number IngressV1#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecRuleHttpPathBackendServicePort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecRuleHttpPathBackendServicePortOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathBackendServicePortOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95d9816c9c11ada3a241c9929ae29c1dab38f747adbcf461efef1d6c220dce99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c569ce7e77f90ed25dd80223638e47fecd5816f29eaa471567503eceb4c3f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "number"))

    @number.setter
    def number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bccf8a422789d3996975287683ae436c9c78e2e2a2719486d475508e27c4ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a225a9e48f2ba3b4bf355190730bf201bd89bb164af6dda5d0e767e68382adbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleHttpPathList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f070f7a1cfd48c3bed3b6d427d1bc82ca90919036b1176a4249711e42c5d5fd5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecRuleHttpPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb173d881dd74280b4156ae12076d1b18260923eafd8ee98073f7be433f5791)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecRuleHttpPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d92cef9f053a5239e14a40d1f84e71eec007e59ca0c00adbdf536e8695dbdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed40fd7573238275876a4ef9eb6b42781394d203c79e90e0a6f4e72886d18061)
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
            type_hints = typing.get_type_hints(_typecheckingstub__095e56f09d81b546efcee6efb54fa3ea5cd57bd7c8f93a2666508d98deae4ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49b3fe5c08213e98c4e1cb45a04540ed8c327d9121a7e2f17113dc46fa210927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleHttpPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleHttpPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a14bfe004b25669d02924ed00230a790144c22d511cd72935e0054c85a2e30be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        resource: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
        service: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#resource IngressV1#resource}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#service IngressV1#service}
        '''
        value = IngressV1SpecRuleHttpPathBackend(resource=resource, service=service)

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPathType")
    def reset_path_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathType", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressV1SpecRuleHttpPathBackendOutputReference:
        return typing.cast(IngressV1SpecRuleHttpPathBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressV1SpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttpPathBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pathTypeInput")
    def path_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc791a14dcb65023447a7bf633b1084011d7140b971597897b3ac63ef6267041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="pathType")
    def path_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathType"))

    @path_type.setter
    def path_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7425677f8bbca512f69725fbd0b31211668fc02e9cc36d1f8dc3a7fb130908b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865fc94c5cd3ff873b3347980415adeffbfc4352315c1967baf62f8b028cce15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c106b0a79ad4d4bdb8a2a2b6470ee3fb197c79a039119d0abeff33f12f4acc3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1678054b81386e5bde6c3d166f6c0014094baa43b009cf216ba95bf06fff49)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aabf3b47db9e533d2f61c616544819d571413205d1779141ed06a1180f44a54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4120c01ce272602387525cfa00e43c3c1b255c4fd193dbdc380577ea09e130fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77372e5aec1217454b53b9cc4d0ec3b238b271b196636dd36748c521aeb50360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf50ece903e58354cce4207db687180a2a8165007c38230f1810e9238ff896b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__190a7fc647e1be4bda9d513f2701d250ef4e0512f59fa01ff9ae3acafa7fb256)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#path IngressV1#path}
        '''
        value = IngressV1SpecRuleHttp(path=path)

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> IngressV1SpecRuleHttpOutputReference:
        return typing.cast(IngressV1SpecRuleHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[IngressV1SpecRuleHttp]:
        return typing.cast(typing.Optional[IngressV1SpecRuleHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41642419afd0c367a57c219c8713d5945a48828571690a2d3dfc3b69a3f6e1ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6903ffff9db8496cd212ddb14a1dcf94cb5b3c98e23549d81aea7a28ddc2b5e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecTls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret_name": "secretName"},
)
class IngressV1SpecTls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#hosts IngressV1#hosts}
        :param secret_name: SecretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#secret_name IngressV1#secret_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf4c96000a9328dbb5d126816d4a0f7510db77e8ac3e81226cb308f71561213e)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Hosts are a list of hosts included in the TLS certificate.

        The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#hosts IngressV1#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''SecretName is the name of the secret used to terminate TLS traffic on port 443.

        Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress_v1#secret_name IngressV1#secret_name}
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1SpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1SpecTlsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecTlsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abb3c4e430bbc2681507563758e9f252f5fdf332ef043071d5cd336da41d0329)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1SpecTlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57bec0c6f2455715bc9033abaea2ab5eb8cde6a70afc46a83f155ed56b502d3f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1SpecTlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6681a330559eba58892116fe2fdf09b2d3623f5bbb5c01e9f7e88daf70b2bfa1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88268e95d63445af0fdd37ecaba491dcb6e76fe12c986c6bf992ae88415f5580)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a6bda1f9dd174d371040960c8c5ae72d5ab7b0e67d6b2eca7c070b37c655744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6da0e575073b6dd2ec7c5f4fcafd90ff21dc5ade476eb275693aaed8e36710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1SpecTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1SpecTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95b4fb727365f8b1dd969b8b5d2f43a4de2b24a341cbc9f0494bb5d5bbe6e56d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetSecretName")
    def reset_secret_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretName", []))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1471f64cc6652141f0332f116c19654802bff17673fa3a66d9a3052a9c47e9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd70717d141b924279e61b74c6390e78d9206ba8f750c86f9c1c4c6174b11d89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12434058982a33a5b1e3a9ca1a62cfdfa1053d5b6f227e8816abd51589dd220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1Status",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1Status:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1Status(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1StatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cec90a7b4a80462101eba77d66d674a7b8b0d60b6f7fcd8955f6bd2d292deea3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1StatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c4d6350383bad1275dd8438f051cfbb9f3fc805374ef15a34ab92801cbe2a4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508f3cb22455d3a30df6c48394920c24eaa8b752e2478e36b0d935c3cfacb2d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bc85a9942aef3430b230316a66854d0f9afa56949554cfe42131c3ffeaffce0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48e583bfb174a6f3c3d8155930af3290045567645de61d575221e3f8105092b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1StatusLoadBalancer:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1StatusLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancerIngress",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressV1StatusLoadBalancerIngress:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressV1StatusLoadBalancerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressV1StatusLoadBalancerIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancerIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__713f91d105ce47034e0ca16b830ab456f1de5c6ed442e78bad8a9e5a1244b94b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IngressV1StatusLoadBalancerIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f98a0314b4998a46dc9ca1fc866eff646c86c848c666b0af4644adf7760b282)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusLoadBalancerIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc9934ccd8a3cf4f8f8b3eb8a2df1b1ae1f18b7cba5488e1caf6e32db9a3aa18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8235af910186d8a558231291c189aea1ab1ede2e228cbbedc991de63a735ef9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29babef2a96ac680d55fbde0b6362fb3427ff36a14ad7826d737ef5d09908baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressV1StatusLoadBalancerIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancerIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e62a37b6d036cb246071d6732398b46ff11e6c50d7b366f94c4f0ca2bb244eb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1StatusLoadBalancerIngress]:
        return typing.cast(typing.Optional[IngressV1StatusLoadBalancerIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1StatusLoadBalancerIngress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9660304b74ed682faac2ab3dafe4470693bda79f3aaabf3393ed83adac2cef16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1StatusLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c5772e4a40b245f96b9a6766cb3a70e10a396294d036d3cd94a06f62f350be2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressV1StatusLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a557a71e21dd6d6b5cce3a7c5045aa02528f52123b06635b53ac9ee79d46e6d6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressV1StatusLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524ccc12706893220ac7bab68599d2e4804c76270ce8663a3ba95bbc15b0f316)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c53d39aab28723aa555f643a9db1b52f330088c84d71ee990f920d46d1a94b0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6cf48b2b32cb1670bb785fd1be6d8c1f8febc821d0a723f033a19360a654782e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressV1StatusLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd23f80f77e1a004554bcc837d466afaf589a5461ed1971555e8c5dbed0f63d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> IngressV1StatusLoadBalancerIngressList:
        return typing.cast(IngressV1StatusLoadBalancerIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1StatusLoadBalancer]:
        return typing.cast(typing.Optional[IngressV1StatusLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressV1StatusLoadBalancer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1e869c58d4d4a31dca7ff1ca916a9a925c1cb84df2bd3e57ec21366a8340e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressV1StatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingressV1.IngressV1StatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e25f93b78069951076bc2d263100f7f000237b56ae00001267d990abee693853)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> IngressV1StatusLoadBalancerList:
        return typing.cast(IngressV1StatusLoadBalancerList, jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressV1Status]:
        return typing.cast(typing.Optional[IngressV1Status], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressV1Status]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__024616dbd795b5e3e5c1acde21349c82d28a9bc5f0e5fceae5753df8ae32252c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IngressV1",
    "IngressV1Config",
    "IngressV1Metadata",
    "IngressV1MetadataOutputReference",
    "IngressV1Spec",
    "IngressV1SpecDefaultBackend",
    "IngressV1SpecDefaultBackendOutputReference",
    "IngressV1SpecDefaultBackendResource",
    "IngressV1SpecDefaultBackendResourceOutputReference",
    "IngressV1SpecDefaultBackendService",
    "IngressV1SpecDefaultBackendServiceOutputReference",
    "IngressV1SpecDefaultBackendServicePort",
    "IngressV1SpecDefaultBackendServicePortOutputReference",
    "IngressV1SpecOutputReference",
    "IngressV1SpecRule",
    "IngressV1SpecRuleHttp",
    "IngressV1SpecRuleHttpOutputReference",
    "IngressV1SpecRuleHttpPath",
    "IngressV1SpecRuleHttpPathBackend",
    "IngressV1SpecRuleHttpPathBackendOutputReference",
    "IngressV1SpecRuleHttpPathBackendResource",
    "IngressV1SpecRuleHttpPathBackendResourceOutputReference",
    "IngressV1SpecRuleHttpPathBackendService",
    "IngressV1SpecRuleHttpPathBackendServiceOutputReference",
    "IngressV1SpecRuleHttpPathBackendServicePort",
    "IngressV1SpecRuleHttpPathBackendServicePortOutputReference",
    "IngressV1SpecRuleHttpPathList",
    "IngressV1SpecRuleHttpPathOutputReference",
    "IngressV1SpecRuleList",
    "IngressV1SpecRuleOutputReference",
    "IngressV1SpecTls",
    "IngressV1SpecTlsList",
    "IngressV1SpecTlsOutputReference",
    "IngressV1Status",
    "IngressV1StatusList",
    "IngressV1StatusLoadBalancer",
    "IngressV1StatusLoadBalancerIngress",
    "IngressV1StatusLoadBalancerIngressList",
    "IngressV1StatusLoadBalancerIngressOutputReference",
    "IngressV1StatusLoadBalancerList",
    "IngressV1StatusLoadBalancerOutputReference",
    "IngressV1StatusOutputReference",
]

publication.publish()

def _typecheckingstub__3c906024ebb2917b40aa4b415615e01f82dfe593b0fb2fb9bd04170155a63e24(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[IngressV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__0c38d3556ec643facfb08bd45f8a5010eef2402a7bbfae7c20ce6d2ae4fe9406(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e589a552b007274dc1be966db9ea1a5a61099700dfcdcaaefea90f95d3537c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf63d53e98f6209c118910104409793a0f869e7eb79464ba34555d69c4f2412a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[IngressV1Metadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressV1Spec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc98afd4bc3156d01361dc929cc5a7a73a825754b39a76da76fa788a21d9e83(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89b7f06e8bbfa73d95b207b61b802c869e985045f1b2cd52f5f8a5a57b58dc5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363d5d09211b9c504b5646e2958205a6517707e367bc68f7305289dff69daad4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871a4a76d11535f748649ac20d97b115db8737760cc87c0ea932bd9814f06577(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e678690cd1e1703c49aa8ded17e5cbf3bf248ddc438465ff96477607678cb627(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35020cc2235fe398a8033b6e664fdf78feca1e47c775f0abdfd664c00388346f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adecf7f34fe3aa1251c67fd84b404aae95a9f7e8b9394a99707efc5596eaef63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa9c31fc6e3183426016ae58660377e947d810b1d9b2faf65c21f37ff63bd8f(
    value: typing.Optional[IngressV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f135a737d6b6269cc4bad1c464aabb55630f8ed90fcb3beeb413a6bae5c7d44b(
    *,
    default_backend: typing.Optional[typing.Union[IngressV1SpecDefaultBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecTls, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8d246346bee7a8d927238cfc191b9c751f7403151f5933a5f657127dfc8f58(
    *,
    resource: typing.Optional[typing.Union[IngressV1SpecDefaultBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[IngressV1SpecDefaultBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e93f1123f82b9d1445387cac5645ee06cd6adeb3a00a2b02e9c95688381526(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5f8c560b1dc8337e45a443e736bce48bff61a8888ac14c5e2912c695803b71(
    value: typing.Optional[IngressV1SpecDefaultBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186ab9d837f46b0dfd676cf18f5734040dc21755721743da9551c8b2cfaeddcf(
    *,
    api_group: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eed59ed7313e9c64884d0dc4b427c302014862dd6c282ffcde11504cefbf78b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0c9607dbe28a42c4b3af13c498b6266f9da9ab38c967ed2c2e6067df8a6416(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1caff48385507b21b8971ba316644494d18747c99f1ca6439fcf61a27cb7c018(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f11d64104b4bff4bd50af019aa6e5bd6d3a5fe7d1ff36bdff8b0f856deeec25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f93a1c8ceb3d300efb9ea6523be36d8855f0ec492853630c15dcecc19c16d9(
    value: typing.Optional[IngressV1SpecDefaultBackendResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5418fdbc4702da4008a9eeddb18ce9d19e527f09567f19aeaacb28b7cc4bb73b(
    *,
    name: builtins.str,
    port: typing.Union[IngressV1SpecDefaultBackendServicePort, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c84f2ec3458317ffac9660907f83d16a26c16badf155326ded672d1d795f838(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b23dd6a7dcdc02f7ab0f6da9123bda8702170cc8937bcfd6bbca000d172f7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505efffc431df1c9c9cfc450b53e3d2bcabe5f5055c9232088ffb5c697fef06a(
    value: typing.Optional[IngressV1SpecDefaultBackendService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99d732cf89605de87bc88e4499bea6367e652c8fbba0b97a9ebdb388e8bf26d7(
    *,
    name: typing.Optional[builtins.str] = None,
    number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18cdfd02dd8b4588e107a9e3013f668302cf17ecf8245ab9a128c5359595066b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae0d7c42c0db876196b4f9c1aed3c432d2cb6ec27463605a5cff08094c33ed1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3219bd18b34f7b3470b9e8cd64407702ec6cb1ea06e6558c171968f3eaf1f60f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ef19c8cc2ba61f57563fffac23ca68e5e9d3b82cc15b836a33488e1f266767(
    value: typing.Optional[IngressV1SpecDefaultBackendServicePort],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eac9a4a9df131d0864032f0f7796d397234e32854749ddd0d808d2983b6d12a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3569eca26641df64c2f282b7db1def5a58cb4a02becda38125c22d59f2e40012(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ce6e879cbe1e017a8f8d37addfb0380a1f435bcf977eff24cdc8d46a477018(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecTls, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07696d4f2fe41441d9c919551ec6b4933edcc7a2ba51a9cb1aee81c217f64883(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43333428ac69830ce13d9454f9029d17020625b12c1ac5fefd0c70a5565e9ef6(
    value: typing.Optional[IngressV1Spec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__161adce870403a7dfee95ba04fd0daaa515c870443b196bb151dc096773775bf(
    *,
    host: typing.Optional[builtins.str] = None,
    http: typing.Optional[typing.Union[IngressV1SpecRuleHttp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5403d0999a4f97b23974b2a5e46d63d3027335852b76c915edfa036e747c52e0(
    *,
    path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11eeadd7c9ba973c8fbddc46e45f234e304ea2c45a3f3bcf3307c7c83609f2d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322a9278fbeda1e205ff002508092eb7955ab39470242ea6d9b14c53e5587fef(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressV1SpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d4023f941ec08ebe0c364c2a95ca182613f0dd40cd0ac483cdb43f4da93982(
    value: typing.Optional[IngressV1SpecRuleHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318858710f2074f6663608b99ea18ec593f47c41c694cc0c2f4b78e305955d25(
    *,
    backend: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    path_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15de79e1524fa215bee3f4959cfcfe62412143c53a7ccac16a9e2ace8fc1fd0d(
    *,
    resource: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendResource, typing.Dict[builtins.str, typing.Any]]] = None,
    service: typing.Optional[typing.Union[IngressV1SpecRuleHttpPathBackendService, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912745f5feb88ae395aef6fc362bb7f822fa155136e6c36d0b9e047286df7629(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936c7a2b554e923d738867ad8bdddbe53f2d1b118cc5c10b333b02c9259a6368(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c8b364ce625eab4bb92ae8363d017c511c9df769ac9a5073e27b7b076228c3(
    *,
    api_group: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e73c8a8e9d52c2dfcb86fc1d60ec37a5a206d562a911062c56a4a065ab0b229(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022a3c53c3a6e19a4e4df8a50a4fa188ad7c0aa3ba29b20034fff98084668955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7973ce78c73746bf4a4f5304d97150fa8d1932982703339d7e049836c23fc65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b621a3c312d49e6710e1db30cf594636296623f3a0e5b9bf0c43f78bf8b3135(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8123d2f414177a62c0656eec02516c41ef3cf39f0f2873d0a9356fe7867d91(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendResource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c04ee4260742d65e1cbec29c0a8191345eaac52ebf84d2175f65d2d09ce955(
    *,
    name: builtins.str,
    port: typing.Union[IngressV1SpecRuleHttpPathBackendServicePort, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5de6e218db218f8843ee412ae409b191aa1dae0218c15bbc17c27177f3ba1ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e94ee297473ee6552424f856380c947351433c3736fce0b5694e5f5f2fa7e8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2767169520a9f5f5b8a84798c4f7e80e1f8d991cf77f9580648e415a218baf33(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19fced465f6d72e454b4168f951a099a6d425d59d6b78ff369ba0fccd19fb801(
    *,
    name: typing.Optional[builtins.str] = None,
    number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d9816c9c11ada3a241c9929ae29c1dab38f747adbcf461efef1d6c220dce99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c569ce7e77f90ed25dd80223638e47fecd5816f29eaa471567503eceb4c3f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bccf8a422789d3996975287683ae436c9c78e2e2a2719486d475508e27c4ac(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a225a9e48f2ba3b4bf355190730bf201bd89bb164af6dda5d0e767e68382adbb(
    value: typing.Optional[IngressV1SpecRuleHttpPathBackendServicePort],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f070f7a1cfd48c3bed3b6d427d1bc82ca90919036b1176a4249711e42c5d5fd5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb173d881dd74280b4156ae12076d1b18260923eafd8ee98073f7be433f5791(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d92cef9f053a5239e14a40d1f84e71eec007e59ca0c00adbdf536e8695dbdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed40fd7573238275876a4ef9eb6b42781394d203c79e90e0a6f4e72886d18061(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095e56f09d81b546efcee6efb54fa3ea5cd57bd7c8f93a2666508d98deae4ebc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b3fe5c08213e98c4e1cb45a04540ed8c327d9121a7e2f17113dc46fa210927(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRuleHttpPath]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a14bfe004b25669d02924ed00230a790144c22d511cd72935e0054c85a2e30be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc791a14dcb65023447a7bf633b1084011d7140b971597897b3ac63ef6267041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7425677f8bbca512f69725fbd0b31211668fc02e9cc36d1f8dc3a7fb130908b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865fc94c5cd3ff873b3347980415adeffbfc4352315c1967baf62f8b028cce15(
    value: typing.Optional[typing.Union[IngressV1SpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c106b0a79ad4d4bdb8a2a2b6470ee3fb197c79a039119d0abeff33f12f4acc3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1678054b81386e5bde6c3d166f6c0014094baa43b009cf216ba95bf06fff49(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aabf3b47db9e533d2f61c616544819d571413205d1779141ed06a1180f44a54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4120c01ce272602387525cfa00e43c3c1b255c4fd193dbdc380577ea09e130fd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77372e5aec1217454b53b9cc4d0ec3b238b271b196636dd36748c521aeb50360(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf50ece903e58354cce4207db687180a2a8165007c38230f1810e9238ff896b6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__190a7fc647e1be4bda9d513f2701d250ef4e0512f59fa01ff9ae3acafa7fb256(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41642419afd0c367a57c219c8713d5945a48828571690a2d3dfc3b69a3f6e1ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6903ffff9db8496cd212ddb14a1dcf94cb5b3c98e23549d81aea7a28ddc2b5e5(
    value: typing.Optional[typing.Union[IngressV1SpecRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4c96000a9328dbb5d126816d4a0f7510db77e8ac3e81226cb308f71561213e(
    *,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb3c4e430bbc2681507563758e9f252f5fdf332ef043071d5cd336da41d0329(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bec0c6f2455715bc9033abaea2ab5eb8cde6a70afc46a83f155ed56b502d3f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6681a330559eba58892116fe2fdf09b2d3623f5bbb5c01e9f7e88daf70b2bfa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88268e95d63445af0fdd37ecaba491dcb6e76fe12c986c6bf992ae88415f5580(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a6bda1f9dd174d371040960c8c5ae72d5ab7b0e67d6b2eca7c070b37c655744(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6da0e575073b6dd2ec7c5f4fcafd90ff21dc5ade476eb275693aaed8e36710(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressV1SpecTls]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b4fb727365f8b1dd969b8b5d2f43a4de2b24a341cbc9f0494bb5d5bbe6e56d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1471f64cc6652141f0332f116c19654802bff17673fa3a66d9a3052a9c47e9f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd70717d141b924279e61b74c6390e78d9206ba8f750c86f9c1c4c6174b11d89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12434058982a33a5b1e3a9ca1a62cfdfa1053d5b6f227e8816abd51589dd220(
    value: typing.Optional[typing.Union[IngressV1SpecTls, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec90a7b4a80462101eba77d66d674a7b8b0d60b6f7fcd8955f6bd2d292deea3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c4d6350383bad1275dd8438f051cfbb9f3fc805374ef15a34ab92801cbe2a4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508f3cb22455d3a30df6c48394920c24eaa8b752e2478e36b0d935c3cfacb2d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc85a9942aef3430b230316a66854d0f9afa56949554cfe42131c3ffeaffce0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e583bfb174a6f3c3d8155930af3290045567645de61d575221e3f8105092b3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713f91d105ce47034e0ca16b830ab456f1de5c6ed442e78bad8a9e5a1244b94b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f98a0314b4998a46dc9ca1fc866eff646c86c848c666b0af4644adf7760b282(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9934ccd8a3cf4f8f8b3eb8a2df1b1ae1f18b7cba5488e1caf6e32db9a3aa18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8235af910186d8a558231291c189aea1ab1ede2e228cbbedc991de63a735ef9c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29babef2a96ac680d55fbde0b6362fb3427ff36a14ad7826d737ef5d09908baf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62a37b6d036cb246071d6732398b46ff11e6c50d7b366f94c4f0ca2bb244eb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9660304b74ed682faac2ab3dafe4470693bda79f3aaabf3393ed83adac2cef16(
    value: typing.Optional[IngressV1StatusLoadBalancerIngress],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5772e4a40b245f96b9a6766cb3a70e10a396294d036d3cd94a06f62f350be2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a557a71e21dd6d6b5cce3a7c5045aa02528f52123b06635b53ac9ee79d46e6d6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524ccc12706893220ac7bab68599d2e4804c76270ce8663a3ba95bbc15b0f316(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53d39aab28723aa555f643a9db1b52f330088c84d71ee990f920d46d1a94b0b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf48b2b32cb1670bb785fd1be6d8c1f8febc821d0a723f033a19360a654782e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd23f80f77e1a004554bcc837d466afaf589a5461ed1971555e8c5dbed0f63d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1e869c58d4d4a31dca7ff1ca916a9a925c1cb84df2bd3e57ec21366a8340e0(
    value: typing.Optional[IngressV1StatusLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e25f93b78069951076bc2d263100f7f000237b56ae00001267d990abee693853(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024616dbd795b5e3e5c1acde21349c82d28a9bc5f0e5fceae5753df8ae32252c(
    value: typing.Optional[IngressV1Status],
) -> None:
    """Type checking stubs"""
    pass
