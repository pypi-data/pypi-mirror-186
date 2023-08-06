'''
# `kubernetes_validating_webhook_configuration_v1`

Refer to the Terraform Registory for docs: [`kubernetes_validating_webhook_configuration_v1`](https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1).
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


class ValidatingWebhookConfigurationV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1 kubernetes_validating_webhook_configuration_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ValidatingWebhookConfigurationV1Metadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1 kubernetes_validating_webhook_configuration_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#metadata ValidatingWebhookConfigurationV1#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#webhook ValidatingWebhookConfigurationV1#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#id ValidatingWebhookConfigurationV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446da1283b551f7aee5b180af749472e96d6604e2278fa27ef78457751719562)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ValidatingWebhookConfigurationV1Config(
            metadata=metadata,
            webhook=webhook,
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
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#annotations ValidatingWebhookConfigurationV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#generate_name ValidatingWebhookConfigurationV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#labels ValidatingWebhookConfigurationV1#labels}
        :param name: Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        '''
        value = ValidatingWebhookConfigurationV1Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putWebhook")
    def put_webhook(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b476f2e237de812bcebd98bc62473157cdeb153a1d1e6f18d027a325f530759a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhook", [value]))

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
    def metadata(self) -> "ValidatingWebhookConfigurationV1MetadataOutputReference":
        return typing.cast("ValidatingWebhookConfigurationV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> "ValidatingWebhookConfigurationV1WebhookList":
        return typing.cast("ValidatingWebhookConfigurationV1WebhookList", jsii.get(self, "webhook"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationV1Metadata"]:
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1Webhook"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1Webhook"]]], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de35ee6d79e007ef74578a019579b83d4aaa516e612d7d6296d10e79d0460b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1Config",
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
        "webhook": "webhook",
        "id": "id",
    },
)
class ValidatingWebhookConfigurationV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ValidatingWebhookConfigurationV1Metadata", typing.Dict[builtins.str, typing.Any]],
        webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1Webhook", typing.Dict[builtins.str, typing.Any]]]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#metadata ValidatingWebhookConfigurationV1#metadata}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#webhook ValidatingWebhookConfigurationV1#webhook}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#id ValidatingWebhookConfigurationV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ValidatingWebhookConfigurationV1Metadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01df406d9d75e723df6b3531717c23c73f0ae37dfb1318be156fd550b833e2e8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "webhook": webhook,
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
    def metadata(self) -> "ValidatingWebhookConfigurationV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#metadata ValidatingWebhookConfigurationV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ValidatingWebhookConfigurationV1Metadata", result)

    @builtins.property
    def webhook(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1Webhook"]]:
        '''webhook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#webhook ValidatingWebhookConfigurationV1#webhook}
        '''
        result = self._values.get("webhook")
        assert result is not None, "Required property 'webhook' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1Webhook"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#id ValidatingWebhookConfigurationV1#id}.

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
        return "ValidatingWebhookConfigurationV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class ValidatingWebhookConfigurationV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#annotations ValidatingWebhookConfigurationV1#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#generate_name ValidatingWebhookConfigurationV1#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#labels ValidatingWebhookConfigurationV1#labels}
        :param name: Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198d78eaa51225d01fc50ddac48ece7fa07e3a938e215ad0bd08041b237a797d)
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
        '''An unstructured key value map stored with the validating webhook configuration that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#annotations ValidatingWebhookConfigurationV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#generate_name ValidatingWebhookConfigurationV1#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the validating webhook configuration.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#labels ValidatingWebhookConfigurationV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the validating webhook configuration, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f19f0e50ea1cf8923f04d2c7ccc8ead3e4d4e6f39e47ead81f9b6fda7124ff9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ffb63ad0d18d00ef4a7333856d3acb7745ab46ed5b21fd149e86bca6a73e1aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ddf2e4882572361c588c05ea66458498da0f5f9b73120e1e91ae79f15cda6cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e788c84bd056f3cd6c72c241873aff4d079da6208221dfee9efd1b8331ca7a32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa07157d8bf1e221f9d58304b9d882801bfdbd9c85016799b2781ff7be0607b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1Metadata]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e67ff5f1938fd04ebd1a51d86ff967d00e8dc2fd3031cf2075573a64e624055a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1Webhook",
    jsii_struct_bases=[],
    name_mapping={
        "client_config": "clientConfig",
        "name": "name",
        "admission_review_versions": "admissionReviewVersions",
        "failure_policy": "failurePolicy",
        "match_policy": "matchPolicy",
        "namespace_selector": "namespaceSelector",
        "object_selector": "objectSelector",
        "rule": "rule",
        "side_effects": "sideEffects",
        "timeout_seconds": "timeoutSeconds",
    },
)
class ValidatingWebhookConfigurationV1Webhook:
    def __init__(
        self,
        *,
        client_config: typing.Union["ValidatingWebhookConfigurationV1WebhookClientConfig", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        failure_policy: typing.Optional[builtins.str] = None,
        match_policy: typing.Optional[builtins.str] = None,
        namespace_selector: typing.Optional[typing.Union["ValidatingWebhookConfigurationV1WebhookNamespaceSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        object_selector: typing.Optional[typing.Union["ValidatingWebhookConfigurationV1WebhookObjectSelector", typing.Dict[builtins.str, typing.Any]]] = None,
        rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1WebhookRule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        side_effects: typing.Optional[builtins.str] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#client_config ValidatingWebhookConfigurationV1#client_config}
        :param name: The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        :param admission_review_versions: AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#admission_review_versions ValidatingWebhookConfigurationV1#admission_review_versions}
        :param failure_policy: FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#failure_policy ValidatingWebhookConfigurationV1#failure_policy}
        :param match_policy: matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent". - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook. - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook. Defaults to "Equivalent" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_policy ValidatingWebhookConfigurationV1#match_policy}
        :param namespace_selector: namespace_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#namespace_selector ValidatingWebhookConfigurationV1#namespace_selector}
        :param object_selector: object_selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#object_selector ValidatingWebhookConfigurationV1#object_selector}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#rule ValidatingWebhookConfigurationV1#rule}
        :param side_effects: SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#side_effects ValidatingWebhookConfigurationV1#side_effects}
        :param timeout_seconds: TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#timeout_seconds ValidatingWebhookConfigurationV1#timeout_seconds}
        '''
        if isinstance(client_config, dict):
            client_config = ValidatingWebhookConfigurationV1WebhookClientConfig(**client_config)
        if isinstance(namespace_selector, dict):
            namespace_selector = ValidatingWebhookConfigurationV1WebhookNamespaceSelector(**namespace_selector)
        if isinstance(object_selector, dict):
            object_selector = ValidatingWebhookConfigurationV1WebhookObjectSelector(**object_selector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0184f7860f69a04a02a5d7b3dbf0a4e5bcac01942de3042c496c221db116206f)
            check_type(argname="argument client_config", value=client_config, expected_type=type_hints["client_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument admission_review_versions", value=admission_review_versions, expected_type=type_hints["admission_review_versions"])
            check_type(argname="argument failure_policy", value=failure_policy, expected_type=type_hints["failure_policy"])
            check_type(argname="argument match_policy", value=match_policy, expected_type=type_hints["match_policy"])
            check_type(argname="argument namespace_selector", value=namespace_selector, expected_type=type_hints["namespace_selector"])
            check_type(argname="argument object_selector", value=object_selector, expected_type=type_hints["object_selector"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument side_effects", value=side_effects, expected_type=type_hints["side_effects"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_config": client_config,
            "name": name,
        }
        if admission_review_versions is not None:
            self._values["admission_review_versions"] = admission_review_versions
        if failure_policy is not None:
            self._values["failure_policy"] = failure_policy
        if match_policy is not None:
            self._values["match_policy"] = match_policy
        if namespace_selector is not None:
            self._values["namespace_selector"] = namespace_selector
        if object_selector is not None:
            self._values["object_selector"] = object_selector
        if rule is not None:
            self._values["rule"] = rule
        if side_effects is not None:
            self._values["side_effects"] = side_effects
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def client_config(self) -> "ValidatingWebhookConfigurationV1WebhookClientConfig":
        '''client_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#client_config ValidatingWebhookConfigurationV1#client_config}
        '''
        result = self._values.get("client_config")
        assert result is not None, "Required property 'client_config' is missing"
        return typing.cast("ValidatingWebhookConfigurationV1WebhookClientConfig", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the admission webhook.

        Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admission_review_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AdmissionReviewVersions is an ordered list of preferred ``AdmissionReview`` versions the Webhook expects.

        API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#admission_review_versions ValidatingWebhookConfigurationV1#admission_review_versions}
        '''
        result = self._values.get("admission_review_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def failure_policy(self) -> typing.Optional[builtins.str]:
        '''FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail.

        Defaults to Fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#failure_policy ValidatingWebhookConfigurationV1#failure_policy}
        '''
        result = self._values.get("failure_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match_policy(self) -> typing.Optional[builtins.str]:
        '''matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".

        - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.
        - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included ``apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]``, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.

        Defaults to "Equivalent"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_policy ValidatingWebhookConfigurationV1#match_policy}
        '''
        result = self._values.get("match_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_selector(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationV1WebhookNamespaceSelector"]:
        '''namespace_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#namespace_selector ValidatingWebhookConfigurationV1#namespace_selector}
        '''
        result = self._values.get("namespace_selector")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationV1WebhookNamespaceSelector"], result)

    @builtins.property
    def object_selector(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationV1WebhookObjectSelector"]:
        '''object_selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#object_selector ValidatingWebhookConfigurationV1#object_selector}
        '''
        result = self._values.get("object_selector")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationV1WebhookObjectSelector"], result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#rule ValidatingWebhookConfigurationV1#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookRule"]]], result)

    @builtins.property
    def side_effects(self) -> typing.Optional[builtins.str]:
        '''SideEffects states whether this webhook has side effects.

        Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#side_effects ValidatingWebhookConfigurationV1#side_effects}
        '''
        result = self._values.get("side_effects")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''TimeoutSeconds specifies the timeout for this webhook.

        After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#timeout_seconds ValidatingWebhookConfigurationV1#timeout_seconds}
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1Webhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookClientConfig",
    jsii_struct_bases=[],
    name_mapping={"ca_bundle": "caBundle", "service": "service", "url": "url"},
)
class ValidatingWebhookConfigurationV1WebhookClientConfig:
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union["ValidatingWebhookConfigurationV1WebhookClientConfigService", typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#ca_bundle ValidatingWebhookConfigurationV1#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#service ValidatingWebhookConfigurationV1#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#url ValidatingWebhookConfigurationV1#url}
        '''
        if isinstance(service, dict):
            service = ValidatingWebhookConfigurationV1WebhookClientConfigService(**service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b679ece456b988ce28bb3c376959c1fb860237f08b7a44321f7e466fcdb4ed)
            check_type(argname="argument ca_bundle", value=ca_bundle, expected_type=type_hints["ca_bundle"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_bundle is not None:
            self._values["ca_bundle"] = ca_bundle
        if service is not None:
            self._values["service"] = service
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def ca_bundle(self) -> typing.Optional[builtins.str]:
        '''``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate.

        If unspecified, system trust roots on the apiserver are used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#ca_bundle ValidatingWebhookConfigurationV1#ca_bundle}
        '''
        result = self._values.get("ca_bundle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationV1WebhookClientConfigService"]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#service ValidatingWebhookConfigurationV1#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationV1WebhookClientConfigService"], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``).

        Exactly one of ``url`` or ``service`` must be specified.

        The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address.

        Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.

        The scheme must be "https"; the URL must begin with "https://".

        A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.

        Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#url ValidatingWebhookConfigurationV1#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1WebhookClientConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookClientConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfd25332fd886fea762fe2d578aac8c7434aa86d527fb666ab07001ed39afb73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#namespace ValidatingWebhookConfigurationV1#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#path ValidatingWebhookConfigurationV1#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#port ValidatingWebhookConfigurationV1#port}
        '''
        value = ValidatingWebhookConfigurationV1WebhookClientConfigService(
            name=name, namespace=namespace, path=path, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetCaBundle")
    def reset_ca_bundle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaBundle", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(
        self,
    ) -> "ValidatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference":
        return typing.cast("ValidatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="caBundleInput")
    def ca_bundle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caBundleInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional["ValidatingWebhookConfigurationV1WebhookClientConfigService"]:
        return typing.cast(typing.Optional["ValidatingWebhookConfigurationV1WebhookClientConfigService"], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="caBundle")
    def ca_bundle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caBundle"))

    @ca_bundle.setter
    def ca_bundle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ecd609943c2b29850b00cfb803a9c834c8dbb08b425509c5ff03f381937ae10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caBundle", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1c8b6a994921499fc0741358c3ecb9325406c2b675e148c090c15ed1703959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61b7bc2219e5c9b286ab2dc079b8eea192bf8be4f09cde976991e98907ead74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookClientConfigService",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "namespace": "namespace",
        "path": "path",
        "port": "port",
    },
)
class ValidatingWebhookConfigurationV1WebhookClientConfigService:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: builtins.str,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: ``name`` is the name of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        :param namespace: ``namespace`` is the namespace of the service. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#namespace ValidatingWebhookConfigurationV1#namespace}
        :param path: ``path`` is an optional URL path which will be sent in any request to this service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#path ValidatingWebhookConfigurationV1#path}
        :param port: If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#port ValidatingWebhookConfigurationV1#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c501aaddcedc95055e38f18c00b06d199b0ea43ec4db2f66fb8b991ffd38a8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "namespace": namespace,
        }
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def name(self) -> builtins.str:
        '''``name`` is the name of the service. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#name ValidatingWebhookConfigurationV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''``namespace`` is the namespace of the service. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#namespace ValidatingWebhookConfigurationV1#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''``path`` is an optional URL path which will be sent in any request to this service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#path ValidatingWebhookConfigurationV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''If specified, the port on the service that hosting webhook.

        Default to 443 for backward compatibility. ``port`` should be a valid port number (1-65535, inclusive).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#port ValidatingWebhookConfigurationV1#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookClientConfigService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0ca2b5dcd938c38442e48db33681483e9536c9973a28a824421900dec173ad2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35913ab74ce368dd8aa168fcf966e51f45f1c26a07973ada1b7d3a075da00f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01296ea2e41b948dc6e9ead6489b54843b9fa245c74edd82b060016bc16334dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be3533e2e2c1e6211d8848f43097d4203de029f7eafb1f797d0010221c784ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5baa87e5fa02976100181eabdb5014e4b95c789164abedf7fee1392edc809b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfigService]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfigService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfigService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0eb39c47b9cbaeb2627b3d9262967152da41357fe8ab6a0c88a082e9f983fe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc0837929b3c9c10a803e7ece448c6c599395ce5aea4c8db11f449a7fb5c617a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationV1WebhookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fa133aa38de06166dc6fa0f4b178d7ee46d37479025e5af197ae793242f9a5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationV1WebhookOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5a777cabacf2d4cff3962f35e9e38ef636a06fe1e07ec5060482ee26367d03c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__388b3dcf5fbe748b4e7c91c5f5e7a8a375cd845621104ccd4b555cd442738422)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8aae8a1cb41c1a0db8d8eefbf0e111d1e11be03def72c60e6b35dc785be3a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1Webhook]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1Webhook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1Webhook]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4fb1936555703c654e908ad3651a4716351c584fcd33271227e787c81596eed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookNamespaceSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ValidatingWebhookConfigurationV1WebhookNamespaceSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5273ba8d9693a6f6172bae2c5dfa2f582623dc5803d219b60ce559fe7b60b9fa)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookNamespaceSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#key ValidatingWebhookConfigurationV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operator ValidatingWebhookConfigurationV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#values ValidatingWebhookConfigurationV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69bb4b91752b6397026db87ff239f363c08db7f4dd3e25ec44b4c49c4587e929)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#key ValidatingWebhookConfigurationV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operator ValidatingWebhookConfigurationV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#values ValidatingWebhookConfigurationV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f6e44010d42e4b46341e094bbfe2fd1a6feec986670289ff910812910c4d219)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e5e1945460c88f76b4a1e5611bb5080319858b69f790b337f33a2666a233164)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c08d4b78b01552c71ffa7d22d1d662289d61a0d9053ebec6999a4ad9c5d79951)
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
            type_hints = typing.get_type_hints(_typecheckingstub__136cfadee2e3c1288cbc4be190d7ebb457808c6e6505b0e532f0eac05efebb47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3209d8444e15cb522627443b630afed7c64062d5207efc93855e4da1d50d24af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbc924ed27757ba04fe70a03f8a8a8f6672869551b70a32b945e9e6d24409ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f746a826fd5a2783784c82e1b9b1c67a76ef655701b53d546937847a3f2efc03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d904ab8b3644b183d8caa82dcdfb740ad18a9831e37f8b27fcba85c71ab0539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb23ada9bd8659f63a32d1e3e4a7cf388b23b2a9f4e29ca252a39904728a719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d1f90c511a992327a79be6acd4b4989f595d812bc65995ec5a0adebe193bf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473c1a6ae5b6c36ad46eee76e38307fe6a9f6649b1823b2530301bed1e2732d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__51bfc242aacecee73ce95103a816a9fd7058af27226187c48dc8d13dc55961f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd224411a542a82de1ea16b6f4b5457f8c75230a927d38b33bde018a12e2f1b)
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
    ) -> ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList:
        return typing.cast(ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a1d77cf9a7c3c16133c72d1b4087e12f5b31ee76a7fbd8c1357272d145081a9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b4eb4a7fb885428526e3ef99d536897fd22322ca51df3a53e9752009f47b4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookObjectSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class ValidatingWebhookConfigurationV1WebhookObjectSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b11e7c27b5dca96d2f305d3a2a50ea2b7b4714ce80b5e86bca20cf1965dba2)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookObjectSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#key ValidatingWebhookConfigurationV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operator ValidatingWebhookConfigurationV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#values ValidatingWebhookConfigurationV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d9226156760d7f09f63c48b37fe49b37e2340c4c7821982ce027784b369e193)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#key ValidatingWebhookConfigurationV1#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operator ValidatingWebhookConfigurationV1#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#values ValidatingWebhookConfigurationV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9204590319bcf67acf4adb3d829437a4f5308aab65fcafc5029540becec51d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6ff88c6b899cc0de64f411e895952ddaa5b0e79cc9b1cf5d5ebe121a77dd11)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5c8d3c62cb526b63b3caeb26481fc6f3b06b447ab8c55f67b5ef2641612b49)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae2b44600e24ce914d6d679825976791765244444b7bf0b7d986bfbc958baa90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a873db01f90ead8e00ade4656c05bff20e0fccf2a71df4c107df948c5395ccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8a8cc7dfc9269dc90ed22c468b642591fc3fdcd3fa653d7b7675f87ecf735a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8a64523f37c45413ba67a987104c3a8bcaae4b728378b05d03a9404db72c976)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ae089a0ba3039fccd8fa963f210d224c2e46972aa7ef70c9816468db30f05f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdabece14015150d34ece82e9e55afb9072d488d64ce3caa0cf8426df6f5744a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f550fed8319595893569391cbfb5f0c82d6bb8f5506710b0c85db3d6e72324a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d527612089a9b5482f1a22fcfde93820a5d77bf1e20a101c764b8245735690e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookObjectSelectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookObjectSelectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b6035ca86cedb4a6a6c7426bc9ad6a0ad163d53b9622d12bd09753686bc2b03)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5a2118283f0d798dc03e565367aacdcfb5c015fd027d1841c777c3291987c1)
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
    ) -> ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList:
        return typing.cast(ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__da442c6a447fdc6bdce8635dae1159a98b29378a633b83b5b12db004439e4f9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856f30c6d9c66265598c7605874a6abf236486e890b564c9b849c97511d251f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05c21745bad3b8426a4cab838bf90590e4059644bd3c3854bbdb0d62a8f9f061)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClientConfig")
    def put_client_config(
        self,
        *,
        ca_bundle: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_bundle: ``caBundle`` is a PEM encoded CA bundle which will be used to validate the webhook's server certificate. If unspecified, system trust roots on the apiserver are used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#ca_bundle ValidatingWebhookConfigurationV1#ca_bundle}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#service ValidatingWebhookConfigurationV1#service}
        :param url: ``url`` gives the location of the webhook, in standard URL form (``scheme://host:port/path``). Exactly one of ``url`` or ``service`` must be specified. The ``host`` should not refer to a service running in the cluster; use the ``service`` field instead. The host might be resolved via external DNS in some apiservers (e.g., ``kube-apiserver`` cannot resolve in-cluster DNS as that would be a layering violation). ``host`` may also be an IP address. Please note that using ``localhost`` or ``127.0.0.1`` as a ``host`` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster. The scheme must be "https"; the URL must begin with "https://". A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier. Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#...") and query parameters ("?...") are not allowed, either. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#url ValidatingWebhookConfigurationV1#url}
        '''
        value = ValidatingWebhookConfigurationV1WebhookClientConfig(
            ca_bundle=ca_bundle, service=service, url=url
        )

        return typing.cast(None, jsii.invoke(self, "putClientConfig", [value]))

    @jsii.member(jsii_name="putNamespaceSelector")
    def put_namespace_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        value = ValidatingWebhookConfigurationV1WebhookNamespaceSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putNamespaceSelector", [value]))

    @jsii.member(jsii_name="putObjectSelector")
    def put_object_selector(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_expressions ValidatingWebhookConfigurationV1#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#match_labels ValidatingWebhookConfigurationV1#match_labels}
        '''
        value = ValidatingWebhookConfigurationV1WebhookObjectSelector(
            match_expressions=match_expressions, match_labels=match_labels
        )

        return typing.cast(None, jsii.invoke(self, "putObjectSelector", [value]))

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ValidatingWebhookConfigurationV1WebhookRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c9d98c7c00121fac426212e30633aa4736117fd365479fcf8e527689f753bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetAdmissionReviewVersions")
    def reset_admission_review_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdmissionReviewVersions", []))

    @jsii.member(jsii_name="resetFailurePolicy")
    def reset_failure_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailurePolicy", []))

    @jsii.member(jsii_name="resetMatchPolicy")
    def reset_match_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchPolicy", []))

    @jsii.member(jsii_name="resetNamespaceSelector")
    def reset_namespace_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceSelector", []))

    @jsii.member(jsii_name="resetObjectSelector")
    def reset_object_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectSelector", []))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @jsii.member(jsii_name="resetSideEffects")
    def reset_side_effects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSideEffects", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="clientConfig")
    def client_config(
        self,
    ) -> ValidatingWebhookConfigurationV1WebhookClientConfigOutputReference:
        return typing.cast(ValidatingWebhookConfigurationV1WebhookClientConfigOutputReference, jsii.get(self, "clientConfig"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelector")
    def namespace_selector(
        self,
    ) -> ValidatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference:
        return typing.cast(ValidatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference, jsii.get(self, "namespaceSelector"))

    @builtins.property
    @jsii.member(jsii_name="objectSelector")
    def object_selector(
        self,
    ) -> ValidatingWebhookConfigurationV1WebhookObjectSelectorOutputReference:
        return typing.cast(ValidatingWebhookConfigurationV1WebhookObjectSelectorOutputReference, jsii.get(self, "objectSelector"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ValidatingWebhookConfigurationV1WebhookRuleList":
        return typing.cast("ValidatingWebhookConfigurationV1WebhookRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="admissionReviewVersionsInput")
    def admission_review_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "admissionReviewVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigInput")
    def client_config_input(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig], jsii.get(self, "clientConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="failurePolicyInput")
    def failure_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failurePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPolicyInput")
    def match_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceSelectorInput")
    def namespace_selector_input(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector], jsii.get(self, "namespaceSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="objectSelectorInput")
    def object_selector_input(
        self,
    ) -> typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector]:
        return typing.cast(typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector], jsii.get(self, "objectSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ValidatingWebhookConfigurationV1WebhookRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="sideEffectsInput")
    def side_effects_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sideEffectsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="admissionReviewVersions")
    def admission_review_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "admissionReviewVersions"))

    @admission_review_versions.setter
    def admission_review_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb1c647e0c8ed4da74b5c86f09f62416a008b9da79d6159532ad86056c58d83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admissionReviewVersions", value)

    @builtins.property
    @jsii.member(jsii_name="failurePolicy")
    def failure_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failurePolicy"))

    @failure_policy.setter
    def failure_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e30003649a8b7fd0e6d23c004ddaa8ba967b5c4b1231d0d493ca3ea9df2ebf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failurePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="matchPolicy")
    def match_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matchPolicy"))

    @match_policy.setter
    def match_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d487cd3f50db053bf9da1b87ecc1784ac1d992a5b764258167d44349cfcd83a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440ac708ac3f28281bb9ddfb6ce10e93c0fb4f576892d28abc752cd7c3f65e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sideEffects")
    def side_effects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sideEffects"))

    @side_effects.setter
    def side_effects(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d4763ba26571ee6b5307663979cae457ef58fe63db65cffce70534f0f5693b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sideEffects", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__babaa0187eb670816676c397ca0da6affba715e148401377cf9995a7c4fea6aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__783a87bb2820704611948ce6b66274a37b3ea058311a08283f89aa364c944faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookRule",
    jsii_struct_bases=[],
    name_mapping={
        "api_groups": "apiGroups",
        "api_versions": "apiVersions",
        "operations": "operations",
        "resources": "resources",
        "scope": "scope",
    },
)
class ValidatingWebhookConfigurationV1WebhookRule:
    def __init__(
        self,
        *,
        api_groups: typing.Sequence[builtins.str],
        api_versions: typing.Sequence[builtins.str],
        operations: typing.Sequence[builtins.str],
        resources: typing.Sequence[builtins.str],
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#api_groups ValidatingWebhookConfigurationV1#api_groups}.
        :param api_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#api_versions ValidatingWebhookConfigurationV1#api_versions}.
        :param operations: Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operations ValidatingWebhookConfigurationV1#operations}
        :param resources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#resources ValidatingWebhookConfigurationV1#resources}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#scope ValidatingWebhookConfigurationV1#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e3e229dd8c8d973f89a1e1b288513190f34bcd9f0df3268951f59ca68c9a5c)
            check_type(argname="argument api_groups", value=api_groups, expected_type=type_hints["api_groups"])
            check_type(argname="argument api_versions", value=api_versions, expected_type=type_hints["api_versions"])
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_groups": api_groups,
            "api_versions": api_versions,
            "operations": operations,
            "resources": resources,
        }
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def api_groups(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#api_groups ValidatingWebhookConfigurationV1#api_groups}.'''
        result = self._values.get("api_groups")
        assert result is not None, "Required property 'api_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def api_versions(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#api_versions ValidatingWebhookConfigurationV1#api_versions}.'''
        result = self._values.get("api_versions")
        assert result is not None, "Required property 'api_versions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operations(self) -> typing.List[builtins.str]:
        '''Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added.

        If '*' is present, the length of the slice must be one. Required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#operations ValidatingWebhookConfigurationV1#operations}
        '''
        result = self._values.get("operations")
        assert result is not None, "Required property 'operations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#resources ValidatingWebhookConfigurationV1#resources}.'''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/validating_webhook_configuration_v1#scope ValidatingWebhookConfigurationV1#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidatingWebhookConfigurationV1WebhookRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidatingWebhookConfigurationV1WebhookRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fe8366769646243f5057f3bb6e974c0fa8b1e833ba95ec0c808efa74f173bb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ValidatingWebhookConfigurationV1WebhookRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f963dd8de40c3e1d378f30780211c8c03bb75ff8ab233850d4e8a73333e78a3b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ValidatingWebhookConfigurationV1WebhookRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1782a255e81cd8ab4e59c3338931ca767f183e3b03680f79724229be32bb48ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9da5e77f072833db872705160ea6e64b749d0a96cc3313c880833969450eaf8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9e682c6b45584ee21b1acd397f773bfb1333e619f48cc07778c61a3dcf8f359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7cdec94db47963860f7289a7680455f5e5853dbb6153b56756f9db98830b51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ValidatingWebhookConfigurationV1WebhookRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.validatingWebhookConfigurationV1.ValidatingWebhookConfigurationV1WebhookRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08cf6969dcdbaae86c59725db5b43c8702f7ab7938711eeff8983917ae614a35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="apiGroupsInput")
    def api_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionsInput")
    def api_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroups")
    def api_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiGroups"))

    @api_groups.setter
    def api_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2180c7eeced394a1181a68cc75f1f5381ce6155b3b69213486d0a22a381c1d7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroups", value)

    @builtins.property
    @jsii.member(jsii_name="apiVersions")
    def api_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiVersions"))

    @api_versions.setter
    def api_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b5baaed1b442de90bbf88fe72f0d0f0a1522d160daa02af7ba14973a4865d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersions", value)

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "operations"))

    @operations.setter
    def operations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f1aebb4c916f4d812491e2a345b378a5a6ca8ce012320ddf9982ba0af68523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operations", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a07e688bb729ae69d6d66f1b927b4785c46690ea2edd91da2d068a2eb1ce3b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f10d7e895fc821e3fef481c8323df47b71867f5af4d16a0cc9d9b23ea1173458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8ed7f677f712a500b09b2a7a69da31849662fb42b12998f0cc1549bf4802a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ValidatingWebhookConfigurationV1",
    "ValidatingWebhookConfigurationV1Config",
    "ValidatingWebhookConfigurationV1Metadata",
    "ValidatingWebhookConfigurationV1MetadataOutputReference",
    "ValidatingWebhookConfigurationV1Webhook",
    "ValidatingWebhookConfigurationV1WebhookClientConfig",
    "ValidatingWebhookConfigurationV1WebhookClientConfigOutputReference",
    "ValidatingWebhookConfigurationV1WebhookClientConfigService",
    "ValidatingWebhookConfigurationV1WebhookClientConfigServiceOutputReference",
    "ValidatingWebhookConfigurationV1WebhookList",
    "ValidatingWebhookConfigurationV1WebhookNamespaceSelector",
    "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions",
    "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsList",
    "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressionsOutputReference",
    "ValidatingWebhookConfigurationV1WebhookNamespaceSelectorOutputReference",
    "ValidatingWebhookConfigurationV1WebhookObjectSelector",
    "ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions",
    "ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsList",
    "ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressionsOutputReference",
    "ValidatingWebhookConfigurationV1WebhookObjectSelectorOutputReference",
    "ValidatingWebhookConfigurationV1WebhookOutputReference",
    "ValidatingWebhookConfigurationV1WebhookRule",
    "ValidatingWebhookConfigurationV1WebhookRuleList",
    "ValidatingWebhookConfigurationV1WebhookRuleOutputReference",
]

publication.publish()

def _typecheckingstub__446da1283b551f7aee5b180af749472e96d6604e2278fa27ef78457751719562(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ValidatingWebhookConfigurationV1Metadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__b476f2e237de812bcebd98bc62473157cdeb153a1d1e6f18d027a325f530759a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de35ee6d79e007ef74578a019579b83d4aaa516e612d7d6296d10e79d0460b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01df406d9d75e723df6b3531717c23c73f0ae37dfb1318be156fd550b833e2e8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ValidatingWebhookConfigurationV1Metadata, typing.Dict[builtins.str, typing.Any]],
    webhook: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1Webhook, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198d78eaa51225d01fc50ddac48ece7fa07e3a938e215ad0bd08041b237a797d(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    generate_name: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19f0e50ea1cf8923f04d2c7ccc8ead3e4d4e6f39e47ead81f9b6fda7124ff9c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffb63ad0d18d00ef4a7333856d3acb7745ab46ed5b21fd149e86bca6a73e1aa(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ddf2e4882572361c588c05ea66458498da0f5f9b73120e1e91ae79f15cda6cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e788c84bd056f3cd6c72c241873aff4d079da6208221dfee9efd1b8331ca7a32(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa07157d8bf1e221f9d58304b9d882801bfdbd9c85016799b2781ff7be0607b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67ff5f1938fd04ebd1a51d86ff967d00e8dc2fd3031cf2075573a64e624055a(
    value: typing.Optional[ValidatingWebhookConfigurationV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0184f7860f69a04a02a5d7b3dbf0a4e5bcac01942de3042c496c221db116206f(
    *,
    client_config: typing.Union[ValidatingWebhookConfigurationV1WebhookClientConfig, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    admission_review_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    failure_policy: typing.Optional[builtins.str] = None,
    match_policy: typing.Optional[builtins.str] = None,
    namespace_selector: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    object_selector: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelector, typing.Dict[builtins.str, typing.Any]]] = None,
    rule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    side_effects: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b679ece456b988ce28bb3c376959c1fb860237f08b7a44321f7e466fcdb4ed(
    *,
    ca_bundle: typing.Optional[builtins.str] = None,
    service: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookClientConfigService, typing.Dict[builtins.str, typing.Any]]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd25332fd886fea762fe2d578aac8c7434aa86d527fb666ab07001ed39afb73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecd609943c2b29850b00cfb803a9c834c8dbb08b425509c5ff03f381937ae10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1c8b6a994921499fc0741358c3ecb9325406c2b675e148c090c15ed1703959(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61b7bc2219e5c9b286ab2dc079b8eea192bf8be4f09cde976991e98907ead74(
    value: typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c501aaddcedc95055e38f18c00b06d199b0ea43ec4db2f66fb8b991ffd38a8(
    *,
    name: builtins.str,
    namespace: builtins.str,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ca2b5dcd938c38442e48db33681483e9536c9973a28a824421900dec173ad2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35913ab74ce368dd8aa168fcf966e51f45f1c26a07973ada1b7d3a075da00f46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01296ea2e41b948dc6e9ead6489b54843b9fa245c74edd82b060016bc16334dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be3533e2e2c1e6211d8848f43097d4203de029f7eafb1f797d0010221c784ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5baa87e5fa02976100181eabdb5014e4b95c789164abedf7fee1392edc809b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0eb39c47b9cbaeb2627b3d9262967152da41357fe8ab6a0c88a082e9f983fe4(
    value: typing.Optional[ValidatingWebhookConfigurationV1WebhookClientConfigService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc0837929b3c9c10a803e7ece448c6c599395ce5aea4c8db11f449a7fb5c617a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fa133aa38de06166dc6fa0f4b178d7ee46d37479025e5af197ae793242f9a5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a777cabacf2d4cff3962f35e9e38ef636a06fe1e07ec5060482ee26367d03c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__388b3dcf5fbe748b4e7c91c5f5e7a8a375cd845621104ccd4b555cd442738422(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8aae8a1cb41c1a0db8d8eefbf0e111d1e11be03def72c60e6b35dc785be3a35(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4fb1936555703c654e908ad3651a4716351c584fcd33271227e787c81596eed(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1Webhook]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5273ba8d9693a6f6172bae2c5dfa2f582623dc5803d219b60ce559fe7b60b9fa(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69bb4b91752b6397026db87ff239f363c08db7f4dd3e25ec44b4c49c4587e929(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6e44010d42e4b46341e094bbfe2fd1a6feec986670289ff910812910c4d219(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e5e1945460c88f76b4a1e5611bb5080319858b69f790b337f33a2666a233164(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c08d4b78b01552c71ffa7d22d1d662289d61a0d9053ebec6999a4ad9c5d79951(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136cfadee2e3c1288cbc4be190d7ebb457808c6e6505b0e532f0eac05efebb47(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3209d8444e15cb522627443b630afed7c64062d5207efc93855e4da1d50d24af(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc924ed27757ba04fe70a03f8a8a8f6672869551b70a32b945e9e6d24409ff3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f746a826fd5a2783784c82e1b9b1c67a76ef655701b53d546937847a3f2efc03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d904ab8b3644b183d8caa82dcdfb740ad18a9831e37f8b27fcba85c71ab0539(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb23ada9bd8659f63a32d1e3e4a7cf388b23b2a9f4e29ca252a39904728a719(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d1f90c511a992327a79be6acd4b4989f595d812bc65995ec5a0adebe193bf0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473c1a6ae5b6c36ad46eee76e38307fe6a9f6649b1823b2530301bed1e2732d7(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51bfc242aacecee73ce95103a816a9fd7058af27226187c48dc8d13dc55961f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd224411a542a82de1ea16b6f4b5457f8c75230a927d38b33bde018a12e2f1b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookNamespaceSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d77cf9a7c3c16133c72d1b4087e12f5b31ee76a7fbd8c1357272d145081a9c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b4eb4a7fb885428526e3ef99d536897fd22322ca51df3a53e9752009f47b4a(
    value: typing.Optional[ValidatingWebhookConfigurationV1WebhookNamespaceSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b11e7c27b5dca96d2f305d3a2a50ea2b7b4714ce80b5e86bca20cf1965dba2(
    *,
    match_expressions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d9226156760d7f09f63c48b37fe49b37e2340c4c7821982ce027784b369e193(
    *,
    key: typing.Optional[builtins.str] = None,
    operator: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9204590319bcf67acf4adb3d829437a4f5308aab65fcafc5029540becec51d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6ff88c6b899cc0de64f411e895952ddaa5b0e79cc9b1cf5d5ebe121a77dd11(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5c8d3c62cb526b63b3caeb26481fc6f3b06b447ab8c55f67b5ef2641612b49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2b44600e24ce914d6d679825976791765244444b7bf0b7d986bfbc958baa90(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a873db01f90ead8e00ade4656c05bff20e0fccf2a71df4c107df948c5395ccb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8a8cc7dfc9269dc90ed22c468b642591fc3fdcd3fa653d7b7675f87ecf735a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a64523f37c45413ba67a987104c3a8bcaae4b728378b05d03a9404db72c976(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ae089a0ba3039fccd8fa963f210d224c2e46972aa7ef70c9816468db30f05f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdabece14015150d34ece82e9e55afb9072d488d64ce3caa0cf8426df6f5744a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f550fed8319595893569391cbfb5f0c82d6bb8f5506710b0c85db3d6e72324a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d527612089a9b5482f1a22fcfde93820a5d77bf1e20a101c764b8245735690e(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b6035ca86cedb4a6a6c7426bc9ad6a0ad163d53b9622d12bd09753686bc2b03(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5a2118283f0d798dc03e565367aacdcfb5c015fd027d1841c777c3291987c1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookObjectSelectorMatchExpressions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da442c6a447fdc6bdce8635dae1159a98b29378a633b83b5b12db004439e4f9c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856f30c6d9c66265598c7605874a6abf236486e890b564c9b849c97511d251f5(
    value: typing.Optional[ValidatingWebhookConfigurationV1WebhookObjectSelector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c21745bad3b8426a4cab838bf90590e4059644bd3c3854bbdb0d62a8f9f061(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c9d98c7c00121fac426212e30633aa4736117fd365479fcf8e527689f753bc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb1c647e0c8ed4da74b5c86f09f62416a008b9da79d6159532ad86056c58d83(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e30003649a8b7fd0e6d23c004ddaa8ba967b5c4b1231d0d493ca3ea9df2ebf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d487cd3f50db053bf9da1b87ecc1784ac1d992a5b764258167d44349cfcd83a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440ac708ac3f28281bb9ddfb6ce10e93c0fb4f576892d28abc752cd7c3f65e5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4763ba26571ee6b5307663979cae457ef58fe63db65cffce70534f0f5693b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babaa0187eb670816676c397ca0da6affba715e148401377cf9995a7c4fea6aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783a87bb2820704611948ce6b66274a37b3ea058311a08283f89aa364c944faf(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1Webhook, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e3e229dd8c8d973f89a1e1b288513190f34bcd9f0df3268951f59ca68c9a5c(
    *,
    api_groups: typing.Sequence[builtins.str],
    api_versions: typing.Sequence[builtins.str],
    operations: typing.Sequence[builtins.str],
    resources: typing.Sequence[builtins.str],
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe8366769646243f5057f3bb6e974c0fa8b1e833ba95ec0c808efa74f173bb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f963dd8de40c3e1d378f30780211c8c03bb75ff8ab233850d4e8a73333e78a3b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1782a255e81cd8ab4e59c3338931ca767f183e3b03680f79724229be32bb48ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9da5e77f072833db872705160ea6e64b749d0a96cc3313c880833969450eaf8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e682c6b45584ee21b1acd397f773bfb1333e619f48cc07778c61a3dcf8f359(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7cdec94db47963860f7289a7680455f5e5853dbb6153b56756f9db98830b51(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ValidatingWebhookConfigurationV1WebhookRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08cf6969dcdbaae86c59725db5b43c8702f7ab7938711eeff8983917ae614a35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2180c7eeced394a1181a68cc75f1f5381ce6155b3b69213486d0a22a381c1d7b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b5baaed1b442de90bbf88fe72f0d0f0a1522d160daa02af7ba14973a4865d0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45f1aebb4c916f4d812491e2a345b378a5a6ca8ce012320ddf9982ba0af68523(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a07e688bb729ae69d6d66f1b927b4785c46690ea2edd91da2d068a2eb1ce3b1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f10d7e895fc821e3fef481c8323df47b71867f5af4d16a0cc9d9b23ea1173458(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8ed7f677f712a500b09b2a7a69da31849662fb42b12998f0cc1549bf4802a4(
    value: typing.Optional[typing.Union[ValidatingWebhookConfigurationV1WebhookRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
