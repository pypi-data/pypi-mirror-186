'''
# `data_azurestack_public_ips`

Refer to the Terraform Registory for docs: [`data_azurestack_public_ips`](https://www.terraform.io/docs/providers/azurestack/d/public_ips).
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


class DataAzurestackPublicIps(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIps",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips azurestack_public_ips}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        resource_group_name: builtins.str,
        allocation_type: typing.Optional[builtins.str] = None,
        attached: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        attachment_status: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAzurestackPublicIpsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips azurestack_public_ips} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#resource_group_name DataAzurestackPublicIps#resource_group_name}.
        :param allocation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#allocation_type DataAzurestackPublicIps#allocation_type}.
        :param attached: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attached DataAzurestackPublicIps#attached}.
        :param attachment_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attachment_status DataAzurestackPublicIps#attachment_status}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#id DataAzurestackPublicIps#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#name_prefix DataAzurestackPublicIps#name_prefix}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#timeouts DataAzurestackPublicIps#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d43a9bb5412eef2179b834b70958061371139983bc99ff745fb95c087e37b75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAzurestackPublicIpsConfig(
            resource_group_name=resource_group_name,
            allocation_type=allocation_type,
            attached=attached,
            attachment_status=attachment_status,
            id=id,
            name_prefix=name_prefix,
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
    def put_timeouts(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#read DataAzurestackPublicIps#read}.
        '''
        value = DataAzurestackPublicIpsTimeouts(read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllocationType")
    def reset_allocation_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocationType", []))

    @jsii.member(jsii_name="resetAttached")
    def reset_attached(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttached", []))

    @jsii.member(jsii_name="resetAttachmentStatus")
    def reset_attachment_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachmentStatus", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

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
    @jsii.member(jsii_name="publicIps")
    def public_ips(self) -> "DataAzurestackPublicIpsPublicIpsList":
        return typing.cast("DataAzurestackPublicIpsPublicIpsList", jsii.get(self, "publicIps"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataAzurestackPublicIpsTimeoutsOutputReference":
        return typing.cast("DataAzurestackPublicIpsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allocationTypeInput")
    def allocation_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="attachedInput")
    def attached_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "attachedInput"))

    @builtins.property
    @jsii.member(jsii_name="attachmentStatusInput")
    def attachment_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attachmentStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataAzurestackPublicIpsTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataAzurestackPublicIpsTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationType")
    def allocation_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationType"))

    @allocation_type.setter
    def allocation_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6a0afd8889f8c648e346ff7291a91d513bc4f4edb2d07c40226bb7eb106e4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationType", value)

    @builtins.property
    @jsii.member(jsii_name="attached")
    def attached(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "attached"))

    @attached.setter
    def attached(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90bf841bdffe6c204328253e73d85a045e141e34648938edfdcf15c1467b0a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attached", value)

    @builtins.property
    @jsii.member(jsii_name="attachmentStatus")
    def attachment_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attachmentStatus"))

    @attachment_status.setter
    def attachment_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b1ffcbf31e3fbb599280011abce88d461b9e1abbd1f385d6f155d377089c706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentStatus", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed8d7ac8a1ef261fa6976d31be6d2f616f395776b73652d700a46aa3ac7cbbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa4911b6d62a0131bcba56d8e2bba2ea72cc45c37168850ff61bf153a1f954c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ae7694f6fa6d787c12900ffe8aa2e52ae383d375d60e39f4d322ac1e7d322f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "resource_group_name": "resourceGroupName",
        "allocation_type": "allocationType",
        "attached": "attached",
        "attachment_status": "attachmentStatus",
        "id": "id",
        "name_prefix": "namePrefix",
        "timeouts": "timeouts",
    },
)
class DataAzurestackPublicIpsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        allocation_type: typing.Optional[builtins.str] = None,
        attached: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        attachment_status: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataAzurestackPublicIpsTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#resource_group_name DataAzurestackPublicIps#resource_group_name}.
        :param allocation_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#allocation_type DataAzurestackPublicIps#allocation_type}.
        :param attached: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attached DataAzurestackPublicIps#attached}.
        :param attachment_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attachment_status DataAzurestackPublicIps#attachment_status}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#id DataAzurestackPublicIps#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#name_prefix DataAzurestackPublicIps#name_prefix}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#timeouts DataAzurestackPublicIps#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataAzurestackPublicIpsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4af504f594e7b73cb00855602ec29852db656b91ae131c684ed4c852b1c229)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument allocation_type", value=allocation_type, expected_type=type_hints["allocation_type"])
            check_type(argname="argument attached", value=attached, expected_type=type_hints["attached"])
            check_type(argname="argument attachment_status", value=attachment_status, expected_type=type_hints["attachment_status"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if allocation_type is not None:
            self._values["allocation_type"] = allocation_type
        if attached is not None:
            self._values["attached"] = attached
        if attachment_status is not None:
            self._values["attachment_status"] = attachment_status
        if id is not None:
            self._values["id"] = id
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
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
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#resource_group_name DataAzurestackPublicIps#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#allocation_type DataAzurestackPublicIps#allocation_type}.'''
        result = self._values.get("allocation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attached(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attached DataAzurestackPublicIps#attached}.'''
        result = self._values.get("attached")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def attachment_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#attachment_status DataAzurestackPublicIps#attachment_status}.'''
        result = self._values.get("attachment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#id DataAzurestackPublicIps#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#name_prefix DataAzurestackPublicIps#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataAzurestackPublicIpsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#timeouts DataAzurestackPublicIps#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataAzurestackPublicIpsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurestackPublicIpsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsPublicIps",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAzurestackPublicIpsPublicIps:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurestackPublicIpsPublicIps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurestackPublicIpsPublicIpsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsPublicIpsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8974b62ead706047e39f2f2b4c30ac756338bbe5e19b8f418bd127e4415eea73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAzurestackPublicIpsPublicIpsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10272c3b9357faaab4e505901630aab06535641cdd259ab2fe82a16f70fa7711)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAzurestackPublicIpsPublicIpsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b009522aa6df710c15f04b18b84cc1cab73061a1932dad4458399be8e7d5e75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9992a0dc689803d9d04841b88a5dc04e6946e4bfc04d33bf5a3733d20142713)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1895fd5c20a8b6b2cbeac1fceeb0f3b510d1df991840ea0398066932654f5cee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAzurestackPublicIpsPublicIpsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsPublicIpsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7543e0816ba9f0bcf8477d4323334ec0db0412b369b6a775a82e928d14d8266)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="domainNameLabel")
    def domain_name_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainNameLabel"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAzurestackPublicIpsPublicIps]:
        return typing.cast(typing.Optional[DataAzurestackPublicIpsPublicIps], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAzurestackPublicIpsPublicIps],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6452234b689707fe2a19dfa58709a75185b2eb55ee41029daea802281e634a9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"read": "read"},
)
class DataAzurestackPublicIpsTimeouts:
    def __init__(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#read DataAzurestackPublicIps#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3c4da99590edef12c1a69e2ef5a5c6c2b680ad608dc1adccf5225b079d62c3)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/d/public_ips#read DataAzurestackPublicIps#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzurestackPublicIpsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzurestackPublicIpsTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dataAzurestackPublicIps.DataAzurestackPublicIpsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__181a318e0e5700f5a2a3bdc6f0162525f8203bd88b1e18d398a0b66e8788238a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a0e7be92a1cb87489e7ef84d3f0a09d303a7e2fbb6825ad05be3f3c409867cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0918701aea38b9275153ea040b16852d31a3a831d80b34599955b20219fa6ed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAzurestackPublicIps",
    "DataAzurestackPublicIpsConfig",
    "DataAzurestackPublicIpsPublicIps",
    "DataAzurestackPublicIpsPublicIpsList",
    "DataAzurestackPublicIpsPublicIpsOutputReference",
    "DataAzurestackPublicIpsTimeouts",
    "DataAzurestackPublicIpsTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__3d43a9bb5412eef2179b834b70958061371139983bc99ff745fb95c087e37b75(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    resource_group_name: builtins.str,
    allocation_type: typing.Optional[builtins.str] = None,
    attached: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    attachment_status: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9c6a0afd8889f8c648e346ff7291a91d513bc4f4edb2d07c40226bb7eb106e4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90bf841bdffe6c204328253e73d85a045e141e34648938edfdcf15c1467b0a8a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b1ffcbf31e3fbb599280011abce88d461b9e1abbd1f385d6f155d377089c706(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed8d7ac8a1ef261fa6976d31be6d2f616f395776b73652d700a46aa3ac7cbbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4911b6d62a0131bcba56d8e2bba2ea72cc45c37168850ff61bf153a1f954c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ae7694f6fa6d787c12900ffe8aa2e52ae383d375d60e39f4d322ac1e7d322f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4af504f594e7b73cb00855602ec29852db656b91ae131c684ed4c852b1c229(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    resource_group_name: builtins.str,
    allocation_type: typing.Optional[builtins.str] = None,
    attached: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    attachment_status: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8974b62ead706047e39f2f2b4c30ac756338bbe5e19b8f418bd127e4415eea73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10272c3b9357faaab4e505901630aab06535641cdd259ab2fe82a16f70fa7711(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b009522aa6df710c15f04b18b84cc1cab73061a1932dad4458399be8e7d5e75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9992a0dc689803d9d04841b88a5dc04e6946e4bfc04d33bf5a3733d20142713(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1895fd5c20a8b6b2cbeac1fceeb0f3b510d1df991840ea0398066932654f5cee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7543e0816ba9f0bcf8477d4323334ec0db0412b369b6a775a82e928d14d8266(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6452234b689707fe2a19dfa58709a75185b2eb55ee41029daea802281e634a9e(
    value: typing.Optional[DataAzurestackPublicIpsPublicIps],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3c4da99590edef12c1a69e2ef5a5c6c2b680ad608dc1adccf5225b079d62c3(
    *,
    read: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181a318e0e5700f5a2a3bdc6f0162525f8203bd88b1e18d398a0b66e8788238a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0e7be92a1cb87489e7ef84d3f0a09d303a7e2fbb6825ad05be3f3c409867cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0918701aea38b9275153ea040b16852d31a3a831d80b34599955b20219fa6ed9(
    value: typing.Optional[typing.Union[DataAzurestackPublicIpsTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
