'''
# `kubernetes_cluster_role_binding_v1`

Refer to the Terraform Registory for docs: [`kubernetes_cluster_role_binding_v1`](https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1).
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


class ClusterRoleBindingV1(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1 kubernetes_cluster_role_binding_v1}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["ClusterRoleBindingV1Metadata", typing.Dict[builtins.str, typing.Any]],
        role_ref: typing.Union["ClusterRoleBindingV1RoleRef", typing.Dict[builtins.str, typing.Any]],
        subject: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterRoleBindingV1Subject", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1 kubernetes_cluster_role_binding_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#metadata ClusterRoleBindingV1#metadata}
        :param role_ref: role_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#role_ref ClusterRoleBindingV1#role_ref}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#subject ClusterRoleBindingV1#subject}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#id ClusterRoleBindingV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0b3fa2e0a0edd410240c71f8ffa30653a94c0772445893d941584cf2a3b7a65)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ClusterRoleBindingV1Config(
            metadata=metadata,
            role_ref=role_ref,
            subject=subject,
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
        :param annotations: An unstructured key value map stored with the clusterRoleBinding that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#annotations ClusterRoleBindingV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the clusterRoleBinding. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#labels ClusterRoleBindingV1#labels}
        :param name: Name of the clusterRoleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        value = ClusterRoleBindingV1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putRoleRef")
    def put_role_ref(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#api_group ClusterRoleBindingV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#kind ClusterRoleBindingV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        value = ClusterRoleBindingV1RoleRef(api_group=api_group, kind=kind, name=name)

        return typing.cast(None, jsii.invoke(self, "putRoleRef", [value]))

    @jsii.member(jsii_name="putSubject")
    def put_subject(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterRoleBindingV1Subject", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22e05f6352b546d787e4c857fc6b89fb9433209263bc24b6673c26179bad5f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubject", [value]))

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
    def metadata(self) -> "ClusterRoleBindingV1MetadataOutputReference":
        return typing.cast("ClusterRoleBindingV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="roleRef")
    def role_ref(self) -> "ClusterRoleBindingV1RoleRefOutputReference":
        return typing.cast("ClusterRoleBindingV1RoleRefOutputReference", jsii.get(self, "roleRef"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> "ClusterRoleBindingV1SubjectList":
        return typing.cast("ClusterRoleBindingV1SubjectList", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["ClusterRoleBindingV1Metadata"]:
        return typing.cast(typing.Optional["ClusterRoleBindingV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="roleRefInput")
    def role_ref_input(self) -> typing.Optional["ClusterRoleBindingV1RoleRef"]:
        return typing.cast(typing.Optional["ClusterRoleBindingV1RoleRef"], jsii.get(self, "roleRefInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterRoleBindingV1Subject"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterRoleBindingV1Subject"]]], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903dacfc7346b114d1e032d507d890c9ba7960d943a4d4e406fd8694026cda0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1Config",
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
        "role_ref": "roleRef",
        "subject": "subject",
        "id": "id",
    },
)
class ClusterRoleBindingV1Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metadata: typing.Union["ClusterRoleBindingV1Metadata", typing.Dict[builtins.str, typing.Any]],
        role_ref: typing.Union["ClusterRoleBindingV1RoleRef", typing.Dict[builtins.str, typing.Any]],
        subject: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterRoleBindingV1Subject", typing.Dict[builtins.str, typing.Any]]]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#metadata ClusterRoleBindingV1#metadata}
        :param role_ref: role_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#role_ref ClusterRoleBindingV1#role_ref}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#subject ClusterRoleBindingV1#subject}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#id ClusterRoleBindingV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = ClusterRoleBindingV1Metadata(**metadata)
        if isinstance(role_ref, dict):
            role_ref = ClusterRoleBindingV1RoleRef(**role_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff4b7a8b154d7b17b02e654f50e0685349a73260ad69e50b3ac4fc5081723cc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument role_ref", value=role_ref, expected_type=type_hints["role_ref"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metadata": metadata,
            "role_ref": role_ref,
            "subject": subject,
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
    def metadata(self) -> "ClusterRoleBindingV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#metadata ClusterRoleBindingV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("ClusterRoleBindingV1Metadata", result)

    @builtins.property
    def role_ref(self) -> "ClusterRoleBindingV1RoleRef":
        '''role_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#role_ref ClusterRoleBindingV1#role_ref}
        '''
        result = self._values.get("role_ref")
        assert result is not None, "Required property 'role_ref' is missing"
        return typing.cast("ClusterRoleBindingV1RoleRef", result)

    @builtins.property
    def subject(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterRoleBindingV1Subject"]]:
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#subject ClusterRoleBindingV1#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterRoleBindingV1Subject"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#id ClusterRoleBindingV1#id}.

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
        return "ClusterRoleBindingV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class ClusterRoleBindingV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the clusterRoleBinding that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#annotations ClusterRoleBindingV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the clusterRoleBinding. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#labels ClusterRoleBindingV1#labels}
        :param name: Name of the clusterRoleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81858ec5435932a720396fe9b55e6d8485a671969d7073377c9e07f8f2f729f7)
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
        '''An unstructured key value map stored with the clusterRoleBinding that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#annotations ClusterRoleBindingV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the clusterRoleBinding.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#labels ClusterRoleBindingV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the clusterRoleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRoleBindingV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterRoleBindingV1MetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee095c3f5b0d09aa6ed81e6bfc61c7d0b1b48334a5c537f2a1dddfd4ad982c94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19ebb7ecfcf889658a431703f4ec4ef79ca636226684e09d9d9d8af21e7a1479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff7892aee866cb8b9807db178ac713922c74dfef512a0e9a629843b5140356a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa64a545b4fea925926265cbf32cc97c6765c38ab9668048a0bdeaa803d68110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterRoleBindingV1Metadata]:
        return typing.cast(typing.Optional[ClusterRoleBindingV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterRoleBindingV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6220670beb1991826d5cd958db1bc21451e62afa9f090c0e5f4797149054bc97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1RoleRef",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class ClusterRoleBindingV1RoleRef:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#api_group ClusterRoleBindingV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#kind ClusterRoleBindingV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2225e8afff9780d7a9a3ff537141a38d0a0d64fa49337550ad34345a22e5a4cd)
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
        '''The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#api_group ClusterRoleBindingV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#kind ClusterRoleBindingV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRoleBindingV1RoleRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterRoleBindingV1RoleRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1RoleRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70860071f02543daf7f3f705c497ba7229d4bb807f59b1f7e9a8e6ce9ceef7d0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1381b7f31f91067a03c9b9fc1f5cb7131f258475bc117c529a9dcbd5fa33a0b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba9a2740ba7bb808588193be8213451f772f6c1122baea0d3e99931b73a478f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b37480c43092252607fc2ec96f66b4dddab7fca06e253d28fbbe1d54c83b26a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterRoleBindingV1RoleRef]:
        return typing.cast(typing.Optional[ClusterRoleBindingV1RoleRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterRoleBindingV1RoleRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__803fe7659bd50c089c560672e11da7e614053ddeaa1a80489581545667f17c7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1Subject",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "api_group": "apiGroup",
        "namespace": "namespace",
    },
)
class ClusterRoleBindingV1Subject:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_group: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#kind ClusterRoleBindingV1#kind}
        :param name: The name of the resource to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        :param api_group: The API group of the subject resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#api_group ClusterRoleBindingV1#api_group}
        :param namespace: The Namespace of the subject resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#namespace ClusterRoleBindingV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44c7ee8752db0262deb79900c96ece4b72c8f60574867a78c09ed43e6b8e21a)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_group is not None:
            self._values["api_group"] = api_group
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#kind ClusterRoleBindingV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the resource to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#name ClusterRoleBindingV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_group(self) -> typing.Optional[builtins.str]:
        '''The API group of the subject resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#api_group ClusterRoleBindingV1#api_group}
        '''
        result = self._values.get("api_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The Namespace of the subject resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/cluster_role_binding_v1#namespace ClusterRoleBindingV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterRoleBindingV1Subject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterRoleBindingV1SubjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1SubjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9b3e02369cd79f98ea2fa55f3830b6accc8f77700bfb66fcfd0d1cceab47535)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterRoleBindingV1SubjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d192336ec22ace56dc8e31e7228953a87b34dd438b05563042a95a26f1efd7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterRoleBindingV1SubjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72b46a51be1c82cfdbe2f73ad0b9b45ae3f9ea8e64c326a52c93736413eaef07)
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
            type_hints = typing.get_type_hints(_typecheckingstub__014d70d334bae1a100d23b865af2e69e7c93c01f475454ce5468fd48d05d81df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20fe6ade9dd87061d4142d73d8f34c45f0c78d31ec96f2e353ea314d57803b15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterRoleBindingV1Subject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterRoleBindingV1Subject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterRoleBindingV1Subject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e683ca88e5cef204b56f357082c0cacf069b9095692fe6d8dba7d434539f6a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterRoleBindingV1SubjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.clusterRoleBindingV1.ClusterRoleBindingV1SubjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a53d82691b1d8f77993a85c76b6e4a6d8569996fc74dc293ef54d1fa483b758d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApiGroup")
    def reset_api_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiGroup", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2dbda95c1c3cfc3c408104f754803555514e8716b89a40776108a5402d01b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57e92d6b5857c65d13b794aea1afad3ac10053648c98bd45a39f2ec6fb5ee18c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ca3eb613f12d0091882026b942216c766344da102c4258f30ee3e239fa335b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28645f7ebec36880013251509e688253e77ce588d44bec6d43560ec615c540d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterRoleBindingV1Subject, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterRoleBindingV1Subject, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterRoleBindingV1Subject, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61f25b260e7a86ef8843ed076d26cdbfc8d9d6673b179c6d4bdc29a26ee3be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ClusterRoleBindingV1",
    "ClusterRoleBindingV1Config",
    "ClusterRoleBindingV1Metadata",
    "ClusterRoleBindingV1MetadataOutputReference",
    "ClusterRoleBindingV1RoleRef",
    "ClusterRoleBindingV1RoleRefOutputReference",
    "ClusterRoleBindingV1Subject",
    "ClusterRoleBindingV1SubjectList",
    "ClusterRoleBindingV1SubjectOutputReference",
]

publication.publish()

def _typecheckingstub__c0b3fa2e0a0edd410240c71f8ffa30653a94c0772445893d941584cf2a3b7a65(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metadata: typing.Union[ClusterRoleBindingV1Metadata, typing.Dict[builtins.str, typing.Any]],
    role_ref: typing.Union[ClusterRoleBindingV1RoleRef, typing.Dict[builtins.str, typing.Any]],
    subject: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterRoleBindingV1Subject, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__e22e05f6352b546d787e4c857fc6b89fb9433209263bc24b6673c26179bad5f5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterRoleBindingV1Subject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903dacfc7346b114d1e032d507d890c9ba7960d943a4d4e406fd8694026cda0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff4b7a8b154d7b17b02e654f50e0685349a73260ad69e50b3ac4fc5081723cc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metadata: typing.Union[ClusterRoleBindingV1Metadata, typing.Dict[builtins.str, typing.Any]],
    role_ref: typing.Union[ClusterRoleBindingV1RoleRef, typing.Dict[builtins.str, typing.Any]],
    subject: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterRoleBindingV1Subject, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81858ec5435932a720396fe9b55e6d8485a671969d7073377c9e07f8f2f729f7(
    *,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee095c3f5b0d09aa6ed81e6bfc61c7d0b1b48334a5c537f2a1dddfd4ad982c94(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ebb7ecfcf889658a431703f4ec4ef79ca636226684e09d9d9d8af21e7a1479(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff7892aee866cb8b9807db178ac713922c74dfef512a0e9a629843b5140356a1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa64a545b4fea925926265cbf32cc97c6765c38ab9668048a0bdeaa803d68110(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6220670beb1991826d5cd958db1bc21451e62afa9f090c0e5f4797149054bc97(
    value: typing.Optional[ClusterRoleBindingV1Metadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2225e8afff9780d7a9a3ff537141a38d0a0d64fa49337550ad34345a22e5a4cd(
    *,
    api_group: builtins.str,
    kind: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70860071f02543daf7f3f705c497ba7229d4bb807f59b1f7e9a8e6ce9ceef7d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1381b7f31f91067a03c9b9fc1f5cb7131f258475bc117c529a9dcbd5fa33a0b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba9a2740ba7bb808588193be8213451f772f6c1122baea0d3e99931b73a478f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b37480c43092252607fc2ec96f66b4dddab7fca06e253d28fbbe1d54c83b26a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803fe7659bd50c089c560672e11da7e614053ddeaa1a80489581545667f17c7d(
    value: typing.Optional[ClusterRoleBindingV1RoleRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44c7ee8752db0262deb79900c96ece4b72c8f60574867a78c09ed43e6b8e21a(
    *,
    kind: builtins.str,
    name: builtins.str,
    api_group: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9b3e02369cd79f98ea2fa55f3830b6accc8f77700bfb66fcfd0d1cceab47535(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d192336ec22ace56dc8e31e7228953a87b34dd438b05563042a95a26f1efd7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b46a51be1c82cfdbe2f73ad0b9b45ae3f9ea8e64c326a52c93736413eaef07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014d70d334bae1a100d23b865af2e69e7c93c01f475454ce5468fd48d05d81df(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fe6ade9dd87061d4142d73d8f34c45f0c78d31ec96f2e353ea314d57803b15(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e683ca88e5cef204b56f357082c0cacf069b9095692fe6d8dba7d434539f6a1f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterRoleBindingV1Subject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53d82691b1d8f77993a85c76b6e4a6d8569996fc74dc293ef54d1fa483b758d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2dbda95c1c3cfc3c408104f754803555514e8716b89a40776108a5402d01b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e92d6b5857c65d13b794aea1afad3ac10053648c98bd45a39f2ec6fb5ee18c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ca3eb613f12d0091882026b942216c766344da102c4258f30ee3e239fa335b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28645f7ebec36880013251509e688253e77ce588d44bec6d43560ec615c540d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61f25b260e7a86ef8843ed076d26cdbfc8d9d6673b179c6d4bdc29a26ee3be3(
    value: typing.Optional[typing.Union[ClusterRoleBindingV1Subject, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
