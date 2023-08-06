'''
# `azurestack_lb_rule`

Refer to the Terraform Registory for docs: [`azurestack_lb_rule`](https://www.terraform.io/docs/providers/azurestack/r/lb_rule).
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


class LbRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbRule.LbRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule azurestack_lb_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        backend_port: jsii.Number,
        frontend_ip_configuration_name: builtins.str,
        frontend_port: jsii.Number,
        loadbalancer_id: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        backend_address_pool_id: typing.Optional[builtins.str] = None,
        disable_outbound_snat: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        load_distribution: typing.Optional[builtins.str] = None,
        probe_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LbRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule azurestack_lb_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_port LbRule#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_ip_configuration_name LbRule#frontend_ip_configuration_name}.
        :param frontend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_port LbRule#frontend_port}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#loadbalancer_id LbRule#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#name LbRule#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#protocol LbRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#resource_group_name LbRule#resource_group_name}.
        :param backend_address_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_address_pool_id LbRule#backend_address_pool_id}.
        :param disable_outbound_snat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#disable_outbound_snat LbRule#disable_outbound_snat}.
        :param enable_floating_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#enable_floating_ip LbRule#enable_floating_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#id LbRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#idle_timeout_in_minutes LbRule#idle_timeout_in_minutes}.
        :param load_distribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#load_distribution LbRule#load_distribution}.
        :param probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#probe_id LbRule#probe_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#timeouts LbRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c2557cfff3007178931e509dfbe1f7d39fc72f8fd9db17d50d6dd110f3f269)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbRuleConfig(
            backend_port=backend_port,
            frontend_ip_configuration_name=frontend_ip_configuration_name,
            frontend_port=frontend_port,
            loadbalancer_id=loadbalancer_id,
            name=name,
            protocol=protocol,
            resource_group_name=resource_group_name,
            backend_address_pool_id=backend_address_pool_id,
            disable_outbound_snat=disable_outbound_snat,
            enable_floating_ip=enable_floating_ip,
            id=id,
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            load_distribution=load_distribution,
            probe_id=probe_id,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#create LbRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#delete LbRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#read LbRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#update LbRule#update}.
        '''
        value = LbRuleTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackendAddressPoolId")
    def reset_backend_address_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendAddressPoolId", []))

    @jsii.member(jsii_name="resetDisableOutboundSnat")
    def reset_disable_outbound_snat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableOutboundSnat", []))

    @jsii.member(jsii_name="resetEnableFloatingIp")
    def reset_enable_floating_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFloatingIp", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetLoadDistribution")
    def reset_load_distribution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadDistribution", []))

    @jsii.member(jsii_name="resetProbeId")
    def reset_probe_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbeId", []))

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
    @jsii.member(jsii_name="frontendIpConfigurationId")
    def frontend_ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LbRuleTimeoutsOutputReference":
        return typing.cast("LbRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolIdInput")
    def backend_address_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendAddressPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="disableOutboundSnatInput")
    def disable_outbound_snat_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableOutboundSnatInput"))

    @builtins.property
    @jsii.member(jsii_name="enableFloatingIpInput")
    def enable_floating_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableFloatingIpInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationNameInput")
    def frontend_ip_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendIpConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortInput")
    def frontend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frontendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="loadbalancerIdInput")
    def loadbalancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadbalancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="loadDistributionInput")
    def load_distribution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadDistributionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="probeIdInput")
    def probe_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LbRuleTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LbRuleTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendAddressPoolId")
    def backend_address_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendAddressPoolId"))

    @backend_address_pool_id.setter
    def backend_address_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c159873757ace5577ab6ab977f3e222d668ce73eeaa27866314f3f796b79ee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendAddressPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd55e3cf937f6b9c39c8314de4472524027f6465b38c4784249be310910f574)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

    @builtins.property
    @jsii.member(jsii_name="disableOutboundSnat")
    def disable_outbound_snat(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableOutboundSnat"))

    @disable_outbound_snat.setter
    def disable_outbound_snat(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa56bbfeca6c5a8162155f283b4c74b7012e567f3856ff3d816eeb69ae47870e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableOutboundSnat", value)

    @builtins.property
    @jsii.member(jsii_name="enableFloatingIp")
    def enable_floating_ip(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableFloatingIp"))

    @enable_floating_ip.setter
    def enable_floating_ip(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__701f71327ade7971c193de713adb047dae372155f0d37687996deb1fcccc4e17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFloatingIp", value)

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationName")
    def frontend_ip_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationName"))

    @frontend_ip_configuration_name.setter
    def frontend_ip_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__210a2838ad2456f1bad1cde9392da7267c8acd3374b55f3828e6c691441b7025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendIpConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPort")
    def frontend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPort"))

    @frontend_port.setter
    def frontend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88887d38f7ad5c609575462e765cef394205d7213ab72dddaa01f587f7ca08da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPort", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c558b6d081cbe78cb61f47d141e994a46cfb9bcf051615f60bb7fb90d349a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9473d4710aeac6107081be31c200ac88249b10a7c9f9adcd820a8b9eca3af350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="loadbalancerId")
    def loadbalancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadbalancerId"))

    @loadbalancer_id.setter
    def loadbalancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8000b30eb0afde676d887318644efa032e0b979558948a7050c9eeb4637e5b0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadbalancerId", value)

    @builtins.property
    @jsii.member(jsii_name="loadDistribution")
    def load_distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadDistribution"))

    @load_distribution.setter
    def load_distribution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54fb6e088d5f2764108974c9554e718c9d78a5f7240194bf551f55a8fc31df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadDistribution", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3604229c7083d8d998c43abf76bb1e485f58128923d11b6a825f2dce74bcb9cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="probeId")
    def probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeId"))

    @probe_id.setter
    def probe_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20ef3a554123ce554db3ca8f4617a98ae6b3e5ce1f0e8b17273f493112b9858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probeId", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b75ee3c95a3ef424a613ef667c45e0791d177154be9fc392a172802ac388372f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256ffefc9f0b87ec9dcaa38326cf8a71c637a729b886751700acfd5bc6eeb8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbRule.LbRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend_port": "backendPort",
        "frontend_ip_configuration_name": "frontendIpConfigurationName",
        "frontend_port": "frontendPort",
        "loadbalancer_id": "loadbalancerId",
        "name": "name",
        "protocol": "protocol",
        "resource_group_name": "resourceGroupName",
        "backend_address_pool_id": "backendAddressPoolId",
        "disable_outbound_snat": "disableOutboundSnat",
        "enable_floating_ip": "enableFloatingIp",
        "id": "id",
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "load_distribution": "loadDistribution",
        "probe_id": "probeId",
        "timeouts": "timeouts",
    },
)
class LbRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        backend_port: jsii.Number,
        frontend_ip_configuration_name: builtins.str,
        frontend_port: jsii.Number,
        loadbalancer_id: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        backend_address_pool_id: typing.Optional[builtins.str] = None,
        disable_outbound_snat: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        load_distribution: typing.Optional[builtins.str] = None,
        probe_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LbRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_port LbRule#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_ip_configuration_name LbRule#frontend_ip_configuration_name}.
        :param frontend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_port LbRule#frontend_port}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#loadbalancer_id LbRule#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#name LbRule#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#protocol LbRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#resource_group_name LbRule#resource_group_name}.
        :param backend_address_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_address_pool_id LbRule#backend_address_pool_id}.
        :param disable_outbound_snat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#disable_outbound_snat LbRule#disable_outbound_snat}.
        :param enable_floating_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#enable_floating_ip LbRule#enable_floating_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#id LbRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#idle_timeout_in_minutes LbRule#idle_timeout_in_minutes}.
        :param load_distribution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#load_distribution LbRule#load_distribution}.
        :param probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#probe_id LbRule#probe_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#timeouts LbRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = LbRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d2ca5d708e2f10f7aac13824ed472edbcb4ff3d10b211f043305b9740228590)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend_port", value=backend_port, expected_type=type_hints["backend_port"])
            check_type(argname="argument frontend_ip_configuration_name", value=frontend_ip_configuration_name, expected_type=type_hints["frontend_ip_configuration_name"])
            check_type(argname="argument frontend_port", value=frontend_port, expected_type=type_hints["frontend_port"])
            check_type(argname="argument loadbalancer_id", value=loadbalancer_id, expected_type=type_hints["loadbalancer_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument backend_address_pool_id", value=backend_address_pool_id, expected_type=type_hints["backend_address_pool_id"])
            check_type(argname="argument disable_outbound_snat", value=disable_outbound_snat, expected_type=type_hints["disable_outbound_snat"])
            check_type(argname="argument enable_floating_ip", value=enable_floating_ip, expected_type=type_hints["enable_floating_ip"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument load_distribution", value=load_distribution, expected_type=type_hints["load_distribution"])
            check_type(argname="argument probe_id", value=probe_id, expected_type=type_hints["probe_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backend_port": backend_port,
            "frontend_ip_configuration_name": frontend_ip_configuration_name,
            "frontend_port": frontend_port,
            "loadbalancer_id": loadbalancer_id,
            "name": name,
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
        if backend_address_pool_id is not None:
            self._values["backend_address_pool_id"] = backend_address_pool_id
        if disable_outbound_snat is not None:
            self._values["disable_outbound_snat"] = disable_outbound_snat
        if enable_floating_ip is not None:
            self._values["enable_floating_ip"] = enable_floating_ip
        if id is not None:
            self._values["id"] = id
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if load_distribution is not None:
            self._values["load_distribution"] = load_distribution
        if probe_id is not None:
            self._values["probe_id"] = probe_id
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
    def backend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_port LbRule#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_ip_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_ip_configuration_name LbRule#frontend_ip_configuration_name}.'''
        result = self._values.get("frontend_ip_configuration_name")
        assert result is not None, "Required property 'frontend_ip_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frontend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#frontend_port LbRule#frontend_port}.'''
        result = self._values.get("frontend_port")
        assert result is not None, "Required property 'frontend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def loadbalancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#loadbalancer_id LbRule#loadbalancer_id}.'''
        result = self._values.get("loadbalancer_id")
        assert result is not None, "Required property 'loadbalancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#name LbRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#protocol LbRule#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#resource_group_name LbRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend_address_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#backend_address_pool_id LbRule#backend_address_pool_id}.'''
        result = self._values.get("backend_address_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_outbound_snat(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#disable_outbound_snat LbRule#disable_outbound_snat}.'''
        result = self._values.get("disable_outbound_snat")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_floating_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#enable_floating_ip LbRule#enable_floating_ip}.'''
        result = self._values.get("enable_floating_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#id LbRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#idle_timeout_in_minutes LbRule#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def load_distribution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#load_distribution LbRule#load_distribution}.'''
        result = self._values.get("load_distribution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probe_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#probe_id LbRule#probe_id}.'''
        result = self._values.get("probe_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LbRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#timeouts LbRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LbRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbRule.LbRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LbRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#create LbRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#delete LbRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#read LbRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#update LbRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37997c987c560329784be747e8d65a92666013395fc24f389f01d9600597b95)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#create LbRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#delete LbRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#read LbRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_rule#update LbRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbRuleTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbRule.LbRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb1674eb8f49cee569a354040e0c91b75ff18e7353812390f002bd641060701c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d00f6522061d35954ab02eb8afcc6e9341bab2bb07bd813f8f5dffc3328ffca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6600005198e998ce29fb4c7845070f51bde6ce73f3f2e2cd6fbf212b9c357971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bb820ffc98420419a3981fc6757443bc76254fb8d5566479e2c9ba56350202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e62d3d4a85db0c54bbcc28e8affc9dc1249826b8ff12b6170f8f5383b2331a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbRuleTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbRuleTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e8828d22b86104dc6a6b7817a52e6b96fc5d1c32e0fd2ef7901bc7a91413f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbRule",
    "LbRuleConfig",
    "LbRuleTimeouts",
    "LbRuleTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__20c2557cfff3007178931e509dfbe1f7d39fc72f8fd9db17d50d6dd110f3f269(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    backend_port: jsii.Number,
    frontend_ip_configuration_name: builtins.str,
    frontend_port: jsii.Number,
    loadbalancer_id: builtins.str,
    name: builtins.str,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    backend_address_pool_id: typing.Optional[builtins.str] = None,
    disable_outbound_snat: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    load_distribution: typing.Optional[builtins.str] = None,
    probe_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LbRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__6c159873757ace5577ab6ab977f3e222d668ce73eeaa27866314f3f796b79ee7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd55e3cf937f6b9c39c8314de4472524027f6465b38c4784249be310910f574(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa56bbfeca6c5a8162155f283b4c74b7012e567f3856ff3d816eeb69ae47870e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__701f71327ade7971c193de713adb047dae372155f0d37687996deb1fcccc4e17(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__210a2838ad2456f1bad1cde9392da7267c8acd3374b55f3828e6c691441b7025(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88887d38f7ad5c609575462e765cef394205d7213ab72dddaa01f587f7ca08da(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c558b6d081cbe78cb61f47d141e994a46cfb9bcf051615f60bb7fb90d349a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9473d4710aeac6107081be31c200ac88249b10a7c9f9adcd820a8b9eca3af350(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8000b30eb0afde676d887318644efa032e0b979558948a7050c9eeb4637e5b0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54fb6e088d5f2764108974c9554e718c9d78a5f7240194bf551f55a8fc31df5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3604229c7083d8d998c43abf76bb1e485f58128923d11b6a825f2dce74bcb9cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20ef3a554123ce554db3ca8f4617a98ae6b3e5ce1f0e8b17273f493112b9858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b75ee3c95a3ef424a613ef667c45e0791d177154be9fc392a172802ac388372f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256ffefc9f0b87ec9dcaa38326cf8a71c637a729b886751700acfd5bc6eeb8f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d2ca5d708e2f10f7aac13824ed472edbcb4ff3d10b211f043305b9740228590(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backend_port: jsii.Number,
    frontend_ip_configuration_name: builtins.str,
    frontend_port: jsii.Number,
    loadbalancer_id: builtins.str,
    name: builtins.str,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    backend_address_pool_id: typing.Optional[builtins.str] = None,
    disable_outbound_snat: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    load_distribution: typing.Optional[builtins.str] = None,
    probe_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LbRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b37997c987c560329784be747e8d65a92666013395fc24f389f01d9600597b95(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1674eb8f49cee569a354040e0c91b75ff18e7353812390f002bd641060701c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d00f6522061d35954ab02eb8afcc6e9341bab2bb07bd813f8f5dffc3328ffca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6600005198e998ce29fb4c7845070f51bde6ce73f3f2e2cd6fbf212b9c357971(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bb820ffc98420419a3981fc6757443bc76254fb8d5566479e2c9ba56350202(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e62d3d4a85db0c54bbcc28e8affc9dc1249826b8ff12b6170f8f5383b2331a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e8828d22b86104dc6a6b7817a52e6b96fc5d1c32e0fd2ef7901bc7a91413f8(
    value: typing.Optional[typing.Union[LbRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
