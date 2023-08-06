'''
# `azurestack_lb_nat_rule`

Refer to the Terraform Registory for docs: [`azurestack_lb_nat_rule`](https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule).
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


class LbNatRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbNatRule.LbNatRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule azurestack_lb_nat_rule}.'''

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
        enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["LbNatRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule azurestack_lb_nat_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#backend_port LbNatRule#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_ip_configuration_name LbNatRule#frontend_ip_configuration_name}.
        :param frontend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_port LbNatRule#frontend_port}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#loadbalancer_id LbNatRule#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#name LbNatRule#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#protocol LbNatRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#resource_group_name LbNatRule#resource_group_name}.
        :param enable_floating_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#enable_floating_ip LbNatRule#enable_floating_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#id LbNatRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#idle_timeout_in_minutes LbNatRule#idle_timeout_in_minutes}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#timeouts LbNatRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2c3cd26affa7bdf1772f2a28e882ca52e3050fd4cda578b40dccd088ccca34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbNatRuleConfig(
            backend_port=backend_port,
            frontend_ip_configuration_name=frontend_ip_configuration_name,
            frontend_port=frontend_port,
            loadbalancer_id=loadbalancer_id,
            name=name,
            protocol=protocol,
            resource_group_name=resource_group_name,
            enable_floating_ip=enable_floating_ip,
            id=id,
            idle_timeout_in_minutes=idle_timeout_in_minutes,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#create LbNatRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#delete LbNatRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#read LbNatRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#update LbNatRule#update}.
        '''
        value = LbNatRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnableFloatingIp")
    def reset_enable_floating_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFloatingIp", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

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
    @jsii.member(jsii_name="backendIpConfigurationId")
    def backend_ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendIpConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationId")
    def frontend_ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LbNatRuleTimeoutsOutputReference":
        return typing.cast("LbNatRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    ) -> typing.Optional[typing.Union["LbNatRuleTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LbNatRuleTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f072917c41e51af856f646910a2a525ed1efcbfe1eb7a48fcf1973a4067bbb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__45d330381176d7312d499b6bf0fd02616d4ecb1d8f8ba2756f5a0ab4a997851e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFloatingIp", value)

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationName")
    def frontend_ip_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationName"))

    @frontend_ip_configuration_name.setter
    def frontend_ip_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320157707445454619b269da1e4cc8ec97d8944852b8c3ebed7f8a4197cb3f10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendIpConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPort")
    def frontend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPort"))

    @frontend_port.setter
    def frontend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945ab6f3a04c128d1a9456ff7e7a7c32e05853f1cdabf3b1e5481e4e50b98acf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPort", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed00453c9063de07f696273e3761978e4c8695a1706f2184dd65bb8fa50ee102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c42d0bd0b830ff9d78e4789d5bfc1d58880637e3cf648546061fa8d263a050)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="loadbalancerId")
    def loadbalancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadbalancerId"))

    @loadbalancer_id.setter
    def loadbalancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__251f6dd796a0817d9fdc4356d3283fa481037f8c3e2372352a9067813719f2e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadbalancerId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b693caf9170b3ac33ea32a2446d01e86a40db1b19f6bae6c593e866c800f2da5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1052b485f9b23db0147968b8170662ce578a3883b0c06003d08f19f6ae190c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da75d5608b1e4e087cbb8218c4ebb997c8a72ece41091ef6f9a9241da43575f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbNatRule.LbNatRuleConfig",
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
        "enable_floating_ip": "enableFloatingIp",
        "id": "id",
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "timeouts": "timeouts",
    },
)
class LbNatRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["LbNatRuleTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#backend_port LbNatRule#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_ip_configuration_name LbNatRule#frontend_ip_configuration_name}.
        :param frontend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_port LbNatRule#frontend_port}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#loadbalancer_id LbNatRule#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#name LbNatRule#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#protocol LbNatRule#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#resource_group_name LbNatRule#resource_group_name}.
        :param enable_floating_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#enable_floating_ip LbNatRule#enable_floating_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#id LbNatRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#idle_timeout_in_minutes LbNatRule#idle_timeout_in_minutes}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#timeouts LbNatRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = LbNatRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__976d9301ee6ebd23bde963348f9224ad2423ef6802c907320ede48f6456d1b26)
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
            check_type(argname="argument enable_floating_ip", value=enable_floating_ip, expected_type=type_hints["enable_floating_ip"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
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
        if enable_floating_ip is not None:
            self._values["enable_floating_ip"] = enable_floating_ip
        if id is not None:
            self._values["id"] = id
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#backend_port LbNatRule#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_ip_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_ip_configuration_name LbNatRule#frontend_ip_configuration_name}.'''
        result = self._values.get("frontend_ip_configuration_name")
        assert result is not None, "Required property 'frontend_ip_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frontend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#frontend_port LbNatRule#frontend_port}.'''
        result = self._values.get("frontend_port")
        assert result is not None, "Required property 'frontend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def loadbalancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#loadbalancer_id LbNatRule#loadbalancer_id}.'''
        result = self._values.get("loadbalancer_id")
        assert result is not None, "Required property 'loadbalancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#name LbNatRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#protocol LbNatRule#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#resource_group_name LbNatRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_floating_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#enable_floating_ip LbNatRule#enable_floating_ip}.'''
        result = self._values.get("enable_floating_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#id LbNatRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#idle_timeout_in_minutes LbNatRule#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LbNatRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#timeouts LbNatRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LbNatRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbNatRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbNatRule.LbNatRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LbNatRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#create LbNatRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#delete LbNatRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#read LbNatRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#update LbNatRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a35a7f78f165715d33fbd85f4c2b875d38a43da3bdebfe4109d54df79f27d4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#create LbNatRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#delete LbNatRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#read LbNatRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_rule#update LbNatRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbNatRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbNatRuleTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbNatRule.LbNatRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf6fb490bb857507bdfe82ddd97a07e0f003220da95565dac6c21f575f25adba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bdf0e6e87bf187531fd82de1ab4671592cd48fbc45a695eda57be0895ac4789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f90f27fdd37244601466bb551bef018769b9300daf17d78c2477053874e873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c2d81dce745a6500c96a2e98b7be4561da110e6cefdc1734efd0555d52c7004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54579ccde35481eb2e5bfe44f3ce20989af1d3ff3fb2b208a428b6f677783570)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbNatRuleTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbNatRuleTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbNatRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__875831b552d5b15e5314190045830305fb0969cd2899283718e5aab8c60ea76f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbNatRule",
    "LbNatRuleConfig",
    "LbNatRuleTimeouts",
    "LbNatRuleTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__fc2c3cd26affa7bdf1772f2a28e882ca52e3050fd4cda578b40dccd088ccca34(
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
    enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    timeouts: typing.Optional[typing.Union[LbNatRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__4f072917c41e51af856f646910a2a525ed1efcbfe1eb7a48fcf1973a4067bbb2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d330381176d7312d499b6bf0fd02616d4ecb1d8f8ba2756f5a0ab4a997851e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320157707445454619b269da1e4cc8ec97d8944852b8c3ebed7f8a4197cb3f10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945ab6f3a04c128d1a9456ff7e7a7c32e05853f1cdabf3b1e5481e4e50b98acf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed00453c9063de07f696273e3761978e4c8695a1706f2184dd65bb8fa50ee102(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c42d0bd0b830ff9d78e4789d5bfc1d58880637e3cf648546061fa8d263a050(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__251f6dd796a0817d9fdc4356d3283fa481037f8c3e2372352a9067813719f2e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b693caf9170b3ac33ea32a2446d01e86a40db1b19f6bae6c593e866c800f2da5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1052b485f9b23db0147968b8170662ce578a3883b0c06003d08f19f6ae190c06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da75d5608b1e4e087cbb8218c4ebb997c8a72ece41091ef6f9a9241da43575f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__976d9301ee6ebd23bde963348f9224ad2423ef6802c907320ede48f6456d1b26(
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
    enable_floating_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    timeouts: typing.Optional[typing.Union[LbNatRuleTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a35a7f78f165715d33fbd85f4c2b875d38a43da3bdebfe4109d54df79f27d4(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6fb490bb857507bdfe82ddd97a07e0f003220da95565dac6c21f575f25adba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bdf0e6e87bf187531fd82de1ab4671592cd48fbc45a695eda57be0895ac4789(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f90f27fdd37244601466bb551bef018769b9300daf17d78c2477053874e873(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2d81dce745a6500c96a2e98b7be4561da110e6cefdc1734efd0555d52c7004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54579ccde35481eb2e5bfe44f3ce20989af1d3ff3fb2b208a428b6f677783570(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__875831b552d5b15e5314190045830305fb0969cd2899283718e5aab8c60ea76f(
    value: typing.Optional[typing.Union[LbNatRuleTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
