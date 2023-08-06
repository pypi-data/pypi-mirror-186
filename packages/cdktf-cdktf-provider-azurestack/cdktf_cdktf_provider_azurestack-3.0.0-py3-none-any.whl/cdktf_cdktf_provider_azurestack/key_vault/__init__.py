'''
# `azurestack_key_vault`

Refer to the Terraform Registory for docs: [`azurestack_key_vault`](https://www.terraform.io/docs/providers/azurestack/r/key_vault).
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


class KeyVault(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVault",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault azurestack_key_vault}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        tenant_id: builtins.str,
        access_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyVaultAccessPolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        network_acls: typing.Optional[typing.Union["KeyVaultNetworkAcls", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault azurestack_key_vault} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#location KeyVault#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#name KeyVault#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#resource_group_name KeyVault#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#sku_name KeyVault#sku_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tenant_id KeyVault#tenant_id}.
        :param access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#access_policy KeyVault#access_policy}.
        :param enabled_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.
        :param enabled_for_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.
        :param enabled_for_template_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.
        :param enable_rbac_authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#id KeyVault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_acls: network_acls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#network_acls KeyVault#network_acls}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tags KeyVault#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#timeouts KeyVault#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d000889d0c678b0decd84240145a24b38de67132eca6182aad62a08cf6744620)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KeyVaultConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            tenant_id=tenant_id,
            access_policy=access_policy,
            enabled_for_deployment=enabled_for_deployment,
            enabled_for_disk_encryption=enabled_for_disk_encryption,
            enabled_for_template_deployment=enabled_for_template_deployment,
            enable_rbac_authorization=enable_rbac_authorization,
            id=id,
            network_acls=network_acls,
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

    @jsii.member(jsii_name="putAccessPolicy")
    def put_access_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KeyVaultAccessPolicy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e472a73e8ff2c0efb6a8a1c5b9310643dcaefdc0de16fdc1b0ba9c9a8dc7625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessPolicy", [value]))

    @jsii.member(jsii_name="putNetworkAcls")
    def put_network_acls(
        self,
        *,
        bypass: builtins.str,
        default_action: builtins.str,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#bypass KeyVault#bypass}.
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#default_action KeyVault#default_action}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#ip_rules KeyVault#ip_rules}.
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.
        '''
        value = KeyVaultNetworkAcls(
            bypass=bypass,
            default_action=default_action,
            ip_rules=ip_rules,
            virtual_network_subnet_ids=virtual_network_subnet_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkAcls", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#create KeyVault#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#delete KeyVault#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#read KeyVault#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#update KeyVault#update}.
        '''
        value = KeyVaultTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessPolicy")
    def reset_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPolicy", []))

    @jsii.member(jsii_name="resetEnabledForDeployment")
    def reset_enabled_for_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForDeployment", []))

    @jsii.member(jsii_name="resetEnabledForDiskEncryption")
    def reset_enabled_for_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForDiskEncryption", []))

    @jsii.member(jsii_name="resetEnabledForTemplateDeployment")
    def reset_enabled_for_template_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledForTemplateDeployment", []))

    @jsii.member(jsii_name="resetEnableRbacAuthorization")
    def reset_enable_rbac_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRbacAuthorization", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetworkAcls")
    def reset_network_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAcls", []))

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
    @jsii.member(jsii_name="accessPolicy")
    def access_policy(self) -> "KeyVaultAccessPolicyList":
        return typing.cast("KeyVaultAccessPolicyList", jsii.get(self, "accessPolicy"))

    @builtins.property
    @jsii.member(jsii_name="networkAcls")
    def network_acls(self) -> "KeyVaultNetworkAclsOutputReference":
        return typing.cast("KeyVaultNetworkAclsOutputReference", jsii.get(self, "networkAcls"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "KeyVaultTimeoutsOutputReference":
        return typing.cast("KeyVaultTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vaultUri")
    def vault_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultUri"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicyInput")
    def access_policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyVaultAccessPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KeyVaultAccessPolicy"]]], jsii.get(self, "accessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDeploymentInput")
    def enabled_for_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledForDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDiskEncryptionInput")
    def enabled_for_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledForDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForTemplateDeploymentInput")
    def enabled_for_template_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledForTemplateDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRbacAuthorizationInput")
    def enable_rbac_authorization_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableRbacAuthorizationInput"))

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
    @jsii.member(jsii_name="networkAclsInput")
    def network_acls_input(self) -> typing.Optional["KeyVaultNetworkAcls"]:
        return typing.cast(typing.Optional["KeyVaultNetworkAcls"], jsii.get(self, "networkAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["KeyVaultTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["KeyVaultTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledForDeployment")
    def enabled_for_deployment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabledForDeployment"))

    @enabled_for_deployment.setter
    def enabled_for_deployment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9912e78a3c129aae299581ebd372ecee1f3242629f1d0a74fefb90093e632d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabledForDiskEncryption"))

    @enabled_for_disk_encryption.setter
    def enabled_for_disk_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18e115ac7388250e02bcfc2d38a9e264f06d4fe8ce0e28c9474e21fbaca4e364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabledForTemplateDeployment"))

    @enabled_for_template_deployment.setter
    def enabled_for_template_deployment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e492dfb4162cffbe4328d4506d2e9163b066fdf73738269dc2b7a82d4b502476)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledForTemplateDeployment", value)

    @builtins.property
    @jsii.member(jsii_name="enableRbacAuthorization")
    def enable_rbac_authorization(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableRbacAuthorization"))

    @enable_rbac_authorization.setter
    def enable_rbac_authorization(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a1bd0913b7fdaa41f41f7ae9bd3932316092ba58de4d10afa73f29465674bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRbacAuthorization", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cba2ed1baab031e9d8898e56dbd0d812129daaffea0ea10db1af9c740924077f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8904eee7ea98a415d085786a630cbbcf590f38349067bda3651628b0b5bdd9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7032953f9743f085cb102be20570f2487adbab80e1dd35552e633587b817471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a1b9e2c4d180ba43f491be1691c4b474c9e5743356b50cf79b3aba811ea4bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd6473ce4e5bc7e795b87a66a63b7d04e10b5854311cb6ed048ac82fadf35de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c25d2bb2aa73b4afb3fb950577180201b3ef7528e7591c91496b6fb5d4a5f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6aa2676cf64c9816a938d7b823af12f6cccda7d80290c14686a53c92528c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultAccessPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "certificate_permissions": "certificatePermissions",
        "key_permissions": "keyPermissions",
        "object_id": "objectId",
        "secret_permissions": "secretPermissions",
        "storage_permissions": "storagePermissions",
        "tenant_id": "tenantId",
    },
)
class KeyVaultAccessPolicy:
    def __init__(
        self,
        *,
        application_id: typing.Optional[builtins.str] = None,
        certificate_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        object_id: typing.Optional[builtins.str] = None,
        secret_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#application_id KeyVault#application_id}.
        :param certificate_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#certificate_permissions KeyVault#certificate_permissions}.
        :param key_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#key_permissions KeyVault#key_permissions}.
        :param object_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#object_id KeyVault#object_id}.
        :param secret_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#secret_permissions KeyVault#secret_permissions}.
        :param storage_permissions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#storage_permissions KeyVault#storage_permissions}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tenant_id KeyVault#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ffa214ed4eb30bd5fb7f43b242d4f7e3a1c532bd761b3c2e390ffc31d43a0b)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument certificate_permissions", value=certificate_permissions, expected_type=type_hints["certificate_permissions"])
            check_type(argname="argument key_permissions", value=key_permissions, expected_type=type_hints["key_permissions"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument secret_permissions", value=secret_permissions, expected_type=type_hints["secret_permissions"])
            check_type(argname="argument storage_permissions", value=storage_permissions, expected_type=type_hints["storage_permissions"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_id is not None:
            self._values["application_id"] = application_id
        if certificate_permissions is not None:
            self._values["certificate_permissions"] = certificate_permissions
        if key_permissions is not None:
            self._values["key_permissions"] = key_permissions
        if object_id is not None:
            self._values["object_id"] = object_id
        if secret_permissions is not None:
            self._values["secret_permissions"] = secret_permissions
        if storage_permissions is not None:
            self._values["storage_permissions"] = storage_permissions
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#application_id KeyVault#application_id}.'''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#certificate_permissions KeyVault#certificate_permissions}.'''
        result = self._values.get("certificate_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#key_permissions KeyVault#key_permissions}.'''
        result = self._values.get("key_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def object_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#object_id KeyVault#object_id}.'''
        result = self._values.get("object_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#secret_permissions KeyVault#secret_permissions}.'''
        result = self._values.get("secret_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#storage_permissions KeyVault#storage_permissions}.'''
        result = self._values.get("storage_permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tenant_id KeyVault#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultAccessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultAccessPolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultAccessPolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7985ada42aeec13ab5f464ab5a6b11249a811d739480817c382e1c0b58985d11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KeyVaultAccessPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be3b3ac7f92b3ac4bae47d7fb4db3d8262b8d858d24d7e9c4b484907b19433a8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KeyVaultAccessPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aefb0d2a96ab7578b26884cd89a8eb714e19536da944b14dae6e471d858372b7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b68da18299abf3975c01797d8e5373c7521b043362e316eb7d9b01298e56a67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca49ba21d1f35b7e0f05d693b498236d1f78c0cbb20f447d0aa1f2ca26697bb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ddc6a704ed5c583bbcd4e0b4cec582d99f2183d6846923b9bd3af8cf1a4026b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KeyVaultAccessPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultAccessPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b298f261f526ebf6ff6c33763a1e55b6ba6eee2ac9f75bde318ad04cef2909bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApplicationId")
    def reset_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationId", []))

    @jsii.member(jsii_name="resetCertificatePermissions")
    def reset_certificate_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePermissions", []))

    @jsii.member(jsii_name="resetKeyPermissions")
    def reset_key_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPermissions", []))

    @jsii.member(jsii_name="resetObjectId")
    def reset_object_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectId", []))

    @jsii.member(jsii_name="resetSecretPermissions")
    def reset_secret_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretPermissions", []))

    @jsii.member(jsii_name="resetStoragePermissions")
    def reset_storage_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragePermissions", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePermissionsInput")
    def certificate_permissions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificatePermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPermissionsInput")
    def key_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keyPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretPermissionsInput")
    def secret_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretPermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="storagePermissionsInput")
    def storage_permissions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "storagePermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945d43a12644a44f26e752f55ad46ee3fdefd8c30d2d709581b8b806e1862cb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePermissions")
    def certificate_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificatePermissions"))

    @certificate_permissions.setter
    def certificate_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d228cb2a74b42215069a187de5a13be71420efb6e99353df409125359b1e221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePermissions", value)

    @builtins.property
    @jsii.member(jsii_name="keyPermissions")
    def key_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keyPermissions"))

    @key_permissions.setter
    def key_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47977a72183511ff6c679f7282fd41dcbf6715b05e945833a77a430f5bae45ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @object_id.setter
    def object_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0672cf70d0715d2094bc009f88f2fcf3c747e367a0c8973e8238df75210fcdd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectId", value)

    @builtins.property
    @jsii.member(jsii_name="secretPermissions")
    def secret_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secretPermissions"))

    @secret_permissions.setter
    def secret_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a27c88d3ec71f323057ef788a4a00b3a6ab283647e92196b709ff670dc26c962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="storagePermissions")
    def storage_permissions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "storagePermissions"))

    @storage_permissions.setter
    def storage_permissions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8585986c9d8f2597f80f249a56ddb58c66102fe51805d864367b2ad64a0fdf41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagePermissions", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0ee8256e4b289034742de4a90e39302f5194cf6e98452c37f75313b93b2ea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultAccessPolicy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultAccessPolicy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultAccessPolicy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb4971ea5468f906a3abcea9b88cc6db3e827dee062c02eae256e73e42db716b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "tenant_id": "tenantId",
        "access_policy": "accessPolicy",
        "enabled_for_deployment": "enabledForDeployment",
        "enabled_for_disk_encryption": "enabledForDiskEncryption",
        "enabled_for_template_deployment": "enabledForTemplateDeployment",
        "enable_rbac_authorization": "enableRbacAuthorization",
        "id": "id",
        "network_acls": "networkAcls",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class KeyVaultConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        tenant_id: builtins.str,
        access_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyVaultAccessPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        network_acls: typing.Optional[typing.Union["KeyVaultNetworkAcls", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["KeyVaultTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#location KeyVault#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#name KeyVault#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#resource_group_name KeyVault#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#sku_name KeyVault#sku_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tenant_id KeyVault#tenant_id}.
        :param access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#access_policy KeyVault#access_policy}.
        :param enabled_for_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.
        :param enabled_for_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.
        :param enabled_for_template_deployment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.
        :param enable_rbac_authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#id KeyVault#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_acls: network_acls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#network_acls KeyVault#network_acls}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tags KeyVault#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#timeouts KeyVault#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(network_acls, dict):
            network_acls = KeyVaultNetworkAcls(**network_acls)
        if isinstance(timeouts, dict):
            timeouts = KeyVaultTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63285cd7f4c3b1ed91947e16ce30fa45471b2cff52a49e5a903f32a816eeadda)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument enabled_for_deployment", value=enabled_for_deployment, expected_type=type_hints["enabled_for_deployment"])
            check_type(argname="argument enabled_for_disk_encryption", value=enabled_for_disk_encryption, expected_type=type_hints["enabled_for_disk_encryption"])
            check_type(argname="argument enabled_for_template_deployment", value=enabled_for_template_deployment, expected_type=type_hints["enabled_for_template_deployment"])
            check_type(argname="argument enable_rbac_authorization", value=enable_rbac_authorization, expected_type=type_hints["enable_rbac_authorization"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network_acls", value=network_acls, expected_type=type_hints["network_acls"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
            "tenant_id": tenant_id,
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
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if enabled_for_deployment is not None:
            self._values["enabled_for_deployment"] = enabled_for_deployment
        if enabled_for_disk_encryption is not None:
            self._values["enabled_for_disk_encryption"] = enabled_for_disk_encryption
        if enabled_for_template_deployment is not None:
            self._values["enabled_for_template_deployment"] = enabled_for_template_deployment
        if enable_rbac_authorization is not None:
            self._values["enable_rbac_authorization"] = enable_rbac_authorization
        if id is not None:
            self._values["id"] = id
        if network_acls is not None:
            self._values["network_acls"] = network_acls
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#location KeyVault#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#name KeyVault#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#resource_group_name KeyVault#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#sku_name KeyVault#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tenant_id KeyVault#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#access_policy KeyVault#access_policy}.'''
        result = self._values.get("access_policy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]], result)

    @builtins.property
    def enabled_for_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_deployment KeyVault#enabled_for_deployment}.'''
        result = self._values.get("enabled_for_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enabled_for_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_disk_encryption KeyVault#enabled_for_disk_encryption}.'''
        result = self._values.get("enabled_for_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enabled_for_template_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enabled_for_template_deployment KeyVault#enabled_for_template_deployment}.'''
        result = self._values.get("enabled_for_template_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_rbac_authorization(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#enable_rbac_authorization KeyVault#enable_rbac_authorization}.'''
        result = self._values.get("enable_rbac_authorization")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#id KeyVault#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_acls(self) -> typing.Optional["KeyVaultNetworkAcls"]:
        '''network_acls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#network_acls KeyVault#network_acls}
        '''
        result = self._values.get("network_acls")
        return typing.cast(typing.Optional["KeyVaultNetworkAcls"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#tags KeyVault#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["KeyVaultTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#timeouts KeyVault#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["KeyVaultTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultNetworkAcls",
    jsii_struct_bases=[],
    name_mapping={
        "bypass": "bypass",
        "default_action": "defaultAction",
        "ip_rules": "ipRules",
        "virtual_network_subnet_ids": "virtualNetworkSubnetIds",
    },
)
class KeyVaultNetworkAcls:
    def __init__(
        self,
        *,
        bypass: builtins.str,
        default_action: builtins.str,
        ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#bypass KeyVault#bypass}.
        :param default_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#default_action KeyVault#default_action}.
        :param ip_rules: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#ip_rules KeyVault#ip_rules}.
        :param virtual_network_subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a11747144a69bb3a6bd1f34dd073d65c8ac8213ea3bf7ede75ea0935d40672)
            check_type(argname="argument bypass", value=bypass, expected_type=type_hints["bypass"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
            check_type(argname="argument ip_rules", value=ip_rules, expected_type=type_hints["ip_rules"])
            check_type(argname="argument virtual_network_subnet_ids", value=virtual_network_subnet_ids, expected_type=type_hints["virtual_network_subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bypass": bypass,
            "default_action": default_action,
        }
        if ip_rules is not None:
            self._values["ip_rules"] = ip_rules
        if virtual_network_subnet_ids is not None:
            self._values["virtual_network_subnet_ids"] = virtual_network_subnet_ids

    @builtins.property
    def bypass(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#bypass KeyVault#bypass}.'''
        result = self._values.get("bypass")
        assert result is not None, "Required property 'bypass' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#default_action KeyVault#default_action}.'''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_rules(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#ip_rules KeyVault#ip_rules}.'''
        result = self._values.get("ip_rules")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def virtual_network_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#virtual_network_subnet_ids KeyVault#virtual_network_subnet_ids}.'''
        result = self._values.get("virtual_network_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultNetworkAcls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultNetworkAclsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultNetworkAclsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__985eb535eb12d30b16a9a804957ab96ca4aed3ef807834c924f51566aeb69631)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIpRules")
    def reset_ip_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRules", []))

    @jsii.member(jsii_name="resetVirtualNetworkSubnetIds")
    def reset_virtual_network_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkSubnetIds", []))

    @builtins.property
    @jsii.member(jsii_name="bypassInput")
    def bypass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bypassInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultActionInput")
    def default_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultActionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRulesInput")
    def ip_rules_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIdsInput")
    def virtual_network_subnet_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualNetworkSubnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="bypass")
    def bypass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bypass"))

    @bypass.setter
    def bypass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b647136ea144197716b49beeb97af2aae8bd54a394ef318a44c98f435b853e92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypass", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a3a963fd5e95be099fa1ca5a24be2923db4d290bbf08d6d94427376c57585f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAction", value)

    @builtins.property
    @jsii.member(jsii_name="ipRules")
    def ip_rules(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipRules"))

    @ip_rules.setter
    def ip_rules(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a756916c802e02bd6758a385f9b2f5a8abe2fa67577b8dec1fda3ab2693d697)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRules", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkSubnetIds")
    def virtual_network_subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualNetworkSubnetIds"))

    @virtual_network_subnet_ids.setter
    def virtual_network_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc3dd32ec145146f73049059283bd1d81f3ed950943b0949422ccea6b6fbe00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkSubnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[KeyVaultNetworkAcls]:
        return typing.cast(typing.Optional[KeyVaultNetworkAcls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[KeyVaultNetworkAcls]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dcac59f634380490b90ed1f93bb38b1ef2c23d2efb50fe51fe3612f7a86845e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class KeyVaultTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#create KeyVault#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#delete KeyVault#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#read KeyVault#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#update KeyVault#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e40621eee98d0448ae8b7b92b7eb782321ad0933eec48d77105f49e2a9166a0)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#create KeyVault#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#delete KeyVault#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#read KeyVault#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/key_vault#update KeyVault#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyVaultTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyVaultTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.keyVault.KeyVaultTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__049c12b8a2d480ed4846682641c38b56e00aedb9887901f89e3b800965ca7541)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce2407fac4175921f9a3dce7f49b75f93a320c163c6cbe137aaf7c3a142f963e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3186773640fcf50694b8bf14820622bb2dfedee15f0b748438c74fa204a3f1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579d7a948a594a4e530c0e37799f9faa3dc18cd6b7becb270ad818c539f2b859)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc255354cadf3a992b1a81b7f18e40641b4681f2734118d03ee19587424cac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[KeyVaultTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[KeyVaultTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[KeyVaultTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b2bb64c5629dbb96706439f56e51d66b604944302627ca511e6062a522766a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KeyVault",
    "KeyVaultAccessPolicy",
    "KeyVaultAccessPolicyList",
    "KeyVaultAccessPolicyOutputReference",
    "KeyVaultConfig",
    "KeyVaultNetworkAcls",
    "KeyVaultNetworkAclsOutputReference",
    "KeyVaultTimeouts",
    "KeyVaultTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d000889d0c678b0decd84240145a24b38de67132eca6182aad62a08cf6744620(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    sku_name: builtins.str,
    tenant_id: builtins.str,
    access_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyVaultAccessPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    network_acls: typing.Optional[typing.Union[KeyVaultNetworkAcls, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KeyVaultTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9e472a73e8ff2c0efb6a8a1c5b9310643dcaefdc0de16fdc1b0ba9c9a8dc7625(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyVaultAccessPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9912e78a3c129aae299581ebd372ecee1f3242629f1d0a74fefb90093e632d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e115ac7388250e02bcfc2d38a9e264f06d4fe8ce0e28c9474e21fbaca4e364(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e492dfb4162cffbe4328d4506d2e9163b066fdf73738269dc2b7a82d4b502476(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a1bd0913b7fdaa41f41f7ae9bd3932316092ba58de4d10afa73f29465674bf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cba2ed1baab031e9d8898e56dbd0d812129daaffea0ea10db1af9c740924077f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8904eee7ea98a415d085786a630cbbcf590f38349067bda3651628b0b5bdd9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7032953f9743f085cb102be20570f2487adbab80e1dd35552e633587b817471(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a1b9e2c4d180ba43f491be1691c4b474c9e5743356b50cf79b3aba811ea4bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6473ce4e5bc7e795b87a66a63b7d04e10b5854311cb6ed048ac82fadf35de1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c25d2bb2aa73b4afb3fb950577180201b3ef7528e7591c91496b6fb5d4a5f6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6aa2676cf64c9816a938d7b823af12f6cccda7d80290c14686a53c92528c78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ffa214ed4eb30bd5fb7f43b242d4f7e3a1c532bd761b3c2e390ffc31d43a0b(
    *,
    application_id: typing.Optional[builtins.str] = None,
    certificate_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    object_id: typing.Optional[builtins.str] = None,
    secret_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tenant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7985ada42aeec13ab5f464ab5a6b11249a811d739480817c382e1c0b58985d11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be3b3ac7f92b3ac4bae47d7fb4db3d8262b8d858d24d7e9c4b484907b19433a8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aefb0d2a96ab7578b26884cd89a8eb714e19536da944b14dae6e471d858372b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b68da18299abf3975c01797d8e5373c7521b043362e316eb7d9b01298e56a67(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca49ba21d1f35b7e0f05d693b498236d1f78c0cbb20f447d0aa1f2ca26697bb2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ddc6a704ed5c583bbcd4e0b4cec582d99f2183d6846923b9bd3af8cf1a4026b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KeyVaultAccessPolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b298f261f526ebf6ff6c33763a1e55b6ba6eee2ac9f75bde318ad04cef2909bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945d43a12644a44f26e752f55ad46ee3fdefd8c30d2d709581b8b806e1862cb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d228cb2a74b42215069a187de5a13be71420efb6e99353df409125359b1e221(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47977a72183511ff6c679f7282fd41dcbf6715b05e945833a77a430f5bae45ad(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0672cf70d0715d2094bc009f88f2fcf3c747e367a0c8973e8238df75210fcdd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27c88d3ec71f323057ef788a4a00b3a6ab283647e92196b709ff670dc26c962(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8585986c9d8f2597f80f249a56ddb58c66102fe51805d864367b2ad64a0fdf41(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0ee8256e4b289034742de4a90e39302f5194cf6e98452c37f75313b93b2ea9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4971ea5468f906a3abcea9b88cc6db3e827dee062c02eae256e73e42db716b(
    value: typing.Optional[typing.Union[KeyVaultAccessPolicy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63285cd7f4c3b1ed91947e16ce30fa45471b2cff52a49e5a903f32a816eeadda(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    sku_name: builtins.str,
    tenant_id: builtins.str,
    access_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KeyVaultAccessPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled_for_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled_for_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled_for_template_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_rbac_authorization: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    network_acls: typing.Optional[typing.Union[KeyVaultNetworkAcls, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[KeyVaultTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a11747144a69bb3a6bd1f34dd073d65c8ac8213ea3bf7ede75ea0935d40672(
    *,
    bypass: builtins.str,
    default_action: builtins.str,
    ip_rules: typing.Optional[typing.Sequence[builtins.str]] = None,
    virtual_network_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985eb535eb12d30b16a9a804957ab96ca4aed3ef807834c924f51566aeb69631(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b647136ea144197716b49beeb97af2aae8bd54a394ef318a44c98f435b853e92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a3a963fd5e95be099fa1ca5a24be2923db4d290bbf08d6d94427376c57585f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a756916c802e02bd6758a385f9b2f5a8abe2fa67577b8dec1fda3ab2693d697(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc3dd32ec145146f73049059283bd1d81f3ed950943b0949422ccea6b6fbe00(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dcac59f634380490b90ed1f93bb38b1ef2c23d2efb50fe51fe3612f7a86845e(
    value: typing.Optional[KeyVaultNetworkAcls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e40621eee98d0448ae8b7b92b7eb782321ad0933eec48d77105f49e2a9166a0(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049c12b8a2d480ed4846682641c38b56e00aedb9887901f89e3b800965ca7541(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2407fac4175921f9a3dce7f49b75f93a320c163c6cbe137aaf7c3a142f963e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3186773640fcf50694b8bf14820622bb2dfedee15f0b748438c74fa204a3f1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579d7a948a594a4e530c0e37799f9faa3dc18cd6b7becb270ad818c539f2b859(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc255354cadf3a992b1a81b7f18e40641b4681f2734118d03ee19587424cac0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b2bb64c5629dbb96706439f56e51d66b604944302627ca511e6062a522766a(
    value: typing.Optional[typing.Union[KeyVaultTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
