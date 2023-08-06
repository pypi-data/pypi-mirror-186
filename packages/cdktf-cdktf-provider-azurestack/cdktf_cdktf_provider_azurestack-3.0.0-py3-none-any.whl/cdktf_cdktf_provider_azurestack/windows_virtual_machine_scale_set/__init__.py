'''
# `azurestack_windows_virtual_machine_scale_set`

Refer to the Terraform Registory for docs: [`azurestack_windows_virtual_machine_scale_set`](https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set).
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


class WindowsVirtualMachineScaleSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set azurestack_windows_virtual_machine_scale_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_password: builtins.str,
        admin_username: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        os_disk: typing.Union["WindowsVirtualMachineScaleSetOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetAdditionalCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetAdditionalUnattendContent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetAutomaticInstanceRepair", typing.Dict[builtins.str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetBootDiagnostics", typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetPlan", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTerminateNotification", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
        winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetWinrmListener", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set azurestack_windows_virtual_machine_scale_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_password WindowsVirtualMachineScaleSet#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_username WindowsVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#instances WindowsVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#location WindowsVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#network_interface WindowsVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#os_disk WindowsVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#resource_group_name WindowsVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_capabilities WindowsVirtualMachineScaleSet#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_unattend_content WindowsVirtualMachineScaleSet#additional_unattend_content}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_instance_repair WindowsVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_os_upgrade_policy WindowsVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#boot_diagnostics WindowsVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#computer_name_prefix WindowsVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#custom_data WindowsVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#data_disk WindowsVirtualMachineScaleSet#data_disk}
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines WindowsVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_updates WindowsVirtualMachineScaleSet#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#encryption_at_host_enabled WindowsVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#extension WindowsVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#health_probe_id WindowsVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#id WindowsVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#license_type WindowsVirtualMachineScaleSet#license_type}.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#overprovision WindowsVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#plan WindowsVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#platform_fault_domain_count WindowsVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#provision_vm_agent WindowsVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#scale_in_policy WindowsVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#secret WindowsVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#single_placement_group WindowsVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_id WindowsVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_reference WindowsVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#tags WindowsVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#terminate_notification WindowsVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeouts WindowsVirtualMachineScaleSet#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timezone WindowsVirtualMachineScaleSet#timezone}.
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#upgrade_mode WindowsVirtualMachineScaleSet#upgrade_mode}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#winrm_listener WindowsVirtualMachineScaleSet#winrm_listener}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e152b25cfd84de79a3ed40200a30e849f7c42b6e7ccbfaab23a81a762314ce7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WindowsVirtualMachineScaleSetConfig(
            admin_password=admin_password,
            admin_username=admin_username,
            instances=instances,
            location=location,
            name=name,
            network_interface=network_interface,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            sku=sku,
            additional_capabilities=additional_capabilities,
            additional_unattend_content=additional_unattend_content,
            automatic_instance_repair=automatic_instance_repair,
            automatic_os_upgrade_policy=automatic_os_upgrade_policy,
            boot_diagnostics=boot_diagnostics,
            computer_name_prefix=computer_name_prefix,
            custom_data=custom_data,
            data_disk=data_disk,
            do_not_run_extensions_on_overprovisioned_machines=do_not_run_extensions_on_overprovisioned_machines,
            enable_automatic_updates=enable_automatic_updates,
            encryption_at_host_enabled=encryption_at_host_enabled,
            extension=extension,
            health_probe_id=health_probe_id,
            id=id,
            license_type=license_type,
            overprovision=overprovision,
            plan=plan,
            platform_fault_domain_count=platform_fault_domain_count,
            provision_vm_agent=provision_vm_agent,
            scale_in_policy=scale_in_policy,
            secret=secret,
            single_placement_group=single_placement_group,
            source_image_id=source_image_id,
            source_image_reference=source_image_reference,
            tags=tags,
            terminate_notification=terminate_notification,
            timeouts=timeouts,
            timezone=timezone,
            upgrade_mode=upgrade_mode,
            winrm_listener=winrm_listener,
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
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#ultra_ssd_enabled WindowsVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        value = WindowsVirtualMachineScaleSetAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdditionalUnattendContent")
    def put_additional_unattend_content(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetAdditionalUnattendContent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0747e95c20f740c8116a0afd00cdbce9506149c68e0477faac40205a17c900ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalUnattendContent", [value]))

    @jsii.member(jsii_name="putAutomaticInstanceRepair")
    def put_automatic_instance_repair(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#grace_period WindowsVirtualMachineScaleSet#grace_period}.
        '''
        value = WindowsVirtualMachineScaleSetAutomaticInstanceRepair(
            enabled=enabled, grace_period=grace_period
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticInstanceRepair", [value]))

    @jsii.member(jsii_name="putAutomaticOsUpgradePolicy")
    def put_automatic_os_upgrade_policy(
        self,
        *,
        disable_automatic_rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        enable_automatic_os_upgrade: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disable_automatic_rollback WindowsVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_os_upgrade WindowsVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        value = WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy(
            disable_automatic_rollback=disable_automatic_rollback,
            enable_automatic_os_upgrade=enable_automatic_os_upgrade,
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticOsUpgradePolicy", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_uri WindowsVirtualMachineScaleSet#storage_account_uri}.
        '''
        value = WindowsVirtualMachineScaleSetBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putDataDisk")
    def put_data_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b04232ef6a93cd6cb51dd22ee56612531643b1af961b015a0feabc5aa115b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataDisk", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55b172130493f9bf0c8b64e7726ad1d92be508b2d3b3e41c17073bd8963d66dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e439f9395730cfe7d36e744ce13188b88606a2192ae3788fc8099fa045dd477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#caching WindowsVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_type WindowsVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#diff_disk_settings WindowsVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_encryption_set_id WindowsVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_size_gb WindowsVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#write_accelerator_enabled WindowsVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        value = WindowsVirtualMachineScaleSetOsDisk(
            caching=caching,
            storage_account_type=storage_account_type,
            diff_disk_settings=diff_disk_settings,
            disk_encryption_set_id=disk_encryption_set_id,
            disk_size_gb=disk_size_gb,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#product WindowsVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.
        '''
        value = WindowsVirtualMachineScaleSetPlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e0780198f85067f1e22002a8ad682f7915a7a50f9baea7d7b794d9034c5fcc)
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
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#offer WindowsVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#version WindowsVirtualMachineScaleSet#version}.
        '''
        value = WindowsVirtualMachineScaleSetSourceImageReference(
            offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putSourceImageReference", [value]))

    @jsii.member(jsii_name="putTerminateNotification")
    def put_terminate_notification(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeout WindowsVirtualMachineScaleSet#timeout}.
        '''
        value = WindowsVirtualMachineScaleSetTerminateNotification(
            enabled=enabled, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putTerminateNotification", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#create WindowsVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#delete WindowsVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#read WindowsVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#update WindowsVirtualMachineScaleSet#update}.
        '''
        value = WindowsVirtualMachineScaleSetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWinrmListener")
    def put_winrm_listener(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetWinrmListener", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96467d635d701e0a2da4b3641ccce7b3242fca61817622cbdbcd0d03ad55934)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWinrmListener", [value]))

    @jsii.member(jsii_name="resetAdditionalCapabilities")
    def reset_additional_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCapabilities", []))

    @jsii.member(jsii_name="resetAdditionalUnattendContent")
    def reset_additional_unattend_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalUnattendContent", []))

    @jsii.member(jsii_name="resetAutomaticInstanceRepair")
    def reset_automatic_instance_repair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticInstanceRepair", []))

    @jsii.member(jsii_name="resetAutomaticOsUpgradePolicy")
    def reset_automatic_os_upgrade_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticOsUpgradePolicy", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetComputerNamePrefix")
    def reset_computer_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputerNamePrefix", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetDataDisk")
    def reset_data_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataDisk", []))

    @jsii.member(jsii_name="resetDoNotRunExtensionsOnOverprovisionedMachines")
    def reset_do_not_run_extensions_on_overprovisioned_machines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDoNotRunExtensionsOnOverprovisionedMachines", []))

    @jsii.member(jsii_name="resetEnableAutomaticUpdates")
    def reset_enable_automatic_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpdates", []))

    @jsii.member(jsii_name="resetEncryptionAtHostEnabled")
    def reset_encryption_at_host_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtHostEnabled", []))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetHealthProbeId")
    def reset_health_probe_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthProbeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetOverprovision")
    def reset_overprovision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverprovision", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPlatformFaultDomainCount")
    def reset_platform_fault_domain_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformFaultDomainCount", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetScaleInPolicy")
    def reset_scale_in_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInPolicy", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSinglePlacementGroup")
    def reset_single_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSinglePlacementGroup", []))

    @jsii.member(jsii_name="resetSourceImageId")
    def reset_source_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageId", []))

    @jsii.member(jsii_name="resetSourceImageReference")
    def reset_source_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTerminateNotification")
    def reset_terminate_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateNotification", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetUpgradeMode")
    def reset_upgrade_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeMode", []))

    @jsii.member(jsii_name="resetWinrmListener")
    def reset_winrm_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmListener", []))

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
    ) -> "WindowsVirtualMachineScaleSetAdditionalCapabilitiesOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContent")
    def additional_unattend_content(
        self,
    ) -> "WindowsVirtualMachineScaleSetAdditionalUnattendContentList":
        return typing.cast("WindowsVirtualMachineScaleSetAdditionalUnattendContentList", jsii.get(self, "additionalUnattendContent"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepair")
    def automatic_instance_repair(
        self,
    ) -> "WindowsVirtualMachineScaleSetAutomaticInstanceRepairOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetAutomaticInstanceRepairOutputReference", jsii.get(self, "automaticInstanceRepair"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicy")
    def automatic_os_upgrade_policy(
        self,
    ) -> "WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference", jsii.get(self, "automaticOsUpgradePolicy"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(
        self,
    ) -> "WindowsVirtualMachineScaleSetBootDiagnosticsOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="dataDisk")
    def data_disk(self) -> "WindowsVirtualMachineScaleSetDataDiskList":
        return typing.cast("WindowsVirtualMachineScaleSetDataDiskList", jsii.get(self, "dataDisk"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "WindowsVirtualMachineScaleSetExtensionList":
        return typing.cast("WindowsVirtualMachineScaleSetExtensionList", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "WindowsVirtualMachineScaleSetNetworkInterfaceList":
        return typing.cast("WindowsVirtualMachineScaleSetNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "WindowsVirtualMachineScaleSetOsDiskOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "WindowsVirtualMachineScaleSetPlanOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetPlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "WindowsVirtualMachineScaleSetSecretList":
        return typing.cast("WindowsVirtualMachineScaleSetSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "WindowsVirtualMachineScaleSetSourceImageReferenceOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotification")
    def terminate_notification(
        self,
    ) -> "WindowsVirtualMachineScaleSetTerminateNotificationOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetTerminateNotificationOutputReference", jsii.get(self, "terminateNotification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WindowsVirtualMachineScaleSetTimeoutsOutputReference":
        return typing.cast("WindowsVirtualMachineScaleSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property
    @jsii.member(jsii_name="winrmListener")
    def winrm_listener(self) -> "WindowsVirtualMachineScaleSetWinrmListenerList":
        return typing.cast("WindowsVirtualMachineScaleSetWinrmListenerList", jsii.get(self, "winrmListener"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetAdditionalCapabilities"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContentInput")
    def additional_unattend_content_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetAdditionalUnattendContent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetAdditionalUnattendContent"]]], jsii.get(self, "additionalUnattendContentInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepairInput")
    def automatic_instance_repair_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetAutomaticInstanceRepair"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetAutomaticInstanceRepair"], jsii.get(self, "automaticInstanceRepairInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicyInput")
    def automatic_os_upgrade_policy_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy"], jsii.get(self, "automaticOsUpgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetBootDiagnostics"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefixInput")
    def computer_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskInput")
    def data_disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetDataDisk"]]], jsii.get(self, "dataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="doNotRunExtensionsOnOverprovisionedMachinesInput")
    def do_not_run_extensions_on_overprovisioned_machines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "doNotRunExtensionsOnOverprovisionedMachinesInput"))

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
    @jsii.member(jsii_name="extensionInput")
    def extension_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetExtension"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetExtension"]]], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="healthProbeIdInput")
    def health_probe_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthProbeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

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
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["WindowsVirtualMachineScaleSetOsDisk"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="overprovisionInput")
    def overprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["WindowsVirtualMachineScaleSetPlan"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetPlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainCountInput")
    def platform_fault_domain_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "platformFaultDomainCountInput"))

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
    @jsii.member(jsii_name="scaleInPolicyInput")
    def scale_in_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleInPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecret"]]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="singlePlacementGroupInput")
    def single_placement_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "singlePlacementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageIdInput")
    def source_image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReferenceInput")
    def source_image_reference_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetSourceImageReference"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotificationInput")
    def terminate_notification_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetTerminateNotification"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetTerminateNotification"], jsii.get(self, "terminateNotificationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeModeInput")
    def upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmListenerInput")
    def winrm_listener_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetWinrmListener"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetWinrmListener"]]], jsii.get(self, "winrmListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__941eee20b7b5bdd2eca0ad2c7ccda1fb080f46fd8d727cc2097024339db10376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ed803ab7450ff5417752f1611a5c2fa16bc7cda2b3a6884b4bc3ef11f14113)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefix")
    def computer_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerNamePrefix"))

    @computer_name_prefix.setter
    def computer_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4c112dce6fad92c377690c2c7bf6292a0cefa0e0e614ea6ae395238dac62c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__202ce0ba4997ceaf1d10708986b8904def83085a9a884f4c7646ec80d92085c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="doNotRunExtensionsOnOverprovisionedMachines")
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "doNotRunExtensionsOnOverprovisionedMachines"))

    @do_not_run_extensions_on_overprovisioned_machines.setter
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__918167be0432a2ea7d01750fa7fb67c2f90de0e535543708abe0968c300ff703)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "doNotRunExtensionsOnOverprovisionedMachines", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__4498e7f9316209fd7dcbf14c706684e279c07af87de440d67f6afa9a8469e291)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3f11b6471d0eb236830ee571a28c74332dbfd6baa3665e72adb868a53b5e5a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthProbeId")
    def health_probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthProbeId"))

    @health_probe_id.setter
    def health_probe_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e0841f1d0725ec037ead63e9e08ef9da1b90bc5a391aef4af0ffde03456a7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthProbeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093498b1ae63307033814181c91eeb8fbf1f4d831cdbd8efabbdc589c5ff7e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__624c7a676bb9b4a8094c1caf31c51927e84b1fc949566c7e09968473fed0bac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fed0d0efeeea60826ee8989cd01e57789cb2122da68deb64cc1563772d71df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b8acae0a0f8e9db97e76ecf1da72287c8384f105f8a945988751714aae0e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317f43e2e93a3c858c006127f06fdea6611a37a10d4f4a6ba97469caf0cd1ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overprovision")
    def overprovision(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overprovision"))

    @overprovision.setter
    def overprovision(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48c5c3d3b4a2b1c7c0143fcde0b4eda93953e06b2701d3f3797e8a8175c9e035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overprovision", value)

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "platformFaultDomainCount"))

    @platform_fault_domain_count.setter
    def platform_fault_domain_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6cff81858110eddf03357663e396a2a117aaccaee0ac0b2d9abff097dae84b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformFaultDomainCount", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__618135cf8ff5cb75e8d4e7970e8ccbf9f7619dcb28b456892f0a6d07078a7a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2d3a94c97ee200e2a89094ecc2c0051abf2305fe51012efc3cf0531a01af3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicy")
    def scale_in_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleInPolicy"))

    @scale_in_policy.setter
    def scale_in_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94f021ca0119f18ac3745b825bd71f483727df0abe5315d23802f372807e5120)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleInPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="singlePlacementGroup")
    def single_placement_group(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "singlePlacementGroup"))

    @single_placement_group.setter
    def single_placement_group(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e1204676647b3c197b93ff2318e300ac9cd313ab423c582a6fcf999e09217aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singlePlacementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a137850be7e93fa258f1325a98eb7bfd6887e3cd27abe6804a573093d3cc9cbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a268b1930c7985cb015760bc0627d6b58591316c1c7f7b498bb447407510289d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab36953650360391e45570d85ffebb51fdc07818b3a9248e228d3f9465fe438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2a41edff6da465ce6631994d66e69a1fa2b7eda9af575e3816ec7eab08e6a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeMode")
    def upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeMode"))

    @upgrade_mode.setter
    def upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73bf7d363ad6732b8e6ec3925d9641102d15ee8596a1ce244a5a9ee86ba77ca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class WindowsVirtualMachineScaleSetAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#ultra_ssd_enabled WindowsVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e806b23fdf97909cc1e4e8aa7d8a557bea8b8327c171646875655b1624ef8c91)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#ultra_ssd_enabled WindowsVirtualMachineScaleSet#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetAdditionalCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__daa6aa0e9de500f76bc356d0dc4c03aa18d82fd9ae090d98ac9b938c2b4e91bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f01100aceb1870e8f6a7c2ee4759c54fd0b61e450e210fd9ac2e5e1700697923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64f468eaeef2c6ca9512d3249da6b4a572fec847d640a41a2fa1c52f45b75b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAdditionalUnattendContent",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "setting": "setting"},
)
class WindowsVirtualMachineScaleSetAdditionalUnattendContent:
    def __init__(self, *, content: builtins.str, setting: builtins.str) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#content WindowsVirtualMachineScaleSet#content}.
        :param setting: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#setting WindowsVirtualMachineScaleSet#setting}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1831b893fdeb0e916654f3798130bd5bd0405d695eaffd6d0fc7bbf0ad2033d4)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument setting", value=setting, expected_type=type_hints["setting"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "setting": setting,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#content WindowsVirtualMachineScaleSet#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#setting WindowsVirtualMachineScaleSet#setting}.'''
        result = self._values.get("setting")
        assert result is not None, "Required property 'setting' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetAdditionalUnattendContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetAdditionalUnattendContentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAdditionalUnattendContentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e3c0cfc98381a028971289161d44fdfa4fb1c7181ce0f149bd462fe3c36070b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetAdditionalUnattendContentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d06ec9f1408ca8325adc35ab17dc955816fc9cd16263e81036ee9f33caded8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetAdditionalUnattendContentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b720fae0e80c520a3c19cdc827826b3c277161276183757111180471c1cb1b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d3e91723d8d0fe815ece2ec1e678e27d46bb262e8fab97225c32098e31bfe68)
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
            type_hints = typing.get_type_hints(_typecheckingstub__febcadd7c10829301906f53d9d7f1f8342f26b54e213c39971a9a54ebb3aa315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9e4c0e4d3cfc5cbadb6568d66aa934ce99050376f95810eb7681908bd30162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetAdditionalUnattendContentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAdditionalUnattendContentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b665ffe5cc75d82523c5ca0a84395f78be1b3f31ec4c2e296f18e2b0c00e2393)
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
            type_hints = typing.get_type_hints(_typecheckingstub__baf29c85eec1acd2e248d3a8976b74487d6d61384504cf1597199cd2d460b236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="setting")
    def setting(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setting"))

    @setting.setter
    def setting(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe92668958d25555fab24c6de9564d16c6c6c411eeb19dca66cb540fcdc19be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setting", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b421b7af11174ba58fab97ed19347515c04b0407c7090f0cf7253c989f1ac03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAutomaticInstanceRepair",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "grace_period": "gracePeriod"},
)
class WindowsVirtualMachineScaleSetAutomaticInstanceRepair:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#grace_period WindowsVirtualMachineScaleSet#grace_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ffe2c5d4853b1ffd9953bc11377bef15bb95fb400b2096b5f0c2e7e7cf95c1)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if grace_period is not None:
            self._values["grace_period"] = grace_period

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#grace_period WindowsVirtualMachineScaleSet#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetAutomaticInstanceRepair(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetAutomaticInstanceRepairOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9789a7a68785ab499a56b4a6216232aac7907de484e0e6140ea047c37a29dd0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracePeriodInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0ee3d1b74ca8ce5d9c482c0f9434214e89412040ff9253826b7a1587a75be144)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb7be908f0ea19560114d8614fb3f0144a01fc782a826206b2ed71ef7718965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47650057875da4baabfab8c86457fbd31f24f8e938ab491bbdd98bbaf091489b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disable_automatic_rollback": "disableAutomaticRollback",
        "enable_automatic_os_upgrade": "enableAutomaticOsUpgrade",
    },
)
class WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy:
    def __init__(
        self,
        *,
        disable_automatic_rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        enable_automatic_os_upgrade: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disable_automatic_rollback WindowsVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_os_upgrade WindowsVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d9102dedf4bcc6b950b331488a53f593c40e7850e7219fee2598024c15b9d9)
            check_type(argname="argument disable_automatic_rollback", value=disable_automatic_rollback, expected_type=type_hints["disable_automatic_rollback"])
            check_type(argname="argument enable_automatic_os_upgrade", value=enable_automatic_os_upgrade, expected_type=type_hints["enable_automatic_os_upgrade"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disable_automatic_rollback": disable_automatic_rollback,
            "enable_automatic_os_upgrade": enable_automatic_os_upgrade,
        }

    @builtins.property
    def disable_automatic_rollback(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disable_automatic_rollback WindowsVirtualMachineScaleSet#disable_automatic_rollback}.'''
        result = self._values.get("disable_automatic_rollback")
        assert result is not None, "Required property 'disable_automatic_rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def enable_automatic_os_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_os_upgrade WindowsVirtualMachineScaleSet#enable_automatic_os_upgrade}.'''
        result = self._values.get("enable_automatic_os_upgrade")
        assert result is not None, "Required property 'enable_automatic_os_upgrade' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87467c643e5d2362e7c394918a7094dfed3a82fea7676158af726c37fd895333)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disableAutomaticRollbackInput")
    def disable_automatic_rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableAutomaticRollbackInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticOsUpgradeInput")
    def enable_automatic_os_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAutomaticOsUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="disableAutomaticRollback")
    def disable_automatic_rollback(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableAutomaticRollback"))

    @disable_automatic_rollback.setter
    def disable_automatic_rollback(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e632b3943b7f9e9c663d5edc41fbf9b76aa89c09f303abb2cab3aba562160ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableAutomaticRollback", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticOsUpgrade")
    def enable_automatic_os_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAutomaticOsUpgrade"))

    @enable_automatic_os_upgrade.setter
    def enable_automatic_os_upgrade(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__588b4d02ce36280d44169aeb4257192ed9af0c8b62ddcc8bc171d95ffd7b701c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticOsUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b1c006bf5607c5a65d22d48aaaac90fbbf4e86e2010639140c9cfd81a19afdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class WindowsVirtualMachineScaleSetBootDiagnostics:
    def __init__(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_uri WindowsVirtualMachineScaleSet#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87552489d38e9a3dc7bb4adebd920691c501012203960d64425fc9f4dee9c5cd)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_account_uri": storage_account_uri,
        }

    @builtins.property
    def storage_account_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_uri WindowsVirtualMachineScaleSet#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        assert result is not None, "Required property 'storage_account_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetBootDiagnosticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__49113947ae3ecda6bb2fe778f53152b731de24975411c53390eb12689dd9dfa9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__66591c167ae4e873bc88df06628036b7d6a2dee3b6ae991edf5cf51f3c8080af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4131be9b8a8a7195e0b2e5d478d0e53c05d83117bf2be7ada47e9c766787cb28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetConfig",
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
        "instances": "instances",
        "location": "location",
        "name": "name",
        "network_interface": "networkInterface",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "additional_capabilities": "additionalCapabilities",
        "additional_unattend_content": "additionalUnattendContent",
        "automatic_instance_repair": "automaticInstanceRepair",
        "automatic_os_upgrade_policy": "automaticOsUpgradePolicy",
        "boot_diagnostics": "bootDiagnostics",
        "computer_name_prefix": "computerNamePrefix",
        "custom_data": "customData",
        "data_disk": "dataDisk",
        "do_not_run_extensions_on_overprovisioned_machines": "doNotRunExtensionsOnOverprovisionedMachines",
        "enable_automatic_updates": "enableAutomaticUpdates",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "extension": "extension",
        "health_probe_id": "healthProbeId",
        "id": "id",
        "license_type": "licenseType",
        "overprovision": "overprovision",
        "plan": "plan",
        "platform_fault_domain_count": "platformFaultDomainCount",
        "provision_vm_agent": "provisionVmAgent",
        "scale_in_policy": "scaleInPolicy",
        "secret": "secret",
        "single_placement_group": "singlePlacementGroup",
        "source_image_id": "sourceImageId",
        "source_image_reference": "sourceImageReference",
        "tags": "tags",
        "terminate_notification": "terminateNotification",
        "timeouts": "timeouts",
        "timezone": "timezone",
        "upgrade_mode": "upgradeMode",
        "winrm_listener": "winrmListener",
    },
)
class WindowsVirtualMachineScaleSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        os_disk: typing.Union["WindowsVirtualMachineScaleSetOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetPlan", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTerminateNotification", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
        winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetWinrmListener", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_password WindowsVirtualMachineScaleSet#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_username WindowsVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#instances WindowsVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#location WindowsVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#network_interface WindowsVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#os_disk WindowsVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#resource_group_name WindowsVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_capabilities WindowsVirtualMachineScaleSet#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_unattend_content WindowsVirtualMachineScaleSet#additional_unattend_content}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_instance_repair WindowsVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_os_upgrade_policy WindowsVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#boot_diagnostics WindowsVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#computer_name_prefix WindowsVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#custom_data WindowsVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#data_disk WindowsVirtualMachineScaleSet#data_disk}
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines WindowsVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_updates WindowsVirtualMachineScaleSet#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#encryption_at_host_enabled WindowsVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#extension WindowsVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#health_probe_id WindowsVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#id WindowsVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#license_type WindowsVirtualMachineScaleSet#license_type}.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#overprovision WindowsVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#plan WindowsVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#platform_fault_domain_count WindowsVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#provision_vm_agent WindowsVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#scale_in_policy WindowsVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#secret WindowsVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#single_placement_group WindowsVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_id WindowsVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_reference WindowsVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#tags WindowsVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#terminate_notification WindowsVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeouts WindowsVirtualMachineScaleSet#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timezone WindowsVirtualMachineScaleSet#timezone}.
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#upgrade_mode WindowsVirtualMachineScaleSet#upgrade_mode}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#winrm_listener WindowsVirtualMachineScaleSet#winrm_listener}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = WindowsVirtualMachineScaleSetOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = WindowsVirtualMachineScaleSetAdditionalCapabilities(**additional_capabilities)
        if isinstance(automatic_instance_repair, dict):
            automatic_instance_repair = WindowsVirtualMachineScaleSetAutomaticInstanceRepair(**automatic_instance_repair)
        if isinstance(automatic_os_upgrade_policy, dict):
            automatic_os_upgrade_policy = WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy(**automatic_os_upgrade_policy)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = WindowsVirtualMachineScaleSetBootDiagnostics(**boot_diagnostics)
        if isinstance(plan, dict):
            plan = WindowsVirtualMachineScaleSetPlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = WindowsVirtualMachineScaleSetSourceImageReference(**source_image_reference)
        if isinstance(terminate_notification, dict):
            terminate_notification = WindowsVirtualMachineScaleSetTerminateNotification(**terminate_notification)
        if isinstance(timeouts, dict):
            timeouts = WindowsVirtualMachineScaleSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a6b5b16b2a6b4f0289b611ceca7ad07d3dea7b5b15710056f8c822b2dd3890f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument additional_unattend_content", value=additional_unattend_content, expected_type=type_hints["additional_unattend_content"])
            check_type(argname="argument automatic_instance_repair", value=automatic_instance_repair, expected_type=type_hints["automatic_instance_repair"])
            check_type(argname="argument automatic_os_upgrade_policy", value=automatic_os_upgrade_policy, expected_type=type_hints["automatic_os_upgrade_policy"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument computer_name_prefix", value=computer_name_prefix, expected_type=type_hints["computer_name_prefix"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument data_disk", value=data_disk, expected_type=type_hints["data_disk"])
            check_type(argname="argument do_not_run_extensions_on_overprovisioned_machines", value=do_not_run_extensions_on_overprovisioned_machines, expected_type=type_hints["do_not_run_extensions_on_overprovisioned_machines"])
            check_type(argname="argument enable_automatic_updates", value=enable_automatic_updates, expected_type=type_hints["enable_automatic_updates"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument health_probe_id", value=health_probe_id, expected_type=type_hints["health_probe_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument overprovision", value=overprovision, expected_type=type_hints["overprovision"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument platform_fault_domain_count", value=platform_fault_domain_count, expected_type=type_hints["platform_fault_domain_count"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument single_placement_group", value=single_placement_group, expected_type=type_hints["single_placement_group"])
            check_type(argname="argument source_image_id", value=source_image_id, expected_type=type_hints["source_image_id"])
            check_type(argname="argument source_image_reference", value=source_image_reference, expected_type=type_hints["source_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument terminate_notification", value=terminate_notification, expected_type=type_hints["terminate_notification"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument upgrade_mode", value=upgrade_mode, expected_type=type_hints["upgrade_mode"])
            check_type(argname="argument winrm_listener", value=winrm_listener, expected_type=type_hints["winrm_listener"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_password": admin_password,
            "admin_username": admin_username,
            "instances": instances,
            "location": location,
            "name": name,
            "network_interface": network_interface,
            "os_disk": os_disk,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if automatic_instance_repair is not None:
            self._values["automatic_instance_repair"] = automatic_instance_repair
        if automatic_os_upgrade_policy is not None:
            self._values["automatic_os_upgrade_policy"] = automatic_os_upgrade_policy
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if computer_name_prefix is not None:
            self._values["computer_name_prefix"] = computer_name_prefix
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if data_disk is not None:
            self._values["data_disk"] = data_disk
        if do_not_run_extensions_on_overprovisioned_machines is not None:
            self._values["do_not_run_extensions_on_overprovisioned_machines"] = do_not_run_extensions_on_overprovisioned_machines
        if enable_automatic_updates is not None:
            self._values["enable_automatic_updates"] = enable_automatic_updates
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if extension is not None:
            self._values["extension"] = extension
        if health_probe_id is not None:
            self._values["health_probe_id"] = health_probe_id
        if id is not None:
            self._values["id"] = id
        if license_type is not None:
            self._values["license_type"] = license_type
        if overprovision is not None:
            self._values["overprovision"] = overprovision
        if plan is not None:
            self._values["plan"] = plan
        if platform_fault_domain_count is not None:
            self._values["platform_fault_domain_count"] = platform_fault_domain_count
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if scale_in_policy is not None:
            self._values["scale_in_policy"] = scale_in_policy
        if secret is not None:
            self._values["secret"] = secret
        if single_placement_group is not None:
            self._values["single_placement_group"] = single_placement_group
        if source_image_id is not None:
            self._values["source_image_id"] = source_image_id
        if source_image_reference is not None:
            self._values["source_image_reference"] = source_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if terminate_notification is not None:
            self._values["terminate_notification"] = terminate_notification
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone is not None:
            self._values["timezone"] = timezone
        if upgrade_mode is not None:
            self._values["upgrade_mode"] = upgrade_mode
        if winrm_listener is not None:
            self._values["winrm_listener"] = winrm_listener

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_password WindowsVirtualMachineScaleSet#admin_password}.'''
        result = self._values.get("admin_password")
        assert result is not None, "Required property 'admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#admin_username WindowsVirtualMachineScaleSet#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#instances WindowsVirtualMachineScaleSet#instances}.'''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#location WindowsVirtualMachineScaleSet#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterface"]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#network_interface WindowsVirtualMachineScaleSet#network_interface}
        '''
        result = self._values.get("network_interface")
        assert result is not None, "Required property 'network_interface' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterface"]], result)

    @builtins.property
    def os_disk(self) -> "WindowsVirtualMachineScaleSetOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#os_disk WindowsVirtualMachineScaleSet#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("WindowsVirtualMachineScaleSetOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#resource_group_name WindowsVirtualMachineScaleSet#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_capabilities WindowsVirtualMachineScaleSet#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities], result)

    @builtins.property
    def additional_unattend_content(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]]:
        '''additional_unattend_content block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#additional_unattend_content WindowsVirtualMachineScaleSet#additional_unattend_content}
        '''
        result = self._values.get("additional_unattend_content")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]], result)

    @builtins.property
    def automatic_instance_repair(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair]:
        '''automatic_instance_repair block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_instance_repair WindowsVirtualMachineScaleSet#automatic_instance_repair}
        '''
        result = self._values.get("automatic_instance_repair")
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair], result)

    @builtins.property
    def automatic_os_upgrade_policy(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        '''automatic_os_upgrade_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_os_upgrade_policy WindowsVirtualMachineScaleSet#automatic_os_upgrade_policy}
        '''
        result = self._values.get("automatic_os_upgrade_policy")
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy], result)

    @builtins.property
    def boot_diagnostics(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#boot_diagnostics WindowsVirtualMachineScaleSet#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics], result)

    @builtins.property
    def computer_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#computer_name_prefix WindowsVirtualMachineScaleSet#computer_name_prefix}.'''
        result = self._values.get("computer_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#custom_data WindowsVirtualMachineScaleSet#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetDataDisk"]]]:
        '''data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#data_disk WindowsVirtualMachineScaleSet#data_disk}
        '''
        result = self._values.get("data_disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetDataDisk"]]], result)

    @builtins.property
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines WindowsVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.'''
        result = self._values.get("do_not_run_extensions_on_overprovisioned_machines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_automatic_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_automatic_updates WindowsVirtualMachineScaleSet#enable_automatic_updates}.'''
        result = self._values.get("enable_automatic_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#encryption_at_host_enabled WindowsVirtualMachineScaleSet#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#extension WindowsVirtualMachineScaleSet#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetExtension"]]], result)

    @builtins.property
    def health_probe_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#health_probe_id WindowsVirtualMachineScaleSet#health_probe_id}.'''
        result = self._values.get("health_probe_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#id WindowsVirtualMachineScaleSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#license_type WindowsVirtualMachineScaleSet#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#overprovision WindowsVirtualMachineScaleSet#overprovision}.'''
        result = self._values.get("overprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional["WindowsVirtualMachineScaleSetPlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#plan WindowsVirtualMachineScaleSet#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetPlan"], result)

    @builtins.property
    def platform_fault_domain_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#platform_fault_domain_count WindowsVirtualMachineScaleSet#platform_fault_domain_count}.'''
        result = self._values.get("platform_fault_domain_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#provision_vm_agent WindowsVirtualMachineScaleSet#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def scale_in_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#scale_in_policy WindowsVirtualMachineScaleSet#scale_in_policy}.'''
        result = self._values.get("scale_in_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#secret WindowsVirtualMachineScaleSet#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecret"]]], result)

    @builtins.property
    def single_placement_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#single_placement_group WindowsVirtualMachineScaleSet#single_placement_group}.'''
        result = self._values.get("single_placement_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_id WindowsVirtualMachineScaleSet#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#source_image_reference WindowsVirtualMachineScaleSet#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#tags WindowsVirtualMachineScaleSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_notification(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetTerminateNotification"]:
        '''terminate_notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#terminate_notification WindowsVirtualMachineScaleSet#terminate_notification}
        '''
        result = self._values.get("terminate_notification")
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetTerminateNotification"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WindowsVirtualMachineScaleSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeouts WindowsVirtualMachineScaleSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetTimeouts"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timezone WindowsVirtualMachineScaleSet#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def upgrade_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#upgrade_mode WindowsVirtualMachineScaleSet#upgrade_mode}.'''
        result = self._values.get("upgrade_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def winrm_listener(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetWinrmListener"]]]:
        '''winrm_listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#winrm_listener WindowsVirtualMachineScaleSet#winrm_listener}
        '''
        result = self._values.get("winrm_listener")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetWinrmListener"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "disk_size_gb": "diskSizeGb",
        "lun": "lun",
        "storage_account_type": "storageAccountType",
        "create_option": "createOption",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class WindowsVirtualMachineScaleSetDataDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        disk_size_gb: jsii.Number,
        lun: jsii.Number,
        storage_account_type: builtins.str,
        create_option: typing.Optional[builtins.str] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#caching WindowsVirtualMachineScaleSet#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_size_gb WindowsVirtualMachineScaleSet#disk_size_gb}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#lun WindowsVirtualMachineScaleSet#lun}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_type WindowsVirtualMachineScaleSet#storage_account_type}.
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#create_option WindowsVirtualMachineScaleSet#create_option}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_encryption_set_id WindowsVirtualMachineScaleSet#disk_encryption_set_id}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#write_accelerator_enabled WindowsVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee552332a4c7d1cc2dd57818e601d9334dacf64154c3c0522ae24343c5252fd)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "caching": caching,
            "disk_size_gb": disk_size_gb,
            "lun": lun,
            "storage_account_type": storage_account_type,
        }
        if create_option is not None:
            self._values["create_option"] = create_option
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#caching WindowsVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_size_gb WindowsVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        assert result is not None, "Required property 'disk_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#lun WindowsVirtualMachineScaleSet#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_type WindowsVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#create_option WindowsVirtualMachineScaleSet#create_option}.'''
        result = self._values.get("create_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_encryption_set_id WindowsVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#write_accelerator_enabled WindowsVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetDataDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetDataDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__819c4fd9e6045d0a70e967f7e4bd94e1252f2b30867f2f61524c36ed0503e9ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df79473a51c9d02ae0abcfff1691a24cd052d5f27e5512580722e0fc0552806)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__647ac1d6ad691552dd2c7f16cd4ef22e152ea4e9033a877f5e927801c25a7589)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c2436f256e0f058d24d13979e92f5063e581e927e1ac1d6396c32835c3d6655)
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
            type_hints = typing.get_type_hints(_typecheckingstub__115fd28345f5744afbfc12df13598104ec305075dbaeee031658ab86e7405d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd5f58063080a738ac87e6de1ff022e548156c1b56f628cd4ae414b27d3c3a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetDataDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__568a3d7722f076ccb91c50b6ec2e0f7d3f46b40a1dfb4efa1e356c33b651f5f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCreateOption")
    def reset_create_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateOption", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

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
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__eb5a721975d78b80a6434e187ba30dc8e843a524a7cd5932e9e2131cca990310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28acb7c7369adb0451c5ef53f9cf4ec01256f30fc37e1afb1cffb9ba256ddc03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa14dede692b50c157d14cdf37f08e0664b7dad9cd4f81876d9ac7c03c03f695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaed6f0f8ef480e0a35761fad4116b3d73d80c02e8b74fd7dee67da172c0c9f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2526214d05b38eda8f088afba206f2c4a1f5bbd9f4c0948da278150a0e302be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db7679bfc68d541ba1e1d02a52a8d1612e0d73bcff5da3dbb3222731d30fc14d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f8d52765c0426fb9c9bd6a0ec975351099418df9693d9c454e668adeb9ab45b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f213f217de6311f52cfe326185110758e4602b345644a03652279a2bd3b358a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetExtension",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "publisher": "publisher",
        "type": "type",
        "type_handler_version": "typeHandlerVersion",
        "automatic_upgrade_enabled": "automaticUpgradeEnabled",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "force_update_tag": "forceUpdateTag",
        "protected_settings": "protectedSettings",
        "provision_after_extensions": "provisionAfterExtensions",
        "settings": "settings",
    },
)
class WindowsVirtualMachineScaleSetExtension:
    def __init__(
        self,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        automatic_upgrade_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_update_tag: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        provision_after_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#type WindowsVirtualMachineScaleSet#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#type_handler_version WindowsVirtualMachineScaleSet#type_handler_version}.
        :param automatic_upgrade_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_upgrade_enabled WindowsVirtualMachineScaleSet#automatic_upgrade_enabled}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#auto_upgrade_minor_version WindowsVirtualMachineScaleSet#auto_upgrade_minor_version}.
        :param force_update_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#force_update_tag WindowsVirtualMachineScaleSet#force_update_tag}.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#protected_settings WindowsVirtualMachineScaleSet#protected_settings}.
        :param provision_after_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#provision_after_extensions WindowsVirtualMachineScaleSet#provision_after_extensions}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#settings WindowsVirtualMachineScaleSet#settings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e831db4e5579b98594c29526f4d83190d2b4e1a98937523f19fcafb7d77b122)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_handler_version", value=type_handler_version, expected_type=type_hints["type_handler_version"])
            check_type(argname="argument automatic_upgrade_enabled", value=automatic_upgrade_enabled, expected_type=type_hints["automatic_upgrade_enabled"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument force_update_tag", value=force_update_tag, expected_type=type_hints["force_update_tag"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument provision_after_extensions", value=provision_after_extensions, expected_type=type_hints["provision_after_extensions"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
            "type_handler_version": type_handler_version,
        }
        if automatic_upgrade_enabled is not None:
            self._values["automatic_upgrade_enabled"] = automatic_upgrade_enabled
        if auto_upgrade_minor_version is not None:
            self._values["auto_upgrade_minor_version"] = auto_upgrade_minor_version
        if force_update_tag is not None:
            self._values["force_update_tag"] = force_update_tag
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if provision_after_extensions is not None:
            self._values["provision_after_extensions"] = provision_after_extensions
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#type WindowsVirtualMachineScaleSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#type_handler_version WindowsVirtualMachineScaleSet#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_upgrade_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#automatic_upgrade_enabled WindowsVirtualMachineScaleSet#automatic_upgrade_enabled}.'''
        result = self._values.get("automatic_upgrade_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#auto_upgrade_minor_version WindowsVirtualMachineScaleSet#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_update_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#force_update_tag WindowsVirtualMachineScaleSet#force_update_tag}.'''
        result = self._values.get("force_update_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#protected_settings WindowsVirtualMachineScaleSet#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_after_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#provision_after_extensions WindowsVirtualMachineScaleSet#provision_after_extensions}.'''
        result = self._values.get("provision_after_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#settings WindowsVirtualMachineScaleSet#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetExtensionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetExtensionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaaaea3d4065a4c0ce869acdc452a9ef45aa844ac18b840e7b53faad4d11eae9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d3eb2f05fb09ee6a235ce67427a9207efcf2effc1a4d1af4b87fd8db9f8ffc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d9d771ec212b393f15987477c5751e2e343b9bf6d774f28c6e05423b9e5d5f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30812cc981e9f590f8c2fad786a102846edee714e4423f03d12e2822ad471a31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__301e51d0622a6f5aeb2248c23a8e3843c9d6f8239c864c4ccbfa3bc2870ae48b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetExtension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ebfa4ff28c32984c60638f39c400562e9f8e77b48636f22ecfbf04de8ac5d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetExtensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetExtensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a89fa59e16f02db85d91a29892c8580e7e40cc17c558c1929667524226c7904)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutomaticUpgradeEnabled")
    def reset_automatic_upgrade_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticUpgradeEnabled", []))

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetForceUpdateTag")
    def reset_force_update_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceUpdateTag", []))

    @jsii.member(jsii_name="resetProtectedSettings")
    def reset_protected_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedSettings", []))

    @jsii.member(jsii_name="resetProvisionAfterExtensions")
    def reset_provision_after_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionAfterExtensions", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="automaticUpgradeEnabledInput")
    def automatic_upgrade_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "automaticUpgradeEnabledInput"))

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
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedSettingsInput")
    def protected_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensionsInput")
    def provision_after_extensions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "provisionAfterExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersionInput")
    def type_handler_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeHandlerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticUpgradeEnabled")
    def automatic_upgrade_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "automaticUpgradeEnabled"))

    @automatic_upgrade_enabled.setter
    def automatic_upgrade_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66da741f79fb699a27196b08ad2612f96e0c2226a07e954758f2504568cb8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticUpgradeEnabled", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__2b7e2ace9e9a8d69e795daba8a171968dbeb6d66eaaab90da0ec59d8571a3625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTag")
    def force_update_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceUpdateTag"))

    @force_update_tag.setter
    def force_update_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa5bd03c83ea366a71774147a5183e72f74e1c8d1e45e91c3dfdb14375ebf89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdateTag", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a739e9cff5797c0ad5b7b57f9f6cf4539e0f0232b05ada578f8e0d7ce1112c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391bb849b1ae5e67ca642756eca3fa6ee81ef4ed77b7912a961a0ba624b3f398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensions")
    def provision_after_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisionAfterExtensions"))

    @provision_after_extensions.setter
    def provision_after_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1771c85db1e503c863ccb23844fd0810ff010c8e7e95894c933928433e0edf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionAfterExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049c4c0b89ca1397c4221a0e259a351fb9ac2023f5088159875f19bc639d6a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479fa5fd96efe9506b17a20d9e340956486c36bfab90522b7de6e6f71b9fa70d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe8df59869b335d807888321da6311998289aa64a08f4513069eae3530a7661a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a20658c00f0e7ef67a54fff192db4def6e05cfb9181bca364afd0194ac8e944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0516d43fc06b031cc5fbe73886f982b9259235f87601ffc163016f581b64bc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "ip_configuration": "ipConfiguration",
        "name": "name",
        "dns_servers": "dnsServers",
        "enable_ip_forwarding": "enableIpForwarding",
        "network_security_group_id": "networkSecurityGroupId",
        "primary": "primary",
    },
)
class WindowsVirtualMachineScaleSetNetworkInterface:
    def __init__(
        self,
        *,
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_security_group_id: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#ip_configuration WindowsVirtualMachineScaleSet#ip_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#dns_servers WindowsVirtualMachineScaleSet#dns_servers}.
        :param enable_ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_ip_forwarding WindowsVirtualMachineScaleSet#enable_ip_forwarding}.
        :param network_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#network_security_group_id WindowsVirtualMachineScaleSet#network_security_group_id}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#primary WindowsVirtualMachineScaleSet#primary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b4600fd4d24c8eb182f1579cf6c4cd169cdf3ef94e3cbdd629d2436b57ebed)
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument enable_ip_forwarding", value=enable_ip_forwarding, expected_type=type_hints["enable_ip_forwarding"])
            check_type(argname="argument network_security_group_id", value=network_security_group_id, expected_type=type_hints["network_security_group_id"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "name": name,
        }
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if enable_ip_forwarding is not None:
            self._values["enable_ip_forwarding"] = enable_ip_forwarding
        if network_security_group_id is not None:
            self._values["network_security_group_id"] = network_security_group_id
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#ip_configuration WindowsVirtualMachineScaleSet#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#dns_servers WindowsVirtualMachineScaleSet#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enable_ip_forwarding WindowsVirtualMachineScaleSet#enable_ip_forwarding}.'''
        result = self._values.get("enable_ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#network_security_group_id WindowsVirtualMachineScaleSet#network_security_group_id}.'''
        result = self._values.get("network_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#primary WindowsVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "load_balancer_backend_address_pool_ids": "loadBalancerBackendAddressPoolIds",
        "load_balancer_inbound_nat_rules_ids": "loadBalancerInboundNatRulesIds",
        "primary": "primary",
        "subnet_id": "subnetId",
        "version": "version",
    },
)
class WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        load_balancer_backend_address_pool_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_inbound_nat_rules_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param load_balancer_backend_address_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#load_balancer_backend_address_pool_ids WindowsVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.
        :param load_balancer_inbound_nat_rules_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids WindowsVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#primary WindowsVirtualMachineScaleSet#primary}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#subnet_id WindowsVirtualMachineScaleSet#subnet_id}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#version WindowsVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b567f6e9eafa85a6a61f5adb254e1254ffb21fb25daccc774887e590af20c48)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument load_balancer_backend_address_pool_ids", value=load_balancer_backend_address_pool_ids, expected_type=type_hints["load_balancer_backend_address_pool_ids"])
            check_type(argname="argument load_balancer_inbound_nat_rules_ids", value=load_balancer_inbound_nat_rules_ids, expected_type=type_hints["load_balancer_inbound_nat_rules_ids"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if load_balancer_backend_address_pool_ids is not None:
            self._values["load_balancer_backend_address_pool_ids"] = load_balancer_backend_address_pool_ids
        if load_balancer_inbound_nat_rules_ids is not None:
            self._values["load_balancer_inbound_nat_rules_ids"] = load_balancer_inbound_nat_rules_ids
        if primary is not None:
            self._values["primary"] = primary
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_backend_address_pool_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#load_balancer_backend_address_pool_ids WindowsVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.'''
        result = self._values.get("load_balancer_backend_address_pool_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_inbound_nat_rules_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids WindowsVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.'''
        result = self._values.get("load_balancer_inbound_nat_rules_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#primary WindowsVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#subnet_id WindowsVirtualMachineScaleSet#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#version WindowsVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f0866782b46f8cc44bc56564c0c8ef9b69867285b9e49fdfebe1b7015be0c36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7815fe126f3cdec0c8b938089d5acebb30ce3f800b3c39d4dfd2abdf87a30a32)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c8d72f4dc1585cc6e529090b4cdcccd6b2bf0d4fafce85299e39aee5b174e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__55dc1dde789691d83b12fa9a65c4734f8ba681d811bfe41199db317b4b2b9379)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df70300cd20125f9577563f5b8de64b3999744a04b957aee680bdd90fb3ab81b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__507480717d7d685de0adb4507a367fb75df6d6b38d4ed863bd398c282f1d0d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2eb891188edf0cfcbb501f31cd292f500903a149df3820457f23e81a1b67f1de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLoadBalancerBackendAddressPoolIds")
    def reset_load_balancer_backend_address_pool_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerBackendAddressPoolIds", []))

    @jsii.member(jsii_name="resetLoadBalancerInboundNatRulesIds")
    def reset_load_balancer_inbound_nat_rules_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerInboundNatRulesIds", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolIdsInput")
    def load_balancer_backend_address_pool_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerBackendAddressPoolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInboundNatRulesIdsInput")
    def load_balancer_inbound_nat_rules_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerInboundNatRulesIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolIds")
    def load_balancer_backend_address_pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerBackendAddressPoolIds"))

    @load_balancer_backend_address_pool_ids.setter
    def load_balancer_backend_address_pool_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca3fb06201fc0767130e7519d89d96c7e16b14591cbc69feb88bbc7e2dc34d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerBackendAddressPoolIds", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInboundNatRulesIds")
    def load_balancer_inbound_nat_rules_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerInboundNatRulesIds"))

    @load_balancer_inbound_nat_rules_ids.setter
    def load_balancer_inbound_nat_rules_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95d0f81597aa8a4e3d874fcda9b4fd4eed0388aae81f39e5add8f30c66f4bd06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerInboundNatRulesIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b03165dbf0391c38870e9794e8a7e2f5d4378f391608345a17aaaa5aa888d3f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f470cc84a9046100cc07773af16a86fe2bae6eeff99122b2a9672723d7d319da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c3612b11e84d11f4be7cd2fac1d1d42c348d69b0f1306dc1796fc55241ee97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89aad644a19f582d7b7d339dd2b6bb3de3899470d5cef6adec90e000ae858f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658e0b5cf6b31b757fcc5d32668da2219bf62c024b27211bdad8d5604fec5873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82a00e1aa3c25269dfd9e8915088eebc0874ff4c6382f83b013f7c5e8ac6bbba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cef38d74b39b1e4f528c3e3e42d154e34bf238380cc55d89d7d112b5ce03679)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0b7bfdfa7a1bb1505ad2a08db3c47beae0e4879370a1b7cb3f4d1d8b4029afd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86963956ebdf0394bde76d434175a396e70024ecc99e481d1b518e7be27b59fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1541c60d8fbc8b61fcb4255d8d3ed7dacb41b709f24de7c3186c0691299fc66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed46192076df48aac0865ae73cdb990ec4b00562a291076e7e29e678293a66ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c430277af92d7e4539541fbee079afb0f92471b92b0407cd07512f5bd6bcbda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b4ed8acf640e56b687cbe7f2514661678702991caec8333c678c94a868f3ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetEnableIpForwarding")
    def reset_enable_ip_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIpForwarding", []))

    @jsii.member(jsii_name="resetNetworkSecurityGroupId")
    def reset_network_security_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkSecurityGroupId", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationList:
        return typing.cast(WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIpForwardingInput")
    def enable_ip_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableIpForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupIdInput")
    def network_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7b3083a0d57d9585c908deba7f3f0279b64cc256489202524378da7f659d628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="enableIpForwarding")
    def enable_ip_forwarding(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableIpForwarding"))

    @enable_ip_forwarding.setter
    def enable_ip_forwarding(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb80b2ed550ac58519086d46f420add3bf1a450726d9160d1647df34024bea85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb439735faecdb9b35deda0176d71fa3e3e5d40450c26107ca7ff5b9a2acabb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupId")
    def network_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupId"))

    @network_security_group_id.setter
    def network_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7927ae9b2c2d60038d2f8d2abaa22b0306b454cfe698b637713f2e3a1d5d060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9bffdbdf26216f692cf810e464053cec449cf237a39168436edec0732ed2d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe29ff96cddb3646b7cdfd1c3f3c6a38e1d6784ccbc44812e18b99c549fdc24d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "storage_account_type": "storageAccountType",
        "diff_disk_settings": "diffDiskSettings",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "disk_size_gb": "diskSizeGb",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class WindowsVirtualMachineScaleSetOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#caching WindowsVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_type WindowsVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#diff_disk_settings WindowsVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_encryption_set_id WindowsVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_size_gb WindowsVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#write_accelerator_enabled WindowsVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9e5918278cfd7e36a4beace24e56857b1115aea84bb9598b28e1001578c5f79)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument diff_disk_settings", value=diff_disk_settings, expected_type=type_hints["diff_disk_settings"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
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
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#caching WindowsVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#storage_account_type WindowsVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#diff_disk_settings WindowsVirtualMachineScaleSet#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_encryption_set_id WindowsVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#disk_size_gb WindowsVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#write_accelerator_enabled WindowsVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option"},
)
class WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings:
    def __init__(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#option WindowsVirtualMachineScaleSet#option}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7890f4f129c3aa6fe533b00ac164a57bda4b2ee18df12f3cc5d78d55bb459ff4)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "option": option,
        }

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#option WindowsVirtualMachineScaleSet#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6021fbfbe8f7eec106bb9ef346019e99cc08392b99b5cd4c69c3660904b0487)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d26b473cfd94df98f1d87ad8cb6424214d2d3d338c0a303892c75d52352b0aa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ed001bc3b96d61420aa9b863317c11064d8250ac01500749d33629af4c51fcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd8a2ccd8d4fdd454847beab02091a663559e61fe256f99ae4030f0cf68cb315)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#option WindowsVirtualMachineScaleSet#option}.
        '''
        value = WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings(option=option)

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

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettings")
    def diff_disk_settings(
        self,
    ) -> WindowsVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(WindowsVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__21f03e2b2b5ae37f06c483ca838bb0777e654b1040b1a887ff7a4104e4e2032f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cfbbcb9f3d6af323580034dfb32eee68966ba02dfb49ca7071d257f313c7f85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d67961b736d944a33cfc51d06899579036ea3b7d72423c1dd52e391364635b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b6e6eaf26e835252bdb9890d44212f1cbfdb10ef6b5b1d84e52f23c1f0f859)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f68b61c632e65bcbb303139097bc2e2b0c585acd6259b4992858e4f536c601d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineScaleSetOsDisk]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0be88b74643ac54ad1103991b47af279bfbb76b0e0563fcc97f7c9410b72179)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetPlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class WindowsVirtualMachineScaleSetPlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#product WindowsVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89a5ecca61a853877a3238ff65e361039a4887c63fd2e7b472012be85817f31)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#name WindowsVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#product WindowsVirtualMachineScaleSet#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31c698ae3a96db107cccebb1b19a68c4fcd2329ae992a031565aeb6bebbdcf80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2a98fe8af97b7adad496f1d502d7949025aea94980bb7b6f7788795a1466ac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd1858a6bd27afae6d67007f2e2c797f225e38a89d08920b38dfbd202d69076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24b00a8f205e1f45d6f31be66e2a7d0bdc2abf75a59fb61bdba933c18db717c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineScaleSetPlan]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetPlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetPlan],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824de2895fe3f1a4129c91231fd7d19cd3efe8e1ea35d7bf02f030de485f1789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class WindowsVirtualMachineScaleSetSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineScaleSetSecretCertificate", typing.Dict[builtins.str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#certificate WindowsVirtualMachineScaleSet#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#key_vault_id WindowsVirtualMachineScaleSet#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3dc441b7b4ffda70b5a095b730c12ba1b5ff6b4435a05fcec730c32b6731723)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#certificate WindowsVirtualMachineScaleSet#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["WindowsVirtualMachineScaleSetSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#key_vault_id WindowsVirtualMachineScaleSet#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={"store": "store"},
)
class WindowsVirtualMachineScaleSetSecretCertificate:
    def __init__(self, *, store: builtins.str) -> None:
        '''
        :param store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#store WindowsVirtualMachineScaleSet#store}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98014f116dd7e8f129a05c006302d57770da4dd59433dd24f43224379b5d6fd1)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "store": store,
        }

    @builtins.property
    def store(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#store WindowsVirtualMachineScaleSet#store}.'''
        result = self._values.get("store")
        assert result is not None, "Required property 'store' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetSecretCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecretCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d33eabc31e51844366fc75a514acaf091a47a651a3710a2989a11cff8b97c534)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb2146b4cb5665c6857adfa4909a85b1bf960ba1ab4416655bf5d2560049a105)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2349c118254286d920ac6d8638a6c267a5d3fb477bec101d804c66932bc317)
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
            type_hints = typing.get_type_hints(_typecheckingstub__009ef964031135a2c5ed4a31d9546210552a3748efd201286b861c18d99491d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e443420df8a7c986cb3a32f3a48241850683347ed0d7949da336a52d659045b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c4538dbc4aa6b9bf5432886f4c002f4718ec7f9bee7c65dd41615972126e5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetSecretCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d155cf920b12e71ce6574d4776ddbc5d2de72759827072160975502fb9c1804)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2492053573f1aa3d2009278783f2e07ab783a676036831ec928956d82da3039c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "store", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722c3375b5ab841dfbb775d84a054cf7a753647bffeebc7a9a13c7f37e703291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetSecretList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecretList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac5ae2005595a3734671033a6d2d93a477b66225718880420d6123b94bc22d5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc927238b689921c8648dab6d46803ad6b5aa46fc9439547bcbfb6008180cb3e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff5deab5868a2702ad142c8023255cbf3e3e33576d9d7b3a3961586cdda1724)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c5b370934744adc489491c186cd49f5e2a1b96753fa405c574a433d52ad70af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c32002983c6e56a9c8169c6ad98c36434db20431908ac237c3891cd5d11ab033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecret]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__662025aeb636a4277fd601af18712f0c6de07b4e31beed3d861605c1b599316f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetSecretOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSecretOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1c97634955d6aacd09fdbf8bb9bb3c581bf51e9932236d08573e48d2cfa35f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a2ad487cf9db728d96a652e2153649917145315a9153b287056aa3da60cc12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> WindowsVirtualMachineScaleSetSecretCertificateList:
        return typing.cast(WindowsVirtualMachineScaleSetSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "certificateInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a7168ee7a4a8fa5fb132b6a05caba925f300d70ff519e4ad13a20f433c773342)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__326d8f3a7bbaa2462c9564848c6f76ec44d997057cb8c680c5e2dc88e37fef12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class WindowsVirtualMachineScaleSetSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#offer WindowsVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#version WindowsVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d151e4089a7f241215e8be372868a707033e321defc98bb07ec12243b8b771b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#offer WindowsVirtualMachineScaleSet#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#publisher WindowsVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#sku WindowsVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#version WindowsVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetSourceImageReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__422be347d730b4a29af59bffe1bb1b16dcb586b28dbf3abb525639d6d8c16362)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31db84e0161c4e8e84d57e43686a3f619e23b71ec55b2ffa11d42aa4c3bb998e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a11ba3f22dcefc497d5a9084dd53d1d02f1600f2b46f8a3ab309ab5c882181f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0641626ee4f5ad7fa6774dd66ab9496fdfcc7233a0524e778fdbda4d1f63b7f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc7de860ab7e1bb3c92d8ce0848b79fab3ff525ffc461fb685d020cbb891fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetSourceImageReference]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cceba7d853e9cde1f9a1867c5b7b55725a59923f8c5345b9730a8cc6a825253f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetTerminateNotification",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "timeout": "timeout"},
)
class WindowsVirtualMachineScaleSetTerminateNotification:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeout WindowsVirtualMachineScaleSet#timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93ebec2f7248d8689f25416d5949b8788cf3866056f6ac5e57c2260733e6007)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#enabled WindowsVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#timeout WindowsVirtualMachineScaleSet#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetTerminateNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetTerminateNotificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetTerminateNotificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bcdda4165133d2c3658178484b9625a8ef8e1a0af702469c6375606f1c3f248)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7e285d0d0be4ec9d47f3f82d043f6e7a107ceab64a304e487d67784ecd9b55c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4664818765f9e09ffd7178c3626bdbcc83ab96be0cfa8881517d898c75dc57cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineScaleSetTerminateNotification]:
        return typing.cast(typing.Optional[WindowsVirtualMachineScaleSetTerminateNotification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineScaleSetTerminateNotification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cb0dfaf720e3703acac1b285fd2c17c37016ac15e1c215cc56d4efaf6d8e3a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WindowsVirtualMachineScaleSetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#create WindowsVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#delete WindowsVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#read WindowsVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#update WindowsVirtualMachineScaleSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f19600558feede2a4df3ddb30084c3ee12a54319305d7ea3fe7227ad95514ea)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#create WindowsVirtualMachineScaleSet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#delete WindowsVirtualMachineScaleSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#read WindowsVirtualMachineScaleSet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#update WindowsVirtualMachineScaleSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4922f48de3bb2759d4c024f68762d2b8554394a2f35514a7142dfd76b6b02de6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6ec72918d2c3f9344fa2771ce4682c0571ddbdfb809d617d48819e331ef4d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bd446e1044f5608d2eacb6c6110f0d7863124ff539c68cfa6014b2faa3bfed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0269c0eb31bfe297f6e50ae1d5ea9cb65fc77d45aa328a3e7099e57b33048dca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6ed10e7e0187c12f94958837b0dea99c099aa5e9ec84b7d1cdb624f08fa4fee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1366545dd63deff718b730368c73e8c9017abf14a886c6c0d45deb42bbec502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetWinrmListener",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol"},
)
class WindowsVirtualMachineScaleSetWinrmListener:
    def __init__(self, *, protocol: builtins.str) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#protocol WindowsVirtualMachineScaleSet#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94a62074a153fdd92bb88dff62ea901b78a36a0e9c3f0b4c99d3b06097e1712)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protocol": protocol,
        }

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/windows_virtual_machine_scale_set#protocol WindowsVirtualMachineScaleSet#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineScaleSetWinrmListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineScaleSetWinrmListenerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetWinrmListenerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a562d4dd44e99ab2223506ea0b4cd482a7f5fac74662d1f70bdddb329cd02968)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineScaleSetWinrmListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26448f3258d812fede60a87f393085badf6280d4aa93fe39bd4652f2c722b306)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineScaleSetWinrmListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ba9fbef01b481f9864022f8755d2dfb6ac009a9f96a151840c1b50fb66ad61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf4b59711b71caf23d349a598677b0cad3221721130c339234b16b60e0b863d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b2e690e918f28f6070462859d666fc80d158f56d59bf2d559f8648f14905cfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetWinrmListener]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetWinrmListener]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetWinrmListener]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198b838f8a6c22e6f5285cdfd244a1ee66df021fb0734ddd7041e09a9eec536a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineScaleSetWinrmListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.windowsVirtualMachineScaleSet.WindowsVirtualMachineScaleSetWinrmListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bf9bac35e8461502df24c42ee48a62c38de9953f1caf4fff97992ef3150b4a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__926e2f1398d80ad886c44f15b491ac2cddbba60e3daff23a32dba78a9f9fd202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c045b4e73f9b1d34d238c050881f99cb17d8896b16987f211a712a6f1671e0c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WindowsVirtualMachineScaleSet",
    "WindowsVirtualMachineScaleSetAdditionalCapabilities",
    "WindowsVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
    "WindowsVirtualMachineScaleSetAdditionalUnattendContent",
    "WindowsVirtualMachineScaleSetAdditionalUnattendContentList",
    "WindowsVirtualMachineScaleSetAdditionalUnattendContentOutputReference",
    "WindowsVirtualMachineScaleSetAutomaticInstanceRepair",
    "WindowsVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
    "WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    "WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
    "WindowsVirtualMachineScaleSetBootDiagnostics",
    "WindowsVirtualMachineScaleSetBootDiagnosticsOutputReference",
    "WindowsVirtualMachineScaleSetConfig",
    "WindowsVirtualMachineScaleSetDataDisk",
    "WindowsVirtualMachineScaleSetDataDiskList",
    "WindowsVirtualMachineScaleSetDataDiskOutputReference",
    "WindowsVirtualMachineScaleSetExtension",
    "WindowsVirtualMachineScaleSetExtensionList",
    "WindowsVirtualMachineScaleSetExtensionOutputReference",
    "WindowsVirtualMachineScaleSetNetworkInterface",
    "WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
    "WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
    "WindowsVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
    "WindowsVirtualMachineScaleSetNetworkInterfaceList",
    "WindowsVirtualMachineScaleSetNetworkInterfaceOutputReference",
    "WindowsVirtualMachineScaleSetOsDisk",
    "WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings",
    "WindowsVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
    "WindowsVirtualMachineScaleSetOsDiskOutputReference",
    "WindowsVirtualMachineScaleSetPlan",
    "WindowsVirtualMachineScaleSetPlanOutputReference",
    "WindowsVirtualMachineScaleSetSecret",
    "WindowsVirtualMachineScaleSetSecretCertificate",
    "WindowsVirtualMachineScaleSetSecretCertificateList",
    "WindowsVirtualMachineScaleSetSecretCertificateOutputReference",
    "WindowsVirtualMachineScaleSetSecretList",
    "WindowsVirtualMachineScaleSetSecretOutputReference",
    "WindowsVirtualMachineScaleSetSourceImageReference",
    "WindowsVirtualMachineScaleSetSourceImageReferenceOutputReference",
    "WindowsVirtualMachineScaleSetTerminateNotification",
    "WindowsVirtualMachineScaleSetTerminateNotificationOutputReference",
    "WindowsVirtualMachineScaleSetTimeouts",
    "WindowsVirtualMachineScaleSetTimeoutsOutputReference",
    "WindowsVirtualMachineScaleSetWinrmListener",
    "WindowsVirtualMachineScaleSetWinrmListenerList",
    "WindowsVirtualMachineScaleSetWinrmListenerOutputReference",
]

