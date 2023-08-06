'''
# `azurestack_storage_account`

Refer to the Terraform Registory for docs: [`azurestack_storage_account`](https://www.terraform.io/docs/providers/azurestack/r/storage_account).
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


class StorageAccount(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account azurestack_storage_account}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_replication_type: builtins.str,
        account_tier: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        account_encryption_source: typing.Optional[builtins.str] = None,
        account_kind: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[typing.Union["StorageAccountCustomDomain", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_blob_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account azurestack_storage_account} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_replication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_replication_type StorageAccount#account_replication_type}.
        :param account_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_tier StorageAccount#account_tier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#location StorageAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#resource_group_name StorageAccount#resource_group_name}.
        :param account_encryption_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_encryption_source StorageAccount#account_encryption_source}.
        :param account_kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_kind StorageAccount#account_kind}.
        :param custom_domain: custom_domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#custom_domain StorageAccount#custom_domain}
        :param enable_blob_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_blob_encryption StorageAccount#enable_blob_encryption}.
        :param enable_https_traffic_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#id StorageAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#tags StorageAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#timeouts StorageAccount#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c5b973c1422d208ef8e122171ba9d021b53c233742f3be8e8370428d671d54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageAccountConfig(
            account_replication_type=account_replication_type,
            account_tier=account_tier,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            account_encryption_source=account_encryption_source,
            account_kind=account_kind,
            custom_domain=custom_domain,
            enable_blob_encryption=enable_blob_encryption,
            enable_https_traffic_only=enable_https_traffic_only,
            id=id,
            tags=tags,
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

    @jsii.member(jsii_name="putCustomDomain")
    def put_custom_domain(
        self,
        *,
        name: builtins.str,
        use_subdomain: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.
        :param use_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#use_subdomain StorageAccount#use_subdomain}.
        '''
        value = StorageAccountCustomDomain(name=name, use_subdomain=use_subdomain)

        return typing.cast(None, jsii.invoke(self, "putCustomDomain", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#create StorageAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#read StorageAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#update StorageAccount#update}.
        '''
        value = StorageAccountTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccountEncryptionSource")
    def reset_account_encryption_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountEncryptionSource", []))

    @jsii.member(jsii_name="resetAccountKind")
    def reset_account_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountKind", []))

    @jsii.member(jsii_name="resetCustomDomain")
    def reset_custom_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDomain", []))

    @jsii.member(jsii_name="resetEnableBlobEncryption")
    def reset_enable_blob_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBlobEncryption", []))

    @jsii.member(jsii_name="resetEnableHttpsTrafficOnly")
    def reset_enable_https_traffic_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttpsTrafficOnly", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="customDomain")
    def custom_domain(self) -> "StorageAccountCustomDomainOutputReference":
        return typing.cast("StorageAccountCustomDomainOutputReference", jsii.get(self, "customDomain"))

    @builtins.property
    @jsii.member(jsii_name="primaryAccessKey")
    def primary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="primaryBlobConnectionString")
    def primary_blob_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryBlobConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="primaryBlobEndpoint")
    def primary_blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryBlobEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryConnectionString")
    def primary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="primaryFileEndpoint")
    def primary_file_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryFileEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryLocation")
    def primary_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLocation"))

    @builtins.property
    @jsii.member(jsii_name="primaryQueueEndpoint")
    def primary_queue_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="primaryTableEndpoint")
    def primary_table_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryTableEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryAccessKey")
    def secondary_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryAccessKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryBlobConnectionString")
    def secondary_blob_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryBlobConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="secondaryBlobEndpoint")
    def secondary_blob_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryBlobEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryConnectionString")
    def secondary_connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="secondaryLocation")
    def secondary_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryLocation"))

    @builtins.property
    @jsii.member(jsii_name="secondaryQueueEndpoint")
    def secondary_queue_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryQueueEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="secondaryTableEndpoint")
    def secondary_table_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryTableEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "StorageAccountTimeoutsOutputReference":
        return typing.cast("StorageAccountTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accountEncryptionSourceInput")
    def account_encryption_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountEncryptionSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="accountKindInput")
    def account_kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountKindInput"))

    @builtins.property
    @jsii.member(jsii_name="accountReplicationTypeInput")
    def account_replication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountReplicationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountTierInput")
    def account_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountTierInput"))

    @builtins.property
    @jsii.member(jsii_name="customDomainInput")
    def custom_domain_input(self) -> typing.Optional["StorageAccountCustomDomain"]:
        return typing.cast(typing.Optional["StorageAccountCustomDomain"], jsii.get(self, "customDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBlobEncryptionInput")
    def enable_blob_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBlobEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpsTrafficOnlyInput")
    def enable_https_traffic_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableHttpsTrafficOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["StorageAccountTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["StorageAccountTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountEncryptionSource")
    def account_encryption_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountEncryptionSource"))

    @account_encryption_source.setter
    def account_encryption_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8d51cd87c71a43fcb348bc9aa790681c56722b798bd494146ff238eafd070a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountEncryptionSource", value)

    @builtins.property
    @jsii.member(jsii_name="accountKind")
    def account_kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountKind"))

    @account_kind.setter
    def account_kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f4991e1ee0666dfc411c1316fb996301dc46f1473862dc0746c59da8cccbe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountKind", value)

    @builtins.property
    @jsii.member(jsii_name="accountReplicationType")
    def account_replication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountReplicationType"))

    @account_replication_type.setter
    def account_replication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__606c4adb7dd8d6e19de87f1a21ad0d4678c70077d26f17d8fe1defe9fe6ff272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountReplicationType", value)

    @builtins.property
    @jsii.member(jsii_name="accountTier")
    def account_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountTier"))

    @account_tier.setter
    def account_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca4ab1e47082537ec6a3c12389cf99c8c267e92287b6674478255cf6ea3b19d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountTier", value)

    @builtins.property
    @jsii.member(jsii_name="enableBlobEncryption")
    def enable_blob_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBlobEncryption"))

    @enable_blob_encryption.setter
    def enable_blob_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8945190854deb389ed0f0909356e18bb92a410f6176c1da77f7626ce7c1d65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBlobEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableHttpsTrafficOnly"))

    @enable_https_traffic_only.setter
    def enable_https_traffic_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2373c6ecaa3ad3695136bf52c3a8ea1d2b7b5c17727464c0436865d7aa54c8c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpsTrafficOnly", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217d01e344b3fca59e0fcda3780aba0d96893bd71af8da89818866b171151c1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65618c53a54dcf8c24dacdabfd4de6c448a08bae3a7ffaa6685e68ff8e57b150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a2e22fee7d67aa5a4a896129dcf62ff8a63451040f6b7062dc42e4af6625c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327f7f3ac996c519327c7d5a5deabb2067c7144e8c244804599e3ca4696f65ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c638d3be4f5c8b584a6132e3381ce170b62ac2bbb65749fbda15272b311df932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccountConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_replication_type": "accountReplicationType",
        "account_tier": "accountTier",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "account_encryption_source": "accountEncryptionSource",
        "account_kind": "accountKind",
        "custom_domain": "customDomain",
        "enable_blob_encryption": "enableBlobEncryption",
        "enable_https_traffic_only": "enableHttpsTrafficOnly",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class StorageAccountConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_replication_type: builtins.str,
        account_tier: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        account_encryption_source: typing.Optional[builtins.str] = None,
        account_kind: typing.Optional[builtins.str] = None,
        custom_domain: typing.Optional[typing.Union["StorageAccountCustomDomain", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_blob_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["StorageAccountTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_replication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_replication_type StorageAccount#account_replication_type}.
        :param account_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_tier StorageAccount#account_tier}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#location StorageAccount#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#resource_group_name StorageAccount#resource_group_name}.
        :param account_encryption_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_encryption_source StorageAccount#account_encryption_source}.
        :param account_kind: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_kind StorageAccount#account_kind}.
        :param custom_domain: custom_domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#custom_domain StorageAccount#custom_domain}
        :param enable_blob_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_blob_encryption StorageAccount#enable_blob_encryption}.
        :param enable_https_traffic_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#id StorageAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#tags StorageAccount#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#timeouts StorageAccount#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_domain, dict):
            custom_domain = StorageAccountCustomDomain(**custom_domain)
        if isinstance(timeouts, dict):
            timeouts = StorageAccountTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb1dbf4cfaca7fe0791a927a6f4ce6391dc60ca3345ceb60ec7e717b15223f2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_replication_type", value=account_replication_type, expected_type=type_hints["account_replication_type"])
            check_type(argname="argument account_tier", value=account_tier, expected_type=type_hints["account_tier"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument account_encryption_source", value=account_encryption_source, expected_type=type_hints["account_encryption_source"])
            check_type(argname="argument account_kind", value=account_kind, expected_type=type_hints["account_kind"])
            check_type(argname="argument custom_domain", value=custom_domain, expected_type=type_hints["custom_domain"])
            check_type(argname="argument enable_blob_encryption", value=enable_blob_encryption, expected_type=type_hints["enable_blob_encryption"])
            check_type(argname="argument enable_https_traffic_only", value=enable_https_traffic_only, expected_type=type_hints["enable_https_traffic_only"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_replication_type": account_replication_type,
            "account_tier": account_tier,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if account_encryption_source is not None:
            self._values["account_encryption_source"] = account_encryption_source
        if account_kind is not None:
            self._values["account_kind"] = account_kind
        if custom_domain is not None:
            self._values["custom_domain"] = custom_domain
        if enable_blob_encryption is not None:
            self._values["enable_blob_encryption"] = enable_blob_encryption
        if enable_https_traffic_only is not None:
            self._values["enable_https_traffic_only"] = enable_https_traffic_only
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
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
    def account_replication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_replication_type StorageAccount#account_replication_type}.'''
        result = self._values.get("account_replication_type")
        assert result is not None, "Required property 'account_replication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_tier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_tier StorageAccount#account_tier}.'''
        result = self._values.get("account_tier")
        assert result is not None, "Required property 'account_tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#location StorageAccount#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#resource_group_name StorageAccount#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_encryption_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_encryption_source StorageAccount#account_encryption_source}.'''
        result = self._values.get("account_encryption_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_kind(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#account_kind StorageAccount#account_kind}.'''
        result = self._values.get("account_kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_domain(self) -> typing.Optional["StorageAccountCustomDomain"]:
        '''custom_domain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#custom_domain StorageAccount#custom_domain}
        '''
        result = self._values.get("custom_domain")
        return typing.cast(typing.Optional["StorageAccountCustomDomain"], result)

    @builtins.property
    def enable_blob_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_blob_encryption StorageAccount#enable_blob_encryption}.'''
        result = self._values.get("enable_blob_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_https_traffic_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#enable_https_traffic_only StorageAccount#enable_https_traffic_only}.'''
        result = self._values.get("enable_https_traffic_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#id StorageAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#tags StorageAccount#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["StorageAccountTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#timeouts StorageAccount#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["StorageAccountTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccountCustomDomain",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "use_subdomain": "useSubdomain"},
)
class StorageAccountCustomDomain:
    def __init__(
        self,
        *,
        name: builtins.str,
        use_subdomain: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.
        :param use_subdomain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#use_subdomain StorageAccount#use_subdomain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7ee540fb320e91e6a39844aea511c470b020a55d22623a6c282b86799d9675)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument use_subdomain", value=use_subdomain, expected_type=type_hints["use_subdomain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if use_subdomain is not None:
            self._values["use_subdomain"] = use_subdomain

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#name StorageAccount#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_subdomain(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#use_subdomain StorageAccount#use_subdomain}.'''
        result = self._values.get("use_subdomain")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountCustomDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountCustomDomainOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccountCustomDomainOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ce4f08ba1daf858a3e26daa6dd79c352565ad6ed995815791da34fea6074af8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseSubdomain")
    def reset_use_subdomain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseSubdomain", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="useSubdomainInput")
    def use_subdomain_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useSubdomainInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e237682833422b3bcc568bf3cfe4172cf12e623b13974009be1ada1ac8fbe25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="useSubdomain")
    def use_subdomain(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useSubdomain"))

    @use_subdomain.setter
    def use_subdomain(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fffcde117f53d7d517d455a56145c91ad1a9fa9954a3be339f4ec38eee8346f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useSubdomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageAccountCustomDomain]:
        return typing.cast(typing.Optional[StorageAccountCustomDomain], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageAccountCustomDomain],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd51603db9420280abb8d9daecbc38c52608d914aa01af6f389e023889e8303)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccountTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class StorageAccountTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#create StorageAccount#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#delete StorageAccount#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#read StorageAccount#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#update StorageAccount#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9401b0d08360a7e3b288c6fc0d571865679ec3a6b21c80580a096f188dfbb102)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#create StorageAccount#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#delete StorageAccount#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#read StorageAccount#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/storage_account#update StorageAccount#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageAccountTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageAccountTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.storageAccount.StorageAccountTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae64f267025ebdb82b40bdc476ec675b863a31d70702c430c379140d28ebbe0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d938b473616c4cef6f7f13e99924d11fb9a981c42723915aa53721a66e41480b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c54aec887ef5f2395015dbb1a064dd14989bb76a73621aed575cb3ae7831578b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5311e35f35e6e77eae42ee611627e55eabc46af0e80fa988b9f72e07cdbcc8f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8a953dc6d4a2b22757e2e48a8eb3a51a39cca9709ff7d79bb32e4ff19684097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[StorageAccountTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[StorageAccountTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[StorageAccountTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a76b0f434b89680994007ff72652dd2bb7596b72cdc1766c197da6fddad1908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageAccount",
    "StorageAccountConfig",
    "StorageAccountCustomDomain",
    "StorageAccountCustomDomainOutputReference",
    "StorageAccountTimeouts",
    "StorageAccountTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__70c5b973c1422d208ef8e122171ba9d021b53c233742f3be8e8370428d671d54(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_replication_type: builtins.str,
    account_tier: builtins.str,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    account_encryption_source: typing.Optional[builtins.str] = None,
    account_kind: typing.Optional[builtins.str] = None,
    custom_domain: typing.Optional[typing.Union[StorageAccountCustomDomain, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_blob_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StorageAccountTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a8d51cd87c71a43fcb348bc9aa790681c56722b798bd494146ff238eafd070a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f4991e1ee0666dfc411c1316fb996301dc46f1473862dc0746c59da8cccbe6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606c4adb7dd8d6e19de87f1a21ad0d4678c70077d26f17d8fe1defe9fe6ff272(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca4ab1e47082537ec6a3c12389cf99c8c267e92287b6674478255cf6ea3b19d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8945190854deb389ed0f0909356e18bb92a410f6176c1da77f7626ce7c1d65(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2373c6ecaa3ad3695136bf52c3a8ea1d2b7b5c17727464c0436865d7aa54c8c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217d01e344b3fca59e0fcda3780aba0d96893bd71af8da89818866b171151c1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65618c53a54dcf8c24dacdabfd4de6c448a08bae3a7ffaa6685e68ff8e57b150(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a2e22fee7d67aa5a4a896129dcf62ff8a63451040f6b7062dc42e4af6625c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327f7f3ac996c519327c7d5a5deabb2067c7144e8c244804599e3ca4696f65ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c638d3be4f5c8b584a6132e3381ce170b62ac2bbb65749fbda15272b311df932(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb1dbf4cfaca7fe0791a927a6f4ce6391dc60ca3345ceb60ec7e717b15223f2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_replication_type: builtins.str,
    account_tier: builtins.str,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    account_encryption_source: typing.Optional[builtins.str] = None,
    account_kind: typing.Optional[builtins.str] = None,
    custom_domain: typing.Optional[typing.Union[StorageAccountCustomDomain, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_blob_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_https_traffic_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[StorageAccountTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7ee540fb320e91e6a39844aea511c470b020a55d22623a6c282b86799d9675(
    *,
    name: builtins.str,
    use_subdomain: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce4f08ba1daf858a3e26daa6dd79c352565ad6ed995815791da34fea6074af8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e237682833422b3bcc568bf3cfe4172cf12e623b13974009be1ada1ac8fbe25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fffcde117f53d7d517d455a56145c91ad1a9fa9954a3be339f4ec38eee8346f2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd51603db9420280abb8d9daecbc38c52608d914aa01af6f389e023889e8303(
    value: typing.Optional[StorageAccountCustomDomain],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9401b0d08360a7e3b288c6fc0d571865679ec3a6b21c80580a096f188dfbb102(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae64f267025ebdb82b40bdc476ec675b863a31d70702c430c379140d28ebbe0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d938b473616c4cef6f7f13e99924d11fb9a981c42723915aa53721a66e41480b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54aec887ef5f2395015dbb1a064dd14989bb76a73621aed575cb3ae7831578b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5311e35f35e6e77eae42ee611627e55eabc46af0e80fa988b9f72e07cdbcc8f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a953dc6d4a2b22757e2e48a8eb3a51a39cca9709ff7d79bb32e4ff19684097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a76b0f434b89680994007ff72652dd2bb7596b72cdc1766c197da6fddad1908(
    value: typing.Optional[typing.Union[StorageAccountTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
