'''
# `kubernetes_persistent_volume`

Refer to the Terraform Registory for docs: [`kubernetes_persistent_volume`](https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume).
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


class PersistentVolume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume kubernetes_persistent_volume}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PersistentVolumeMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume kubernetes_persistent_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571dd23064a9e6f8f4fde39c1213906f742ee4d62430ed15c094e6f1790b840f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PersistentVolumeConfig(
            metadata=metadata,
            spec=spec,
            id=id,
            timeouts=timeouts,
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
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        value = PersistentVolumeMetadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda466cca8a7fcb2b33fec35d3cb2a8560d11aa85bc45b27a77b20a5bffbfa32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.
        '''
        value = PersistentVolumeTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "PersistentVolumeMetadataOutputReference":
        return typing.cast("PersistentVolumeMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PersistentVolumeSpecList":
        return typing.cast("PersistentVolumeSpecList", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PersistentVolumeTimeoutsOutputReference":
        return typing.cast("PersistentVolumeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PersistentVolumeMetadata"]:
        return typing.cast(typing.Optional["PersistentVolumeMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PersistentVolumeTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PersistentVolumeTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb98d2bfdec1563422506a47f82cea3c89784f25355629edcc9d8c727c818095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeConfig",
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
        "timeouts": "timeouts",
    },
)
class PersistentVolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["PersistentVolumeMetadata", typing.Dict[builtins.str, typing.Any]],
        spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpec", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PersistentVolumeMetadata(**metadata)
        if isinstance(timeouts, dict):
            timeouts = PersistentVolumeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3763e04ed0b9162049c4fdf0868462a60fa9484be5fd4d58cdcdc9b48bea4380)
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
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def metadata(self) -> "PersistentVolumeMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#metadata PersistentVolume#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PersistentVolumeMetadata", result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#spec PersistentVolume#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpec"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#id PersistentVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PersistentVolumeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#timeouts PersistentVolume#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PersistentVolumeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PersistentVolumeMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__809244eb2703375b712200509b3fecacb4c136175bffe83d138db59d505dadc1)
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
        '''An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#annotations PersistentVolume#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#labels PersistentVolume#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a87998f2bcc1fcf14c5c13902f3a4c2bfc57d22308db9336ad2ff1ea7c8ecba2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29c1096409656cb711a76177bc7a8877fda32abc886723e418fb3c722b867ce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9bd23d14ccc68d2f5353e427212fa97a9e21edeb5c32e0e3fb9ab4d39f0928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72caba99d9149c927b2f54542fe0670f2de1ddc782cf00c9b77d3ab8c7f829f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeMetadata]:
        return typing.cast(typing.Optional[PersistentVolumeMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PersistentVolumeMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ededf8c469827b7f85796fb8533671d2e0ee1eadb92c145159815c7c960daac3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpec",
    jsii_struct_bases=[],
    name_mapping={
        "access_modes": "accessModes",
        "capacity": "capacity",
        "persistent_volume_source": "persistentVolumeSource",
        "claim_ref": "claimRef",
        "mount_options": "mountOptions",
        "node_affinity": "nodeAffinity",
        "persistent_volume_reclaim_policy": "persistentVolumeReclaimPolicy",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeSpec:
    def __init__(
        self,
        *,
        access_modes: typing.Sequence[builtins.str],
        capacity: typing.Mapping[builtins.str, builtins.str],
        persistent_volume_source: typing.Union["PersistentVolumeSpecPersistentVolumeSource", typing.Dict[builtins.str, typing.Any]],
        claim_ref: typing.Optional[typing.Union["PersistentVolumeSpecClaimRef", typing.Dict[builtins.str, typing.Any]]] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_affinity: typing.Optional[typing.Union["PersistentVolumeSpecNodeAffinity", typing.Dict[builtins.str, typing.Any]]] = None,
        persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_modes: Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#access_modes PersistentVolume#access_modes}
        :param capacity: A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#capacity PersistentVolume#capacity}
        :param persistent_volume_source: persistent_volume_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_source PersistentVolume#persistent_volume_source}
        :param claim_ref: claim_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#claim_ref PersistentVolume#claim_ref}
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#mount_options PersistentVolume#mount_options}
        :param node_affinity: node_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_affinity PersistentVolume#node_affinity}
        :param persistent_volume_reclaim_policy: What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_reclaim_policy PersistentVolume#persistent_volume_reclaim_policy}
        :param storage_class_name: A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#storage_class_name PersistentVolume#storage_class_name}
        :param volume_mode: Defines if a volume is intended to be used with a formatted filesystem. or to remain in raw block state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_mode PersistentVolume#volume_mode}
        '''
        if isinstance(persistent_volume_source, dict):
            persistent_volume_source = PersistentVolumeSpecPersistentVolumeSource(**persistent_volume_source)
        if isinstance(claim_ref, dict):
            claim_ref = PersistentVolumeSpecClaimRef(**claim_ref)
        if isinstance(node_affinity, dict):
            node_affinity = PersistentVolumeSpecNodeAffinity(**node_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd456ef86f01d297f8d4582fbfe979914f880df2ac4871331601a874e8311d6b)
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument persistent_volume_source", value=persistent_volume_source, expected_type=type_hints["persistent_volume_source"])
            check_type(argname="argument claim_ref", value=claim_ref, expected_type=type_hints["claim_ref"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument persistent_volume_reclaim_policy", value=persistent_volume_reclaim_policy, expected_type=type_hints["persistent_volume_reclaim_policy"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_modes": access_modes,
            "capacity": capacity,
            "persistent_volume_source": persistent_volume_source,
        }
        if claim_ref is not None:
            self._values["claim_ref"] = claim_ref
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if persistent_volume_reclaim_policy is not None:
            self._values["persistent_volume_reclaim_policy"] = persistent_volume_reclaim_policy
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def access_modes(self) -> typing.List[builtins.str]:
        '''Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#access_modes PersistentVolume#access_modes}
        '''
        result = self._values.get("access_modes")
        assert result is not None, "Required property 'access_modes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#capacity PersistentVolume#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def persistent_volume_source(self) -> "PersistentVolumeSpecPersistentVolumeSource":
        '''persistent_volume_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_source PersistentVolume#persistent_volume_source}
        '''
        result = self._values.get("persistent_volume_source")
        assert result is not None, "Required property 'persistent_volume_source' is missing"
        return typing.cast("PersistentVolumeSpecPersistentVolumeSource", result)

    @builtins.property
    def claim_ref(self) -> typing.Optional["PersistentVolumeSpecClaimRef"]:
        '''claim_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#claim_ref PersistentVolume#claim_ref}
        '''
        result = self._values.get("claim_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecClaimRef"], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#mount_options PersistentVolume#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_affinity(self) -> typing.Optional["PersistentVolumeSpecNodeAffinity"]:
        '''node_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_affinity PersistentVolume#node_affinity}
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinity"], result)

    @builtins.property
    def persistent_volume_reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''What happens to a persistent volume when released from its claim.

        Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#persistent_volume_reclaim_policy PersistentVolume#persistent_volume_reclaim_policy}
        '''
        result = self._values.get("persistent_volume_reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#storage_class_name PersistentVolume#storage_class_name}
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[builtins.str]:
        '''Defines if a volume is intended to be used with a formatted filesystem.

        or to remain in raw block state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_mode PersistentVolume#volume_mode}
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecClaimRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecClaimRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e602117492fb7da813a6ca33a3dc82851025a2b3748e4959513eea35269784)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the PersistentVolumeClaim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecClaimRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecClaimRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecClaimRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__290a5aa558d8f77628371cb696994826a4749b9aaa16075a79dfc04205aa9313)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a7fe8ff486bd4179bf781142b9d2b4e65e2bc43444d52b70ea84aadfb9acac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7876f9e8ee39f4ee35b4a640d60d3f8d5c8c7a07599e485de8993dc3487b8be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeSpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecClaimRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecClaimRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__951fd510abfa1b85f5df9a45ce5cdd0ed341e30ea9513fc6f3a2b0f31544b1e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d9f33074c60369c9bd9b89942a66bdd666459d92ae41977075007b9b6743ffb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PersistentVolumeSpecOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8249d312b88855e850334468f3de4f0f7179f6813ea063180f65702ac37345cb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceb320d250f2024e0982107937a730f02dd6ae456a2c2cfadb8c7d1b63fcf414)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e81c735e2ed7c87fe0650df5f6eae2acb042fd8854f63cc09c18d1e574e341cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1df872801007d2a8372d1627df9ebda3fbd03c0c171b8bd59073a3921b9e225d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5720e81642e60e6380b569a2e01a55573838b47706b18a71f6b49b711e1d521e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class PersistentVolumeSpecNodeAffinity:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["PersistentVolumeSpecNodeAffinityRequired", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        if isinstance(required, dict):
            required = PersistentVolumeSpecNodeAffinityRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6fb2d6174789e0dadfb2d39affa73fe6f4f4c69656a2282e0db9770c70b35d)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional["PersistentVolumeSpecNodeAffinityRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinityRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dab5d7f2eea301d264274e0052d52726e7df232187f4ff1062bfb2ca5e2be684)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        value = PersistentVolumeSpecNodeAffinityRequired(
            node_selector_term=node_selector_term
        )

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "PersistentVolumeSpecNodeAffinityRequiredOutputReference":
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecNodeAffinityRequired"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecNodeAffinityRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeSpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecNodeAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2703aa257f17eb55e23215b42c6ae6f82cabfadac815b1caca7528ef9a46818f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequired",
    jsii_struct_bases=[],
    name_mapping={"node_selector_term": "nodeSelectorTerm"},
)
class PersistentVolumeSpecNodeAffinityRequired:
    def __init__(
        self,
        *,
        node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd327867005215322bcef988af50289e5d26763d00d8a99f5290262ef89ed31)
            check_type(argname="argument node_selector_term", value=node_selector_term, expected_type=type_hints["node_selector_term"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_selector_term": node_selector_term,
        }

    @builtins.property
    def node_selector_term(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm"]]:
        '''node_selector_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_selector_term PersistentVolume#node_selector_term}
        '''
        result = self._values.get("node_selector_term")
        assert result is not None, "Required property 'node_selector_term' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_expressions PersistentVolume#match_expressions}
        :param match_fields: match_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_fields PersistentVolume#match_fields}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841c458ceeb7b87a7850fa92512b1321b3f842bbc08415a8dd9059efaaa22856)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_expressions PersistentVolume#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]]:
        '''match_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#match_fields PersistentVolume#match_fields}
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4df4d83b749296b7d590bd68cd38b019184f303fbfa8bccedb70ebbc16d27de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72aaa65a90b870a3435cc8a545fbd37e3686509399ef768684302a8563592acd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a18ad697e3c0ce1f48e3f4c09b74e7df2bcae1da4b4cf4083a1ca573340c26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbcab2c4ee80e48a1b0b9258bf99b6bbf2fe1037b1a0412d12ce95ff9d2960ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7e6b628d5176dfb240ef573f7497384d2f9954bc5b6bc9b8b2025a534d3f97f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2cdc3340d2109a3343aea7c1901b33135e5a37e41e0dc2b5e9e86c6823e4cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e490a3a17f1a72e443a794f6e400e1c982b23e81fbf62ab2024d46535ddad7)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__735bbc6e66eff740f5bac171f5295c9d9a52692f62b55daef48072d5cb49db3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928266139e4f536830eefc01c1bc868791e4226cd21e46c842ef4ea72ee4a74b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57387b6f7d631a9c1f234cf5bfc1816dd176480bcb171b4b4e31a00719573380)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c75b1981f0e480c78f9e44bdf410ae7e6ed31e3cac78516bd37e3b32a9518238)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b0206ec7f0d1381af7d5282f6d162ca90643b4a4f84a9a0cced0cfd15d33aa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b31928962bd453d5e6925c30eb884e5386695006f115d68ead9013a6b4c468e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ff0eb73ce28b79bd31e8db79a5e6cac19e98fff86ce261546a17e1349286f96)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__3ddf162a7e206ecad9efdb2aa887c2bfcfda209977d4e54fc3c15ea857c284b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d4344eb696d9d46c6a3c409a0a95711b419ba03bf4b7f5ddc89927bcaa27ec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f13370a2379d2e0a4ead372b0d556923c537691740ae8f47d7c0a8613031e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459b3a73627354ebbc4191aea48dd7e9ad8778b09e64d0b29eca5bf03a30e04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c680a3ab1c1645de5093b59c917f8e5ecd7e240679866c08ccdae1d3fea34d47)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#key PersistentVolume#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#operator PersistentVolume#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#values PersistentVolume#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48884470f555763d8ed42d6ca10df23daf47ef7f64a613495874438af44c5106)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c72cbf74334c4e0e2b4c2221a784cfe38bd35e56d26710d2897ab211db9ac18)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19f467968ef149e872c1d17b5077236ce64db53c119e94d466f3c79f127e9b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a252e10d0e6d72a4b870bde47ad55cd6d5082135622bb89b04609a5ebfd1ee2f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b8bd4c38d461fe569df453bc389b813700bd13f573d7c34b70720cd0bf53eb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c48c813f9c1cd6c87eb875a5356cbc6ff4e9587f1a8739cf23688e3543afce5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3eabc23768f7824d0d59fcbb4850ef9f33ac79c9f34dc76c15bde118f1bb3cb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__8cd1654989a3c665ff3a77b511ca3b6145ccdc0454c1fb70fbcdcb4e1be2d0cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ecddaf7dcc61a4eeb58a6df00093d6e768c83b25937da109eabb1e827573749)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__138f26c2e5db920c9fdf35522e5a6798a002203d79f9f82f88985ddf1aeb12c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c192035360585fbd6b014e3a620acbccd85ef2996fc7cdfb760c6c518514430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__325f9f5050d852167f5822e8390750a0e0f8d6943fd622aa675bd4d0d88457f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8be17e70968408bcc213fe4a5073242b57fdaec6093b1812bb6bc3c7682ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="putMatchFields")
    def put_match_fields(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf28f0567f1d3d2e6778842018c29192771a4e3bd50653d92b5b0d1825404e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchFields", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchFields")
    def reset_match_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchFields", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchFields")
    def match_fields(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, jsii.get(self, "matchFields"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchFieldsInput")
    def match_fields_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "matchFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a45eca8f2e352c3fce7698183629fbfd302a4a2249bf361b2b636f8032d1eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecNodeAffinityRequiredOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecNodeAffinityRequiredOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f41f4c623f4ac0bec5d4fb32a7a70ad7903ccfd795c3599b5bce2e80c87fcf42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeSelectorTerm")
    def put_node_selector_term(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa01a710f30e125c46800fc9b04914984059fb8586acea30eee92d7e92627a75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeSelectorTerm", [value]))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTerm")
    def node_selector_term(
        self,
    ) -> PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList:
        return typing.cast(PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList, jsii.get(self, "nodeSelectorTerm"))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTermInput")
    def node_selector_term_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "nodeSelectorTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecNodeAffinityRequired]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinityRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecNodeAffinityRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33cf927ea2dd9fe0f8eeaa5a80661b349d350ce27f3f7fdae4131e4fb2561b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57088624504c449ea6614aebde35b5418b418fe1e5b3d1dcde4f96c56a8eef95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClaimRef")
    def put_claim_ref(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecClaimRef(name=name, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putClaimRef", [value]))

    @jsii.member(jsii_name="putNodeAffinity")
    def put_node_affinity(
        self,
        *,
        required: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#required PersistentVolume#required}
        '''
        value = PersistentVolumeSpecNodeAffinity(required=required)

        return typing.cast(None, jsii.invoke(self, "putNodeAffinity", [value]))

    @jsii.member(jsii_name="putPersistentVolumeSource")
    def put_persistent_volume_source(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        value = PersistentVolumeSpecPersistentVolumeSource(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            ceph_fs=ceph_fs,
            cinder=cinder,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            nfs=nfs,
            photon_persistent_disk=photon_persistent_disk,
            quobyte=quobyte,
            rbd=rbd,
            vsphere_volume=vsphere_volume,
        )

        return typing.cast(None, jsii.invoke(self, "putPersistentVolumeSource", [value]))

    @jsii.member(jsii_name="resetClaimRef")
    def reset_claim_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRef", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNodeAffinity")
    def reset_node_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAffinity", []))

    @jsii.member(jsii_name="resetPersistentVolumeReclaimPolicy")
    def reset_persistent_volume_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistentVolumeReclaimPolicy", []))

    @jsii.member(jsii_name="resetStorageClassName")
    def reset_storage_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassName", []))

    @jsii.member(jsii_name="resetVolumeMode")
    def reset_volume_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeMode", []))

    @builtins.property
    @jsii.member(jsii_name="claimRef")
    def claim_ref(self) -> PersistentVolumeSpecClaimRefOutputReference:
        return typing.cast(PersistentVolumeSpecClaimRefOutputReference, jsii.get(self, "claimRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinity")
    def node_affinity(self) -> PersistentVolumeSpecNodeAffinityOutputReference:
        return typing.cast(PersistentVolumeSpecNodeAffinityOutputReference, jsii.get(self, "nodeAffinity"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSource")
    def persistent_volume_source(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceOutputReference", jsii.get(self, "persistentVolumeSource"))

    @builtins.property
    @jsii.member(jsii_name="accessModesInput")
    def access_modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessModesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRefInput")
    def claim_ref_input(self) -> typing.Optional[PersistentVolumeSpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecClaimRef], jsii.get(self, "claimRefInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinityInput")
    def node_affinity_input(self) -> typing.Optional[PersistentVolumeSpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeSpecNodeAffinity], jsii.get(self, "nodeAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicyInput")
    def persistent_volume_reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "persistentVolumeReclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSourceInput")
    def persistent_volume_source_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSource"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSource"], jsii.get(self, "persistentVolumeSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassNameInput")
    def storage_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeModeInput")
    def volume_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessModes"))

    @access_modes.setter
    def access_modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603f8678d5870e90df2909e99ade7abb1d195b4b97cda84fee7632a8a48afc96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessModes", value)

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__761cf6e4b0ce0114425a64791cec7caeef88f966b859437e44a4787075df8320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d139f694c5ce63b10f596910d95a5cbf0134a5ffa929e5183edd9a2cdd119eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicy")
    def persistent_volume_reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistentVolumeReclaimPolicy"))

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae23fef58cfacf30a0833bd56697f6c4e0d41474fb4d0740672eb807b7a7d06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistentVolumeReclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClassName"))

    @storage_class_name.setter
    def storage_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__637bc758a9dd785890b7181454eaaa7383021d1d7c073ef197d65b82ce7216dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClassName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeMode"))

    @volume_mode.setter
    def volume_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f8b5817ce7a661d5338729cfdac4c09d26a98fcf2a70d5686e567d6583f800f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c12cf626fbb7ab0119a9ff25c7c2a817d700eb61d022520846a017088f199d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSource",
    jsii_struct_bases=[],
    name_mapping={
        "aws_elastic_block_store": "awsElasticBlockStore",
        "azure_disk": "azureDisk",
        "azure_file": "azureFile",
        "ceph_fs": "cephFs",
        "cinder": "cinder",
        "csi": "csi",
        "fc": "fc",
        "flex_volume": "flexVolume",
        "flocker": "flocker",
        "gce_persistent_disk": "gcePersistentDisk",
        "glusterfs": "glusterfs",
        "host_path": "hostPath",
        "iscsi": "iscsi",
        "local": "local",
        "nfs": "nfs",
        "photon_persistent_disk": "photonPersistentDisk",
        "quobyte": "quobyte",
        "rbd": "rbd",
        "vsphere_volume": "vsphereVolume",
    },
)
class PersistentVolumeSpecPersistentVolumeSource:
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceAzureFile", typing.Dict[builtins.str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFs", typing.Dict[builtins.str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCinder", typing.Dict[builtins.str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsi", typing.Dict[builtins.str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFc", typing.Dict[builtins.str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolume", typing.Dict[builtins.str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlocker", typing.Dict[builtins.str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceGlusterfs", typing.Dict[builtins.str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceHostPath", typing.Dict[builtins.str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceIscsi", typing.Dict[builtins.str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceLocal", typing.Dict[builtins.str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceNfs", typing.Dict[builtins.str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceQuobyte", typing.Dict[builtins.str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbd", typing.Dict[builtins.str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        if isinstance(aws_elastic_block_store, dict):
            aws_elastic_block_store = PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(**aws_elastic_block_store)
        if isinstance(azure_disk, dict):
            azure_disk = PersistentVolumeSpecPersistentVolumeSourceAzureDisk(**azure_disk)
        if isinstance(azure_file, dict):
            azure_file = PersistentVolumeSpecPersistentVolumeSourceAzureFile(**azure_file)
        if isinstance(ceph_fs, dict):
            ceph_fs = PersistentVolumeSpecPersistentVolumeSourceCephFs(**ceph_fs)
        if isinstance(cinder, dict):
            cinder = PersistentVolumeSpecPersistentVolumeSourceCinder(**cinder)
        if isinstance(csi, dict):
            csi = PersistentVolumeSpecPersistentVolumeSourceCsi(**csi)
        if isinstance(fc, dict):
            fc = PersistentVolumeSpecPersistentVolumeSourceFc(**fc)
        if isinstance(flex_volume, dict):
            flex_volume = PersistentVolumeSpecPersistentVolumeSourceFlexVolume(**flex_volume)
        if isinstance(flocker, dict):
            flocker = PersistentVolumeSpecPersistentVolumeSourceFlocker(**flocker)
        if isinstance(gce_persistent_disk, dict):
            gce_persistent_disk = PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(**gce_persistent_disk)
        if isinstance(glusterfs, dict):
            glusterfs = PersistentVolumeSpecPersistentVolumeSourceGlusterfs(**glusterfs)
        if isinstance(host_path, dict):
            host_path = PersistentVolumeSpecPersistentVolumeSourceHostPath(**host_path)
        if isinstance(iscsi, dict):
            iscsi = PersistentVolumeSpecPersistentVolumeSourceIscsi(**iscsi)
        if isinstance(local, dict):
            local = PersistentVolumeSpecPersistentVolumeSourceLocal(**local)
        if isinstance(nfs, dict):
            nfs = PersistentVolumeSpecPersistentVolumeSourceNfs(**nfs)
        if isinstance(photon_persistent_disk, dict):
            photon_persistent_disk = PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(**photon_persistent_disk)
        if isinstance(quobyte, dict):
            quobyte = PersistentVolumeSpecPersistentVolumeSourceQuobyte(**quobyte)
        if isinstance(rbd, dict):
            rbd = PersistentVolumeSpecPersistentVolumeSourceRbd(**rbd)
        if isinstance(vsphere_volume, dict):
            vsphere_volume = PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(**vsphere_volume)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc40aec29680e95f449909c7d358c5c287f48c1a1ba48c39613a9d4b31e28086)
            check_type(argname="argument aws_elastic_block_store", value=aws_elastic_block_store, expected_type=type_hints["aws_elastic_block_store"])
            check_type(argname="argument azure_disk", value=azure_disk, expected_type=type_hints["azure_disk"])
            check_type(argname="argument azure_file", value=azure_file, expected_type=type_hints["azure_file"])
            check_type(argname="argument ceph_fs", value=ceph_fs, expected_type=type_hints["ceph_fs"])
            check_type(argname="argument cinder", value=cinder, expected_type=type_hints["cinder"])
            check_type(argname="argument csi", value=csi, expected_type=type_hints["csi"])
            check_type(argname="argument fc", value=fc, expected_type=type_hints["fc"])
            check_type(argname="argument flex_volume", value=flex_volume, expected_type=type_hints["flex_volume"])
            check_type(argname="argument flocker", value=flocker, expected_type=type_hints["flocker"])
            check_type(argname="argument gce_persistent_disk", value=gce_persistent_disk, expected_type=type_hints["gce_persistent_disk"])
            check_type(argname="argument glusterfs", value=glusterfs, expected_type=type_hints["glusterfs"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument iscsi", value=iscsi, expected_type=type_hints["iscsi"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            check_type(argname="argument photon_persistent_disk", value=photon_persistent_disk, expected_type=type_hints["photon_persistent_disk"])
            check_type(argname="argument quobyte", value=quobyte, expected_type=type_hints["quobyte"])
            check_type(argname="argument rbd", value=rbd, expected_type=type_hints["rbd"])
            check_type(argname="argument vsphere_volume", value=vsphere_volume, expected_type=type_hints["vsphere_volume"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_elastic_block_store is not None:
            self._values["aws_elastic_block_store"] = aws_elastic_block_store
        if azure_disk is not None:
            self._values["azure_disk"] = azure_disk
        if azure_file is not None:
            self._values["azure_file"] = azure_file
        if ceph_fs is not None:
            self._values["ceph_fs"] = ceph_fs
        if cinder is not None:
            self._values["cinder"] = cinder
        if csi is not None:
            self._values["csi"] = csi
        if fc is not None:
            self._values["fc"] = fc
        if flex_volume is not None:
            self._values["flex_volume"] = flex_volume
        if flocker is not None:
            self._values["flocker"] = flocker
        if gce_persistent_disk is not None:
            self._values["gce_persistent_disk"] = gce_persistent_disk
        if glusterfs is not None:
            self._values["glusterfs"] = glusterfs
        if host_path is not None:
            self._values["host_path"] = host_path
        if iscsi is not None:
            self._values["iscsi"] = iscsi
        if local is not None:
            self._values["local"] = local
        if nfs is not None:
            self._values["nfs"] = nfs
        if photon_persistent_disk is not None:
            self._values["photon_persistent_disk"] = photon_persistent_disk
        if quobyte is not None:
            self._values["quobyte"] = quobyte
        if rbd is not None:
            self._values["rbd"] = rbd
        if vsphere_volume is not None:
            self._values["vsphere_volume"] = vsphere_volume

    @builtins.property
    def aws_elastic_block_store(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore"]:
        '''aws_elastic_block_store block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#aws_elastic_block_store PersistentVolume#aws_elastic_block_store}
        '''
        result = self._values.get("aws_elastic_block_store")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore"], result)

    @builtins.property
    def azure_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureDisk"]:
        '''azure_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_disk PersistentVolume#azure_disk}
        '''
        result = self._values.get("azure_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureDisk"], result)

    @builtins.property
    def azure_file(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureFile"]:
        '''azure_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#azure_file PersistentVolume#azure_file}
        '''
        result = self._values.get("azure_file")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceAzureFile"], result)

    @builtins.property
    def ceph_fs(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFs"]:
        '''ceph_fs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_fs PersistentVolume#ceph_fs}
        '''
        result = self._values.get("ceph_fs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFs"], result)

    @builtins.property
    def cinder(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCinder"]:
        '''cinder block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#cinder PersistentVolume#cinder}
        '''
        result = self._values.get("cinder")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCinder"], result)

    @builtins.property
    def csi(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsi"]:
        '''csi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#csi PersistentVolume#csi}
        '''
        result = self._values.get("csi")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsi"], result)

    @builtins.property
    def fc(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFc"]:
        '''fc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fc PersistentVolume#fc}
        '''
        result = self._values.get("fc")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFc"], result)

    @builtins.property
    def flex_volume(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolume"]:
        '''flex_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flex_volume PersistentVolume#flex_volume}
        '''
        result = self._values.get("flex_volume")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolume"], result)

    @builtins.property
    def flocker(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlocker"]:
        '''flocker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#flocker PersistentVolume#flocker}
        '''
        result = self._values.get("flocker")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlocker"], result)

    @builtins.property
    def gce_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk"]:
        '''gce_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#gce_persistent_disk PersistentVolume#gce_persistent_disk}
        '''
        result = self._values.get("gce_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk"], result)

    @builtins.property
    def glusterfs(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGlusterfs"]:
        '''glusterfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#glusterfs PersistentVolume#glusterfs}
        '''
        result = self._values.get("glusterfs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceGlusterfs"], result)

    @builtins.property
    def host_path(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceHostPath"]:
        '''host_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#host_path PersistentVolume#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceHostPath"], result)

    @builtins.property
    def iscsi(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceIscsi"]:
        '''iscsi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi PersistentVolume#iscsi}
        '''
        result = self._values.get("iscsi")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceIscsi"], result)

    @builtins.property
    def local(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceLocal"]:
        '''local block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#local PersistentVolume#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceLocal"], result)

    @builtins.property
    def nfs(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceNfs"]:
        '''nfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#nfs PersistentVolume#nfs}
        '''
        result = self._values.get("nfs")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceNfs"], result)

    @builtins.property
    def photon_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"]:
        '''photon_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#photon_persistent_disk PersistentVolume#photon_persistent_disk}
        '''
        result = self._values.get("photon_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"], result)

    @builtins.property
    def quobyte(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"]:
        '''quobyte block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#quobyte PersistentVolume#quobyte}
        '''
        result = self._values.get("quobyte")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"], result)

    @builtins.property
    def rbd(self) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"]:
        '''rbd block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd PersistentVolume#rbd}
        '''
        result = self._values.get("rbd")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"], result)

    @builtins.property
    def vsphere_volume(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"]:
        '''vsphere_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#vsphere_volume PersistentVolume#vsphere_volume}
        '''
        result = self._values.get("vsphere_volume")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__741a16139cfa367cb716be8134f385801adc61159ce8935285e21026ab3f0736)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfa06e58a08f7e05725902301a4b867a24c65dd6bda3b9957aa2192fbcb92795)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bff97efa6813190d58cc97fcbf1fa7ea9d10d6b6102bc8b7d700a2e4faf77c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8468322e7b5dc6018762f54432fc77a8c5f94f518ba96f7dec7b9cb4eb93af03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__6064edf30586bab85338bdd7316af7a3c737506a3d20e0615e83352e94c32079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796b8353fe5f017afecb87c24e5792509fbc52e614e5d6369c3ddfbb9e180962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ac43221e900ffe25d39cbe1c6c81abd606e4de290cfd495644fa12bdc42a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "data_disk_uri": "dataDiskUri",
        "disk_name": "diskName",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAzureDisk:
    def __init__(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e790150315dd2741cab598f528f5a450185203af2dec3036412b3292fe3487bf)
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument data_disk_uri", value=data_disk_uri, expected_type=type_hints["data_disk_uri"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "caching_mode": caching_mode,
            "data_disk_uri": data_disk_uri,
            "disk_name": disk_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> builtins.str:
        '''Host Caching mode: None, Read Only, Read Write.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        '''
        result = self._values.get("caching_mode")
        assert result is not None, "Required property 'caching_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        '''
        result = self._values.get("data_disk_uri")
        assert result is not None, "Required property 'data_disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAzureDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70f3e30e727de082080c17eed535fdf701c0cae809b57b678c08d5dada7ec00a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="cachingModeInput")
    def caching_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskUriInput")
    def data_disk_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataDiskUriInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachingMode"))

    @caching_mode.setter
    def caching_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e45ca9ea52ca441a8fcff211143242dc4e44aa95c218da3d9c3b5ff5a37c338e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskUri")
    def data_disk_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDiskUri"))

    @data_disk_uri.setter
    def data_disk_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a79395e5d7a7f492c922c505bf961cf2840741eb599edc9258ccd3475dde8542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskUri", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387f3a4466171e0bf4d0f4b763005f32268cb1b79a08774850f09388ac53fb76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f470d6f54109bfde6db7e66a62e8a92d7baabb5b4b0bc2b183609277d836db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c7c8e6f7918d4b54f01f14ec33b566c02cfd82732151dac9249b3a3b1a68b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__0374146b9ff870b2d010bf2e2020b95cbbaf5059519303365c5a263153978eae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f36542c5ba03bfbe717ab617395b6f708fa560ac76f82d6133d0470e4c635f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureFile",
    jsii_struct_bases=[],
    name_mapping={
        "secret_name": "secretName",
        "share_name": "shareName",
        "read_only": "readOnly",
        "secret_namespace": "secretNamespace",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceAzureFile:
    def __init__(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__347f0f32b0cfd834d2dd1d95b75b3a6928880a028e21ec174d47f45986062573)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_namespace", value=secret_namespace, expected_type=type_hints["secret_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
            "share_name": share_name,
        }
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_namespace is not None:
            self._values["secret_namespace"] = secret_namespace

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''The name of secret that contains Azure Storage Account Name and Key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        '''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Share Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        '''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the secret that contains Azure Storage Account Name and Key.

        For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        result = self._values.get("secret_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceAzureFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7775f8ec8935e3b2eaf16a00928623c5923d5cfa3526dbe6735bb26f45459961)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretNamespace")
    def reset_secret_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNamespaceInput")
    def secret_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__833752376d84fd73ef17b1531bbccc0ca933bbfd98f5e17886ac94a483e8cb56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44dffc6358aece5f84e07c7e140a9ac8780b3d16d2d2c544dccae08c485c7cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="secretNamespace")
    def secret_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretNamespace"))

    @secret_namespace.setter
    def secret_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61106469a5eca17d0c2b59601fec24974275f714a599523944feab6bd72cdb1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ab49751beeb0849f7167c2a3672b98bc2a9198315eb787de8312d445bc1058)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856fa03af4d9f31d61eb870c9fb37c6356dd8717fdc28541f770facdeb37a7d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFs",
    jsii_struct_bases=[],
    name_mapping={
        "monitors": "monitors",
        "path": "path",
        "read_only": "readOnly",
        "secret_file": "secretFile",
        "secret_ref": "secretRef",
        "user": "user",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCephFs:
    def __init__(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d86d06d48877c23f6cd672019c3fda8f2f4698df7d348248904855cad95ed4)
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_file", value=secret_file, expected_type=type_hints["secret_file"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitors": monitors,
        }
        if path is not None:
            self._values["path"] = path
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_file is not None:
            self._values["secret_file"] = secret_file
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def monitors(self) -> typing.List[builtins.str]:
        '''Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        '''
        result = self._values.get("monitors")
        assert result is not None, "Required property 'monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Used as the mounted root, rather than the full Ceph tree, default is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_file(self) -> typing.Optional[builtins.str]:
        '''The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        '''
        result = self._values.get("secret_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCephFs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50b5dcab5da8788d99dd7ff4fec1d86b0443ec170bd2e6cde444b11d37e2e1c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretFile")
    def reset_secret_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretFile", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="monitorsInput")
    def monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretFileInput")
    def secret_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretFileInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09898e5446e993982a11c97eb3adeedabafecb2351077ce966b1bb8d8230a19b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8862c8590b54d8726772bddf03e3381909fa342b27e55c6e7ec394634474dd5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__8c56a0c65af5502a64a6884f90085d2d3d2acd02d2dc589ee2add4f02bdf7aa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretFile")
    def secret_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretFile"))

    @secret_file.setter
    def secret_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092e3f0afb7419a5427a1b52b9b2f9a8a86f83dc7fd020bb94c2a6f57f344443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretFile", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba1726ed09db39846e4f7a99179514638986438ed54dae6a94d6c133f84c2c33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db3b780d1456af120f5e3ea49df5eabc22b3ef57bbe9a4600f3c0fe1ccc0995)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cc3004ccfbd40a60fc4df59b2f51b2108210e13e211f574a0f010ce1177b99)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bbbb328506833f9464bd1cd4c9780d9faea343519f6cb0683d14154d636a241)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd1095d2756174df15d6614af96d61d581bda9e4d6863b1a203347bd716200d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__549ed057a5c6f188f39a49c73c9c76c6fdcc8e04b774d3e98de1eb2997215f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe73073cc544af7c00db29bed48fa9f6e4858cd6e2e5117e9e68935c2ee4bdcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCinder",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCinder:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d2b306e5293f0372e432293ef4ba7b101308cc9b817f2999317a8c42041810)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCinder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7dafec68fa560502e5bfa374d513af2f515b84588315a0c90d5907b20493a01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6351f474af639aacd434ad4507fc5bfa87fd307b24da4ee5c8a35214c31a407d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__b3ef9e285eaed6ce7e013a37e536fb985f21a55a87ca81f440608f5faef34ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fc1683806209ed5f22847d4562acc255a2b14695d70aba0395a8f3b90f54b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24320630f61f8e48aa786dbc3c7d30f8af977da891f2d17ece5447e7366f9258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsi",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "volume_handle": "volumeHandle",
        "controller_expand_secret_ref": "controllerExpandSecretRef",
        "controller_publish_secret_ref": "controllerPublishSecretRef",
        "fs_type": "fsType",
        "node_publish_secret_ref": "nodePublishSecretRef",
        "node_stage_secret_ref": "nodeStageSecretRef",
        "read_only": "readOnly",
        "volume_attributes": "volumeAttributes",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceCsi:
    def __init__(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        if isinstance(controller_expand_secret_ref, dict):
            controller_expand_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(**controller_expand_secret_ref)
        if isinstance(controller_publish_secret_ref, dict):
            controller_publish_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(**controller_publish_secret_ref)
        if isinstance(node_publish_secret_ref, dict):
            node_publish_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(**node_publish_secret_ref)
        if isinstance(node_stage_secret_ref, dict):
            node_stage_secret_ref = PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(**node_stage_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cc1f5ae61e1b02b0173960288c32b32a155a757af3912f1d224b0a258d68bd)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument volume_handle", value=volume_handle, expected_type=type_hints["volume_handle"])
            check_type(argname="argument controller_expand_secret_ref", value=controller_expand_secret_ref, expected_type=type_hints["controller_expand_secret_ref"])
            check_type(argname="argument controller_publish_secret_ref", value=controller_publish_secret_ref, expected_type=type_hints["controller_publish_secret_ref"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument node_publish_secret_ref", value=node_publish_secret_ref, expected_type=type_hints["node_publish_secret_ref"])
            check_type(argname="argument node_stage_secret_ref", value=node_stage_secret_ref, expected_type=type_hints["node_stage_secret_ref"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_attributes", value=volume_attributes, expected_type=type_hints["volume_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
            "volume_handle": volume_handle,
        }
        if controller_expand_secret_ref is not None:
            self._values["controller_expand_secret_ref"] = controller_expand_secret_ref
        if controller_publish_secret_ref is not None:
            self._values["controller_publish_secret_ref"] = controller_publish_secret_ref
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if node_publish_secret_ref is not None:
            self._values["node_publish_secret_ref"] = node_publish_secret_ref
        if node_stage_secret_ref is not None:
            self._values["node_stage_secret_ref"] = node_stage_secret_ref
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_attributes is not None:
            self._values["volume_attributes"] = volume_attributes

    @builtins.property
    def driver(self) -> builtins.str:
        '''the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_handle(self) -> builtins.str:
        '''A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        '''
        result = self._values.get("volume_handle")
        assert result is not None, "Required property 'volume_handle' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def controller_expand_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef"]:
        '''controller_expand_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        '''
        result = self._values.get("controller_expand_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef"], result)

    @builtins.property
    def controller_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef"]:
        '''controller_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        '''
        result = self._values.get("controller_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef"], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef"]:
        '''node_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        '''
        result = self._values.get("node_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef"], result)

    @builtins.property
    def node_stage_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef"]:
        '''node_stage_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        '''
        result = self._values.get("node_stage_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def volume_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Attributes of the volume to publish.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        result = self._values.get("volume_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204856ea75d673734ef8a66cb92042cb860c5619c30bfcc9b4257dec8963ddfd)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9571715b61271f7464633f8e6e17aeda6b3de5695232f2df44fcdd13e7a60568)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__277ca4d632f39227fd15f5dece6946745fec45301b1a18ab8122d4512843d950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b313554d87e30abf55923da0f5d85449ef873f5c143ebcf4495d07eb008dc732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3f0c185a09bef0769b8a8715e96eaa7d15467eca6db91211f8a056681755c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__493582cf93c32304ac1a69f4cd843e9836ddc7100ed3eaa80fd81d3471a8b8ed)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0a1fb7786f5416d688bdba96b9ec4fb9e365362c32771b6d2380884f681abf9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b412a02e9603425c8391e1cf08ea90ee04381a0b3a6a8f53eafe15ee8fa6ef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f7064943df90471ae11955e1ac91900c97f2ee1791cd29e71598547f0b8d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51e5d34d0464348e4bace174f10df99bce97fd27bc3b98f4806cf18ae9b6a757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b01fbaadf2fffa7d85a7af40ad04923c524b6c95de044bf08b7c2daeeb2d01)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f745c0500573491effd8ff5f0e0798de29a4bbb54bb7cbd332d22e312a13ec9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e137285df1d4bb505aa302b07ec187e399a6d2c762d49595c1a7a102fd6ebc53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed75a9f748287df11522d113fc05cd49427282f7b947cd55de2c7567739bdf32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b13f98befe6fe2bcbe3f3963965b409526b5ca4659444d1a062ea4f72ba1bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7633206a5658f1eda3fa296be8a4ca3e4c7cfca38b987b69fd7b02136d8f8d2c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9cf05fd13abaafb720d0ede77268e06c5e17877d9b3807f1fe1d189ec74330e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78919df8293d0d14702b71d8722e59d9448d3a0960c9c2f763dbf3c8f89586c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911e231bdb2806929f2858edf9ebb4327c693fb07c7b26a7b73e9c75c9f780df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62679391de3e4314059aa7abad25093d78682d4c4dd96c2124025be3e1b087bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37baed910e2cdba44cccd68a8f606bea775addae6917685e8561d510d9468ffc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putControllerExpandSecretRef")
    def put_controller_expand_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerExpandSecretRef", [value]))

    @jsii.member(jsii_name="putControllerPublishSecretRef")
    def put_controller_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerPublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodePublishSecretRef")
    def put_node_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodePublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodeStageSecretRef")
    def put_node_stage_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodeStageSecretRef", [value]))

    @jsii.member(jsii_name="resetControllerExpandSecretRef")
    def reset_controller_expand_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerExpandSecretRef", []))

    @jsii.member(jsii_name="resetControllerPublishSecretRef")
    def reset_controller_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerPublishSecretRef", []))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetNodePublishSecretRef")
    def reset_node_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePublishSecretRef", []))

    @jsii.member(jsii_name="resetNodeStageSecretRef")
    def reset_node_stage_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeStageSecretRef", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeAttributes")
    def reset_volume_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRef")
    def controller_expand_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, jsii.get(self, "controllerExpandSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRef")
    def controller_publish_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, jsii.get(self, "controllerPublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRef")
    def node_publish_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, jsii.get(self, "nodePublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRef")
    def node_stage_secret_ref(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, jsii.get(self, "nodeStageSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRefInput")
    def controller_expand_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "controllerExpandSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRefInput")
    def controller_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "controllerPublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRefInput")
    def node_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "nodePublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRefInput")
    def node_stage_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "nodeStageSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeAttributesInput")
    def volume_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeHandleInput")
    def volume_handle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeHandleInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3b69e904ae8dfe9c226a13187c1c2daa610c4225410cad4a1dc9b68399f0b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3257943b3189bce78b907018cc9eb7ecb10a501188fe430e7f361405ebe51ec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__f169b347667c134a7697623d70c70ee239acab6f8fa46997c0cabbda56b94b59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeAttributes")
    def volume_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeAttributes"))

    @volume_attributes.setter
    def volume_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e68e8e4d4779084de2fdb81b04898f115f742f11e16a9ff92395a29fc87bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="volumeHandle")
    def volume_handle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeHandle"))

    @volume_handle.setter
    def volume_handle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93060697ebd67bcc533110d0206cf966f8d0bac691364c4d6aec994b4dd52f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeHandle", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4486f1a6520ed520167fbd322039433cccbe78616581e5722a6a8c72dabb0a59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFc",
    jsii_struct_bases=[],
    name_mapping={
        "lun": "lun",
        "target_ww_ns": "targetWwNs",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceFc:
    def __init__(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77807467c0087e74ac5c45a976183418652b6e30c83327d5168c6472bf56350c)
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument target_ww_ns", value=target_ww_ns, expected_type=type_hints["target_ww_ns"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lun": lun,
            "target_ww_ns": target_ww_ns,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def lun(self) -> jsii.Number:
        '''FC target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        '''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_ww_ns(self) -> typing.List[builtins.str]:
        '''FC target worldwide names (WWNs).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        '''
        result = self._values.get("target_ww_ns")
        assert result is not None, "Required property 'target_ww_ns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b57992b16094cda9842feee65eb15ed2efff6b1e723cc09d5b847ab27535f4be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWwNsInput")
    def target_ww_ns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetWwNsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5c4f632ccf04f3c4e625bd208b19f28c7e3edbe16aa6207f0b2cf9be2a1202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8a23766709bf361fc38c4cca11a53d0bdc1b7997bd4bf7b9eb90968290d809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__9a5753ef43382dd0b2293d473aff510f1a47dbc70d6c46893e8b2a1a6f3c9e71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetWwNs")
    def target_ww_ns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetWwNs"))

    @target_ww_ns.setter
    def target_ww_ns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ed1516aa6ffa05a7a42410550f5f068d8905f69a8dbd8ccf26d69302341d61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWwNs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091fae0041b4ee7b36e7cd9b3092d2b7b71b007e1a703eb5e985cbb58c3090f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolume",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "fs_type": "fsType",
        "options": "options",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceFlexVolume:
    def __init__(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0228801f16cc0a0f7e0db2751d7319c8dd2a899c2f2781de3c655382ea1865)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "driver": driver,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if options is not None:
            self._values["options"] = options
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def driver(self) -> builtins.str:
        '''Driver is the name of the driver to use for this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Extra command options if any.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlexVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ceec9ee4418624ff7eb0def24f642ebf0349ecf901016a95bae455f51978b96)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea46be7e1400c980c6d103c7fea31cd869bc6b89bedf57938b2ae55f8171020)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032412c9d25e452c49461528335a5e4e0bc0b2eebfbed7c61fe7b3e57ec87445)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43bf55ede2dce7764475544dae248f503df7b57f58f978bbdc4797d5003eb5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__165017ed2777eff0eaeb747acf78cbd64bc94942a771adcbf830bdda935e0cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8cff150448fed8edd575e3927b9e5b40b4965b647c1efd26ad56bd7ac64d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6de0c555f77fe22b803b9995ece59f4bcbbb3035a89538942a6c02cce8714b9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccdf25b6e713366f76de0ae878d78f5635f3c1ea1874b1221b11f722ca4557ae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__458467b1e21ba8fb71f698bcbb9b7de1e88c0fc163315024d0e0931708512556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09ce3653bc941551df3599688ec33e7659b495a6f213f14ab8a9f6d3da1588e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac75b9c125a9df38d6d5f2a4e4d2f275eada56c8ba5545c634a769c761fd724c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlocker",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName", "dataset_uuid": "datasetUuid"},
)
class PersistentVolumeSpecPersistentVolumeSourceFlocker:
    def __init__(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa2db6620e566c282735d2f7285d477cd9829a56bad7dd5f1b625385a60410d)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_uuid", value=dataset_uuid, expected_type=type_hints["dataset_uuid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if dataset_uuid is not None:
            self._values["dataset_uuid"] = dataset_uuid

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dataset_uuid(self) -> typing.Optional[builtins.str]:
        '''UUID of the dataset. This is unique identifier of a Flocker dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        result = self._values.get("dataset_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceFlocker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__736bf27761e106844fe1ea183bea39c2ea7833ec26813d34a49c9ca59642d579)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetName")
    def reset_dataset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetName", []))

    @jsii.member(jsii_name="resetDatasetUuid")
    def reset_dataset_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetUuid", []))

    @builtins.property
    @jsii.member(jsii_name="datasetNameInput")
    def dataset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetUuidInput")
    def dataset_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600d284d9415275095b9e29230ad5ee24790232e59f38df167e172e9b07831a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property
    @jsii.member(jsii_name="datasetUuid")
    def dataset_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetUuid"))

    @dataset_uuid.setter
    def dataset_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7feb7a76d67ff4767166a9aec8e3cc6235070cce3cb022e063a8f97ea80c7535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetUuid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cfae432c3ca55167534d8a1946191658a625df0e088b25087830e4e435d3dd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk",
    jsii_struct_bases=[],
    name_mapping={
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk:
    def __init__(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a858ca03c24ce9ec529ad09189a0429970e7227c16e45dcf712efe05bef092e)
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_name": pd_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57466fe3b338dd604fa85eb495e2681bb7c4f46b09275ad9e014b444c3ed779a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="pdNameInput")
    def pd_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4299a698dc7a132888115d7cb158c4254f26785414f74384ebd80289ba89497d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e52f37c99fd51ab217361a5569498ec15433db9469b88a50c259100b6be98b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @pd_name.setter
    def pd_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9aa5f88cff12a7a3f1dba322a7cc78b708a4ee1408082486f520c739058956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdName", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__416920b6a3a5705e78dce5a1f6598f404282ae26fc89829c6ca2d9a45bf82d55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0d34015738d478accf903fdbd0ac8a3800d103623dbd4ec2bc07b5a554f2d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGlusterfs",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints_name": "endpointsName",
        "path": "path",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceGlusterfs:
    def __init__(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a013afd8a20fca1f5cfe017bd3c50879f80510c5fe445829906a19ef139ced5)
            check_type(argname="argument endpoints_name", value=endpoints_name, expected_type=type_hints["endpoints_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoints_name": endpoints_name,
            "path": path,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def endpoints_name(self) -> builtins.str:
        '''The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        '''
        result = self._values.get("endpoints_name")
        assert result is not None, "Required property 'endpoints_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceGlusterfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__83bb7000744f0ea2ab1bc0758f08dbca27211265224d5e5c8a58f1b9334a1650)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="endpointsNameInput")
    def endpoints_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsName")
    def endpoints_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointsName"))

    @endpoints_name.setter
    def endpoints_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adcba58752787ed65e5e165b49614e93848fc38b89d6f5a38200e98054fe119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointsName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43ff5e3049d6ce247f7fb1de936ee8169b44853ffb2c301d0c548760c591c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__81c86356fe0c24cd91c45f6c9bc4c1e704ff14b6bf41fb3d1f7b1760ee75b4c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b87bd60daac7cf700f94f24fe018d71428417e7bf76c289bfaeceff7cf6fa2e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceHostPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "type": "type"},
)
class PersistentVolumeSpecPersistentVolumeSourceHostPath:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad95a54a00b56346390fbe47e70507a04d30617e19e45bc9975020e5f279a60)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceHostPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1be6a070ce6fd456ccbc00738b643f3202da84a3ab497216d8736f493e4ccb81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5a4ee459aa4c188c675a9b50276920a406b5d4e7ac88d753694fce8e41603e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606f8fac81518a5720756800f90a5c08431d8d3c7bccc800d6b2ba8cd8933f99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530a63ef3d30472c929db708a35cd4148e955da5d27b7ca81d7b8c49a07e0d38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceIscsi",
    jsii_struct_bases=[],
    name_mapping={
        "iqn": "iqn",
        "target_portal": "targetPortal",
        "fs_type": "fsType",
        "iscsi_interface": "iscsiInterface",
        "lun": "lun",
        "read_only": "readOnly",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceIscsi:
    def __init__(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b7688993e4f1fb35afe31ab1a61386be7891f38451cdd07bddec5cfba8fd6d2)
            check_type(argname="argument iqn", value=iqn, expected_type=type_hints["iqn"])
            check_type(argname="argument target_portal", value=target_portal, expected_type=type_hints["target_portal"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument iscsi_interface", value=iscsi_interface, expected_type=type_hints["iscsi_interface"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iqn": iqn,
            "target_portal": target_portal,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if iscsi_interface is not None:
            self._values["iscsi_interface"] = iscsi_interface
        if lun is not None:
            self._values["lun"] = lun
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def iqn(self) -> builtins.str:
        '''Target iSCSI Qualified Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        '''
        result = self._values.get("iqn")
        assert result is not None, "Required property 'iqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_portal(self) -> builtins.str:
        '''iSCSI target portal.

        The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        '''
        result = self._values.get("target_portal")
        assert result is not None, "Required property 'target_portal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iscsi_interface(self) -> typing.Optional[builtins.str]:
        '''iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        '''
        result = self._values.get("iscsi_interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[jsii.Number]:
        '''iSCSI target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        '''
        result = self._values.get("lun")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceIscsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b3418aa845e287053afaeb452c31fd06f85e5eb40d3a642b338fc7457c56211)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetIscsiInterface")
    def reset_iscsi_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiInterface", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iqnInput")
    def iqn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iqnInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInterfaceInput")
    def iscsi_interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscsiInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortalInput")
    def target_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5ec2e779af680c40a08b71b7654379e87df17847ec97585e5ecd8b0b9de720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="iqn")
    def iqn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iqn"))

    @iqn.setter
    def iqn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56f4d44d839f4af5257b844379926336d6b859f4024da754c28ee89d7117093b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iqn", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiInterface")
    def iscsi_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscsiInterface"))

    @iscsi_interface.setter
    def iscsi_interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d7ac64d894ad41d13bf0842118f00f0ad976680a80217f450ccb2f5243010b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiInterface", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9961c74eeb5059d00e306712d8b1110af052492618f892aa84289cf1884f2b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__d8f284344ff51f9a098e2111da173349dd99f0a8ce9a325407e0d674a2ec4db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetPortal")
    def target_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPortal"))

    @target_portal.setter
    def target_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5858e8e594a1402422e19f4794a2cae769d297f8270e0577e2042b9ac79a1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPortal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d3c9feb432d29292b79b76650b4a95126189624f3905827856778c93dfb38c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceLocal",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PersistentVolumeSpecPersistentVolumeSourceLocal:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0dd09f634b821bd60026ff1069b11f7e72b0252b63a59c2ccaa69b5adbe3a68)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceLocal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6ad78a34dfd4790fce3600052c4d3d8bf51129d7bfbea4a35de4234ea0336b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__4141e595736728907fcaa38b3d31a8dd740339af67861cfb9b58c467b489b6c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c333ba07bfc1e71514fa247685288c05fc0b8bc938b81a71e57c7687d03dab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceNfs",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "server": "server", "read_only": "readOnly"},
)
class PersistentVolumeSpecPersistentVolumeSourceNfs:
    def __init__(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242b7f69bb1a4c3854adfc4e7f3fab1ab4154cf5a24cfae3f6ade3e23e379da0)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
            "server": server,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path(self) -> builtins.str:
        '''Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        '''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0340ef6686deb43442fe18a0cf3a6b0d264f481eabf72182f4627f7a059da2b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53cd497dd5701fe50e6333273d2693f89d6f84d8d894e4034ffc7aa935c50b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1a83c22d5ffffbec99b506d644e97c31a2561c614004bf5956e142bb11c3a78c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77d8b7358173d029d025253c3411d63c386a9b04d36ce8a72788cee674b86dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bc54b5d25aab3419a08bf6d841311bd01d3d9f977651bab3c71b8d74f70978e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeSpecPersistentVolumeSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a558e1dd4be6ef91fa57da0b9f5d4606d284f76001ed7b561efc9f0008f58bd8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsElasticBlockStore")
    def put_aws_elastic_block_store(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsElasticBlockStore", [value]))

    @jsii.member(jsii_name="putAzureDisk")
    def put_azure_disk(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#caching_mode PersistentVolume#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#data_disk_uri PersistentVolume#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#disk_name PersistentVolume#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#kind PersistentVolume#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAzureDisk(
            caching_mode=caching_mode,
            data_disk_uri=data_disk_uri,
            disk_name=disk_name,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureDisk", [value]))

    @jsii.member(jsii_name="putAzureFile")
    def put_azure_file(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_name PersistentVolume#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#share_name PersistentVolume#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_namespace PersistentVolume#secret_namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceAzureFile(
            secret_name=secret_name,
            share_name=share_name,
            read_only=read_only,
            secret_namespace=secret_namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFile", [value]))

    @jsii.member(jsii_name="putCephFs")
    def put_ceph_fs(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#monitors PersistentVolume#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_file PersistentVolume#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCephFs(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCephFs", [value]))

    @jsii.member(jsii_name="putCinder")
    def put_cinder(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_id PersistentVolume#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCinder(
            volume_id=volume_id, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putCinder", [value]))

    @jsii.member(jsii_name="putCsi")
    def put_csi(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_handle PersistentVolume#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_expand_secret_ref PersistentVolume#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#controller_publish_secret_ref PersistentVolume#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_publish_secret_ref PersistentVolume#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#node_stage_secret_ref PersistentVolume#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_attributes PersistentVolume#volume_attributes}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceCsi(
            driver=driver,
            volume_handle=volume_handle,
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putCsi", [value]))

    @jsii.member(jsii_name="putFc")
    def put_fc(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_ww_ns PersistentVolume#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFc(
            lun=lun, target_ww_ns=target_ww_ns, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putFc", [value]))

    @jsii.member(jsii_name="putFlexVolume")
    def put_flex_volume(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#driver PersistentVolume#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#options PersistentVolume#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlexVolume(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putFlexVolume", [value]))

    @jsii.member(jsii_name="putFlocker")
    def put_flocker(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_name PersistentVolume#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#dataset_uuid PersistentVolume#dataset_uuid}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceFlocker(
            dataset_name=dataset_name, dataset_uuid=dataset_uuid
        )

        return typing.cast(None, jsii.invoke(self, "putFlocker", [value]))

    @jsii.member(jsii_name="putGcePersistentDisk")
    def put_gce_persistent_disk(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_name PersistentVolume#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#partition PersistentVolume#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk(
            pd_name=pd_name, fs_type=fs_type, partition=partition, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGcePersistentDisk", [value]))

    @jsii.member(jsii_name="putGlusterfs")
    def put_glusterfs(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#endpoints_name PersistentVolume#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceGlusterfs(
            endpoints_name=endpoints_name, path=path, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGlusterfs", [value]))

    @jsii.member(jsii_name="putHostPath")
    def put_host_path(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#type PersistentVolume#type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceHostPath(
            path=path, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putHostPath", [value]))

    @jsii.member(jsii_name="putIscsi")
    def put_iscsi(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iqn PersistentVolume#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#target_portal PersistentVolume#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#iscsi_interface PersistentVolume#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#lun PersistentVolume#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceIscsi(
            iqn=iqn,
            target_portal=target_portal,
            fs_type=fs_type,
            iscsi_interface=iscsi_interface,
            lun=lun,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putIscsi", [value]))

    @jsii.member(jsii_name="putLocal")
    def put_local(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceLocal(path=path)

        return typing.cast(None, jsii.invoke(self, "putLocal", [value]))

    @jsii.member(jsii_name="putNfs")
    def put_nfs(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#path PersistentVolume#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#server PersistentVolume#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceNfs(
            path=path, server=server, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putNfs", [value]))

    @jsii.member(jsii_name="putPhotonPersistentDisk")
    def put_photon_persistent_disk(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(
            pd_id=pd_id, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putPhotonPersistentDisk", [value]))

    @jsii.member(jsii_name="putQuobyte")
    def put_quobyte(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceQuobyte(
            registry=registry,
            volume=volume,
            group=group,
            read_only=read_only,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putQuobyte", [value]))

    @jsii.member(jsii_name="putRbd")
    def put_rbd(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceRbd(
            ceph_monitors=ceph_monitors,
            rbd_image=rbd_image,
            fs_type=fs_type,
            keyring=keyring,
            rados_user=rados_user,
            rbd_pool=rbd_pool,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putRbd", [value]))

    @jsii.member(jsii_name="putVsphereVolume")
    def put_vsphere_volume(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(
            volume_path=volume_path, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putVsphereVolume", [value]))

    @jsii.member(jsii_name="resetAwsElasticBlockStore")
    def reset_aws_elastic_block_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsElasticBlockStore", []))

    @jsii.member(jsii_name="resetAzureDisk")
    def reset_azure_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDisk", []))

    @jsii.member(jsii_name="resetAzureFile")
    def reset_azure_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFile", []))

    @jsii.member(jsii_name="resetCephFs")
    def reset_ceph_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCephFs", []))

    @jsii.member(jsii_name="resetCinder")
    def reset_cinder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCinder", []))

    @jsii.member(jsii_name="resetCsi")
    def reset_csi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsi", []))

    @jsii.member(jsii_name="resetFc")
    def reset_fc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFc", []))

    @jsii.member(jsii_name="resetFlexVolume")
    def reset_flex_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlexVolume", []))

    @jsii.member(jsii_name="resetFlocker")
    def reset_flocker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlocker", []))

    @jsii.member(jsii_name="resetGcePersistentDisk")
    def reset_gce_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePersistentDisk", []))

    @jsii.member(jsii_name="resetGlusterfs")
    def reset_glusterfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlusterfs", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetIscsi")
    def reset_iscsi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsi", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetNfs")
    def reset_nfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfs", []))

    @jsii.member(jsii_name="resetPhotonPersistentDisk")
    def reset_photon_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonPersistentDisk", []))

    @jsii.member(jsii_name="resetQuobyte")
    def reset_quobyte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuobyte", []))

    @jsii.member(jsii_name="resetRbd")
    def reset_rbd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbd", []))

    @jsii.member(jsii_name="resetVsphereVolume")
    def reset_vsphere_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsphereVolume", []))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStore")
    def aws_elastic_block_store(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, jsii.get(self, "awsElasticBlockStore"))

    @builtins.property
    @jsii.member(jsii_name="azureDisk")
    def azure_disk(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference, jsii.get(self, "azureDisk"))

    @builtins.property
    @jsii.member(jsii_name="azureFile")
    def azure_file(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference, jsii.get(self, "azureFile"))

    @builtins.property
    @jsii.member(jsii_name="cephFs")
    def ceph_fs(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference, jsii.get(self, "cephFs"))

    @builtins.property
    @jsii.member(jsii_name="cinder")
    def cinder(self) -> PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference, jsii.get(self, "cinder"))

    @builtins.property
    @jsii.member(jsii_name="csi")
    def csi(self) -> PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference, jsii.get(self, "csi"))

    @builtins.property
    @jsii.member(jsii_name="fc")
    def fc(self) -> PersistentVolumeSpecPersistentVolumeSourceFcOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFcOutputReference, jsii.get(self, "fc"))

    @builtins.property
    @jsii.member(jsii_name="flexVolume")
    def flex_volume(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference, jsii.get(self, "flexVolume"))

    @builtins.property
    @jsii.member(jsii_name="flocker")
    def flocker(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference, jsii.get(self, "flocker"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDisk")
    def gce_persistent_disk(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference, jsii.get(self, "gcePersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="glusterfs")
    def glusterfs(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference, jsii.get(self, "glusterfs"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(
        self,
    ) -> PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference, jsii.get(self, "hostPath"))

    @builtins.property
    @jsii.member(jsii_name="iscsi")
    def iscsi(self) -> PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference, jsii.get(self, "iscsi"))

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference, jsii.get(self, "local"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(self) -> PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference:
        return typing.cast(PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDisk")
    def photon_persistent_disk(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference", jsii.get(self, "photonPersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="quobyte")
    def quobyte(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference", jsii.get(self, "quobyte"))

    @builtins.property
    @jsii.member(jsii_name="rbd")
    def rbd(self) -> "PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference", jsii.get(self, "rbd"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolume")
    def vsphere_volume(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference", jsii.get(self, "vsphereVolume"))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStoreInput")
    def aws_elastic_block_store_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "awsElasticBlockStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskInput")
    def azure_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk], jsii.get(self, "azureDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileInput")
    def azure_file_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile], jsii.get(self, "azureFileInput"))

    @builtins.property
    @jsii.member(jsii_name="cephFsInput")
    def ceph_fs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs], jsii.get(self, "cephFsInput"))

    @builtins.property
    @jsii.member(jsii_name="cinderInput")
    def cinder_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder], jsii.get(self, "cinderInput"))

    @builtins.property
    @jsii.member(jsii_name="csiInput")
    def csi_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi], jsii.get(self, "csiInput"))

    @builtins.property
    @jsii.member(jsii_name="fcInput")
    def fc_input(self) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc], jsii.get(self, "fcInput"))

    @builtins.property
    @jsii.member(jsii_name="flexVolumeInput")
    def flex_volume_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume], jsii.get(self, "flexVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="flockerInput")
    def flocker_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker], jsii.get(self, "flockerInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskInput")
    def gce_persistent_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "gcePersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="glusterfsInput")
    def glusterfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs], jsii.get(self, "glusterfsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInput")
    def iscsi_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi], jsii.get(self, "iscsiInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsInput")
    def nfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs], jsii.get(self, "nfsInput"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDiskInput")
    def photon_persistent_disk_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk"], jsii.get(self, "photonPersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="quobyteInput")
    def quobyte_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceQuobyte"], jsii.get(self, "quobyteInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdInput")
    def rbd_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbd"], jsii.get(self, "rbdInput"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolumeInput")
    def vsphere_volume_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceVsphereVolume"], jsii.get(self, "vsphereVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSource]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c84468f3fe9e3c0cdcb5e32f49d05f593e7e41f9ee0d0de099d9fc74ca9cf393)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={"pd_id": "pdId", "fs_type": "fsType"},
)
class PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk:
    def __init__(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1579c46f09bd91510cef450f644771fce159f892ae2a4f313bf12be5a6a78b69)
            check_type(argname="argument pd_id", value=pd_id, expected_type=type_hints["pd_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pd_id": pd_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def pd_id(self) -> builtins.str:
        '''ID that identifies Photon Controller persistent disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#pd_id PersistentVolume#pd_id}
        '''
        result = self._values.get("pd_id")
        assert result is not None, "Required property 'pd_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec4ceb56ea944d39bf131d51ddf682aa32274f0805fa8f0250ba040bf09f4ad4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pdIdInput")
    def pd_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955e4e2fe1dec9aa94ce979e21250275f3990ca6d6091dfc25a7b2777a78d5e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="pdId")
    def pd_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdId"))

    @pd_id.setter
    def pd_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41d196c904c9131c53761f0e2f93b8c6a68151c08895921516ccd07c4f87412)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa02e61bd3efd8e66b4c1e6de74c5f9750d357e098a3a325428d2e1d62ad32e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceQuobyte",
    jsii_struct_bases=[],
    name_mapping={
        "registry": "registry",
        "volume": "volume",
        "group": "group",
        "read_only": "readOnly",
        "user": "user",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceQuobyte:
    def __init__(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f26263c02066a7a3b8a3336dad3eb0e474a7b892a8c925eab875e7aee792f02)
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry": registry,
            "volume": volume,
        }
        if group is not None:
            self._values["group"] = group
        if read_only is not None:
            self._values["read_only"] = read_only
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def registry(self) -> builtins.str:
        '''Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#registry PersistentVolume#registry}
        '''
        result = self._values.get("registry")
        assert result is not None, "Required property 'registry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Volume is a string that references an already created Quobyte volume by name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume PersistentVolume#volume}
        '''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group to map volume access to Default is no group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#group PersistentVolume#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User to map volume access to Defaults to serivceaccount user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#user PersistentVolume#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceQuobyte(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42412a4816ccc8ed57415387aea3992c2298e0947d6a7ecb6a79b23624a66045)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51a9127acb2cef8ada889bf34eb306e02209d1344962c5fc7a3c0bd5406d663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__09efd4f2c56c1d6d9bff895076f45e7a1984e66dce88909be54186c3a711f419)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7392c69226e514d051633ec8a89bfde25f45b0ae2d77f75a952c0c94b3dfa44d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf4f40df7228d572004a131e55e742e044d40cd4ec1541de54a9d8e75dcde34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80fe21cb0bf39f6b56e96e33250520670f414346241c371e89287a80c8dc8bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5885498b2cc2892f782aad63fc4ee85efbc3ac4ef5d5f491e2879de1d58623e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbd",
    jsii_struct_bases=[],
    name_mapping={
        "ceph_monitors": "cephMonitors",
        "rbd_image": "rbdImage",
        "fs_type": "fsType",
        "keyring": "keyring",
        "rados_user": "radosUser",
        "rbd_pool": "rbdPool",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeSpecPersistentVolumeSourceRbd:
    def __init__(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d60c11dad5a229f29bfc0151c1f89829e9acfe541c052a4f4192e11a79d243d9)
            check_type(argname="argument ceph_monitors", value=ceph_monitors, expected_type=type_hints["ceph_monitors"])
            check_type(argname="argument rbd_image", value=rbd_image, expected_type=type_hints["rbd_image"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument keyring", value=keyring, expected_type=type_hints["keyring"])
            check_type(argname="argument rados_user", value=rados_user, expected_type=type_hints["rados_user"])
            check_type(argname="argument rbd_pool", value=rbd_pool, expected_type=type_hints["rbd_pool"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ceph_monitors": ceph_monitors,
            "rbd_image": rbd_image,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if keyring is not None:
            self._values["keyring"] = keyring
        if rados_user is not None:
            self._values["rados_user"] = rados_user
        if rbd_pool is not None:
            self._values["rbd_pool"] = rbd_pool
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def ceph_monitors(self) -> typing.List[builtins.str]:
        '''A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#ceph_monitors PersistentVolume#ceph_monitors}
        '''
        result = self._values.get("ceph_monitors")
        assert result is not None, "Required property 'ceph_monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rbd_image(self) -> builtins.str:
        '''The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_image PersistentVolume#rbd_image}
        '''
        result = self._values.get("rbd_image")
        assert result is not None, "Required property 'rbd_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyring(self) -> typing.Optional[builtins.str]:
        '''Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#keyring PersistentVolume#keyring}
        '''
        result = self._values.get("keyring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rados_user(self) -> typing.Optional[builtins.str]:
        '''The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rados_user PersistentVolume#rados_user}
        '''
        result = self._values.get("rados_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbd_pool(self) -> typing.Optional[builtins.str]:
        '''The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#rbd_pool PersistentVolume#rbd_pool}
        '''
        result = self._values.get("rbd_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#read_only PersistentVolume#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#secret_ref PersistentVolume#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceRbd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97a28edda862cca7be5954902c3d87b28d9608e5f62a999719b7fb0a145fbc0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        value = PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKeyring")
    def reset_keyring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyring", []))

    @jsii.member(jsii_name="resetRadosUser")
    def reset_rados_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadosUser", []))

    @jsii.member(jsii_name="resetRbdPool")
    def reset_rbd_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbdPool", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference":
        return typing.cast("PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitorsInput")
    def ceph_monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cephMonitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyringInput")
    def keyring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyringInput"))

    @builtins.property
    @jsii.member(jsii_name="radosUserInput")
    def rados_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radosUserInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdImageInput")
    def rbd_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdImageInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdPoolInput")
    def rbd_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitors")
    def ceph_monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cephMonitors"))

    @ceph_monitors.setter
    def ceph_monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cb1f9000e80bd537fe2d27a881bbcc3fcaca13daa58e4201d1f51899f8027f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cephMonitors", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__631679aee998ce49d3a90dda3ac2ae30b6f46919ca538a10d484e31a2fd817ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="keyring")
    def keyring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyring"))

    @keyring.setter
    def keyring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e197875fbe453dc08425531d973c223c9395a8f2b9a62e604609d8a3fb6b626)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyring", value)

    @builtins.property
    @jsii.member(jsii_name="radosUser")
    def rados_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radosUser"))

    @rados_user.setter
    def rados_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00bbb10ca0a6ab3aae1b1fa990b86535d8b03c998811df90974521a28c55fb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radosUser", value)

    @builtins.property
    @jsii.member(jsii_name="rbdImage")
    def rbd_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdImage"))

    @rbd_image.setter
    def rbd_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08998fa5646b914228922860a3db9c16e924eee1431b06d393c8c0ef0a898e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdImage", value)

    @builtins.property
    @jsii.member(jsii_name="rbdPool")
    def rbd_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdPool"))

    @rbd_pool.setter
    def rbd_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115cac1ed02278c28d5f5dda4547eb5cbb4e0c59c740c718c7a7e3383596aee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdPool", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__fda3e545547a6a26a3eadb6786142c5eb0d73438f4fa2ac5d760d31d12c22db2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8487034dda8590440593ebfe88cc6f7b6f97d1d66135ec26e62276745aa29ca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23640e0881ee2871dde0fa0c9d6b30b7ffdf7b6a651091271c0f6b1587cb478a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#name PersistentVolume#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#namespace PersistentVolume#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d55f9aa0463982b30856c33f0905c7a1ac3c41571984a56e552c9ca71d22ecd8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d700bfc73014404c3c1062a9b56108bb1133c64b406baf1e964df2930be5a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5962836d052f831717c951e141a6e138ca0d4aec45eec3eb32d9147d444f8f99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98bff6777a72b8ba89be685b5f5e1851b465161f95147be70b9212ff1af25fa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceVsphereVolume",
    jsii_struct_bases=[],
    name_mapping={"volume_path": "volumePath", "fs_type": "fsType"},
)
class PersistentVolumeSpecPersistentVolumeSourceVsphereVolume:
    def __init__(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd967930377787bced1ed899d5ee19fd3fab284b6fb1fb4cfbc3fc44cd5eed0)
            check_type(argname="argument volume_path", value=volume_path, expected_type=type_hints["volume_path"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_path": volume_path,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def volume_path(self) -> builtins.str:
        '''Path that identifies vSphere volume vmdk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#volume_path PersistentVolume#volume_path}
        '''
        result = self._values.get("volume_path")
        assert result is not None, "Required property 'volume_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#fs_type PersistentVolume#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeSpecPersistentVolumeSourceVsphereVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__216b9053310656bcc6fec2338a16d0eeb3d7242dd3ef7ca0d7b60f5f1318c49e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumePathInput")
    def volume_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumePathInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9acb0272d5fdd672cc946077f9218fb42557a5069923765e057605324595e4ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="volumePath")
    def volume_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumePath"))

    @volume_path.setter
    def volume_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed6c1c2c66cfc6d2d31600acbf32806d01869c8e912c28e10e9989dba0f0661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume]:
        return typing.cast(typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ca133daa0e1d5c62a14748f85dbcff29b71a10f23756b7e48e78888d4e3744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class PersistentVolumeTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1835900d84e01703e28ae97979f5a3765be17d9ab65dc78540ec2608ba9a963a)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume#create PersistentVolume#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolume.PersistentVolumeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4f1e2973e4830563ee541d3f808e5663e8ea9104802f1b43cc97ad3978db108)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e9eea9d476f5668d8b861e66a9baa8dfc0d8e7bcb833f0db0c2c19819cd0cb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6bd520be8bbdd722be4fd1ca5f0e181298a11f9c4ca3689c256d62ef855d291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PersistentVolume",
    "PersistentVolumeConfig",
    "PersistentVolumeMetadata",
    "PersistentVolumeMetadataOutputReference",
    "PersistentVolumeSpec",
    "PersistentVolumeSpecClaimRef",
    "PersistentVolumeSpecClaimRefOutputReference",
    "PersistentVolumeSpecList",
    "PersistentVolumeSpecNodeAffinity",
    "PersistentVolumeSpecNodeAffinityOutputReference",
    "PersistentVolumeSpecNodeAffinityRequired",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermOutputReference",
    "PersistentVolumeSpecNodeAffinityRequiredOutputReference",
    "PersistentVolumeSpecOutputReference",
    "PersistentVolumeSpecPersistentVolumeSource",
    "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore",
    "PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceAzureDisk",
    "PersistentVolumeSpecPersistentVolumeSourceAzureDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceAzureFile",
    "PersistentVolumeSpecPersistentVolumeSourceAzureFileOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCephFs",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCinder",
    "PersistentVolumeSpecPersistentVolumeSourceCinderOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsi",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceCsiOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFc",
    "PersistentVolumeSpecPersistentVolumeSourceFcOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolume",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceFlocker",
    "PersistentVolumeSpecPersistentVolumeSourceFlockerOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk",
    "PersistentVolumeSpecPersistentVolumeSourceGcePersistentDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceGlusterfs",
    "PersistentVolumeSpecPersistentVolumeSourceGlusterfsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceHostPath",
    "PersistentVolumeSpecPersistentVolumeSourceHostPathOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceIscsi",
    "PersistentVolumeSpecPersistentVolumeSourceIscsiOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceLocal",
    "PersistentVolumeSpecPersistentVolumeSourceLocalOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceNfs",
    "PersistentVolumeSpecPersistentVolumeSourceNfsOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk",
    "PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceQuobyte",
    "PersistentVolumeSpecPersistentVolumeSourceQuobyteOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceRbd",
    "PersistentVolumeSpecPersistentVolumeSourceRbdOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef",
    "PersistentVolumeSpecPersistentVolumeSourceRbdSecretRefOutputReference",
    "PersistentVolumeSpecPersistentVolumeSourceVsphereVolume",
    "PersistentVolumeSpecPersistentVolumeSourceVsphereVolumeOutputReference",
    "PersistentVolumeTimeouts",
    "PersistentVolumeTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__571dd23064a9e6f8f4fde39c1213906f742ee4d62430ed15c094e6f1790b840f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[PersistentVolumeMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PersistentVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__eda466cca8a7fcb2b33fec35d3cb2a8560d11aa85bc45b27a77b20a5bffbfa32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb98d2bfdec1563422506a47f82cea3c89784f25355629edcc9d8c727c818095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3763e04ed0b9162049c4fdf0868462a60fa9484be5fd4d58cdcdc9b48bea4380(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[PersistentVolumeMetadata, typing.Dict[builtins.str, typing.Any]],
    spec: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpec, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PersistentVolumeTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__809244eb2703375b712200509b3fecacb4c136175bffe83d138db59d505dadc1(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87998f2bcc1fcf14c5c13902f3a4c2bfc57d22308db9336ad2ff1ea7c8ecba2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c1096409656cb711a76177bc7a8877fda32abc886723e418fb3c722b867ce0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9bd23d14ccc68d2f5353e427212fa97a9e21edeb5c32e0e3fb9ab4d39f0928(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72caba99d9149c927b2f54542fe0670f2de1ddc782cf00c9b77d3ab8c7f829f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ededf8c469827b7f85796fb8533671d2e0ee1eadb92c145159815c7c960daac3(
    value: typing.Optional[PersistentVolumeMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd456ef86f01d297f8d4582fbfe979914f880df2ac4871331601a874e8311d6b(
    *,
    access_modes: typing.Sequence[builtins.str],
    capacity: typing.Mapping[builtins.str, builtins.str],
    persistent_volume_source: typing.Union[PersistentVolumeSpecPersistentVolumeSource, typing.Dict[builtins.str, typing.Any]],
    claim_ref: typing.Optional[typing.Union[PersistentVolumeSpecClaimRef, typing.Dict[builtins.str, typing.Any]]] = None,
    mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
    node_affinity: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinity, typing.Dict[builtins.str, typing.Any]]] = None,
    persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
    storage_class_name: typing.Optional[builtins.str] = None,
    volume_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e602117492fb7da813a6ca33a3dc82851025a2b3748e4959513eea35269784(
    *,
    name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__290a5aa558d8f77628371cb696994826a4749b9aaa16075a79dfc04205aa9313(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a7fe8ff486bd4179bf781142b9d2b4e65e2bc43444d52b70ea84aadfb9acac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7876f9e8ee39f4ee35b4a640d60d3f8d5c8c7a07599e485de8993dc3487b8be0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__951fd510abfa1b85f5df9a45ce5cdd0ed341e30ea9513fc6f3a2b0f31544b1e9(
    value: typing.Optional[PersistentVolumeSpecClaimRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9f33074c60369c9bd9b89942a66bdd666459d92ae41977075007b9b6743ffb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8249d312b88855e850334468f3de4f0f7179f6813ea063180f65702ac37345cb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceb320d250f2024e0982107937a730f02dd6ae456a2c2cfadb8c7d1b63fcf414(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81c735e2ed7c87fe0650df5f6eae2acb042fd8854f63cc09c18d1e574e341cc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df872801007d2a8372d1627df9ebda3fbd03c0c171b8bd59073a3921b9e225d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5720e81642e60e6380b569a2e01a55573838b47706b18a71f6b49b711e1d521e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpec]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6fb2d6174789e0dadfb2d39affa73fe6f4f4c69656a2282e0db9770c70b35d(
    *,
    required: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequired, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dab5d7f2eea301d264274e0052d52726e7df232187f4ff1062bfb2ca5e2be684(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2703aa257f17eb55e23215b42c6ae6f82cabfadac815b1caca7528ef9a46818f(
    value: typing.Optional[PersistentVolumeSpecNodeAffinity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd327867005215322bcef988af50289e5d26763d00d8a99f5290262ef89ed31(
    *,
    node_selector_term: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841c458ceeb7b87a7850fa92512b1321b3f842bbc08415a8dd9059efaaa22856(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_fields: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4df4d83b749296b7d590bd68cd38b019184f303fbfa8bccedb70ebbc16d27de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72aaa65a90b870a3435cc8a545fbd37e3686509399ef768684302a8563592acd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a18ad697e3c0ce1f48e3f4c09b74e7df2bcae1da4b4cf4083a1ca573340c26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbcab2c4ee80e48a1b0b9258bf99b6bbf2fe1037b1a0412d12ce95ff9d2960ce(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e6b628d5176dfb240ef573f7497384d2f9954bc5b6bc9b8b2025a534d3f97f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2cdc3340d2109a3343aea7c1901b33135e5a37e41e0dc2b5e9e86c6823e4cc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e490a3a17f1a72e443a794f6e400e1c982b23e81fbf62ab2024d46535ddad7(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__735bbc6e66eff740f5bac171f5295c9d9a52692f62b55daef48072d5cb49db3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928266139e4f536830eefc01c1bc868791e4226cd21e46c842ef4ea72ee4a74b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57387b6f7d631a9c1f234cf5bfc1816dd176480bcb171b4b4e31a00719573380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75b1981f0e480c78f9e44bdf410ae7e6ed31e3cac78516bd37e3b32a9518238(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0206ec7f0d1381af7d5282f6d162ca90643b4a4f84a9a0cced0cfd15d33aa7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b31928962bd453d5e6925c30eb884e5386695006f115d68ead9013a6b4c468e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ff0eb73ce28b79bd31e8db79a5e6cac19e98fff86ce261546a17e1349286f96(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ddf162a7e206ecad9efdb2aa887c2bfcfda209977d4e54fc3c15ea857c284b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d4344eb696d9d46c6a3c409a0a95711b419ba03bf4b7f5ddc89927bcaa27ec8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f13370a2379d2e0a4ead372b0d556923c537691740ae8f47d7c0a8613031e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459b3a73627354ebbc4191aea48dd7e9ad8778b09e64d0b29eca5bf03a30e04d(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c680a3ab1c1645de5093b59c917f8e5ecd7e240679866c08ccdae1d3fea34d47(
    *,
    key: builtins.str,
    operator: builtins.str,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48884470f555763d8ed42d6ca10df23daf47ef7f64a613495874438af44c5106(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c72cbf74334c4e0e2b4c2221a784cfe38bd35e56d26710d2897ab211db9ac18(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19f467968ef149e872c1d17b5077236ce64db53c119e94d466f3c79f127e9b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a252e10d0e6d72a4b870bde47ad55cd6d5082135622bb89b04609a5ebfd1ee2f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8bd4c38d461fe569df453bc389b813700bd13f573d7c34b70720cd0bf53eb1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c48c813f9c1cd6c87eb875a5356cbc6ff4e9587f1a8739cf23688e3543afce5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eabc23768f7824d0d59fcbb4850ef9f33ac79c9f34dc76c15bde118f1bb3cb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd1654989a3c665ff3a77b511ca3b6145ccdc0454c1fb70fbcdcb4e1be2d0cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ecddaf7dcc61a4eeb58a6df00093d6e768c83b25937da109eabb1e827573749(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138f26c2e5db920c9fdf35522e5a6798a002203d79f9f82f88985ddf1aeb12c3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c192035360585fbd6b014e3a620acbccd85ef2996fc7cdfb760c6c518514430(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325f9f5050d852167f5822e8390750a0e0f8d6943fd622aa675bd4d0d88457f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8be17e70968408bcc213fe4a5073242b57fdaec6093b1812bb6bc3c7682ea3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf28f0567f1d3d2e6778842018c29192771a4e3bd50653d92b5b0d1825404e7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a45eca8f2e352c3fce7698183629fbfd302a4a2249bf361b2b636f8032d1eb5(
    value: typing.Optional[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41f4c623f4ac0bec5d4fb32a7a70ad7903ccfd795c3599b5bce2e80c87fcf42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa01a710f30e125c46800fc9b04914984059fb8586acea30eee92d7e92627a75(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PersistentVolumeSpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33cf927ea2dd9fe0f8eeaa5a80661b349d350ce27f3f7fdae4131e4fb2561b1a(
    value: typing.Optional[PersistentVolumeSpecNodeAffinityRequired],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57088624504c449ea6614aebde35b5418b418fe1e5b3d1dcde4f96c56a8eef95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603f8678d5870e90df2909e99ade7abb1d195b4b97cda84fee7632a8a48afc96(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761cf6e4b0ce0114425a64791cec7caeef88f966b859437e44a4787075df8320(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d139f694c5ce63b10f596910d95a5cbf0134a5ffa929e5183edd9a2cdd119eb7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae23fef58cfacf30a0833bd56697f6c4e0d41474fb4d0740672eb807b7a7d06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637bc758a9dd785890b7181454eaaa7383021d1d7c073ef197d65b82ce7216dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f8b5817ce7a661d5338729cfdac4c09d26a98fcf2a70d5686e567d6583f800f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c12cf626fbb7ab0119a9ff25c7c2a817d700eb61d022520846a017088f199d(
    value: typing.Optional[typing.Union[PersistentVolumeSpec, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc40aec29680e95f449909c7d358c5c287f48c1a1ba48c39613a9d4b31e28086(
    *,
    aws_elastic_block_store: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAzureDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_file: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceAzureFile, typing.Dict[builtins.str, typing.Any]]] = None,
    ceph_fs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFs, typing.Dict[builtins.str, typing.Any]]] = None,
    cinder: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCinder, typing.Dict[builtins.str, typing.Any]]] = None,
    csi: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsi, typing.Dict[builtins.str, typing.Any]]] = None,
    fc: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFc, typing.Dict[builtins.str, typing.Any]]] = None,
    flex_volume: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolume, typing.Dict[builtins.str, typing.Any]]] = None,
    flocker: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlocker, typing.Dict[builtins.str, typing.Any]]] = None,
    gce_persistent_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    glusterfs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceGlusterfs, typing.Dict[builtins.str, typing.Any]]] = None,
    host_path: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceHostPath, typing.Dict[builtins.str, typing.Any]]] = None,
    iscsi: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceIscsi, typing.Dict[builtins.str, typing.Any]]] = None,
    local: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceLocal, typing.Dict[builtins.str, typing.Any]]] = None,
    nfs: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceNfs, typing.Dict[builtins.str, typing.Any]]] = None,
    photon_persistent_disk: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    quobyte: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceQuobyte, typing.Dict[builtins.str, typing.Any]]] = None,
    rbd: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceRbd, typing.Dict[builtins.str, typing.Any]]] = None,
    vsphere_volume: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__741a16139cfa367cb716be8134f385801adc61159ce8935285e21026ab3f0736(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa06e58a08f7e05725902301a4b867a24c65dd6bda3b9957aa2192fbcb92795(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bff97efa6813190d58cc97fcbf1fa7ea9d10d6b6102bc8b7d700a2e4faf77c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8468322e7b5dc6018762f54432fc77a8c5f94f518ba96f7dec7b9cb4eb93af03(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6064edf30586bab85338bdd7316af7a3c737506a3d20e0615e83352e94c32079(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796b8353fe5f017afecb87c24e5792509fbc52e614e5d6369c3ddfbb9e180962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ac43221e900ffe25d39cbe1c6c81abd606e4de290cfd495644fa12bdc42a67(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAwsElasticBlockStore],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e790150315dd2741cab598f528f5a450185203af2dec3036412b3292fe3487bf(
    *,
    caching_mode: builtins.str,
    data_disk_uri: builtins.str,
    disk_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    kind: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f3e30e727de082080c17eed535fdf701c0cae809b57b678c08d5dada7ec00a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45ca9ea52ca441a8fcff211143242dc4e44aa95c218da3d9c3b5ff5a37c338e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79395e5d7a7f492c922c505bf961cf2840741eb599edc9258ccd3475dde8542(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387f3a4466171e0bf4d0f4b763005f32268cb1b79a08774850f09388ac53fb76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f470d6f54109bfde6db7e66a62e8a92d7baabb5b4b0bc2b183609277d836db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c7c8e6f7918d4b54f01f14ec33b566c02cfd82732151dac9249b3a3b1a68b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0374146b9ff870b2d010bf2e2020b95cbbaf5059519303365c5a263153978eae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f36542c5ba03bfbe717ab617395b6f708fa560ac76f82d6133d0470e4c635f5(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__347f0f32b0cfd834d2dd1d95b75b3a6928880a028e21ec174d47f45986062573(
    *,
    secret_name: builtins.str,
    share_name: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7775f8ec8935e3b2eaf16a00928623c5923d5cfa3526dbe6735bb26f45459961(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833752376d84fd73ef17b1531bbccc0ca933bbfd98f5e17886ac94a483e8cb56(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44dffc6358aece5f84e07c7e140a9ac8780b3d16d2d2c544dccae08c485c7cf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61106469a5eca17d0c2b59601fec24974275f714a599523944feab6bd72cdb1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ab49751beeb0849f7167c2a3672b98bc2a9198315eb787de8312d445bc1058(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856fa03af4d9f31d61eb870c9fb37c6356dd8717fdc28541f770facdeb37a7d0(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceAzureFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d86d06d48877c23f6cd672019c3fda8f2f4698df7d348248904855cad95ed4(
    *,
    monitors: typing.Sequence[builtins.str],
    path: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_file: typing.Optional[builtins.str] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b5dcab5da8788d99dd7ff4fec1d86b0443ec170bd2e6cde444b11d37e2e1c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09898e5446e993982a11c97eb3adeedabafecb2351077ce966b1bb8d8230a19b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8862c8590b54d8726772bddf03e3381909fa342b27e55c6e7ec394634474dd5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c56a0c65af5502a64a6884f90085d2d3d2acd02d2dc589ee2add4f02bdf7aa5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092e3f0afb7419a5427a1b52b9b2f9a8a86f83dc7fd020bb94c2a6f57f344443(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba1726ed09db39846e4f7a99179514638986438ed54dae6a94d6c133f84c2c33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db3b780d1456af120f5e3ea49df5eabc22b3ef57bbe9a4600f3c0fe1ccc0995(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21cc3004ccfbd40a60fc4df59b2f51b2108210e13e211f574a0f010ce1177b99(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbbb328506833f9464bd1cd4c9780d9faea343519f6cb0683d14154d636a241(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1095d2756174df15d6614af96d61d581bda9e4d6863b1a203347bd716200d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__549ed057a5c6f188f39a49c73c9c76c6fdcc8e04b774d3e98de1eb2997215f16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe73073cc544af7c00db29bed48fa9f6e4858cd6e2e5117e9e68935c2ee4bdcd(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCephFsSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d2b306e5293f0372e432293ef4ba7b101308cc9b817f2999317a8c42041810(
    *,
    volume_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dafec68fa560502e5bfa374d513af2f515b84588315a0c90d5907b20493a01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6351f474af639aacd434ad4507fc5bfa87fd307b24da4ee5c8a35214c31a407d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ef9e285eaed6ce7e013a37e536fb985f21a55a87ca81f440608f5faef34ac5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fc1683806209ed5f22847d4562acc255a2b14695d70aba0395a8f3b90f54b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24320630f61f8e48aa786dbc3c7d30f8af977da891f2d17ece5447e7366f9258(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCinder],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8cc1f5ae61e1b02b0173960288c32b32a155a757af3912f1d224b0a258d68bd(
    *,
    driver: builtins.str,
    volume_handle: builtins.str,
    controller_expand_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    controller_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    fs_type: typing.Optional[builtins.str] = None,
    node_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    node_stage_secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204856ea75d673734ef8a66cb92042cb860c5619c30bfcc9b4257dec8963ddfd(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9571715b61271f7464633f8e6e17aeda6b3de5695232f2df44fcdd13e7a60568(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277ca4d632f39227fd15f5dece6946745fec45301b1a18ab8122d4512843d950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b313554d87e30abf55923da0f5d85449ef873f5c143ebcf4495d07eb008dc732(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3f0c185a09bef0769b8a8715e96eaa7d15467eca6db91211f8a056681755c3(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerExpandSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493582cf93c32304ac1a69f4cd843e9836ddc7100ed3eaa80fd81d3471a8b8ed(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a1fb7786f5416d688bdba96b9ec4fb9e365362c32771b6d2380884f681abf9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b412a02e9603425c8391e1cf08ea90ee04381a0b3a6a8f53eafe15ee8fa6ef7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f7064943df90471ae11955e1ac91900c97f2ee1791cd29e71598547f0b8d54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e5d34d0464348e4bace174f10df99bce97fd27bc3b98f4806cf18ae9b6a757(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiControllerPublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b01fbaadf2fffa7d85a7af40ad04923c524b6c95de044bf08b7c2daeeb2d01(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f745c0500573491effd8ff5f0e0798de29a4bbb54bb7cbd332d22e312a13ec9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e137285df1d4bb505aa302b07ec187e399a6d2c762d49595c1a7a102fd6ebc53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed75a9f748287df11522d113fc05cd49427282f7b947cd55de2c7567739bdf32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b13f98befe6fe2bcbe3f3963965b409526b5ca4659444d1a062ea4f72ba1bb(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodePublishSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7633206a5658f1eda3fa296be8a4ca3e4c7cfca38b987b69fd7b02136d8f8d2c(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf05fd13abaafb720d0ede77268e06c5e17877d9b3807f1fe1d189ec74330e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78919df8293d0d14702b71d8722e59d9448d3a0960c9c2f763dbf3c8f89586c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911e231bdb2806929f2858edf9ebb4327c693fb07c7b26a7b73e9c75c9f780df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62679391de3e4314059aa7abad25093d78682d4c4dd96c2124025be3e1b087bf(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsiNodeStageSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37baed910e2cdba44cccd68a8f606bea775addae6917685e8561d510d9468ffc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3b69e904ae8dfe9c226a13187c1c2daa610c4225410cad4a1dc9b68399f0b27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3257943b3189bce78b907018cc9eb7ecb10a501188fe430e7f361405ebe51ec9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f169b347667c134a7697623d70c70ee239acab6f8fa46997c0cabbda56b94b59(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e68e8e4d4779084de2fdb81b04898f115f742f11e16a9ff92395a29fc87bf8(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93060697ebd67bcc533110d0206cf966f8d0bac691364c4d6aec994b4dd52f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4486f1a6520ed520167fbd322039433cccbe78616581e5722a6a8c72dabb0a59(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceCsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77807467c0087e74ac5c45a976183418652b6e30c83327d5168c6472bf56350c(
    *,
    lun: jsii.Number,
    target_ww_ns: typing.Sequence[builtins.str],
    fs_type: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57992b16094cda9842feee65eb15ed2efff6b1e723cc09d5b847ab27535f4be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5c4f632ccf04f3c4e625bd208b19f28c7e3edbe16aa6207f0b2cf9be2a1202(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8a23766709bf361fc38c4cca11a53d0bdc1b7997bd4bf7b9eb90968290d809(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5753ef43382dd0b2293d473aff510f1a47dbc70d6c46893e8b2a1a6f3c9e71(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ed1516aa6ffa05a7a42410550f5f068d8905f69a8dbd8ccf26d69302341d61(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091fae0041b4ee7b36e7cd9b3092d2b7b71b007e1a703eb5e985cbb58c3090f1(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0228801f16cc0a0f7e0db2751d7319c8dd2a899c2f2781de3c655382ea1865(
    *,
    driver: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceec9ee4418624ff7eb0def24f642ebf0349ecf901016a95bae455f51978b96(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea46be7e1400c980c6d103c7fea31cd869bc6b89bedf57938b2ae55f8171020(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032412c9d25e452c49461528335a5e4e0bc0b2eebfbed7c61fe7b3e57ec87445(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43bf55ede2dce7764475544dae248f503df7b57f58f978bbdc4797d5003eb5a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165017ed2777eff0eaeb747acf78cbd64bc94942a771adcbf830bdda935e0cca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8cff150448fed8edd575e3927b9e5b40b4965b647c1efd26ad56bd7ac64d70(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6de0c555f77fe22b803b9995ece59f4bcbbb3035a89538942a6c02cce8714b9(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccdf25b6e713366f76de0ae878d78f5635f3c1ea1874b1221b11f722ca4557ae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__458467b1e21ba8fb71f698bcbb9b7de1e88c0fc163315024d0e0931708512556(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09ce3653bc941551df3599688ec33e7659b495a6f213f14ab8a9f6d3da1588e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac75b9c125a9df38d6d5f2a4e4d2f275eada56c8ba5545c634a769c761fd724c(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlexVolumeSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa2db6620e566c282735d2f7285d477cd9829a56bad7dd5f1b625385a60410d(
    *,
    dataset_name: typing.Optional[builtins.str] = None,
    dataset_uuid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736bf27761e106844fe1ea183bea39c2ea7833ec26813d34a49c9ca59642d579(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600d284d9415275095b9e29230ad5ee24790232e59f38df167e172e9b07831a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feb7a76d67ff4767166a9aec8e3cc6235070cce3cb022e063a8f97ea80c7535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cfae432c3ca55167534d8a1946191658a625df0e088b25087830e4e435d3dd5(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceFlocker],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a858ca03c24ce9ec529ad09189a0429970e7227c16e45dcf712efe05bef092e(
    *,
    pd_name: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    partition: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57466fe3b338dd604fa85eb495e2681bb7c4f46b09275ad9e014b444c3ed779a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4299a698dc7a132888115d7cb158c4254f26785414f74384ebd80289ba89497d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e52f37c99fd51ab217361a5569498ec15433db9469b88a50c259100b6be98b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9aa5f88cff12a7a3f1dba322a7cc78b708a4ee1408082486f520c739058956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416920b6a3a5705e78dce5a1f6598f404282ae26fc89829c6ca2d9a45bf82d55(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0d34015738d478accf903fdbd0ac8a3800d103623dbd4ec2bc07b5a554f2d3(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGcePersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a013afd8a20fca1f5cfe017bd3c50879f80510c5fe445829906a19ef139ced5(
    *,
    endpoints_name: builtins.str,
    path: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83bb7000744f0ea2ab1bc0758f08dbca27211265224d5e5c8a58f1b9334a1650(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adcba58752787ed65e5e165b49614e93848fc38b89d6f5a38200e98054fe119(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43ff5e3049d6ce247f7fb1de936ee8169b44853ffb2c301d0c548760c591c74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c86356fe0c24cd91c45f6c9bc4c1e704ff14b6bf41fb3d1f7b1760ee75b4c6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b87bd60daac7cf700f94f24fe018d71428417e7bf76c289bfaeceff7cf6fa2e1(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceGlusterfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad95a54a00b56346390fbe47e70507a04d30617e19e45bc9975020e5f279a60(
    *,
    path: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be6a070ce6fd456ccbc00738b643f3202da84a3ab497216d8736f493e4ccb81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5a4ee459aa4c188c675a9b50276920a406b5d4e7ac88d753694fce8e41603e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606f8fac81518a5720756800f90a5c08431d8d3c7bccc800d6b2ba8cd8933f99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530a63ef3d30472c929db708a35cd4148e955da5d27b7ca81d7b8c49a07e0d38(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceHostPath],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b7688993e4f1fb35afe31ab1a61386be7891f38451cdd07bddec5cfba8fd6d2(
    *,
    iqn: builtins.str,
    target_portal: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    iscsi_interface: typing.Optional[builtins.str] = None,
    lun: typing.Optional[jsii.Number] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3418aa845e287053afaeb452c31fd06f85e5eb40d3a642b338fc7457c56211(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5ec2e779af680c40a08b71b7654379e87df17847ec97585e5ecd8b0b9de720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f4d44d839f4af5257b844379926336d6b859f4024da754c28ee89d7117093b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7ac64d894ad41d13bf0842118f00f0ad976680a80217f450ccb2f5243010b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9961c74eeb5059d00e306712d8b1110af052492618f892aa84289cf1884f2b26(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f284344ff51f9a098e2111da173349dd99f0a8ce9a325407e0d674a2ec4db7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5858e8e594a1402422e19f4794a2cae769d297f8270e0577e2042b9ac79a1d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d3c9feb432d29292b79b76650b4a95126189624f3905827856778c93dfb38c3(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceIscsi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0dd09f634b821bd60026ff1069b11f7e72b0252b63a59c2ccaa69b5adbe3a68(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ad78a34dfd4790fce3600052c4d3d8bf51129d7bfbea4a35de4234ea0336b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4141e595736728907fcaa38b3d31a8dd740339af67861cfb9b58c467b489b6c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c333ba07bfc1e71514fa247685288c05fc0b8bc938b81a71e57c7687d03dab(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceLocal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242b7f69bb1a4c3854adfc4e7f3fab1ab4154cf5a24cfae3f6ade3e23e379da0(
    *,
    path: builtins.str,
    server: builtins.str,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0340ef6686deb43442fe18a0cf3a6b0d264f481eabf72182f4627f7a059da2b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53cd497dd5701fe50e6333273d2693f89d6f84d8d894e4034ffc7aa935c50b58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a83c22d5ffffbec99b506d644e97c31a2561c614004bf5956e142bb11c3a78c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77d8b7358173d029d025253c3411d63c386a9b04d36ce8a72788cee674b86dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc54b5d25aab3419a08bf6d841311bd01d3d9f977651bab3c71b8d74f70978e(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceNfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a558e1dd4be6ef91fa57da0b9f5d4606d284f76001ed7b561efc9f0008f58bd8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84468f3fe9e3c0cdcb5e32f49d05f593e7e41f9ee0d0de099d9fc74ca9cf393(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1579c46f09bd91510cef450f644771fce159f892ae2a4f313bf12be5a6a78b69(
    *,
    pd_id: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4ceb56ea944d39bf131d51ddf682aa32274f0805fa8f0250ba040bf09f4ad4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955e4e2fe1dec9aa94ce979e21250275f3990ca6d6091dfc25a7b2777a78d5e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41d196c904c9131c53761f0e2f93b8c6a68151c08895921516ccd07c4f87412(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa02e61bd3efd8e66b4c1e6de74c5f9750d357e098a3a325428d2e1d62ad32e8(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourcePhotonPersistentDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f26263c02066a7a3b8a3336dad3eb0e474a7b892a8c925eab875e7aee792f02(
    *,
    registry: builtins.str,
    volume: builtins.str,
    group: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42412a4816ccc8ed57415387aea3992c2298e0947d6a7ecb6a79b23624a66045(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51a9127acb2cef8ada889bf34eb306e02209d1344962c5fc7a3c0bd5406d663(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09efd4f2c56c1d6d9bff895076f45e7a1984e66dce88909be54186c3a711f419(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7392c69226e514d051633ec8a89bfde25f45b0ae2d77f75a952c0c94b3dfa44d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf4f40df7228d572004a131e55e742e044d40cd4ec1541de54a9d8e75dcde34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80fe21cb0bf39f6b56e96e33250520670f414346241c371e89287a80c8dc8bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5885498b2cc2892f782aad63fc4ee85efbc3ac4ef5d5f491e2879de1d58623e2(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceQuobyte],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60c11dad5a229f29bfc0151c1f89829e9acfe541c052a4f4192e11a79d243d9(
    *,
    ceph_monitors: typing.Sequence[builtins.str],
    rbd_image: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
    keyring: typing.Optional[builtins.str] = None,
    rados_user: typing.Optional[builtins.str] = None,
    rbd_pool: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret_ref: typing.Optional[typing.Union[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a28edda862cca7be5954902c3d87b28d9608e5f62a999719b7fb0a145fbc0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cb1f9000e80bd537fe2d27a881bbcc3fcaca13daa58e4201d1f51899f8027f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631679aee998ce49d3a90dda3ac2ae30b6f46919ca538a10d484e31a2fd817ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e197875fbe453dc08425531d973c223c9395a8f2b9a62e604609d8a3fb6b626(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00bbb10ca0a6ab3aae1b1fa990b86535d8b03c998811df90974521a28c55fb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08998fa5646b914228922860a3db9c16e924eee1431b06d393c8c0ef0a898e60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115cac1ed02278c28d5f5dda4547eb5cbb4e0c59c740c718c7a7e3383596aee0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda3e545547a6a26a3eadb6786142c5eb0d73438f4fa2ac5d760d31d12c22db2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8487034dda8590440593ebfe88cc6f7b6f97d1d66135ec26e62276745aa29ca1(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbd],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23640e0881ee2871dde0fa0c9d6b30b7ffdf7b6a651091271c0f6b1587cb478a(
    *,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55f9aa0463982b30856c33f0905c7a1ac3c41571984a56e552c9ca71d22ecd8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d700bfc73014404c3c1062a9b56108bb1133c64b406baf1e964df2930be5a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5962836d052f831717c951e141a6e138ca0d4aec45eec3eb32d9147d444f8f99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98bff6777a72b8ba89be685b5f5e1851b465161f95147be70b9212ff1af25fa1(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceRbdSecretRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd967930377787bced1ed899d5ee19fd3fab284b6fb1fb4cfbc3fc44cd5eed0(
    *,
    volume_path: builtins.str,
    fs_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__216b9053310656bcc6fec2338a16d0eeb3d7242dd3ef7ca0d7b60f5f1318c49e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9acb0272d5fdd672cc946077f9218fb42557a5069923765e057605324595e4ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed6c1c2c66cfc6d2d31600acbf32806d01869c8e912c28e10e9989dba0f0661(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ca133daa0e1d5c62a14748f85dbcff29b71a10f23756b7e48e78888d4e3744(
    value: typing.Optional[PersistentVolumeSpecPersistentVolumeSourceVsphereVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1835900d84e01703e28ae97979f5a3765be17d9ab65dc78540ec2608ba9a963a(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f1e2973e4830563ee541d3f808e5663e8ea9104802f1b43cc97ad3978db108(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e9eea9d476f5668d8b861e66a9baa8dfc0d8e7bcb833f0db0c2c19819cd0cb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6bd520be8bbdd722be4fd1ca5f0e181298a11f9c4ca3689c256d62ef855d291(
    value: typing.Optional[typing.Union[PersistentVolumeTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