publication.publish()

def _typecheckingstub__9e152b25cfd84de79a3ed40200a30e849f7c42b6e7ccbfaab23a81a762314ce7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_password: builtins.str,
    admin_username: builtins.str,
    instances: jsii.Number,
    location: builtins.str,
    name: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    os_disk: typing.Union[WindowsVirtualMachineScaleSetOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    sku: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    automatic_instance_repair: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
    automatic_os_upgrade_policy: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name_prefix: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]]] = None,
    health_probe_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetPlan, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_fault_domain_count: typing.Optional[jsii.Number] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scale_in_policy: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_notification: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTerminateNotification, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    upgrade_mode: typing.Optional[builtins.str] = None,
    winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__0747e95c20f740c8116a0afd00cdbce9506149c68e0477faac40205a17c900ed(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b04232ef6a93cd6cb51dd22ee56612531643b1af961b015a0feabc5aa115b3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55b172130493f9bf0c8b64e7726ad1d92be508b2d3b3e41c17073bd8963d66dd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e439f9395730cfe7d36e744ce13188b88606a2192ae3788fc8099fa045dd477(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e0780198f85067f1e22002a8ad682f7915a7a50f9baea7d7b794d9034c5fcc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96467d635d701e0a2da4b3641ccce7b3242fca61817622cbdbcd0d03ad55934(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941eee20b7b5bdd2eca0ad2c7ccda1fb080f46fd8d727cc2097024339db10376(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ed803ab7450ff5417752f1611a5c2fa16bc7cda2b3a6884b4bc3ef11f14113(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4c112dce6fad92c377690c2c7bf6292a0cefa0e0e614ea6ae395238dac62c23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202ce0ba4997ceaf1d10708986b8904def83085a9a884f4c7646ec80d92085c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__918167be0432a2ea7d01750fa7fb67c2f90de0e535543708abe0968c300ff703(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4498e7f9316209fd7dcbf14c706684e279c07af87de440d67f6afa9a8469e291(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f11b6471d0eb236830ee571a28c74332dbfd6baa3665e72adb868a53b5e5a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e0841f1d0725ec037ead63e9e08ef9da1b90bc5a391aef4af0ffde03456a7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093498b1ae63307033814181c91eeb8fbf1f4d831cdbd8efabbdc589c5ff7e2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624c7a676bb9b4a8094c1caf31c51927e84b1fc949566c7e09968473fed0bac2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fed0d0efeeea60826ee8989cd01e57789cb2122da68deb64cc1563772d71df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b8acae0a0f8e9db97e76ecf1da72287c8384f105f8a945988751714aae0e85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317f43e2e93a3c858c006127f06fdea6611a37a10d4f4a6ba97469caf0cd1ebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48c5c3d3b4a2b1c7c0143fcde0b4eda93953e06b2701d3f3797e8a8175c9e035(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6cff81858110eddf03357663e396a2a117aaccaee0ac0b2d9abff097dae84b7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618135cf8ff5cb75e8d4e7970e8ccbf9f7619dcb28b456892f0a6d07078a7a3b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2d3a94c97ee200e2a89094ecc2c0051abf2305fe51012efc3cf0531a01af3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f021ca0119f18ac3745b825bd71f483727df0abe5315d23802f372807e5120(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e1204676647b3c197b93ff2318e300ac9cd313ab423c582a6fcf999e09217aa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a137850be7e93fa258f1325a98eb7bfd6887e3cd27abe6804a573093d3cc9cbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a268b1930c7985cb015760bc0627d6b58591316c1c7f7b498bb447407510289d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab36953650360391e45570d85ffebb51fdc07818b3a9248e228d3f9465fe438(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2a41edff6da465ce6631994d66e69a1fa2b7eda9af575e3816ec7eab08e6a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73bf7d363ad6732b8e6ec3925d9641102d15ee8596a1ce244a5a9ee86ba77ca4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e806b23fdf97909cc1e4e8aa7d8a557bea8b8327c171646875655b1624ef8c91(
    *,
    ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa6aa0e9de500f76bc356d0dc4c03aa18d82fd9ae090d98ac9b938c2b4e91bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01100aceb1870e8f6a7c2ee4759c54fd0b61e450e210fd9ac2e5e1700697923(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64f468eaeef2c6ca9512d3249da6b4a572fec847d640a41a2fa1c52f45b75b0(
    value: typing.Optional[WindowsVirtualMachineScaleSetAdditionalCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1831b893fdeb0e916654f3798130bd5bd0405d695eaffd6d0fc7bbf0ad2033d4(
    *,
    content: builtins.str,
    setting: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e3c0cfc98381a028971289161d44fdfa4fb1c7181ce0f149bd462fe3c36070b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d06ec9f1408ca8325adc35ab17dc955816fc9cd16263e81036ee9f33caded8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b720fae0e80c520a3c19cdc827826b3c277161276183757111180471c1cb1b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d3e91723d8d0fe815ece2ec1e678e27d46bb262e8fab97225c32098e31bfe68(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febcadd7c10829301906f53d9d7f1f8342f26b54e213c39971a9a54ebb3aa315(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9e4c0e4d3cfc5cbadb6568d66aa934ce99050376f95810eb7681908bd30162(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetAdditionalUnattendContent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b665ffe5cc75d82523c5ca0a84395f78be1b3f31ec4c2e296f18e2b0c00e2393(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf29c85eec1acd2e248d3a8976b74487d6d61384504cf1597199cd2d460b236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe92668958d25555fab24c6de9564d16c6c6c411eeb19dca66cb540fcdc19be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b421b7af11174ba58fab97ed19347515c04b0407c7090f0cf7253c989f1ac03(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ffe2c5d4853b1ffd9953bc11377bef15bb95fb400b2096b5f0c2e7e7cf95c1(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    grace_period: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9789a7a68785ab499a56b4a6216232aac7907de484e0e6140ea047c37a29dd0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee3d1b74ca8ce5d9c482c0f9434214e89412040ff9253826b7a1587a75be144(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb7be908f0ea19560114d8614fb3f0144a01fc782a826206b2ed71ef7718965(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47650057875da4baabfab8c86457fbd31f24f8e938ab491bbdd98bbaf091489b(
    value: typing.Optional[WindowsVirtualMachineScaleSetAutomaticInstanceRepair],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d9102dedf4bcc6b950b331488a53f593c40e7850e7219fee2598024c15b9d9(
    *,
    disable_automatic_rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    enable_automatic_os_upgrade: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87467c643e5d2362e7c394918a7094dfed3a82fea7676158af726c37fd895333(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e632b3943b7f9e9c663d5edc41fbf9b76aa89c09f303abb2cab3aba562160ad(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__588b4d02ce36280d44169aeb4257192ed9af0c8b62ddcc8bc171d95ffd7b701c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b1c006bf5607c5a65d22d48aaaac90fbbf4e86e2010639140c9cfd81a19afdc(
    value: typing.Optional[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87552489d38e9a3dc7bb4adebd920691c501012203960d64425fc9f4dee9c5cd(
    *,
    storage_account_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49113947ae3ecda6bb2fe778f53152b731de24975411c53390eb12689dd9dfa9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66591c167ae4e873bc88df06628036b7d6a2dee3b6ae991edf5cf51f3c8080af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4131be9b8a8a7195e0b2e5d478d0e53c05d83117bf2be7ada47e9c766787cb28(
    value: typing.Optional[WindowsVirtualMachineScaleSetBootDiagnostics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a6b5b16b2a6b4f0289b611ceca7ad07d3dea7b5b15710056f8c822b2dd3890f(
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
    instances: jsii.Number,
    location: builtins.str,
    name: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    os_disk: typing.Union[WindowsVirtualMachineScaleSetOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    sku: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    additional_unattend_content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetAdditionalUnattendContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    automatic_instance_repair: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
    automatic_os_upgrade_policy: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name_prefix: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]]] = None,
    health_probe_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetPlan, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_fault_domain_count: typing.Optional[jsii.Number] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scale_in_policy: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_notification: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTerminateNotification, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    timezone: typing.Optional[builtins.str] = None,
    upgrade_mode: typing.Optional[builtins.str] = None,
    winrm_listener: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee552332a4c7d1cc2dd57818e601d9334dacf64154c3c0522ae24343c5252fd(
    *,
    caching: builtins.str,
    disk_size_gb: jsii.Number,
    lun: jsii.Number,
    storage_account_type: builtins.str,
    create_option: typing.Optional[builtins.str] = None,
    disk_encryption_set_id: typing.Optional[builtins.str] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__819c4fd9e6045d0a70e967f7e4bd94e1252f2b30867f2f61524c36ed0503e9ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df79473a51c9d02ae0abcfff1691a24cd052d5f27e5512580722e0fc0552806(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__647ac1d6ad691552dd2c7f16cd4ef22e152ea4e9033a877f5e927801c25a7589(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2436f256e0f058d24d13979e92f5063e581e927e1ac1d6396c32835c3d6655(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115fd28345f5744afbfc12df13598104ec305075dbaeee031658ab86e7405d77(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd5f58063080a738ac87e6de1ff022e548156c1b56f628cd4ae414b27d3c3a8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetDataDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__568a3d7722f076ccb91c50b6ec2e0f7d3f46b40a1dfb4efa1e356c33b651f5f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb5a721975d78b80a6434e187ba30dc8e843a524a7cd5932e9e2131cca990310(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28acb7c7369adb0451c5ef53f9cf4ec01256f30fc37e1afb1cffb9ba256ddc03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa14dede692b50c157d14cdf37f08e0664b7dad9cd4f81876d9ac7c03c03f695(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaed6f0f8ef480e0a35761fad4116b3d73d80c02e8b74fd7dee67da172c0c9f9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2526214d05b38eda8f088afba206f2c4a1f5bbd9f4c0948da278150a0e302be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db7679bfc68d541ba1e1d02a52a8d1612e0d73bcff5da3dbb3222731d30fc14d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8d52765c0426fb9c9bd6a0ec975351099418df9693d9c454e668adeb9ab45b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f213f217de6311f52cfe326185110758e4602b345644a03652279a2bd3b358a(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e831db4e5579b98594c29526f4d83190d2b4e1a98937523f19fcafb7d77b122(
    *,
    name: builtins.str,
    publisher: builtins.str,
    type: builtins.str,
    type_handler_version: builtins.str,
    automatic_upgrade_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_update_tag: typing.Optional[builtins.str] = None,
    protected_settings: typing.Optional[builtins.str] = None,
    provision_after_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    settings: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaaaea3d4065a4c0ce869acdc452a9ef45aa844ac18b840e7b53faad4d11eae9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d3eb2f05fb09ee6a235ce67427a9207efcf2effc1a4d1af4b87fd8db9f8ffc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d9d771ec212b393f15987477c5751e2e343b9bf6d774f28c6e05423b9e5d5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30812cc981e9f590f8c2fad786a102846edee714e4423f03d12e2822ad471a31(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301e51d0622a6f5aeb2248c23a8e3843c9d6f8239c864c4ccbfa3bc2870ae48b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ebfa4ff28c32984c60638f39c400562e9f8e77b48636f22ecfbf04de8ac5d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetExtension]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a89fa59e16f02db85d91a29892c8580e7e40cc17c558c1929667524226c7904(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66da741f79fb699a27196b08ad2612f96e0c2226a07e954758f2504568cb8c0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7e2ace9e9a8d69e795daba8a171968dbeb6d66eaaab90da0ec59d8571a3625(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa5bd03c83ea366a71774147a5183e72f74e1c8d1e45e91c3dfdb14375ebf89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a739e9cff5797c0ad5b7b57f9f6cf4539e0f0232b05ada578f8e0d7ce1112c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391bb849b1ae5e67ca642756eca3fa6ee81ef4ed77b7912a961a0ba624b3f398(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1771c85db1e503c863ccb23844fd0810ff010c8e7e95894c933928433e0edf(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049c4c0b89ca1397c4221a0e259a351fb9ac2023f5088159875f19bc639d6a5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479fa5fd96efe9506b17a20d9e340956486c36bfab90522b7de6e6f71b9fa70d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe8df59869b335d807888321da6311998289aa64a08f4513069eae3530a7661a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a20658c00f0e7ef67a54fff192db4def6e05cfb9181bca364afd0194ac8e944(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0516d43fc06b031cc5fbe73886f982b9259235f87601ffc163016f581b64bc0(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b4600fd4d24c8eb182f1579cf6c4cd169cdf3ef94e3cbdd629d2436b57ebed(
    *,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_security_group_id: typing.Optional[builtins.str] = None,
    primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b567f6e9eafa85a6a61f5adb254e1254ffb21fb25daccc774887e590af20c48(
    *,
    name: builtins.str,
    load_balancer_backend_address_pool_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    load_balancer_inbound_nat_rules_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0866782b46f8cc44bc56564c0c8ef9b69867285b9e49fdfebe1b7015be0c36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7815fe126f3cdec0c8b938089d5acebb30ce3f800b3c39d4dfd2abdf87a30a32(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c8d72f4dc1585cc6e529090b4cdcccd6b2bf0d4fafce85299e39aee5b174e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dc1dde789691d83b12fa9a65c4734f8ba681d811bfe41199db317b4b2b9379(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df70300cd20125f9577563f5b8de64b3999744a04b957aee680bdd90fb3ab81b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__507480717d7d685de0adb4507a367fb75df6d6b38d4ed863bd398c282f1d0d70(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb891188edf0cfcbb501f31cd292f500903a149df3820457f23e81a1b67f1de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca3fb06201fc0767130e7519d89d96c7e16b14591cbc69feb88bbc7e2dc34d6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d0f81597aa8a4e3d874fcda9b4fd4eed0388aae81f39e5add8f30c66f4bd06(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03165dbf0391c38870e9794e8a7e2f5d4378f391608345a17aaaa5aa888d3f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f470cc84a9046100cc07773af16a86fe2bae6eeff99122b2a9672723d7d319da(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c3612b11e84d11f4be7cd2fac1d1d42c348d69b0f1306dc1796fc55241ee97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89aad644a19f582d7b7d339dd2b6bb3de3899470d5cef6adec90e000ae858f98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658e0b5cf6b31b757fcc5d32668da2219bf62c024b27211bdad8d5604fec5873(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a00e1aa3c25269dfd9e8915088eebc0874ff4c6382f83b013f7c5e8ac6bbba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cef38d74b39b1e4f528c3e3e42d154e34bf238380cc55d89d7d112b5ce03679(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0b7bfdfa7a1bb1505ad2a08db3c47beae0e4879370a1b7cb3f4d1d8b4029afd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86963956ebdf0394bde76d434175a396e70024ecc99e481d1b518e7be27b59fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1541c60d8fbc8b61fcb4255d8d3ed7dacb41b709f24de7c3186c0691299fc66(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed46192076df48aac0865ae73cdb990ec4b00562a291076e7e29e678293a66ac(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c430277af92d7e4539541fbee079afb0f92471b92b0407cd07512f5bd6bcbda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b4ed8acf640e56b687cbe7f2514661678702991caec8333c678c94a868f3ca(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b3083a0d57d9585c908deba7f3f0279b64cc256489202524378da7f659d628(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb80b2ed550ac58519086d46f420add3bf1a450726d9160d1647df34024bea85(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb439735faecdb9b35deda0176d71fa3e3e5d40450c26107ca7ff5b9a2acabb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7927ae9b2c2d60038d2f8d2abaa22b0306b454cfe698b637713f2e3a1d5d060(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9bffdbdf26216f692cf810e464053cec449cf237a39168436edec0732ed2d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe29ff96cddb3646b7cdfd1c3f3c6a38e1d6784ccbc44812e18b99c549fdc24d(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9e5918278cfd7e36a4beace24e56857b1115aea84bb9598b28e1001578c5f79(
    *,
    caching: builtins.str,
    storage_account_type: builtins.str,
    diff_disk_settings: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_encryption_set_id: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7890f4f129c3aa6fe533b00ac164a57bda4b2ee18df12f3cc5d78d55bb459ff4(
    *,
    option: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6021fbfbe8f7eec106bb9ef346019e99cc08392b99b5cd4c69c3660904b0487(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26b473cfd94df98f1d87ad8cb6424214d2d3d338c0a303892c75d52352b0aa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ed001bc3b96d61420aa9b863317c11064d8250ac01500749d33629af4c51fcc(
    value: typing.Optional[WindowsVirtualMachineScaleSetOsDiskDiffDiskSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8a2ccd8d4fdd454847beab02091a663559e61fe256f99ae4030f0cf68cb315(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f03e2b2b5ae37f06c483ca838bb0777e654b1040b1a887ff7a4104e4e2032f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cfbbcb9f3d6af323580034dfb32eee68966ba02dfb49ca7071d257f313c7f85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d67961b736d944a33cfc51d06899579036ea3b7d72423c1dd52e391364635b8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b6e6eaf26e835252bdb9890d44212f1cbfdb10ef6b5b1d84e52f23c1f0f859(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f68b61c632e65bcbb303139097bc2e2b0c585acd6259b4992858e4f536c601d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0be88b74643ac54ad1103991b47af279bfbb76b0e0563fcc97f7c9410b72179(
    value: typing.Optional[WindowsVirtualMachineScaleSetOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89a5ecca61a853877a3238ff65e361039a4887c63fd2e7b472012be85817f31(
    *,
    name: builtins.str,
    product: builtins.str,
    publisher: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c698ae3a96db107cccebb1b19a68c4fcd2329ae992a031565aeb6bebbdcf80(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a98fe8af97b7adad496f1d502d7949025aea94980bb7b6f7788795a1466ac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd1858a6bd27afae6d67007f2e2c797f225e38a89d08920b38dfbd202d69076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b00a8f205e1f45d6f31be66e2a7d0bdc2abf75a59fb61bdba933c18db717c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824de2895fe3f1a4129c91231fd7d19cd3efe8e1ea35d7bf02f030de485f1789(
    value: typing.Optional[WindowsVirtualMachineScaleSetPlan],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3dc441b7b4ffda70b5a095b730c12ba1b5ff6b4435a05fcec730c32b6731723(
    *,
    certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    key_vault_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98014f116dd7e8f129a05c006302d57770da4dd59433dd24f43224379b5d6fd1(
    *,
    store: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d33eabc31e51844366fc75a514acaf091a47a651a3710a2989a11cff8b97c534(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb2146b4cb5665c6857adfa4909a85b1bf960ba1ab4416655bf5d2560049a105(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2349c118254286d920ac6d8638a6c267a5d3fb477bec101d804c66932bc317(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009ef964031135a2c5ed4a31d9546210552a3748efd201286b861c18d99491d2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e443420df8a7c986cb3a32f3a48241850683347ed0d7949da336a52d659045b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c4538dbc4aa6b9bf5432886f4c002f4718ec7f9bee7c65dd41615972126e5f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecretCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d155cf920b12e71ce6574d4776ddbc5d2de72759827072160975502fb9c1804(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2492053573f1aa3d2009278783f2e07ab783a676036831ec928956d82da3039c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722c3375b5ab841dfbb775d84a054cf7a753647bffeebc7a9a13c7f37e703291(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5ae2005595a3734671033a6d2d93a477b66225718880420d6123b94bc22d5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc927238b689921c8648dab6d46803ad6b5aa46fc9439547bcbfb6008180cb3e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff5deab5868a2702ad142c8023255cbf3e3e33576d9d7b3a3961586cdda1724(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5b370934744adc489491c186cd49f5e2a1b96753fa405c574a433d52ad70af(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32002983c6e56a9c8169c6ad98c36434db20431908ac237c3891cd5d11ab033(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662025aeb636a4277fd601af18712f0c6de07b4e31beed3d861605c1b599316f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetSecret]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c97634955d6aacd09fdbf8bb9bb3c581bf51e9932236d08573e48d2cfa35f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a2ad487cf9db728d96a652e2153649917145315a9153b287056aa3da60cc12(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7168ee7a4a8fa5fb132b6a05caba925f300d70ff519e4ad13a20f433c773342(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__326d8f3a7bbaa2462c9564848c6f76ec44d997057cb8c680c5e2dc88e37fef12(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d151e4089a7f241215e8be372868a707033e321defc98bb07ec12243b8b771b(
    *,
    offer: builtins.str,
    publisher: builtins.str,
    sku: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422be347d730b4a29af59bffe1bb1b16dcb586b28dbf3abb525639d6d8c16362(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31db84e0161c4e8e84d57e43686a3f619e23b71ec55b2ffa11d42aa4c3bb998e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a11ba3f22dcefc497d5a9084dd53d1d02f1600f2b46f8a3ab309ab5c882181f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0641626ee4f5ad7fa6774dd66ab9496fdfcc7233a0524e778fdbda4d1f63b7f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc7de860ab7e1bb3c92d8ce0848b79fab3ff525ffc461fb685d020cbb891fe8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cceba7d853e9cde1f9a1867c5b7b55725a59923f8c5345b9730a8cc6a825253f(
    value: typing.Optional[WindowsVirtualMachineScaleSetSourceImageReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93ebec2f7248d8689f25416d5949b8788cf3866056f6ac5e57c2260733e6007(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bcdda4165133d2c3658178484b9625a8ef8e1a0af702469c6375606f1c3f248(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e285d0d0be4ec9d47f3f82d043f6e7a107ceab64a304e487d67784ecd9b55c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4664818765f9e09ffd7178c3626bdbcc83ab96be0cfa8881517d898c75dc57cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cb0dfaf720e3703acac1b285fd2c17c37016ac15e1c215cc56d4efaf6d8e3a3(
    value: typing.Optional[WindowsVirtualMachineScaleSetTerminateNotification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f19600558feede2a4df3ddb30084c3ee12a54319305d7ea3fe7227ad95514ea(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4922f48de3bb2759d4c024f68762d2b8554394a2f35514a7142dfd76b6b02de6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ec72918d2c3f9344fa2771ce4682c0571ddbdfb809d617d48819e331ef4d70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bd446e1044f5608d2eacb6c6110f0d7863124ff539c68cfa6014b2faa3bfed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0269c0eb31bfe297f6e50ae1d5ea9cb65fc77d45aa328a3e7099e57b33048dca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ed10e7e0187c12f94958837b0dea99c099aa5e9ec84b7d1cdb624f08fa4fee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1366545dd63deff718b730368c73e8c9017abf14a886c6c0d45deb42bbec502(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94a62074a153fdd92bb88dff62ea901b78a36a0e9c3f0b4c99d3b06097e1712(
    *,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a562d4dd44e99ab2223506ea0b4cd482a7f5fac74662d1f70bdddb329cd02968(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26448f3258d812fede60a87f393085badf6280d4aa93fe39bd4652f2c722b306(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ba9fbef01b481f9864022f8755d2dfb6ac009a9f96a151840c1b50fb66ad61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4b59711b71caf23d349a598677b0cad3221721130c339234b16b60e0b863d5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2e690e918f28f6070462859d666fc80d158f56d59bf2d559f8648f14905cfb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198b838f8a6c22e6f5285cdfd244a1ee66df021fb0734ddd7041e09a9eec536a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[WindowsVirtualMachineScaleSetWinrmListener]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf9bac35e8461502df24c42ee48a62c38de9953f1caf4fff97992ef3150b4a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__926e2f1398d80ad886c44f15b491ac2cddbba60e3daff23a32dba78a9f9fd202(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c045b4e73f9b1d34d238c050881f99cb17d8896b16987f211a712a6f1671e0c1(
    value: typing.Optional[typing.Union[WindowsVirtualMachineScaleSetWinrmListener, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
