'''
# `azurestack_virtual_machine_scale_set_extension`

Refer to the Terraform Registory for docs: [`azurestack_virtual_machine_scale_set_extension`](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension).
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


class VirtualMachineScaleSetExtensionA(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachineScaleSetExtension.VirtualMachineScaleSetExtensionA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension azurestack_virtual_machine_scale_set_extension}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        virtual_machine_scale_set_id: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_update_tag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        settings: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineScaleSetExtensionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension azurestack_virtual_machine_scale_set_extension} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#name VirtualMachineScaleSetExtensionA#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#publisher VirtualMachineScaleSetExtensionA#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type VirtualMachineScaleSetExtensionA#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type_handler_version VirtualMachineScaleSetExtensionA#type_handler_version}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#virtual_machine_scale_set_id VirtualMachineScaleSetExtensionA#virtual_machine_scale_set_id}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#auto_upgrade_minor_version VirtualMachineScaleSetExtensionA#auto_upgrade_minor_version}.
        :param force_update_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#force_update_tag VirtualMachineScaleSetExtensionA#force_update_tag}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#id VirtualMachineScaleSetExtensionA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#protected_settings VirtualMachineScaleSetExtensionA#protected_settings}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#settings VirtualMachineScaleSetExtensionA#settings}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#timeouts VirtualMachineScaleSetExtensionA#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f01228ace1fb4ce695994c2d35d762c0ff398b3eb2982f783f3202fe6c8208)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualMachineScaleSetExtensionAConfig(
            name=name,
            publisher=publisher,
            type=type,
            type_handler_version=type_handler_version,
            virtual_machine_scale_set_id=virtual_machine_scale_set_id,
            auto_upgrade_minor_version=auto_upgrade_minor_version,
            force_update_tag=force_update_tag,
            id=id,
            protected_settings=protected_settings,
            settings=settings,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#create VirtualMachineScaleSetExtensionA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#delete VirtualMachineScaleSetExtensionA#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#read VirtualMachineScaleSetExtensionA#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#update VirtualMachineScaleSetExtensionA#update}.
        '''
        value = VirtualMachineScaleSetExtensionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetForceUpdateTag")
    def reset_force_update_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceUpdateTag", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProtectedSettings")
    def reset_protected_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedSettings", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

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
    def timeouts(self) -> "VirtualMachineScaleSetExtensionTimeoutsOutputReference":
        return typing.cast("VirtualMachineScaleSetExtensionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersionInput")
    def auto_upgrade_minor_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoUpgradeMinorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTagInput")
    def force_update_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forceUpdateTagInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedSettingsInput")
    def protected_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualMachineScaleSetExtensionTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualMachineScaleSetExtensionTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersionInput")
    def type_handler_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeHandlerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetIdInput")
    def virtual_machine_scale_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineScaleSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoUpgradeMinorVersion"))

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341a006b38f52bd5c2b7a65ba87c69f7a1a196754f8f96c882a6149c8bf3b40e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTag")
    def force_update_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceUpdateTag"))

    @force_update_tag.setter
    def force_update_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac77c4fcbddf1deee748c6a83c52d0ffc636f28a4b12caf5c902e0ace7172806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdateTag", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bc1168387b7630c4e88247f389fc739e5dac014f07c8e8d182ba34bff3d9e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5fcab293f30782f32dca1e16e8c6af26b23a94060d1685523621296d8dfe8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1121a70d8d3c0e34fd0a986029b182ea0806ada4764a9d3b1ff4b9b76670c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0598f7d527b47c2ef87c6c7896c48f8f320ba550da9bccbe3fce9f78cc16953c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fc4e04ab1aa684e0a381d9ad831e1592b64cbfc56fa45bf5ae0edb8c5741387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae2510fc4038be133659339022c8718e78e21eec6fcd47749f7c8651ab9cc4be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45bb3299cc986d80a8e66a73efe48a30e68948b8fb53f83d2bb5e9dc045dfdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetId")
    def virtual_machine_scale_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineScaleSetId"))

    @virtual_machine_scale_set_id.setter
    def virtual_machine_scale_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01862fe60064d71bce49980e9089a43c5639b98db1ca7aa345a89711cd7768a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineScaleSetId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachineScaleSetExtension.VirtualMachineScaleSetExtensionAConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "publisher": "publisher",
        "type": "type",
        "type_handler_version": "typeHandlerVersion",
        "virtual_machine_scale_set_id": "virtualMachineScaleSetId",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "force_update_tag": "forceUpdateTag",
        "id": "id",
        "protected_settings": "protectedSettings",
        "settings": "settings",
        "timeouts": "timeouts",
    },
)
class VirtualMachineScaleSetExtensionAConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        virtual_machine_scale_set_id: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_update_tag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        settings: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineScaleSetExtensionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#name VirtualMachineScaleSetExtensionA#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#publisher VirtualMachineScaleSetExtensionA#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type VirtualMachineScaleSetExtensionA#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type_handler_version VirtualMachineScaleSetExtensionA#type_handler_version}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#virtual_machine_scale_set_id VirtualMachineScaleSetExtensionA#virtual_machine_scale_set_id}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#auto_upgrade_minor_version VirtualMachineScaleSetExtensionA#auto_upgrade_minor_version}.
        :param force_update_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#force_update_tag VirtualMachineScaleSetExtensionA#force_update_tag}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#id VirtualMachineScaleSetExtensionA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#protected_settings VirtualMachineScaleSetExtensionA#protected_settings}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#settings VirtualMachineScaleSetExtensionA#settings}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#timeouts VirtualMachineScaleSetExtensionA#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = VirtualMachineScaleSetExtensionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b9eeb26fdedd192a34888cea7e46e0bf168d070c2c78b5680a512c0daa37b5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_handler_version", value=type_handler_version, expected_type=type_hints["type_handler_version"])
            check_type(argname="argument virtual_machine_scale_set_id", value=virtual_machine_scale_set_id, expected_type=type_hints["virtual_machine_scale_set_id"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument force_update_tag", value=force_update_tag, expected_type=type_hints["force_update_tag"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
            "type_handler_version": type_handler_version,
            "virtual_machine_scale_set_id": virtual_machine_scale_set_id,
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
        if auto_upgrade_minor_version is not None:
            self._values["auto_upgrade_minor_version"] = auto_upgrade_minor_version
        if force_update_tag is not None:
            self._values["force_update_tag"] = force_update_tag
        if id is not None:
            self._values["id"] = id
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if settings is not None:
            self._values["settings"] = settings
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#name VirtualMachineScaleSetExtensionA#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#publisher VirtualMachineScaleSetExtensionA#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type VirtualMachineScaleSetExtensionA#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#type_handler_version VirtualMachineScaleSetExtensionA#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_scale_set_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#virtual_machine_scale_set_id VirtualMachineScaleSetExtensionA#virtual_machine_scale_set_id}.'''
        result = self._values.get("virtual_machine_scale_set_id")
        assert result is not None, "Required property 'virtual_machine_scale_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#auto_upgrade_minor_version VirtualMachineScaleSetExtensionA#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_update_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#force_update_tag VirtualMachineScaleSetExtensionA#force_update_tag}.'''
        result = self._values.get("force_update_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#id VirtualMachineScaleSetExtensionA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#protected_settings VirtualMachineScaleSetExtensionA#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#settings VirtualMachineScaleSetExtensionA#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualMachineScaleSetExtensionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#timeouts VirtualMachineScaleSetExtensionA#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualMachineScaleSetExtensionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetExtensionAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachineScaleSetExtension.VirtualMachineScaleSetExtensionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualMachineScaleSetExtensionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#create VirtualMachineScaleSetExtensionA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#delete VirtualMachineScaleSetExtensionA#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#read VirtualMachineScaleSetExtensionA#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#update VirtualMachineScaleSetExtensionA#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8227ba5de5fc23a44e5b4624a6a53364afa828bcc7bb9fe04ae5dd251dbfd84d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#create VirtualMachineScaleSetExtensionA#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#delete VirtualMachineScaleSetExtensionA#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#read VirtualMachineScaleSetExtensionA#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_scale_set_extension#update VirtualMachineScaleSetExtensionA#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetExtensionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetExtensionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachineScaleSetExtension.VirtualMachineScaleSetExtensionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ad0c63d3080e9ef5649086a6bc35b1a05b7f49a3f77bd5939556bfd0e3613ee)
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
            type_hints = typing.get_type_hints(_typecheckingstub__66de8c92f1d6e30263c47df5bcf8dda8255325b9d9fda8d20920c23ee0b3ee54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__359c99d5d7e3b490c8cfd1e124110d857d116afcb5b777e4f804bf6f6e403042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3b346fe6f9d0316b5b89202479dee7eeb8a559dc520a71c8e4428e836a977e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091241a0d1d84b16c0a77239f894c00eda6b41cf4a195f2e5b4eeb53b2ef7838)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369c5a235903ce36d1a048490866366ad16936c56daf5b55e768d22a090442eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualMachineScaleSetExtensionA",
    "VirtualMachineScaleSetExtensionAConfig",
    "VirtualMachineScaleSetExtensionTimeouts",
    "VirtualMachineScaleSetExtensionTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__22f01228ace1fb4ce695994c2d35d762c0ff398b3eb2982f783f3202fe6c8208(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    publisher: builtins.str,
    type: builtins.str,
    type_handler_version: builtins.str,
    virtual_machine_scale_set_id: builtins.str,
    auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_update_tag: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    protected_settings: typing.Optional[builtins.str] = None,
    settings: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__341a006b38f52bd5c2b7a65ba87c69f7a1a196754f8f96c882a6149c8bf3b40e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac77c4fcbddf1deee748c6a83c52d0ffc636f28a4b12caf5c902e0ace7172806(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc1168387b7630c4e88247f389fc739e5dac014f07c8e8d182ba34bff3d9e0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5fcab293f30782f32dca1e16e8c6af26b23a94060d1685523621296d8dfe8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1121a70d8d3c0e34fd0a986029b182ea0806ada4764a9d3b1ff4b9b76670c3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0598f7d527b47c2ef87c6c7896c48f8f320ba550da9bccbe3fce9f78cc16953c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fc4e04ab1aa684e0a381d9ad831e1592b64cbfc56fa45bf5ae0edb8c5741387(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2510fc4038be133659339022c8718e78e21eec6fcd47749f7c8651ab9cc4be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bb3299cc986d80a8e66a73efe48a30e68948b8fb53f83d2bb5e9dc045dfdd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01862fe60064d71bce49980e9089a43c5639b98db1ca7aa345a89711cd7768a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b9eeb26fdedd192a34888cea7e46e0bf168d070c2c78b5680a512c0daa37b5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    publisher: builtins.str,
    type: builtins.str,
    type_handler_version: builtins.str,
    virtual_machine_scale_set_id: builtins.str,
    auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_update_tag: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    protected_settings: typing.Optional[builtins.str] = None,
    settings: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8227ba5de5fc23a44e5b4624a6a53364afa828bcc7bb9fe04ae5dd251dbfd84d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad0c63d3080e9ef5649086a6bc35b1a05b7f49a3f77bd5939556bfd0e3613ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66de8c92f1d6e30263c47df5bcf8dda8255325b9d9fda8d20920c23ee0b3ee54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359c99d5d7e3b490c8cfd1e124110d857d116afcb5b777e4f804bf6f6e403042(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3b346fe6f9d0316b5b89202479dee7eeb8a559dc520a71c8e4428e836a977e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091241a0d1d84b16c0a77239f894c00eda6b41cf4a195f2e5b4eeb53b2ef7838(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369c5a235903ce36d1a048490866366ad16936c56daf5b55e768d22a090442eb(
    value: typing.Optional[typing.Union[VirtualMachineScaleSetExtensionTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
