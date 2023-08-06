'''
# `azurestack_public_ip`

Refer to the Terraform Registory for docs: [`azurestack_public_ip`](https://www.terraform.io/docs/providers/azurestack/r/public_ip).
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


class PublicIp(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.publicIp.PublicIp",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip azurestack_public_ip}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        allocation_method: typing.Optional[builtins.str] = None,
        domain_name_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        ip_version: typing.Optional[builtins.str] = None,
        public_ip_address_allocation: typing.Optional[builtins.str] = None,
        reverse_fqdn: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PublicIpTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip azurestack_public_ip} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#location PublicIp#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#name PublicIp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#resource_group_name PublicIp#resource_group_name}.
        :param allocation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#allocation_method PublicIp#allocation_method}.
        :param domain_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#domain_name_label PublicIp#domain_name_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#id PublicIp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#idle_timeout_in_minutes PublicIp#idle_timeout_in_minutes}.
        :param ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#ip_version PublicIp#ip_version}.
        :param public_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#public_ip_address_allocation PublicIp#public_ip_address_allocation}.
        :param reverse_fqdn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#reverse_fqdn PublicIp#reverse_fqdn}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#sku PublicIp#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#tags PublicIp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#timeouts PublicIp#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33c9fa07e77b0deb41744d4584cd6395dbeecd79df22848c1c2205928d6f0bd9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PublicIpConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            allocation_method=allocation_method,
            domain_name_label=domain_name_label,
            id=id,
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            ip_version=ip_version,
            public_ip_address_allocation=public_ip_address_allocation,
            reverse_fqdn=reverse_fqdn,
            sku=sku,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#create PublicIp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#delete PublicIp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#read PublicIp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#update PublicIp#update}.
        '''
        value = PublicIpTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocationMethod")
    def reset_allocation_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationMethod", []))

    @jsii.member(jsii_name="resetDomainNameLabel")
    def reset_domain_name_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainNameLabel", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetPublicIpAddressAllocation")
    def reset_public_ip_address_allocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressAllocation", []))

    @jsii.member(jsii_name="resetReverseFqdn")
    def reset_reverse_fqdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseFqdn", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

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
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PublicIpTimeoutsOutputReference":
        return typing.cast("PublicIpTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocationMethodInput")
    def allocation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameLabelInput")
    def domain_name_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressAllocationInput")
    def public_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseFqdnInput")
    def reverse_fqdn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reverseFqdnInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PublicIpTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PublicIpTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationMethod")
    def allocation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationMethod"))

    @allocation_method.setter
    def allocation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b235429fd55eab0c7ab753e23842bfe07690443b330f281ee6a198d51e3bb14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="domainNameLabel")
    def domain_name_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainNameLabel"))

    @domain_name_label.setter
    def domain_name_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2909f091e17037940c0dd49606ae995ba5235995fc6bfbd02073e6023512f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainNameLabel", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d76c0df593b3d694260028c39b06c2711f918f86b0ca1a1d9ade980c254bfe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d62fd11bcce3cb24695ae2d0c2cdb30eab9be506ca93db9b1011d94073f4da5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4d42b06ff8bc08126166b86e66964bf130a4b343a53c66e9736f85b040cc1ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e1a50d1a7d0bcb4dbc51ca10728ebaf7e7863bc080084509f47104eb63778b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db988d1812f8dc6cf9dd77cea84fe8f8e066fa89edc23f2d6d9307afc28459cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressAllocation")
    def public_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressAllocation"))

    @public_ip_address_allocation.setter
    def public_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e108ae60eda72c2400de040c2ca0c12c53e99e8883515d3f3d3b9762c85b59bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9549c674de7ed3826972dc21594abf859e8bc5638570ce5f9aab5362acf2473a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="reverseFqdn")
    def reverse_fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reverseFqdn"))

    @reverse_fqdn.setter
    def reverse_fqdn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9cc842bc61e1f27b7ac85acd4c1e8e495a20ce4277686716f6e0c33ee3b60e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverseFqdn", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bbe54be5b0638db0a6814760e560e4d23502a3801a5b0af3bcfd70ffa2efcd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b21c21a28eeb2579cb35ffc96e2364b83def3b790e57af4b16b5549dbf5a9e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.publicIp.PublicIpConfig",
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
        "allocation_method": "allocationMethod",
        "domain_name_label": "domainNameLabel",
        "id": "id",
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "ip_version": "ipVersion",
        "public_ip_address_allocation": "publicIpAddressAllocation",
        "reverse_fqdn": "reverseFqdn",
        "sku": "sku",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class PublicIpConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        allocation_method: typing.Optional[builtins.str] = None,
        domain_name_label: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        ip_version: typing.Optional[builtins.str] = None,
        public_ip_address_allocation: typing.Optional[builtins.str] = None,
        reverse_fqdn: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PublicIpTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#location PublicIp#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#name PublicIp#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#resource_group_name PublicIp#resource_group_name}.
        :param allocation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#allocation_method PublicIp#allocation_method}.
        :param domain_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#domain_name_label PublicIp#domain_name_label}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#id PublicIp#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#idle_timeout_in_minutes PublicIp#idle_timeout_in_minutes}.
        :param ip_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#ip_version PublicIp#ip_version}.
        :param public_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#public_ip_address_allocation PublicIp#public_ip_address_allocation}.
        :param reverse_fqdn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#reverse_fqdn PublicIp#reverse_fqdn}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#sku PublicIp#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#tags PublicIp#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#timeouts PublicIp#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = PublicIpTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be3b715ed525c1820f0e8fd8ae3980a11db634e55831005ccc7bd1e335e7a801)
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
            check_type(argname="argument allocation_method", value=allocation_method, expected_type=type_hints["allocation_method"])
            check_type(argname="argument domain_name_label", value=domain_name_label, expected_type=type_hints["domain_name_label"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument public_ip_address_allocation", value=public_ip_address_allocation, expected_type=type_hints["public_ip_address_allocation"])
            check_type(argname="argument reverse_fqdn", value=reverse_fqdn, expected_type=type_hints["reverse_fqdn"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if allocation_method is not None:
            self._values["allocation_method"] = allocation_method
        if domain_name_label is not None:
            self._values["domain_name_label"] = domain_name_label
        if id is not None:
            self._values["id"] = id
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if public_ip_address_allocation is not None:
            self._values["public_ip_address_allocation"] = public_ip_address_allocation
        if reverse_fqdn is not None:
            self._values["reverse_fqdn"] = reverse_fqdn
        if sku is not None:
            self._values["sku"] = sku
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#location PublicIp#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#name PublicIp#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#resource_group_name PublicIp#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#allocation_method PublicIp#allocation_method}.'''
        result = self._values.get("allocation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name_label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#domain_name_label PublicIp#domain_name_label}.'''
        result = self._values.get("domain_name_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#id PublicIp#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#idle_timeout_in_minutes PublicIp#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#ip_version PublicIp#ip_version}.'''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ip_address_allocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#public_ip_address_allocation PublicIp#public_ip_address_allocation}.'''
        result = self._values.get("public_ip_address_allocation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reverse_fqdn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#reverse_fqdn PublicIp#reverse_fqdn}.'''
        result = self._values.get("reverse_fqdn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#sku PublicIp#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#tags PublicIp#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PublicIpTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#timeouts PublicIp#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PublicIpTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicIpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.publicIp.PublicIpTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class PublicIpTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#create PublicIp#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#delete PublicIp#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#read PublicIp#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#update PublicIp#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__309a6de1d00110260b7d056b1f246202f804eaff07427c27488a713d04e75eab)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#create PublicIp#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#delete PublicIp#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#read PublicIp#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/public_ip#update PublicIp#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicIpTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PublicIpTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.publicIp.PublicIpTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9724b001a4caa08ad16dfb6157c71ff19a8612ac4c37b2d6cae5e96bbba9ad70)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb148355a50bd8e3d328c12d73cc0b3334cb29be9f2bffa6111af1a98d22d066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdc23376d25be323e220dff4b05d147375ed0dccfe856bc9fee2f8e80f18b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fbc98a4b33a3118e45333a042b75cb5473725b171f88984a91431ceed1b3357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bced1903838020ff19c77c66848fc2e0fe8fa5a21b06e2433548a5ed0e3e5839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PublicIpTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PublicIpTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PublicIpTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae17171a548bd615338eae3f4df9a987762d6926c0b430dc46d232a6764ce4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PublicIp",
    "PublicIpConfig",
    "PublicIpTimeouts",
    "PublicIpTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__33c9fa07e77b0deb41744d4584cd6395dbeecd79df22848c1c2205928d6f0bd9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    allocation_method: typing.Optional[builtins.str] = None,
    domain_name_label: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ip_version: typing.Optional[builtins.str] = None,
    public_ip_address_allocation: typing.Optional[builtins.str] = None,
    reverse_fqdn: typing.Optional[builtins.str] = None,
    sku: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[PublicIpTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__6b235429fd55eab0c7ab753e23842bfe07690443b330f281ee6a198d51e3bb14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2909f091e17037940c0dd49606ae995ba5235995fc6bfbd02073e6023512f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d76c0df593b3d694260028c39b06c2711f918f86b0ca1a1d9ade980c254bfe4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d62fd11bcce3cb24695ae2d0c2cdb30eab9be506ca93db9b1011d94073f4da5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d42b06ff8bc08126166b86e66964bf130a4b343a53c66e9736f85b040cc1ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e1a50d1a7d0bcb4dbc51ca10728ebaf7e7863bc080084509f47104eb63778b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db988d1812f8dc6cf9dd77cea84fe8f8e066fa89edc23f2d6d9307afc28459cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e108ae60eda72c2400de040c2ca0c12c53e99e8883515d3f3d3b9762c85b59bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9549c674de7ed3826972dc21594abf859e8bc5638570ce5f9aab5362acf2473a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9cc842bc61e1f27b7ac85acd4c1e8e495a20ce4277686716f6e0c33ee3b60e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bbe54be5b0638db0a6814760e560e4d23502a3801a5b0af3bcfd70ffa2efcd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b21c21a28eeb2579cb35ffc96e2364b83def3b790e57af4b16b5549dbf5a9e25(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be3b715ed525c1820f0e8fd8ae3980a11db634e55831005ccc7bd1e335e7a801(
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
    allocation_method: typing.Optional[builtins.str] = None,
    domain_name_label: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ip_version: typing.Optional[builtins.str] = None,
    public_ip_address_allocation: typing.Optional[builtins.str] = None,
    reverse_fqdn: typing.Optional[builtins.str] = None,
    sku: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[PublicIpTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309a6de1d00110260b7d056b1f246202f804eaff07427c27488a713d04e75eab(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9724b001a4caa08ad16dfb6157c71ff19a8612ac4c37b2d6cae5e96bbba9ad70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb148355a50bd8e3d328c12d73cc0b3334cb29be9f2bffa6111af1a98d22d066(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdc23376d25be323e220dff4b05d147375ed0dccfe856bc9fee2f8e80f18b4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbc98a4b33a3118e45333a042b75cb5473725b171f88984a91431ceed1b3357(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bced1903838020ff19c77c66848fc2e0fe8fa5a21b06e2433548a5ed0e3e5839(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae17171a548bd615338eae3f4df9a987762d6926c0b430dc46d232a6764ce4f(
    value: typing.Optional[typing.Union[PublicIpTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
