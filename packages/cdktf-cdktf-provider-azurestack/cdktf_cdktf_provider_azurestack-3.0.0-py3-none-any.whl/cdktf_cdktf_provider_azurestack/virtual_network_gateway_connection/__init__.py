'''
# `azurestack_virtual_network_gateway_connection`

Refer to the Terraform Registory for docs: [`azurestack_virtual_network_gateway_connection`](https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection).
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


class VirtualNetworkGatewayConnection(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection azurestack_virtual_network_gateway_connection}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        type: builtins.str,
        virtual_network_gateway_id: builtins.str,
        authorization_key: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        express_route_circuit_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipsec_policy: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionIpsecPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        local_network_gateway_id: typing.Optional[builtins.str] = None,
        peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
        routing_weight: typing.Optional[jsii.Number] = None,
        shared_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection azurestack_virtual_network_gateway_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.
        :param authorization_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.
        :param express_route_circuit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        :param local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.
        :param peer_virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.
        :param routing_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.
        :param shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        :param use_policy_based_traffic_selectors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2709440d0263d79f4b45d97a3631b739ac2ee34ea59cbc0fcb4bb219581e64c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualNetworkGatewayConnectionConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            type=type,
            virtual_network_gateway_id=virtual_network_gateway_id,
            authorization_key=authorization_key,
            enable_bgp=enable_bgp,
            express_route_circuit_id=express_route_circuit_id,
            id=id,
            ipsec_policy=ipsec_policy,
            local_network_gateway_id=local_network_gateway_id,
            peer_virtual_network_gateway_id=peer_virtual_network_gateway_id,
            routing_weight=routing_weight,
            shared_key=shared_key,
            tags=tags,
            timeouts=timeouts,
            use_policy_based_traffic_selectors=use_policy_based_traffic_selectors,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIpsecPolicy")
    def put_ipsec_policy(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_datasize: typing.Optional[jsii.Number] = None,
        sa_lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.
        :param sa_datasize: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.
        :param sa_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.
        '''
        value = VirtualNetworkGatewayConnectionIpsecPolicy(
            dh_group=dh_group,
            ike_encryption=ike_encryption,
            ike_integrity=ike_integrity,
            ipsec_encryption=ipsec_encryption,
            ipsec_integrity=ipsec_integrity,
            pfs_group=pfs_group,
            sa_datasize=sa_datasize,
            sa_lifetime=sa_lifetime,
        )

        return typing.cast(None, jsii.invoke(self, "putIpsecPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.
        '''
        value = VirtualNetworkGatewayConnectionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthorizationKey")
    def reset_authorization_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationKey", []))

    @jsii.member(jsii_name="resetEnableBgp")
    def reset_enable_bgp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBgp", []))

    @jsii.member(jsii_name="resetExpressRouteCircuitId")
    def reset_express_route_circuit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpressRouteCircuitId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpsecPolicy")
    def reset_ipsec_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpsecPolicy", []))

    @jsii.member(jsii_name="resetLocalNetworkGatewayId")
    def reset_local_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalNetworkGatewayId", []))

    @jsii.member(jsii_name="resetPeerVirtualNetworkGatewayId")
    def reset_peer_virtual_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerVirtualNetworkGatewayId", []))

    @jsii.member(jsii_name="resetRoutingWeight")
    def reset_routing_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingWeight", []))

    @jsii.member(jsii_name="resetSharedKey")
    def reset_shared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedKey", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUsePolicyBasedTrafficSelectors")
    def reset_use_policy_based_traffic_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePolicyBasedTrafficSelectors", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicy")
    def ipsec_policy(
        self,
    ) -> "VirtualNetworkGatewayConnectionIpsecPolicyOutputReference":
        return typing.cast("VirtualNetworkGatewayConnectionIpsecPolicyOutputReference", jsii.get(self, "ipsecPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualNetworkGatewayConnectionTimeoutsOutputReference":
        return typing.cast("VirtualNetworkGatewayConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="authorizationKeyInput")
    def authorization_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBgpInput")
    def enable_bgp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBgpInput"))

    @builtins.property
    @jsii.member(jsii_name="expressRouteCircuitIdInput")
    def express_route_circuit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressRouteCircuitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicyInput")
    def ipsec_policy_input(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"], jsii.get(self, "ipsecPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="localNetworkGatewayIdInput")
    def local_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peerVirtualNetworkGatewayIdInput")
    def peer_virtual_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVirtualNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="routingWeightInput")
    def routing_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "routingWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedKeyInput")
    def shared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usePolicyBasedTrafficSelectorsInput")
    def use_policy_based_traffic_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "usePolicyBasedTrafficSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayIdInput")
    def virtual_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationKey")
    def authorization_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationKey"))

    @authorization_key.setter
    def authorization_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b7d4d393d98272b6525474536c1e301e21b02f863304945c0885fdb7809754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationKey", value)

    @builtins.property
    @jsii.member(jsii_name="enableBgp")
    def enable_bgp(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableBgp"))

    @enable_bgp.setter
    def enable_bgp(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a74d58369940126786219be42c5d25e14969fb32a00029d30cd07802a649da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBgp", value)

    @builtins.property
    @jsii.member(jsii_name="expressRouteCircuitId")
    def express_route_circuit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expressRouteCircuitId"))

    @express_route_circuit_id.setter
    def express_route_circuit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256a6135d39a16faebd0d62a58bdb8e5c2008f0602b9aa0c41460c8e3a03733f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expressRouteCircuitId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2d831f94762f018aeb868e890c7cc14f3cb8267744bc300668ffe3097ccabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="localNetworkGatewayId")
    def local_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localNetworkGatewayId"))

    @local_network_gateway_id.setter
    def local_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c1d5feceb39a0c7c3fa72add6b73446d194280ab2fdba51ada51cd203fc938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localNetworkGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836130c5cde6b24af0ca31af6a469f18605aa1fd0d932a3077c7c00090d533ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf40cf4a58a2c94da183e82d6ebd34b2d826816d73a2f8b6256671ad9b742582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peerVirtualNetworkGatewayId")
    def peer_virtual_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVirtualNetworkGatewayId"))

    @peer_virtual_network_gateway_id.setter
    def peer_virtual_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1905f9cbe68b483651898f5f437c5dcd7886c0ee0fd9d38f4bb90e63f318baca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVirtualNetworkGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d276f0f1973833f682834f40156c0916251e2a97d820762ba571f64cd08ce434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="routingWeight")
    def routing_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "routingWeight"))

    @routing_weight.setter
    def routing_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bbfbea3cb595500b0faf526f926e7e46b7742d3ecc11f698b1ea2581788954a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingWeight", value)

    @builtins.property
    @jsii.member(jsii_name="sharedKey")
    def shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedKey"))

    @shared_key.setter
    def shared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c9411a9270d6d97006e56533c47546ee0d3b74197290fcd864b620a2f4424d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__705d9ce83b685dc6d43ae655fbac925989e8da0bdcc092411a674710bf6aad81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ebe5706429e88de1ee2ddb0ddf101baf223440ccac499617a89015bbb5347f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usePolicyBasedTrafficSelectors")
    def use_policy_based_traffic_selectors(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "usePolicyBasedTrafficSelectors"))

    @use_policy_based_traffic_selectors.setter
    def use_policy_based_traffic_selectors(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82aff500122bddce5be933859c914d4e8ce929dbfe027162c2b5e4a03a3cff56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePolicyBasedTrafficSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayId")
    def virtual_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkGatewayId"))

    @virtual_network_gateway_id.setter
    def virtual_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__255ec853ff2bc1d440c42ba7447ee8de73d6941bab9d51876bc309eb188aa60f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionConfig",
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
        "type": "type",
        "virtual_network_gateway_id": "virtualNetworkGatewayId",
        "authorization_key": "authorizationKey",
        "enable_bgp": "enableBgp",
        "express_route_circuit_id": "expressRouteCircuitId",
        "id": "id",
        "ipsec_policy": "ipsecPolicy",
        "local_network_gateway_id": "localNetworkGatewayId",
        "peer_virtual_network_gateway_id": "peerVirtualNetworkGatewayId",
        "routing_weight": "routingWeight",
        "shared_key": "sharedKey",
        "tags": "tags",
        "timeouts": "timeouts",
        "use_policy_based_traffic_selectors": "usePolicyBasedTrafficSelectors",
    },
)
class VirtualNetworkGatewayConnectionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        type: builtins.str,
        virtual_network_gateway_id: builtins.str,
        authorization_key: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        express_route_circuit_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ipsec_policy: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionIpsecPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        local_network_gateway_id: typing.Optional[builtins.str] = None,
        peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
        routing_weight: typing.Optional[jsii.Number] = None,
        shared_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.
        :param authorization_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.
        :param express_route_circuit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        :param local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.
        :param peer_virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.
        :param routing_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.
        :param shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        :param use_policy_based_traffic_selectors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ipsec_policy, dict):
            ipsec_policy = VirtualNetworkGatewayConnectionIpsecPolicy(**ipsec_policy)
        if isinstance(timeouts, dict):
            timeouts = VirtualNetworkGatewayConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c38c73c0ac05e6ba2b3c415d48d1eb2c922ddb93d0cd62f273b1eea695d77ec)
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
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument virtual_network_gateway_id", value=virtual_network_gateway_id, expected_type=type_hints["virtual_network_gateway_id"])
            check_type(argname="argument authorization_key", value=authorization_key, expected_type=type_hints["authorization_key"])
            check_type(argname="argument enable_bgp", value=enable_bgp, expected_type=type_hints["enable_bgp"])
            check_type(argname="argument express_route_circuit_id", value=express_route_circuit_id, expected_type=type_hints["express_route_circuit_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ipsec_policy", value=ipsec_policy, expected_type=type_hints["ipsec_policy"])
            check_type(argname="argument local_network_gateway_id", value=local_network_gateway_id, expected_type=type_hints["local_network_gateway_id"])
            check_type(argname="argument peer_virtual_network_gateway_id", value=peer_virtual_network_gateway_id, expected_type=type_hints["peer_virtual_network_gateway_id"])
            check_type(argname="argument routing_weight", value=routing_weight, expected_type=type_hints["routing_weight"])
            check_type(argname="argument shared_key", value=shared_key, expected_type=type_hints["shared_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_policy_based_traffic_selectors", value=use_policy_based_traffic_selectors, expected_type=type_hints["use_policy_based_traffic_selectors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "type": type,
            "virtual_network_gateway_id": virtual_network_gateway_id,
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
        if authorization_key is not None:
            self._values["authorization_key"] = authorization_key
        if enable_bgp is not None:
            self._values["enable_bgp"] = enable_bgp
        if express_route_circuit_id is not None:
            self._values["express_route_circuit_id"] = express_route_circuit_id
        if id is not None:
            self._values["id"] = id
        if ipsec_policy is not None:
            self._values["ipsec_policy"] = ipsec_policy
        if local_network_gateway_id is not None:
            self._values["local_network_gateway_id"] = local_network_gateway_id
        if peer_virtual_network_gateway_id is not None:
            self._values["peer_virtual_network_gateway_id"] = peer_virtual_network_gateway_id
        if routing_weight is not None:
            self._values["routing_weight"] = routing_weight
        if shared_key is not None:
            self._values["shared_key"] = shared_key
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_policy_based_traffic_selectors is not None:
            self._values["use_policy_based_traffic_selectors"] = use_policy_based_traffic_selectors

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.'''
        result = self._values.get("virtual_network_gateway_id")
        assert result is not None, "Required property 'virtual_network_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.'''
        result = self._values.get("authorization_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_bgp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.'''
        result = self._values.get("enable_bgp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def express_route_circuit_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.'''
        result = self._values.get("express_route_circuit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipsec_policy(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"]:
        '''ipsec_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        '''
        result = self._values.get("ipsec_policy")
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"], result)

    @builtins.property
    def local_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.'''
        result = self._values.get("local_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_virtual_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.'''
        result = self._values.get("peer_virtual_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.'''
        result = self._values.get("routing_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.'''
        result = self._values.get("shared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualNetworkGatewayConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionTimeouts"], result)

    @builtins.property
    def use_policy_based_traffic_selectors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.'''
        result = self._values.get("use_policy_based_traffic_selectors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionIpsecPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "ike_encryption": "ikeEncryption",
        "ike_integrity": "ikeIntegrity",
        "ipsec_encryption": "ipsecEncryption",
        "ipsec_integrity": "ipsecIntegrity",
        "pfs_group": "pfsGroup",
        "sa_datasize": "saDatasize",
        "sa_lifetime": "saLifetime",
    },
)
class VirtualNetworkGatewayConnectionIpsecPolicy:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_datasize: typing.Optional[jsii.Number] = None,
        sa_lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.
        :param sa_datasize: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.
        :param sa_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98a0adec5ea0f658e5910aebc6dc8e7e4f4b0492859b0de6a391fb9e0452073b)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument ike_encryption", value=ike_encryption, expected_type=type_hints["ike_encryption"])
            check_type(argname="argument ike_integrity", value=ike_integrity, expected_type=type_hints["ike_integrity"])
            check_type(argname="argument ipsec_encryption", value=ipsec_encryption, expected_type=type_hints["ipsec_encryption"])
            check_type(argname="argument ipsec_integrity", value=ipsec_integrity, expected_type=type_hints["ipsec_integrity"])
            check_type(argname="argument pfs_group", value=pfs_group, expected_type=type_hints["pfs_group"])
            check_type(argname="argument sa_datasize", value=sa_datasize, expected_type=type_hints["sa_datasize"])
            check_type(argname="argument sa_lifetime", value=sa_lifetime, expected_type=type_hints["sa_lifetime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dh_group": dh_group,
            "ike_encryption": ike_encryption,
            "ike_integrity": ike_integrity,
            "ipsec_encryption": ipsec_encryption,
            "ipsec_integrity": ipsec_integrity,
            "pfs_group": pfs_group,
        }
        if sa_datasize is not None:
            self._values["sa_datasize"] = sa_datasize
        if sa_lifetime is not None:
            self._values["sa_lifetime"] = sa_lifetime

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.'''
        result = self._values.get("ike_encryption")
        assert result is not None, "Required property 'ike_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.'''
        result = self._values.get("ike_integrity")
        assert result is not None, "Required property 'ike_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.'''
        result = self._values.get("ipsec_encryption")
        assert result is not None, "Required property 'ipsec_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.'''
        result = self._values.get("ipsec_integrity")
        assert result is not None, "Required property 'ipsec_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pfs_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.'''
        result = self._values.get("pfs_group")
        assert result is not None, "Required property 'pfs_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sa_datasize(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.'''
        result = self._values.get("sa_datasize")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sa_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.'''
        result = self._values.get("sa_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionIpsecPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionIpsecPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionIpsecPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf3512c51134e43e6b247c477895036a91051451d46b2fa882ec243a6d9166fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSaDatasize")
    def reset_sa_datasize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaDatasize", []))

    @jsii.member(jsii_name="resetSaLifetime")
    def reset_sa_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeEncryptionInput")
    def ike_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrityInput")
    def ike_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryptionInput")
    def ipsec_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrityInput")
    def ipsec_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="pfsGroupInput")
    def pfs_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="saDatasizeInput")
    def sa_datasize_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saDatasizeInput"))

    @builtins.property
    @jsii.member(jsii_name="saLifetimeInput")
    def sa_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e8ffb7c85faa26c01069ffc8dd362fa915ae84ae58a4acaa03cb8e81173ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="ikeEncryption")
    def ike_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeEncryption"))

    @ike_encryption.setter
    def ike_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0786cbe01fca20fe21b8ce844d4acb05472a8cc6e7ba9e218b4a3f0390539e87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrity")
    def ike_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIntegrity"))

    @ike_integrity.setter
    def ike_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e188b8b11e0d349876b8a2bab19b83bcee70cbd2f1b1290ec33bfcc967264368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryption")
    def ipsec_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecEncryption"))

    @ipsec_encryption.setter
    def ipsec_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa0e03a2a0311e8cd325720e159bf8e6c2a02efa58ca246d215288b6259c8041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrity")
    def ipsec_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecIntegrity"))

    @ipsec_integrity.setter
    def ipsec_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b52a7f9632f5f25b0d329ddb0c603ae38dc4873c8799c6018c6791272cb7dac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="pfsGroup")
    def pfs_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfsGroup"))

    @pfs_group.setter
    def pfs_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a74beebb29a00bab9086886d9a4b5d96a08797560ed646729ea8b81090c5b23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="saDatasize")
    def sa_datasize(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saDatasize"))

    @sa_datasize.setter
    def sa_datasize(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d610699ea0e6378514e9d3d091c4a718f6788ddaf2deb17f70ede5040d4dcc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saDatasize", value)

    @builtins.property
    @jsii.member(jsii_name="saLifetime")
    def sa_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saLifetime"))

    @sa_lifetime.setter
    def sa_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c50a0db603fef2e4e1184773a0dc46697f0e0d29eeb670633c8e3b14dbed00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaf09d1ce7ccb65f72fd0f0f58293416a74777dd2f38f52a1d8d31d3ce8a8d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualNetworkGatewayConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb33c1aa90af1dface0c5b4b31b9aac2d1624b2e71646a766da5e5a87c327c8)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__392e46fb13a2621d1641b8e5e2f5eed2c9f9b3ef90acbd4e33def15e059506bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__648c9c313d4d40d2b7f656685985f17ec5823c82dc0676ced871fd09b82dcb75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9d103fef47a676dd7cd1e20f8916d3fd09a2ceb32cd83ddd716a8a85265342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3865e099e1b5f6a91c963049755c12fc7499f3a708531d3c80410d7dd3957aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f1bf046a8d05a7cf4cafde7e8760716e09dd3b01be74d6c9d14b0edc98755ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3f6156fb4031b2c9a9487a71fceeb292418d6ad37d7ee762290a3e40b3279ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualNetworkGatewayConnection",
    "VirtualNetworkGatewayConnectionConfig",
    "VirtualNetworkGatewayConnectionIpsecPolicy",
    "VirtualNetworkGatewayConnectionIpsecPolicyOutputReference",
    "VirtualNetworkGatewayConnectionTimeouts",
    "VirtualNetworkGatewayConnectionTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b2709440d0263d79f4b45d97a3631b739ac2ee34ea59cbc0fcb4bb219581e64c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    type: builtins.str,
    virtual_network_gateway_id: builtins.str,
    authorization_key: typing.Optional[builtins.str] = None,
    enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    express_route_circuit_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipsec_policy: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionIpsecPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    local_network_gateway_id: typing.Optional[builtins.str] = None,
    peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
    routing_weight: typing.Optional[jsii.Number] = None,
    shared_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__f9b7d4d393d98272b6525474536c1e301e21b02f863304945c0885fdb7809754(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a74d58369940126786219be42c5d25e14969fb32a00029d30cd07802a649da(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256a6135d39a16faebd0d62a58bdb8e5c2008f0602b9aa0c41460c8e3a03733f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2d831f94762f018aeb868e890c7cc14f3cb8267744bc300668ffe3097ccabf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c1d5feceb39a0c7c3fa72add6b73446d194280ab2fdba51ada51cd203fc938(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836130c5cde6b24af0ca31af6a469f18605aa1fd0d932a3077c7c00090d533ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf40cf4a58a2c94da183e82d6ebd34b2d826816d73a2f8b6256671ad9b742582(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1905f9cbe68b483651898f5f437c5dcd7886c0ee0fd9d38f4bb90e63f318baca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d276f0f1973833f682834f40156c0916251e2a97d820762ba571f64cd08ce434(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbfbea3cb595500b0faf526f926e7e46b7742d3ecc11f698b1ea2581788954a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c9411a9270d6d97006e56533c47546ee0d3b74197290fcd864b620a2f4424d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__705d9ce83b685dc6d43ae655fbac925989e8da0bdcc092411a674710bf6aad81(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ebe5706429e88de1ee2ddb0ddf101baf223440ccac499617a89015bbb5347f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82aff500122bddce5be933859c914d4e8ce929dbfe027162c2b5e4a03a3cff56(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__255ec853ff2bc1d440c42ba7447ee8de73d6941bab9d51876bc309eb188aa60f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c38c73c0ac05e6ba2b3c415d48d1eb2c922ddb93d0cd62f273b1eea695d77ec(
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
    type: builtins.str,
    virtual_network_gateway_id: builtins.str,
    authorization_key: typing.Optional[builtins.str] = None,
    enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    express_route_circuit_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ipsec_policy: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionIpsecPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    local_network_gateway_id: typing.Optional[builtins.str] = None,
    peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
    routing_weight: typing.Optional[jsii.Number] = None,
    shared_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a0adec5ea0f658e5910aebc6dc8e7e4f4b0492859b0de6a391fb9e0452073b(
    *,
    dh_group: builtins.str,
    ike_encryption: builtins.str,
    ike_integrity: builtins.str,
    ipsec_encryption: builtins.str,
    ipsec_integrity: builtins.str,
    pfs_group: builtins.str,
    sa_datasize: typing.Optional[jsii.Number] = None,
    sa_lifetime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf3512c51134e43e6b247c477895036a91051451d46b2fa882ec243a6d9166fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e8ffb7c85faa26c01069ffc8dd362fa915ae84ae58a4acaa03cb8e81173ff2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0786cbe01fca20fe21b8ce844d4acb05472a8cc6e7ba9e218b4a3f0390539e87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e188b8b11e0d349876b8a2bab19b83bcee70cbd2f1b1290ec33bfcc967264368(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa0e03a2a0311e8cd325720e159bf8e6c2a02efa58ca246d215288b6259c8041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52a7f9632f5f25b0d329ddb0c603ae38dc4873c8799c6018c6791272cb7dac5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a74beebb29a00bab9086886d9a4b5d96a08797560ed646729ea8b81090c5b23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d610699ea0e6378514e9d3d091c4a718f6788ddaf2deb17f70ede5040d4dcc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c50a0db603fef2e4e1184773a0dc46697f0e0d29eeb670633c8e3b14dbed00(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf09d1ce7ccb65f72fd0f0f58293416a74777dd2f38f52a1d8d31d3ce8a8d3a(
    value: typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb33c1aa90af1dface0c5b4b31b9aac2d1624b2e71646a766da5e5a87c327c8(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392e46fb13a2621d1641b8e5e2f5eed2c9f9b3ef90acbd4e33def15e059506bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648c9c313d4d40d2b7f656685985f17ec5823c82dc0676ced871fd09b82dcb75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9d103fef47a676dd7cd1e20f8916d3fd09a2ceb32cd83ddd716a8a85265342(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3865e099e1b5f6a91c963049755c12fc7499f3a708531d3c80410d7dd3957aff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1bf046a8d05a7cf4cafde7e8760716e09dd3b01be74d6c9d14b0edc98755ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f6156fb4031b2c9a9487a71fceeb292418d6ad37d7ee762290a3e40b3279ea(
    value: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
