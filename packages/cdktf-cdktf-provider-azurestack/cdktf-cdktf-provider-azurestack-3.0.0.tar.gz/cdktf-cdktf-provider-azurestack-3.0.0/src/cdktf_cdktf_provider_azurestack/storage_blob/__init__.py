'''
# `azurestack_storage_blob`

Refer to the Terraform Registory for docs: [`azurestack_storage_blob`](https://www.terraform.io/docs/providers/azurestack/r/storage_blob).
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


class StorageBlob(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.storageBlob.StorageBlob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob azurestack_storage_blob}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        storage_account_name: builtins.str,
        storage_container_name: builtins.str,
        type: builtins.str,
        cache_control: typing.Optional[builtins.str] = None,
        content_md5: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        parallelism: typing.Optional[jsii.Number] = None,
        size: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        source_content: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StorageBlobTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob azurestack_storage_blob} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#name StorageBlob#name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_account_name StorageBlob#storage_account_name}.
        :param storage_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_container_name StorageBlob#storage_container_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#type StorageBlob#type}.
        :param cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#cache_control StorageBlob#cache_control}.
        :param content_md5: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_md5 StorageBlob#content_md5}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_type StorageBlob#content_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#id StorageBlob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#metadata StorageBlob#metadata}.
        :param parallelism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#parallelism StorageBlob#parallelism}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#size StorageBlob#size}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source StorageBlob#source}.
        :param source_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_content StorageBlob#source_content}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_uri StorageBlob#source_uri}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#timeouts StorageBlob#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e7fb6b44d52687a5dd070e6d7dd8cfe35447252bcf092f6496dba1d90326b35)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageBlobConfig(
            name=name,
            storage_account_name=storage_account_name,
            storage_container_name=storage_container_name,
            type=type,
            cache_control=cache_control,
            content_md5=content_md5,
            content_type=content_type,
            id=id,
            metadata=metadata,
            parallelism=parallelism,
            size=size,
            source=source,
            source_content=source_content,
            source_uri=source_uri,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#create StorageBlob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#delete StorageBlob#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#read StorageBlob#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#update StorageBlob#update}.
        '''
        value = StorageBlobTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCacheControl")
    def reset_cache_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheControl", []))

    @jsii.member(jsii_name="resetContentMd5")
    def reset_content_md5(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentMd5", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourceContent")
    def reset_source_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceContent", []))

    @jsii.member(jsii_name="resetSourceUri")
    def reset_source_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceUri", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageBlobTimeoutsOutputReference":
        return typing.cast("StorageBlobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="cacheControlInput")
    def cache_control_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheControlInput"))

    @builtins.property
    @jsii.member(jsii_name="contentMd5Input")
    def content_md5_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentMd5Input"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceContentInput")
    def source_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceContentInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUriInput")
    def source_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageContainerNameInput")
    def storage_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageBlobTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageBlobTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheControl")
    def cache_control(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheControl"))

    @cache_control.setter
    def cache_control(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c096dd9a74465c83feb35f6c93aff7a0d12752cfc29515ebb4eb401244c1db92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheControl", value)

    @builtins.property
    @jsii.member(jsii_name="contentMd5")
    def content_md5(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentMd5"))

    @content_md5.setter
    def content_md5(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f652d3934f1661f5e9b89fbccc2f1fdcdadaa36abe21096623cb3049596fb7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentMd5", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd32ca2259faec4ceeb5d8e81a565b4d230fede627240a55f1ceab7a33691f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc67a8316954db186649e28851dc64fdb80afb500a5402fc2c9c54fd8c7bdee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51d9182b649195b73f391fb35474643d170ac584cf6aed3b397a640bab1d40d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64cf7430563914c2ba1e09468f1b977ee1bcf5c2406d470148bd6105051eb034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelism"))

    @parallelism.setter
    def parallelism(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d8bf59fa65dc634f40b8cb1f3778bed7c44137d62fa6fa4cd16f4c5e145a3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelism", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738a143e75ecca285043f0c14c388197f8c7304f9ef6f3e6e93a6874a88fa2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10842ce66c5352ee46a41cbeda68371c250b8c5f868d7b18737153bb35f37ceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="sourceContent")
    def source_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceContent"))

    @source_content.setter
    def source_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9865e0f65986058f0f0aa51df009a39e6ebfce05d2ed4dfd06286dcd647a17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceContent", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUri")
    def source_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUri"))

    @source_uri.setter
    def source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb562e8680270cb3a5d16e04557378f084c90954acb47be4f9be989e2932228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUri", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ffcdde8e2fde8b1407bbcfca0fe224ae718df05c4291213a884c499a1eb0ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="storageContainerName")
    def storage_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageContainerName"))

    @storage_container_name.setter
    def storage_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d672f6ad44471c3b612139d0f2e3e1ee0125c4de7a3fd3e710040d0e01469df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__474762cb96d7652288586aabbd4afc38133e1a18f209f3ceed0db67d606f1535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.storageBlob.StorageBlobConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "storage_account_name": "storageAccountName",
        "storage_container_name": "storageContainerName",
        "type": "type",
        "cache_control": "cacheControl",
        "content_md5": "contentMd5",
        "content_type": "contentType",
        "id": "id",
        "metadata": "metadata",
        "parallelism": "parallelism",
        "size": "size",
        "source": "source",
        "source_content": "sourceContent",
        "source_uri": "sourceUri",
        "timeouts": "timeouts",
    },
)
class StorageBlobConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        storage_account_name: builtins.str,
        storage_container_name: builtins.str,
        type: builtins.str,
        cache_control: typing.Optional[builtins.str] = None,
        content_md5: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        parallelism: typing.Optional[jsii.Number] = None,
        size: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        source_content: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["StorageBlobTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#name StorageBlob#name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_account_name StorageBlob#storage_account_name}.
        :param storage_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_container_name StorageBlob#storage_container_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#type StorageBlob#type}.
        :param cache_control: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#cache_control StorageBlob#cache_control}.
        :param content_md5: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_md5 StorageBlob#content_md5}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_type StorageBlob#content_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#id StorageBlob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#metadata StorageBlob#metadata}.
        :param parallelism: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#parallelism StorageBlob#parallelism}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#size StorageBlob#size}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source StorageBlob#source}.
        :param source_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_content StorageBlob#source_content}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_uri StorageBlob#source_uri}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#timeouts StorageBlob#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = StorageBlobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6160d551b8f10f53010c5ab811a5facf619284dbd984cb716d07aeb68dafb5f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument storage_container_name", value=storage_container_name, expected_type=type_hints["storage_container_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument cache_control", value=cache_control, expected_type=type_hints["cache_control"])
            check_type(argname="argument content_md5", value=content_md5, expected_type=type_hints["content_md5"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_content", value=source_content, expected_type=type_hints["source_content"])
            check_type(argname="argument source_uri", value=source_uri, expected_type=type_hints["source_uri"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "storage_account_name": storage_account_name,
            "storage_container_name": storage_container_name,
            "type": type,
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
        if cache_control is not None:
            self._values["cache_control"] = cache_control
        if content_md5 is not None:
            self._values["content_md5"] = content_md5
        if content_type is not None:
            self._values["content_type"] = content_type
        if id is not None:
            self._values["id"] = id
        if metadata is not None:
            self._values["metadata"] = metadata
        if parallelism is not None:
            self._values["parallelism"] = parallelism
        if size is not None:
            self._values["size"] = size
        if source is not None:
            self._values["source"] = source
        if source_content is not None:
            self._values["source_content"] = source_content
        if source_uri is not None:
            self._values["source_uri"] = source_uri
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#name StorageBlob#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_account_name StorageBlob#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#storage_container_name StorageBlob#storage_container_name}.'''
        result = self._values.get("storage_container_name")
        assert result is not None, "Required property 'storage_container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#type StorageBlob#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_control(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#cache_control StorageBlob#cache_control}.'''
        result = self._values.get("cache_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_md5(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_md5 StorageBlob#content_md5}.'''
        result = self._values.get("content_md5")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#content_type StorageBlob#content_type}.'''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#id StorageBlob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#metadata StorageBlob#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def parallelism(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#parallelism StorageBlob#parallelism}.'''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#size StorageBlob#size}.'''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source StorageBlob#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_content StorageBlob#source_content}.'''
        result = self._values.get("source_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#source_uri StorageBlob#source_uri}.'''
        result = self._values.get("source_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageBlobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#timeouts StorageBlob#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageBlobTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.storageBlob.StorageBlobTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageBlobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#create StorageBlob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#delete StorageBlob#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#read StorageBlob#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#update StorageBlob#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c53df9a3a36ecc60892e8c86a0e2d11fc407d8763baa2a556767b2d83188fd)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#create StorageBlob#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#delete StorageBlob#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#read StorageBlob#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_blob#update StorageBlob#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBlobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBlobTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.storageBlob.StorageBlobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c3b711362f894e6cba2cfc05c0c8f0d7f0e46313839a619b7391392de53014a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0879cd507fd3c7ec7efcc3f3d7b570a7eb6810b8ced6f6619759500623b18e24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb435f8aad56f2ecf53b037e105f4c70bc52524ffd780408d35d60f8178cf58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f892fadcd06220d9bfd61c79dd4b17094a66da0748af7f02f8190ad51465428a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d666d85133ec72af5fdc63e01d5bc6d0bd56a74c054a211414f3615ffb3624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageBlobTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageBlobTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageBlobTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282ca78f811d486eb7c3975eeab6abba83d5fd320c43835a23ebd38ff3bdee95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageBlob",
    "StorageBlobConfig",
    "StorageBlobTimeouts",
    "StorageBlobTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6e7fb6b44d52687a5dd070e6d7dd8cfe35447252bcf092f6496dba1d90326b35(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    storage_account_name: builtins.str,
    storage_container_name: builtins.str,
    type: builtins.str,
    cache_control: typing.Optional[builtins.str] = None,
    content_md5: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    parallelism: typing.Optional[jsii.Number] = None,
    size: typing.Optional[jsii.Number] = None,
    source: typing.Optional[builtins.str] = None,
    source_content: typing.Optional[builtins.str] = None,
    source_uri: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[StorageBlobTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__c096dd9a74465c83feb35f6c93aff7a0d12752cfc29515ebb4eb401244c1db92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f652d3934f1661f5e9b89fbccc2f1fdcdadaa36abe21096623cb3049596fb7ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd32ca2259faec4ceeb5d8e81a565b4d230fede627240a55f1ceab7a33691f58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc67a8316954db186649e28851dc64fdb80afb500a5402fc2c9c54fd8c7bdee7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51d9182b649195b73f391fb35474643d170ac584cf6aed3b397a640bab1d40d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64cf7430563914c2ba1e09468f1b977ee1bcf5c2406d470148bd6105051eb034(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d8bf59fa65dc634f40b8cb1f3778bed7c44137d62fa6fa4cd16f4c5e145a3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738a143e75ecca285043f0c14c388197f8c7304f9ef6f3e6e93a6874a88fa2f1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10842ce66c5352ee46a41cbeda68371c250b8c5f868d7b18737153bb35f37ceb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9865e0f65986058f0f0aa51df009a39e6ebfce05d2ed4dfd06286dcd647a17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb562e8680270cb3a5d16e04557378f084c90954acb47be4f9be989e2932228(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ffcdde8e2fde8b1407bbcfca0fe224ae718df05c4291213a884c499a1eb0ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d672f6ad44471c3b612139d0f2e3e1ee0125c4de7a3fd3e710040d0e01469df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__474762cb96d7652288586aabbd4afc38133e1a18f209f3ceed0db67d606f1535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6160d551b8f10f53010c5ab811a5facf619284dbd984cb716d07aeb68dafb5f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    storage_account_name: builtins.str,
    storage_container_name: builtins.str,
    type: builtins.str,
    cache_control: typing.Optional[builtins.str] = None,
    content_md5: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    parallelism: typing.Optional[jsii.Number] = None,
    size: typing.Optional[jsii.Number] = None,
    source: typing.Optional[builtins.str] = None,
    source_content: typing.Optional[builtins.str] = None,
    source_uri: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[StorageBlobTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c53df9a3a36ecc60892e8c86a0e2d11fc407d8763baa2a556767b2d83188fd(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3b711362f894e6cba2cfc05c0c8f0d7f0e46313839a619b7391392de53014a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0879cd507fd3c7ec7efcc3f3d7b570a7eb6810b8ced6f6619759500623b18e24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb435f8aad56f2ecf53b037e105f4c70bc52524ffd780408d35d60f8178cf58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f892fadcd06220d9bfd61c79dd4b17094a66da0748af7f02f8190ad51465428a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d666d85133ec72af5fdc63e01d5bc6d0bd56a74c054a211414f3615ffb3624(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282ca78f811d486eb7c3975eeab6abba83d5fd320c43835a23ebd38ff3bdee95(
    value: typing.Optional[typing.Union[StorageBlobTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
