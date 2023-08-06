'''
# `azurestack_virtual_machine_extension`

Refer to the Terraform Registory for docs: [`azurestack_virtual_machine_extension`](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension).
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


class VirtualMachineExtension(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachineExtension.VirtualMachineExtension",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension azurestack_virtual_machine_extension}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        virtual_machine_id: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        settings: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineExtensionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension azurestack_virtual_machine_extension} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#name VirtualMachineExtension#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#publisher VirtualMachineExtension#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type VirtualMachineExtension#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type_handler_version VirtualMachineExtension#type_handler_version}.
        :param virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#virtual_machine_id VirtualMachineExtension#virtual_machine_id}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#auto_upgrade_minor_version VirtualMachineExtension#auto_upgrade_minor_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#id VirtualMachineExtension#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#protected_settings VirtualMachineExtension#protected_settings}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#settings VirtualMachineExtension#settings}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#tags VirtualMachineExtension#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#timeouts VirtualMachineExtension#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53e7fb5b9befb0e821f68378b54cfaf37c09560fe931bbf8800077dfddf6aaa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualMachineExtensionConfig(
            name=name,
            publisher=publisher,
            type=type,
            type_handler_version=type_handler_version,
            virtual_machine_id=virtual_machine_id,
            auto_upgrade_minor_version=auto_upgrade_minor_version,
            id=id,
            protected_settings=protected_settings,
            settings=settings,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#create VirtualMachineExtension#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#delete VirtualMachineExtension#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#read VirtualMachineExtension#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#update VirtualMachineExtension#update}.
        '''
        value = VirtualMachineExtensionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProtectedSettings")
    def reset_protected_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedSettings", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualMachineExtensionTimeoutsOutputReference":
        return typing.cast("VirtualMachineExtensionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersionInput")
    def auto_upgrade_minor_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoUpgradeMinorVersionInput"))

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
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualMachineExtensionTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualMachineExtensionTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersionInput")
    def type_handler_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeHandlerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineIdInput")
    def virtual_machine_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineIdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ea9bb5598f3bd3c1cc9e9bdd4f8c688ddee649f67d64bafe60cdbc0bc2d2c6c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a273f56e0f6ac017da04a459f02402210fcdeb2288b8a219e4890713792b46d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7045ad561fafc2ad94ed53ea815f9a0f80a73cd9731cff3a801a06fe0a518ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c13cb393f550bdbdc91740ebb5a00236457eef3ad606d974570f3f2df1933a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbd62599b4afda9e4b6a68b4faac770fd707cd2e7c92499c610a0462a8aa929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__190ddfe88afd9dab396292da597caae2245a6b2d4147a6c82d413cfe0f31062f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c02cd83ccc09076bf08258dd7750f10402693bfd868eb259c2f58ab1f86f409)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12949cc83834f6d10aa2e6bf0ee3a5a76c6c321f2631ec7005fcbe4105ae81c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2ba6e02e22e3ff74295141238a6b32e41fd6c2deae01644c57fb03fd891074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56aecd756494035d2d829e08a817c6ea20c6e452439e3be45d444418467fb99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachineExtension.VirtualMachineExtensionConfig",
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
        "virtual_machine_id": "virtualMachineId",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "id": "id",
        "protected_settings": "protectedSettings",
        "settings": "settings",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class VirtualMachineExtensionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        virtual_machine_id: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        settings: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineExtensionTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#name VirtualMachineExtension#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#publisher VirtualMachineExtension#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type VirtualMachineExtension#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type_handler_version VirtualMachineExtension#type_handler_version}.
        :param virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#virtual_machine_id VirtualMachineExtension#virtual_machine_id}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#auto_upgrade_minor_version VirtualMachineExtension#auto_upgrade_minor_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#id VirtualMachineExtension#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#protected_settings VirtualMachineExtension#protected_settings}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#settings VirtualMachineExtension#settings}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#tags VirtualMachineExtension#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#timeouts VirtualMachineExtension#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = VirtualMachineExtensionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7356aca49d768d65d6e56d59438ecc3ac653c9b30291071193ba7890a96581e3)
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
            check_type(argname="argument virtual_machine_id", value=virtual_machine_id, expected_type=type_hints["virtual_machine_id"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
            "type_handler_version": type_handler_version,
            "virtual_machine_id": virtual_machine_id,
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
        if id is not None:
            self._values["id"] = id
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if settings is not None:
            self._values["settings"] = settings
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#name VirtualMachineExtension#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#publisher VirtualMachineExtension#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type VirtualMachineExtension#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#type_handler_version VirtualMachineExtension#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_machine_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#virtual_machine_id VirtualMachineExtension#virtual_machine_id}.'''
        result = self._values.get("virtual_machine_id")
        assert result is not None, "Required property 'virtual_machine_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#auto_upgrade_minor_version VirtualMachineExtension#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#id VirtualMachineExtension#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#protected_settings VirtualMachineExtension#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#settings VirtualMachineExtension#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#tags VirtualMachineExtension#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualMachineExtensionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#timeouts VirtualMachineExtension#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualMachineExtensionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineExtensionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachineExtension.VirtualMachineExtensionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualMachineExtensionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#create VirtualMachineExtension#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#delete VirtualMachineExtension#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#read VirtualMachineExtension#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#update VirtualMachineExtension#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac4951a4310abdc1f17f2d3699018315726cfe3f0cdea504fb792be15a077dd)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#create VirtualMachineExtension#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#delete VirtualMachineExtension#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#read VirtualMachineExtension#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine_extension#update VirtualMachineExtension#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineExtensionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineExtensionTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachineExtension.VirtualMachineExtensionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9a945cf758dedfff73630136dcd043a761266a5069467c4a01fb5a43cb8d128)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08cf30597685fd8c572983b531c107c34a381cfc3f28988f87eaf47136ad8451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b5cd0dbe84f0cae4ccc3497443d023b1d19fb3b7db9a63da5f3567b819888a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc23e4da228ab43e44f0a4b094c4b30900d019586dfea36d8ca3b19ff9f3bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e45f96ba6ae58085a5eee3e044cc076c72420a9e5b3293d2f625880b5b01701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a77f3b99bf234ebd1cf57fd617f8acb750d62931e7b7fc57651ca250cd5c4b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualMachineExtension",
    "VirtualMachineExtensionConfig",
    "VirtualMachineExtensionTimeouts",
    "VirtualMachineExtensionTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__c53e7fb5b9befb0e821f68378b54cfaf37c09560fe931bbf8800077dfddf6aaa(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    publisher: builtins.str,
    type: builtins.str,
    type_handler_version: builtins.str,
    virtual_machine_id: builtins.str,
    auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    protected_settings: typing.Optional[builtins.str] = None,
    settings: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__ea9bb5598f3bd3c1cc9e9bdd4f8c688ddee649f67d64bafe60cdbc0bc2d2c6c4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a273f56e0f6ac017da04a459f02402210fcdeb2288b8a219e4890713792b46d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7045ad561fafc2ad94ed53ea815f9a0f80a73cd9731cff3a801a06fe0a518ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c13cb393f550bdbdc91740ebb5a00236457eef3ad606d974570f3f2df1933a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbd62599b4afda9e4b6a68b4faac770fd707cd2e7c92499c610a0462a8aa929(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__190ddfe88afd9dab396292da597caae2245a6b2d4147a6c82d413cfe0f31062f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c02cd83ccc09076bf08258dd7750f10402693bfd868eb259c2f58ab1f86f409(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12949cc83834f6d10aa2e6bf0ee3a5a76c6c321f2631ec7005fcbe4105ae81c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2ba6e02e22e3ff74295141238a6b32e41fd6c2deae01644c57fb03fd891074(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56aecd756494035d2d829e08a817c6ea20c6e452439e3be45d444418467fb99c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7356aca49d768d65d6e56d59438ecc3ac653c9b30291071193ba7890a96581e3(
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
    virtual_machine_id: builtins.str,
    auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    protected_settings: typing.Optional[builtins.str] = None,
    settings: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac4951a4310abdc1f17f2d3699018315726cfe3f0cdea504fb792be15a077dd(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a945cf758dedfff73630136dcd043a761266a5069467c4a01fb5a43cb8d128(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08cf30597685fd8c572983b531c107c34a381cfc3f28988f87eaf47136ad8451(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b5cd0dbe84f0cae4ccc3497443d023b1d19fb3b7db9a63da5f3567b819888a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc23e4da228ab43e44f0a4b094c4b30900d019586dfea36d8ca3b19ff9f3bf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e45f96ba6ae58085a5eee3e044cc076c72420a9e5b3293d2f625880b5b01701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77f3b99bf234ebd1cf57fd617f8acb750d62931e7b7fc57651ca250cd5c4b55(
    value: typing.Optional[typing.Union[VirtualMachineExtensionTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
