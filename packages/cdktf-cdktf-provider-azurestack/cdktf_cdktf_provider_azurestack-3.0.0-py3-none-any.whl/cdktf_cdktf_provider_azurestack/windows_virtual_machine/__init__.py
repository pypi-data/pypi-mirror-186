'''
# `azurestack_windows_virtual_machine`

Refer to the Terraform Registory for docs: [`azurestack_windows_virtual_machine`](https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine).
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


class WindowsVirtualMachine(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine azurestack_windows_virtual_machine}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_password: builtins.str,
        admin_username: builtins.str,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["WindowsVirtualMachineOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["WindowsVirtualMachineAdditionalCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineAdditionalUnattendContent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union["WindowsVirtualMachineBootDiagnostics", typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        patch_mode: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
        winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[builtins.str, typing.Any]]]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine azurestack_windows_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#location WindowsVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#size WindowsVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#id WindowsVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.
        :param patch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f983246ee6b34a7374f8f8793e629fbcc60faf3f9bc8ad00e5d45aa9062e7b2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WindowsVirtualMachineConfig(
            admin_password=admin_password,
            admin_username=admin_username,
            location=location,
            name=name,
            network_interface_ids=network_interface_ids,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            size=size,
            additional_capabilities=additional_capabilities,
            additional_unattend_content=additional_unattend_content,
            allow_extension_operations=allow_extension_operations,
            availability_set_id=availability_set_id,
            boot_diagnostics=boot_diagnostics,
            computer_name=computer_name,
            custom_data=custom_data,
            enable_automatic_updates=enable_automatic_updates,
            encryption_at_host_enabled=encryption_at_host_enabled,
            eviction_policy=eviction_policy,
            extensions_time_budget=extensions_time_budget,
            id=id,
            license_type=license_type,
            max_bid_price=max_bid_price,
            patch_mode=patch_mode,
            plan=plan,
            priority=priority,
            provision_vm_agent=provision_vm_agent,
            secret=secret,
            source_image_id=source_image_id,
            source_image_reference=source_image_reference,
            tags=tags,
            timeouts=timeouts,
            timezone=timezone,
            virtual_machine_scale_set_id=virtual_machine_scale_set_id,
            winrm_listener=winrm_listener,
            zone=zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdditionalCapabilities")
    def put_additional_capabilities(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.
        '''
        value = WindowsVirtualMachineAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdditionalUnattendContent")
    def put_additional_unattend_content(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineAdditionalUnattendContent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba4602ee9f1e57ac88174525d2e431fc4c5806cadcf6e3a4625ffe0059002d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalUnattendContent", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.
        '''
        value = WindowsVirtualMachineBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.
        '''
        value = WindowsVirtualMachineOsDisk(
            caching=caching,
            storage_account_type=storage_account_type,
            diff_disk_settings=diff_disk_settings,
            disk_encryption_set_id=disk_encryption_set_id,
            disk_size_gb=disk_size_gb,
            name=name,
            write_accelerator_enabled=write_accelerator_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putOsDisk", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#product WindowsVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        '''
        value = WindowsVirtualMachinePlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2faff73a61bbabd23029bbd9b6d6295fff2e0c356e9988a031ae211ca3b226e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecret", [value]))

    @jsii.member(jsii_name="putSourceImageReference")
    def put_source_image_reference(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#version WindowsVirtualMachine#version}.
        '''
        value = WindowsVirtualMachineSourceImageReference(
            offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putSourceImageReference", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#create WindowsVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#read WindowsVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#update WindowsVirtualMachine#update}.
        '''
        value = WindowsVirtualMachineTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWinrmListener")
    def put_winrm_listener(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952659fd979e4913adbd31af84095953516ad20acec2d9d9a6570be2bb44b2fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWinrmListener", [value]))

    @jsii.member(jsii_name="resetAdditionalCapabilities")
    def reset_additional_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCapabilities", []))

    @jsii.member(jsii_name="resetAdditionalUnattendContent")
    def reset_additional_unattend_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalUnattendContent", []))

    @jsii.member(jsii_name="resetAllowExtensionOperations")
    def reset_allow_extension_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowExtensionOperations", []))

    @jsii.member(jsii_name="resetAvailabilitySetId")
    def reset_availability_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilitySetId", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetComputerName")
    def reset_computer_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputerName", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetEnableAutomaticUpdates")
    def reset_enable_automatic_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpdates", []))

    @jsii.member(jsii_name="resetEncryptionAtHostEnabled")
    def reset_encryption_at_host_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtHostEnabled", []))

    @jsii.member(jsii_name="resetEvictionPolicy")
    def reset_eviction_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionPolicy", []))

    @jsii.member(jsii_name="resetExtensionsTimeBudget")
    def reset_extensions_time_budget(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtensionsTimeBudget", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetMaxBidPrice")
    def reset_max_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBidPrice", []))

    @jsii.member(jsii_name="resetPatchMode")
    def reset_patch_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatchMode", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSourceImageId")
    def reset_source_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageId", []))

    @jsii.member(jsii_name="resetSourceImageReference")
    def reset_source_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetVirtualMachineScaleSetId")
    def reset_virtual_machine_scale_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachineScaleSetId", []))

    @jsii.member(jsii_name="resetWinrmListener")
    def reset_winrm_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmListener", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> "WindowsVirtualMachineAdditionalCapabilitiesOutputReference":
        return typing.cast("WindowsVirtualMachineAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContent")
    def additional_unattend_content(
        self,
    ) -> "WindowsVirtualMachineAdditionalUnattendContentList":
        return typing.cast("WindowsVirtualMachineAdditionalUnattendContentList", jsii.get(self, "additionalUnattendContent"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(self) -> "WindowsVirtualMachineBootDiagnosticsOutputReference":
        return typing.cast("WindowsVirtualMachineBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "WindowsVirtualMachineOsDiskOutputReference":
        return typing.cast("WindowsVirtualMachineOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "WindowsVirtualMachinePlanOutputReference":
        return typing.cast("WindowsVirtualMachinePlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddress")
    def public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddresses")
    def public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "WindowsVirtualMachineSecretList":
        return typing.cast("WindowsVirtualMachineSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "WindowsVirtualMachineSourceImageReferenceOutputReference":
        return typing.cast("WindowsVirtualMachineSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WindowsVirtualMachineTimeoutsOutputReference":
        return typing.cast("WindowsVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @builtins.property
    @jsii.member(jsii_name="winrmListener")
    def winrm_listener(self) -> "WindowsVirtualMachineWinrmListenerList":
        return typing.cast("WindowsVirtualMachineWinrmListenerList", jsii.get(self, "winrmListener"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineAdditionalCapabilities"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContentInput")
    def additional_unattend_content_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineAdditionalUnattendContent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineAdditionalUnattendContent"]]], jsii.get(self, "additionalUnattendContentInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowExtensionOperationsInput")
    def allow_extension_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowExtensionOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilitySetIdInput")
    def availability_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilitySetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineBootDiagnostics"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNameInput")
    def computer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdatesInput")
    def enable_automatic_updates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutomaticUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabledInput")
    def encryption_at_host_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptionAtHostEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="evictionPolicyInput")
    def eviction_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evictionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionsTimeBudgetInput")
    def extensions_time_budget_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionsTimeBudgetInput"))

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
    @jsii.member(jsii_name="maxBidPriceInput")
    def max_bid_price_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIdsInput")
    def network_interface_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkInterfaceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["WindowsVirtualMachineOsDisk"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="patchModeInput")
    def patch_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patchModeInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["WindowsVirtualMachinePlan"]:
        return typing.cast(typing.Optional["WindowsVirtualMachinePlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgentInput")
    def provision_vm_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "provisionVmAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecret"]]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageIdInput")
    def source_image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReferenceInput")
    def source_image_reference_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineSourceImageReference"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetIdInput")
    def virtual_machine_scale_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineScaleSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmListenerInput")
    def winrm_listener_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]], jsii.get(self, "winrmListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ffbc7228e8a42a80dc7232215368a707417c5b5f9cea685d54f1de171010348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91448588033805652e645308b884b93b1ef89db59729da71a4004280aa39be79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="allowExtensionOperations")
    def allow_extension_operations(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowExtensionOperations"))

    @allow_extension_operations.setter
    def allow_extension_operations(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a8dfc895ec57983bf731d9f449980f9f015c170a357de6468da9edb1ed192b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExtensionOperations", value)

    @builtins.property
    @jsii.member(jsii_name="availabilitySetId")
    def availability_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilitySetId"))

    @availability_set_id.setter
    def availability_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e1a9a4e77f1c1ff254087b8f83b68b95f3b92a8f3bb2507321d2ae000d28657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilitySetId", value)

    @builtins.property
    @jsii.member(jsii_name="computerName")
    def computer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerName"))

    @computer_name.setter
    def computer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836c911717abf1e7b0f7429977f37a32c1a48420d432af83d7934c79f9e32a5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerName", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ce3504c79711a7bcf419a83e43b76bd20facdeaef09d1dca93fcbe8b41b1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdates")
    def enable_automatic_updates(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutomaticUpdates"))

    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e631853d1468215182979f56e1554d1ad8ef3e6c0e1fb39804a4d09c4ec3558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticUpdates", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabled")
    def encryption_at_host_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encryptionAtHostEnabled"))

    @encryption_at_host_enabled.setter
    def encryption_at_host_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__926316619f0eae679893272a9766445d8e8ed2f4b5d782911d5c508a96970be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="evictionPolicy")
    def eviction_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evictionPolicy"))

    @eviction_policy.setter
    def eviction_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e473abb18f44ed69c2105f0dbeec2e18fbfeca4bbf0f9ecf9d27d5a4a4d73b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evictionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="extensionsTimeBudget")
    def extensions_time_budget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extensionsTimeBudget"))

    @extensions_time_budget.setter
    def extensions_time_budget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d49768706900cf64682e5c9f44b58955c5fabe49ea64ce540a5155c42eb618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionsTimeBudget", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7699f09650c43bb97c88fabd48ffe5446d008a8e78a01c6a618cd8904ae7d4ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e058401719dc0b55a07078cf77a296405f45120f02dbe9b104397de54b42057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__400dc9ac369b4c0a28cb1e80d5da7153de8e694ac4ec05ae61717515b7d7c81e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maxBidPrice")
    def max_bid_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBidPrice"))

    @max_bid_price.setter
    def max_bid_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdff186404c6630aba79026bd9ad3731103752f8ec0ed8bb679df5b10eba8a98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d38397d7f35ef1328c1346c2797e4bb00d628921c774fb67d4b9600628c6c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @network_interface_ids.setter
    def network_interface_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29653ccbefd973002b0886e1a75f00c8a80c3e91fb7cf679febd55f2bcd8f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceIds", value)

    @builtins.property
    @jsii.member(jsii_name="patchMode")
    def patch_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchMode"))

    @patch_mode.setter
    def patch_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d858ab6f4a57e4a3f901c9f5306310b71d0f9820df4ea59f7d563e0e9a9cf3c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchMode", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f5712ffa4152a7dc662ecd6f0abc14caacdefc725ef9e052137f27e8ab9d92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__a24f26e56c116f3242c89062eb282a6668d561d573a40eacd65f610593618e1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d98555af6abb51583d68ba3ce88bf541c69ef6a8445b7b9d02271e6969e6258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b13dd29491d62bb25c2187bde134e9cd1ca70b204fed4d0ff34ba1c385ed311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ef5c4a050eec0d1d76642da8507b05d06337da63779b8fe2f9959d2a0352069)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc836b372b6d33dfc099744a7f59bf1ac80205ac24cc7a031dd3f807167fcca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7d09cd575d546b51f9a2d34d27df67e78774f7ba7241fe219da35fe97305f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetId")
    def virtual_machine_scale_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineScaleSetId"))

    @virtual_machine_scale_set_id.setter
    def virtual_machine_scale_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcbb51e38ce5943333c6174aaae8142ce0b3a359e956f1713925394802124787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineScaleSetId", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa6fb2deab1a74cc406b58301edb9cf5415721372ac419c5b456401ff815098)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class WindowsVirtualMachineAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381f444b477a1a736b8e103f541b2f7e5269b95698e4883414fa77deaf042981)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineAdditionalCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b34b102f7fb9ede8bc9033cfb4dda7ce1728b3a2ec85f010b7b19208d4eb3e4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUltraSsdEnabled")
    def reset_ultra_ssd_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUltraSsdEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabledInput")
    def ultra_ssd_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ultraSsdEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabled")
    def ultra_ssd_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ultraSsdEnabled"))

    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf785a0e36b8dc68b3df23f108f3336e6764bf0457e911a88c5ac36f5ff5ac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineAdditionalCapabilities]:
        return typing.cast(typing.Optional[WindowsVirtualMachineAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4602d533d92457a9ec390ef46e963350a8b8fb1659a453d213f7996bd73cb8ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContent",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "setting": "setting"},
)
class WindowsVirtualMachineAdditionalUnattendContent:
    def __init__(self, *, content: builtins.str, setting: builtins.str) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#content WindowsVirtualMachine#content}.
        :param setting: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#setting WindowsVirtualMachine#setting}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a056730eba3276415bd68c1e498cad2a3ad1f9a50aa10dd84953ce5d8c80c974)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument setting", value=setting, expected_type=type_hints["setting"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "setting": setting,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#content WindowsVirtualMachine#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#setting WindowsVirtualMachine#setting}.'''
        result = self._values.get("setting")
        assert result is not None, "Required property 'setting' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineAdditionalUnattendContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineAdditionalUnattendContentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f656d2b5818de2706b19f90ce77247882b90d56e29e58ed3e28df6b2a9a2097)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineAdditionalUnattendContentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2843d2d45cde43275d27fd8be1d49b535dc667470cbc21f947d339709807d4b2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineAdditionalUnattendContentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28bc65e0268aba6749f46a009a91383a2da409a6b3d98c968c2f2c7ec0237b94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21db536bb14d933cb97820063a18f598204b7ad79da9b283f7684b492b84fd2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f83d7afbadc8092c32d03f79fa6a381590fc00bf739317126b6a9e05fb1aa90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca7eb4df74f8bec71164aa48a6fee682b16af00a43ab47b4c2dfc6310e5ef9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineAdditionalUnattendContentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a1754bea2e223e43b14072e1a3318aa3d6acac7e252c1830475606ce9e06abd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="settingInput")
    def setting_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8793642b54764646767372185bd47291fd9dcae16422193b4911a8a650b2db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="setting")
    def setting(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setting"))

    @setting.setter
    def setting(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__850dcfe8026a13900dd5cc59b7e6a2277dedf431150fea391d4cab3b91ae69b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setting", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ad23248d7bb22b827e651057663273e53867bd44bd2c9dfb3e7629f1dbfa30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class WindowsVirtualMachineBootDiagnostics:
    def __init__(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704cea54a486a5864e0de4df54edf022746fe0734a9956b9dab1aaeb4e2a3000)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_account_uri": storage_account_uri,
        }

    @builtins.property
    def storage_account_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        assert result is not None, "Required property 'storage_account_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineBootDiagnosticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8abe1de3936cfcea8df998ed006ff3598739912739ffe4ab2171b999437d925)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="storageAccountUriInput")
    def storage_account_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountUriInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountUri")
    def storage_account_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUri"))

    @storage_account_uri.setter
    def storage_account_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae58a48274f3ba01fa29794ee763928bea8e48c5a64175a8760dbb84be33872a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineBootDiagnostics]:
        return typing.cast(typing.Optional[WindowsVirtualMachineBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b822428201a6d5620550cc8ed507c68f84b2a7bde29bb4f2bc57d4f8a3f7781b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_password": "adminPassword",
        "admin_username": "adminUsername",
        "location": "location",
        "name": "name",
        "network_interface_ids": "networkInterfaceIds",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "size": "size",
        "additional_capabilities": "additionalCapabilities",
        "additional_unattend_content": "additionalUnattendContent",
        "allow_extension_operations": "allowExtensionOperations",
        "availability_set_id": "availabilitySetId",
        "boot_diagnostics": "bootDiagnostics",
        "computer_name": "computerName",
        "custom_data": "customData",
        "enable_automatic_updates": "enableAutomaticUpdates",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "eviction_policy": "evictionPolicy",
        "extensions_time_budget": "extensionsTimeBudget",
        "id": "id",
        "license_type": "licenseType",
        "max_bid_price": "maxBidPrice",
        "patch_mode": "patchMode",
        "plan": "plan",
        "priority": "priority",
        "provision_vm_agent": "provisionVmAgent",
        "secret": "secret",
        "source_image_id": "sourceImageId",
        "source_image_reference": "sourceImageReference",
        "tags": "tags",
        "timeouts": "timeouts",
        "timezone": "timezone",
        "virtual_machine_scale_set_id": "virtualMachineScaleSetId",
        "winrm_listener": "winrmListener",
        "zone": "zone",
    },
)
class WindowsVirtualMachineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admin_password: builtins.str,
        admin_username: builtins.str,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["WindowsVirtualMachineOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        patch_mode: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
        winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[builtins.str, typing.Any]]]]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#location WindowsVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#size WindowsVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#id WindowsVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.
        :param patch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = WindowsVirtualMachineOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = WindowsVirtualMachineAdditionalCapabilities(**additional_capabilities)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = WindowsVirtualMachineBootDiagnostics(**boot_diagnostics)
        if isinstance(plan, dict):
            plan = WindowsVirtualMachinePlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = WindowsVirtualMachineSourceImageReference(**source_image_reference)
        if isinstance(timeouts, dict):
            timeouts = WindowsVirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26720eab850312b946df5e938219b65ca05fc7974759d8eed523f5929e25ef87)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface_ids", value=network_interface_ids, expected_type=type_hints["network_interface_ids"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument additional_unattend_content", value=additional_unattend_content, expected_type=type_hints["additional_unattend_content"])
            check_type(argname="argument allow_extension_operations", value=allow_extension_operations, expected_type=type_hints["allow_extension_operations"])
            check_type(argname="argument availability_set_id", value=availability_set_id, expected_type=type_hints["availability_set_id"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument computer_name", value=computer_name, expected_type=type_hints["computer_name"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument enable_automatic_updates", value=enable_automatic_updates, expected_type=type_hints["enable_automatic_updates"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument eviction_policy", value=eviction_policy, expected_type=type_hints["eviction_policy"])
            check_type(argname="argument extensions_time_budget", value=extensions_time_budget, expected_type=type_hints["extensions_time_budget"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument max_bid_price", value=max_bid_price, expected_type=type_hints["max_bid_price"])
            check_type(argname="argument patch_mode", value=patch_mode, expected_type=type_hints["patch_mode"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument source_image_id", value=source_image_id, expected_type=type_hints["source_image_id"])
            check_type(argname="argument source_image_reference", value=source_image_reference, expected_type=type_hints["source_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument virtual_machine_scale_set_id", value=virtual_machine_scale_set_id, expected_type=type_hints["virtual_machine_scale_set_id"])
            check_type(argname="argument winrm_listener", value=winrm_listener, expected_type=type_hints["winrm_listener"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_password": admin_password,
            "admin_username": admin_username,
            "location": location,
            "name": name,
            "network_interface_ids": network_interface_ids,
            "os_disk": os_disk,
            "resource_group_name": resource_group_name,
            "size": size,
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
        if additional_capabilities is not None:
            self._values["additional_capabilities"] = additional_capabilities
        if additional_unattend_content is not None:
            self._values["additional_unattend_content"] = additional_unattend_content
        if allow_extension_operations is not None:
            self._values["allow_extension_operations"] = allow_extension_operations
        if availability_set_id is not None:
            self._values["availability_set_id"] = availability_set_id
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if computer_name is not None:
            self._values["computer_name"] = computer_name
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if enable_automatic_updates is not None:
            self._values["enable_automatic_updates"] = enable_automatic_updates
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if eviction_policy is not None:
            self._values["eviction_policy"] = eviction_policy
        if extensions_time_budget is not None:
            self._values["extensions_time_budget"] = extensions_time_budget
        if id is not None:
            self._values["id"] = id
        if license_type is not None:
            self._values["license_type"] = license_type
        if max_bid_price is not None:
            self._values["max_bid_price"] = max_bid_price
        if patch_mode is not None:
            self._values["patch_mode"] = patch_mode
        if plan is not None:
            self._values["plan"] = plan
        if priority is not None:
            self._values["priority"] = priority
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if secret is not None:
            self._values["secret"] = secret
        if source_image_id is not None:
            self._values["source_image_id"] = source_image_id
        if source_image_reference is not None:
            self._values["source_image_reference"] = source_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone is not None:
            self._values["timezone"] = timezone
        if virtual_machine_scale_set_id is not None:
            self._values["virtual_machine_scale_set_id"] = virtual_machine_scale_set_id
        if winrm_listener is not None:
            self._values["winrm_listener"] = winrm_listener
        if zone is not None:
            self._values["zone"] = zone

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
    def admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.'''
        result = self._values.get("admin_password")
        assert result is not None, "Required property 'admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#location WindowsVirtualMachine#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.'''
        result = self._values.get("network_interface_ids")
        assert result is not None, "Required property 'network_interface_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def os_disk(self) -> "WindowsVirtualMachineOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("WindowsVirtualMachineOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#size WindowsVirtualMachine#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[WindowsVirtualMachineAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[WindowsVirtualMachineAdditionalCapabilities], result)

    @builtins.property
    def additional_unattend_content(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]]:
        '''additional_unattend_content block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        '''
        result = self._values.get("additional_unattend_content")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]], result)

    @builtins.property
    def allow_extension_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.'''
        result = self._values.get("allow_extension_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.'''
        result = self._values.get("availability_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_diagnostics(self) -> typing.Optional[WindowsVirtualMachineBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[WindowsVirtualMachineBootDiagnostics], result)

    @builtins.property
    def computer_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.'''
        result = self._values.get("computer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_automatic_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.'''
        result = self._values.get("enable_automatic_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def eviction_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.'''
        result = self._values.get("eviction_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extensions_time_budget(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.'''
        result = self._values.get("extensions_time_budget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#id WindowsVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_bid_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.'''
        result = self._values.get("max_bid_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def patch_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.'''
        result = self._values.get("patch_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(self) -> typing.Optional["WindowsVirtualMachinePlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["WindowsVirtualMachinePlan"], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecret"]]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["WindowsVirtualMachineSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["WindowsVirtualMachineSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WindowsVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WindowsVirtualMachineTimeouts"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_machine_scale_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.'''
        result = self._values.get("virtual_machine_scale_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def winrm_listener(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]]:
        '''winrm_listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        '''
        result = self._values.get("winrm_listener")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "storage_account_type": "storageAccountType",
        "diff_disk_settings": "diffDiskSettings",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "disk_size_gb": "diskSizeGb",
        "name": "name",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class WindowsVirtualMachineOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = WindowsVirtualMachineOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2cf98a28c78ab1e27c5f30b49ad5e332368a9b70cbf3e171f8b7a068b40db1)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument diff_disk_settings", value=diff_disk_settings, expected_type=type_hints["diff_disk_settings"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "caching": caching,
            "storage_account_type": storage_account_type,
        }
        if diff_disk_settings is not None:
            self._values["diff_disk_settings"] = diff_disk_settings
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if name is not None:
            self._values["name"] = name
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["WindowsVirtualMachineOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["WindowsVirtualMachineOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option"},
)
class WindowsVirtualMachineOsDiskDiffDiskSettings:
    def __init__(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#option WindowsVirtualMachine#option}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19876abd219ff3648a06d7794ddc539d06e8ab1737c7e065395549f91a4995fd)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "option": option,
        }

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#option WindowsVirtualMachine#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e02087b3253b9efb25c75244d566e86ddb7aae1f8b1a5807274363e0f94259e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="optionInput")
    def option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionInput"))

    @builtins.property
    @jsii.member(jsii_name="option")
    def option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "option"))

    @option.setter
    def option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10dfab16ed57863171edafdd5b1fd0f43b56507d5d62001f74a4d5e00b3fa726)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67846a5357dee972e5670c3918b78b611d23d47286ac3beb805649d42013cff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72d5eb0bb9c35899c3d7ac2df5e829d9e2308486720c65e7af6a7970970156a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#option WindowsVirtualMachine#option}.
        '''
        value = WindowsVirtualMachineOsDiskDiffDiskSettings(option=option)

        return typing.cast(None, jsii.invoke(self, "putDiffDiskSettings", [value]))

    @jsii.member(jsii_name="resetDiffDiskSettings")
    def reset_diff_disk_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiffDiskSettings", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettings")
    def diff_disk_settings(
        self,
    ) -> WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__87a15700eb512ce7b7de8d13101334994531ca92d3fe47de0d77547665b15b19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5815cb3036166469561c3822a8a8a437c8b524df764a20e762553dd8c35cf4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6815405d4e3600114c368b71638512c944df20950b701ffa46a182654b481a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7284123a35079ebab54c6c84b399294c58ddedfeb725f48eae1b6417c04724ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd0ebbafe7d46500fa55e480555f334cb785f6af98c80f953da5d4bbf28a3c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__b16e66ddf4f28bea5311f03843c845fc3a6c3232dfba0a128792a8825580edca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineOsDisk]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cecb5be8047ed9c865813d915a4d986eee8b9a6c93261c3995f080d874413ed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachinePlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class WindowsVirtualMachinePlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#product WindowsVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e11614fb7d78c89a39a22099f065b5c14be27acd0ca00845fd9295d6e46b843)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#product WindowsVirtualMachine#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachinePlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachinePlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachinePlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c0830577698f975035d4f8563393f81d9edaa7e7563601e10bcdbd707ed0a3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23426642d34bcd427637f5b660064a9ed8efc578e8a3c945eeb0c2ead1fed269)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27427f966b3d9bb29be5c19919fdad3be31893c5a60aa6d0a914e77b79ee5546)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240a3096767031efa3484e55cf1a9dfb136c45e24ad5509810e96e82278a83fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachinePlan]:
        return typing.cast(typing.Optional[WindowsVirtualMachinePlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsVirtualMachinePlan]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c68f264eb338cf7565fa75912c69dea905cd0fda368304c301bb8bd9e764706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class WindowsVirtualMachineSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecretCertificate", typing.Dict[builtins.str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#certificate WindowsVirtualMachine#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#key_vault_id WindowsVirtualMachine#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de59719674d71fb1c3fb0e21dc5883c67d2f73748a81c0adc276c3b364381990)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#certificate WindowsVirtualMachine#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#key_vault_id WindowsVirtualMachine#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={"store": "store"},
)
class WindowsVirtualMachineSecretCertificate:
    def __init__(self, *, store: builtins.str) -> None:
        '''
        :param store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#store WindowsVirtualMachine#store}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fad3ec74c8a4f818dfaf4bf1029db213b2955aba46de6165b2565f5ae150f7f)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "store": store,
        }

    @builtins.property
    def store(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#store WindowsVirtualMachine#store}.'''
        result = self._values.get("store")
        assert result is not None, "Required property 'store' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineSecretCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecretCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__408b773303a964daa4dcbee01b00a117dbaa1e10945fddcf9c2df962c2661916)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ada062fe4e795cb733db10611fa22ffc80e9214c29dd18f391fc07223fefe2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ad26ffc4b4a976cc5ec19909ec56fc7bc5c794c84d93390ef4feaa52ee24052)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b81c03f2bbeb9dd4416fc2f03fefde7a1f8fc209f2501bcdfbea6c608ea8910)
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
            type_hints = typing.get_type_hints(_typecheckingstub__036cbb154faab5a0403d049cd2c4ea8eb529ac154d767a8263ab7f064e68093f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28eea9e17af1112962024f160940bad4b53dc46be7753dbb25978bd6f13ccad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e21ef2ba4146a8d6eb284295cf59cb919fdeee5a517004c97c32a3cdc6e7ab2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="storeInput")
    def store_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeInput"))

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "store"))

    @store.setter
    def store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0fbf121d6076018f7f47e4310e25ea791ee100e6f90fa105c023ae98d6cd6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "store", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a4105049ac4b4c3bcad526b737cf502050aaaca71663cd39f2ae2da8123557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecretList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64203190941007aa8b70eb148d5a0908c0bf754fd1de71a5f31bea1179aa88c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WindowsVirtualMachineSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50333700b0df616b443e9f77ad071a377b62849c576a8eeddb1307ee8e4fffdb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9b78a79239841a8fb8f3cbf4ceaf5db4c9179efaf6d57fb0b43e4eb94d7503a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__442d818197d1ad9335d3261c3033550602bc7a24c64e7b1adcb6d9c775bd8aeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__79a4c7fddf937ff109f6cb4b9058f6b9d3e7671a08bd989fd96bfb952f2e2556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecret]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2650aaca920ce9ad150c0699bbf42ae40004d3dfec1f030a80883d73d3f507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSecretOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a82cebd2229f10fecee90122ea8f8fe367a08cf3eda48b21c98b5db5131d43b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6125684964d49221b8da20dd022c6d1ed8a0d90def0e244d6f1b057fc71e6405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> WindowsVirtualMachineSecretCertificateList:
        return typing.cast(WindowsVirtualMachineSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090d6ed75e485c4548f3d6c56d03b4a9e7bb25ee8abfec2155ac8830e0c6f1d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fdc616df93f3fc42946e5c04fac76fc43c5633e372834cc66cf2e497eecf5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class WindowsVirtualMachineSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#version WindowsVirtualMachine#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a180e043290632bd48df8872785f9fd87dd2cf0249bd2027724d25093d089a4f)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "offer": offer,
            "publisher": publisher,
            "sku": sku,
            "version": version,
        }

    @builtins.property
    def offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#version WindowsVirtualMachine#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineSourceImageReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dc2d28e6f56a985f5e3b4dc575b5e868edfe6bd58f6d4696968e5181512ba2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d1b86c1279422f0d359817136bf20f4869789a6db63b87504a9b61889e86cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3459e440656fd57ca24bdf405783ef90e181f4ef99e4c888025795d6c156d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b71de8d33be5a70637ec03e470e7fd65fcda111614abfacb6ea3f915a89ff724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a8ca76928ef677cb1fb354861c16fa64155e02b5f24a7d7a85e883584d97f3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineSourceImageReference]:
        return typing.cast(typing.Optional[WindowsVirtualMachineSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a05d934b027f4aa2760bcf282ed4570b94bcbb16f27e325ad3d0a94d61a2caa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WindowsVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#create WindowsVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#read WindowsVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#update WindowsVirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f39d6ac9f1ba29a2ee7a0a8ad4f322de98375a68e4593fac9a102c1688384929)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#create WindowsVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#read WindowsVirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#update WindowsVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b21daefbb8dd93e0b6eea4d07a7254e9bf829c8723dbe7fe749b0abd2815b4dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__edb3d7a52096dc05a5b75ca59e4e1ad13e05e57b1d295dcb1d02c8267669289e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81a5d0c2c851b38e9593b507f644690d050e11f8ed958dfe18600861dbc5d84f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e232667086516e9edd056f2dfed8997417bf7c2f27ed8b5137f79ba61921bfb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d05f8560ebb975fce8390a9d686618bd387810f8b586d02df281776c49b3daa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc9c79bb5e8e89f41aca897a8a8cd8150dccf55e6b49a8c9bb473d13eec93b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineWinrmListener",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol"},
)
class WindowsVirtualMachineWinrmListener:
    def __init__(self, *, protocol: builtins.str) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#protocol WindowsVirtualMachine#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f2221a3ae11018f6b8ace599beb9f64e92e091f4f814037b9ee049c1d6dbf6)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine#protocol WindowsVirtualMachine#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineWinrmListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineWinrmListenerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineWinrmListenerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7659ad53dba35a187398c2d22692ac5a701212ed69394c36ef633c73ba88536)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineWinrmListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1301e4cd9c56f09f4b0f72b32a99bbf186c2d7ceac4db4873d8fe5aa3fa6de17)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineWinrmListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78393f139a32b5399c020e78182d7b602e56dff2821b1f697816d4bb02c9dc14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__926c7bf3ed4ccb43bd01da5811d15e268ac0c4879eb74237763c533c610d67d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7188b2da921b2ccf5389dc3d7f147ec5044c534a8692ee6bb28b523f3afaed5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f29f634d19ba8f777ea39158d0dcd989ea5b472cbf13ac8757fd57729eef61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineWinrmListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachine.WindowsVirtualMachineWinrmListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff2a66e264a75cc2dc92b1be552d0d0a1ab9e6d5e085bcf37ee4bff35fec53c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b530c543b85bef026dea37f0e067a07fae85ca42e0fce0e77a1cfc889db96cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d63ef50ed0ec09fc5514ed86c6651f334266dc832bee3e81d3561b73aaa7c559)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WindowsVirtualMachine",
    "WindowsVirtualMachineAdditionalCapabilities",
    "WindowsVirtualMachineAdditionalCapabilitiesOutputReference",
    "WindowsVirtualMachineAdditionalUnattendContent",
    "WindowsVirtualMachineAdditionalUnattendContentList",
    "WindowsVirtualMachineAdditionalUnattendContentOutputReference",
    "WindowsVirtualMachineBootDiagnostics",
    "WindowsVirtualMachineBootDiagnosticsOutputReference",
    "WindowsVirtualMachineConfig",
    "WindowsVirtualMachineOsDisk",
    "WindowsVirtualMachineOsDiskDiffDiskSettings",
    "WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference",
    "WindowsVirtualMachineOsDiskOutputReference",
    "WindowsVirtualMachinePlan",
    "WindowsVirtualMachinePlanOutputReference",
    "WindowsVirtualMachineSecret",
    "WindowsVirtualMachineSecretCertificate",
    "WindowsVirtualMachineSecretCertificateList",
    "WindowsVirtualMachineSecretCertificateOutputReference",
    "WindowsVirtualMachineSecretList",
    "WindowsVirtualMachineSecretOutputReference",
    "WindowsVirtualMachineSourceImageReference",
    "WindowsVirtualMachineSourceImageReferenceOutputReference",
    "WindowsVirtualMachineTimeouts",
    "WindowsVirtualMachineTimeoutsOutputReference",
    "WindowsVirtualMachineWinrmListener",
    "WindowsVirtualMachineWinrmListenerList",
    "WindowsVirtualMachineWinrmListenerOutputReference",
]

publication.publish()

def _typecheckingstub__f983246ee6b34a7374f8f8793e629fbcc60faf3f9bc8ad00e5d45aa9062e7b2f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_password: builtins.str,
    admin_username: builtins.str,
    location: builtins.str,
    name: builtins.str,
    network_interface_ids: typing.Sequence[builtins.str],
    os_disk: typing.Union[WindowsVirtualMachineOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    size: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    eviction_policy: typing.Optional[builtins.str] = None,
    extensions_time_budget: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    max_bid_price: typing.Optional[jsii.Number] = None,
    patch_mode: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[WindowsVirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[builtins.str] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[WindowsVirtualMachineSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
    winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineWinrmListener, typing.Dict[builtins.str, typing.Any]]]]] = None,
    zone: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4ba4602ee9f1e57ac88174525d2e431fc4c5806cadcf6e3a4625ffe0059002d4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2faff73a61bbabd23029bbd9b6d6295fff2e0c356e9988a031ae211ca3b226e6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952659fd979e4913adbd31af84095953516ad20acec2d9d9a6570be2bb44b2fa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineWinrmListener, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ffbc7228e8a42a80dc7232215368a707417c5b5f9cea685d54f1de171010348(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91448588033805652e645308b884b93b1ef89db59729da71a4004280aa39be79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a8dfc895ec57983bf731d9f449980f9f015c170a357de6468da9edb1ed192b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1a9a4e77f1c1ff254087b8f83b68b95f3b92a8f3bb2507321d2ae000d28657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836c911717abf1e7b0f7429977f37a32c1a48420d432af83d7934c79f9e32a5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ce3504c79711a7bcf419a83e43b76bd20facdeaef09d1dca93fcbe8b41b1d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e631853d1468215182979f56e1554d1ad8ef3e6c0e1fb39804a4d09c4ec3558(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__926316619f0eae679893272a9766445d8e8ed2f4b5d782911d5c508a96970be8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e473abb18f44ed69c2105f0dbeec2e18fbfeca4bbf0f9ecf9d27d5a4a4d73b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d49768706900cf64682e5c9f44b58955c5fabe49ea64ce540a5155c42eb618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7699f09650c43bb97c88fabd48ffe5446d008a8e78a01c6a618cd8904ae7d4ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e058401719dc0b55a07078cf77a296405f45120f02dbe9b104397de54b42057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400dc9ac369b4c0a28cb1e80d5da7153de8e694ac4ec05ae61717515b7d7c81e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdff186404c6630aba79026bd9ad3731103752f8ec0ed8bb679df5b10eba8a98(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d38397d7f35ef1328c1346c2797e4bb00d628921c774fb67d4b9600628c6c2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29653ccbefd973002b0886e1a75f00c8a80c3e91fb7cf679febd55f2bcd8f7b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d858ab6f4a57e4a3f901c9f5306310b71d0f9820df4ea59f7d563e0e9a9cf3c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f5712ffa4152a7dc662ecd6f0abc14caacdefc725ef9e052137f27e8ab9d92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24f26e56c116f3242c89062eb282a6668d561d573a40eacd65f610593618e1d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d98555af6abb51583d68ba3ce88bf541c69ef6a8445b7b9d02271e6969e6258(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b13dd29491d62bb25c2187bde134e9cd1ca70b204fed4d0ff34ba1c385ed311(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ef5c4a050eec0d1d76642da8507b05d06337da63779b8fe2f9959d2a0352069(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc836b372b6d33dfc099744a7f59bf1ac80205ac24cc7a031dd3f807167fcca(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7d09cd575d546b51f9a2d34d27df67e78774f7ba7241fe219da35fe97305f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcbb51e38ce5943333c6174aaae8142ce0b3a359e956f1713925394802124787(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa6fb2deab1a74cc406b58301edb9cf5415721372ac419c5b456401ff815098(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381f444b477a1a736b8e103f541b2f7e5269b95698e4883414fa77deaf042981(
    *,
    ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34b102f7fb9ede8bc9033cfb4dda7ce1728b3a2ec85f010b7b19208d4eb3e4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf785a0e36b8dc68b3df23f108f3336e6764bf0457e911a88c5ac36f5ff5ac8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4602d533d92457a9ec390ef46e963350a8b8fb1659a453d213f7996bd73cb8ad(
    value: typing.Optional[WindowsVirtualMachineAdditionalCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a056730eba3276415bd68c1e498cad2a3ad1f9a50aa10dd84953ce5d8c80c974(
    *,
    content: builtins.str,
    setting: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f656d2b5818de2706b19f90ce77247882b90d56e29e58ed3e28df6b2a9a2097(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2843d2d45cde43275d27fd8be1d49b535dc667470cbc21f947d339709807d4b2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28bc65e0268aba6749f46a009a91383a2da409a6b3d98c968c2f2c7ec0237b94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21db536bb14d933cb97820063a18f598204b7ad79da9b283f7684b492b84fd2d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f83d7afbadc8092c32d03f79fa6a381590fc00bf739317126b6a9e05fb1aa90(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca7eb4df74f8bec71164aa48a6fee682b16af00a43ab47b4c2dfc6310e5ef9c1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1754bea2e223e43b14072e1a3318aa3d6acac7e252c1830475606ce9e06abd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8793642b54764646767372185bd47291fd9dcae16422193b4911a8a650b2db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__850dcfe8026a13900dd5cc59b7e6a2277dedf431150fea391d4cab3b91ae69b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ad23248d7bb22b827e651057663273e53867bd44bd2c9dfb3e7629f1dbfa30(
    value: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704cea54a486a5864e0de4df54edf022746fe0734a9956b9dab1aaeb4e2a3000(
    *,
    storage_account_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8abe1de3936cfcea8df998ed006ff3598739912739ffe4ab2171b999437d925(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae58a48274f3ba01fa29794ee763928bea8e48c5a64175a8760dbb84be33872a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b822428201a6d5620550cc8ed507c68f84b2a7bde29bb4f2bc57d4f8a3f7781b(
    value: typing.Optional[WindowsVirtualMachineBootDiagnostics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26720eab850312b946df5e938219b65ca05fc7974759d8eed523f5929e25ef87(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    admin_password: builtins.str,
    admin_username: builtins.str,
    location: builtins.str,
    name: builtins.str,
    network_interface_ids: typing.Sequence[builtins.str],
    os_disk: typing.Union[WindowsVirtualMachineOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    size: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    eviction_policy: typing.Optional[builtins.str] = None,
    extensions_time_budget: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    max_bid_price: typing.Optional[jsii.Number] = None,
    patch_mode: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[WindowsVirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[builtins.str] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[WindowsVirtualMachineSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
    winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineWinrmListener, typing.Dict[builtins.str, typing.Any]]]]] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2cf98a28c78ab1e27c5f30b49ad5e332368a9b70cbf3e171f8b7a068b40db1(
    *,
    caching: builtins.str,
    storage_account_type: builtins.str,
    diff_disk_settings: typing.Optional[typing.Union[WindowsVirtualMachineOsDiskDiffDiskSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_encryption_set_id: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19876abd219ff3648a06d7794ddc539d06e8ab1737c7e065395549f91a4995fd(
    *,
    option: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e02087b3253b9efb25c75244d566e86ddb7aae1f8b1a5807274363e0f94259e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10dfab16ed57863171edafdd5b1fd0f43b56507d5d62001f74a4d5e00b3fa726(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67846a5357dee972e5670c3918b78b611d23d47286ac3beb805649d42013cff(
    value: typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d5eb0bb9c35899c3d7ac2df5e829d9e2308486720c65e7af6a7970970156a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a15700eb512ce7b7de8d13101334994531ca92d3fe47de0d77547665b15b19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5815cb3036166469561c3822a8a8a437c8b524df764a20e762553dd8c35cf4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6815405d4e3600114c368b71638512c944df20950b701ffa46a182654b481a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7284123a35079ebab54c6c84b399294c58ddedfeb725f48eae1b6417c04724ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd0ebbafe7d46500fa55e480555f334cb785f6af98c80f953da5d4bbf28a3c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16e66ddf4f28bea5311f03843c845fc3a6c3232dfba0a128792a8825580edca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cecb5be8047ed9c865813d915a4d986eee8b9a6c93261c3995f080d874413ed4(
    value: typing.Optional[WindowsVirtualMachineOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e11614fb7d78c89a39a22099f065b5c14be27acd0ca00845fd9295d6e46b843(
    *,
    name: builtins.str,
    product: builtins.str,
    publisher: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0830577698f975035d4f8563393f81d9edaa7e7563601e10bcdbd707ed0a3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23426642d34bcd427637f5b660064a9ed8efc578e8a3c945eeb0c2ead1fed269(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27427f966b3d9bb29be5c19919fdad3be31893c5a60aa6d0a914e77b79ee5546(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240a3096767031efa3484e55cf1a9dfb136c45e24ad5509810e96e82278a83fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c68f264eb338cf7565fa75912c69dea905cd0fda368304c301bb8bd9e764706(
    value: typing.Optional[WindowsVirtualMachinePlan],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de59719674d71fb1c3fb0e21dc5883c67d2f73748a81c0adc276c3b364381990(
    *,
    certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    key_vault_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fad3ec74c8a4f818dfaf4bf1029db213b2955aba46de6165b2565f5ae150f7f(
    *,
    store: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408b773303a964daa4dcbee01b00a117dbaa1e10945fddcf9c2df962c2661916(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ada062fe4e795cb733db10611fa22ffc80e9214c29dd18f391fc07223fefe2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad26ffc4b4a976cc5ec19909ec56fc7bc5c794c84d93390ef4feaa52ee24052(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b81c03f2bbeb9dd4416fc2f03fefde7a1f8fc209f2501bcdfbea6c608ea8910(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__036cbb154faab5a0403d049cd2c4ea8eb529ac154d767a8263ab7f064e68093f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28eea9e17af1112962024f160940bad4b53dc46be7753dbb25978bd6f13ccad1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e21ef2ba4146a8d6eb284295cf59cb919fdeee5a517004c97c32a3cdc6e7ab2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0fbf121d6076018f7f47e4310e25ea791ee100e6f90fa105c023ae98d6cd6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a4105049ac4b4c3bcad526b737cf502050aaaca71663cd39f2ae2da8123557(
    value: typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64203190941007aa8b70eb148d5a0908c0bf754fd1de71a5f31bea1179aa88c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50333700b0df616b443e9f77ad071a377b62849c576a8eeddb1307ee8e4fffdb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b78a79239841a8fb8f3cbf4ceaf5db4c9179efaf6d57fb0b43e4eb94d7503a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442d818197d1ad9335d3261c3033550602bc7a24c64e7b1adcb6d9c775bd8aeb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a4c7fddf937ff109f6cb4b9058f6b9d3e7671a08bd989fd96bfb952f2e2556(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2650aaca920ce9ad150c0699bbf42ae40004d3dfec1f030a80883d73d3f507(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineSecret]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82cebd2229f10fecee90122ea8f8fe367a08cf3eda48b21c98b5db5131d43b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6125684964d49221b8da20dd022c6d1ed8a0d90def0e244d6f1b057fc71e6405(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090d6ed75e485c4548f3d6c56d03b4a9e7bb25ee8abfec2155ac8830e0c6f1d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fdc616df93f3fc42946e5c04fac76fc43c5633e372834cc66cf2e497eecf5b(
    value: typing.Optional[typing.Union[WindowsVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a180e043290632bd48df8872785f9fd87dd2cf0249bd2027724d25093d089a4f(
    *,
    offer: builtins.str,
    publisher: builtins.str,
    sku: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc2d28e6f56a985f5e3b4dc575b5e868edfe6bd58f6d4696968e5181512ba2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d1b86c1279422f0d359817136bf20f4869789a6db63b87504a9b61889e86cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3459e440656fd57ca24bdf405783ef90e181f4ef99e4c888025795d6c156d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71de8d33be5a70637ec03e470e7fd65fcda111614abfacb6ea3f915a89ff724(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a8ca76928ef677cb1fb354861c16fa64155e02b5f24a7d7a85e883584d97f3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a05d934b027f4aa2760bcf282ed4570b94bcbb16f27e325ad3d0a94d61a2caa(
    value: typing.Optional[WindowsVirtualMachineSourceImageReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39d6ac9f1ba29a2ee7a0a8ad4f322de98375a68e4593fac9a102c1688384929(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b21daefbb8dd93e0b6eea4d07a7254e9bf829c8723dbe7fe749b0abd2815b4dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb3d7a52096dc05a5b75ca59e4e1ad13e05e57b1d295dcb1d02c8267669289e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a5d0c2c851b38e9593b507f644690d050e11f8ed958dfe18600861dbc5d84f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e232667086516e9edd056f2dfed8997417bf7c2f27ed8b5137f79ba61921bfb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05f8560ebb975fce8390a9d686618bd387810f8b586d02df281776c49b3daa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc9c79bb5e8e89f41aca897a8a8cd8150dccf55e6b49a8c9bb473d13eec93b8(
    value: typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f2221a3ae11018f6b8ace599beb9f64e92e091f4f814037b9ee049c1d6dbf6(
    *,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7659ad53dba35a187398c2d22692ac5a701212ed69394c36ef633c73ba88536(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1301e4cd9c56f09f4b0f72b32a99bbf186c2d7ceac4db4873d8fe5aa3fa6de17(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78393f139a32b5399c020e78182d7b602e56dff2821b1f697816d4bb02c9dc14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__926c7bf3ed4ccb43bd01da5811d15e268ac0c4879eb74237763c533c610d67d8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7188b2da921b2ccf5389dc3d7f147ec5044c534a8692ee6bb28b523f3afaed5f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f29f634d19ba8f777ea39158d0dcd989ea5b472cbf13ac8757fd57729eef61(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2a66e264a75cc2dc92b1be552d0d0a1ab9e6d5e085bcf37ee4bff35fec53c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b530c543b85bef026dea37f0e067a07fae85ca42e0fce0e77a1cfc889db96cd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63ef50ed0ec09fc5514ed86c6651f334266dc832bee3e81d3561b73aaa7c559(
    value: typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
