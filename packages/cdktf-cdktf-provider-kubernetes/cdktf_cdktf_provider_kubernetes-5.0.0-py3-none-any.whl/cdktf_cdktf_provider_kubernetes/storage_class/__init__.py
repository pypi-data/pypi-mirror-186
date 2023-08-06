'''
# `kubernetes_storage_class`

Refer to the Terraform Registory for docs: [`kubernetes_storage_class`](https://www.terraform.io/docs/providers/kubernetes/r/storage_class).
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


class StorageClass(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClass",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class kubernetes_storage_class}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["StorageClassMetadata", typing.Dict[builtins.str, typing.Any]],
        storage_provisioner: builtins.str,
        allowed_topologies: typing.Optional[typing.Union["StorageClassAllowedTopologies", typing.Dict[builtins.str, typing.Any]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class kubernetes_storage_class} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#metadata StorageClass#metadata}
        :param storage_provisioner: Indicates the type of the provisioner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#storage_provisioner StorageClass#storage_provisioner}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allowed_topologies StorageClass#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allow_volume_expansion StorageClass#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#id StorageClass#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#mount_options StorageClass#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#parameters StorageClass#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#reclaim_policy StorageClass#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#volume_binding_mode StorageClass#volume_binding_mode}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad8cdeb139fb30017457a1dfc6f3cc81777eea5c181c2e2a493f3f1abce479c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageClassConfig(
            metadata=metadata,
            storage_provisioner=storage_provisioner,
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
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageClassAllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#match_label_expressions StorageClass#match_label_expressions}
        '''
        value = StorageClassAllowedTopologies(
            match_label_expressions=match_label_expressions
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedTopologies", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#annotations StorageClass#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#generate_name StorageClass#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#labels StorageClass#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#name StorageClass#name}
        '''
        value = StorageClassMetadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
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
    def allowed_topologies(self) -> "StorageClassAllowedTopologiesOutputReference":
        return typing.cast("StorageClassAllowedTopologiesOutputReference", jsii.get(self, "allowedTopologies"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "StorageClassMetadataOutputReference":
        return typing.cast("StorageClassMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="allowedTopologiesInput")
    def allowed_topologies_input(
        self,
    ) -> typing.Optional["StorageClassAllowedTopologies"]:
        return typing.cast(typing.Optional["StorageClassAllowedTopologies"], jsii.get(self, "allowedTopologiesInput"))

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
    def metadata_input(self) -> typing.Optional["StorageClassMetadata"]:
        return typing.cast(typing.Optional["StorageClassMetadata"], jsii.get(self, "metadataInput"))

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
    @jsii.member(jsii_name="storageProvisionerInput")
    def storage_provisioner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageProvisionerInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__80a80ef2d590858ea99963bd221c3e184afc251488c38e0d27e1483cdb77e30b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVolumeExpansion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2633285456a283c150e1fef0372d051088a3e5b30268913ddbe93ec6c86e890d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc964ecc011c920e446326508ea4c192cd6943202b33fca2bb050dde1a202223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4adcf92743817d6b65eeaa6768175df01f3360882c080c56f4eeaad7f014e0ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="reclaimPolicy")
    def reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reclaimPolicy"))

    @reclaim_policy.setter
    def reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabfc38888986d561b4bf61d80b80e03121c94d1a25c2c9c9ef97a411e912d48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageProvisioner")
    def storage_provisioner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageProvisioner"))

    @storage_provisioner.setter
    def storage_provisioner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3471ea874d1b939ebc10bf33fe7b09aa5f31460fc6782cd8c2ab8087a12e832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageProvisioner", value)

    @builtins.property
    @jsii.member(jsii_name="volumeBindingMode")
    def volume_binding_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeBindingMode"))

    @volume_binding_mode.setter
    def volume_binding_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429be33d8032d892ed6b611f1400d9f961b46aacfaa306498fb9a24454b9aa4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeBindingMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassAllowedTopologies",
    jsii_struct_bases=[],
    name_mapping={"match_label_expressions": "matchLabelExpressions"},
)
class StorageClassAllowedTopologies:
    def __init__(
        self,
        *,
        match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageClassAllowedTopologiesMatchLabelExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_label_expressions: match_label_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#match_label_expressions StorageClass#match_label_expressions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77de7f67e6cba82c5208c2cc05563477af106c613581617d804fe375fb0dacfb)
            check_type(argname="argument match_label_expressions", value=match_label_expressions, expected_type=type_hints["match_label_expressions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_label_expressions is not None:
            self._values["match_label_expressions"] = match_label_expressions

    @builtins.property
    def match_label_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageClassAllowedTopologiesMatchLabelExpressions"]]]:
        '''match_label_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#match_label_expressions StorageClass#match_label_expressions}
        '''
        result = self._values.get("match_label_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageClassAllowedTopologiesMatchLabelExpressions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassAllowedTopologies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassAllowedTopologiesMatchLabelExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class StorageClassAllowedTopologiesMatchLabelExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#key StorageClass#key}
        :param values: An array of string values. One value must match the label to be selected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#values StorageClass#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61bb143ab52abab7354287a81c2f23d9e4da9e600dab02654a8d0ebf031c6b0a)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#key StorageClass#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values. One value must match the label to be selected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#values StorageClass#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassAllowedTopologiesMatchLabelExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageClassAllowedTopologiesMatchLabelExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassAllowedTopologiesMatchLabelExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24019504b4821d336c768b0e4a8a4f864480c35b7d0147761d1672fae938b274)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageClassAllowedTopologiesMatchLabelExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c05ebeadf2d4d7534762141be79a967083b6dc8dcf5622958691b3d9196c9a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageClassAllowedTopologiesMatchLabelExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51bab584cc8471f225c2856afc26f300c5d56954f45c1246266fa47173a2c964)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e94529a5eaa17530d4a8043b88a2437f0451fe1826180248e98ccd9b64622a4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3be14ecb31f02c2fd3b15a362c364f8f424ddad8bdd644c858137d21ed012ddd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__779159ae2d97465094ea8a3d5fd5dc7d090cd74e890ba7dac95f2b1fd898b787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageClassAllowedTopologiesMatchLabelExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassAllowedTopologiesMatchLabelExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce043b3648225d7fc1f9a13cfb064b80494f69cbd41afeeb06df000949a04819)
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
            type_hints = typing.get_type_hints(_typecheckingstub__434e4a942c5748b556ce84b914dea050545382582805377a443a6e54ec20c0d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c420c4e1aad05f0fc4b60591202a752ff46dd3af396beeb8e2e7b8c2ebd1694)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89c73b42762ffcdd93e7236e680956669ad0d1d7acb283c25ad2ba62e27566f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageClassAllowedTopologiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassAllowedTopologiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbb2c7c0c2e006929d8bb49d19867658ed4ceb54436edf74041a221628649b7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchLabelExpressions")
    def put_match_label_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e929fe86dc69170158f6a0c6463440960fe12e3a335f9861b0b77f8889b104bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchLabelExpressions", [value]))

    @jsii.member(jsii_name="resetMatchLabelExpressions")
    def reset_match_label_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabelExpressions", []))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressions")
    def match_label_expressions(
        self,
    ) -> StorageClassAllowedTopologiesMatchLabelExpressionsList:
        return typing.cast(StorageClassAllowedTopologiesMatchLabelExpressionsList, jsii.get(self, "matchLabelExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelExpressionsInput")
    def match_label_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]], jsii.get(self, "matchLabelExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageClassAllowedTopologies]:
        return typing.cast(typing.Optional[StorageClassAllowedTopologies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageClassAllowedTopologies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ff10da82bd446007c2e89b9faf42bbac45a39b0fda2e2dec65f8dcf8a6bf9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassConfig",
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
        "storage_provisioner": "storageProvisioner",
        "allowed_topologies": "allowedTopologies",
        "allow_volume_expansion": "allowVolumeExpansion",
        "id": "id",
        "mount_options": "mountOptions",
        "parameters": "parameters",
        "reclaim_policy": "reclaimPolicy",
        "volume_binding_mode": "volumeBindingMode",
    },
)
class StorageClassConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["StorageClassMetadata", typing.Dict[builtins.str, typing.Any]],
        storage_provisioner: builtins.str,
        allowed_topologies: typing.Optional[typing.Union[StorageClassAllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#metadata StorageClass#metadata}
        :param storage_provisioner: Indicates the type of the provisioner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#storage_provisioner StorageClass#storage_provisioner}
        :param allowed_topologies: allowed_topologies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allowed_topologies StorageClass#allowed_topologies}
        :param allow_volume_expansion: Indicates whether the storage class allow volume expand. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allow_volume_expansion StorageClass#allow_volume_expansion}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#id StorageClass#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mount_options: Persistent Volumes that are dynamically created by a storage class will have the mount options specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#mount_options StorageClass#mount_options}
        :param parameters: The parameters for the provisioner that should create volumes of this storage class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#parameters StorageClass#parameters}
        :param reclaim_policy: Indicates the type of the reclaim policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#reclaim_policy StorageClass#reclaim_policy}
        :param volume_binding_mode: Indicates when volume binding and dynamic provisioning should occur. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#volume_binding_mode StorageClass#volume_binding_mode}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = StorageClassMetadata(**metadata)
        if isinstance(allowed_topologies, dict):
            allowed_topologies = StorageClassAllowedTopologies(**allowed_topologies)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70118fee325a80bb2222a20c4f86f1117f9146cb392758a8681719b90a0ba8d5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument storage_provisioner", value=storage_provisioner, expected_type=type_hints["storage_provisioner"])
            check_type(argname="argument allowed_topologies", value=allowed_topologies, expected_type=type_hints["allowed_topologies"])
            check_type(argname="argument allow_volume_expansion", value=allow_volume_expansion, expected_type=type_hints["allow_volume_expansion"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument reclaim_policy", value=reclaim_policy, expected_type=type_hints["reclaim_policy"])
            check_type(argname="argument volume_binding_mode", value=volume_binding_mode, expected_type=type_hints["volume_binding_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "storage_provisioner": storage_provisioner,
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
    def metadata(self) -> "StorageClassMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#metadata StorageClass#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("StorageClassMetadata", result)

    @builtins.property
    def storage_provisioner(self) -> builtins.str:
        '''Indicates the type of the provisioner.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#storage_provisioner StorageClass#storage_provisioner}
        '''
        result = self._values.get("storage_provisioner")
        assert result is not None, "Required property 'storage_provisioner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_topologies(self) -> typing.Optional[StorageClassAllowedTopologies]:
        '''allowed_topologies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allowed_topologies StorageClass#allowed_topologies}
        '''
        result = self._values.get("allowed_topologies")
        return typing.cast(typing.Optional[StorageClassAllowedTopologies], result)

    @builtins.property
    def allow_volume_expansion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Indicates whether the storage class allow volume expand.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#allow_volume_expansion StorageClass#allow_volume_expansion}
        '''
        result = self._values.get("allow_volume_expansion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#id StorageClass#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Persistent Volumes that are dynamically created by a storage class will have the mount options specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#mount_options StorageClass#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The parameters for the provisioner that should create volumes of this storage class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#parameters StorageClass#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of the reclaim policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#reclaim_policy StorageClass#reclaim_policy}
        '''
        result = self._values.get("reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_binding_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates when volume binding and dynamic provisioning should occur.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#volume_binding_mode StorageClass#volume_binding_mode}
        '''
        result = self._values.get("volume_binding_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class StorageClassMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the storage class that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#annotations StorageClass#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#generate_name StorageClass#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the storage class. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#labels StorageClass#labels}
        :param name: Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#name StorageClass#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44708c757fdecdce8bd3b62f640da4f52a89bc52dd9f872fe15629444410649b)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#annotations StorageClass#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#generate_name StorageClass#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the storage class.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#labels StorageClass#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the storage class, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/storage_class#name StorageClass#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClassMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageClassMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.storageClass.StorageClassMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58a5ae871412513054338aad0cc1ecd9831a8e0d9b97db715af1eac0946b71ed)
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
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645d992ebc92e805088a99b4f00d2bb5a68e69aded98539f38eddf9997915fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30e5b1d2f9b4cb94252edb9f920361b324899dea4ca10cc340a5d329001fa709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5131d6662902d8d73a10d38322dd0f1a664c6952c8502af0ca6689c4fb533c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c1900f152f0bc798c8126f253379fd0a088821636ea727950cf6376319459d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageClassMetadata]:
        return typing.cast(typing.Optional[StorageClassMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageClassMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab29ed8d53b2abc4e5d3b6423e041f8ecef5633c6c2725625ed0d1d00353e1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageClass",
    "StorageClassAllowedTopologies",
    "StorageClassAllowedTopologiesMatchLabelExpressions",
    "StorageClassAllowedTopologiesMatchLabelExpressionsList",
    "StorageClassAllowedTopologiesMatchLabelExpressionsOutputReference",
    "StorageClassAllowedTopologiesOutputReference",
    "StorageClassConfig",
    "StorageClassMetadata",
    "StorageClassMetadataOutputReference",
]

publication.publish()

def _typecheckingstub__4ad8cdeb139fb30017457a1dfc6f3cc81777eea5c181c2e2a493f3f1abce479c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[StorageClassMetadata, typing.Dict[builtins.str, typing.Any]],
    storage_provisioner: builtins.str,
    allowed_topologies: typing.Optional[typing.Union[StorageClassAllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__80a80ef2d590858ea99963bd221c3e184afc251488c38e0d27e1483cdb77e30b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2633285456a283c150e1fef0372d051088a3e5b30268913ddbe93ec6c86e890d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc964ecc011c920e446326508ea4c192cd6943202b33fca2bb050dde1a202223(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4adcf92743817d6b65eeaa6768175df01f3360882c080c56f4eeaad7f014e0ab(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabfc38888986d561b4bf61d80b80e03121c94d1a25c2c9c9ef97a411e912d48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3471ea874d1b939ebc10bf33fe7b09aa5f31460fc6782cd8c2ab8087a12e832(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429be33d8032d892ed6b611f1400d9f961b46aacfaa306498fb9a24454b9aa4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77de7f67e6cba82c5208c2cc05563477af106c613581617d804fe375fb0dacfb(
    *,
    match_label_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bb143ab52abab7354287a81c2f23d9e4da9e600dab02654a8d0ebf031c6b0a(
    *,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24019504b4821d336c768b0e4a8a4f864480c35b7d0147761d1672fae938b274(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c05ebeadf2d4d7534762141be79a967083b6dc8dcf5622958691b3d9196c9a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51bab584cc8471f225c2856afc26f300c5d56954f45c1246266fa47173a2c964(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94529a5eaa17530d4a8043b88a2437f0451fe1826180248e98ccd9b64622a4b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be14ecb31f02c2fd3b15a362c364f8f424ddad8bdd644c858137d21ed012ddd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__779159ae2d97465094ea8a3d5fd5dc7d090cd74e890ba7dac95f2b1fd898b787(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageClassAllowedTopologiesMatchLabelExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce043b3648225d7fc1f9a13cfb064b80494f69cbd41afeeb06df000949a04819(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434e4a942c5748b556ce84b914dea050545382582805377a443a6e54ec20c0d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c420c4e1aad05f0fc4b60591202a752ff46dd3af396beeb8e2e7b8c2ebd1694(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89c73b42762ffcdd93e7236e680956669ad0d1d7acb283c25ad2ba62e27566f(
    value: typing.Optional[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb2c7c0c2e006929d8bb49d19867658ed4ceb54436edf74041a221628649b7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e929fe86dc69170158f6a0c6463440960fe12e3a335f9861b0b77f8889b104bd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageClassAllowedTopologiesMatchLabelExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ff10da82bd446007c2e89b9faf42bbac45a39b0fda2e2dec65f8dcf8a6bf9b8(
    value: typing.Optional[StorageClassAllowedTopologies],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70118fee325a80bb2222a20c4f86f1117f9146cb392758a8681719b90a0ba8d5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[StorageClassMetadata, typing.Dict[builtins.str, typing.Any]],
    storage_provisioner: builtins.str,
    allowed_topologies: typing.Optional[typing.Union[StorageClassAllowedTopologies, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_volume_expansion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reclaim_policy: typing.Optional[builtins.str] = None,
    volume_binding_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44708c757fdecdce8bd3b62f640da4f52a89bc52dd9f872fe15629444410649b(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a5ae871412513054338aad0cc1ecd9831a8e0d9b97db715af1eac0946b71ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645d992ebc92e805088a99b4f00d2bb5a68e69aded98539f38eddf9997915fce(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e5b1d2f9b4cb94252edb9f920361b324899dea4ca10cc340a5d329001fa709(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5131d6662902d8d73a10d38322dd0f1a664c6952c8502af0ca6689c4fb533c2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c1900f152f0bc798c8126f253379fd0a088821636ea727950cf6376319459d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab29ed8d53b2abc4e5d3b6423e041f8ecef5633c6c2725625ed0d1d00353e1e(
    value: typing.Optional[StorageClassMetadata],
) -> None:
    """Type checking stubs"""
    pass
