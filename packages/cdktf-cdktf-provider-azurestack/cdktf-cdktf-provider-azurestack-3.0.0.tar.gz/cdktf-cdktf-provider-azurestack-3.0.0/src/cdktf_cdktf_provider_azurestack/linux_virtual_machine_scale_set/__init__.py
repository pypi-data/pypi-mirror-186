'''
# `azurestack_linux_virtual_machine_scale_set`

Refer to the Terraform Registory for docs: [`azurestack_linux_virtual_machine_scale_set`](https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set).
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


class LinuxVirtualMachineScaleSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set azurestack_linux_virtual_machine_scale_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_username: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        os_disk: typing.Union["LinuxVirtualMachineScaleSetOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAdditionalCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetAdminSshKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAutomaticInstanceRepair", typing.Dict[builtins.str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetBootDiagnostics", typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetPlan", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTerminateNotification", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set azurestack_linux_virtual_machine_scale_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__055523e29eeac020f5b92fd67ad9a05c9813887680e01008f57c779f10989c30)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LinuxVirtualMachineScaleSetConfig(
            admin_username=admin_username,
            instances=instances,
            location=location,
            name=name,
            network_interface=network_interface,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            sku=sku,
            additional_capabilities=additional_capabilities,
            admin_password=admin_password,
            admin_ssh_key=admin_ssh_key,
            automatic_instance_repair=automatic_instance_repair,
            automatic_os_upgrade_policy=automatic_os_upgrade_policy,
            boot_diagnostics=boot_diagnostics,
            computer_name_prefix=computer_name_prefix,
            custom_data=custom_data,
            data_disk=data_disk,
            disable_password_authentication=disable_password_authentication,
            do_not_run_extensions_on_overprovisioned_machines=do_not_run_extensions_on_overprovisioned_machines,
            encryption_at_host_enabled=encryption_at_host_enabled,
            extension=extension,
            health_probe_id=health_probe_id,
            id=id,
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
            upgrade_mode=upgrade_mode,
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
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        value = LinuxVirtualMachineScaleSetAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdminSshKey")
    def put_admin_ssh_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetAdminSshKey", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08fc93edae94df20d0929abb26dab5e80645b40129f142a26b9a4302addf5d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdminSshKey", [value]))

    @jsii.member(jsii_name="putAutomaticInstanceRepair")
    def put_automatic_instance_repair(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.
        '''
        value = LinuxVirtualMachineScaleSetAutomaticInstanceRepair(
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
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        value = LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(
            disable_automatic_rollback=disable_automatic_rollback,
            enable_automatic_os_upgrade=enable_automatic_os_upgrade,
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticOsUpgradePolicy", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.
        '''
        value = LinuxVirtualMachineScaleSetBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putDataDisk")
    def put_data_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2d945e2461e94f65b8f8f83bb2755df057f3190fa614997e8b965053e1c1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataDisk", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3f2da5aee368a49b3637b57480b5a3aab212cfe95456a44c614062b0da4867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ec2f4d35cdfcf67511bb92be66724a8180f64d343384b784f5855f66f91b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        value = LinuxVirtualMachineScaleSetOsDisk(
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        '''
        value = LinuxVirtualMachineScaleSetPlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254adfca8023c58f6cb3b97d6d255521e9f48222366289558116c9f339fb8cf5)
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
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        value = LinuxVirtualMachineScaleSetSourceImageReference(
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.
        '''
        value = LinuxVirtualMachineScaleSetTerminateNotification(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.
        '''
        value = LinuxVirtualMachineScaleSetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdditionalCapabilities")
    def reset_additional_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCapabilities", []))

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetAdminSshKey")
    def reset_admin_ssh_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminSshKey", []))

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

    @jsii.member(jsii_name="resetDisablePasswordAuthentication")
    def reset_disable_password_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePasswordAuthentication", []))

    @jsii.member(jsii_name="resetDoNotRunExtensionsOnOverprovisionedMachines")
    def reset_do_not_run_extensions_on_overprovisioned_machines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDoNotRunExtensionsOnOverprovisionedMachines", []))

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

    @jsii.member(jsii_name="resetUpgradeMode")
    def reset_upgrade_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeMode", []))

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
    ) -> "LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKey")
    def admin_ssh_key(self) -> "LinuxVirtualMachineScaleSetAdminSshKeyList":
        return typing.cast("LinuxVirtualMachineScaleSetAdminSshKeyList", jsii.get(self, "adminSshKey"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepair")
    def automatic_instance_repair(
        self,
    ) -> "LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference", jsii.get(self, "automaticInstanceRepair"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicy")
    def automatic_os_upgrade_policy(
        self,
    ) -> "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference", jsii.get(self, "automaticOsUpgradePolicy"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(
        self,
    ) -> "LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="dataDisk")
    def data_disk(self) -> "LinuxVirtualMachineScaleSetDataDiskList":
        return typing.cast("LinuxVirtualMachineScaleSetDataDiskList", jsii.get(self, "dataDisk"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "LinuxVirtualMachineScaleSetExtensionList":
        return typing.cast("LinuxVirtualMachineScaleSetExtensionList", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "LinuxVirtualMachineScaleSetNetworkInterfaceList":
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "LinuxVirtualMachineScaleSetOsDiskOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "LinuxVirtualMachineScaleSetPlanOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetPlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "LinuxVirtualMachineScaleSetSecretList":
        return typing.cast("LinuxVirtualMachineScaleSetSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotification")
    def terminate_notification(
        self,
    ) -> "LinuxVirtualMachineScaleSetTerminateNotificationOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetTerminateNotificationOutputReference", jsii.get(self, "terminateNotification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LinuxVirtualMachineScaleSetTimeoutsOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAdditionalCapabilities"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKeyInput")
    def admin_ssh_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetAdminSshKey"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetAdminSshKey"]]], jsii.get(self, "adminSshKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepairInput")
    def automatic_instance_repair_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAutomaticInstanceRepair"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAutomaticInstanceRepair"], jsii.get(self, "automaticInstanceRepairInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicyInput")
    def automatic_os_upgrade_policy_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy"], jsii.get(self, "automaticOsUpgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetBootDiagnostics"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]], jsii.get(self, "dataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthenticationInput")
    def disable_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disablePasswordAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="doNotRunExtensionsOnOverprovisionedMachinesInput")
    def do_not_run_extensions_on_overprovisioned_machines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "doNotRunExtensionsOnOverprovisionedMachinesInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]], jsii.get(self, "extensionInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["LinuxVirtualMachineScaleSetOsDisk"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="overprovisionInput")
    def overprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["LinuxVirtualMachineScaleSetPlan"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetPlan"], jsii.get(self, "planInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]], jsii.get(self, "secretInput"))

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
    ) -> typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotificationInput")
    def terminate_notification_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"], jsii.get(self, "terminateNotificationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeModeInput")
    def upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ffefd70347113ff904912f94cfe62ecbe55e58405d9b0c77215608cc7525f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__326a30f647f7ab4cfac907007beff1462ff247f16297c46d003c1b508b964c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefix")
    def computer_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerNamePrefix"))

    @computer_name_prefix.setter
    def computer_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83e76caa432bfa4ea74f48e1e6c7155b685dc0acce6122047ffab562a7de1358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff556783ff1f284d5ebd50b6f85029debd0e90022c80c60025b1395195deef42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__6943ed093630313c57a1602894a2414dca8a5544cbb120c93dbc69a2e5b8ba45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordAuthentication", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__a3f365ea92334cc232aae4f3ee13982ed7a6d7f8cdf65c1181d5bfdff732e990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "doNotRunExtensionsOnOverprovisionedMachines", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__62845b461c9785e45e2e79fe12524a99f7c2fc9dd821916db455711c66dc7a93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthProbeId")
    def health_probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthProbeId"))

    @health_probe_id.setter
    def health_probe_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1631b7b0f230d0eef6bcdb681186b302b7e69d03ed01ff15eaf51230f62f47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthProbeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0329d0d13ae51476ef2a3135df1f967fd9cc3efbe517963765d60a4b6828dbf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c9fe60c797fb4e73c0c10d10fe4cba6dd574d84c40a2a967e71cda3e5d759af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57ab46ee9aaf167df80be1ff2fb0326c9889aac6c14111592c567998c2d15dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1500000596f256eb8c649fe8520be0fb811bab1362c191671a9fad2cdcc0dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__082e4f3c41a767ffde0e4f13d5faf0167f5282667d148ec278ee9ccca178e963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overprovision", value)

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "platformFaultDomainCount"))

    @platform_fault_domain_count.setter
    def platform_fault_domain_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77187d9e70294b8d9543335fcaf6693afea408d4a6447610ef8bf8e125a8bab)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eaa60cb9f3db37f3eaddd7148150b36d55b8e3710c7c0967b8bb44fc3b9f5d7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1882b3be1c65d72957cf716c90674676522da1eaf2049001933d37ddd09cbb4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicy")
    def scale_in_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleInPolicy"))

    @scale_in_policy.setter
    def scale_in_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5091ed7ec9949de3cb92cc1a1c465fee4b2b87a623a08e4d55cbd3debc12e4eb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14f281f1297bccf7efd82b08c30ec974e13f233350afa3df8ddc82e84fdc58ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singlePlacementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adee2293a8db28b80b06bac1cbf6e89a788912d2c2b65a980253a3079cf486f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d414032761375a63271a7a7f5c6344de2390b2fce2b3b1e53ed216f7539368c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0707a2f82e579781a013f78eaf9b441f2336f1df6aa6463917d48cc2350c914e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeMode")
    def upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeMode"))

    @upgrade_mode.setter
    def upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e3eb1196bd4bd965ad1fb7ea76fded5f299ea5824a75bd50ea29aade71a625f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class LinuxVirtualMachineScaleSetAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3d1979b1a46d373561b0699951dfaebfcebce473be42f933bb8c61be279859)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2995be3bd8f7148288936b7467f727c5a009b203a40c4ffd93e088fda055b8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f35c3520fea4684321971dc58a723bf3b9e5ecc326dfce2c610477540e88b5b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8637ea92ad21e1bf2da04916c0dc09ad11afbab6fe1f28f27af78bbe17e771f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKey",
    jsii_struct_bases=[],
    name_mapping={"public_key": "publicKey", "username": "username"},
)
class LinuxVirtualMachineScaleSetAdminSshKey:
    def __init__(self, *, public_key: builtins.str, username: builtins.str) -> None:
        '''
        :param public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#public_key LinuxVirtualMachineScaleSet#public_key}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#username LinuxVirtualMachineScaleSet#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7742b9d7e65bcaae1516996ddcf02335b867b8423c1594702d666eae392849c8)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key": public_key,
            "username": username,
        }

    @builtins.property
    def public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#public_key LinuxVirtualMachineScaleSet#public_key}.'''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#username LinuxVirtualMachineScaleSet#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAdminSshKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAdminSshKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKeyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a575eaae2a8aad0225dd721ab5564b065e43416468b6942e0427501af3db173)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetAdminSshKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3605018d67e3394d966a7516a31c34505ca39c8b082ab36ef67817b7537023)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetAdminSshKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ce27b1b1b217a7ac1955131071af0a6e658662835f71b9e3e9ebd2370bd293)
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
            type_hints = typing.get_type_hints(_typecheckingstub__83cd007912b454471d80deb886a4b4be887c60dd1fbc2645aecc164bcad787b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfdb594dbbc9166c1ea4f358e1ca8388f1e267dfb594c68c37261f60b56e4b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd80d099eff0ddcd4b53a61e5fef570165de0374020633de90a9b3ece81738c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetAdminSshKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2e870d5bd02333497e1a3353dfd3a0f25c5b1466c81225b4297cefa95efcd97)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aecbd58fe79d4acbd06357e7301324f95dce3d2a33d24097c4a58c9b7d0f200e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23baf9997b0d9ccef8009a28e6ef1377a53e335269fcffbe904290f9f7281824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284e0884bb0f163954d8e76acd7416068058876045f312e0ecab969afd50d288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticInstanceRepair",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "grace_period": "gracePeriod"},
)
class LinuxVirtualMachineScaleSetAutomaticInstanceRepair:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc0c6a9ac5dd7320155eb56faf8f3ef9db8e09e51817ffe74fa83f527529be1)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if grace_period is not None:
            self._values["grace_period"] = grace_period

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAutomaticInstanceRepair(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__774afbbb39c915e8c18be6a71edb45a4d4fec3f1e845ba05f40783e7a523cca0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df9d2c826d89709a64838b43fbe666dee4ffe5f5ef87d0b5d92aca9428c9c1fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f672973542e1854ddb1ab57f607738166e97288465ef7c7ecaf7f2c8268628e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01ba793e21550a1cc5f1d0b4638e7c2af152b81d493abd60a65e002d0c9c9aee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disable_automatic_rollback": "disableAutomaticRollback",
        "enable_automatic_os_upgrade": "enableAutomaticOsUpgrade",
    },
)
class LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy:
    def __init__(
        self,
        *,
        disable_automatic_rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        enable_automatic_os_upgrade: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c51edb5ce65c1f089948c3a0427fc37aff6aeaca060cf16139c0ad9bb735d7)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.'''
        result = self._values.get("disable_automatic_rollback")
        assert result is not None, "Required property 'disable_automatic_rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def enable_automatic_os_upgrade(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.'''
        result = self._values.get("enable_automatic_os_upgrade")
        assert result is not None, "Required property 'enable_automatic_os_upgrade' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d54ffc4060df49dbfc66d4cf2d2621bd1c5db59734f8c68233ddc3b2bf959a1a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a22810871db1b935cadcc40f4e2b0466f9c40b4d2028a46489c5cfc97067a31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7467a78e868095bc5697a767291f853f4de2cb8ad5fe0d31e732522f009fe5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticOsUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056c4c35e1a0ced80bde80b03f3268a366d22b08152f48bab1ea5b9650c81152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class LinuxVirtualMachineScaleSetBootDiagnostics:
    def __init__(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4965143202cae667c77b0af2adad1087b6f555c3a96ee5bac56e829845353c0e)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_account_uri": storage_account_uri,
        }

    @builtins.property
    def storage_account_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        assert result is not None, "Required property 'storage_account_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc317c637c38ef9b0709727484201713f8d4a00e1f530a2671ad330a561f2d8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78865fa05233895f0a226694101b1c301ff526cb6a009ae22ce0f7458e43d07e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e16ec46f93e25eb94364f05ec6422dfe3fa1eb65791092297037d4e488a2ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_username": "adminUsername",
        "instances": "instances",
        "location": "location",
        "name": "name",
        "network_interface": "networkInterface",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "additional_capabilities": "additionalCapabilities",
        "admin_password": "adminPassword",
        "admin_ssh_key": "adminSshKey",
        "automatic_instance_repair": "automaticInstanceRepair",
        "automatic_os_upgrade_policy": "automaticOsUpgradePolicy",
        "boot_diagnostics": "bootDiagnostics",
        "computer_name_prefix": "computerNamePrefix",
        "custom_data": "customData",
        "data_disk": "dataDisk",
        "disable_password_authentication": "disablePasswordAuthentication",
        "do_not_run_extensions_on_overprovisioned_machines": "doNotRunExtensionsOnOverprovisionedMachines",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "extension": "extension",
        "health_probe_id": "healthProbeId",
        "id": "id",
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
        "upgrade_mode": "upgradeMode",
    },
)
class LinuxVirtualMachineScaleSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admin_username: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
        os_disk: typing.Union["LinuxVirtualMachineScaleSetOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[builtins.str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetPlan", typing.Dict[builtins.str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTerminateNotification", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = LinuxVirtualMachineScaleSetOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = LinuxVirtualMachineScaleSetAdditionalCapabilities(**additional_capabilities)
        if isinstance(automatic_instance_repair, dict):
            automatic_instance_repair = LinuxVirtualMachineScaleSetAutomaticInstanceRepair(**automatic_instance_repair)
        if isinstance(automatic_os_upgrade_policy, dict):
            automatic_os_upgrade_policy = LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(**automatic_os_upgrade_policy)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = LinuxVirtualMachineScaleSetBootDiagnostics(**boot_diagnostics)
        if isinstance(plan, dict):
            plan = LinuxVirtualMachineScaleSetPlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = LinuxVirtualMachineScaleSetSourceImageReference(**source_image_reference)
        if isinstance(terminate_notification, dict):
            terminate_notification = LinuxVirtualMachineScaleSetTerminateNotification(**terminate_notification)
        if isinstance(timeouts, dict):
            timeouts = LinuxVirtualMachineScaleSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56877334d17285900d0cba20ba64669d21b7a22d44f00dc51feb208f24ad4495)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_ssh_key", value=admin_ssh_key, expected_type=type_hints["admin_ssh_key"])
            check_type(argname="argument automatic_instance_repair", value=automatic_instance_repair, expected_type=type_hints["automatic_instance_repair"])
            check_type(argname="argument automatic_os_upgrade_policy", value=automatic_os_upgrade_policy, expected_type=type_hints["automatic_os_upgrade_policy"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument computer_name_prefix", value=computer_name_prefix, expected_type=type_hints["computer_name_prefix"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument data_disk", value=data_disk, expected_type=type_hints["data_disk"])
            check_type(argname="argument disable_password_authentication", value=disable_password_authentication, expected_type=type_hints["disable_password_authentication"])
            check_type(argname="argument do_not_run_extensions_on_overprovisioned_machines", value=do_not_run_extensions_on_overprovisioned_machines, expected_type=type_hints["do_not_run_extensions_on_overprovisioned_machines"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument health_probe_id", value=health_probe_id, expected_type=type_hints["health_probe_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
            check_type(argname="argument upgrade_mode", value=upgrade_mode, expected_type=type_hints["upgrade_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_ssh_key is not None:
            self._values["admin_ssh_key"] = admin_ssh_key
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
        if disable_password_authentication is not None:
            self._values["disable_password_authentication"] = disable_password_authentication
        if do_not_run_extensions_on_overprovisioned_machines is not None:
            self._values["do_not_run_extensions_on_overprovisioned_machines"] = do_not_run_extensions_on_overprovisioned_machines
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if extension is not None:
            self._values["extension"] = extension
        if health_probe_id is not None:
            self._values["health_probe_id"] = health_probe_id
        if id is not None:
            self._values["id"] = id
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
        if upgrade_mode is not None:
            self._values["upgrade_mode"] = upgrade_mode

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
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.'''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        '''
        result = self._values.get("network_interface")
        assert result is not None, "Required property 'network_interface' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]], result)

    @builtins.property
    def os_disk(self) -> "LinuxVirtualMachineScaleSetOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("LinuxVirtualMachineScaleSetOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities], result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_ssh_key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]]:
        '''admin_ssh_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        '''
        result = self._values.get("admin_ssh_key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]], result)

    @builtins.property
    def automatic_instance_repair(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair]:
        '''automatic_instance_repair block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        '''
        result = self._values.get("automatic_instance_repair")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair], result)

    @builtins.property
    def automatic_os_upgrade_policy(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        '''automatic_os_upgrade_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        '''
        result = self._values.get("automatic_os_upgrade_policy")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy], result)

    @builtins.property
    def boot_diagnostics(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics], result)

    @builtins.property
    def computer_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.'''
        result = self._values.get("computer_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]]:
        '''data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        '''
        result = self._values.get("data_disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]], result)

    @builtins.property
    def disable_password_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.'''
        result = self._values.get("disable_password_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.'''
        result = self._values.get("do_not_run_extensions_on_overprovisioned_machines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]], result)

    @builtins.property
    def health_probe_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.'''
        result = self._values.get("health_probe_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.'''
        result = self._values.get("overprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional["LinuxVirtualMachineScaleSetPlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetPlan"], result)

    @builtins.property
    def platform_fault_domain_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.'''
        result = self._values.get("platform_fault_domain_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def scale_in_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.'''
        result = self._values.get("scale_in_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]], result)

    @builtins.property
    def single_placement_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.'''
        result = self._values.get("single_placement_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_notification(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"]:
        '''terminate_notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        '''
        result = self._values.get("terminate_notification")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LinuxVirtualMachineScaleSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTimeouts"], result)

    @builtins.property
    def upgrade_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.'''
        result = self._values.get("upgrade_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDisk",
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
class LinuxVirtualMachineScaleSetDataDisk:
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
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#lun LinuxVirtualMachineScaleSet#lun}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create_option LinuxVirtualMachineScaleSet#create_option}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bad0f225e7cb150de4e1a5ab32c7118fe2b175721d9b1a802bc4f6272c49a9f)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        assert result is not None, "Required property 'disk_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#lun LinuxVirtualMachineScaleSet#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create_option LinuxVirtualMachineScaleSet#create_option}.'''
        result = self._values.get("create_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetDataDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__074007a5b3502d3d703a89614d37f13fe06075b74a880e91273dfd0754430592)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa485ebbe2df9e887d6da5e953feaa2d87256ed5d921860b7fef84c1335dcc7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25b439996e1294514770d93df87603117ad4622346390b8fa5785c19069a89d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6df1563c53969bc06dc00dca772820e65c6483645d4d62f6f7f96d116f1750e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__865722d1b227074bd0cb7ed293cc275f88b6eeacf465db8d1602e42997d88958)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02242441a46f906cc97edfcc870e48472d1e7ce65298cace937d487cacf2265d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetDataDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5d5eae17f49ed43885bcaaf6dd2a39b61f2b75118f83202d72757aed16c1c45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a2192a0f1f62996cae8b149b208fd8e3078e991a2f79d1da94a0aeaf9f3282b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f905ff840d99c4c23a83a948735270da5598774610cd00a989929d73116b87aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3e60ec0d1559afd77e0d5688cc576a11ec0afc55ab8869dd6b1605541e0f30e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a8b8f049071ce85b32c65c6b76e14e83dc9e50c13bfbc99e687c600694fe90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa2b129b337134f0ad14786523d424534b3437d3cff527f025e80a206cd610a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b027513b6c1de3f89af5913a249be3d408f88568e7b88240f0f955fe9d24af86)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec74e360ead37dcc8c54b1310585438e111e87a29ff8377981e53c02f35b27bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8c9d94d4198113b34fe2761634cbac783aae0c4df054ee6b38d045b060f4e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtension",
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
class LinuxVirtualMachineScaleSetExtension:
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type LinuxVirtualMachineScaleSet#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type_handler_version LinuxVirtualMachineScaleSet#type_handler_version}.
        :param automatic_upgrade_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_upgrade_enabled LinuxVirtualMachineScaleSet#automatic_upgrade_enabled}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#auto_upgrade_minor_version LinuxVirtualMachineScaleSet#auto_upgrade_minor_version}.
        :param force_update_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#force_update_tag LinuxVirtualMachineScaleSet#force_update_tag}.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#protected_settings LinuxVirtualMachineScaleSet#protected_settings}.
        :param provision_after_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_after_extensions LinuxVirtualMachineScaleSet#provision_after_extensions}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#settings LinuxVirtualMachineScaleSet#settings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a69e1f95e426dfc8fb8a1cc4b39641f19a8d5f458f2cd347018c88b821c76ab6)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type LinuxVirtualMachineScaleSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type_handler_version LinuxVirtualMachineScaleSet#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_upgrade_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_upgrade_enabled LinuxVirtualMachineScaleSet#automatic_upgrade_enabled}.'''
        result = self._values.get("automatic_upgrade_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#auto_upgrade_minor_version LinuxVirtualMachineScaleSet#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_update_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#force_update_tag LinuxVirtualMachineScaleSet#force_update_tag}.'''
        result = self._values.get("force_update_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#protected_settings LinuxVirtualMachineScaleSet#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_after_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_after_extensions LinuxVirtualMachineScaleSet#provision_after_extensions}.'''
        result = self._values.get("provision_after_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#settings LinuxVirtualMachineScaleSet#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetExtensionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtensionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fc7b94d160812a97f7e973b3cddc3daf787fb5f281ccab5b7260707332dd81c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c57eae4e7d7ef41e2725257ffbd95c1e24f542a29ad4ecfd695720a740df8e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6d75408cecbcfe1d2123e6bd6ff436714765cdc5811ff7f7aea63c5c853352b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc5a56e5ce757ef8322538929a29cdb84a0ffa6af732dc344c2112c3466440d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db8924a0b7c3ae585f30b4eea29aa11fd988f97b64d24b9a5d5474a2ff5af78b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a037a7c50921d11d6da22be1841d8bc73dddf076170c11fd9137f3cad253ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetExtensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c90d4f22f6a3c1ba109df73fc249bf0e3c099f7a33fbd8862eed25ee09eeb54b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0648cc3ee59ac8cb2a405628bb06a1a65b44397d615431fcc1dbb0c62b2c070b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__547233a721467cbf1235c3ba922a46ca4b39ddc1dadda91d3288554f1bcf89af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTag")
    def force_update_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceUpdateTag"))

    @force_update_tag.setter
    def force_update_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d503e4fc84484f2fbe37e0c566a8225faa69f39e9937ef550c34ba28c9d43c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdateTag", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4966aa01604cd2298da27827a3c2b84bd035cd0844ced505e1831278c313b630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1811dcb7272e94818897f3b3c58632689ce7c172a093a1a2f5d9da3bb94fa05a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensions")
    def provision_after_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisionAfterExtensions"))

    @provision_after_extensions.setter
    def provision_after_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1150bc6f2dea741f5054e899dba1f8148b2efbd15b650d03258984179cb795)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionAfterExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106e961f3454f10da57ef3a8b5106a25814dfae635beb558cbd1a4a7773e0656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94fda1942b6928bdd19902af08183b5dc3263164272e5822b75104f1f939f6d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b3dc78a79f40767d823320632dc9ea0a66abed531d4e2583efeeb7950cf328d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2880b1394f41f0b008c26dc170eee529532422fb8437b7f0d629c5351d13b8bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fdbd73211d0bfd946042000d5fd6bfc20466d457c3eba0978af7c5515d2d59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterface",
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
class LinuxVirtualMachineScaleSetNetworkInterface:
    def __init__(
        self,
        *,
        ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_security_group_id: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ip_configuration LinuxVirtualMachineScaleSet#ip_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#dns_servers LinuxVirtualMachineScaleSet#dns_servers}.
        :param enable_ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_ip_forwarding LinuxVirtualMachineScaleSet#enable_ip_forwarding}.
        :param network_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_security_group_id LinuxVirtualMachineScaleSet#network_security_group_id}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6cd19504b958e0129a10e029f936e4df1e6af39a81e89e842ff68d9ae50a31)
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
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ip_configuration LinuxVirtualMachineScaleSet#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#dns_servers LinuxVirtualMachineScaleSet#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_ip_forwarding LinuxVirtualMachineScaleSet#enable_ip_forwarding}.'''
        result = self._values.get("enable_ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_security_group_id LinuxVirtualMachineScaleSet#network_security_group_id}.'''
        result = self._values.get("network_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
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
class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration:
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param load_balancer_backend_address_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_backend_address_pool_ids LinuxVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.
        :param load_balancer_inbound_nat_rules_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids LinuxVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#subnet_id LinuxVirtualMachineScaleSet#subnet_id}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55dfb3082fa1b603f0cb45fcc079c1db162fe152d97f52ca3da81447a793a38e)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_backend_address_pool_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_backend_address_pool_ids LinuxVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.'''
        result = self._values.get("load_balancer_backend_address_pool_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_inbound_nat_rules_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids LinuxVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.'''
        result = self._values.get("load_balancer_inbound_nat_rules_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#subnet_id LinuxVirtualMachineScaleSet#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f61ff203f6999e6c0599c0b909a043204618b7bb8288ffe725576d65eafdb278)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08ccc109d3d3af294e88b7ef5501c360ec30d04b9864cefb28048df7a640cd24)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6678c3600008f72cd44f305230745b5ac0c6b6926ed76894a144d05898ee82dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1e988a9692dc9ea148c6d1b74a9388b982248a43eb15a681d19707fbcb7acb6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15439c8871a73d224af6ff06ab58ea42e911502484f91fccab494860d09e1e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0066d070a556be6ca0811a2f0d7b44e74fb5453cb64205a6a35730c9f3dfaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0c6c5d089eb77514d5312b84410ed6172786b0171d12737fee94b39812dbc35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de1eaf26913a8eba9db403a2bd3d79f2bb139bb1f1baaae8a202edfd07dcc073)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2be69dcf3e16892c7e8e79720f22ebcc653c961789e7fb11a4af196a85855cd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerInboundNatRulesIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb6d753fc6ca2c2b9ba74e30119c90db4dfc58f16548a1a9af30e9da49271f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13ee0f1145b00c34b5393a78d12d04ae12b18be9d0a1c31d7598ad7384a47f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c2b10b3895c169e57ab97d8c03d63d42df8b2565947524c642434c96b569a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8356622e5abec7bb7738f6061fe988e1182c61af56cae4ef4cb83f14547c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9577851883d12a2d9cc48b6a5d98e3cfe11840093c80a068d6bdafb29c318868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3be2433d0cc3fd5936f4f211409137ba8cb45f387f30cd7cc010511f13a797fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20bae672e61aee5c358e2245595f4a95fd3e1bd940f3ecdffb1a87c109654d5b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ab0c5fbd8098931d19aa21e221855eb30c7a7a9aca5d347b7fa540848ce5f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13dbce3bc8b32843f561072e6150e3db99b8ea90597035fd3bd5fd74ccf26009)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7642a1053bb5beb448aecb287f1c13c57219484c929cb7f6b0f31f8ea022dc81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba8501e68eb5d470d5542a005729cd6e24e6a87c48ce0fa190272b353f77dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ab2052086ea82c52a27ff3c6eb32144c12d5f3bb5d057dfd5be45fccff5f167)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb02f9b77a87433c8b9d6b48f135235ac3de84a5be40bb5487ba2e3246997da)
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
    ) -> LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList:
        return typing.cast(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, jsii.get(self, "ipConfiguration"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "ipConfigurationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__96f1360f9c5aaed5bc369feaee2365646227cd1511a91d32cbac465cfcd60293)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f6835c7eeffb5668efe17c4e3ac51081946f51332d7e6241f73251aaccfe996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df3687269953443730a84709b5d7264f416b6b20ca7f006e81653de2273f701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupId")
    def network_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupId"))

    @network_security_group_id.setter
    def network_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__122803584d716e2dec32b1d70c4c177262e69c915bc155e347de5d72c0ef9efd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b110ed0f2a18ec7eea13b23639a4ec81aa6d34d444485c263e552655ac065a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9011a17a1efab59c981440f8e79b24e9cf01ef8d45d75449e34e939a3ec90b78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDisk",
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
class LinuxVirtualMachineScaleSetOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e9b5120bbba8f90cfe1d39d40833a560251eb558c891b4515f0b11afa7c41f7)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option"},
)
class LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings:
    def __init__(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f2544be1ca1b26dd3a99e4968befc505ba3a124f53fea701c4d8d164e139480)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "option": option,
        }

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8e69195957e75f050de267a77ec456dcc3a1886ac76faafe497ff5216c9b165)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4570f5b673354dfc6066c6e1f118f6ca55213806751093e98cd998acb5b92e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90b2a5e4badb3d8d5badb2e8481fdcc1062166bd304fcf9d4af7ff91719541e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efd625886c9286f15a6207d85a3c61fa1cc7e321444f652f723a47e2ca9fba5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.
        '''
        value = LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(option=option)

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
    ) -> LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__7015d2205534b31af4baf9fbea00891f106d6bc8b71937d0bde49b94bfc7353c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd603cf4eda7a60a5bddd7cbd96fc78db6883604555b1304a3225bff39512e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33abaaf3e09d16993e1aa4e2d75a0684a27aa8a48465e2fd1dafbcb0bf138f23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c0466f881e59b943ccf7f78ec4d15bd052a345216fd10b8d85e0f6aaf8b0be6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__543ebfd0a74d57ee2a08df40144f0cb71b477d277f7bbe44c3b83866d680b535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineScaleSetOsDisk]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55321916545d97e809f9cd1fcbdb8423b0dc272de55cf3a01c6eed70a387338e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetPlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class LinuxVirtualMachineScaleSetPlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1379dee7be66745d38015b13eb6d54a5fef839d43518154a5b1989942cf9bdb1)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b84c9180881ad7d3a52ac4dee96a169d76ed5d1c405b20fb4a279888131b958f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb489ebb9e2c3706381a220973d62a6ae06f01c8683ec52aae6414050082ffde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9125b8ab7e8a5e1acb3f4feae5fc1ed507e7e5eda7f1f31e9ff345664209a746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6536eed10b287812ab31ee93eae7d7ae858ab3b463ad1c1f02b74eff258c7415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineScaleSetPlan]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetPlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetPlan],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__054888d9f2576c48530250aa539dbbf805b97d525b13ebe170bda08cc0a668cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class LinuxVirtualMachineScaleSetSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecretCertificate", typing.Dict[builtins.str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#certificate LinuxVirtualMachineScaleSet#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#key_vault_id LinuxVirtualMachineScaleSet#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc3f9ae2b759dca6a853a3af0f50f78845e45f2d4705276d1df08a0607fb8e41)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#certificate LinuxVirtualMachineScaleSet#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#key_vault_id LinuxVirtualMachineScaleSet#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={},
)
class LinuxVirtualMachineScaleSetSecretCertificate:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetSecretCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__670b0d9bc64c580ab91dc503d45037e7373add71465f07351245ad338f1f4386)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ed56ccca84d415e474b7f7911472753871fe071a53a024c6e56124347a98a0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef6a65298984cd61e933b835c7d5ee3918949fe3fd123fdd7c07abf9813b5af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__059b65e1052e8b9d86612194af2a4f06bde2a09928715b80492ea24a373bc01e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ad70fdc6883ca9a437c8d2e5b90ab0e6f3c22a1287c7b7953bb024f46f43d60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b03ab9894a55fa1a524488ff348f049be3070ac6b2994a4bc1f96bafd174d391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7158563a225359690a2f74e43d87ecbcfb0cece7ea24455082e3d9cc68e87f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d6caf6b486366b974c03d4aeff1ec334006fb40cbf0235ccb5b466e232fff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ee978000794d6426b079a3903002e015ecb9c7e5f705f4f3d9de2cbf7f412cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e37d454e657d54b316cf03cf9973e0ad0caa8f703bf3a80bbdfe6ec899fe626)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f74313e7e6af0d3718d22f08b18d08b3104b2797959c2bf62aad973f89270568)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c048ab94d4dd7ef88693e33c5cf36f7d7e17a81e28d09449d137558790a02a27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea5cefb2dd86a944c7a9ec1b0889d7854c44cb1e99c3e3c71fd2982182bcd939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a542c50f9416bcc0a8547c90130052e09e76c74e51092930248907e8b9b1451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c746d2adf88aa10f6ed718b4d21230848418e4fd13fa49309cbb39573f5a8bc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d0e1d92cfa4c82c41a8a47f8eb37bcdde1b307f389c96304167d960569e2b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> LinuxVirtualMachineScaleSetSecretCertificateList:
        return typing.cast(LinuxVirtualMachineScaleSetSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "certificateInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__1bde02ebe957fec73df32fc57c6e3368bfde563ff97e34686fb3087ae5772e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcaed1e18aed67d4017e6051d19bb86dacd19f47a950af09334d199e56a0e523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class LinuxVirtualMachineScaleSetSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e85a71277cec83d5bd89a7248827958ed323f6f5915fffc61041ab0edd88e6)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__683a1a608e6556d2d218c2840530a3d165aeaa54166607f4f8ea48ef45d47994)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0b2ceefed8b945b3a50dd4e977eba214f2775dfd0bbccf9204ea2b07fe1729f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417715268e0689daf664c1edac2e249371df35e607ea16a2bb9f3ca8993a1e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edfe5f56979cb3a3a0c960953ae372af2f770a801f0713e2e13d1d09e4cf429f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fccb7c9d93345f1b46fadadee4c2518d288132c29916d2afb176d42d94bb057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5025054e8a26edab8bc8f276258095384cb5cf6ac9e94d4f852a258626f472c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTerminateNotification",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "timeout": "timeout"},
)
class LinuxVirtualMachineScaleSetTerminateNotification:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd39b1b25112a1b5ce9e59ca37de9f8c889acb5d1122c934a092179604f2ffc)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetTerminateNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetTerminateNotificationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTerminateNotificationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__947f502267f1db3c7e610df0a067e21136edc89f4d025f301d2099618db88068)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e50c929a6115efc01455d39fa19782a12f9289632d563ae0153bdf6ae9d8142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0441837a913326e13f9130cb4c7dfb2f1b44f3059b103fa46173541ee868136b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe6c56504b0f14dc8b68690ef8056ca8e87dcfea38b9dc84a7cd554452c1367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LinuxVirtualMachineScaleSetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44308bf9ff007aa940baceadd666f89fc482145b23545b640a2b322cad68be2)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cfa1b19cf51c8a65a6ac75eb2af6028cb2ad5a102c7ed69e05624f46c86bb69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da3e830fd560c8c1e58ccee6b44b28c5a7ba1af0b78f44f91b8823a138f5a5a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603cb1a459b1855808aa2d315aa477bfe20f2bff04a799911c5c38e6bffed320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b112f2e2a2b44b69d4eb00e2165a934762c32f65cf43445ef1b5d632af0f83f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e346771ea2182a996cf249aa6d75f0dfc3c3c01f17e6e3369f35fd7ea333cd9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2217b8bdf72e5f2ab7c7439bfaa217ad9b12f240862b7bda572736415bfc9906)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LinuxVirtualMachineScaleSet",
    "LinuxVirtualMachineScaleSetAdditionalCapabilities",
    "LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
    "LinuxVirtualMachineScaleSetAdminSshKey",
    "LinuxVirtualMachineScaleSetAdminSshKeyList",
    "LinuxVirtualMachineScaleSetAdminSshKeyOutputReference",
    "LinuxVirtualMachineScaleSetAutomaticInstanceRepair",
    "LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
    "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
    "LinuxVirtualMachineScaleSetBootDiagnostics",
    "LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference",
    "LinuxVirtualMachineScaleSetConfig",
    "LinuxVirtualMachineScaleSetDataDisk",
    "LinuxVirtualMachineScaleSetDataDiskList",
    "LinuxVirtualMachineScaleSetDataDiskOutputReference",
    "LinuxVirtualMachineScaleSetExtension",
    "LinuxVirtualMachineScaleSetExtensionList",
    "LinuxVirtualMachineScaleSetExtensionOutputReference",
    "LinuxVirtualMachineScaleSetNetworkInterface",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
    "LinuxVirtualMachineScaleSetNetworkInterfaceList",
    "LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference",
    "LinuxVirtualMachineScaleSetOsDisk",
    "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings",
    "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
    "LinuxVirtualMachineScaleSetOsDiskOutputReference",
    "LinuxVirtualMachineScaleSetPlan",
    "LinuxVirtualMachineScaleSetPlanOutputReference",
    "LinuxVirtualMachineScaleSetSecret",
    "LinuxVirtualMachineScaleSetSecretCertificate",
    "LinuxVirtualMachineScaleSetSecretCertificateList",
    "LinuxVirtualMachineScaleSetSecretCertificateOutputReference",
    "LinuxVirtualMachineScaleSetSecretList",
    "LinuxVirtualMachineScaleSetSecretOutputReference",
    "LinuxVirtualMachineScaleSetSourceImageReference",
    "LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference",
    "LinuxVirtualMachineScaleSetTerminateNotification",
    "LinuxVirtualMachineScaleSetTerminateNotificationOutputReference",
    "LinuxVirtualMachineScaleSetTimeouts",
    "LinuxVirtualMachineScaleSetTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__055523e29eeac020f5b92fd67ad9a05c9813887680e01008f57c779f10989c30(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_username: builtins.str,
    instances: jsii.Number,
    location: builtins.str,
    name: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    os_disk: typing.Union[LinuxVirtualMachineScaleSetOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    sku: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_password: typing.Optional[builtins.str] = None,
    admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    automatic_instance_repair: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
    automatic_os_upgrade_policy: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name_prefix: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]]] = None,
    health_probe_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetPlan, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_fault_domain_count: typing.Optional[jsii.Number] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scale_in_policy: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_notification: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTerminateNotification, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    upgrade_mode: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__08fc93edae94df20d0929abb26dab5e80645b40129f142a26b9a4302addf5d4b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2d945e2461e94f65b8f8f83bb2755df057f3190fa614997e8b965053e1c1b5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3f2da5aee368a49b3637b57480b5a3aab212cfe95456a44c614062b0da4867(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ec2f4d35cdfcf67511bb92be66724a8180f64d343384b784f5855f66f91b9f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254adfca8023c58f6cb3b97d6d255521e9f48222366289558116c9f339fb8cf5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ffefd70347113ff904912f94cfe62ecbe55e58405d9b0c77215608cc7525f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__326a30f647f7ab4cfac907007beff1462ff247f16297c46d003c1b508b964c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e76caa432bfa4ea74f48e1e6c7155b685dc0acce6122047ffab562a7de1358(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff556783ff1f284d5ebd50b6f85029debd0e90022c80c60025b1395195deef42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6943ed093630313c57a1602894a2414dca8a5544cbb120c93dbc69a2e5b8ba45(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f365ea92334cc232aae4f3ee13982ed7a6d7f8cdf65c1181d5bfdff732e990(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62845b461c9785e45e2e79fe12524a99f7c2fc9dd821916db455711c66dc7a93(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1631b7b0f230d0eef6bcdb681186b302b7e69d03ed01ff15eaf51230f62f47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0329d0d13ae51476ef2a3135df1f967fd9cc3efbe517963765d60a4b6828dbf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c9fe60c797fb4e73c0c10d10fe4cba6dd574d84c40a2a967e71cda3e5d759af(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57ab46ee9aaf167df80be1ff2fb0326c9889aac6c14111592c567998c2d15dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1500000596f256eb8c649fe8520be0fb811bab1362c191671a9fad2cdcc0dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082e4f3c41a767ffde0e4f13d5faf0167f5282667d148ec278ee9ccca178e963(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77187d9e70294b8d9543335fcaf6693afea408d4a6447610ef8bf8e125a8bab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaa60cb9f3db37f3eaddd7148150b36d55b8e3710c7c0967b8bb44fc3b9f5d7b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1882b3be1c65d72957cf716c90674676522da1eaf2049001933d37ddd09cbb4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5091ed7ec9949de3cb92cc1a1c465fee4b2b87a623a08e4d55cbd3debc12e4eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f281f1297bccf7efd82b08c30ec974e13f233350afa3df8ddc82e84fdc58ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adee2293a8db28b80b06bac1cbf6e89a788912d2c2b65a980253a3079cf486f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d414032761375a63271a7a7f5c6344de2390b2fce2b3b1e53ed216f7539368c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0707a2f82e579781a013f78eaf9b441f2336f1df6aa6463917d48cc2350c914e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e3eb1196bd4bd965ad1fb7ea76fded5f299ea5824a75bd50ea29aade71a625f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3d1979b1a46d373561b0699951dfaebfcebce473be42f933bb8c61be279859(
    *,
    ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2995be3bd8f7148288936b7467f727c5a009b203a40c4ffd93e088fda055b8a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f35c3520fea4684321971dc58a723bf3b9e5ecc326dfce2c610477540e88b5b3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8637ea92ad21e1bf2da04916c0dc09ad11afbab6fe1f28f27af78bbe17e771f(
    value: typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7742b9d7e65bcaae1516996ddcf02335b867b8423c1594702d666eae392849c8(
    *,
    public_key: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a575eaae2a8aad0225dd721ab5564b065e43416468b6942e0427501af3db173(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3605018d67e3394d966a7516a31c34505ca39c8b082ab36ef67817b7537023(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ce27b1b1b217a7ac1955131071af0a6e658662835f71b9e3e9ebd2370bd293(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83cd007912b454471d80deb886a4b4be887c60dd1fbc2645aecc164bcad787b4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdb594dbbc9166c1ea4f358e1ca8388f1e267dfb594c68c37261f60b56e4b89(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd80d099eff0ddcd4b53a61e5fef570165de0374020633de90a9b3ece81738c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e870d5bd02333497e1a3353dfd3a0f25c5b1466c81225b4297cefa95efcd97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecbd58fe79d4acbd06357e7301324f95dce3d2a33d24097c4a58c9b7d0f200e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23baf9997b0d9ccef8009a28e6ef1377a53e335269fcffbe904290f9f7281824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284e0884bb0f163954d8e76acd7416068058876045f312e0ecab969afd50d288(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc0c6a9ac5dd7320155eb56faf8f3ef9db8e09e51817ffe74fa83f527529be1(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    grace_period: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__774afbbb39c915e8c18be6a71edb45a4d4fec3f1e845ba05f40783e7a523cca0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9d2c826d89709a64838b43fbe666dee4ffe5f5ef87d0b5d92aca9428c9c1fb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f672973542e1854ddb1ab57f607738166e97288465ef7c7ecaf7f2c8268628e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ba793e21550a1cc5f1d0b4638e7c2af152b81d493abd60a65e002d0c9c9aee(
    value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c51edb5ce65c1f089948c3a0427fc37aff6aeaca060cf16139c0ad9bb735d7(
    *,
    disable_automatic_rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    enable_automatic_os_upgrade: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54ffc4060df49dbfc66d4cf2d2621bd1c5db59734f8c68233ddc3b2bf959a1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a22810871db1b935cadcc40f4e2b0466f9c40b4d2028a46489c5cfc97067a31(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7467a78e868095bc5697a767291f853f4de2cb8ad5fe0d31e732522f009fe5a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056c4c35e1a0ced80bde80b03f3268a366d22b08152f48bab1ea5b9650c81152(
    value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4965143202cae667c77b0af2adad1087b6f555c3a96ee5bac56e829845353c0e(
    *,
    storage_account_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc317c637c38ef9b0709727484201713f8d4a00e1f530a2671ad330a561f2d8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78865fa05233895f0a226694101b1c301ff526cb6a009ae22ce0f7458e43d07e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e16ec46f93e25eb94364f05ec6422dfe3fa1eb65791092297037d4e488a2ed(
    value: typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56877334d17285900d0cba20ba64669d21b7a22d44f00dc51feb208f24ad4495(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    admin_username: builtins.str,
    instances: jsii.Number,
    location: builtins.str,
    name: builtins.str,
    network_interface: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
    os_disk: typing.Union[LinuxVirtualMachineScaleSetOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    sku: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_password: typing.Optional[builtins.str] = None,
    admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    automatic_instance_repair: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[builtins.str, typing.Any]]] = None,
    automatic_os_upgrade_policy: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name_prefix: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    extension: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetExtension, typing.Dict[builtins.str, typing.Any]]]]] = None,
    health_probe_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    overprovision: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    plan: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetPlan, typing.Dict[builtins.str, typing.Any]]] = None,
    platform_fault_domain_count: typing.Optional[jsii.Number] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scale_in_policy: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    single_placement_group: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_notification: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTerminateNotification, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    upgrade_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bad0f225e7cb150de4e1a5ab32c7118fe2b175721d9b1a802bc4f6272c49a9f(
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

def _typecheckingstub__074007a5b3502d3d703a89614d37f13fe06075b74a880e91273dfd0754430592(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa485ebbe2df9e887d6da5e953feaa2d87256ed5d921860b7fef84c1335dcc7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25b439996e1294514770d93df87603117ad4622346390b8fa5785c19069a89d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df1563c53969bc06dc00dca772820e65c6483645d4d62f6f7f96d116f1750e8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865722d1b227074bd0cb7ed293cc275f88b6eeacf465db8d1602e42997d88958(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02242441a46f906cc97edfcc870e48472d1e7ce65298cace937d487cacf2265d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d5eae17f49ed43885bcaaf6dd2a39b61f2b75118f83202d72757aed16c1c45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2192a0f1f62996cae8b149b208fd8e3078e991a2f79d1da94a0aeaf9f3282b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f905ff840d99c4c23a83a948735270da5598774610cd00a989929d73116b87aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3e60ec0d1559afd77e0d5688cc576a11ec0afc55ab8869dd6b1605541e0f30e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a8b8f049071ce85b32c65c6b76e14e83dc9e50c13bfbc99e687c600694fe90(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa2b129b337134f0ad14786523d424534b3437d3cff527f025e80a206cd610a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b027513b6c1de3f89af5913a249be3d408f88568e7b88240f0f955fe9d24af86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec74e360ead37dcc8c54b1310585438e111e87a29ff8377981e53c02f35b27bc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8c9d94d4198113b34fe2761634cbac783aae0c4df054ee6b38d045b060f4e9(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69e1f95e426dfc8fb8a1cc4b39641f19a8d5f458f2cd347018c88b821c76ab6(
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

def _typecheckingstub__5fc7b94d160812a97f7e973b3cddc3daf787fb5f281ccab5b7260707332dd81c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c57eae4e7d7ef41e2725257ffbd95c1e24f542a29ad4ecfd695720a740df8e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6d75408cecbcfe1d2123e6bd6ff436714765cdc5811ff7f7aea63c5c853352b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5a56e5ce757ef8322538929a29cdb84a0ffa6af732dc344c2112c3466440d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8924a0b7c3ae585f30b4eea29aa11fd988f97b64d24b9a5d5474a2ff5af78b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a037a7c50921d11d6da22be1841d8bc73dddf076170c11fd9137f3cad253ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90d4f22f6a3c1ba109df73fc249bf0e3c099f7a33fbd8862eed25ee09eeb54b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0648cc3ee59ac8cb2a405628bb06a1a65b44397d615431fcc1dbb0c62b2c070b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__547233a721467cbf1235c3ba922a46ca4b39ddc1dadda91d3288554f1bcf89af(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d503e4fc84484f2fbe37e0c566a8225faa69f39e9937ef550c34ba28c9d43c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4966aa01604cd2298da27827a3c2b84bd035cd0844ced505e1831278c313b630(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1811dcb7272e94818897f3b3c58632689ce7c172a093a1a2f5d9da3bb94fa05a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1150bc6f2dea741f5054e899dba1f8148b2efbd15b650d03258984179cb795(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106e961f3454f10da57ef3a8b5106a25814dfae635beb558cbd1a4a7773e0656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fda1942b6928bdd19902af08183b5dc3263164272e5822b75104f1f939f6d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3dc78a79f40767d823320632dc9ea0a66abed531d4e2583efeeb7950cf328d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2880b1394f41f0b008c26dc170eee529532422fb8437b7f0d629c5351d13b8bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fdbd73211d0bfd946042000d5fd6bfc20466d457c3eba0978af7c5515d2d59(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6cd19504b958e0129a10e029f936e4df1e6af39a81e89e842ff68d9ae50a31(
    *,
    ip_configuration: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_security_group_id: typing.Optional[builtins.str] = None,
    primary: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dfb3082fa1b603f0cb45fcc079c1db162fe152d97f52ca3da81447a793a38e(
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

def _typecheckingstub__f61ff203f6999e6c0599c0b909a043204618b7bb8288ffe725576d65eafdb278(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08ccc109d3d3af294e88b7ef5501c360ec30d04b9864cefb28048df7a640cd24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6678c3600008f72cd44f305230745b5ac0c6b6926ed76894a144d05898ee82dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e988a9692dc9ea148c6d1b74a9388b982248a43eb15a681d19707fbcb7acb6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15439c8871a73d224af6ff06ab58ea42e911502484f91fccab494860d09e1e51(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0066d070a556be6ca0811a2f0d7b44e74fb5453cb64205a6a35730c9f3dfaa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c6c5d089eb77514d5312b84410ed6172786b0171d12737fee94b39812dbc35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1eaf26913a8eba9db403a2bd3d79f2bb139bb1f1baaae8a202edfd07dcc073(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be69dcf3e16892c7e8e79720f22ebcc653c961789e7fb11a4af196a85855cd5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb6d753fc6ca2c2b9ba74e30119c90db4dfc58f16548a1a9af30e9da49271f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ee0f1145b00c34b5393a78d12d04ae12b18be9d0a1c31d7598ad7384a47f09(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c2b10b3895c169e57ab97d8c03d63d42df8b2565947524c642434c96b569a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8356622e5abec7bb7738f6061fe988e1182c61af56cae4ef4cb83f14547c74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9577851883d12a2d9cc48b6a5d98e3cfe11840093c80a068d6bdafb29c318868(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3be2433d0cc3fd5936f4f211409137ba8cb45f387f30cd7cc010511f13a797fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20bae672e61aee5c358e2245595f4a95fd3e1bd940f3ecdffb1a87c109654d5b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ab0c5fbd8098931d19aa21e221855eb30c7a7a9aca5d347b7fa540848ce5f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13dbce3bc8b32843f561072e6150e3db99b8ea90597035fd3bd5fd74ccf26009(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7642a1053bb5beb448aecb287f1c13c57219484c929cb7f6b0f31f8ea022dc81(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba8501e68eb5d470d5542a005729cd6e24e6a87c48ce0fa190272b353f77dc1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab2052086ea82c52a27ff3c6eb32144c12d5f3bb5d057dfd5be45fccff5f167(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb02f9b77a87433c8b9d6b48f135235ac3de84a5be40bb5487ba2e3246997da(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f1360f9c5aaed5bc369feaee2365646227cd1511a91d32cbac465cfcd60293(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6835c7eeffb5668efe17c4e3ac51081946f51332d7e6241f73251aaccfe996(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df3687269953443730a84709b5d7264f416b6b20ca7f006e81653de2273f701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122803584d716e2dec32b1d70c4c177262e69c915bc155e347de5d72c0ef9efd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b110ed0f2a18ec7eea13b23639a4ec81aa6d34d444485c263e552655ac065a5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9011a17a1efab59c981440f8e79b24e9cf01ef8d45d75449e34e939a3ec90b78(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e9b5120bbba8f90cfe1d39d40833a560251eb558c891b4515f0b11afa7c41f7(
    *,
    caching: builtins.str,
    storage_account_type: builtins.str,
    diff_disk_settings: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_encryption_set_id: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2544be1ca1b26dd3a99e4968befc505ba3a124f53fea701c4d8d164e139480(
    *,
    option: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e69195957e75f050de267a77ec456dcc3a1886ac76faafe497ff5216c9b165(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4570f5b673354dfc6066c6e1f118f6ca55213806751093e98cd998acb5b92e38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90b2a5e4badb3d8d5badb2e8481fdcc1062166bd304fcf9d4af7ff91719541e9(
    value: typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd625886c9286f15a6207d85a3c61fa1cc7e321444f652f723a47e2ca9fba5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7015d2205534b31af4baf9fbea00891f106d6bc8b71937d0bde49b94bfc7353c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd603cf4eda7a60a5bddd7cbd96fc78db6883604555b1304a3225bff39512e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33abaaf3e09d16993e1aa4e2d75a0684a27aa8a48465e2fd1dafbcb0bf138f23(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0466f881e59b943ccf7f78ec4d15bd052a345216fd10b8d85e0f6aaf8b0be6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543ebfd0a74d57ee2a08df40144f0cb71b477d277f7bbe44c3b83866d680b535(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55321916545d97e809f9cd1fcbdb8423b0dc272de55cf3a01c6eed70a387338e(
    value: typing.Optional[LinuxVirtualMachineScaleSetOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1379dee7be66745d38015b13eb6d54a5fef839d43518154a5b1989942cf9bdb1(
    *,
    name: builtins.str,
    product: builtins.str,
    publisher: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84c9180881ad7d3a52ac4dee96a169d76ed5d1c405b20fb4a279888131b958f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb489ebb9e2c3706381a220973d62a6ae06f01c8683ec52aae6414050082ffde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9125b8ab7e8a5e1acb3f4feae5fc1ed507e7e5eda7f1f31e9ff345664209a746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6536eed10b287812ab31ee93eae7d7ae858ab3b463ad1c1f02b74eff258c7415(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__054888d9f2576c48530250aa539dbbf805b97d525b13ebe170bda08cc0a668cb(
    value: typing.Optional[LinuxVirtualMachineScaleSetPlan],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3f9ae2b759dca6a853a3af0f50f78845e45f2d4705276d1df08a0607fb8e41(
    *,
    certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    key_vault_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__670b0d9bc64c580ab91dc503d45037e7373add71465f07351245ad338f1f4386(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ed56ccca84d415e474b7f7911472753871fe071a53a024c6e56124347a98a0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef6a65298984cd61e933b835c7d5ee3918949fe3fd123fdd7c07abf9813b5af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__059b65e1052e8b9d86612194af2a4f06bde2a09928715b80492ea24a373bc01e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad70fdc6883ca9a437c8d2e5b90ab0e6f3c22a1287c7b7953bb024f46f43d60(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03ab9894a55fa1a524488ff348f049be3070ac6b2994a4bc1f96bafd174d391(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7158563a225359690a2f74e43d87ecbcfb0cece7ea24455082e3d9cc68e87f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d6caf6b486366b974c03d4aeff1ec334006fb40cbf0235ccb5b466e232fff5(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ee978000794d6426b079a3903002e015ecb9c7e5f705f4f3d9de2cbf7f412cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e37d454e657d54b316cf03cf9973e0ad0caa8f703bf3a80bbdfe6ec899fe626(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74313e7e6af0d3718d22f08b18d08b3104b2797959c2bf62aad973f89270568(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c048ab94d4dd7ef88693e33c5cf36f7d7e17a81e28d09449d137558790a02a27(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5cefb2dd86a944c7a9ec1b0889d7854c44cb1e99c3e3c71fd2982182bcd939(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a542c50f9416bcc0a8547c90130052e09e76c74e51092930248907e8b9b1451(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c746d2adf88aa10f6ed718b4d21230848418e4fd13fa49309cbb39573f5a8bc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d0e1d92cfa4c82c41a8a47f8eb37bcdde1b307f389c96304167d960569e2b4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bde02ebe957fec73df32fc57c6e3368bfde563ff97e34686fb3087ae5772e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcaed1e18aed67d4017e6051d19bb86dacd19f47a950af09334d199e56a0e523(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e85a71277cec83d5bd89a7248827958ed323f6f5915fffc61041ab0edd88e6(
    *,
    offer: builtins.str,
    publisher: builtins.str,
    sku: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683a1a608e6556d2d218c2840530a3d165aeaa54166607f4f8ea48ef45d47994(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b2ceefed8b945b3a50dd4e977eba214f2775dfd0bbccf9204ea2b07fe1729f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417715268e0689daf664c1edac2e249371df35e607ea16a2bb9f3ca8993a1e08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edfe5f56979cb3a3a0c960953ae372af2f770a801f0713e2e13d1d09e4cf429f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fccb7c9d93345f1b46fadadee4c2518d288132c29916d2afb176d42d94bb057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5025054e8a26edab8bc8f276258095384cb5cf6ac9e94d4f852a258626f472c4(
    value: typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd39b1b25112a1b5ce9e59ca37de9f8c889acb5d1122c934a092179604f2ffc(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947f502267f1db3c7e610df0a067e21136edc89f4d025f301d2099618db88068(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e50c929a6115efc01455d39fa19782a12f9289632d563ae0153bdf6ae9d8142(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0441837a913326e13f9130cb4c7dfb2f1b44f3059b103fa46173541ee868136b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe6c56504b0f14dc8b68690ef8056ca8e87dcfea38b9dc84a7cd554452c1367(
    value: typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44308bf9ff007aa940baceadd666f89fc482145b23545b640a2b322cad68be2(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cfa1b19cf51c8a65a6ac75eb2af6028cb2ad5a102c7ed69e05624f46c86bb69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3e830fd560c8c1e58ccee6b44b28c5a7ba1af0b78f44f91b8823a138f5a5a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603cb1a459b1855808aa2d315aa477bfe20f2bff04a799911c5c38e6bffed320(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b112f2e2a2b44b69d4eb00e2165a934762c32f65cf43445ef1b5d632af0f83f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e346771ea2182a996cf249aa6d75f0dfc3c3c01f17e6e3369f35fd7ea333cd9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2217b8bdf72e5f2ab7c7439bfaa217ad9b12f240862b7bda572736415bfc9906(
    value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
