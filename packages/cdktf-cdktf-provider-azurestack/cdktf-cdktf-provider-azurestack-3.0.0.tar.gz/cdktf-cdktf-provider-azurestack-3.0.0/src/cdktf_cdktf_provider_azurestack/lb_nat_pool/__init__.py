'''
# `azurestack_lb_nat_pool`

Refer to the Terraform Registory for docs: [`azurestack_lb_nat_pool`](https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool).
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


class LbNatPool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbNatPool.LbNatPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool azurestack_lb_nat_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        backend_port: jsii.Number,
        frontend_ip_configuration_name: builtins.str,
        frontend_port_end: jsii.Number,
        frontend_port_start: jsii.Number,
        loadbalancer_id: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LbNatPoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool azurestack_lb_nat_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#backend_port LbNatPool#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_ip_configuration_name LbNatPool#frontend_ip_configuration_name}.
        :param frontend_port_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_end LbNatPool#frontend_port_end}.
        :param frontend_port_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_start LbNatPool#frontend_port_start}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#loadbalancer_id LbNatPool#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#name LbNatPool#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#protocol LbNatPool#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#resource_group_name LbNatPool#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#id LbNatPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#timeouts LbNatPool#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71b20f4624c455fb7b01c637c66074a649e9610a1c7b1d942ac1fc9a8ac3b6a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbNatPoolConfig(
            backend_port=backend_port,
            frontend_ip_configuration_name=frontend_ip_configuration_name,
            frontend_port_end=frontend_port_end,
            frontend_port_start=frontend_port_start,
            loadbalancer_id=loadbalancer_id,
            name=name,
            protocol=protocol,
            resource_group_name=resource_group_name,
            id=id,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#create LbNatPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#delete LbNatPool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#read LbNatPool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#update LbNatPool#update}.
        '''
        value = LbNatPoolTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    def timeouts(self) -> "LbNatPoolTimeoutsOutputReference":
        return typing.cast("LbNatPoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationNameInput")
    def frontend_ip_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendIpConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortEndInput")
    def frontend_port_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frontendPortEndInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortStartInput")
    def frontend_port_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frontendPortStartInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    ) -> typing.Optional[typing.Union["LbNatPoolTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LbNatPoolTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e975068510f623d74269f2150e3b963deb3d8b56ea46a3e21a02520cea663b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

    @builtins.property
    @jsii.member(jsii_name="frontendIpConfigurationName")
    def frontend_ip_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendIpConfigurationName"))

    @frontend_ip_configuration_name.setter
    def frontend_ip_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a827b7cc692048411eaa47a3bd749bd82562e72acc66c8dcb5a3ab68bb5ef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendIpConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPortEnd")
    def frontend_port_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPortEnd"))

    @frontend_port_end.setter
    def frontend_port_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eafb2940157fbfcba3c1f7cfcef64e6d3d4a27a1fd841a8e929a817c638d9a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPortEnd", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPortStart")
    def frontend_port_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frontendPortStart"))

    @frontend_port_start.setter
    def frontend_port_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d3eff88f40cffbccd20cad55f2d58ed47f87fb703e046ae5d2ecf53a54b8fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPortStart", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01b4dd53ef26135839113e10f0ca19196fd3bd630711aad9f2774b4b0f05828)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadbalancerId")
    def loadbalancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadbalancerId"))

    @loadbalancer_id.setter
    def loadbalancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db3baff37a7e74924868f6117eabb7140ab4ae4965de87f9f9e52c6b6b66f85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadbalancerId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43beb518f79d13b789929d563eccc678ab853bb54f00efc325ef100162302d6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__661c7ece644f44ace1b8bc2bea3d8dd54eff9cce837d24fa41b54a4afe1c6470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d7f05171ebe6231c03704e639e50932ec0d54029b895ce972b94506d19c0140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbNatPool.LbNatPoolConfig",
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
        "frontend_port_end": "frontendPortEnd",
        "frontend_port_start": "frontendPortStart",
        "loadbalancer_id": "loadbalancerId",
        "name": "name",
        "protocol": "protocol",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class LbNatPoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        frontend_port_end: jsii.Number,
        frontend_port_start: jsii.Number,
        loadbalancer_id: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["LbNatPoolTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#backend_port LbNatPool#backend_port}.
        :param frontend_ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_ip_configuration_name LbNatPool#frontend_ip_configuration_name}.
        :param frontend_port_end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_end LbNatPool#frontend_port_end}.
        :param frontend_port_start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_start LbNatPool#frontend_port_start}.
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#loadbalancer_id LbNatPool#loadbalancer_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#name LbNatPool#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#protocol LbNatPool#protocol}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#resource_group_name LbNatPool#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#id LbNatPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#timeouts LbNatPool#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = LbNatPoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e7086d264a2e0b0eb2895fe0a632f6465b71065e26888f18871f784e8510b5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend_port", value=backend_port, expected_type=type_hints["backend_port"])
            check_type(argname="argument frontend_ip_configuration_name", value=frontend_ip_configuration_name, expected_type=type_hints["frontend_ip_configuration_name"])
            check_type(argname="argument frontend_port_end", value=frontend_port_end, expected_type=type_hints["frontend_port_end"])
            check_type(argname="argument frontend_port_start", value=frontend_port_start, expected_type=type_hints["frontend_port_start"])
            check_type(argname="argument loadbalancer_id", value=loadbalancer_id, expected_type=type_hints["loadbalancer_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backend_port": backend_port,
            "frontend_ip_configuration_name": frontend_ip_configuration_name,
            "frontend_port_end": frontend_port_end,
            "frontend_port_start": frontend_port_start,
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
        if id is not None:
            self._values["id"] = id
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#backend_port LbNatPool#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_ip_configuration_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_ip_configuration_name LbNatPool#frontend_ip_configuration_name}.'''
        result = self._values.get("frontend_ip_configuration_name")
        assert result is not None, "Required property 'frontend_ip_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frontend_port_end(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_end LbNatPool#frontend_port_end}.'''
        result = self._values.get("frontend_port_end")
        assert result is not None, "Required property 'frontend_port_end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_port_start(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#frontend_port_start LbNatPool#frontend_port_start}.'''
        result = self._values.get("frontend_port_start")
        assert result is not None, "Required property 'frontend_port_start' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def loadbalancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#loadbalancer_id LbNatPool#loadbalancer_id}.'''
        result = self._values.get("loadbalancer_id")
        assert result is not None, "Required property 'loadbalancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#name LbNatPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#protocol LbNatPool#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#resource_group_name LbNatPool#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#id LbNatPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LbNatPoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#timeouts LbNatPool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LbNatPoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbNatPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.lbNatPool.LbNatPoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LbNatPoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#create LbNatPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#delete LbNatPool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#read LbNatPool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#update LbNatPool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3014d481a5ed4f91d81a443d485845fc0886a2d9adb109660030dac3536e5bfa)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#create LbNatPool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#delete LbNatPool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#read LbNatPool#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/lb_nat_pool#update LbNatPool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbNatPoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbNatPoolTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.lbNatPool.LbNatPoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe97ed5326621e4db4f4de178f5f6082a8c5b849421da5f35e869aac1f1d48d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aedc1bca179879fc314609f5536ea5ebf6228cba7a23ebcbd70e6490f57b464c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a32627253f2aa8d8e8ae111eadedea8409f7e50c3d319b38295cc9b274ffccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b1e18c61d89a4de63624638eda78b6c5b1c572fa97605ee17bf6a9fb4c3a2d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03444b2a19822d763851d936422b6c6a73536c23adccca00a0c8a81e5e68d729)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LbNatPoolTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LbNatPoolTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LbNatPoolTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904dcbf17e3cec6eb7d0ca7c39a70f0ab3cc6118ffe17ccec3fb4907098e736b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbNatPool",
    "LbNatPoolConfig",
    "LbNatPoolTimeouts",
    "LbNatPoolTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__f71b20f4624c455fb7b01c637c66074a649e9610a1c7b1d942ac1fc9a8ac3b6a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    backend_port: jsii.Number,
    frontend_ip_configuration_name: builtins.str,
    frontend_port_end: jsii.Number,
    frontend_port_start: jsii.Number,
    loadbalancer_id: builtins.str,
    name: builtins.str,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LbNatPoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__e975068510f623d74269f2150e3b963deb3d8b56ea46a3e21a02520cea663b4f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a827b7cc692048411eaa47a3bd749bd82562e72acc66c8dcb5a3ab68bb5ef7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eafb2940157fbfcba3c1f7cfcef64e6d3d4a27a1fd841a8e929a817c638d9a6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d3eff88f40cffbccd20cad55f2d58ed47f87fb703e046ae5d2ecf53a54b8fde(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01b4dd53ef26135839113e10f0ca19196fd3bd630711aad9f2774b4b0f05828(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1db3baff37a7e74924868f6117eabb7140ab4ae4965de87f9f9e52c6b6b66f85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43beb518f79d13b789929d563eccc678ab853bb54f00efc325ef100162302d6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__661c7ece644f44ace1b8bc2bea3d8dd54eff9cce837d24fa41b54a4afe1c6470(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d7f05171ebe6231c03704e639e50932ec0d54029b895ce972b94506d19c0140(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e7086d264a2e0b0eb2895fe0a632f6465b71065e26888f18871f784e8510b5(
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
    frontend_port_end: jsii.Number,
    frontend_port_start: jsii.Number,
    loadbalancer_id: builtins.str,
    name: builtins.str,
    protocol: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[LbNatPoolTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3014d481a5ed4f91d81a443d485845fc0886a2d9adb109660030dac3536e5bfa(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe97ed5326621e4db4f4de178f5f6082a8c5b849421da5f35e869aac1f1d48d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aedc1bca179879fc314609f5536ea5ebf6228cba7a23ebcbd70e6490f57b464c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a32627253f2aa8d8e8ae111eadedea8409f7e50c3d319b38295cc9b274ffccb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b1e18c61d89a4de63624638eda78b6c5b1c572fa97605ee17bf6a9fb4c3a2d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03444b2a19822d763851d936422b6c6a73536c23adccca00a0c8a81e5e68d729(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904dcbf17e3cec6eb7d0ca7c39a70f0ab3cc6118ffe17ccec3fb4907098e736b(
    value: typing.Optional[typing.Union[LbNatPoolTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
