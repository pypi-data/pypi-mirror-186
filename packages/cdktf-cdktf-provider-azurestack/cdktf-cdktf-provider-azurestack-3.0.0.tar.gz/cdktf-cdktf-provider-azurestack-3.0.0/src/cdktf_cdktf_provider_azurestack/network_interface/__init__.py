'''
# `azurestack_network_interface`

Refer to the Terraform Registory for docs: [`azurestack_network_interface`](https://www.terraform.io/docs/providers/azurestack/r/network_interface).
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


class NetworkInterface(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterface",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface azurestack_network_interface}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkInterfaceIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkInterfaceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface azurestack_network_interface} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#ip_configuration NetworkInterface#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#location NetworkInterface#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#name NetworkInterface#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#resource_group_name NetworkInterface#resource_group_name}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#dns_servers NetworkInterface#dns_servers}.
        :param enable_ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#enable_ip_forwarding NetworkInterface#enable_ip_forwarding}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#id NetworkInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#tags NetworkInterface#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#timeouts NetworkInterface#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__030453aa8b0a6986f1f2b0c948122653d5f36df5d6ab87c92031333c656183a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkInterfaceConfig(
            ip_configuration=ip_configuration,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            dns_servers=dns_servers,
            enable_ip_forwarding=enable_ip_forwarding,
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

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkInterfaceIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c403c462b7f7ed8500896bc8dbd5d62c1dca99b4b505f478da61bf605129eaba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#create NetworkInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#delete NetworkInterface#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#read NetworkInterface#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#update NetworkInterface#update}.
        '''
        value = NetworkInterfaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetEnableIpForwarding")
    def reset_enable_ip_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIpForwarding", []))

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
    @jsii.member(jsii_name="appliedDnsServers")
    def applied_dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "appliedDnsServers"))

    @builtins.property
    @jsii.member(jsii_name="internalDomainNameSuffix")
    def internal_domain_name_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalDomainNameSuffix"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(self) -> "NetworkInterfaceIpConfigurationList":
        return typing.cast("NetworkInterfaceIpConfigurationList", jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkInterfaceTimeoutsOutputReference":
        return typing.cast("NetworkInterfaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIpForwardingInput")
    def enable_ip_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableIpForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkInterfaceIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkInterfaceIpConfiguration"]]], jsii.get(self, "ipConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["NetworkInterfaceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkInterfaceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b966de9fc8b519f714334f222e7ba5505a80a179429fd1922cf0dc97627769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="enableIpForwarding")
    def enable_ip_forwarding(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableIpForwarding"))

    @enable_ip_forwarding.setter
    def enable_ip_forwarding(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30515895ba120e0ade47945e640ecc5cd52f1c84e02b4874deaf0c7ba9d066c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abcd0ec2592676bf8a3c5d576362e7a81c8e5010cbcd1646226ff2364f7e124)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9392a2e9da9f432d72f0f8b23a6e2c1d7af7ca471a47cd72c71b1f665c758a07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709cd490ad33aa53c0606994a3e267fed0b564d67030fd8479b1cce4490007a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c63a22007fab11ebd112afe190c15c797dcf6590197be11999f31833eca154c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7eed3a129380d1d936d93ccabb064b20357a94e38e815e8b349668cd139c0c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ip_configuration": "ipConfiguration",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "dns_servers": "dnsServers",
        "enable_ip_forwarding": "enableIpForwarding",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class NetworkInterfaceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkInterfaceIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkInterfaceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#ip_configuration NetworkInterface#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#location NetworkInterface#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#name NetworkInterface#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#resource_group_name NetworkInterface#resource_group_name}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#dns_servers NetworkInterface#dns_servers}.
        :param enable_ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#enable_ip_forwarding NetworkInterface#enable_ip_forwarding}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#id NetworkInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#tags NetworkInterface#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#timeouts NetworkInterface#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = NetworkInterfaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f962433652df4c4adb3133c828fefbdf004fa1e1b0cb9f94b96978af4017696f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument enable_ip_forwarding", value=enable_ip_forwarding, expected_type=type_hints["enable_ip_forwarding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_configuration": ip_configuration,
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
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if enable_ip_forwarding is not None:
            self._values["enable_ip_forwarding"] = enable_ip_forwarding
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
    def ip_configuration(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkInterfaceIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#ip_configuration NetworkInterface#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkInterfaceIpConfiguration"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#location NetworkInterface#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#name NetworkInterface#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#resource_group_name NetworkInterface#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#dns_servers NetworkInterface#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#enable_ip_forwarding NetworkInterface#enable_ip_forwarding}.'''
        result = self._values.get("enable_ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#id NetworkInterface#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#tags NetworkInterface#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkInterfaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#timeouts NetworkInterface#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkInterfaceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "private_ip_address_allocation": "privateIpAddressAllocation",
        "primary": "primary",
        "private_ip_address": "privateIpAddress",
        "private_ip_address_version": "privateIpAddressVersion",
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
    },
)
class NetworkInterfaceIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        private_ip_address_allocation: builtins.str,
        primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        private_ip_address: typing.Optional[builtins.str] = None,
        private_ip_address_version: typing.Optional[builtins.str] = None,
        public_ip_address_id: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#name NetworkInterface#name}.
        :param private_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address_allocation NetworkInterface#private_ip_address_allocation}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#primary NetworkInterface#primary}.
        :param private_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address NetworkInterface#private_ip_address}.
        :param private_ip_address_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address_version NetworkInterface#private_ip_address_version}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#public_ip_address_id NetworkInterface#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#subnet_id NetworkInterface#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5d8602d6dee815985fffec730ead7c9e8841bd8114a23f9d99b511ef68d14c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_address_allocation", value=private_ip_address_allocation, expected_type=type_hints["private_ip_address_allocation"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
            check_type(argname="argument private_ip_address_version", value=private_ip_address_version, expected_type=type_hints["private_ip_address_version"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "private_ip_address_allocation": private_ip_address_allocation,
        }
        if primary is not None:
            self._values["primary"] = primary
        if private_ip_address is not None:
            self._values["private_ip_address"] = private_ip_address
        if private_ip_address_version is not None:
            self._values["private_ip_address_version"] = private_ip_address_version
        if public_ip_address_id is not None:
            self._values["public_ip_address_id"] = public_ip_address_id
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#name NetworkInterface#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_ip_address_allocation(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address_allocation NetworkInterface#private_ip_address_allocation}.'''
        result = self._values.get("private_ip_address_allocation")
        assert result is not None, "Required property 'private_ip_address_allocation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#primary NetworkInterface#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def private_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address NetworkInterface#private_ip_address}.'''
        result = self._values.get("private_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#private_ip_address_version NetworkInterface#private_ip_address_version}.'''
        result = self._values.get("private_ip_address_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ip_address_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#public_ip_address_id NetworkInterface#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#subnet_id NetworkInterface#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkInterfaceIpConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceIpConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05513003638164b6c2d69495bb63f5dfbaf58b37d1131ff9df0174c62f3c009b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkInterfaceIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b3dc9008d8b8950d7398b48c628f468fd242bf530e5100b38a28bae5d05b1d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkInterfaceIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbbd66883ef3e03f18f2aa5c40985e04b27d2786c637665b7db7e557d8a2dd9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5c3c6a27db3bbb273f058e409acd5a0b10774bf7d8e0cf48e96e3dc508a3f94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60c0fbd51aeb15c252dfb5b46ca74d25c02204102b1c022a82c32281bf119cbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkInterfaceIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkInterfaceIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6371cded62baf9ae3a4b1fa2e01e87200ea5004c35bb8b05cd87704112805317)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkInterfaceIpConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fb8450b98eb993a28de08b1b544ccf7d4e0296d463596f711e5d73e22cdb674)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetPrivateIpAddress")
    def reset_private_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddress", []))

    @jsii.member(jsii_name="resetPrivateIpAddressVersion")
    def reset_private_ip_address_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddressVersion", []))

    @jsii.member(jsii_name="resetPublicIpAddressId")
    def reset_public_ip_address_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressId", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocationInput")
    def private_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressInput")
    def private_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressVersionInput")
    def private_ip_address_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c1403f3520d93e92d98f6f5898e42dc57ec23825475079ddb7f2b0e8a425fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c14a90e7da2c89772ddec843bd9eb616cee94613d21b9e425f5fb5571644c4fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @private_ip_address.setter
    def private_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9f600aaee12e372fdca0ed5cf7563a6a6e8fdc332d2d7be18ba1c82d5d09b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressAllocation"))

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0431f06c9165bdfc2515edfc77bbdec1d1af8f12c270db91d4e54a5921492cbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressVersion")
    def private_ip_address_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressVersion"))

    @private_ip_address_version.setter
    def private_ip_address_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2f7e4f5ea9d91418235d5648a7741503b7fe1e4dc2b7949c897ec3cdb98f951)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressVersion", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd92a7ac4b38cdc1d67c0abb1a0aaf70d717933224e9bd88ef9fb507d08ca30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc10f0678a15bb5f3f79ba3a658b62d75672d2341cb231445ec94cfd55e98a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53b82370787973d3c5922bdcb5e5bb5ce208206acbaf1c7d3a24ccc2f4ecde6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetworkInterfaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#create NetworkInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#delete NetworkInterface#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#read NetworkInterface#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#update NetworkInterface#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ee2fffd5b3f6346703bc3617952105d1d1de36c0bc84cd77ddb629c21303af)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#create NetworkInterface#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#delete NetworkInterface#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#read NetworkInterface#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_interface#update NetworkInterface#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkInterfaceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkInterface.NetworkInterfaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4637ab893059f2e73783a5787daf7438d4f009c84f5f53cd259fb51c9c216a28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__993544799f3c7cc1ca4c548d9ca0d5649d81f7c839b902e304000cb71d485370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f5764b2f73b531d6291e83639c0307b282924753405bb80c826d85b6ac6543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aede65f39e14b1c3c93337f5b831a1ccda7712e1ebc40aa801e94a6d829d9122)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c93e45ace1596803838e83b602d16562f01eb999458d1dcb659a2a4fb5cd95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkInterfaceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkInterfaceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkInterfaceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d5d5eb435e6015a88284b0947917613327ed01153413bde9f584c14476c601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkInterface",
    "NetworkInterfaceConfig",
    "NetworkInterfaceIpConfiguration",
    "NetworkInterfaceIpConfigurationList",
    "NetworkInterfaceIpConfigurationOutputReference",
    "NetworkInterfaceTimeouts",
    "NetworkInterfaceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__030453aa8b0a6986f1f2b0c948122653d5f36df5d6ab87c92031333c656183a3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[NetworkInterfaceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__c403c462b7f7ed8500896bc8dbd5d62c1dca99b4b505f478da61bf605129eaba(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b966de9fc8b519f714334f222e7ba5505a80a179429fd1922cf0dc97627769(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30515895ba120e0ade47945e640ecc5cd52f1c84e02b4874deaf0c7ba9d066c7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abcd0ec2592676bf8a3c5d576362e7a81c8e5010cbcd1646226ff2364f7e124(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9392a2e9da9f432d72f0f8b23a6e2c1d7af7ca471a47cd72c71b1f665c758a07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709cd490ad33aa53c0606994a3e267fed0b564d67030fd8479b1cce4490007a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c63a22007fab11ebd112afe190c15c797dcf6590197be11999f31833eca154c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7eed3a129380d1d936d93ccabb064b20357a94e38e815e8b349668cd139c0c1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f962433652df4c4adb3133c828fefbdf004fa1e1b0cb9f94b96978af4017696f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[NetworkInterfaceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5d8602d6dee815985fffec730ead7c9e8841bd8114a23f9d99b511ef68d14c(
    *,
    name: builtins.str,
    private_ip_address_allocation: builtins.str,
    primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    private_ip_address: typing.Optional[builtins.str] = None,
    private_ip_address_version: typing.Optional[builtins.str] = None,
    public_ip_address_id: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05513003638164b6c2d69495bb63f5dfbaf58b37d1131ff9df0174c62f3c009b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b3dc9008d8b8950d7398b48c628f468fd242bf530e5100b38a28bae5d05b1d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbd66883ef3e03f18f2aa5c40985e04b27d2786c637665b7db7e557d8a2dd9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c3c6a27db3bbb273f058e409acd5a0b10774bf7d8e0cf48e96e3dc508a3f94(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c0fbd51aeb15c252dfb5b46ca74d25c02204102b1c022a82c32281bf119cbb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6371cded62baf9ae3a4b1fa2e01e87200ea5004c35bb8b05cd87704112805317(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkInterfaceIpConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb8450b98eb993a28de08b1b544ccf7d4e0296d463596f711e5d73e22cdb674(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c1403f3520d93e92d98f6f5898e42dc57ec23825475079ddb7f2b0e8a425fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c14a90e7da2c89772ddec843bd9eb616cee94613d21b9e425f5fb5571644c4fb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9f600aaee12e372fdca0ed5cf7563a6a6e8fdc332d2d7be18ba1c82d5d09b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0431f06c9165bdfc2515edfc77bbdec1d1af8f12c270db91d4e54a5921492cbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f7e4f5ea9d91418235d5648a7741503b7fe1e4dc2b7949c897ec3cdb98f951(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd92a7ac4b38cdc1d67c0abb1a0aaf70d717933224e9bd88ef9fb507d08ca30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc10f0678a15bb5f3f79ba3a658b62d75672d2341cb231445ec94cfd55e98a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b82370787973d3c5922bdcb5e5bb5ce208206acbaf1c7d3a24ccc2f4ecde6b(
    value: typing.Optional[typing.Union[NetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ee2fffd5b3f6346703bc3617952105d1d1de36c0bc84cd77ddb629c21303af(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4637ab893059f2e73783a5787daf7438d4f009c84f5f53cd259fb51c9c216a28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993544799f3c7cc1ca4c548d9ca0d5649d81f7c839b902e304000cb71d485370(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f5764b2f73b531d6291e83639c0307b282924753405bb80c826d85b6ac6543(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aede65f39e14b1c3c93337f5b831a1ccda7712e1ebc40aa801e94a6d829d9122(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c93e45ace1596803838e83b602d16562f01eb999458d1dcb659a2a4fb5cd95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d5d5eb435e6015a88284b0947917613327ed01153413bde9f584c14476c601(
    value: typing.Optional[typing.Union[NetworkInterfaceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
