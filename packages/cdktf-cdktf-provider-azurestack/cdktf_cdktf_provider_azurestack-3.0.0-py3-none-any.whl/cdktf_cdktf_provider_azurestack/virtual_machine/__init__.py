'''
# `azurestack_virtual_machine`

Refer to the Terraform Registory for docs: [`azurestack_virtual_machine`](https://www.terraform.io/docs/providers/azurestack/r/virtual_machine).
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


class VirtualMachine(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine azurestack_virtual_machine}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        resource_group_name: builtins.str,
        storage_os_disk: typing.Union["VirtualMachineStorageOsDisk", typing.Dict[builtins.str, typing.Any]],
        vm_size: builtins.str,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union["VirtualMachineBootDiagnostics", typing.Dict[builtins.str, typing.Any]]] = None,
        delete_data_disks_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delete_os_disk_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["VirtualMachineIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        os_profile: typing.Optional[typing.Union["VirtualMachineOsProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        os_profile_linux_config: typing.Optional[typing.Union["VirtualMachineOsProfileLinuxConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        os_profile_secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileSecrets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        os_profile_windows_config: typing.Optional[typing.Union["VirtualMachineOsProfileWindowsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        plan: typing.Optional[typing.Union["VirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        primary_network_interface_id: typing.Optional[builtins.str] = None,
        storage_data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineStorageDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        storage_image_reference: typing.Optional[typing.Union["VirtualMachineStorageImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine azurestack_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#location VirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#network_interface_ids VirtualMachine#network_interface_ids}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#resource_group_name VirtualMachine#resource_group_name}.
        :param storage_os_disk: storage_os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_os_disk VirtualMachine#storage_os_disk}
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vm_size VirtualMachine#vm_size}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#availability_set_id VirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#boot_diagnostics VirtualMachine#boot_diagnostics}
        :param delete_data_disks_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_data_disks_on_termination VirtualMachine#delete_data_disks_on_termination}.
        :param delete_os_disk_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_os_disk_on_termination VirtualMachine#delete_os_disk_on_termination}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#identity VirtualMachine#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#license_type VirtualMachine#license_type}.
        :param os_profile: os_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile VirtualMachine#os_profile}
        :param os_profile_linux_config: os_profile_linux_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_linux_config VirtualMachine#os_profile_linux_config}
        :param os_profile_secrets: os_profile_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_secrets VirtualMachine#os_profile_secrets}
        :param os_profile_windows_config: os_profile_windows_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_windows_config VirtualMachine#os_profile_windows_config}
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#plan VirtualMachine#plan}
        :param primary_network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#primary_network_interface_id VirtualMachine#primary_network_interface_id}.
        :param storage_data_disk: storage_data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_data_disk VirtualMachine#storage_data_disk}
        :param storage_image_reference: storage_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_image_reference VirtualMachine#storage_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#tags VirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timeouts VirtualMachine#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#zones VirtualMachine#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b32eebbe99d867007f36b3b462f3df6ee081f57e34fb55d036a924a3338c05b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualMachineConfig(
            location=location,
            name=name,
            network_interface_ids=network_interface_ids,
            resource_group_name=resource_group_name,
            storage_os_disk=storage_os_disk,
            vm_size=vm_size,
            availability_set_id=availability_set_id,
            boot_diagnostics=boot_diagnostics,
            delete_data_disks_on_termination=delete_data_disks_on_termination,
            delete_os_disk_on_termination=delete_os_disk_on_termination,
            id=id,
            identity=identity,
            license_type=license_type,
            os_profile=os_profile,
            os_profile_linux_config=os_profile_linux_config,
            os_profile_secrets=os_profile_secrets,
            os_profile_windows_config=os_profile_windows_config,
            plan=plan,
            primary_network_interface_id=primary_network_interface_id,
            storage_data_disk=storage_data_disk,
            storage_image_reference=storage_image_reference,
            tags=tags,
            timeouts=timeouts,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        storage_uri: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enabled VirtualMachine#enabled}.
        :param storage_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_uri VirtualMachine#storage_uri}.
        '''
        value = VirtualMachineBootDiagnostics(enabled=enabled, storage_uri=storage_uri)

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#type VirtualMachine#type}.
        '''
        value = VirtualMachineIdentity(type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putOsProfile")
    def put_os_profile(
        self,
        *,
        admin_username: builtins.str,
        computer_name: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_username VirtualMachine#admin_username}.
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#computer_name VirtualMachine#computer_name}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_password VirtualMachine#admin_password}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#custom_data VirtualMachine#custom_data}.
        '''
        value = VirtualMachineOsProfile(
            admin_username=admin_username,
            computer_name=computer_name,
            admin_password=admin_password,
            custom_data=custom_data,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfile", [value]))

    @jsii.member(jsii_name="putOsProfileLinuxConfig")
    def put_os_profile_linux_config(
        self,
        *,
        disable_password_authentication: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        ssh_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileLinuxConfigSshKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disable_password_authentication VirtualMachine#disable_password_authentication}.
        :param ssh_keys: ssh_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#ssh_keys VirtualMachine#ssh_keys}
        '''
        value = VirtualMachineOsProfileLinuxConfig(
            disable_password_authentication=disable_password_authentication,
            ssh_keys=ssh_keys,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfileLinuxConfig", [value]))

    @jsii.member(jsii_name="putOsProfileSecrets")
    def put_os_profile_secrets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileSecrets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329d7d0f1b9263f70b8e8ab7403c77dba3ae812fb6dac16a14fa344fc7a87b55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOsProfileSecrets", [value]))

    @jsii.member(jsii_name="putOsProfileWindowsConfig")
    def put_os_profile_windows_config(
        self,
        *,
        additional_unattend_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable_automatic_upgrades: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timezone: typing.Optional[builtins.str] = None,
        winrm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileWindowsConfigWinrm", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_unattend_config: additional_unattend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#additional_unattend_config VirtualMachine#additional_unattend_config}
        :param enable_automatic_upgrades: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enable_automatic_upgrades VirtualMachine#enable_automatic_upgrades}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#provision_vm_agent VirtualMachine#provision_vm_agent}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timezone VirtualMachine#timezone}.
        :param winrm: winrm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#winrm VirtualMachine#winrm}
        '''
        value = VirtualMachineOsProfileWindowsConfig(
            additional_unattend_config=additional_unattend_config,
            enable_automatic_upgrades=enable_automatic_upgrades,
            provision_vm_agent=provision_vm_agent,
            timezone=timezone,
            winrm=winrm,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfileWindowsConfig", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#product VirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.
        '''
        value = VirtualMachinePlan(name=name, product=product, publisher=publisher)

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putStorageDataDisk")
    def put_storage_data_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineStorageDataDisk", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__206c12f82e66ceefe6812bf6d48924d5ebffed887711e1727a76fb5a46480db8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageDataDisk", [value]))

    @jsii.member(jsii_name="putStorageImageReference")
    def put_storage_image_reference(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#offer VirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#sku VirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#version VirtualMachine#version}.
        '''
        value = VirtualMachineStorageImageReference(
            id=id, offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putStorageImageReference", [value]))

    @jsii.member(jsii_name="putStorageOsDisk")
    def put_storage_os_disk(
        self,
        *,
        create_option: builtins.str,
        name: builtins.str,
        caching: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        image_uri: typing.Optional[builtins.str] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        vhd_uri: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create_option VirtualMachine#create_option}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#caching VirtualMachine#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disk_size_gb VirtualMachine#disk_size_gb}.
        :param image_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#image_uri VirtualMachine#image_uri}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_id VirtualMachine#managed_disk_id}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_type VirtualMachine#managed_disk_type}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_type VirtualMachine#os_type}.
        :param vhd_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vhd_uri VirtualMachine#vhd_uri}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#write_accelerator_enabled VirtualMachine#write_accelerator_enabled}.
        '''
        value = VirtualMachineStorageOsDisk(
            create_option=create_option,
            name=name,
            caching=caching,
            disk_size_gb=disk_size_gb,
            image_uri=image_uri,
            managed_disk_id=managed_disk_id,
            managed_disk_type=managed_disk_type,
            os_type=os_type,
            vhd_uri=vhd_uri,
            write_accelerator_enabled=write_accelerator_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageOsDisk", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create VirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete VirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#read VirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#update VirtualMachine#update}.
        '''
        value = VirtualMachineTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAvailabilitySetId")
    def reset_availability_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilitySetId", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetDeleteDataDisksOnTermination")
    def reset_delete_data_disks_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteDataDisksOnTermination", []))

    @jsii.member(jsii_name="resetDeleteOsDiskOnTermination")
    def reset_delete_os_disk_on_termination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteOsDiskOnTermination", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetOsProfile")
    def reset_os_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfile", []))

    @jsii.member(jsii_name="resetOsProfileLinuxConfig")
    def reset_os_profile_linux_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileLinuxConfig", []))

    @jsii.member(jsii_name="resetOsProfileSecrets")
    def reset_os_profile_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileSecrets", []))

    @jsii.member(jsii_name="resetOsProfileWindowsConfig")
    def reset_os_profile_windows_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileWindowsConfig", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPrimaryNetworkInterfaceId")
    def reset_primary_network_interface_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryNetworkInterfaceId", []))

    @jsii.member(jsii_name="resetStorageDataDisk")
    def reset_storage_data_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageDataDisk", []))

    @jsii.member(jsii_name="resetStorageImageReference")
    def reset_storage_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(self) -> "VirtualMachineBootDiagnosticsOutputReference":
        return typing.cast("VirtualMachineBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "VirtualMachineIdentityOutputReference":
        return typing.cast("VirtualMachineIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="osProfile")
    def os_profile(self) -> "VirtualMachineOsProfileOutputReference":
        return typing.cast("VirtualMachineOsProfileOutputReference", jsii.get(self, "osProfile"))

    @builtins.property
    @jsii.member(jsii_name="osProfileLinuxConfig")
    def os_profile_linux_config(
        self,
    ) -> "VirtualMachineOsProfileLinuxConfigOutputReference":
        return typing.cast("VirtualMachineOsProfileLinuxConfigOutputReference", jsii.get(self, "osProfileLinuxConfig"))

    @builtins.property
    @jsii.member(jsii_name="osProfileSecrets")
    def os_profile_secrets(self) -> "VirtualMachineOsProfileSecretsList":
        return typing.cast("VirtualMachineOsProfileSecretsList", jsii.get(self, "osProfileSecrets"))

    @builtins.property
    @jsii.member(jsii_name="osProfileWindowsConfig")
    def os_profile_windows_config(
        self,
    ) -> "VirtualMachineOsProfileWindowsConfigOutputReference":
        return typing.cast("VirtualMachineOsProfileWindowsConfigOutputReference", jsii.get(self, "osProfileWindowsConfig"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "VirtualMachinePlanOutputReference":
        return typing.cast("VirtualMachinePlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="storageDataDisk")
    def storage_data_disk(self) -> "VirtualMachineStorageDataDiskList":
        return typing.cast("VirtualMachineStorageDataDiskList", jsii.get(self, "storageDataDisk"))

    @builtins.property
    @jsii.member(jsii_name="storageImageReference")
    def storage_image_reference(
        self,
    ) -> "VirtualMachineStorageImageReferenceOutputReference":
        return typing.cast("VirtualMachineStorageImageReferenceOutputReference", jsii.get(self, "storageImageReference"))

    @builtins.property
    @jsii.member(jsii_name="storageOsDisk")
    def storage_os_disk(self) -> "VirtualMachineStorageOsDiskOutputReference":
        return typing.cast("VirtualMachineStorageOsDiskOutputReference", jsii.get(self, "storageOsDisk"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualMachineTimeoutsOutputReference":
        return typing.cast("VirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="availabilitySetIdInput")
    def availability_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilitySetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["VirtualMachineBootDiagnostics"]:
        return typing.cast(typing.Optional["VirtualMachineBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteDataDisksOnTerminationInput")
    def delete_data_disks_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteDataDisksOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteOsDiskOnTerminationInput")
    def delete_os_disk_on_termination_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deleteOsDiskOnTerminationInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["VirtualMachineIdentity"]:
        return typing.cast(typing.Optional["VirtualMachineIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIdsInput")
    def network_interface_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkInterfaceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileInput")
    def os_profile_input(self) -> typing.Optional["VirtualMachineOsProfile"]:
        return typing.cast(typing.Optional["VirtualMachineOsProfile"], jsii.get(self, "osProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileLinuxConfigInput")
    def os_profile_linux_config_input(
        self,
    ) -> typing.Optional["VirtualMachineOsProfileLinuxConfig"]:
        return typing.cast(typing.Optional["VirtualMachineOsProfileLinuxConfig"], jsii.get(self, "osProfileLinuxConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileSecretsInput")
    def os_profile_secrets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecrets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecrets"]]], jsii.get(self, "osProfileSecretsInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileWindowsConfigInput")
    def os_profile_windows_config_input(
        self,
    ) -> typing.Optional["VirtualMachineOsProfileWindowsConfig"]:
        return typing.cast(typing.Optional["VirtualMachineOsProfileWindowsConfig"], jsii.get(self, "osProfileWindowsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["VirtualMachinePlan"]:
        return typing.cast(typing.Optional["VirtualMachinePlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryNetworkInterfaceIdInput")
    def primary_network_interface_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryNetworkInterfaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageDataDiskInput")
    def storage_data_disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineStorageDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineStorageDataDisk"]]], jsii.get(self, "storageDataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="storageImageReferenceInput")
    def storage_image_reference_input(
        self,
    ) -> typing.Optional["VirtualMachineStorageImageReference"]:
        return typing.cast(typing.Optional["VirtualMachineStorageImageReference"], jsii.get(self, "storageImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageOsDiskInput")
    def storage_os_disk_input(self) -> typing.Optional["VirtualMachineStorageOsDisk"]:
        return typing.cast(typing.Optional["VirtualMachineStorageOsDisk"], jsii.get(self, "storageOsDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilitySetId")
    def availability_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilitySetId"))

    @availability_set_id.setter
    def availability_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653a671efd4c547c80bd7359b453f84a6a84c72949c01c9f255d7a020251be84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilitySetId", value)

    @builtins.property
    @jsii.member(jsii_name="deleteDataDisksOnTermination")
    def delete_data_disks_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteDataDisksOnTermination"))

    @delete_data_disks_on_termination.setter
    def delete_data_disks_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__152fece75e4bb18445089a664ce974d82808d80fc8791e816af4fcee49541b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteDataDisksOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="deleteOsDiskOnTermination")
    def delete_os_disk_on_termination(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deleteOsDiskOnTermination"))

    @delete_os_disk_on_termination.setter
    def delete_os_disk_on_termination(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3985908be8a679cd2ee8307b8e1cf461435c80457999a8aaf417ec56a4c2b2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOsDiskOnTermination", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d65efc12519ad2eeb8f36d4e02503eb85cb85694b9d7ba44ebf1773ffebb738)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d042ee59f0ce3a482ff49d7fda2b3db11735f1c89dde20bb95e961d40e30ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc39afcaf326aad8d0448d54e0e6fcc2b876a17a3cfa4ee8a3c0b0d87c683b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391c0d2eacdb8f5c4a05e2b77ad9d1fc397f92a91a3d1c9038bbd892d64b411b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @network_interface_ids.setter
    def network_interface_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3dbef4e98e6bdd22144ac5f4096330e98d656669af45e1b6ea4c0d40d7f1516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceIds", value)

    @builtins.property
    @jsii.member(jsii_name="primaryNetworkInterfaceId")
    def primary_network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryNetworkInterfaceId"))

    @primary_network_interface_id.setter
    def primary_network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec3793fd6c38628b06c664dfa9c79e98ca6ba97f426aac40721ad78e91da9c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryNetworkInterfaceId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53344f66e13e64e694b4b58bcc50929ae8c9d660a2c909e1d8daaeca27d0496f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0859a547fe7aae200063c26a374f9c5b8fa3662cad19df05ab0ef14633e43163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90adbc1e15b58ac4657a045c2ef069a9907116e974c8742c5d6e38b039c90604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd7c62c1ec80a6dfde9e6161455959a72cf880b04b02b593767f3b41456a377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "storage_uri": "storageUri"},
)
class VirtualMachineBootDiagnostics:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        storage_uri: builtins.str,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enabled VirtualMachine#enabled}.
        :param storage_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_uri VirtualMachine#storage_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9750aa868242b1172896197fab60f4118fd48ae9bebedfad5f1ae09baf48928)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument storage_uri", value=storage_uri, expected_type=type_hints["storage_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
            "storage_uri": storage_uri,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enabled VirtualMachine#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def storage_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_uri VirtualMachine#storage_uri}.'''
        result = self._values.get("storage_uri")
        assert result is not None, "Required property 'storage_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineBootDiagnosticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ca47811b5e2f5f87c64492ad4f3a9e96a1cc768e69b0b05dc66e7e6d48a8426)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="storageUriInput")
    def storage_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a33979b7ee1a3c0b56ab1954eb6c2848ef0c9c6d9fd0a25d6913e2f4a4a493f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="storageUri")
    def storage_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageUri"))

    @storage_uri.setter
    def storage_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc55ab87166a7db743eac4ba3fef2a8f59410d8e6e1f6c8f8e9f650bc054f277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineBootDiagnostics]:
        return typing.cast(typing.Optional[VirtualMachineBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7282729197827644525a8c8f729965a1d48958b5621557a4137a8c204c39fa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineConfig",
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
        "network_interface_ids": "networkInterfaceIds",
        "resource_group_name": "resourceGroupName",
        "storage_os_disk": "storageOsDisk",
        "vm_size": "vmSize",
        "availability_set_id": "availabilitySetId",
        "boot_diagnostics": "bootDiagnostics",
        "delete_data_disks_on_termination": "deleteDataDisksOnTermination",
        "delete_os_disk_on_termination": "deleteOsDiskOnTermination",
        "id": "id",
        "identity": "identity",
        "license_type": "licenseType",
        "os_profile": "osProfile",
        "os_profile_linux_config": "osProfileLinuxConfig",
        "os_profile_secrets": "osProfileSecrets",
        "os_profile_windows_config": "osProfileWindowsConfig",
        "plan": "plan",
        "primary_network_interface_id": "primaryNetworkInterfaceId",
        "storage_data_disk": "storageDataDisk",
        "storage_image_reference": "storageImageReference",
        "tags": "tags",
        "timeouts": "timeouts",
        "zones": "zones",
    },
)
class VirtualMachineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        network_interface_ids: typing.Sequence[builtins.str],
        resource_group_name: builtins.str,
        storage_os_disk: typing.Union["VirtualMachineStorageOsDisk", typing.Dict[builtins.str, typing.Any]],
        vm_size: builtins.str,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union[VirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
        delete_data_disks_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delete_os_disk_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["VirtualMachineIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        os_profile: typing.Optional[typing.Union["VirtualMachineOsProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        os_profile_linux_config: typing.Optional[typing.Union["VirtualMachineOsProfileLinuxConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        os_profile_secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileSecrets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        os_profile_windows_config: typing.Optional[typing.Union["VirtualMachineOsProfileWindowsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        plan: typing.Optional[typing.Union["VirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        primary_network_interface_id: typing.Optional[builtins.str] = None,
        storage_data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineStorageDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        storage_image_reference: typing.Optional[typing.Union["VirtualMachineStorageImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#location VirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#network_interface_ids VirtualMachine#network_interface_ids}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#resource_group_name VirtualMachine#resource_group_name}.
        :param storage_os_disk: storage_os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_os_disk VirtualMachine#storage_os_disk}
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vm_size VirtualMachine#vm_size}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#availability_set_id VirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#boot_diagnostics VirtualMachine#boot_diagnostics}
        :param delete_data_disks_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_data_disks_on_termination VirtualMachine#delete_data_disks_on_termination}.
        :param delete_os_disk_on_termination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_os_disk_on_termination VirtualMachine#delete_os_disk_on_termination}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#identity VirtualMachine#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#license_type VirtualMachine#license_type}.
        :param os_profile: os_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile VirtualMachine#os_profile}
        :param os_profile_linux_config: os_profile_linux_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_linux_config VirtualMachine#os_profile_linux_config}
        :param os_profile_secrets: os_profile_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_secrets VirtualMachine#os_profile_secrets}
        :param os_profile_windows_config: os_profile_windows_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_windows_config VirtualMachine#os_profile_windows_config}
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#plan VirtualMachine#plan}
        :param primary_network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#primary_network_interface_id VirtualMachine#primary_network_interface_id}.
        :param storage_data_disk: storage_data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_data_disk VirtualMachine#storage_data_disk}
        :param storage_image_reference: storage_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_image_reference VirtualMachine#storage_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#tags VirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timeouts VirtualMachine#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#zones VirtualMachine#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_os_disk, dict):
            storage_os_disk = VirtualMachineStorageOsDisk(**storage_os_disk)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = VirtualMachineBootDiagnostics(**boot_diagnostics)
        if isinstance(identity, dict):
            identity = VirtualMachineIdentity(**identity)
        if isinstance(os_profile, dict):
            os_profile = VirtualMachineOsProfile(**os_profile)
        if isinstance(os_profile_linux_config, dict):
            os_profile_linux_config = VirtualMachineOsProfileLinuxConfig(**os_profile_linux_config)
        if isinstance(os_profile_windows_config, dict):
            os_profile_windows_config = VirtualMachineOsProfileWindowsConfig(**os_profile_windows_config)
        if isinstance(plan, dict):
            plan = VirtualMachinePlan(**plan)
        if isinstance(storage_image_reference, dict):
            storage_image_reference = VirtualMachineStorageImageReference(**storage_image_reference)
        if isinstance(timeouts, dict):
            timeouts = VirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91cfcaafd79175e3228e17088bbea9e32ff929d1e3360ca9eb885c3b675ebfd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface_ids", value=network_interface_ids, expected_type=type_hints["network_interface_ids"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_os_disk", value=storage_os_disk, expected_type=type_hints["storage_os_disk"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument availability_set_id", value=availability_set_id, expected_type=type_hints["availability_set_id"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument delete_data_disks_on_termination", value=delete_data_disks_on_termination, expected_type=type_hints["delete_data_disks_on_termination"])
            check_type(argname="argument delete_os_disk_on_termination", value=delete_os_disk_on_termination, expected_type=type_hints["delete_os_disk_on_termination"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument os_profile", value=os_profile, expected_type=type_hints["os_profile"])
            check_type(argname="argument os_profile_linux_config", value=os_profile_linux_config, expected_type=type_hints["os_profile_linux_config"])
            check_type(argname="argument os_profile_secrets", value=os_profile_secrets, expected_type=type_hints["os_profile_secrets"])
            check_type(argname="argument os_profile_windows_config", value=os_profile_windows_config, expected_type=type_hints["os_profile_windows_config"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument primary_network_interface_id", value=primary_network_interface_id, expected_type=type_hints["primary_network_interface_id"])
            check_type(argname="argument storage_data_disk", value=storage_data_disk, expected_type=type_hints["storage_data_disk"])
            check_type(argname="argument storage_image_reference", value=storage_image_reference, expected_type=type_hints["storage_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
            "name": name,
            "network_interface_ids": network_interface_ids,
            "resource_group_name": resource_group_name,
            "storage_os_disk": storage_os_disk,
            "vm_size": vm_size,
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
        if availability_set_id is not None:
            self._values["availability_set_id"] = availability_set_id
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if delete_data_disks_on_termination is not None:
            self._values["delete_data_disks_on_termination"] = delete_data_disks_on_termination
        if delete_os_disk_on_termination is not None:
            self._values["delete_os_disk_on_termination"] = delete_os_disk_on_termination
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if license_type is not None:
            self._values["license_type"] = license_type
        if os_profile is not None:
            self._values["os_profile"] = os_profile
        if os_profile_linux_config is not None:
            self._values["os_profile_linux_config"] = os_profile_linux_config
        if os_profile_secrets is not None:
            self._values["os_profile_secrets"] = os_profile_secrets
        if os_profile_windows_config is not None:
            self._values["os_profile_windows_config"] = os_profile_windows_config
        if plan is not None:
            self._values["plan"] = plan
        if primary_network_interface_id is not None:
            self._values["primary_network_interface_id"] = primary_network_interface_id
        if storage_data_disk is not None:
            self._values["storage_data_disk"] = storage_data_disk
        if storage_image_reference is not None:
            self._values["storage_image_reference"] = storage_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zones is not None:
            self._values["zones"] = zones

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#location VirtualMachine#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#network_interface_ids VirtualMachine#network_interface_ids}.'''
        result = self._values.get("network_interface_ids")
        assert result is not None, "Required property 'network_interface_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#resource_group_name VirtualMachine#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_os_disk(self) -> "VirtualMachineStorageOsDisk":
        '''storage_os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_os_disk VirtualMachine#storage_os_disk}
        '''
        result = self._values.get("storage_os_disk")
        assert result is not None, "Required property 'storage_os_disk' is missing"
        return typing.cast("VirtualMachineStorageOsDisk", result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vm_size VirtualMachine#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#availability_set_id VirtualMachine#availability_set_id}.'''
        result = self._values.get("availability_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_diagnostics(self) -> typing.Optional[VirtualMachineBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#boot_diagnostics VirtualMachine#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[VirtualMachineBootDiagnostics], result)

    @builtins.property
    def delete_data_disks_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_data_disks_on_termination VirtualMachine#delete_data_disks_on_termination}.'''
        result = self._values.get("delete_data_disks_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def delete_os_disk_on_termination(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete_os_disk_on_termination VirtualMachine#delete_os_disk_on_termination}.'''
        result = self._values.get("delete_os_disk_on_termination")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["VirtualMachineIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#identity VirtualMachine#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["VirtualMachineIdentity"], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#license_type VirtualMachine#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_profile(self) -> typing.Optional["VirtualMachineOsProfile"]:
        '''os_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile VirtualMachine#os_profile}
        '''
        result = self._values.get("os_profile")
        return typing.cast(typing.Optional["VirtualMachineOsProfile"], result)

    @builtins.property
    def os_profile_linux_config(
        self,
    ) -> typing.Optional["VirtualMachineOsProfileLinuxConfig"]:
        '''os_profile_linux_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_linux_config VirtualMachine#os_profile_linux_config}
        '''
        result = self._values.get("os_profile_linux_config")
        return typing.cast(typing.Optional["VirtualMachineOsProfileLinuxConfig"], result)

    @builtins.property
    def os_profile_secrets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecrets"]]]:
        '''os_profile_secrets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_secrets VirtualMachine#os_profile_secrets}
        '''
        result = self._values.get("os_profile_secrets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecrets"]]], result)

    @builtins.property
    def os_profile_windows_config(
        self,
    ) -> typing.Optional["VirtualMachineOsProfileWindowsConfig"]:
        '''os_profile_windows_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_profile_windows_config VirtualMachine#os_profile_windows_config}
        '''
        result = self._values.get("os_profile_windows_config")
        return typing.cast(typing.Optional["VirtualMachineOsProfileWindowsConfig"], result)

    @builtins.property
    def plan(self) -> typing.Optional["VirtualMachinePlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#plan VirtualMachine#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["VirtualMachinePlan"], result)

    @builtins.property
    def primary_network_interface_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#primary_network_interface_id VirtualMachine#primary_network_interface_id}.'''
        result = self._values.get("primary_network_interface_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_data_disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineStorageDataDisk"]]]:
        '''storage_data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_data_disk VirtualMachine#storage_data_disk}
        '''
        result = self._values.get("storage_data_disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineStorageDataDisk"]]], result)

    @builtins.property
    def storage_image_reference(
        self,
    ) -> typing.Optional["VirtualMachineStorageImageReference"]:
        '''storage_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#storage_image_reference VirtualMachine#storage_image_reference}
        '''
        result = self._values.get("storage_image_reference")
        return typing.cast(typing.Optional["VirtualMachineStorageImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#tags VirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timeouts VirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualMachineTimeouts"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#zones VirtualMachine#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class VirtualMachineIdentity:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#type VirtualMachine#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eb0765fe601dfd1ffcf980d4b7b2f2347135944be95d92bce460c79ba73d6b2)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#type VirtualMachine#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineIdentityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b96fba6a326f539a2a95f32f4f9367032a59022c4df2b06561a9ca8cdf25bd94)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1a18cbd1c7fe76e0ba18e7ab08aac5d6241dc2355a72565ef2c7439d6d8082)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineIdentity]:
        return typing.cast(typing.Optional[VirtualMachineIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VirtualMachineIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eadd3d1b9a08d9746401e6762ec7e9d5feffc2e2ccda3f90a5b40f7c4850f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfile",
    jsii_struct_bases=[],
    name_mapping={
        "admin_username": "adminUsername",
        "computer_name": "computerName",
        "admin_password": "adminPassword",
        "custom_data": "customData",
    },
)
class VirtualMachineOsProfile:
    def __init__(
        self,
        *,
        admin_username: builtins.str,
        computer_name: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_username VirtualMachine#admin_username}.
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#computer_name VirtualMachine#computer_name}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_password VirtualMachine#admin_password}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#custom_data VirtualMachine#custom_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3082eab789e827b6495a1fa1e8412d979196a9bfa0c31f517b55ad666371c8e3)
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument computer_name", value=computer_name, expected_type=type_hints["computer_name"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_username": admin_username,
            "computer_name": computer_name,
        }
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if custom_data is not None:
            self._values["custom_data"] = custom_data

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_username VirtualMachine#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def computer_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#computer_name VirtualMachine#computer_name}.'''
        result = self._values.get("computer_name")
        assert result is not None, "Required property 'computer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#admin_password VirtualMachine#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#custom_data VirtualMachine#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileLinuxConfig",
    jsii_struct_bases=[],
    name_mapping={
        "disable_password_authentication": "disablePasswordAuthentication",
        "ssh_keys": "sshKeys",
    },
)
class VirtualMachineOsProfileLinuxConfig:
    def __init__(
        self,
        *,
        disable_password_authentication: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        ssh_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileLinuxConfigSshKeys", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disable_password_authentication VirtualMachine#disable_password_authentication}.
        :param ssh_keys: ssh_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#ssh_keys VirtualMachine#ssh_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c71131c4044c9332b15c94f599d1e2831707ecd15d65c872c23e18dcb07ba09d)
            check_type(argname="argument disable_password_authentication", value=disable_password_authentication, expected_type=type_hints["disable_password_authentication"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disable_password_authentication": disable_password_authentication,
        }
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys

    @builtins.property
    def disable_password_authentication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disable_password_authentication VirtualMachine#disable_password_authentication}.'''
        result = self._values.get("disable_password_authentication")
        assert result is not None, "Required property 'disable_password_authentication' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def ssh_keys(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileLinuxConfigSshKeys"]]]:
        '''ssh_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#ssh_keys VirtualMachine#ssh_keys}
        '''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileLinuxConfigSshKeys"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileLinuxConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileLinuxConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileLinuxConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb89f6cb6aa37cf1becb25351557df397f1dcc51f1d802fc36a42ed09e705a87)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSshKeys")
    def put_ssh_keys(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileLinuxConfigSshKeys", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e875614dc804e366d053e1b8bddd9bf6707a69766fb4f69a2a87a1b255f41da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSshKeys", [value]))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> "VirtualMachineOsProfileLinuxConfigSshKeysList":
        return typing.cast("VirtualMachineOsProfileLinuxConfigSshKeysList", jsii.get(self, "sshKeys"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthenticationInput")
    def disable_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disablePasswordAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileLinuxConfigSshKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileLinuxConfigSshKeys"]]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthentication")
    def disable_password_authentication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disablePasswordAuthentication"))

    @disable_password_authentication.setter
    def disable_password_authentication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6b5839cdfc3f34a0027d0237ecee82e4e11e190f2578e42da7cd8fd0b47f1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineOsProfileLinuxConfig]:
        return typing.cast(typing.Optional[VirtualMachineOsProfileLinuxConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineOsProfileLinuxConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d9c4e01de1232266f7886ce823f533e0f4ccfa8600506d3adf4dfb14b6ce3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileLinuxConfigSshKeys",
    jsii_struct_bases=[],
    name_mapping={"key_data": "keyData", "path": "path"},
)
class VirtualMachineOsProfileLinuxConfigSshKeys:
    def __init__(self, *, key_data: builtins.str, path: builtins.str) -> None:
        '''
        :param key_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#key_data VirtualMachine#key_data}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#path VirtualMachine#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c03283ed69943a640a1c906af274a7df40220f54a507ddafd341ab1b04fecdf)
            check_type(argname="argument key_data", value=key_data, expected_type=type_hints["key_data"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_data": key_data,
            "path": path,
        }

    @builtins.property
    def key_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#key_data VirtualMachine#key_data}.'''
        result = self._values.get("key_data")
        assert result is not None, "Required property 'key_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#path VirtualMachine#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileLinuxConfigSshKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileLinuxConfigSshKeysList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileLinuxConfigSshKeysList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76825923fe4d26edfdf6394fff009c99195d0fc94d4b3079384a5f1444ef1c0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineOsProfileLinuxConfigSshKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55989d699620572482ffb2726a7fd5a7ec477b71264e7a36020da8af3f545d8c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineOsProfileLinuxConfigSshKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__163df36c3dae4088ddc39ccc2bea4b1afe2dc408c4b68db57015e89c603b8c4d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bf1e064a90dc205e4f67c6721c7399d3615a690bd64fd0a58cf1072f1ce04f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11a679068e1335418bd1b8532b3a2756faf6f2ee7e107f875e030c83e7f2f834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileLinuxConfigSshKeys]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileLinuxConfigSshKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileLinuxConfigSshKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b5d853d93a1f0ea28de14b519e07abff1a03642856401114d44ac9a230e498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileLinuxConfigSshKeysOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileLinuxConfigSshKeysOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71f3c89e52698be068af228d9be191711db595005b24cf6db2093cb9f9bcb0c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyDataInput")
    def key_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyDataInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="keyData")
    def key_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyData"))

    @key_data.setter
    def key_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723424d4e328eee5c9c93de6b2cb98556d96670fa49ae5a0e0d9b56f5b5fa684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyData", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb97e22ddb39e902da9b62b5f1cb1da8545b17672675847b3e52bbc6e2e30b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bdabff09aa37118ed68c307a3ba1fe9e98bf0f429522c4078edb16a81d1954c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1e523b159d3b6fdcab9ea198fe62366d998e071aa4a74affe8a52a3a9674a9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNameInput")
    def computer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3943770a0052d07b5eadada2950b3aae8712de5fa1e8a39aaed9ecba6c60e8c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29761a910680b355622302b6cd5ddaf784a33d3ac8372e35e4941cd3b4b49215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="computerName")
    def computer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerName"))

    @computer_name.setter
    def computer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__563f7aeaa3ff2ca625b3a2bae5ad6e34fc3c01835d9fc6ad47e152166b55ede5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerName", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f88a4cd045a1d69c4bce050617d52f3403b2c86b39c23ba80665e5168dc646b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineOsProfile]:
        return typing.cast(typing.Optional[VirtualMachineOsProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VirtualMachineOsProfile]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64fca888011322b9ae6a58864576ff8c47e7f5ec3605c300ee518d048f39076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecrets",
    jsii_struct_bases=[],
    name_mapping={
        "source_vault_id": "sourceVaultId",
        "vault_certificates": "vaultCertificates",
    },
)
class VirtualMachineOsProfileSecrets:
    def __init__(
        self,
        *,
        source_vault_id: builtins.str,
        vault_certificates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileSecretsVaultCertificates", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#source_vault_id VirtualMachine#source_vault_id}.
        :param vault_certificates: vault_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vault_certificates VirtualMachine#vault_certificates}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e0330dd10446d74c58384dfb8cb00ae60d8e6d5c0206442087125d399fa5fa)
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
            check_type(argname="argument vault_certificates", value=vault_certificates, expected_type=type_hints["vault_certificates"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_vault_id": source_vault_id,
        }
        if vault_certificates is not None:
            self._values["vault_certificates"] = vault_certificates

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#source_vault_id VirtualMachine#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vault_certificates(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecretsVaultCertificates"]]]:
        '''vault_certificates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vault_certificates VirtualMachine#vault_certificates}
        '''
        result = self._values.get("vault_certificates")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecretsVaultCertificates"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileSecretsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecretsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31311ce4981fcabf8d71791ff1450a4e4e9e3d75f681b67553c7a6c8883d285f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineOsProfileSecretsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297d72ea46fa2456d1400eed4969e6da95ecfd99443aef16a24af1a258ee337f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineOsProfileSecretsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6bf5d676f9eb4787f8075fb52133fbb121fdc215dc670f2cdcf700c6b6394ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__000c145b6d951be6e666c93621cc3fa06523bd4e0ac08dfc87d4ce81607edde7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3129fd986f81dd4418c14ff99f1b55e674ecc2ecd08178f02956c13c9c5e6bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecrets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecrets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecrets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d82ddb76fdf48598073cc96944eb70861ece5b27520a2c57080675e4a61abb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileSecretsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecretsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__821733d4ac5745b67e421b0b703ff220224d1aca2e14f8828044b0f0d1cfcea9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVaultCertificates")
    def put_vault_certificates(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileSecretsVaultCertificates", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e748c96158b040346c48eba5a57554848cb6141ecd7b2de47d47015b6be400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVaultCertificates", [value]))

    @jsii.member(jsii_name="resetVaultCertificates")
    def reset_vault_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultCertificates", []))

    @builtins.property
    @jsii.member(jsii_name="vaultCertificates")
    def vault_certificates(
        self,
    ) -> "VirtualMachineOsProfileSecretsVaultCertificatesList":
        return typing.cast("VirtualMachineOsProfileSecretsVaultCertificatesList", jsii.get(self, "vaultCertificates"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultCertificatesInput")
    def vault_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecretsVaultCertificates"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileSecretsVaultCertificates"]]], jsii.get(self, "vaultCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d06f8b1b6d1072a04ff6d065edd736b3c2e0ca862da01e2ac783d2d9925eef14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineOsProfileSecrets, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineOsProfileSecrets, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineOsProfileSecrets, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5026ad0889db4315f511cb103b05d7c37a62119fd9738ac4a4e2f7cb152e6a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecretsVaultCertificates",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_url": "certificateUrl",
        "certificate_store": "certificateStore",
    },
)
class VirtualMachineOsProfileSecretsVaultCertificates:
    def __init__(
        self,
        *,
        certificate_url: builtins.str,
        certificate_store: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_url VirtualMachine#certificate_url}.
        :param certificate_store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_store VirtualMachine#certificate_store}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d3601cb77aa4dd5560f383bc65039d69d565650d7a963b1b69272d13a3aedf)
            check_type(argname="argument certificate_url", value=certificate_url, expected_type=type_hints["certificate_url"])
            check_type(argname="argument certificate_store", value=certificate_store, expected_type=type_hints["certificate_store"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_url": certificate_url,
        }
        if certificate_store is not None:
            self._values["certificate_store"] = certificate_store

    @builtins.property
    def certificate_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_url VirtualMachine#certificate_url}.'''
        result = self._values.get("certificate_url")
        assert result is not None, "Required property 'certificate_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_store(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_store VirtualMachine#certificate_store}.'''
        result = self._values.get("certificate_store")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileSecretsVaultCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileSecretsVaultCertificatesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecretsVaultCertificatesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d977bd4f5c5c0a3f19b4769d02462538cb1cb0bca61ff318b8934e8455fd9f2b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineOsProfileSecretsVaultCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e623831d0231c8b05eda233e5d50b6d65c196b94bf2f78b5980c11a56081de83)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineOsProfileSecretsVaultCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01734fe43bc43a99fce98b4136e3391d2ca535ec86c3a542ac46725b6c5c8100)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4939a99f639d793e4fe6ca48045466f3dabf1515597743bf6c5545c4d7efab02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6231a9ee56a2aafbb8a1520bbb995693179fae5458ed0378be1c2632012d6361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecretsVaultCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecretsVaultCertificates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecretsVaultCertificates]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb2323980549a12239cad329ec1d208a31d196fca1beaeb8e03c52ceacbd45f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileSecretsVaultCertificatesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileSecretsVaultCertificatesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90a3ca0bff3e3179de006f713abba920c6242ff7f7de07d1bb9fc83221565556)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateStore")
    def reset_certificate_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateStore", []))

    @builtins.property
    @jsii.member(jsii_name="certificateStoreInput")
    def certificate_store_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateUrlInput")
    def certificate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateStore")
    def certificate_store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStore"))

    @certificate_store.setter
    def certificate_store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c374c16423fff1e4f0302562a11e1839a1c05684bd7be0c92abe832322f929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateStore", value)

    @builtins.property
    @jsii.member(jsii_name="certificateUrl")
    def certificate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUrl"))

    @certificate_url.setter
    def certificate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b43f6aed9dec323ff567feee736ddc6286826a27a826724f63b9b8a311875d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc11cb9edbacd8630011552be499efcc4c8ce6a0475df7b6b868a776f02b5857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_unattend_config": "additionalUnattendConfig",
        "enable_automatic_upgrades": "enableAutomaticUpgrades",
        "provision_vm_agent": "provisionVmAgent",
        "timezone": "timezone",
        "winrm": "winrm",
    },
)
class VirtualMachineOsProfileWindowsConfig:
    def __init__(
        self,
        *,
        additional_unattend_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable_automatic_upgrades: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timezone: typing.Optional[builtins.str] = None,
        winrm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileWindowsConfigWinrm", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_unattend_config: additional_unattend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#additional_unattend_config VirtualMachine#additional_unattend_config}
        :param enable_automatic_upgrades: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enable_automatic_upgrades VirtualMachine#enable_automatic_upgrades}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#provision_vm_agent VirtualMachine#provision_vm_agent}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timezone VirtualMachine#timezone}.
        :param winrm: winrm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#winrm VirtualMachine#winrm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b703a6a5ce7526b343d2d779685673bd2dfe4d299f73bf65aedb25a2bd047b47)
            check_type(argname="argument additional_unattend_config", value=additional_unattend_config, expected_type=type_hints["additional_unattend_config"])
            check_type(argname="argument enable_automatic_upgrades", value=enable_automatic_upgrades, expected_type=type_hints["enable_automatic_upgrades"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument winrm", value=winrm, expected_type=type_hints["winrm"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_unattend_config is not None:
            self._values["additional_unattend_config"] = additional_unattend_config
        if enable_automatic_upgrades is not None:
            self._values["enable_automatic_upgrades"] = enable_automatic_upgrades
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if timezone is not None:
            self._values["timezone"] = timezone
        if winrm is not None:
            self._values["winrm"] = winrm

    @builtins.property
    def additional_unattend_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig"]]]:
        '''additional_unattend_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#additional_unattend_config VirtualMachine#additional_unattend_config}
        '''
        result = self._values.get("additional_unattend_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig"]]], result)

    @builtins.property
    def enable_automatic_upgrades(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#enable_automatic_upgrades VirtualMachine#enable_automatic_upgrades}.'''
        result = self._values.get("enable_automatic_upgrades")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#provision_vm_agent VirtualMachine#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#timezone VirtualMachine#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def winrm(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigWinrm"]]]:
        '''winrm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#winrm VirtualMachine#winrm}
        '''
        result = self._values.get("winrm")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigWinrm"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileWindowsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig",
    jsii_struct_bases=[],
    name_mapping={
        "component": "component",
        "content": "content",
        "pass_": "pass",
        "setting_name": "settingName",
    },
)
class VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig:
    def __init__(
        self,
        *,
        component: builtins.str,
        content: builtins.str,
        pass_: builtins.str,
        setting_name: builtins.str,
    ) -> None:
        '''
        :param component: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#component VirtualMachine#component}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#content VirtualMachine#content}.
        :param pass_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#pass VirtualMachine#pass}.
        :param setting_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#setting_name VirtualMachine#setting_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b92b9474ac43be85bbaeca0efff563a59e7d004b7b1508173f8454b4f766056)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument pass_", value=pass_, expected_type=type_hints["pass_"])
            check_type(argname="argument setting_name", value=setting_name, expected_type=type_hints["setting_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "component": component,
            "content": content,
            "pass_": pass_,
            "setting_name": setting_name,
        }

    @builtins.property
    def component(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#component VirtualMachine#component}.'''
        result = self._values.get("component")
        assert result is not None, "Required property 'component' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#content VirtualMachine#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pass_(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#pass VirtualMachine#pass}.'''
        result = self._values.get("pass_")
        assert result is not None, "Required property 'pass_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#setting_name VirtualMachine#setting_name}.'''
        result = self._values.get("setting_name")
        assert result is not None, "Required property 'setting_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__582849892eaec44d5911539e8548ca5a4036cc81b23047d1a8445ebff3644b6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40a7348a70e04ce883ec46d4439fd8b0d450578839e9f7bd86bbc614e3bdd37)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3a21adc621de317f56655a562faacc4eea9d8258bd1b44aca11f3ca73cb430)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b34f67ab015ae25d624330390904cbba2e3a1825a244f08a26cf980e9ff91770)
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
            type_hints = typing.get_type_hints(_typecheckingstub__68792ee00f93e957d99829dc8846fc165613ae89fa9740b3fc040500f532d39a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__214dbf99d41800a72ca9723f36d52fda60ae7285ef42aeb9e228ecfed0dd1642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6711dc6992b77bef827ac942f3d16ad67d8e9eb1e843d30bc2003a4fe1420634)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="componentInput")
    def component_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="passInput")
    def pass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passInput"))

    @builtins.property
    @jsii.member(jsii_name="settingNameInput")
    def setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "component"))

    @component.setter
    def component(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eefb86ffbfe461a23d0fd8cf390054163fc8347e01371638ce4d2efc20b9f93a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "component", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__604f3f4083fc12b0868def3c6e711f28dbf843a1a7553d7e5767b7319bc9c866)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="pass")
    def pass_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pass"))

    @pass_.setter
    def pass_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a38ea48c25f4385fd3c3fd835dfaa4544f9334a6c85450503b60df831e1bd6fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pass", value)

    @builtins.property
    @jsii.member(jsii_name="settingName")
    def setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingName"))

    @setting_name.setter
    def setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287854a8e77b70a0b0e2d5961589ba86cbfc3ba3f2b4ac138917cf27347a12c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05eaee35c0a8ab074fbd83aefe8cb0c99487e717c20bc8b9991bf0d1bdcac381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileWindowsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a46c558e843f992098762e89ff2b36e97429b48b4b4f5b4a710b4435c01d46b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalUnattendConfig")
    def put_additional_unattend_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd4dcbaa4ca2ce3cd07b36c1b43eeee5efccd946509dab11981fdada6647e53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalUnattendConfig", [value]))

    @jsii.member(jsii_name="putWinrm")
    def put_winrm(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["VirtualMachineOsProfileWindowsConfigWinrm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116acad09fefce139a83efa948ae3a17388059c228218666d804614a17252de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWinrm", [value]))

    @jsii.member(jsii_name="resetAdditionalUnattendConfig")
    def reset_additional_unattend_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalUnattendConfig", []))

    @jsii.member(jsii_name="resetEnableAutomaticUpgrades")
    def reset_enable_automatic_upgrades(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpgrades", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetWinrm")
    def reset_winrm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrm", []))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendConfig")
    def additional_unattend_config(
        self,
    ) -> VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigList:
        return typing.cast(VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigList, jsii.get(self, "additionalUnattendConfig"))

    @builtins.property
    @jsii.member(jsii_name="winrm")
    def winrm(self) -> "VirtualMachineOsProfileWindowsConfigWinrmList":
        return typing.cast("VirtualMachineOsProfileWindowsConfigWinrmList", jsii.get(self, "winrm"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendConfigInput")
    def additional_unattend_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]], jsii.get(self, "additionalUnattendConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpgradesInput")
    def enable_automatic_upgrades_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutomaticUpgradesInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgentInput")
    def provision_vm_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "provisionVmAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmInput")
    def winrm_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigWinrm"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["VirtualMachineOsProfileWindowsConfigWinrm"]]], jsii.get(self, "winrmInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpgrades")
    def enable_automatic_upgrades(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutomaticUpgrades"))

    @enable_automatic_upgrades.setter
    def enable_automatic_upgrades(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ec038e2a3ea780ac95b0df398fc5e68666600c9d707eae170df21d1f818636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticUpgrades", value)

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgent")
    def provision_vm_agent(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "provisionVmAgent"))

    @provision_vm_agent.setter
    def provision_vm_agent(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__083de2052e8f5a4c57212821f61d7d331911c5c9d2d603f4d4fdaa4669c7388c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__336a7c596d937b6e646f1fcf6d523910c3d0906dab37a5495e70dd457c49a1a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineOsProfileWindowsConfig]:
        return typing.cast(typing.Optional[VirtualMachineOsProfileWindowsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineOsProfileWindowsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17afa49b0c8f5225a0a6859a84c2014435c5f97b1581061188e18b02e9c02713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigWinrm",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol", "certificate_url": "certificateUrl"},
)
class VirtualMachineOsProfileWindowsConfigWinrm:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        certificate_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#protocol VirtualMachine#protocol}.
        :param certificate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_url VirtualMachine#certificate_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa801a42fdc1c0661df18e2d565861a857278ef515aeca3272959e48a532ff7)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument certificate_url", value=certificate_url, expected_type=type_hints["certificate_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }
        if certificate_url is not None:
            self._values["certificate_url"] = certificate_url

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#protocol VirtualMachine#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#certificate_url VirtualMachine#certificate_url}.'''
        result = self._values.get("certificate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineOsProfileWindowsConfigWinrm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineOsProfileWindowsConfigWinrmList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigWinrmList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__250c879337377dc994b1c5ac4a328f1ea819019b05626ad8cbed029d567df341)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineOsProfileWindowsConfigWinrmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bfa94f4cce48a8dd965e26dc0e8d57b9635e0ab543ab5e947ddb054194cc5ca)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineOsProfileWindowsConfigWinrmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593200d3882259e71ab90a48c5ea7bcf54916e0eeef6f75c3e58ec1cc8ff8fa5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ea181fef0fe76a15559f042fbb956bdd8519c2f036c1b34862f16a4767dd331)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1832a1200a02698bdd0dc551642bab6b7964b06b2c7f514ea78928fe8d5d23c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigWinrm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigWinrm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigWinrm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ffa9652d6ca0b662ed00261faa148494dbcb31404cf720e2f75097026f1eaae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineOsProfileWindowsConfigWinrmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineOsProfileWindowsConfigWinrmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff4820194a8e5dfbd5e0b1a91b831d31bfbad5d8a717bfa50b2f9c7e7839bd88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateUrl")
    def reset_certificate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateUrl", []))

    @builtins.property
    @jsii.member(jsii_name="certificateUrlInput")
    def certificate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateUrl")
    def certificate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUrl"))

    @certificate_url.setter
    def certificate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c3cdc5ea646f8fa3118d5a542648529cf6d8ce9c984442084c83143f5076c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742d8d6ee4f328e9298008e233d488ae5e083f10b1d170f4470e8d2b1024894c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fe049c9382a143ea12dcb5c15179617eb354798131cbe6f44991dc3d6a8737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachinePlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class VirtualMachinePlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#product VirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454b4e3dd2273ac6976cfa4e5949904e2401d40a7a05d3dba38a17b83e78013e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "product": product,
            "publisher": publisher,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#product VirtualMachine#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachinePlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachinePlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachinePlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1157e8173c99d58b549ba7cb409451cebfe5fbe3a3a29aa9785d54dfccceca42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c84b0853de2d77a07c1d322d88689edca6cc4079ae47762f69225611b12efa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c607727c0fa7ec7d49867a6cb8e871ca3b8df6b670c7c8169949d1b92f73de14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459f6241964750e07cb89e71489aaf9310ede923200fab7f4f9e4e464b82677e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachinePlan]:
        return typing.cast(typing.Optional[VirtualMachinePlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VirtualMachinePlan]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af0aecf80b95cc419ed62e2c84d8740844c2bd70f795402a3d081595b941586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "create_option": "createOption",
        "lun": "lun",
        "name": "name",
        "caching": "caching",
        "disk_size_gb": "diskSizeGb",
        "managed_disk_id": "managedDiskId",
        "managed_disk_type": "managedDiskType",
        "vhd_uri": "vhdUri",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class VirtualMachineStorageDataDisk:
    def __init__(
        self,
        *,
        create_option: builtins.str,
        lun: jsii.Number,
        name: builtins.str,
        caching: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
        vhd_uri: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create_option VirtualMachine#create_option}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#lun VirtualMachine#lun}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#caching VirtualMachine#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disk_size_gb VirtualMachine#disk_size_gb}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_id VirtualMachine#managed_disk_id}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_type VirtualMachine#managed_disk_type}.
        :param vhd_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vhd_uri VirtualMachine#vhd_uri}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#write_accelerator_enabled VirtualMachine#write_accelerator_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124f5ac147c8c65c9769eae8ba0712f82d73989373aefd083d1f148e277c6c9e)
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument managed_disk_id", value=managed_disk_id, expected_type=type_hints["managed_disk_id"])
            check_type(argname="argument managed_disk_type", value=managed_disk_type, expected_type=type_hints["managed_disk_type"])
            check_type(argname="argument vhd_uri", value=vhd_uri, expected_type=type_hints["vhd_uri"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "create_option": create_option,
            "lun": lun,
            "name": name,
        }
        if caching is not None:
            self._values["caching"] = caching
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if managed_disk_id is not None:
            self._values["managed_disk_id"] = managed_disk_id
        if managed_disk_type is not None:
            self._values["managed_disk_type"] = managed_disk_type
        if vhd_uri is not None:
            self._values["vhd_uri"] = vhd_uri
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create_option VirtualMachine#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#lun VirtualMachine#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#caching VirtualMachine#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disk_size_gb VirtualMachine#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_id VirtualMachine#managed_disk_id}.'''
        result = self._values.get("managed_disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_type VirtualMachine#managed_disk_type}.'''
        result = self._values.get("managed_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vhd_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vhd_uri VirtualMachine#vhd_uri}.'''
        result = self._values.get("vhd_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#write_accelerator_enabled VirtualMachine#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineStorageDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineStorageDataDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageDataDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__253d88d465efeb8cda0b4e063914317fda7ef400fd3307b75b7c663f9e1ae4f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VirtualMachineStorageDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e333c3e179b067a92a20423f00ed418de4693d4243d633e931e17705726044)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineStorageDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c4c21aa1827818e9c81c2b43398c343ba9784d64d1f8c69963ba07edeeecde)
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
            type_hints = typing.get_type_hints(_typecheckingstub__903629699a7a72c3256f58cb75a23471edfccdbc8511540c487bc43b5c2a0e10)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2062619a99ed0ea7067a28fa78fa1b5b629ab93d1cdfa028ecc4629892e3d6f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineStorageDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineStorageDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineStorageDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51c5fe280f21fc44c6071e4a26b05e646bd79c2179c2ad8c4b3a23cbe069fae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineStorageDataDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce81f298a73c85559a49e73966446a56737e847c14c64200f7087885e7fa1171)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetManagedDiskId")
    def reset_managed_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskId", []))

    @jsii.member(jsii_name="resetManagedDiskType")
    def reset_managed_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskType", []))

    @jsii.member(jsii_name="resetVhdUri")
    def reset_vhd_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhdUri", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskIdInput")
    def managed_disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskTypeInput")
    def managed_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="vhdUriInput")
    def vhd_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vhdUriInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabledInput")
    def write_accelerator_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "writeAcceleratorEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__122dd05805abae724002840e5419efe9ca35fc741af17dff99ab0efe0e5e7f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b4da2257ee383ef59a62b5f46589ad4049a52cae9ed9c273a52d45cf302033c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709d899d5497b6fcdb3ae8293e9c9e555105d894d4818071888891764175ab7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b636d933e66071b200ac4558d107ca0db2d7e8beea6ea4380e77fd6949599367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskId")
    def managed_disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskId"))

    @managed_disk_id.setter
    def managed_disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ff5024819c01af905506e7161cd584f3aa840f3ec7dac728fcaa3a9ed7b6bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskId", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskType")
    def managed_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskType"))

    @managed_disk_type.setter
    def managed_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242e7fb1999517dd34ac89777fb6c0edeb951eb54e81c5aef3e9fcfd671d1720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29721b2e4e0b7a1bef57a2e8670901415f6ee9fb204f32626a3b2f4249ba9f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="vhdUri")
    def vhd_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vhdUri"))

    @vhd_uri.setter
    def vhd_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb1cc84f5247b4eaeda8bdda9863ad6a4f172171db32e102179b84786ba1091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vhdUri", value)

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabled")
    def write_accelerator_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "writeAcceleratorEnabled"))

    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09cad333de6a646ce81c1b6372a196efbb7deefef99b45b2a9788649ddc5064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineStorageDataDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineStorageDataDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineStorageDataDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05731e9dbfe1fab3c35cff3912bedfa33d48c13c2ac3aa0078e93f78d8b8fa19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class VirtualMachineStorageImageReference:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#offer VirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#sku VirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#version VirtualMachine#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__750cc9e1c77d203875f81222e2909a6468d22b29a9d685241e4f0fe84cc9522d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if offer is not None:
            self._values["offer"] = offer
        if publisher is not None:
            self._values["publisher"] = publisher
        if sku is not None:
            self._values["sku"] = sku
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#id VirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#offer VirtualMachine#offer}.'''
        result = self._values.get("offer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#publisher VirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#sku VirtualMachine#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#version VirtualMachine#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineStorageImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineStorageImageReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36df49dcb7234f5b5472c5c14f0825958e531b7e271d5da61fb9cac4f232c508)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOffer")
    def reset_offer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffer", []))

    @jsii.member(jsii_name="resetPublisher")
    def reset_publisher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublisher", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac81e9735dc643e0f52cc60ac07e0493a00d7c8e2a7934877a2f04344e43cef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b397349264891e7b5205494faf7722932d917adff703cfefd6cbfecd48b991f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccf43ad6c212eed2812f4a4ba5a89d3d3eb1e5b8c5b56d0fc2cf0b453e713062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf63559266161cf1cfe9d896371ae204aecc795b4741e0fe2a797d7cc772c4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d987a6da6c04100123e89c5d7dc935900bd3c49e9d1ad4a397384f25e4b2485d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineStorageImageReference]:
        return typing.cast(typing.Optional[VirtualMachineStorageImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineStorageImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e158ab02cb7b3f3ded362d07e29b40a47c56a8cae74277a49b5233cfcdf55b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "create_option": "createOption",
        "name": "name",
        "caching": "caching",
        "disk_size_gb": "diskSizeGb",
        "image_uri": "imageUri",
        "managed_disk_id": "managedDiskId",
        "managed_disk_type": "managedDiskType",
        "os_type": "osType",
        "vhd_uri": "vhdUri",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class VirtualMachineStorageOsDisk:
    def __init__(
        self,
        *,
        create_option: builtins.str,
        name: builtins.str,
        caching: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        image_uri: typing.Optional[builtins.str] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        vhd_uri: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create_option VirtualMachine#create_option}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#caching VirtualMachine#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disk_size_gb VirtualMachine#disk_size_gb}.
        :param image_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#image_uri VirtualMachine#image_uri}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_id VirtualMachine#managed_disk_id}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_type VirtualMachine#managed_disk_type}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_type VirtualMachine#os_type}.
        :param vhd_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vhd_uri VirtualMachine#vhd_uri}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#write_accelerator_enabled VirtualMachine#write_accelerator_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__288fec8d63165a4bb580692ae12b53a7449a3899fe0da90854ef361304d60773)
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument managed_disk_id", value=managed_disk_id, expected_type=type_hints["managed_disk_id"])
            check_type(argname="argument managed_disk_type", value=managed_disk_type, expected_type=type_hints["managed_disk_type"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument vhd_uri", value=vhd_uri, expected_type=type_hints["vhd_uri"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "create_option": create_option,
            "name": name,
        }
        if caching is not None:
            self._values["caching"] = caching
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if managed_disk_id is not None:
            self._values["managed_disk_id"] = managed_disk_id
        if managed_disk_type is not None:
            self._values["managed_disk_type"] = managed_disk_type
        if os_type is not None:
            self._values["os_type"] = os_type
        if vhd_uri is not None:
            self._values["vhd_uri"] = vhd_uri
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create_option VirtualMachine#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#name VirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#caching VirtualMachine#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#disk_size_gb VirtualMachine#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#image_uri VirtualMachine#image_uri}.'''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_id VirtualMachine#managed_disk_id}.'''
        result = self._values.get("managed_disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#managed_disk_type VirtualMachine#managed_disk_type}.'''
        result = self._values.get("managed_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#os_type VirtualMachine#os_type}.'''
        result = self._values.get("os_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vhd_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#vhd_uri VirtualMachine#vhd_uri}.'''
        result = self._values.get("vhd_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#write_accelerator_enabled VirtualMachine#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineStorageOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineStorageOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineStorageOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb67071117c67d2f240f4b33c70c093955c0ef2332085b7efbfb4f284628d409)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetImageUri")
    def reset_image_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageUri", []))

    @jsii.member(jsii_name="resetManagedDiskId")
    def reset_managed_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskId", []))

    @jsii.member(jsii_name="resetManagedDiskType")
    def reset_managed_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskType", []))

    @jsii.member(jsii_name="resetOsType")
    def reset_os_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsType", []))

    @jsii.member(jsii_name="resetVhdUri")
    def reset_vhd_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhdUri", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUriInput")
    def image_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskIdInput")
    def managed_disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskTypeInput")
    def managed_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="vhdUriInput")
    def vhd_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vhdUriInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabledInput")
    def write_accelerator_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "writeAcceleratorEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7069649c4955d810d7abe1d9bcf4aa0e2da125abadb16e4688f33cf6cd4e56c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db1f1a46166ea586b053d524796b33e69aa01d256dbddcef2eed8e0a5fb763d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfdc5ad370ad0226ed4a5f6ffa95f91089c63ea2872129dd59ad073b6bdf0df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad01ea7a21a50cf9d6b75ba61beac0c361aed903f6d459a09fa0481c838f6fa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskId")
    def managed_disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskId"))

    @managed_disk_id.setter
    def managed_disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7b7fbd55e69a750cbabb7f48b1a2e6581c91fd260bdb0f1e4efe2ba062e104f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskId", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskType")
    def managed_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskType"))

    @managed_disk_type.setter
    def managed_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e00beee14d5ad9c2be93df42d2b73f6564490fe372d4f6bf23e150f2b4daa58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7204cdc279d8b8acb3574be7f896027247936b22748ad951f293fc8a700105c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b945b588577c6ad4927c67ced0ef0ac45bbbbf85a542b063c7175e022d08947c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="vhdUri")
    def vhd_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vhdUri"))

    @vhd_uri.setter
    def vhd_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d380ed32b9532c7ed6c3643d2e27ad8ea7b499b41d5afd6d77be121fbca99a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vhdUri", value)

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabled")
    def write_accelerator_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "writeAcceleratorEnabled"))

    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ffcdfe465952c23bcf02c8e9dfd59ccf166877cefc908670bb64e66bdfd223)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineStorageOsDisk]:
        return typing.cast(typing.Optional[VirtualMachineStorageOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineStorageOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f710806a9d62598d612ba06a23f6ca3a282e7377e33139e4a1550d6c1aca5c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create VirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete VirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#read VirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#update VirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34295a1491b116d8321c31b329796ad145d46168fb9adf1f59c97a63dd150ce)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#create VirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#delete VirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#read VirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/virtual_machine#update VirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.virtualMachine.VirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7552b013d6a06842474fb9e83e66034e1ffa4b00dc51cec52873960221a3b853)
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
            type_hints = typing.get_type_hints(_typecheckingstub__844591d8af1ae4d77bb787039fbabeb19753d2b77d1621840e2631c55e5779fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78e62f25822cce26c396f6500aece5aef3fc98cd3ce1c672b20dda5242a3a776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03de814b34b6b0edeb3b8f0daf867b72d20cecfd3422d6109e5ccc861b4c14b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__185ee6260094d5e0788e38d0560b477c4f4f9ef724a7fd25f367e484f0d7e533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f44b8d46e3bc280fd548f53369e957bc9d78277817c1ef96622bde41d6efcd58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualMachine",
    "VirtualMachineBootDiagnostics",
    "VirtualMachineBootDiagnosticsOutputReference",
    "VirtualMachineConfig",
    "VirtualMachineIdentity",
    "VirtualMachineIdentityOutputReference",
    "VirtualMachineOsProfile",
    "VirtualMachineOsProfileLinuxConfig",
    "VirtualMachineOsProfileLinuxConfigOutputReference",
    "VirtualMachineOsProfileLinuxConfigSshKeys",
    "VirtualMachineOsProfileLinuxConfigSshKeysList",
    "VirtualMachineOsProfileLinuxConfigSshKeysOutputReference",
    "VirtualMachineOsProfileOutputReference",
    "VirtualMachineOsProfileSecrets",
    "VirtualMachineOsProfileSecretsList",
    "VirtualMachineOsProfileSecretsOutputReference",
    "VirtualMachineOsProfileSecretsVaultCertificates",
    "VirtualMachineOsProfileSecretsVaultCertificatesList",
    "VirtualMachineOsProfileSecretsVaultCertificatesOutputReference",
    "VirtualMachineOsProfileWindowsConfig",
    "VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig",
    "VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigList",
    "VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfigOutputReference",
    "VirtualMachineOsProfileWindowsConfigOutputReference",
    "VirtualMachineOsProfileWindowsConfigWinrm",
    "VirtualMachineOsProfileWindowsConfigWinrmList",
    "VirtualMachineOsProfileWindowsConfigWinrmOutputReference",
    "VirtualMachinePlan",
    "VirtualMachinePlanOutputReference",
    "VirtualMachineStorageDataDisk",
    "VirtualMachineStorageDataDiskList",
    "VirtualMachineStorageDataDiskOutputReference",
    "VirtualMachineStorageImageReference",
    "VirtualMachineStorageImageReferenceOutputReference",
    "VirtualMachineStorageOsDisk",
    "VirtualMachineStorageOsDiskOutputReference",
    "VirtualMachineTimeouts",
    "VirtualMachineTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__5b32eebbe99d867007f36b3b462f3df6ee081f57e34fb55d036a924a3338c05b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    network_interface_ids: typing.Sequence[builtins.str],
    resource_group_name: builtins.str,
    storage_os_disk: typing.Union[VirtualMachineStorageOsDisk, typing.Dict[builtins.str, typing.Any]],
    vm_size: builtins.str,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[VirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_data_disks_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delete_os_disk_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[VirtualMachineIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    license_type: typing.Optional[builtins.str] = None,
    os_profile: typing.Optional[typing.Union[VirtualMachineOsProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    os_profile_linux_config: typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    os_profile_secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileSecrets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    os_profile_windows_config: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    plan: typing.Optional[typing.Union[VirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    primary_network_interface_id: typing.Optional[builtins.str] = None,
    storage_data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineStorageDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storage_image_reference: typing.Optional[typing.Union[VirtualMachineStorageImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    zones: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__329d7d0f1b9263f70b8e8ab7403c77dba3ae812fb6dac16a14fa344fc7a87b55(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileSecrets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__206c12f82e66ceefe6812bf6d48924d5ebffed887711e1727a76fb5a46480db8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineStorageDataDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653a671efd4c547c80bd7359b453f84a6a84c72949c01c9f255d7a020251be84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152fece75e4bb18445089a664ce974d82808d80fc8791e816af4fcee49541b96(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3985908be8a679cd2ee8307b8e1cf461435c80457999a8aaf417ec56a4c2b2ff(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d65efc12519ad2eeb8f36d4e02503eb85cb85694b9d7ba44ebf1773ffebb738(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d042ee59f0ce3a482ff49d7fda2b3db11735f1c89dde20bb95e961d40e30ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc39afcaf326aad8d0448d54e0e6fcc2b876a17a3cfa4ee8a3c0b0d87c683b52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391c0d2eacdb8f5c4a05e2b77ad9d1fc397f92a91a3d1c9038bbd892d64b411b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3dbef4e98e6bdd22144ac5f4096330e98d656669af45e1b6ea4c0d40d7f1516(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec3793fd6c38628b06c664dfa9c79e98ca6ba97f426aac40721ad78e91da9c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53344f66e13e64e694b4b58bcc50929ae8c9d660a2c909e1d8daaeca27d0496f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0859a547fe7aae200063c26a374f9c5b8fa3662cad19df05ab0ef14633e43163(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90adbc1e15b58ac4657a045c2ef069a9907116e974c8742c5d6e38b039c90604(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd7c62c1ec80a6dfde9e6161455959a72cf880b04b02b593767f3b41456a377(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9750aa868242b1172896197fab60f4118fd48ae9bebedfad5f1ae09baf48928(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    storage_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca47811b5e2f5f87c64492ad4f3a9e96a1cc768e69b0b05dc66e7e6d48a8426(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a33979b7ee1a3c0b56ab1954eb6c2848ef0c9c6d9fd0a25d6913e2f4a4a493f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc55ab87166a7db743eac4ba3fef2a8f59410d8e6e1f6c8f8e9f650bc054f277(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7282729197827644525a8c8f729965a1d48958b5621557a4137a8c204c39fa5(
    value: typing.Optional[VirtualMachineBootDiagnostics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91cfcaafd79175e3228e17088bbea9e32ff929d1e3360ca9eb885c3b675ebfd(
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
    network_interface_ids: typing.Sequence[builtins.str],
    resource_group_name: builtins.str,
    storage_os_disk: typing.Union[VirtualMachineStorageOsDisk, typing.Dict[builtins.str, typing.Any]],
    vm_size: builtins.str,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[VirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_data_disks_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delete_os_disk_on_termination: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    identity: typing.Optional[typing.Union[VirtualMachineIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    license_type: typing.Optional[builtins.str] = None,
    os_profile: typing.Optional[typing.Union[VirtualMachineOsProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    os_profile_linux_config: typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    os_profile_secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileSecrets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    os_profile_windows_config: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    plan: typing.Optional[typing.Union[VirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    primary_network_interface_id: typing.Optional[builtins.str] = None,
    storage_data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineStorageDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storage_image_reference: typing.Optional[typing.Union[VirtualMachineStorageImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[VirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    zones: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eb0765fe601dfd1ffcf980d4b7b2f2347135944be95d92bce460c79ba73d6b2(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b96fba6a326f539a2a95f32f4f9367032a59022c4df2b06561a9ca8cdf25bd94(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1a18cbd1c7fe76e0ba18e7ab08aac5d6241dc2355a72565ef2c7439d6d8082(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eadd3d1b9a08d9746401e6762ec7e9d5feffc2e2ccda3f90a5b40f7c4850f7b(
    value: typing.Optional[VirtualMachineIdentity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3082eab789e827b6495a1fa1e8412d979196a9bfa0c31f517b55ad666371c8e3(
    *,
    admin_username: builtins.str,
    computer_name: builtins.str,
    admin_password: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71131c4044c9332b15c94f599d1e2831707ecd15d65c872c23e18dcb07ba09d(
    *,
    disable_password_authentication: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ssh_keys: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb89f6cb6aa37cf1becb25351557df397f1dcc51f1d802fc36a42ed09e705a87(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e875614dc804e366d053e1b8bddd9bf6707a69766fb4f69a2a87a1b255f41da(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6b5839cdfc3f34a0027d0237ecee82e4e11e190f2578e42da7cd8fd0b47f1d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d9c4e01de1232266f7886ce823f533e0f4ccfa8600506d3adf4dfb14b6ce3c(
    value: typing.Optional[VirtualMachineOsProfileLinuxConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c03283ed69943a640a1c906af274a7df40220f54a507ddafd341ab1b04fecdf(
    *,
    key_data: builtins.str,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76825923fe4d26edfdf6394fff009c99195d0fc94d4b3079384a5f1444ef1c0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55989d699620572482ffb2726a7fd5a7ec477b71264e7a36020da8af3f545d8c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__163df36c3dae4088ddc39ccc2bea4b1afe2dc408c4b68db57015e89c603b8c4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf1e064a90dc205e4f67c6721c7399d3615a690bd64fd0a58cf1072f1ce04f6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a679068e1335418bd1b8532b3a2756faf6f2ee7e107f875e030c83e7f2f834(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b5d853d93a1f0ea28de14b519e07abff1a03642856401114d44ac9a230e498(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileLinuxConfigSshKeys]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f3c89e52698be068af228d9be191711db595005b24cf6db2093cb9f9bcb0c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723424d4e328eee5c9c93de6b2cb98556d96670fa49ae5a0e0d9b56f5b5fa684(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb97e22ddb39e902da9b62b5f1cb1da8545b17672675847b3e52bbc6e2e30b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bdabff09aa37118ed68c307a3ba1fe9e98bf0f429522c4078edb16a81d1954c(
    value: typing.Optional[typing.Union[VirtualMachineOsProfileLinuxConfigSshKeys, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e523b159d3b6fdcab9ea198fe62366d998e071aa4a74affe8a52a3a9674a9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3943770a0052d07b5eadada2950b3aae8712de5fa1e8a39aaed9ecba6c60e8c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29761a910680b355622302b6cd5ddaf784a33d3ac8372e35e4941cd3b4b49215(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563f7aeaa3ff2ca625b3a2bae5ad6e34fc3c01835d9fc6ad47e152166b55ede5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88a4cd045a1d69c4bce050617d52f3403b2c86b39c23ba80665e5168dc646b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64fca888011322b9ae6a58864576ff8c47e7f5ec3605c300ee518d048f39076(
    value: typing.Optional[VirtualMachineOsProfile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e0330dd10446d74c58384dfb8cb00ae60d8e6d5c0206442087125d399fa5fa(
    *,
    source_vault_id: builtins.str,
    vault_certificates: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31311ce4981fcabf8d71791ff1450a4e4e9e3d75f681b67553c7a6c8883d285f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297d72ea46fa2456d1400eed4969e6da95ecfd99443aef16a24af1a258ee337f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6bf5d676f9eb4787f8075fb52133fbb121fdc215dc670f2cdcf700c6b6394ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000c145b6d951be6e666c93621cc3fa06523bd4e0ac08dfc87d4ce81607edde7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3129fd986f81dd4418c14ff99f1b55e674ecc2ecd08178f02956c13c9c5e6bc3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d82ddb76fdf48598073cc96944eb70861ece5b27520a2c57080675e4a61abb4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecrets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__821733d4ac5745b67e421b0b703ff220224d1aca2e14f8828044b0f0d1cfcea9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e748c96158b040346c48eba5a57554848cb6141ecd7b2de47d47015b6be400(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d06f8b1b6d1072a04ff6d065edd736b3c2e0ca862da01e2ac783d2d9925eef14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5026ad0889db4315f511cb103b05d7c37a62119fd9738ac4a4e2f7cb152e6a7(
    value: typing.Optional[typing.Union[VirtualMachineOsProfileSecrets, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d3601cb77aa4dd5560f383bc65039d69d565650d7a963b1b69272d13a3aedf(
    *,
    certificate_url: builtins.str,
    certificate_store: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d977bd4f5c5c0a3f19b4769d02462538cb1cb0bca61ff318b8934e8455fd9f2b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e623831d0231c8b05eda233e5d50b6d65c196b94bf2f78b5980c11a56081de83(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01734fe43bc43a99fce98b4136e3391d2ca535ec86c3a542ac46725b6c5c8100(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4939a99f639d793e4fe6ca48045466f3dabf1515597743bf6c5545c4d7efab02(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6231a9ee56a2aafbb8a1520bbb995693179fae5458ed0378be1c2632012d6361(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb2323980549a12239cad329ec1d208a31d196fca1beaeb8e03c52ceacbd45f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileSecretsVaultCertificates]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a3ca0bff3e3179de006f713abba920c6242ff7f7de07d1bb9fc83221565556(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c374c16423fff1e4f0302562a11e1839a1c05684bd7be0c92abe832322f929(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b43f6aed9dec323ff567feee736ddc6286826a27a826724f63b9b8a311875d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc11cb9edbacd8630011552be499efcc4c8ce6a0475df7b6b868a776f02b5857(
    value: typing.Optional[typing.Union[VirtualMachineOsProfileSecretsVaultCertificates, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b703a6a5ce7526b343d2d779685673bd2dfe4d299f73bf65aedb25a2bd047b47(
    *,
    additional_unattend_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enable_automatic_upgrades: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timezone: typing.Optional[builtins.str] = None,
    winrm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b92b9474ac43be85bbaeca0efff563a59e7d004b7b1508173f8454b4f766056(
    *,
    component: builtins.str,
    content: builtins.str,
    pass_: builtins.str,
    setting_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582849892eaec44d5911539e8548ca5a4036cc81b23047d1a8445ebff3644b6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40a7348a70e04ce883ec46d4439fd8b0d450578839e9f7bd86bbc614e3bdd37(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3a21adc621de317f56655a562faacc4eea9d8258bd1b44aca11f3ca73cb430(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34f67ab015ae25d624330390904cbba2e3a1825a244f08a26cf980e9ff91770(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68792ee00f93e957d99829dc8846fc165613ae89fa9740b3fc040500f532d39a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214dbf99d41800a72ca9723f36d52fda60ae7285ef42aeb9e228ecfed0dd1642(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6711dc6992b77bef827ac942f3d16ad67d8e9eb1e843d30bc2003a4fe1420634(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eefb86ffbfe461a23d0fd8cf390054163fc8347e01371638ce4d2efc20b9f93a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__604f3f4083fc12b0868def3c6e711f28dbf843a1a7553d7e5767b7319bc9c866(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a38ea48c25f4385fd3c3fd835dfaa4544f9334a6c85450503b60df831e1bd6fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287854a8e77b70a0b0e2d5961589ba86cbfc3ba3f2b4ac138917cf27347a12c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05eaee35c0a8ab074fbd83aefe8cb0c99487e717c20bc8b9991bf0d1bdcac381(
    value: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46c558e843f992098762e89ff2b36e97429b48b4b4f5b4a710b4435c01d46b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd4dcbaa4ca2ce3cd07b36c1b43eeee5efccd946509dab11981fdada6647e53(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileWindowsConfigAdditionalUnattendConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116acad09fefce139a83efa948ae3a17388059c228218666d804614a17252de2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ec038e2a3ea780ac95b0df398fc5e68666600c9d707eae170df21d1f818636(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083de2052e8f5a4c57212821f61d7d331911c5c9d2d603f4d4fdaa4669c7388c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__336a7c596d937b6e646f1fcf6d523910c3d0906dab37a5495e70dd457c49a1a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17afa49b0c8f5225a0a6859a84c2014435c5f97b1581061188e18b02e9c02713(
    value: typing.Optional[VirtualMachineOsProfileWindowsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa801a42fdc1c0661df18e2d565861a857278ef515aeca3272959e48a532ff7(
    *,
    protocol: builtins.str,
    certificate_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250c879337377dc994b1c5ac4a328f1ea819019b05626ad8cbed029d567df341(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bfa94f4cce48a8dd965e26dc0e8d57b9635e0ab543ab5e947ddb054194cc5ca(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593200d3882259e71ab90a48c5ea7bcf54916e0eeef6f75c3e58ec1cc8ff8fa5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea181fef0fe76a15559f042fbb956bdd8519c2f036c1b34862f16a4767dd331(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1832a1200a02698bdd0dc551642bab6b7964b06b2c7f514ea78928fe8d5d23c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ffa9652d6ca0b662ed00261faa148494dbcb31404cf720e2f75097026f1eaae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineOsProfileWindowsConfigWinrm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff4820194a8e5dfbd5e0b1a91b831d31bfbad5d8a717bfa50b2f9c7e7839bd88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c3cdc5ea646f8fa3118d5a542648529cf6d8ce9c984442084c83143f5076c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742d8d6ee4f328e9298008e233d488ae5e083f10b1d170f4470e8d2b1024894c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fe049c9382a143ea12dcb5c15179617eb354798131cbe6f44991dc3d6a8737(
    value: typing.Optional[typing.Union[VirtualMachineOsProfileWindowsConfigWinrm, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454b4e3dd2273ac6976cfa4e5949904e2401d40a7a05d3dba38a17b83e78013e(
    *,
    name: builtins.str,
    product: builtins.str,
    publisher: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1157e8173c99d58b549ba7cb409451cebfe5fbe3a3a29aa9785d54dfccceca42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c84b0853de2d77a07c1d322d88689edca6cc4079ae47762f69225611b12efa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c607727c0fa7ec7d49867a6cb8e871ca3b8df6b670c7c8169949d1b92f73de14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__459f6241964750e07cb89e71489aaf9310ede923200fab7f4f9e4e464b82677e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af0aecf80b95cc419ed62e2c84d8740844c2bd70f795402a3d081595b941586(
    value: typing.Optional[VirtualMachinePlan],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124f5ac147c8c65c9769eae8ba0712f82d73989373aefd083d1f148e277c6c9e(
    *,
    create_option: builtins.str,
    lun: jsii.Number,
    name: builtins.str,
    caching: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    managed_disk_id: typing.Optional[builtins.str] = None,
    managed_disk_type: typing.Optional[builtins.str] = None,
    vhd_uri: typing.Optional[builtins.str] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253d88d465efeb8cda0b4e063914317fda7ef400fd3307b75b7c663f9e1ae4f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e333c3e179b067a92a20423f00ed418de4693d4243d633e931e17705726044(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c4c21aa1827818e9c81c2b43398c343ba9784d64d1f8c69963ba07edeeecde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903629699a7a72c3256f58cb75a23471edfccdbc8511540c487bc43b5c2a0e10(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2062619a99ed0ea7067a28fa78fa1b5b629ab93d1cdfa028ecc4629892e3d6f4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c5fe280f21fc44c6071e4a26b05e646bd79c2179c2ad8c4b3a23cbe069fae0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[VirtualMachineStorageDataDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce81f298a73c85559a49e73966446a56737e847c14c64200f7087885e7fa1171(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122dd05805abae724002840e5419efe9ca35fc741af17dff99ab0efe0e5e7f5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4da2257ee383ef59a62b5f46589ad4049a52cae9ed9c273a52d45cf302033c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709d899d5497b6fcdb3ae8293e9c9e555105d894d4818071888891764175ab7a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b636d933e66071b200ac4558d107ca0db2d7e8beea6ea4380e77fd6949599367(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ff5024819c01af905506e7161cd584f3aa840f3ec7dac728fcaa3a9ed7b6bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242e7fb1999517dd34ac89777fb6c0edeb951eb54e81c5aef3e9fcfd671d1720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29721b2e4e0b7a1bef57a2e8670901415f6ee9fb204f32626a3b2f4249ba9f5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb1cc84f5247b4eaeda8bdda9863ad6a4f172171db32e102179b84786ba1091(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d09cad333de6a646ce81c1b6372a196efbb7deefef99b45b2a9788649ddc5064(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05731e9dbfe1fab3c35cff3912bedfa33d48c13c2ac3aa0078e93f78d8b8fa19(
    value: typing.Optional[typing.Union[VirtualMachineStorageDataDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750cc9e1c77d203875f81222e2909a6468d22b29a9d685241e4f0fe84cc9522d(
    *,
    id: typing.Optional[builtins.str] = None,
    offer: typing.Optional[builtins.str] = None,
    publisher: typing.Optional[builtins.str] = None,
    sku: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36df49dcb7234f5b5472c5c14f0825958e531b7e271d5da61fb9cac4f232c508(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac81e9735dc643e0f52cc60ac07e0493a00d7c8e2a7934877a2f04344e43cef3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b397349264891e7b5205494faf7722932d917adff703cfefd6cbfecd48b991f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf43ad6c212eed2812f4a4ba5a89d3d3eb1e5b8c5b56d0fc2cf0b453e713062(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf63559266161cf1cfe9d896371ae204aecc795b4741e0fe2a797d7cc772c4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d987a6da6c04100123e89c5d7dc935900bd3c49e9d1ad4a397384f25e4b2485d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e158ab02cb7b3f3ded362d07e29b40a47c56a8cae74277a49b5233cfcdf55b4(
    value: typing.Optional[VirtualMachineStorageImageReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__288fec8d63165a4bb580692ae12b53a7449a3899fe0da90854ef361304d60773(
    *,
    create_option: builtins.str,
    name: builtins.str,
    caching: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    image_uri: typing.Optional[builtins.str] = None,
    managed_disk_id: typing.Optional[builtins.str] = None,
    managed_disk_type: typing.Optional[builtins.str] = None,
    os_type: typing.Optional[builtins.str] = None,
    vhd_uri: typing.Optional[builtins.str] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb67071117c67d2f240f4b33c70c093955c0ef2332085b7efbfb4f284628d409(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7069649c4955d810d7abe1d9bcf4aa0e2da125abadb16e4688f33cf6cd4e56c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db1f1a46166ea586b053d524796b33e69aa01d256dbddcef2eed8e0a5fb763d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfdc5ad370ad0226ed4a5f6ffa95f91089c63ea2872129dd59ad073b6bdf0df(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad01ea7a21a50cf9d6b75ba61beac0c361aed903f6d459a09fa0481c838f6fa6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b7fbd55e69a750cbabb7f48b1a2e6581c91fd260bdb0f1e4efe2ba062e104f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e00beee14d5ad9c2be93df42d2b73f6564490fe372d4f6bf23e150f2b4daa58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7204cdc279d8b8acb3574be7f896027247936b22748ad951f293fc8a700105c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b945b588577c6ad4927c67ced0ef0ac45bbbbf85a542b063c7175e022d08947c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d380ed32b9532c7ed6c3643d2e27ad8ea7b499b41d5afd6d77be121fbca99a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ffcdfe465952c23bcf02c8e9dfd59ccf166877cefc908670bb64e66bdfd223(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f710806a9d62598d612ba06a23f6ca3a282e7377e33139e4a1550d6c1aca5c3b(
    value: typing.Optional[VirtualMachineStorageOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34295a1491b116d8321c31b329796ad145d46168fb9adf1f59c97a63dd150ce(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7552b013d6a06842474fb9e83e66034e1ffa4b00dc51cec52873960221a3b853(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844591d8af1ae4d77bb787039fbabeb19753d2b77d1621840e2631c55e5779fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e62f25822cce26c396f6500aece5aef3fc98cd3ce1c672b20dda5242a3a776(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03de814b34b6b0edeb3b8f0daf867b72d20cecfd3422d6109e5ccc861b4c14b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__185ee6260094d5e0788e38d0560b477c4f4f9ef724a7fd25f367e484f0d7e533(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44b8d46e3bc280fd548f53369e957bc9d78277817c1ef96622bde41d6efcd58(
    value: typing.Optional[typing.Union[VirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
