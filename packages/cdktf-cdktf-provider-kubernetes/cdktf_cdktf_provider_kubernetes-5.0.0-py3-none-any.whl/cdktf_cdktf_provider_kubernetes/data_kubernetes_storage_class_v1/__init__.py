'''
# `data_kubernetes_storage_class_v1`

Refer to the Terraform Registory for docs: [`data_kubernetes_storage_class_v1`](https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1).
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


class DataKubernetesStorageClassV1(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1 kubernetes_storage_class_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["DataKubernetesStorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        allowed_topologies: typing.Optional[typing.Union["DataKubernetesStorageClassV1AllowedTopologies", typing.Dict[builtins.str, typing.Any]]] = None,
        allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reclaim_policy: typing.Optional[builtins.str] = None,
        volume_binding_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1 kubernetes_storage_class_v1} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e015673d65707704333482bba9cc07b459f289bad6eb044b0489b0ec336d0653)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataKubernetesStorageClassV1Config(
            metadata=metadata,
            allowed_topologies=allowed_topologies,
            allow_volume_expansion=allow_volume_expansion,
            id=id,
            mount_options=mount_options,
            parameters=parameters,
            reclaim_policy=reclaim_policy,
            volume_binding_mode=volume_binding_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedTopologies")
    def put_allowed_topologies(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        value = DataKubernetesStorageClassV1AllowedTopologies(
            match_label_expressions=match_label_expressions
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedTopologies", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        value = DataKubernetesStorageClassV1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="resetAllowedTopologies")
    def reset_allowed_topologies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedTopologies", []))

    @jsii.member(jsii_name="resetAllowVolumeExpansion")
    def reset_allow_volume_expansion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowVolumeExpansion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetReclaimPolicy")
    def reset_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReclaimPolicy", []))

    @jsii.member(jsii_name="resetVolumeBindingMode")
    def reset_volume_binding_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeBindingMode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologies")
    def allowed_topologies(
        self,
    ) -> "DataKubernetesStorageClassV1AllowedTopologiesOutputReference":
        return typing.cast("DataKubernetesStorageClassV1AllowedTopologiesOutputReference", jsii.get(self, "allowedTopologies"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "DataKubernetesStorageClassV1MetadataOutputReference":
        return typing.cast("DataKubernetesStorageClassV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="storageProvisioner")
    def storage_provisioner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageProvisioner"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologiesInput")
    def allowed_topologies_input(
        self,
    ) -> typing.Optional["DataKubernetesStorageClassV1AllowedTopologies"]:
        return typing.cast(typing.Optional["DataKubernetesStorageClassV1AllowedTopologies"], jsii.get(self, "allowedTopologiesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVolumeExpansionInput")
    def allow_volume_expansion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowVolumeExpansionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["DataKubernetesStorageClassV1Metadata"]:
        return typing.cast(typing.Optional["DataKubernetesStorageClassV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicyInput")
    def reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeBindingModeInput")
    def volume_binding_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeBindingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowVolumeExpansion")
    def allow_volume_expansion(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowVolumeExpansion"))

    @allow_volume_expansion.setter
    def allow_volume_expansion(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9072b59d5efd8eb93cf6f4f3f51d5ce6dcc3758b7f859c31a4e81565247a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVolumeExpansion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee37f370435288ab2cc24a7a11c2ad0c0c97e3d6ca220f1a4aa8cc3377845050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__965169266df66f9e0327a259475c972287173b80158e519e7fc8a635cd754df3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b8625fbf32bd5fac420d4fafb2bdc881a5c229365be60137a8882263f83386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reclaimPolicy"))

    @reclaim_policy.setter
    def reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f1022985001d9095dae2fc925acf11781c39e92ab68b9e55698402893033f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="volumeBindingMode")
    def volume_binding_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeBindingMode"))

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca4395aa0135b155547a0895f6362fbb930ec044f7ebc7854292adbaddb0d24b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeBindingMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologies",
    jsii_struct_bases=[],
    name_mapping={"match_label_expressions": "matchLabelExpressions"},
)
class DataKubernetesStorageClassV1AllowedTopologies:
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad24f6f9735264bfb7a45aeade00a421bc0083f6b0426b54581c61a5107b34c)
            check_type(argname="argument match_label_expressions", value=match_label_expressions, expected_type=type_hints["match_label_expressions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_label_expressions is not None:
            self._values["match_label_expressions"] = match_label_expressions

    @builtins.property
    def match_label_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions"]]]:
        '''match_label_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#match_label_expressions DataKubernetesStorageClassV1#match_label_expressions}
        '''
        result = self._values.get("match_label_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1AllowedTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#key DataKubernetesStorageClassV1#key}
        :param values: An array of string values. One value must match the label to be selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#values DataKubernetesStorageClassV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adce044c5b8dc5e17b7ffa464d0aa0803a88f47bcef4f62a4c26b65f27ab1adc)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#key DataKubernetesStorageClassV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values. One value must match the label to be selected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#values DataKubernetesStorageClassV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8646e4106f88a4cc887cc7b55f2cb124fdcd92c330fdce97fd4edc8ee8120157)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8600ae129b3add8e6cb6410fbef445c490d51c37c71e6a2747609d231a3cc9a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6a553ce8cba01567b1b09223e2643a4c3acac259d147cd9ea08173d05f0e1d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4aa67a231a926b830decec1b1abc3aae6a82653b70f3f16279b134cfa9641842)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f7d077778e93c8c96d9c70d4136eb105435f02ab887338128f2dfcab6fc969a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f113d92ff2e2f6eabe615a565bd0c49acc53f9be45548b74f22e1e338f72addf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__732aa2741dc74360c06723d490e881af6c0ba4b214d8c6866d8da5d1a5dcb3a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__909c224f07ce5813677e23134793dab3fea031c6f37036473b9930fcbf224d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21565d7a4e75ff4737aacee1b3607b02bf982bd4d5a97733e22ee9553e48e036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73042bcfb64084eb74045fcada0b1c20993c9f8fbbfff4c272e5c61fadb3d3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataKubernetesStorageClassV1AllowedTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1AllowedTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efc2dd1ee5b3fad20b7abd920560b129d10ddf432efbd397d41ba14cb6362ad7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchLabelExpressions")
    def put_match_label_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cf260d5312e381fcd082b027bdadbaa4f92b389458038c9384101ad9108413a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchLabelExpressions", [value]))

    @jsii.member(jsii_name="resetMatchLabelExpressions")
    def reset_match_label_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabelExpressions", []))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressions")
    def match_label_expressions(
        self,
    ) -> DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList:
        return typing.cast(DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList, jsii.get(self, "matchLabelExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressionsInput")
    def match_label_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "matchLabelExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKubernetesStorageClassV1AllowedTopologies]:
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1AllowedTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesStorageClassV1AllowedTopologies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c273fae0e5cdb4fa5ee4c12ffa9f74247ee87cc9158dc10160620d0101e4b184)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1Config",
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
        "allowed_topologies": "allowedTopologies",
        "allow_volume_expansion": "allowVolumeExpansion",
        "id": "id",
        "mount_options": "mountOptions",
        "parameters": "parameters",
        "reclaim_policy": "reclaimPolicy",
        "volume_binding_mode": "volumeBindingMode",
    },
)
class DataKubernetesStorageClassV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["DataKubernetesStorageClassV1Metadata", typing.Dict[builtins.str, typing.Any]],
        allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reclaim_policy: typing.Optional[builtins.str] = None,
        volume_binding_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = DataKubernetesStorageClassV1Metadata(**metadata)
        if isinstance(allowed_topologies, dict):
            allowed_topologies = DataKubernetesStorageClassV1AllowedTopologies(**allowed_topologies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d991819812c0bcd87aed6ffa70ac0b1f9e5d9c420b1750e14810128fc037f6e9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument allowed_topologies", value=allowed_topologies, expected_type=type_hints["allowed_topologies"])
            check_type(argname="argument allow_volume_expansion", value=allow_volume_expansion, expected_type=type_hints["allow_volume_expansion"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument volume_binding_mode", value=volume_binding_mode, expected_type=type_hints["volume_binding_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
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
        if allowed_topologies is not None:
            self._values["allowed_topologies"] = allowed_topologies
        if allow_volume_expansion is not None:
            self._values["allow_volume_expansion"] = allow_volume_expansion
        if id is not None:
            self._values["id"] = id
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if parameters is not None:
            self._values["parameters"] = parameters
        if reclaim_policy is not None:
            self._values["reclaim_policy"] = reclaim_policy
        if volume_binding_mode is not None:
            self._values["volume_binding_mode"] = volume_binding_mode

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
    def metadata(self) -> "DataKubernetesStorageClassV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#metadata DataKubernetesStorageClassV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("DataKubernetesStorageClassV1Metadata", result)

    @builtins.property
    def allowed_topologies(
        self,
    ) -> typing.Optional[DataKubernetesStorageClassV1AllowedTopologies]:
        '''allowed_topologies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allowed_topologies DataKubernetesStorageClassV1#allowed_topologies}
        '''
        result = self._values.get("allowed_topologies")
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1AllowedTopologies], result)

    @builtins.property
    def allow_volume_expansion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the storage class allow volume expand.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#allow_volume_expansion DataKubernetesStorageClassV1#allow_volume_expansion}
        '''
        result = self._values.get("allow_volume_expansion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#id DataKubernetesStorageClassV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Persistent Volumes that are dynamically created by a storage class will have the mount options specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#mount_options DataKubernetesStorageClassV1#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The parameters for the provisioner that should create volumes of this storage class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#parameters DataKubernetesStorageClassV1#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of the reclaim policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#reclaim_policy DataKubernetesStorageClassV1#reclaim_policy}
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_binding_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates when volume binding and dynamic provisioning should occur.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#volume_binding_mode DataKubernetesStorageClassV1#volume_binding_mode}
        '''
        result = self._values.get("volume_binding_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class DataKubernetesStorageClassV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c78b7fa9224be69dcb1370592ad1b44db3ee0a14a06fe68a2a134086cb4b382)
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
        '''An unstructured key value map stored with the storage class that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#annotations DataKubernetesStorageClassV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the storage class.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#labels DataKubernetesStorageClassV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/d/storage_class_v1#name DataKubernetesStorageClassV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKubernetesStorageClassV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKubernetesStorageClassV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.dataKubernetesStorageClassV1.DataKubernetesStorageClassV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d55728b5e6107cda936c261857213629cc39b2b7c2e873e629c136bf505f5e44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1cb28eff8059a0fb23aed266c3e82a6066ecdcd858dbbb87eba02d13c722b40c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4a9d5f5faac81c8368f0541b5782eb0275a7b6dc6531801e87194804ae07d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b74d6e83a16a451d78d058f2dcbb43a4f383b71e21abda3be48cfe6e4b2c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataKubernetesStorageClassV1Metadata]:
        return typing.cast(typing.Optional[DataKubernetesStorageClassV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKubernetesStorageClassV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b924905a7d738ba70bcd4a8dd304b8c4e927dd9c82f69c7e05555b439165f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataKubernetesStorageClassV1",
    "DataKubernetesStorageClassV1AllowedTopologies",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsList",
    "DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressionsOutputReference",
    "DataKubernetesStorageClassV1AllowedTopologiesOutputReference",
    "DataKubernetesStorageClassV1Config",
    "DataKubernetesStorageClassV1Metadata",
    "DataKubernetesStorageClassV1MetadataOutputReference",
]

publication.publish()

def _typecheckingstub__e015673d65707704333482bba9cc07b459f289bad6eb044b0489b0ec336d0653(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[DataKubernetesStorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4d9072b59d5efd8eb93cf6f4f3f51d5ce6dcc3758b7f859c31a4e81565247a9f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee37f370435288ab2cc24a7a11c2ad0c0c97e3d6ca220f1a4aa8cc3377845050(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__965169266df66f9e0327a259475c972287173b80158e519e7fc8a635cd754df3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b8625fbf32bd5fac420d4fafb2bdc881a5c229365be60137a8882263f83386(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f1022985001d9095dae2fc925acf11781c39e92ab68b9e55698402893033f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca4395aa0135b155547a0895f6362fbb930ec044f7ebc7854292adbaddb0d24b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad24f6f9735264bfb7a45aeade00a421bc0083f6b0426b54581c61a5107b34c(
    *,
    match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adce044c5b8dc5e17b7ffa464d0aa0803a88f47bcef4f62a4c26b65f27ab1adc(
    *,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8646e4106f88a4cc887cc7b55f2cb124fdcd92c330fdce97fd4edc8ee8120157(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8600ae129b3add8e6cb6410fbef445c490d51c37c71e6a2747609d231a3cc9a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6a553ce8cba01567b1b09223e2643a4c3acac259d147cd9ea08173d05f0e1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa67a231a926b830decec1b1abc3aae6a82653b70f3f16279b134cfa9641842(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7d077778e93c8c96d9c70d4136eb105435f02ab887338128f2dfcab6fc969a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f113d92ff2e2f6eabe615a565bd0c49acc53f9be45548b74f22e1e338f72addf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732aa2741dc74360c06723d490e881af6c0ba4b214d8c6866d8da5d1a5dcb3a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909c224f07ce5813677e23134793dab3fea031c6f37036473b9930fcbf224d69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21565d7a4e75ff4737aacee1b3607b02bf982bd4d5a97733e22ee9553e48e036(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73042bcfb64084eb74045fcada0b1c20993c9f8fbbfff4c272e5c61fadb3d3c(
    value: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc2dd1ee5b3fad20b7abd920560b129d10ddf432efbd397d41ba14cb6362ad7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cf260d5312e381fcd082b027bdadbaa4f92b389458038c9384101ad9108413a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataKubernetesStorageClassV1AllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c273fae0e5cdb4fa5ee4c12ffa9f74247ee87cc9158dc10160620d0101e4b184(
    value: typing.Optional[DataKubernetesStorageClassV1AllowedTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d991819812c0bcd87aed6ffa70ac0b1f9e5d9c420b1750e14810128fc037f6e9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[DataKubernetesStorageClassV1Metadata, typing.Dict[builtins.str, typing.Any]],
    allowed_topologies: typing.Optional[typing.Union[DataKubernetesStorageClassV1AllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c78b7fa9224be69dcb1370592ad1b44db3ee0a14a06fe68a2a134086cb4b382(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55728b5e6107cda936c261857213629cc39b2b7c2e873e629c136bf505f5e44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb28eff8059a0fb23aed266c3e82a6066ecdcd858dbbb87eba02d13c722b40c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a9d5f5faac81c8368f0541b5782eb0275a7b6dc6531801e87194804ae07d08(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b74d6e83a16a451d78d058f2dcbb43a4f383b71e21abda3be48cfe6e4b2c58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b924905a7d738ba70bcd4a8dd304b8c4e927dd9c82f69c7e05555b439165f1(
    value: typing.Optional[DataKubernetesStorageClassV1Metadata],
) -> None:
    """Type checking stubs"""
    pass
