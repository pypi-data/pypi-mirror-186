'''
# `kubernetes_ingress`

Refer to the Terraform Registory for docs: [`kubernetes_ingress`](https://www.terraform.io/docs/providers/kubernetes/r/ingress).
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


class Ingress(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.Ingress",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress kubernetes_ingress}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["IngressMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressSpec", typing.Dict[builtins.str, typing.Any]],
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
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress kubernetes_ingress} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8006946bc35be32a62e96bff7c8ccc97043ea94a1a21e3def57cfadab6d69b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IngressConfig(
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        value = IngressMetadata(
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
        backend: typing.Optional[typing.Union["IngressSpecBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        value = IngressSpec(
            backend=backend, ingress_class_name=ingress_class_name, rule=rule, tls=tls
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
    def metadata(self) -> "IngressMetadataOutputReference":
        return typing.cast("IngressMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "IngressSpecOutputReference":
        return typing.cast("IngressSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "IngressStatusList":
        return typing.cast("IngressStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["IngressMetadata"]:
        return typing.cast(typing.Optional["IngressMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["IngressSpec"]:
        return typing.cast(typing.Optional["IngressSpec"], jsii.get(self, "specInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__56fe964bc28425fee2a37ceb739c40f974a4303b07b49b15af909cfa65bf167b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2eeac00b8f90a1c5bd831cb91403c10110e7542530ac887dc3311a5bcffbca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLoadBalancer", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressConfig",
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
class IngressConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["IngressMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union["IngressSpec", typing.Dict[builtins.str, typing.Any]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param wait_for_load_balancer: Terraform will wait for the load balancer to have at least 1 endpoint before considering the resource created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = IngressMetadata(**metadata)
        if isinstance(spec, dict):
            spec = IngressSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84df8f9d7ee698e9f7f4fa00c49d87a6ce294c144c4348c7421d540db194748)
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
    def metadata(self) -> "IngressMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#metadata Ingress#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("IngressMetadata", result)

    @builtins.property
    def spec(self) -> "IngressSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#spec Ingress#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("IngressSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#id Ingress#id}.

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#wait_for_load_balancer Ingress#wait_for_load_balancer}
        '''
        result = self._values.get("wait_for_load_balancer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class IngressMetadata:
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
        :param annotations: An unstructured key value map stored with the ingress that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the ingress. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        :param name: Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        :param namespace: Namespace defines the space within which name of the ingress must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8a79ba50376ed9849f1147224792b601b74e36aa9a4dc1a612da8fa86d383c8)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#annotations Ingress#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#generate_name Ingress#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the ingress.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#labels Ingress#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the ingress, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#name Ingress#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the ingress must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#namespace Ingress#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6259440d8dd9d319e8bf16554e7dc2d8331dbfe53f1d044cf0f7f3be340f3b67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1de22351605117716792774c642358fb4ca4b58f42b25a1fbf0fc4f9de6e2afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c0c7113d6bc7612c1cae1f362523b5dc59b882bb5539050f6f9d1ec2159bb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce1d4dc78922e9d3cbc6ede722e49df8162b6842222f04b9565c83eda5305788)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b5af26a3653ec1dd706defa673ad1791d838d1f3a3e57a90c233f225a5a997a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d40cef1608c452e00910699057718ec97988497e630d8f2c39e7c05ae5c38966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressMetadata]:
        return typing.cast(typing.Optional[IngressMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7992db5e36ce593f5bd75a8a0d9a78251e454ae54095a8bf436161c969ca02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpec",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "ingress_class_name": "ingressClassName",
        "rule": "rule",
        "tls": "tls",
    },
)
class IngressSpec:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressSpecBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        ingress_class_name: typing.Optional[builtins.str] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param ingress_class_name: IngressClassName is the name of the IngressClass cluster resource. The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        if isinstance(backend, dict):
            backend = IngressSpecBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3021c753777b65b88f43d3dcfff32c9379bf5d63293fadd0976b258f94e00af7)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument ingress_class_name", value=ingress_class_name, expected_type=type_hints["ingress_class_name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if ingress_class_name is not None:
            self._values["ingress_class_name"] = ingress_class_name
        if rule is not None:
            self._values["rule"] = rule
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def backend(self) -> typing.Optional["IngressSpecBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressSpecBackend"], result)

    @builtins.property
    def ingress_class_name(self) -> typing.Optional[builtins.str]:
        '''IngressClassName is the name of the IngressClass cluster resource.

        The associated IngressClass defines which controller will implement the resource. This replaces the deprecated ``kubernetes.io/ingress.class`` annotation. For backwards compatibility, when that annotation is set, it must be given precedence over this field. The controller may emit a warning if the field and annotation have different values. Implementations of this API should ignore Ingresses without a class specified. An IngressClass resource may be marked as default, which can be used to set a default value for this field. For more information, refer to the IngressClass documentation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#ingress_class_name Ingress#ingress_class_name}
        '''
        result = self._values.get("ingress_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#rule Ingress#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#tls Ingress#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecBackend",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "service_port": "servicePort"},
)
class IngressSpecBackend:
    def __init__(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f280b41d733dcb167af41e720fce78f42c56aa6bc2fb406ebd008df2a96aa9d)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument service_port", value=service_port, expected_type=type_hints["service_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if service_name is not None:
            self._values["service_name"] = service_name
        if service_port is not None:
            self._values["service_port"] = service_port

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_port(self) -> typing.Optional[builtins.str]:
        '''Specifies the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b99641a6795d25451794131a009e0310a317178a70e0d29e0b358c92500924f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetServicePort")
    def reset_service_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePort", []))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePortInput")
    def service_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePortInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__758bb3c1590681ec57fe0bdb27dc41afab0fd4123576d3ffc2d2479a246264d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePort")
    def service_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePort"))

    @service_port.setter
    def service_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24e866c60d4c54f83a8aa8f922e18c93744ce4a6e821dac488d14f88654576b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecBackend]:
        return typing.cast(typing.Optional[IngressSpecBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpecBackend]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ada5e7d455d90c7209896dcec6f962d746dc68906077cd24c3ea644cf8995c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eebedb091f291628217ec62a6166734ccd102a4e1e591892588a75dda6872e8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        value = IngressSpecBackend(
            service_name=service_name, service_port=service_port
        )

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41fed929b027eaea1337f2b9b19320ffdba213ce7871ee04889cbd57e84026e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecTls", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2c6ae3b4d5c9118fe2c2a069a2364010ecd1c14db608c8d01bdfb85866f135)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

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
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressSpecBackendOutputReference:
        return typing.cast(IngressSpecBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "IngressSpecRuleList":
        return typing.cast("IngressSpecRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "IngressSpecTlsList":
        return typing.cast("IngressSpecTlsList", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressSpecBackend]:
        return typing.cast(typing.Optional[IngressSpecBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassNameInput")
    def ingress_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ingressClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecTls"]]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressClassName")
    def ingress_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ingressClassName"))

    @ingress_class_name.setter
    def ingress_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445fd0d25620b22b7a76a707b3445b02aa525bc08cc0f6d72b375c60e0f8ca54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressClassName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpec]:
        return typing.cast(typing.Optional[IngressSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8791fc8767395923eefb9f392b4ac9abb6d5865c20e58abb3907611ab3d094be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRule",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "host": "host"},
)
class IngressSpecRule:
    def __init__(
        self,
        *,
        http: typing.Union["IngressSpecRuleHttp", typing.Dict[builtins.str, typing.Any]],
        host: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#http Ingress#http}
        :param host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the IP in the Spec of the parent Ingress. 2. The ``:`` delimiter is not respected because ports are not allowed. Currently the port of an Ingress is implicitly :80 for http and :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue. Host can be "precise" which is a domain name without the terminating dot of a network host (e.g. "foo.bar.com") or "wildcard", which is a domain name prefixed with a single wildcard label (e.g. "*.foo.com"). The wildcard character '*' must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host == "*"). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#host Ingress#host}
        '''
        if isinstance(http, dict):
            http = IngressSpecRuleHttp(**http)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4ed0f224c7aa4dbdfadc3e9b54de344315b0b07a980af0aca7b1cc6388dfc8)
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http": http,
        }
        if host is not None:
            self._values["host"] = host

    @builtins.property
    def http(self) -> "IngressSpecRuleHttp":
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#http Ingress#http}
        '''
        result = self._values.get("http")
        assert result is not None, "Required property 'http' is missing"
        return typing.cast("IngressSpecRuleHttp", result)

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#host Ingress#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttp",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class IngressSpecRuleHttp:
    def __init__(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee17d50cb5da7027171e28626ee1882f8cdbc364e4252c028794883c4c84172f)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecRuleHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__560efc853eac8e84778d4a02eadfb056fb8a1cb0e2ff7907dd4020bc931a1134)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IngressSpecRuleHttpPath", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5e6a6ac2a2f0424909fb97e6d3402f2129daec7bbad041de2f5490409de213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "IngressSpecRuleHttpPathList":
        return typing.cast("IngressSpecRuleHttpPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IngressSpecRuleHttpPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecRuleHttp]:
        return typing.cast(typing.Optional[IngressSpecRuleHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressSpecRuleHttp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fc2f836c2f1b0e04bf5273001ced20b9add5e4728f16d6d1e03df949d3ebcf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpPath",
    jsii_struct_bases=[],
    name_mapping={"backend": "backend", "path": "path"},
)
class IngressSpecRuleHttpPath:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union["IngressSpecRuleHttpPathBackend", typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        :param path: Path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        if isinstance(backend, dict):
            backend = IngressSpecRuleHttpPathBackend(**backend)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e3824a2a1c595698ddeba39c11d317febbf1e86c8d0ce0d39ab63ca1b17ad7)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def backend(self) -> typing.Optional["IngressSpecRuleHttpPathBackend"]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#backend Ingress#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional["IngressSpecRuleHttpPathBackend"], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path is matched against the path of an incoming request.

        Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttpPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpPathBackend",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName", "service_port": "servicePort"},
)
class IngressSpecRuleHttpPathBackend:
    def __init__(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928b6a3b8cb622955865820f8b3f0692e64924367c6444b6d9aa00a725896bf3)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument service_port", value=service_port, expected_type=type_hints["service_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if service_name is not None:
            self._values["service_name"] = service_name
        if service_port is not None:
            self._values["service_port"] = service_port

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_port(self) -> typing.Optional[builtins.str]:
        '''Specifies the port of the referenced service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        result = self._values.get("service_port")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecRuleHttpPathBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecRuleHttpPathBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpPathBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f908d64030b2c4eadf53dfb73f9042c41bfbd6808121146050b9deae820ae913)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @jsii.member(jsii_name="resetServicePort")
    def reset_service_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePort", []))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePortInput")
    def service_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePortInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b87b6a4beed05ef350c2b44a663730a3ecf67fcb5de8131d2e198098387eac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="servicePort")
    def service_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePort"))

    @service_port.setter
    def service_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0e9a3b0efbbd237c7dd85c4d620cfbbbbc6218beb68eb0892a4f4fb12c6201)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressSpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressSpecRuleHttpPathBackend], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressSpecRuleHttpPathBackend],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a210225d219ad5eb91d507992ebf04aea72f56412872a6b5855bf860ee95a91c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleHttpPathList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpPathList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ff38f0276b352dd4c415e036b16946a34bc3defd436da4194ad9c8c4fadd7eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecRuleHttpPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11eaeedf33e8ab5690ab7d1f4985119741dc21b87be74f813fe61e04961ed4c5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecRuleHttpPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c430671af8fb83f01bc1fd2517a5db26eaef994a87a78cd1a67363cd76419c51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__537bd161f24dba27cbe4f3d860c6190c4a52387119a8eda23175efc9380be947)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e931879d7bbaca0e65c1842353281f0872f0238472d76ce8767dcb7ea168364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13af757bb5fa392d090c29b4757d1b8e4355d5359e15078ed44bea044ddb0ea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleHttpPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleHttpPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__956b0de1ed4fd021a294aafdbff1bf968c422baa6b230c0a7ef0dd9766000f45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        *,
        service_name: typing.Optional[builtins.str] = None,
        service_port: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_name: Specifies the name of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_name Ingress#service_name}
        :param service_port: Specifies the port of the referenced service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#service_port Ingress#service_port}
        '''
        value = IngressSpecRuleHttpPathBackend(
            service_name=service_name, service_port=service_port
        )

        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> IngressSpecRuleHttpPathBackendOutputReference:
        return typing.cast(IngressSpecRuleHttpPathBackendOutputReference, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[IngressSpecRuleHttpPathBackend]:
        return typing.cast(typing.Optional[IngressSpecRuleHttpPathBackend], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb994420011d59f9d2b7c4cb29e0723bfc2d044ceb93078ecfa3ca8ce43b232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13682c0a2fd67dcc4e08bc83ca1822f7de4025638d464e360ff3f341f1ff318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcf5f3ad56f8d3b8950efe223c634bb8859eb6dbbda35ff9ac12dddfdb95a739)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2716f669732ef30bfdd9e235ed864a94011d421611b66e788b8a54a01aa67fb9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a6f0d8d7de9192d6aec09ee52ab65a9ddd1708ac72580a17406b3d23b9a491)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d49ac94067a688839a24db964a8230ba0fc649120f35165f64a4fc9052fa848)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dae9e10a82764cef7e049e98031ad906243507ee9ace88944e04f4a5f05b6369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ad4a64e9bed1ed99a5c6071c16e376e555b5872dcd16f31cd351139eb73a8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6c12953100ce489271f324bf66c2e68a5adeb4c6d03d16328307eb6ef051cf2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#path Ingress#path}
        '''
        value = IngressSpecRuleHttp(path=path)

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> IngressSpecRuleHttpOutputReference:
        return typing.cast(IngressSpecRuleHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[IngressSpecRuleHttp]:
        return typing.cast(typing.Optional[IngressSpecRuleHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed213522dd0d7b0a36cea766a63121093817034ad8bc0bfdb941e4af1376d5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8945104ed1d7550f0edf947d3bf94eaefce8bbcf2da46dcceb2f0d08b7cf78c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecTls",
    jsii_struct_bases=[],
    name_mapping={"hosts": "hosts", "secret_name": "secretName"},
)
class IngressSpecTls:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#hosts Ingress#hosts}
        :param secret_name: SecretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#secret_name Ingress#secret_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2b5febd1bc3e4f74de6b36766b01e729113674394c0f0ebacbdeb11c5c8539)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#hosts Ingress#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''SecretName is the name of the secret used to terminate TLS traffic on port 443.

        Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/ingress#secret_name Ingress#secret_name}
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressSpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressSpecTlsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecTlsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4e0681dc43b627cc7b8efa6589571fa50a5f36d97d126c5e102826430810961)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressSpecTlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6dd3dc3c236e0a1e6bea62beea78cb6b5f280829edf19616a670a3c86638ec2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressSpecTlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db4b4da996e506233c0af76ac3cca464f6b3d62c3c3790aa9e020b5bc5fad6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7702bfa718314adffe001a25493682a0b2d5028d86a4a36724ff06d1ee9770b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e47b325b57ea81affa82ab8167f43a4c7ed904bae97ff47622c3d35c6185c845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c42a49985037844bb48bcae2b732fb50e42a7046fe454e6554829f46af0298f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressSpecTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressSpecTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2098fa8c774abd6a4aba7cb485acbee4d1d7984c94f6bdcee72075e0a367f3f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4934c26edcc31c547def0d6b11c84f68e92058cda91174f511d64b6eb0ef4a86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b0c4069d5dfd6db7fa077449578759edbb6fcd599870f77df2daec99c14a65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c854c1a2ea73afa3a96b0ea12979b59929e24407425f33e3387aa376624d75c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressStatusList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7e6cb2b25a8e2657636ad4719e5dd725020b41217d973172b1787d30777c650)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afe008b1e109a749398ce50bc13cb7e2c2bcfaebcf83a64020d5228c3fb0ada)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ccd49c883a4c2b91199e237f815974a94aeebaa83b880281ac403ffa4536c44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7561261034e408e9105a5b02ea31817d585b59e9a068da24e0d93dc5939b7c5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76b9f706d1c8326cefa9fc7e9a34250388dfcb9e14de4a413e3174286b1aad40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatusLoadBalancer:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatusLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancerIngress",
    jsii_struct_bases=[],
    name_mapping={},
)
class IngressStatusLoadBalancerIngress:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngressStatusLoadBalancerIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IngressStatusLoadBalancerIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancerIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__285671b68acb000f0ce30dfb6e4206dcdb9047f2d7420e900549db2dad9c066c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IngressStatusLoadBalancerIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ffcdc77e4f83cab9fc042d8dd91a20f989ca4d0d6762217c34dd07bb72a26f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusLoadBalancerIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__162aeaf6c5819ce111e411f4e79331c4ee2935c585449870e5bcd7b5b025374f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a44489468c0410ba9bdecd9425f178d921ad46a70a277860aee3240ce5b441e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdcf194184beea76bd90ae937ea3c5f4b72d228fe204cca29df63d5ce615e481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressStatusLoadBalancerIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancerIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__220494a9e56b971af7e77fa62620e698d168201e1f1c065fc782e99ed397e776)
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
    def internal_value(self) -> typing.Optional[IngressStatusLoadBalancerIngress]:
        return typing.cast(typing.Optional[IngressStatusLoadBalancerIngress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IngressStatusLoadBalancerIngress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69872fa8ee35e1d066bee9b4f8108eab0aabde9e33c3dfd19c34fa7f965c2cf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressStatusLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77f67925bfd1b35d7e3ffda861ec18dcd8bccb0d05dd4b1431ffb5f81f16b442)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IngressStatusLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__025726fc2bac5b6818a28ca6a8823a1e1a0f7bdff70d522ee4a6171b4cacada3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IngressStatusLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0023e1991020320fbd2b74acec7f6fd9dbedf723fcb47ccda15948b49f16a2ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd673cd8545ee55d7352313407dddb5a9993507890bd116ab3e5f66ad6241001)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f86a195d7a1793eb2b947a507983b6dad737ea44a27dec369173fab92a585945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class IngressStatusLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91ba2a902c72319d0618e4e93e4a6276d8f932ca94af63a152a15b92145f6ca6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> IngressStatusLoadBalancerIngressList:
        return typing.cast(IngressStatusLoadBalancerIngressList, jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressStatusLoadBalancer]:
        return typing.cast(typing.Optional[IngressStatusLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressStatusLoadBalancer]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93be3d6981975a7ba3b03ca6655a42a1b0ba51d53be7a777870a313b1155fa4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IngressStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.ingress.IngressStatusOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__724ce90d8cb8a8258938a2d82d6445dff38c3a0382dec36903f4859aedefbaa6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> IngressStatusLoadBalancerList:
        return typing.cast(IngressStatusLoadBalancerList, jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IngressStatus]:
        return typing.cast(typing.Optional[IngressStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IngressStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bc1fba3a2c45c909194e3e2a085e1fda0340c2bcaa0b5c3a19bfb23afff75fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Ingress",
    "IngressConfig",
    "IngressMetadata",
    "IngressMetadataOutputReference",
    "IngressSpec",
    "IngressSpecBackend",
    "IngressSpecBackendOutputReference",
    "IngressSpecOutputReference",
    "IngressSpecRule",
    "IngressSpecRuleHttp",
    "IngressSpecRuleHttpOutputReference",
    "IngressSpecRuleHttpPath",
    "IngressSpecRuleHttpPathBackend",
    "IngressSpecRuleHttpPathBackendOutputReference",
    "IngressSpecRuleHttpPathList",
    "IngressSpecRuleHttpPathOutputReference",
    "IngressSpecRuleList",
    "IngressSpecRuleOutputReference",
    "IngressSpecTls",
    "IngressSpecTlsList",
    "IngressSpecTlsOutputReference",
    "IngressStatus",
    "IngressStatusList",
    "IngressStatusLoadBalancer",
    "IngressStatusLoadBalancerIngress",
    "IngressStatusLoadBalancerIngressList",
    "IngressStatusLoadBalancerIngressOutputReference",
    "IngressStatusLoadBalancerList",
    "IngressStatusLoadBalancerOutputReference",
    "IngressStatusOutputReference",
]

publication.publish()

def _typecheckingstub__e8006946bc35be32a62e96bff7c8ccc97043ea94a1a21e3def57cfadab6d69b9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[IngressMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressSpec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__56fe964bc28425fee2a37ceb739c40f974a4303b07b49b15af909cfa65bf167b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2eeac00b8f90a1c5bd831cb91403c10110e7542530ac887dc3311a5bcffbca2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84df8f9d7ee698e9f7f4fa00c49d87a6ce294c144c4348c7421d540db194748(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[IngressMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[IngressSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    wait_for_load_balancer: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8a79ba50376ed9849f1147224792b601b74e36aa9a4dc1a612da8fa86d383c8(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6259440d8dd9d319e8bf16554e7dc2d8331dbfe53f1d044cf0f7f3be340f3b67(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de22351605117716792774c642358fb4ca4b58f42b25a1fbf0fc4f9de6e2afc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c0c7113d6bc7612c1cae1f362523b5dc59b882bb5539050f6f9d1ec2159bb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce1d4dc78922e9d3cbc6ede722e49df8162b6842222f04b9565c83eda5305788(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b5af26a3653ec1dd706defa673ad1791d838d1f3a3e57a90c233f225a5a997a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d40cef1608c452e00910699057718ec97988497e630d8f2c39e7c05ae5c38966(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7992db5e36ce593f5bd75a8a0d9a78251e454ae54095a8bf436161c969ca02(
    value: typing.Optional[IngressMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3021c753777b65b88f43d3dcfff32c9379bf5d63293fadd0976b258f94e00af7(
    *,
    backend: typing.Optional[typing.Union[IngressSpecBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    ingress_class_name: typing.Optional[builtins.str] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tls: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecTls, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f280b41d733dcb167af41e720fce78f42c56aa6bc2fb406ebd008df2a96aa9d(
    *,
    service_name: typing.Optional[builtins.str] = None,
    service_port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b99641a6795d25451794131a009e0310a317178a70e0d29e0b358c92500924f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758bb3c1590681ec57fe0bdb27dc41afab0fd4123576d3ffc2d2479a246264d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e866c60d4c54f83a8aa8f922e18c93744ce4a6e821dac488d14f88654576b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ada5e7d455d90c7209896dcec6f962d746dc68906077cd24c3ea644cf8995c4(
    value: typing.Optional[IngressSpecBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebedb091f291628217ec62a6166734ccd102a4e1e591892588a75dda6872e8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41fed929b027eaea1337f2b9b19320ffdba213ce7871ee04889cbd57e84026e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2c6ae3b4d5c9118fe2c2a069a2364010ecd1c14db608c8d01bdfb85866f135(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecTls, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445fd0d25620b22b7a76a707b3445b02aa525bc08cc0f6d72b375c60e0f8ca54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8791fc8767395923eefb9f392b4ac9abb6d5865c20e58abb3907611ab3d094be(
    value: typing.Optional[IngressSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4ed0f224c7aa4dbdfadc3e9b54de344315b0b07a980af0aca7b1cc6388dfc8(
    *,
    http: typing.Union[IngressSpecRuleHttp, typing.Dict[builtins.str, typing.Any]],
    host: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee17d50cb5da7027171e28626ee1882f8cdbc364e4252c028794883c4c84172f(
    *,
    path: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__560efc853eac8e84778d4a02eadfb056fb8a1cb0e2ff7907dd4020bc931a1134(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5e6a6ac2a2f0424909fb97e6d3402f2129daec7bbad041de2f5490409de213(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IngressSpecRuleHttpPath, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fc2f836c2f1b0e04bf5273001ced20b9add5e4728f16d6d1e03df949d3ebcf6(
    value: typing.Optional[IngressSpecRuleHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e3824a2a1c595698ddeba39c11d317febbf1e86c8d0ce0d39ab63ca1b17ad7(
    *,
    backend: typing.Optional[typing.Union[IngressSpecRuleHttpPathBackend, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928b6a3b8cb622955865820f8b3f0692e64924367c6444b6d9aa00a725896bf3(
    *,
    service_name: typing.Optional[builtins.str] = None,
    service_port: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f908d64030b2c4eadf53dfb73f9042c41bfbd6808121146050b9deae820ae913(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b87b6a4beed05ef350c2b44a663730a3ecf67fcb5de8131d2e198098387eac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0e9a3b0efbbd237c7dd85c4d620cfbbbbc6218beb68eb0892a4f4fb12c6201(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a210225d219ad5eb91d507992ebf04aea72f56412872a6b5855bf860ee95a91c(
    value: typing.Optional[IngressSpecRuleHttpPathBackend],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff38f0276b352dd4c415e036b16946a34bc3defd436da4194ad9c8c4fadd7eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11eaeedf33e8ab5690ab7d1f4985119741dc21b87be74f813fe61e04961ed4c5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c430671af8fb83f01bc1fd2517a5db26eaef994a87a78cd1a67363cd76419c51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537bd161f24dba27cbe4f3d860c6190c4a52387119a8eda23175efc9380be947(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e931879d7bbaca0e65c1842353281f0872f0238472d76ce8767dcb7ea168364(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13af757bb5fa392d090c29b4757d1b8e4355d5359e15078ed44bea044ddb0ea9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRuleHttpPath]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956b0de1ed4fd021a294aafdbff1bf968c422baa6b230c0a7ef0dd9766000f45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb994420011d59f9d2b7c4cb29e0723bfc2d044ceb93078ecfa3ca8ce43b232(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13682c0a2fd67dcc4e08bc83ca1822f7de4025638d464e360ff3f341f1ff318(
    value: typing.Optional[typing.Union[IngressSpecRuleHttpPath, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf5f3ad56f8d3b8950efe223c634bb8859eb6dbbda35ff9ac12dddfdb95a739(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2716f669732ef30bfdd9e235ed864a94011d421611b66e788b8a54a01aa67fb9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a6f0d8d7de9192d6aec09ee52ab65a9ddd1708ac72580a17406b3d23b9a491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d49ac94067a688839a24db964a8230ba0fc649120f35165f64a4fc9052fa848(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dae9e10a82764cef7e049e98031ad906243507ee9ace88944e04f4a5f05b6369(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ad4a64e9bed1ed99a5c6071c16e376e555b5872dcd16f31cd351139eb73a8d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c12953100ce489271f324bf66c2e68a5adeb4c6d03d16328307eb6ef051cf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed213522dd0d7b0a36cea766a63121093817034ad8bc0bfdb941e4af1376d5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8945104ed1d7550f0edf947d3bf94eaefce8bbcf2da46dcceb2f0d08b7cf78c8(
    value: typing.Optional[typing.Union[IngressSpecRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2b5febd1bc3e4f74de6b36766b01e729113674394c0f0ebacbdeb11c5c8539(
    *,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e0681dc43b627cc7b8efa6589571fa50a5f36d97d126c5e102826430810961(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6dd3dc3c236e0a1e6bea62beea78cb6b5f280829edf19616a670a3c86638ec2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db4b4da996e506233c0af76ac3cca464f6b3d62c3c3790aa9e020b5bc5fad6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7702bfa718314adffe001a25493682a0b2d5028d86a4a36724ff06d1ee9770b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47b325b57ea81affa82ab8167f43a4c7ed904bae97ff47622c3d35c6185c845(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c42a49985037844bb48bcae2b732fb50e42a7046fe454e6554829f46af0298f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IngressSpecTls]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2098fa8c774abd6a4aba7cb485acbee4d1d7984c94f6bdcee72075e0a367f3f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4934c26edcc31c547def0d6b11c84f68e92058cda91174f511d64b6eb0ef4a86(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b0c4069d5dfd6db7fa077449578759edbb6fcd599870f77df2daec99c14a65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c854c1a2ea73afa3a96b0ea12979b59929e24407425f33e3387aa376624d75c9(
    value: typing.Optional[typing.Union[IngressSpecTls, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e6cb2b25a8e2657636ad4719e5dd725020b41217d973172b1787d30777c650(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afe008b1e109a749398ce50bc13cb7e2c2bcfaebcf83a64020d5228c3fb0ada(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ccd49c883a4c2b91199e237f815974a94aeebaa83b880281ac403ffa4536c44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7561261034e408e9105a5b02ea31817d585b59e9a068da24e0d93dc5939b7c5d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76b9f706d1c8326cefa9fc7e9a34250388dfcb9e14de4a413e3174286b1aad40(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285671b68acb000f0ce30dfb6e4206dcdb9047f2d7420e900549db2dad9c066c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ffcdc77e4f83cab9fc042d8dd91a20f989ca4d0d6762217c34dd07bb72a26f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__162aeaf6c5819ce111e411f4e79331c4ee2935c585449870e5bcd7b5b025374f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a44489468c0410ba9bdecd9425f178d921ad46a70a277860aee3240ce5b441e6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdcf194184beea76bd90ae937ea3c5f4b72d228fe204cca29df63d5ce615e481(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220494a9e56b971af7e77fa62620e698d168201e1f1c065fc782e99ed397e776(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69872fa8ee35e1d066bee9b4f8108eab0aabde9e33c3dfd19c34fa7f965c2cf2(
    value: typing.Optional[IngressStatusLoadBalancerIngress],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f67925bfd1b35d7e3ffda861ec18dcd8bccb0d05dd4b1431ffb5f81f16b442(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__025726fc2bac5b6818a28ca6a8823a1e1a0f7bdff70d522ee4a6171b4cacada3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0023e1991020320fbd2b74acec7f6fd9dbedf723fcb47ccda15948b49f16a2ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd673cd8545ee55d7352313407dddb5a9993507890bd116ab3e5f66ad6241001(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86a195d7a1793eb2b947a507983b6dad737ea44a27dec369173fab92a585945(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ba2a902c72319d0618e4e93e4a6276d8f932ca94af63a152a15b92145f6ca6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93be3d6981975a7ba3b03ca6655a42a1b0ba51d53be7a777870a313b1155fa4e(
    value: typing.Optional[IngressStatusLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__724ce90d8cb8a8258938a2d82d6445dff38c3a0382dec36903f4859aedefbaa6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc1fba3a2c45c909194e3e2a085e1fda0340c2bcaa0b5c3a19bfb23afff75fe(
    value: typing.Optional[IngressStatus],
) -> None:
    """Type checking stubs"""
    pass
