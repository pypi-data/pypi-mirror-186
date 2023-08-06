'''
# `azurestack_virtual_network_gateway`

Refer to the Terraform Registory for docs: [`azurestack_virtual_network_gateway`](https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway).
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


class VirtualNetworkGateway(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway azurestack_virtual_network_gateway}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        type: builtins.str,
        active_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union["VirtualNetworkGatewayBgpSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        default_local_network_gateway_id: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpn_client_configuration: typing.Optional[typing.Union["VirtualNetworkGatewayVpnClientConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpn_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway azurestack_virtual_network_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#location VirtualNetworkGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#type VirtualNetworkGateway#type}.
        :param active_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        :param default_local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#id VirtualNetworkGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        :param vpn_client_configuration: vpn_client_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        :param vpn_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb38a1004c74bca57c7b0e7c7b608fe1832aad495cd23e7b4d14a6a21b113eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualNetworkGatewayConfig(
            ip_configuration=ip_configuration,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            type=type,
            active_active=active_active,
            bgp_settings=bgp_settings,
            default_local_network_gateway_id=default_local_network_gateway_id,
            enable_bgp=enable_bgp,
            id=id,
            tags=tags,
            timeouts=timeouts,
            vpn_client_configuration=vpn_client_configuration,
            vpn_type=vpn_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBgpSettings")
    def put_bgp_settings(
        self,
        *,
        asn: typing.Optional[jsii.Number] = None,
        peering_address: typing.Optional[builtins.str] = None,
        peer_weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.
        :param peering_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peering_address VirtualNetworkGateway#peering_address}.
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.
        '''
        value = VirtualNetworkGatewayBgpSettings(
            asn=asn, peering_address=peering_address, peer_weight=peer_weight
        )

        return typing.cast(None, jsii.invoke(self, "putBgpSettings", [value]))

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0da54847f246e5fa5b73f8d94278914bc196ab4ab72ec6990dafc573196ad9)
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#create VirtualNetworkGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#read VirtualNetworkGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#update VirtualNetworkGateway#update}.
        '''
        value = VirtualNetworkGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpnClientConfiguration")
    def put_vpn_client_configuration(
        self,
        *,
        address_space: typing.Sequence[builtins.str],
        radius_server_address: typing.Optional[builtins.str] = None,
        radius_server_secret: typing.Optional[builtins.str] = None,
        revoked_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        root_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vpn_client_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.
        :param radius_server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.
        :param radius_server_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.
        :param revoked_certificate: revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        :param root_certificate: root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        :param vpn_client_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.
        '''
        value = VirtualNetworkGatewayVpnClientConfiguration(
            address_space=address_space,
            radius_server_address=radius_server_address,
            radius_server_secret=radius_server_secret,
            revoked_certificate=revoked_certificate,
            root_certificate=root_certificate,
            vpn_client_protocols=vpn_client_protocols,
        )

        return typing.cast(None, jsii.invoke(self, "putVpnClientConfiguration", [value]))

    @jsii.member(jsii_name="resetActiveActive")
    def reset_active_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveActive", []))

    @jsii.member(jsii_name="resetBgpSettings")
    def reset_bgp_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpSettings", []))

    @jsii.member(jsii_name="resetDefaultLocalNetworkGatewayId")
    def reset_default_local_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLocalNetworkGatewayId", []))

    @jsii.member(jsii_name="resetEnableBgp")
    def reset_enable_bgp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBgp", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnClientConfiguration")
    def reset_vpn_client_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnClientConfiguration", []))

    @jsii.member(jsii_name="resetVpnType")
    def reset_vpn_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bgpSettings")
    def bgp_settings(self) -> "VirtualNetworkGatewayBgpSettingsOutputReference":
        return typing.cast("VirtualNetworkGatewayBgpSettingsOutputReference", jsii.get(self, "bgpSettings"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(self) -> "VirtualNetworkGatewayIpConfigurationList":
        return typing.cast("VirtualNetworkGatewayIpConfigurationList", jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualNetworkGatewayTimeoutsOutputReference":
        return typing.cast("VirtualNetworkGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientConfiguration")
    def vpn_client_configuration(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationOutputReference":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationOutputReference", jsii.get(self, "vpnClientConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="activeActiveInput")
    def active_active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeActiveInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpSettingsInput")
    def bgp_settings_input(self) -> typing.Optional["VirtualNetworkGatewayBgpSettings"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayBgpSettings"], jsii.get(self, "bgpSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLocalNetworkGatewayIdInput")
    def default_local_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLocalNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBgpInput")
    def enable_bgp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableBgpInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]], jsii.get(self, "ipConfigurationInput"))

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
    ) -> typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientConfigurationInput")
    def vpn_client_configuration_input(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"], jsii.get(self, "vpnClientConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnTypeInput")
    def vpn_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="activeActive")
    def active_active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "activeActive"))

    @active_active.setter
    def active_active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3516f48558eee6444277936d263ec8dbc49bded3288987f28ec97629a1122497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeActive", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLocalNetworkGatewayId")
    def default_local_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLocalNetworkGatewayId"))

    @default_local_network_gateway_id.setter
    def default_local_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59a1fd9a3856829b8c668a8775ea97380c117ebce4b728fb5d7062fbf5dd0ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLocalNetworkGatewayId", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__4f8d20bff3ddb1a63dd23eccf717b4126b0c43c0d340867485ba3e492a1e9210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBgp", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd920662c2f59b44347570b67735ba541f3da4a896d41210e94573049a841631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18230b2c1716455ba257411b9ed17df6b09e0f4f56562c1073e7d0779b191aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f4dde69c273a99007828e270cd268ce36379a7f3da794fa7ad091f84ed9d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1687695dc042c043d1de8ad77e387e1ef0dc18649f9d41d146eaa835683b90f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe7c63a7ed3bc8dc6252492b350af5c0c4d6a07f1e53bfb922a9b0127ce0325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a83bb82e27489718fa4ec5ee3ecafcd4030200f47f97645b81399d5dea353803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c39e24afc69e0fff9a7b906a76cfebf3725c67f9086dc423fb51fa235688fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vpnType")
    def vpn_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnType"))

    @vpn_type.setter
    def vpn_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3b8faa8db4445e896d41a4f7e7772f64654403995e8f3cedcea1251d8fea7fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayBgpSettings",
    jsii_struct_bases=[],
    name_mapping={
        "asn": "asn",
        "peering_address": "peeringAddress",
        "peer_weight": "peerWeight",
    },
)
class VirtualNetworkGatewayBgpSettings:
    def __init__(
        self,
        *,
        asn: typing.Optional[jsii.Number] = None,
        peering_address: typing.Optional[builtins.str] = None,
        peer_weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.
        :param peering_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peering_address VirtualNetworkGateway#peering_address}.
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d53f39e9f3569248b3e2f1ccb57515ca96a2fc8ae83667973ec3fe81a793d07)
            check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
            check_type(argname="argument peering_address", value=peering_address, expected_type=type_hints["peering_address"])
            check_type(argname="argument peer_weight", value=peer_weight, expected_type=type_hints["peer_weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if asn is not None:
            self._values["asn"] = asn
        if peering_address is not None:
            self._values["peering_address"] = peering_address
        if peer_weight is not None:
            self._values["peer_weight"] = peer_weight

    @builtins.property
    def asn(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.'''
        result = self._values.get("asn")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def peering_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peering_address VirtualNetworkGateway#peering_address}.'''
        result = self._values.get("peering_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.'''
        result = self._values.get("peer_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayBgpSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayBgpSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayBgpSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__babe3825631bf4b59327ebcaf9bcbff9dc543a724da1334075988db0b266c245)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAsn")
    def reset_asn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsn", []))

    @jsii.member(jsii_name="resetPeeringAddress")
    def reset_peering_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeeringAddress", []))

    @jsii.member(jsii_name="resetPeerWeight")
    def reset_peer_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerWeight", []))

    @builtins.property
    @jsii.member(jsii_name="asnInput")
    def asn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "asnInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringAddressInput")
    def peering_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peeringAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="peerWeightInput")
    def peer_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "peerWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="asn")
    def asn(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "asn"))

    @asn.setter
    def asn(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__848057dde5e58b62019de30e0ff86792d20bee714fca9fe9f52dcddc715aa76a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asn", value)

    @builtins.property
    @jsii.member(jsii_name="peeringAddress")
    def peering_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peeringAddress"))

    @peering_address.setter
    def peering_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b585ffef01ad9ffb95fc7659f2a176ca484039e6bc84e38da9c34b928bd182fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peeringAddress", value)

    @builtins.property
    @jsii.member(jsii_name="peerWeight")
    def peer_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "peerWeight"))

    @peer_weight.setter
    def peer_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c798c205c9ea91a4f4ecab83169a77139ed877a296c9f958ad0a230efcaef4ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerWeight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualNetworkGatewayBgpSettings]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayBgpSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayBgpSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0321a8a05243d062cfffa41e42f243cca2d7e284b30663597e86f64419f2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayConfig",
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
        "sku": "sku",
        "type": "type",
        "active_active": "activeActive",
        "bgp_settings": "bgpSettings",
        "default_local_network_gateway_id": "defaultLocalNetworkGatewayId",
        "enable_bgp": "enableBgp",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
        "vpn_client_configuration": "vpnClientConfiguration",
        "vpn_type": "vpnType",
    },
)
class VirtualNetworkGatewayConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        type: builtins.str,
        active_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        default_local_network_gateway_id: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpn_client_configuration: typing.Optional[typing.Union["VirtualNetworkGatewayVpnClientConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpn_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#location VirtualNetworkGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#type VirtualNetworkGateway#type}.
        :param active_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        :param default_local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#id VirtualNetworkGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        :param vpn_client_configuration: vpn_client_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        :param vpn_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bgp_settings, dict):
            bgp_settings = VirtualNetworkGatewayBgpSettings(**bgp_settings)
        if isinstance(timeouts, dict):
            timeouts = VirtualNetworkGatewayTimeouts(**timeouts)
        if isinstance(vpn_client_configuration, dict):
            vpn_client_configuration = VirtualNetworkGatewayVpnClientConfiguration(**vpn_client_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b980a9e34f0e3a362502ebd5733e85e6a76e57c97b4377d0ee752f91a61dbf2)
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
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument active_active", value=active_active, expected_type=type_hints["active_active"])
            check_type(argname="argument bgp_settings", value=bgp_settings, expected_type=type_hints["bgp_settings"])
            check_type(argname="argument default_local_network_gateway_id", value=default_local_network_gateway_id, expected_type=type_hints["default_local_network_gateway_id"])
            check_type(argname="argument enable_bgp", value=enable_bgp, expected_type=type_hints["enable_bgp"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_client_configuration", value=vpn_client_configuration, expected_type=type_hints["vpn_client_configuration"])
            check_type(argname="argument vpn_type", value=vpn_type, expected_type=type_hints["vpn_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if active_active is not None:
            self._values["active_active"] = active_active
        if bgp_settings is not None:
            self._values["bgp_settings"] = bgp_settings
        if default_local_network_gateway_id is not None:
            self._values["default_local_network_gateway_id"] = default_local_network_gateway_id
        if enable_bgp is not None:
            self._values["enable_bgp"] = enable_bgp
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_client_configuration is not None:
            self._values["vpn_client_configuration"] = vpn_client_configuration
        if vpn_type is not None:
            self._values["vpn_type"] = vpn_type

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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#location VirtualNetworkGateway#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#type VirtualNetworkGateway#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.'''
        result = self._values.get("active_active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def bgp_settings(self) -> typing.Optional[VirtualNetworkGatewayBgpSettings]:
        '''bgp_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        '''
        result = self._values.get("bgp_settings")
        return typing.cast(typing.Optional[VirtualNetworkGatewayBgpSettings], result)

    @builtins.property
    def default_local_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.'''
        result = self._values.get("default_local_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_bgp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.'''
        result = self._values.get("enable_bgp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#id VirtualNetworkGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualNetworkGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualNetworkGatewayTimeouts"], result)

    @builtins.property
    def vpn_client_configuration(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"]:
        '''vpn_client_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        '''
        result = self._values.get("vpn_client_configuration")
        return typing.cast(typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"], result)

    @builtins.property
    def vpn_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.'''
        result = self._values.get("vpn_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
        "name": "name",
        "private_ip_address_allocation": "privateIpAddressAllocation",
    },
)
class VirtualNetworkGatewayIpConfiguration:
    def __init__(
        self,
        *,
        public_ip_address_id: builtins.str,
        subnet_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        private_ip_address_allocation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#public_ip_address_id VirtualNetworkGateway#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#subnet_id VirtualNetworkGateway#subnet_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param private_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#private_ip_address_allocation VirtualNetworkGateway#private_ip_address_allocation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b3f7a5bc97608c7dd78a1e91694c462a6fe8e3724700a121fa3caaf092dbb7)
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_address_allocation", value=private_ip_address_allocation, expected_type=type_hints["private_ip_address_allocation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_ip_address_id": public_ip_address_id,
            "subnet_id": subnet_id,
        }
        if name is not None:
            self._values["name"] = name
        if private_ip_address_allocation is not None:
            self._values["private_ip_address_allocation"] = private_ip_address_allocation

    @builtins.property
    def public_ip_address_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#public_ip_address_id VirtualNetworkGateway#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        assert result is not None, "Required property 'public_ip_address_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#subnet_id VirtualNetworkGateway#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address_allocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#private_ip_address_allocation VirtualNetworkGateway#private_ip_address_allocation}.'''
        result = self._values.get("private_ip_address_allocation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayIpConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayIpConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99c68ad2463706a9dfad30a6b3c4cf82959f90d122a1f547e6fad0052f67ac00)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7979cbc0be5fe54b78ed75a0a02fd70092b67543a7d6d33588e7fe75e4c4f404)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a0e17dc19d9998a68e53f586d5b095c16c5e3252971d0d71f17693b44d1e36)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96f2765c82d3c977a4ac04f4a8f313ece5c4303dca945cc6b2a81875cd8b2145)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fd7e4ff4c59827596e45890782cd4bdd39250c3dd2a3e79b7e3d9c23e265035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6f2973a2f116c4bebbbeaecf89b051deff7b3c63f4399b17fff355f683f294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayIpConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c41c97d1ddd934924c969904257223a0e6c1379fbeb5c35e662f8387c1a28a12)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPrivateIpAddressAllocation")
    def reset_private_ip_address_allocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddressAllocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocationInput")
    def private_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressAllocationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__901ef510281837938e4deccf61573ce2d130aa8792e2c0e69e2e8dec67e19ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressAllocation"))

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1cd4a8c99ac240479fae1cf0758326869917de0a81a2fc522f2017ba2f82b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e46c61fc4ed7b505cab2b244b2d4f6c3865a3a6a18d43440b2ea123bebffaac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8617a68c7e8e11249c5cfd1382d62fa950722543c6d090bcef074efc8be056c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086c0a1c8a81075e9efe000e7a0221dd2a6c119f106b23de25802d96d6b7d3b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualNetworkGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#create VirtualNetworkGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#read VirtualNetworkGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#update VirtualNetworkGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f35b5cf2a39c3a7d18732851fc1ba93e4f62119e40ead06cc68882e8b307ac)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#create VirtualNetworkGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#read VirtualNetworkGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#update VirtualNetworkGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16e35a52181c74774d6fe1bbc14a96b58835dbfee6c787882a8a1c9334248abb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__28ae108ba387fdd0b54976bcd5f12b85b3e1a3053c4ed15a2c70ee07197640b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae1484529bf3700f0473cfc81f7f71d81eb7be8f1411ca7fdb2d219584b2dc61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2cb10414a5b1c1db0363c4a73b52a66bbccc960ed3d94804385f5bfa6119acd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d453f39daacd68b176d80d7923de56222e26da0d0f31bc590b59f1a0306deff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82efe8c462e7e4034cdfe258f3a4f95194a6df68753fdf91478bed03198c2c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "address_space": "addressSpace",
        "radius_server_address": "radiusServerAddress",
        "radius_server_secret": "radiusServerSecret",
        "revoked_certificate": "revokedCertificate",
        "root_certificate": "rootCertificate",
        "vpn_client_protocols": "vpnClientProtocols",
    },
)
class VirtualNetworkGatewayVpnClientConfiguration:
    def __init__(
        self,
        *,
        address_space: typing.Sequence[builtins.str],
        radius_server_address: typing.Optional[builtins.str] = None,
        radius_server_secret: typing.Optional[builtins.str] = None,
        revoked_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        root_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vpn_client_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.
        :param radius_server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.
        :param radius_server_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.
        :param revoked_certificate: revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        :param root_certificate: root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        :param vpn_client_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8148af1afe4960d786a17c3f13ba5c773a170218ad0c0a34562c32f9f6972ee2)
            check_type(argname="argument address_space", value=address_space, expected_type=type_hints["address_space"])
            check_type(argname="argument radius_server_address", value=radius_server_address, expected_type=type_hints["radius_server_address"])
            check_type(argname="argument radius_server_secret", value=radius_server_secret, expected_type=type_hints["radius_server_secret"])
            check_type(argname="argument revoked_certificate", value=revoked_certificate, expected_type=type_hints["revoked_certificate"])
            check_type(argname="argument root_certificate", value=root_certificate, expected_type=type_hints["root_certificate"])
            check_type(argname="argument vpn_client_protocols", value=vpn_client_protocols, expected_type=type_hints["vpn_client_protocols"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_space": address_space,
        }
        if radius_server_address is not None:
            self._values["radius_server_address"] = radius_server_address
        if radius_server_secret is not None:
            self._values["radius_server_secret"] = radius_server_secret
        if revoked_certificate is not None:
            self._values["revoked_certificate"] = revoked_certificate
        if root_certificate is not None:
            self._values["root_certificate"] = root_certificate
        if vpn_client_protocols is not None:
            self._values["vpn_client_protocols"] = vpn_client_protocols

    @builtins.property
    def address_space(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.'''
        result = self._values.get("address_space")
        assert result is not None, "Required property 'address_space' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def radius_server_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.'''
        result = self._values.get("radius_server_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def radius_server_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.'''
        result = self._values.get("radius_server_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revoked_certificate(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]]:
        '''revoked_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        '''
        result = self._values.get("revoked_certificate")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]], result)

    @builtins.property
    def root_certificate(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]]:
        '''root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        '''
        result = self._values.get("root_certificate")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]], result)

    @builtins.property
    def vpn_client_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.'''
        result = self._values.get("vpn_client_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__308f31c461af1348095b83bfc678418f4c73eeb9f7f57ce34544395179d46c30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRevokedCertificate")
    def put_revoked_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8012e10f1c1d54946febc9f0116f6c12fbe3a379ac77d4ea6bf6b22ea14db6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRevokedCertificate", [value]))

    @jsii.member(jsii_name="putRootCertificate")
    def put_root_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682f624a4a5f093c7309383b537b003fba13b607756f66b9c8007695308d96b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRootCertificate", [value]))

    @jsii.member(jsii_name="resetRadiusServerAddress")
    def reset_radius_server_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadiusServerAddress", []))

    @jsii.member(jsii_name="resetRadiusServerSecret")
    def reset_radius_server_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadiusServerSecret", []))

    @jsii.member(jsii_name="resetRevokedCertificate")
    def reset_revoked_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevokedCertificate", []))

    @jsii.member(jsii_name="resetRootCertificate")
    def reset_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootCertificate", []))

    @jsii.member(jsii_name="resetVpnClientProtocols")
    def reset_vpn_client_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnClientProtocols", []))

    @builtins.property
    @jsii.member(jsii_name="revokedCertificate")
    def revoked_certificate(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList", jsii.get(self, "revokedCertificate"))

    @builtins.property
    @jsii.member(jsii_name="rootCertificate")
    def root_certificate(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRootCertificateList":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRootCertificateList", jsii.get(self, "rootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="addressSpaceInput")
    def address_space_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressSpaceInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusServerAddressInput")
    def radius_server_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radiusServerAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusServerSecretInput")
    def radius_server_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radiusServerSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="revokedCertificateInput")
    def revoked_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]], jsii.get(self, "revokedCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="rootCertificateInput")
    def root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]], jsii.get(self, "rootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientProtocolsInput")
    def vpn_client_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpnClientProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="addressSpace")
    def address_space(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addressSpace"))

    @address_space.setter
    def address_space(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7ae699ede478af666254a88cafcdc11f7b147705592154ed1e9e007122b5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressSpace", value)

    @builtins.property
    @jsii.member(jsii_name="radiusServerAddress")
    def radius_server_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radiusServerAddress"))

    @radius_server_address.setter
    def radius_server_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50e3a7835d612345adba00d99cb500091b3bcff4baa553949cb436cdb87a33cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusServerAddress", value)

    @builtins.property
    @jsii.member(jsii_name="radiusServerSecret")
    def radius_server_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radiusServerSecret"))

    @radius_server_secret.setter
    def radius_server_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a25d1a6bdaa8c15e29277412be7578c218496b11a3a251bf1589a6ee1bda1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusServerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="vpnClientProtocols")
    def vpn_client_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpnClientProtocols"))

    @vpn_client_protocols.setter
    def vpn_client_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d80c963241e5814f40ea3e9ee5493dc983a69abe4dc5a615f17192cddd8022)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnClientProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualNetworkGatewayVpnClientConfiguration]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayVpnClientConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayVpnClientConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee043a7b8140811c9d403decd6289a1befec9d4b61b23d40ca059069e728ec57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "thumbprint": "thumbprint"},
)
class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate:
    def __init__(self, *, name: builtins.str, thumbprint: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#thumbprint VirtualNetworkGateway#thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fdc4d968a577b00144d659c86b0680d75de3b4b7faf8d8db1bd9f022fd4a17e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "thumbprint": thumbprint,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#thumbprint VirtualNetworkGateway#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea35a63d1616c0a0981aa7f578976e67ecd6b9c22f6390ad4f11d8f964efa3f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e171f91909855a3ba8030262ff531f2878079638ed4dd7dbb492366f84a453d7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618960fcb1a2055e9dcb457927a3de1c1afe2c9141259c282628a8013e4d48ab)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f89e96cba526858f51e464654a07f22ff43096578992b150ee72962bb0ca7179)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94eba6b540252be9840dfda8770c68f201dbc3fd3449193ed9196c08f45fe6fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c4d9da2f42ab230de334ba35d3bdcd5bcdc8956824911e3c8592372d7b0869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a93687eaab5e8d6c0cae468cccd33f4226e06334dae569005dbb04e0d9b54cbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce82b554f7c9a3ce7bc37520d39c9121888893cb8e246e0972b443aa1e8a8dd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9875d6db659b76f8daffb1b8635098e022aa63984229e2acb03cf416a5b3813e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91345c431aa84292323ebd5724c1a2c1944e30c596c070ff768f0e532ef40427)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "public_cert_data": "publicCertData"},
)
class VirtualNetworkGatewayVpnClientConfigurationRootCertificate:
    def __init__(self, *, name: builtins.str, public_cert_data: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param public_cert_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#public_cert_data VirtualNetworkGateway#public_cert_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce28fecfbea4bec750f25f5b233706f3642bb847eaf61342a3fcc0e3fb8aed03)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_cert_data", value=public_cert_data, expected_type=type_hints["public_cert_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "public_cert_data": public_cert_data,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_cert_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway#public_cert_data VirtualNetworkGateway#public_cert_data}.'''
        result = self._values.get("public_cert_data")
        assert result is not None, "Required property 'public_cert_data' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfigurationRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationRootCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__676d1827fe0a9a9c9d8c1a92f6627a87e6aa08b14aaf10ce1f3bd7d1de3b1f46)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1eba8db844aa5bcda512311a0ade4b2293950b62194dcc0b00d5edc74b6b71f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d82069c138aa54912f1e5c402683f6eee7d906ad5638d558e7948fcb50cd5deb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70d4d183f4eeddead90ae85e2f214192b8c72cba376b57d8c590ad777a21b174)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9dfd90f148de97027eada6e337be2deb8060297647757d0a84e17cb85ab7655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1205e03386b31a0e942807bd1f025d36132c2b066b075d95af0108cd726eac2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd87863206c60c294de09f95f270afd6a17bef00921e9d073b818328d3520167)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicCertDataInput")
    def public_cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicCertDataInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff8282f7490d90a0648313eed299087745fa0b0c1d09517911fd4387c9d5c49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicCertData")
    def public_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertData"))

    @public_cert_data.setter
    def public_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d85a5f68d1a3846e18a36f17290f5140f437c21c4fc0248b43f16a86b27e46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicCertData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1673f7a0b76a17d642b2e494d6d59b1ab703a90fa25708cec814a4cc959804e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualNetworkGateway",
    "VirtualNetworkGatewayBgpSettings",
    "VirtualNetworkGatewayBgpSettingsOutputReference",
    "VirtualNetworkGatewayConfig",
    "VirtualNetworkGatewayIpConfiguration",
    "VirtualNetworkGatewayIpConfigurationList",
    "VirtualNetworkGatewayIpConfigurationOutputReference",
    "VirtualNetworkGatewayTimeouts",
    "VirtualNetworkGatewayTimeoutsOutputReference",
    "VirtualNetworkGatewayVpnClientConfiguration",
    "VirtualNetworkGatewayVpnClientConfigurationOutputReference",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificate",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificateList",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference",
]

publication.publish()

def _typecheckingstub__afb38a1004c74bca57c7b0e7c7b608fe1832aad495cd23e7b4d14a6a21b113eb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    sku: builtins.str,
    type: builtins.str,
    active_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bgp_settings: typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    default_local_network_gateway_id: typing.Optional[builtins.str] = None,
    enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpn_client_configuration: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpn_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__bd0da54847f246e5fa5b73f8d94278914bc196ab4ab72ec6990dafc573196ad9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3516f48558eee6444277936d263ec8dbc49bded3288987f28ec97629a1122497(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59a1fd9a3856829b8c668a8775ea97380c117ebce4b728fb5d7062fbf5dd0ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f8d20bff3ddb1a63dd23eccf717b4126b0c43c0d340867485ba3e492a1e9210(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd920662c2f59b44347570b67735ba541f3da4a896d41210e94573049a841631(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18230b2c1716455ba257411b9ed17df6b09e0f4f56562c1073e7d0779b191aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f4dde69c273a99007828e270cd268ce36379a7f3da794fa7ad091f84ed9d56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1687695dc042c043d1de8ad77e387e1ef0dc18649f9d41d146eaa835683b90f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe7c63a7ed3bc8dc6252492b350af5c0c4d6a07f1e53bfb922a9b0127ce0325(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a83bb82e27489718fa4ec5ee3ecafcd4030200f47f97645b81399d5dea353803(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c39e24afc69e0fff9a7b906a76cfebf3725c67f9086dc423fb51fa235688fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b8faa8db4445e896d41a4f7e7772f64654403995e8f3cedcea1251d8fea7fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d53f39e9f3569248b3e2f1ccb57515ca96a2fc8ae83667973ec3fe81a793d07(
    *,
    asn: typing.Optional[jsii.Number] = None,
    peering_address: typing.Optional[builtins.str] = None,
    peer_weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babe3825631bf4b59327ebcaf9bcbff9dc543a724da1334075988db0b266c245(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__848057dde5e58b62019de30e0ff86792d20bee714fca9fe9f52dcddc715aa76a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b585ffef01ad9ffb95fc7659f2a176ca484039e6bc84e38da9c34b928bd182fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c798c205c9ea91a4f4ecab83169a77139ed877a296c9f958ad0a230efcaef4ff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0321a8a05243d062cfffa41e42f243cca2d7e284b30663597e86f64419f2eb(
    value: typing.Optional[VirtualNetworkGatewayBgpSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b980a9e34f0e3a362502ebd5733e85e6a76e57c97b4377d0ee752f91a61dbf2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    sku: builtins.str,
    type: builtins.str,
    active_active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bgp_settings: typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    default_local_network_gateway_id: typing.Optional[builtins.str] = None,
    enable_bgp: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpn_client_configuration: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpn_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b3f7a5bc97608c7dd78a1e91694c462a6fe8e3724700a121fa3caaf092dbb7(
    *,
    public_ip_address_id: builtins.str,
    subnet_id: builtins.str,
    name: typing.Optional[builtins.str] = None,
    private_ip_address_allocation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c68ad2463706a9dfad30a6b3c4cf82959f90d122a1f547e6fad0052f67ac00(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7979cbc0be5fe54b78ed75a0a02fd70092b67543a7d6d33588e7fe75e4c4f404(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a0e17dc19d9998a68e53f586d5b095c16c5e3252971d0d71f17693b44d1e36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f2765c82d3c977a4ac04f4a8f313ece5c4303dca945cc6b2a81875cd8b2145(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd7e4ff4c59827596e45890782cd4bdd39250c3dd2a3e79b7e3d9c23e265035(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6f2973a2f116c4bebbbeaecf89b051deff7b3c63f4399b17fff355f683f294(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41c97d1ddd934924c969904257223a0e6c1379fbeb5c35e662f8387c1a28a12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901ef510281837938e4deccf61573ce2d130aa8792e2c0e69e2e8dec67e19ab2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1cd4a8c99ac240479fae1cf0758326869917de0a81a2fc522f2017ba2f82b37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e46c61fc4ed7b505cab2b244b2d4f6c3865a3a6a18d43440b2ea123bebffaac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8617a68c7e8e11249c5cfd1382d62fa950722543c6d090bcef074efc8be056c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086c0a1c8a81075e9efe000e7a0221dd2a6c119f106b23de25802d96d6b7d3b3(
    value: typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f35b5cf2a39c3a7d18732851fc1ba93e4f62119e40ead06cc68882e8b307ac(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e35a52181c74774d6fe1bbc14a96b58835dbfee6c787882a8a1c9334248abb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ae108ba387fdd0b54976bcd5f12b85b3e1a3053c4ed15a2c70ee07197640b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1484529bf3700f0473cfc81f7f71d81eb7be8f1411ca7fdb2d219584b2dc61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2cb10414a5b1c1db0363c4a73b52a66bbccc960ed3d94804385f5bfa6119acd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d453f39daacd68b176d80d7923de56222e26da0d0f31bc590b59f1a0306deff2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82efe8c462e7e4034cdfe258f3a4f95194a6df68753fdf91478bed03198c2c67(
    value: typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8148af1afe4960d786a17c3f13ba5c773a170218ad0c0a34562c32f9f6972ee2(
    *,
    address_space: typing.Sequence[builtins.str],
    radius_server_address: typing.Optional[builtins.str] = None,
    radius_server_secret: typing.Optional[builtins.str] = None,
    revoked_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, typing.Dict[builtins.str, typing.Any]]]]] = None,
    root_certificate: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vpn_client_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308f31c461af1348095b83bfc678418f4c73eeb9f7f57ce34544395179d46c30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8012e10f1c1d54946febc9f0116f6c12fbe3a379ac77d4ea6bf6b22ea14db6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682f624a4a5f093c7309383b537b003fba13b607756f66b9c8007695308d96b4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7ae699ede478af666254a88cafcdc11f7b147705592154ed1e9e007122b5e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50e3a7835d612345adba00d99cb500091b3bcff4baa553949cb436cdb87a33cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a25d1a6bdaa8c15e29277412be7578c218496b11a3a251bf1589a6ee1bda1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d80c963241e5814f40ea3e9ee5493dc983a69abe4dc5a615f17192cddd8022(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee043a7b8140811c9d403decd6289a1befec9d4b61b23d40ca059069e728ec57(
    value: typing.Optional[VirtualNetworkGatewayVpnClientConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fdc4d968a577b00144d659c86b0680d75de3b4b7faf8d8db1bd9f022fd4a17e(
    *,
    name: builtins.str,
    thumbprint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea35a63d1616c0a0981aa7f578976e67ecd6b9c22f6390ad4f11d8f964efa3f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e171f91909855a3ba8030262ff531f2878079638ed4dd7dbb492366f84a453d7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618960fcb1a2055e9dcb457927a3de1c1afe2c9141259c282628a8013e4d48ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f89e96cba526858f51e464654a07f22ff43096578992b150ee72962bb0ca7179(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94eba6b540252be9840dfda8770c68f201dbc3fd3449193ed9196c08f45fe6fc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c4d9da2f42ab230de334ba35d3bdcd5bcdc8956824911e3c8592372d7b0869(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93687eaab5e8d6c0cae468cccd33f4226e06334dae569005dbb04e0d9b54cbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce82b554f7c9a3ce7bc37520d39c9121888893cb8e246e0972b443aa1e8a8dd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9875d6db659b76f8daffb1b8635098e022aa63984229e2acb03cf416a5b3813e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91345c431aa84292323ebd5724c1a2c1944e30c596c070ff768f0e532ef40427(
    value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce28fecfbea4bec750f25f5b233706f3642bb847eaf61342a3fcc0e3fb8aed03(
    *,
    name: builtins.str,
    public_cert_data: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676d1827fe0a9a9c9d8c1a92f6627a87e6aa08b14aaf10ce1f3bd7d1de3b1f46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1eba8db844aa5bcda512311a0ade4b2293950b62194dcc0b00d5edc74b6b71f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d82069c138aa54912f1e5c402683f6eee7d906ad5638d558e7948fcb50cd5deb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d4d183f4eeddead90ae85e2f214192b8c72cba376b57d8c590ad777a21b174(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9dfd90f148de97027eada6e337be2deb8060297647757d0a84e17cb85ab7655(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1205e03386b31a0e942807bd1f025d36132c2b066b075d95af0108cd726eac2a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd87863206c60c294de09f95f270afd6a17bef00921e9d073b818328d3520167(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff8282f7490d90a0648313eed299087745fa0b0c1d09517911fd4387c9d5c49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d85a5f68d1a3846e18a36f17290f5140f437c21c4fc0248b43f16a86b27e46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1673f7a0b76a17d642b2e494d6d59b1ab703a90fa25708cec814a4cc959804e5(
    value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
