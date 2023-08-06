'''
# `azurestack_network_security_rule`

Refer to the Terraform Registory for docs: [`azurestack_network_security_rule`](https://www.terraform.io/docs/providers/azurestack/r/network_security_rule).
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


class NetworkSecurityRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkSecurityRule.NetworkSecurityRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule azurestack_network_security_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        access: builtins.str,
        direction: builtins.str,
        name: builtins.str,
        network_security_group_name: builtins.str,
        priority: jsii.Number,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_address_prefix: typing.Optional[builtins.str] = None,
        destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_port_range: typing.Optional[builtins.str] = None,
        destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        source_address_prefix: typing.Optional[builtins.str] = None,
        source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_port_range: typing.Optional[builtins.str] = None,
        source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule azurestack_network_security_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#access NetworkSecurityRule#access}.
        :param direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#direction NetworkSecurityRule#direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#name NetworkSecurityRule#name}.
        :param network_security_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#priority NetworkSecurityRule#priority}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#protocol NetworkSecurityRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#description NetworkSecurityRule#description}.
        :param destination_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.
        :param destination_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.
        :param destination_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.
        :param destination_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#id NetworkSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.
        :param source_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.
        :param source_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.
        :param source_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__686e30204b3cf986857fd50d9d0565c1134eb819c4833babb9ad51ed0c12ba31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkSecurityRuleConfig(
            access=access,
            direction=direction,
            name=name,
            network_security_group_name=network_security_group_name,
            priority=priority,
            protocol=protocol,
            resource_group_name=resource_group_name,
            description=description,
            destination_address_prefix=destination_address_prefix,
            destination_address_prefixes=destination_address_prefixes,
            destination_port_range=destination_port_range,
            destination_port_ranges=destination_port_ranges,
            id=id,
            source_address_prefix=source_address_prefix,
            source_address_prefixes=source_address_prefixes,
            source_port_range=source_port_range,
            source_port_ranges=source_port_ranges,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#create NetworkSecurityRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#delete NetworkSecurityRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#read NetworkSecurityRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#update NetworkSecurityRule#update}.
        '''
        value = NetworkSecurityRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDestinationAddressPrefix")
    def reset_destination_address_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressPrefix", []))

    @jsii.member(jsii_name="resetDestinationAddressPrefixes")
    def reset_destination_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationAddressPrefixes", []))

    @jsii.member(jsii_name="resetDestinationPortRange")
    def reset_destination_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortRange", []))

    @jsii.member(jsii_name="resetDestinationPortRanges")
    def reset_destination_port_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPortRanges", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSourceAddressPrefix")
    def reset_source_address_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressPrefix", []))

    @jsii.member(jsii_name="resetSourceAddressPrefixes")
    def reset_source_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAddressPrefixes", []))

    @jsii.member(jsii_name="resetSourcePortRange")
    def reset_source_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortRange", []))

    @jsii.member(jsii_name="resetSourcePortRanges")
    def reset_source_port_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortRanges", []))

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
    def timeouts(self) -> "NetworkSecurityRuleTimeoutsOutputReference":
        return typing.cast("NetworkSecurityRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixesInput")
    def destination_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixInput")
    def destination_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRangeInput")
    def destination_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPortRangesInput")
    def destination_port_ranges_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationPortRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupNameInput")
    def network_security_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSecurityGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixesInput")
    def source_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixInput")
    def source_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRangeInput")
    def source_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRangesInput")
    def source_port_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcePortRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11017f2312ed263960203d95aaaf1570fbbd904054ee963d4ff5bd2f45efccd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98d99f2136386259ea8cdf51aea4be8c532e8b29334056ec2ec912b5b41d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefix")
    def destination_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationAddressPrefix"))

    @destination_address_prefix.setter
    def destination_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99be41f41bf3a9a7b37a6eb1bc32f4393fc3f026adafee5623a866b89b5e8344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="destinationAddressPrefixes")
    def destination_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationAddressPrefixes"))

    @destination_address_prefixes.setter
    def destination_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__492686e05a69ae9bff7723e60af634dd6b271f4f00022cfa6409b61c59e44350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortRange")
    def destination_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPortRange"))

    @destination_port_range.setter
    def destination_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb266248217335e4857a39fa3e1f15409ecc82f0d4bde0fae3b13de24f4d842)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortRange", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPortRanges")
    def destination_port_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationPortRanges"))

    @destination_port_ranges.setter
    def destination_port_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9400cafc2542c7495b8e7c093b43375cc76958153d2d23d8d32889daee4b912a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPortRanges", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d20b24daf0a07bf265071e2d4e8ba889c50195977f1015d997ae7821fc75fb87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446148621aa673468d1c092e0a93f5b53eaed468ca4bbe053d2a016ff40835cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__279637e49e303c7ea50640c2cea133ded384e62900ebddc8e2531e8b15a17167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupName")
    def network_security_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupName"))

    @network_security_group_name.setter
    def network_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f38ec0fbb62e4f34bd875b82cf4243192805f9d3bfac1556f2140988ec97fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d455ae8377427273cb3d639196f6073c5b0611e4bc16c527684b67ce0c7bfed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b5583c22395abec3724e3b19fb1e528be1afd891131f4240ffe0a9d325717f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945323170e0237ec27aa8aab1fa36e553ca8f0056d58fd9c384e609d016f3b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefix")
    def source_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAddressPrefix"))

    @source_address_prefix.setter
    def source_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a76f68523228a189a57111bbf401c1d98b699b50586b1ffb307243a176d3165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixes")
    def source_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceAddressPrefixes"))

    @source_address_prefixes.setter
    def source_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0add013d60b881af6cc28a1bd132d81f0d07ecf2413bf456f744faf8930369a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortRange")
    def source_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePortRange"))

    @source_port_range.setter
    def source_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0962b06d61d9f41458e0c5e32e4210aff7c5b54687666da43568831614e6e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortRange", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourcePortRanges"))

    @source_port_ranges.setter
    def source_port_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cb736f9afce0718202d0995ee1d610cc35358d28b347e43ccca8b5c862e0029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortRanges", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.networkSecurityRule.NetworkSecurityRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access": "access",
        "direction": "direction",
        "name": "name",
        "network_security_group_name": "networkSecurityGroupName",
        "priority": "priority",
        "protocol": "protocol",
        "resource_group_name": "resourceGroupName",
        "description": "description",
        "destination_address_prefix": "destinationAddressPrefix",
        "destination_address_prefixes": "destinationAddressPrefixes",
        "destination_port_range": "destinationPortRange",
        "destination_port_ranges": "destinationPortRanges",
        "id": "id",
        "source_address_prefix": "sourceAddressPrefix",
        "source_address_prefixes": "sourceAddressPrefixes",
        "source_port_range": "sourcePortRange",
        "source_port_ranges": "sourcePortRanges",
        "timeouts": "timeouts",
    },
)
class NetworkSecurityRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access: builtins.str,
        direction: builtins.str,
        name: builtins.str,
        network_security_group_name: builtins.str,
        priority: jsii.Number,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        destination_address_prefix: typing.Optional[builtins.str] = None,
        destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        destination_port_range: typing.Optional[builtins.str] = None,
        destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        source_address_prefix: typing.Optional[builtins.str] = None,
        source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_port_range: typing.Optional[builtins.str] = None,
        source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetworkSecurityRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#access NetworkSecurityRule#access}.
        :param direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#direction NetworkSecurityRule#direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#name NetworkSecurityRule#name}.
        :param network_security_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#priority NetworkSecurityRule#priority}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#protocol NetworkSecurityRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#description NetworkSecurityRule#description}.
        :param destination_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.
        :param destination_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.
        :param destination_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.
        :param destination_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#id NetworkSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param source_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.
        :param source_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.
        :param source_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.
        :param source_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = NetworkSecurityRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cc0e7dc52e75c5f36e8601209bff01c8c6721766d9c6760eb17b7985de6f615)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_security_group_name", value=network_security_group_name, expected_type=type_hints["network_security_group_name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_address_prefix", value=destination_address_prefix, expected_type=type_hints["destination_address_prefix"])
            check_type(argname="argument destination_address_prefixes", value=destination_address_prefixes, expected_type=type_hints["destination_address_prefixes"])
            check_type(argname="argument destination_port_range", value=destination_port_range, expected_type=type_hints["destination_port_range"])
            check_type(argname="argument destination_port_ranges", value=destination_port_ranges, expected_type=type_hints["destination_port_ranges"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source_address_prefix", value=source_address_prefix, expected_type=type_hints["source_address_prefix"])
            check_type(argname="argument source_address_prefixes", value=source_address_prefixes, expected_type=type_hints["source_address_prefixes"])
            check_type(argname="argument source_port_range", value=source_port_range, expected_type=type_hints["source_port_range"])
            check_type(argname="argument source_port_ranges", value=source_port_ranges, expected_type=type_hints["source_port_ranges"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access": access,
            "direction": direction,
            "name": name,
            "network_security_group_name": network_security_group_name,
            "priority": priority,
            "protocol": protocol,
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
        if description is not None:
            self._values["description"] = description
        if destination_address_prefix is not None:
            self._values["destination_address_prefix"] = destination_address_prefix
        if destination_address_prefixes is not None:
            self._values["destination_address_prefixes"] = destination_address_prefixes
        if destination_port_range is not None:
            self._values["destination_port_range"] = destination_port_range
        if destination_port_ranges is not None:
            self._values["destination_port_ranges"] = destination_port_ranges
        if id is not None:
            self._values["id"] = id
        if source_address_prefix is not None:
            self._values["source_address_prefix"] = source_address_prefix
        if source_address_prefixes is not None:
            self._values["source_address_prefixes"] = source_address_prefixes
        if source_port_range is not None:
            self._values["source_port_range"] = source_port_range
        if source_port_ranges is not None:
            self._values["source_port_ranges"] = source_port_ranges
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
    def access(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#access NetworkSecurityRule#access}.'''
        result = self._values.get("access")
        assert result is not None, "Required property 'access' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def direction(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#direction NetworkSecurityRule#direction}.'''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#name NetworkSecurityRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_security_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#network_security_group_name NetworkSecurityRule#network_security_group_name}.'''
        result = self._values.get("network_security_group_name")
        assert result is not None, "Required property 'network_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#priority NetworkSecurityRule#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#protocol NetworkSecurityRule#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#resource_group_name NetworkSecurityRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#description NetworkSecurityRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefix NetworkSecurityRule#destination_address_prefix}.'''
        result = self._values.get("destination_address_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_address_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_address_prefixes NetworkSecurityRule#destination_address_prefixes}.'''
        result = self._values.get("destination_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def destination_port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_range NetworkSecurityRule#destination_port_range}.'''
        result = self._values.get("destination_port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_port_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#destination_port_ranges NetworkSecurityRule#destination_port_ranges}.'''
        result = self._values.get("destination_port_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#id NetworkSecurityRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefix NetworkSecurityRule#source_address_prefix}.'''
        result = self._values.get("source_address_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_address_prefixes NetworkSecurityRule#source_address_prefixes}.'''
        result = self._values.get("source_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_port_range(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_range NetworkSecurityRule#source_port_range}.'''
        result = self._values.get("source_port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_port_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#source_port_ranges NetworkSecurityRule#source_port_ranges}.'''
        result = self._values.get("source_port_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkSecurityRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#timeouts NetworkSecurityRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkSecurityRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkSecurityRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.networkSecurityRule.NetworkSecurityRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetworkSecurityRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#create NetworkSecurityRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#delete NetworkSecurityRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#read NetworkSecurityRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#update NetworkSecurityRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7673e608f36210e78865080ed7e4f611692548d69c71f2417c2a4e7d353dcbe2)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#create NetworkSecurityRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#delete NetworkSecurityRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#read NetworkSecurityRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/network_security_rule#update NetworkSecurityRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkSecurityRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkSecurityRuleTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.networkSecurityRule.NetworkSecurityRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d13e43684632d6a1645417e8653366129f5f9711305558d3a88d2540050a142)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f51f1128dfd56bb1f4b013ee90956773301abb1f301ba92ccce29786bb745361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a2df6c54dcef8ea35c9c3801eed1b70b7cb97a3e4c054459e955d504c87d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82d2425ab38ee0712a87c1583d17f08e5e67fc4c36f3e786feb1c0e92957b97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b305c4e97a482932faf28ec89d343887a8be35fb8d7075a764d1586e399f8a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__291219a84ede6ebf2f0440d54a0c5bc5e1d76a5e8ad86c0462c2d48d6b6e0d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkSecurityRule",
    "NetworkSecurityRuleConfig",
    "NetworkSecurityRuleTimeouts",
    "NetworkSecurityRuleTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__686e30204b3cf986857fd50d9d0565c1134eb819c4833babb9ad51ed0c12ba31(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    access: builtins.str,
    direction: builtins.str,
    name: builtins.str,
    network_security_group_name: builtins.str,
    priority: jsii.Number,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    destination_address_prefix: typing.Optional[builtins.str] = None,
    destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    destination_port_range: typing.Optional[builtins.str] = None,
    destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    source_address_prefix: typing.Optional[builtins.str] = None,
    source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_port_range: typing.Optional[builtins.str] = None,
    source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__11017f2312ed263960203d95aaaf1570fbbd904054ee963d4ff5bd2f45efccd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98d99f2136386259ea8cdf51aea4be8c532e8b29334056ec2ec912b5b41d0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99be41f41bf3a9a7b37a6eb1bc32f4393fc3f026adafee5623a866b89b5e8344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__492686e05a69ae9bff7723e60af634dd6b271f4f00022cfa6409b61c59e44350(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb266248217335e4857a39fa3e1f15409ecc82f0d4bde0fae3b13de24f4d842(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9400cafc2542c7495b8e7c093b43375cc76958153d2d23d8d32889daee4b912a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20b24daf0a07bf265071e2d4e8ba889c50195977f1015d997ae7821fc75fb87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446148621aa673468d1c092e0a93f5b53eaed468ca4bbe053d2a016ff40835cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__279637e49e303c7ea50640c2cea133ded384e62900ebddc8e2531e8b15a17167(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f38ec0fbb62e4f34bd875b82cf4243192805f9d3bfac1556f2140988ec97fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d455ae8377427273cb3d639196f6073c5b0611e4bc16c527684b67ce0c7bfed(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b5583c22395abec3724e3b19fb1e528be1afd891131f4240ffe0a9d325717f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945323170e0237ec27aa8aab1fa36e553ca8f0056d58fd9c384e609d016f3b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a76f68523228a189a57111bbf401c1d98b699b50586b1ffb307243a176d3165(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0add013d60b881af6cc28a1bd132d81f0d07ecf2413bf456f744faf8930369a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0962b06d61d9f41458e0c5e32e4210aff7c5b54687666da43568831614e6e39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cb736f9afce0718202d0995ee1d610cc35358d28b347e43ccca8b5c862e0029(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cc0e7dc52e75c5f36e8601209bff01c8c6721766d9c6760eb17b7985de6f615(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    access: builtins.str,
    direction: builtins.str,
    name: builtins.str,
    network_security_group_name: builtins.str,
    priority: jsii.Number,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    destination_address_prefix: typing.Optional[builtins.str] = None,
    destination_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    destination_port_range: typing.Optional[builtins.str] = None,
    destination_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    source_address_prefix: typing.Optional[builtins.str] = None,
    source_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_port_range: typing.Optional[builtins.str] = None,
    source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7673e608f36210e78865080ed7e4f611692548d69c71f2417c2a4e7d353dcbe2(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d13e43684632d6a1645417e8653366129f5f9711305558d3a88d2540050a142(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f51f1128dfd56bb1f4b013ee90956773301abb1f301ba92ccce29786bb745361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a2df6c54dcef8ea35c9c3801eed1b70b7cb97a3e4c054459e955d504c87d27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82d2425ab38ee0712a87c1583d17f08e5e67fc4c36f3e786feb1c0e92957b97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b305c4e97a482932faf28ec89d343887a8be35fb8d7075a764d1586e399f8a8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__291219a84ede6ebf2f0440d54a0c5bc5e1d76a5e8ad86c0462c2d48d6b6e0d1b(
    value: typing.Optional[typing.Union[NetworkSecurityRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
