'''
# `azurestack_linux_virtual_machine`

Refer to the Terraform Registory for docs: [`azurestack_linux_virtual_machine`](https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine).
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


class LinuxVirtualMachine(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine azurestack_linux_virtual_machine}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        admin_username: builtins.str,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["LinuxVirtualMachineOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["LinuxVirtualMachineAdditionalCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineAdminSshKey", typing.Dict[builtins.str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union["LinuxVirtualMachineBootDiagnostics", typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine azurestack_linux_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_username LinuxVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#location LinuxVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#network_interface_ids LinuxVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#os_disk LinuxVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#resource_group_name LinuxVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#size LinuxVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#additional_capabilities LinuxVirtualMachine#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_password LinuxVirtualMachine#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_ssh_key LinuxVirtualMachine#admin_ssh_key}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#allow_extension_operations LinuxVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#availability_set_id LinuxVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#boot_diagnostics LinuxVirtualMachine#boot_diagnostics}
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#computer_name LinuxVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#custom_data LinuxVirtualMachine#custom_data}.
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disable_password_authentication LinuxVirtualMachine#disable_password_authentication}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#encryption_at_host_enabled LinuxVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#eviction_policy LinuxVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#extensions_time_budget LinuxVirtualMachine#extensions_time_budget}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#id LinuxVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#license_type LinuxVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#max_bid_price LinuxVirtualMachine#max_bid_price}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#plan LinuxVirtualMachine#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#priority LinuxVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#provision_vm_agent LinuxVirtualMachine#provision_vm_agent}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#secret LinuxVirtualMachine#secret}
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_id LinuxVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_reference LinuxVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#tags LinuxVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#timeouts LinuxVirtualMachine#timeouts}
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#virtual_machine_scale_set_id LinuxVirtualMachine#virtual_machine_scale_set_id}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#zone LinuxVirtualMachine#zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20479399a4a21a2d30af9e4456f43ecccf7a61505e96781d211d85f59289fca0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LinuxVirtualMachineConfig(
            admin_username=admin_username,
            location=location,
            name=name,
            network_interface_ids=network_interface_ids,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            size=size,
            additional_capabilities=additional_capabilities,
            admin_password=admin_password,
            admin_ssh_key=admin_ssh_key,
            allow_extension_operations=allow_extension_operations,
            availability_set_id=availability_set_id,
            boot_diagnostics=boot_diagnostics,
            computer_name=computer_name,
            custom_data=custom_data,
            disable_password_authentication=disable_password_authentication,
            encryption_at_host_enabled=encryption_at_host_enabled,
            eviction_policy=eviction_policy,
            extensions_time_budget=extensions_time_budget,
            id=id,
            license_type=license_type,
            max_bid_price=max_bid_price,
            plan=plan,
            priority=priority,
            provision_vm_agent=provision_vm_agent,
            secret=secret,
            source_image_id=source_image_id,
            source_image_reference=source_image_reference,
            tags=tags,
            timeouts=timeouts,
            virtual_machine_scale_set_id=virtual_machine_scale_set_id,
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
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#ultra_ssd_enabled LinuxVirtualMachine#ultra_ssd_enabled}.
        '''
        value = LinuxVirtualMachineAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdminSshKey")
    def put_admin_ssh_key(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineAdminSshKey", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd9f2a1aa3bb925116a39970ee8adb3cc3058b11c7df6908f48071c17188a08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdminSshKey", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_uri LinuxVirtualMachine#storage_account_uri}.
        '''
        value = LinuxVirtualMachineBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#caching LinuxVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_type LinuxVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#diff_disk_settings LinuxVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_encryption_set_id LinuxVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_size_gb LinuxVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#write_accelerator_enabled LinuxVirtualMachine#write_accelerator_enabled}.
        '''
        value = LinuxVirtualMachineOsDisk(
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#product LinuxVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.
        '''
        value = LinuxVirtualMachinePlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6082abb21add8560656037befaca19890ef5eeab79cf5dc1bc259a4f071b43de)
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
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#offer LinuxVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#sku LinuxVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#version LinuxVirtualMachine#version}.
        '''
        value = LinuxVirtualMachineSourceImageReference(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#create LinuxVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#delete LinuxVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#read LinuxVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#update LinuxVirtualMachine#update}.
        '''
        value = LinuxVirtualMachineTimeouts(
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

    @jsii.member(jsii_name="resetDisablePasswordAuthentication")
    def reset_disable_password_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePasswordAuthentication", []))

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

    @jsii.member(jsii_name="resetVirtualMachineScaleSetId")
    def reset_virtual_machine_scale_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachineScaleSetId", []))

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
    ) -> "LinuxVirtualMachineAdditionalCapabilitiesOutputReference":
        return typing.cast("LinuxVirtualMachineAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKey")
    def admin_ssh_key(self) -> "LinuxVirtualMachineAdminSshKeyList":
        return typing.cast("LinuxVirtualMachineAdminSshKeyList", jsii.get(self, "adminSshKey"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(self) -> "LinuxVirtualMachineBootDiagnosticsOutputReference":
        return typing.cast("LinuxVirtualMachineBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "LinuxVirtualMachineOsDiskOutputReference":
        return typing.cast("LinuxVirtualMachineOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "LinuxVirtualMachinePlanOutputReference":
        return typing.cast("LinuxVirtualMachinePlanOutputReference", jsii.get(self, "plan"))

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
    def secret(self) -> "LinuxVirtualMachineSecretList":
        return typing.cast("LinuxVirtualMachineSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "LinuxVirtualMachineSourceImageReferenceOutputReference":
        return typing.cast("LinuxVirtualMachineSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LinuxVirtualMachineTimeoutsOutputReference":
        return typing.cast("LinuxVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineAdditionalCapabilities"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKeyInput")
    def admin_ssh_key_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineAdminSshKey"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineAdminSshKey"]]], jsii.get(self, "adminSshKeyInput"))

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
    ) -> typing.Optional["LinuxVirtualMachineBootDiagnostics"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNameInput")
    def computer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthenticationInput")
    def disable_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disablePasswordAuthenticationInput"))

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
    def os_disk_input(self) -> typing.Optional["LinuxVirtualMachineOsDisk"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["LinuxVirtualMachinePlan"]:
        return typing.cast(typing.Optional["LinuxVirtualMachinePlan"], jsii.get(self, "planInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecret"]]], jsii.get(self, "secretInput"))

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
    ) -> typing.Optional["LinuxVirtualMachineSourceImageReference"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LinuxVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LinuxVirtualMachineTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetIdInput")
    def virtual_machine_scale_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineScaleSetIdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__dc923e1bab6bd4d30223fcce600f3614bcf92d9065b975461f42e4ba0febfe44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d88bb2eb3d981509792aa353bace74759d779c96088c8b145716b47b2bdca27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__490f1b990307af60380871fdeb38ccd831ececac3601387e307958ee0b4adf6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExtensionOperations", value)

    @builtins.property
    @jsii.member(jsii_name="availabilitySetId")
    def availability_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilitySetId"))

    @availability_set_id.setter
    def availability_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93d661af35d0b92d0ba4d0d728fca550e1a66c00d86046e63c041f0468a19b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilitySetId", value)

    @builtins.property
    @jsii.member(jsii_name="computerName")
    def computer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerName"))

    @computer_name.setter
    def computer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f22c8ea4f2c31560659e597954e288ea1d108f7315867fb6826eac2b9bfb4ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerName", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db096847e834b0ae218769df4e59cc357d8c8d75e024e3e6b26400844b80c0e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca1320681619e4de8ac063d3bd8990f852b2e45200dfb7ef3fade151b49fb8b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordAuthentication", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__7c964246312a8829944859a1bf0c6e1ea8c0cd9843ca8d00bbd2d50c45340c04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="evictionPolicy")
    def eviction_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evictionPolicy"))

    @eviction_policy.setter
    def eviction_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__036bc0b5f4a6cfaf1c503e0a0b12894134f63222be3b44aee1482396afed4a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evictionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="extensionsTimeBudget")
    def extensions_time_budget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extensionsTimeBudget"))

    @extensions_time_budget.setter
    def extensions_time_budget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a7208b6617f03384180ac2d914e009d327424042bda07a2238e89c68a8a377)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionsTimeBudget", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ca7260e6cd498ab6d255e1e22dfb9b19753f14b27cd5757b1629f3fff25503c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b7cc99b9e2a47b2c33b0c85b81bf6f2773c88b633c0a1c24eeedd24d8291260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d48ca0f579ae289e1a4cb1c51e9ff8db106d090324156c95db2764bc8ed0a338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maxBidPrice")
    def max_bid_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBidPrice"))

    @max_bid_price.setter
    def max_bid_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c67db29979496ade42fefc28c18c01a55952aa5bba5429a829d52b71138b9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3e2cbd71816550411e5564ab785208a548f06a061864af2137bb19df983947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @network_interface_ids.setter
    def network_interface_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f48f05d659297ac463e89e20428d80979881f221f1cb87b44feb79f60a434c47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceIds", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a019d42438732eabd1f52ccb466d9fb70d1a464f1cdf6036fa472e483d0e49e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22f0ef2810e3e50216ef49aaaf969510f6c1cee9ef22d9ca99156153fcd03c14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51bf6cac27a211fa2342cce7819419de15d58af2630552db3e9a2fcb3af39831)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad574987a7922ad333b2527120fa9bff8da000f6bac677ebc7fa26b21c0e1e53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7917cb568ddaaa9ed0019bbed454fa3346169fe4e36530c4aa1ece834e00ad53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f42f622e23dd41b9753c88a1417b25c90ff5dc167b4c38bbe9f7912328b5d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetId")
    def virtual_machine_scale_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineScaleSetId"))

    @virtual_machine_scale_set_id.setter
    def virtual_machine_scale_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dfec20236330ca02616cd965691f998d37b3743ec5fd8926f33574acf03f9ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineScaleSetId", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5740d61e0c648575c7b70d2334cf8d8c03e25eb99c360730c947a926eb95b396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class LinuxVirtualMachineAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#ultra_ssd_enabled LinuxVirtualMachine#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede19b36679ed00d01de0bace21d510fdb57763ab62b1b86405beeff3573ebd4)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#ultra_ssd_enabled LinuxVirtualMachine#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineAdditionalCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a256d3a247a13a0aa687af1cdb55378cf1b29ec4d8ff26f048d59bbdf10205e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dac806c3fccfbeddb3d2e4d478e65a6270e17b34231db3ce39d9dd74af5b0bd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineAdditionalCapabilities]:
        return typing.cast(typing.Optional[LinuxVirtualMachineAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f28bde23143d9256f4e773d905077d4f81086728eb654ef6c0b83fec4983d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineAdminSshKey",
    jsii_struct_bases=[],
    name_mapping={"public_key": "publicKey", "username": "username"},
)
class LinuxVirtualMachineAdminSshKey:
    def __init__(self, *, public_key: builtins.str, username: builtins.str) -> None:
        '''
        :param public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#public_key LinuxVirtualMachine#public_key}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#username LinuxVirtualMachine#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb22e848f843bc9e7289d2d797cc357a5ec5bd3da019af0d69a7d9d14190ae9b)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key": public_key,
            "username": username,
        }

    @builtins.property
    def public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#public_key LinuxVirtualMachine#public_key}.'''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#username LinuxVirtualMachine#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineAdminSshKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineAdminSshKeyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineAdminSshKeyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94a12f6e0ba7be9009443ede001b72a5b6566c0f44540a19f8d9c334551486bd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineAdminSshKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3a76978d5047a5b5f5ed8fca1129be3d52ecf2cdecffb0886438e78680f1c80)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineAdminSshKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__250aff0c42ca46f180b83d77cbe1318501bd575dbe3ea512ac41add878f2a4c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69ae779529101edd5c2f5e93f9469d664b506f16b52662e8744020ed063c6e23)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3d50f498a4fc37a7ccfa4ef2b68922650cf25589bbcfdbbe414682a0072ccb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d62e4f9a55c42586324687cdb7a4bbfe7693cc7b09d9d3f09b875d852c8bdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineAdminSshKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineAdminSshKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3782a94943a498aeb08c49db212a1b2c08875a04791d68cde1ecd3206fe067b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a96664d41d137c25375424537e1904545b21cdfa2c67f0bb76f4e4043ec2bdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb87d95f32abf9a16975fb57393ec463edb4015f918c0609464d16167eb603df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineAdminSshKey, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineAdminSshKey, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineAdminSshKey, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9bb480dfb5c62587148cfe679327e48e4f0171f1cfb01a6f46beca1bf892074)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class LinuxVirtualMachineBootDiagnostics:
    def __init__(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_uri LinuxVirtualMachine#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2048fed9c4adb97a0b474fdb60a43ae91b8418ba5fd6ccbcd0cbc88c62fbd2c0)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_account_uri": storage_account_uri,
        }

    @builtins.property
    def storage_account_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_uri LinuxVirtualMachine#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        assert result is not None, "Required property 'storage_account_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineBootDiagnosticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a691207a0d83d2a64afaa1996a939d1e53a9779cd831340fa5e304954c052f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8244de93caef63091ceab774f3740f919431a575c389fc25e8488f761eabccfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineBootDiagnostics]:
        return typing.cast(typing.Optional[LinuxVirtualMachineBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d515e7e268d1807740b53d731a2ff2cd1f3c1ada9a2fa23a3c79435a711204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineConfig",
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
        "location": "location",
        "name": "name",
        "network_interface_ids": "networkInterfaceIds",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "size": "size",
        "additional_capabilities": "additionalCapabilities",
        "admin_password": "adminPassword",
        "admin_ssh_key": "adminSshKey",
        "allow_extension_operations": "allowExtensionOperations",
        "availability_set_id": "availabilitySetId",
        "boot_diagnostics": "bootDiagnostics",
        "computer_name": "computerName",
        "custom_data": "customData",
        "disable_password_authentication": "disablePasswordAuthentication",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "eviction_policy": "evictionPolicy",
        "extensions_time_budget": "extensionsTimeBudget",
        "id": "id",
        "license_type": "licenseType",
        "max_bid_price": "maxBidPrice",
        "plan": "plan",
        "priority": "priority",
        "provision_vm_agent": "provisionVmAgent",
        "secret": "secret",
        "source_image_id": "sourceImageId",
        "source_image_reference": "sourceImageReference",
        "tags": "tags",
        "timeouts": "timeouts",
        "virtual_machine_scale_set_id": "virtualMachineScaleSetId",
        "zone": "zone",
    },
)
class LinuxVirtualMachineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["LinuxVirtualMachineOsDisk", typing.Dict[builtins.str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachinePlan", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineSecret", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineSourceImageReference", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
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
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_username LinuxVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#location LinuxVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#network_interface_ids LinuxVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#os_disk LinuxVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#resource_group_name LinuxVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#size LinuxVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#additional_capabilities LinuxVirtualMachine#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_password LinuxVirtualMachine#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_ssh_key LinuxVirtualMachine#admin_ssh_key}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#allow_extension_operations LinuxVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#availability_set_id LinuxVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#boot_diagnostics LinuxVirtualMachine#boot_diagnostics}
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#computer_name LinuxVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#custom_data LinuxVirtualMachine#custom_data}.
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disable_password_authentication LinuxVirtualMachine#disable_password_authentication}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#encryption_at_host_enabled LinuxVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#eviction_policy LinuxVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#extensions_time_budget LinuxVirtualMachine#extensions_time_budget}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#id LinuxVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#license_type LinuxVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#max_bid_price LinuxVirtualMachine#max_bid_price}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#plan LinuxVirtualMachine#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#priority LinuxVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#provision_vm_agent LinuxVirtualMachine#provision_vm_agent}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#secret LinuxVirtualMachine#secret}
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_id LinuxVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_reference LinuxVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#tags LinuxVirtualMachine#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#timeouts LinuxVirtualMachine#timeouts}
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#virtual_machine_scale_set_id LinuxVirtualMachine#virtual_machine_scale_set_id}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#zone LinuxVirtualMachine#zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = LinuxVirtualMachineOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = LinuxVirtualMachineAdditionalCapabilities(**additional_capabilities)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = LinuxVirtualMachineBootDiagnostics(**boot_diagnostics)
        if isinstance(plan, dict):
            plan = LinuxVirtualMachinePlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = LinuxVirtualMachineSourceImageReference(**source_image_reference)
        if isinstance(timeouts, dict):
            timeouts = LinuxVirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e57000f214777641303bd424ae824ec66eace3e5b49b3a0f258d032eddc4c53)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface_ids", value=network_interface_ids, expected_type=type_hints["network_interface_ids"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_ssh_key", value=admin_ssh_key, expected_type=type_hints["admin_ssh_key"])
            check_type(argname="argument allow_extension_operations", value=allow_extension_operations, expected_type=type_hints["allow_extension_operations"])
            check_type(argname="argument availability_set_id", value=availability_set_id, expected_type=type_hints["availability_set_id"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument computer_name", value=computer_name, expected_type=type_hints["computer_name"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument disable_password_authentication", value=disable_password_authentication, expected_type=type_hints["disable_password_authentication"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument eviction_policy", value=eviction_policy, expected_type=type_hints["eviction_policy"])
            check_type(argname="argument extensions_time_budget", value=extensions_time_budget, expected_type=type_hints["extensions_time_budget"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument max_bid_price", value=max_bid_price, expected_type=type_hints["max_bid_price"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument source_image_id", value=source_image_id, expected_type=type_hints["source_image_id"])
            check_type(argname="argument source_image_reference", value=source_image_reference, expected_type=type_hints["source_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_machine_scale_set_id", value=virtual_machine_scale_set_id, expected_type=type_hints["virtual_machine_scale_set_id"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_ssh_key is not None:
            self._values["admin_ssh_key"] = admin_ssh_key
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
        if disable_password_authentication is not None:
            self._values["disable_password_authentication"] = disable_password_authentication
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
        if virtual_machine_scale_set_id is not None:
            self._values["virtual_machine_scale_set_id"] = virtual_machine_scale_set_id
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
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_username LinuxVirtualMachine#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#location LinuxVirtualMachine#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#network_interface_ids LinuxVirtualMachine#network_interface_ids}.'''
        result = self._values.get("network_interface_ids")
        assert result is not None, "Required property 'network_interface_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def os_disk(self) -> "LinuxVirtualMachineOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#os_disk LinuxVirtualMachine#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("LinuxVirtualMachineOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#resource_group_name LinuxVirtualMachine#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#size LinuxVirtualMachine#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[LinuxVirtualMachineAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#additional_capabilities LinuxVirtualMachine#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[LinuxVirtualMachineAdditionalCapabilities], result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_password LinuxVirtualMachine#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_ssh_key(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]]:
        '''admin_ssh_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#admin_ssh_key LinuxVirtualMachine#admin_ssh_key}
        '''
        result = self._values.get("admin_ssh_key")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]], result)

    @builtins.property
    def allow_extension_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#allow_extension_operations LinuxVirtualMachine#allow_extension_operations}.'''
        result = self._values.get("allow_extension_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#availability_set_id LinuxVirtualMachine#availability_set_id}.'''
        result = self._values.get("availability_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_diagnostics(self) -> typing.Optional[LinuxVirtualMachineBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#boot_diagnostics LinuxVirtualMachine#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[LinuxVirtualMachineBootDiagnostics], result)

    @builtins.property
    def computer_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#computer_name LinuxVirtualMachine#computer_name}.'''
        result = self._values.get("computer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#custom_data LinuxVirtualMachine#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_password_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disable_password_authentication LinuxVirtualMachine#disable_password_authentication}.'''
        result = self._values.get("disable_password_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#encryption_at_host_enabled LinuxVirtualMachine#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def eviction_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#eviction_policy LinuxVirtualMachine#eviction_policy}.'''
        result = self._values.get("eviction_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extensions_time_budget(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#extensions_time_budget LinuxVirtualMachine#extensions_time_budget}.'''
        result = self._values.get("extensions_time_budget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#id LinuxVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#license_type LinuxVirtualMachine#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_bid_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#max_bid_price LinuxVirtualMachine#max_bid_price}.'''
        result = self._values.get("max_bid_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def plan(self) -> typing.Optional["LinuxVirtualMachinePlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#plan LinuxVirtualMachine#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["LinuxVirtualMachinePlan"], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#priority LinuxVirtualMachine#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#provision_vm_agent LinuxVirtualMachine#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#secret LinuxVirtualMachine#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecret"]]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_id LinuxVirtualMachine#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["LinuxVirtualMachineSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#source_image_reference LinuxVirtualMachine#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["LinuxVirtualMachineSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#tags LinuxVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LinuxVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#timeouts LinuxVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LinuxVirtualMachineTimeouts"], result)

    @builtins.property
    def virtual_machine_scale_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#virtual_machine_scale_set_id LinuxVirtualMachine#virtual_machine_scale_set_id}.'''
        result = self._values.get("virtual_machine_scale_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#zone LinuxVirtualMachine#zone}.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineOsDisk",
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
class LinuxVirtualMachineOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineOsDiskDiffDiskSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#caching LinuxVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_type LinuxVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#diff_disk_settings LinuxVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_encryption_set_id LinuxVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_size_gb LinuxVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#write_accelerator_enabled LinuxVirtualMachine#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = LinuxVirtualMachineOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572faa8e5767f8f212a37a380479b83bac4390f697a5385edb3b12e4e58dc007)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#caching LinuxVirtualMachine#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#storage_account_type LinuxVirtualMachine#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["LinuxVirtualMachineOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#diff_disk_settings LinuxVirtualMachine#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["LinuxVirtualMachineOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_encryption_set_id LinuxVirtualMachine#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#disk_size_gb LinuxVirtualMachine#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#write_accelerator_enabled LinuxVirtualMachine#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option"},
)
class LinuxVirtualMachineOsDiskDiffDiskSettings:
    def __init__(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#option LinuxVirtualMachine#option}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c3b13f53fc0ca857b3b1772f422cc2c24f8143a93b4e18982d381667b71bfb)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "option": option,
        }

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#option LinuxVirtualMachine#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineOsDiskDiffDiskSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__772f4130c9d47ec75f2b5d5e8f7748d0331302a87a397d4b4ec8b68d98e03d44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__002856d48135495f7d483d4f27322270bbe025b0acda89b466a13acf2d702eaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a7504eb59d87b812f96b32f80068809ab223139e1f60a54397c77df6ee24945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd234fcba6da6aae10e5f4291962124aa184bbd41a6edb5b70f9120641782a8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#option LinuxVirtualMachine#option}.
        '''
        value = LinuxVirtualMachineOsDiskDiffDiskSettings(option=option)

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
    ) -> LinuxVirtualMachineOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(LinuxVirtualMachineOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__502d8a3e1dddd26959e4909bd275b1fccb0a341caaee109d16948019d8d9a8a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb38c1befa95f6c4e49bc019e09d9c94145f60a5b33a55526dc4ced5f2dab75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c6a148aacf8d92099937225066bbcc59c6929dec9b3c0de37cd17ea26cbd964)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__010eb976fc231cd306ef4b72a401cc28bcf6fd251d5d6ac9236a752c44673f88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d2e96d9e4e5d64c4b3132aca7c30a598b895e1fb0c361caebe3941adb5cd0a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0d95859d1442347dc6f727a39c4ca95aaf56cf951489f2d59b1c931bc8ffe81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineOsDisk]:
        return typing.cast(typing.Optional[LinuxVirtualMachineOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxVirtualMachineOsDisk]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74923ed94a4b29b7922564ede1a0241867476c703b967d5f077b23ba3badfe3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachinePlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class LinuxVirtualMachinePlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#product LinuxVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7e7669d6b849bf33a345fd3f98b4c6cf0c3d2271098b409a9589657d4eca86)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#name LinuxVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#product LinuxVirtualMachine#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachinePlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachinePlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachinePlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a616da6c052033dc10f0220ec4e7ce05f625f4bcce6433736cb3dd290efb180)
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
            type_hints = typing.get_type_hints(_typecheckingstub__238baad8014d4a469cd9e3820efc1eaa6b2219fd25992ef0cd3e7dc3827d4ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3676c7ea449544d2ae2ba3582f0bf3b36ec083ff58b60c1ef6b363bbbecde73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272b59f52bc9743a3c56365a336065ea4ef01580dac9c7d58afbcf8645895c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachinePlan]:
        return typing.cast(typing.Optional[LinuxVirtualMachinePlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LinuxVirtualMachinePlan]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0eb623582a375da786173267849c02738ba3a90475166f40cc8fb7d3e8940a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class LinuxVirtualMachineSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineSecretCertificate", typing.Dict[builtins.str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#certificate LinuxVirtualMachine#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#key_vault_id LinuxVirtualMachine#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510dec20be477dcf1321c85d85c8edf1427f20445d3a13014ec3e00858fc838b)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#certificate LinuxVirtualMachine#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["LinuxVirtualMachineSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#key_vault_id LinuxVirtualMachine#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={},
)
class LinuxVirtualMachineSecretCertificate:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineSecretCertificateList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecretCertificateList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5af81364ea3041d30fb8c491b8ff2ed75cf6dc33ddddaa802307e9fff0a951ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c690bda11d343e77fdc5b021a04c0fbae88a79881e4e1fae84fe8d8ca4403d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da81ba754f8be5a2b37d065e2a3851f4c3d4f7ca2e864c8e45ea74fd3968fc63)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc68a30f4f875ae160b82c07de26556db36168c3e843919ab41f4a15064bb04f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46d2abbe6a368f05a07e9ff26d75758e7421dac7ba08371400e26c5a5521a8c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__917d172ca07951d1baa4bd3b45cc1ab926b8c8d9ae2409fded5b0d176cbdbd6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineSecretCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d94ffb6e4b7e2c39cdffa16b299d73162f5f1ae1e83b4ea832d8122d08747ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41b3b4481375781e2a6959c2a442d3db4d551c2f4dc9ca90853dc978eb429de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineSecretList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecretList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__722a3596fcf14994b5a9ec2dd745f98a95d871a3f2ffffa6586428b87ec1acdd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LinuxVirtualMachineSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d083fde34f332940c8d718a73cbd8f7892b3e83ea5ab60f05411aa58738fcd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d67e7a259ad9b89b6680fd62a607f98c99efdf0bd6a33981c9f1fe8436fe106)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49c142230bbe0faa29389abc8c3d03354fafca753b134597b8bea64fa7ce8fac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50f5b1b8da985df4c785cc8f80c15bf56947742dc7686097f091f2a8337fede8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecret]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a2f35c1dd633bd3c47c506dc2072367ba2834a11e54b52097a88b286ad0477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineSecretOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSecretOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__79a22d0660ec7a6123288693b188c68c7e9c9c51a1746f66d97bb623a632463f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7352ec38d754ef467d72c5c2da5817bd1c8d28afcd1c6729f74c3ebf1a0231a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> LinuxVirtualMachineSecretCertificateList:
        return typing.cast(LinuxVirtualMachineSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]], jsii.get(self, "certificateInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__571dc63f2396a31b9a495918f2c81193032a50e18438fb505ed4e20aa23c522b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d78b41e38fca191a5fa619812ec78044f17066d85ac3d569956d5f743c9923a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class LinuxVirtualMachineSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#offer LinuxVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#sku LinuxVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#version LinuxVirtualMachine#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f1bf92ea23441ef08df7e3381c00395a36bcbe0ffad60f9859fd5c161ca18fb)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#offer LinuxVirtualMachine#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#publisher LinuxVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#sku LinuxVirtualMachine#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#version LinuxVirtualMachine#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineSourceImageReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f638d8c7eac1f2efb5633744304a0724cdcb759bc97791a7c3c2ac4e19bf18c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__016fee168b64bc731653f0b8abc04b742958c3ca7c157feef07de0bd6e123f3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2f183c549ede637afce680b393b4e2f7c4e1d86ce4f38bdaed2e91fc8cb0e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__758cf49b39db19a4d37eb997e71e269a682be08df0b983f81e41b02b57dc170a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f81b5db356eec65f23dbf5ba407ad4718bcadd95817f89801146fb45d6776c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineSourceImageReference]:
        return typing.cast(typing.Optional[LinuxVirtualMachineSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7239099bc375443162e3977dfeb06367080098c861eae6630de3fd49d65ab5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LinuxVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#create LinuxVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#delete LinuxVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#read LinuxVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#update LinuxVirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258c143659d17ad61dfa6c050fe0b6de1b5bbe69ee44bd65863f151f071039fd)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#create LinuxVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#delete LinuxVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#read LinuxVirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine#update LinuxVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachine.LinuxVirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4d1b4d77fc0bf52a650f015cfad4646bd93f69b6954762bdb448d709d47206b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca849e0f7091110a899d3b0d04ecca20e56e8ec537394001aae28c5426d8f304)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c943dc761b207d435ab7b9ba4932ffbd50ffccc057e4af7f5d702b393757d16c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8cbdb00acbefef98311224db7554a92c6be73c4afa5f2a8779496e20ca391c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82884eab0e0ba12494f7812684d791e69f071a594114ee3c3abce12cf45d2514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32855825b10388bd55bb9121e677f108d18c272f72fab46c7318cb4089b182ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LinuxVirtualMachine",
    "LinuxVirtualMachineAdditionalCapabilities",
    "LinuxVirtualMachineAdditionalCapabilitiesOutputReference",
    "LinuxVirtualMachineAdminSshKey",
    "LinuxVirtualMachineAdminSshKeyList",
    "LinuxVirtualMachineAdminSshKeyOutputReference",
    "LinuxVirtualMachineBootDiagnostics",
    "LinuxVirtualMachineBootDiagnosticsOutputReference",
    "LinuxVirtualMachineConfig",
    "LinuxVirtualMachineOsDisk",
    "LinuxVirtualMachineOsDiskDiffDiskSettings",
    "LinuxVirtualMachineOsDiskDiffDiskSettingsOutputReference",
    "LinuxVirtualMachineOsDiskOutputReference",
    "LinuxVirtualMachinePlan",
    "LinuxVirtualMachinePlanOutputReference",
    "LinuxVirtualMachineSecret",
    "LinuxVirtualMachineSecretCertificate",
    "LinuxVirtualMachineSecretCertificateList",
    "LinuxVirtualMachineSecretCertificateOutputReference",
    "LinuxVirtualMachineSecretList",
    "LinuxVirtualMachineSecretOutputReference",
    "LinuxVirtualMachineSourceImageReference",
    "LinuxVirtualMachineSourceImageReferenceOutputReference",
    "LinuxVirtualMachineTimeouts",
    "LinuxVirtualMachineTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__20479399a4a21a2d30af9e4456f43ecccf7a61505e96781d211d85f59289fca0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    admin_username: builtins.str,
    location: builtins.str,
    name: builtins.str,
    network_interface_ids: typing.Sequence[builtins.str],
    os_disk: typing.Union[LinuxVirtualMachineOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    size: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_password: typing.Optional[builtins.str] = None,
    admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    eviction_policy: typing.Optional[builtins.str] = None,
    extensions_time_budget: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    max_bid_price: typing.Optional[jsii.Number] = None,
    plan: typing.Optional[typing.Union[LinuxVirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[builtins.str] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[LinuxVirtualMachineSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__3dd9f2a1aa3bb925116a39970ee8adb3cc3058b11c7df6908f48071c17188a08(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineAdminSshKey, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6082abb21add8560656037befaca19890ef5eeab79cf5dc1bc259a4f071b43de(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc923e1bab6bd4d30223fcce600f3614bcf92d9065b975461f42e4ba0febfe44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d88bb2eb3d981509792aa353bace74759d779c96088c8b145716b47b2bdca27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490f1b990307af60380871fdeb38ccd831ececac3601387e307958ee0b4adf6a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d661af35d0b92d0ba4d0d728fca550e1a66c00d86046e63c041f0468a19b09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f22c8ea4f2c31560659e597954e288ea1d108f7315867fb6826eac2b9bfb4ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db096847e834b0ae218769df4e59cc357d8c8d75e024e3e6b26400844b80c0e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca1320681619e4de8ac063d3bd8990f852b2e45200dfb7ef3fade151b49fb8b4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c964246312a8829944859a1bf0c6e1ea8c0cd9843ca8d00bbd2d50c45340c04(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__036bc0b5f4a6cfaf1c503e0a0b12894134f63222be3b44aee1482396afed4a1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a7208b6617f03384180ac2d914e009d327424042bda07a2238e89c68a8a377(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca7260e6cd498ab6d255e1e22dfb9b19753f14b27cd5757b1629f3fff25503c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7cc99b9e2a47b2c33b0c85b81bf6f2773c88b633c0a1c24eeedd24d8291260(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d48ca0f579ae289e1a4cb1c51e9ff8db106d090324156c95db2764bc8ed0a338(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c67db29979496ade42fefc28c18c01a55952aa5bba5429a829d52b71138b9d0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3e2cbd71816550411e5564ab785208a548f06a061864af2137bb19df983947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48f05d659297ac463e89e20428d80979881f221f1cb87b44feb79f60a434c47(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a019d42438732eabd1f52ccb466d9fb70d1a464f1cdf6036fa472e483d0e49e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f0ef2810e3e50216ef49aaaf969510f6c1cee9ef22d9ca99156153fcd03c14(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51bf6cac27a211fa2342cce7819419de15d58af2630552db3e9a2fcb3af39831(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad574987a7922ad333b2527120fa9bff8da000f6bac677ebc7fa26b21c0e1e53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7917cb568ddaaa9ed0019bbed454fa3346169fe4e36530c4aa1ece834e00ad53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f42f622e23dd41b9753c88a1417b25c90ff5dc167b4c38bbe9f7912328b5d16(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dfec20236330ca02616cd965691f998d37b3743ec5fd8926f33574acf03f9ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5740d61e0c648575c7b70d2334cf8d8c03e25eb99c360730c947a926eb95b396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede19b36679ed00d01de0bace21d510fdb57763ab62b1b86405beeff3573ebd4(
    *,
    ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a256d3a247a13a0aa687af1cdb55378cf1b29ec4d8ff26f048d59bbdf10205e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac806c3fccfbeddb3d2e4d478e65a6270e17b34231db3ce39d9dd74af5b0bd7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f28bde23143d9256f4e773d905077d4f81086728eb654ef6c0b83fec4983d41(
    value: typing.Optional[LinuxVirtualMachineAdditionalCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb22e848f843bc9e7289d2d797cc357a5ec5bd3da019af0d69a7d9d14190ae9b(
    *,
    public_key: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a12f6e0ba7be9009443ede001b72a5b6566c0f44540a19f8d9c334551486bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3a76978d5047a5b5f5ed8fca1129be3d52ecf2cdecffb0886438e78680f1c80(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250aff0c42ca46f180b83d77cbe1318501bd575dbe3ea512ac41add878f2a4c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69ae779529101edd5c2f5e93f9469d664b506f16b52662e8744020ed063c6e23(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d50f498a4fc37a7ccfa4ef2b68922650cf25589bbcfdbbe414682a0072ccb7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d62e4f9a55c42586324687cdb7a4bbfe7693cc7b09d9d3f09b875d852c8bdd4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineAdminSshKey]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3782a94943a498aeb08c49db212a1b2c08875a04791d68cde1ecd3206fe067b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a96664d41d137c25375424537e1904545b21cdfa2c67f0bb76f4e4043ec2bdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb87d95f32abf9a16975fb57393ec463edb4015f918c0609464d16167eb603df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bb480dfb5c62587148cfe679327e48e4f0171f1cfb01a6f46beca1bf892074(
    value: typing.Optional[typing.Union[LinuxVirtualMachineAdminSshKey, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2048fed9c4adb97a0b474fdb60a43ae91b8418ba5fd6ccbcd0cbc88c62fbd2c0(
    *,
    storage_account_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a691207a0d83d2a64afaa1996a939d1e53a9779cd831340fa5e304954c052f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8244de93caef63091ceab774f3740f919431a575c389fc25e8488f761eabccfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d515e7e268d1807740b53d731a2ff2cd1f3c1ada9a2fa23a3c79435a711204(
    value: typing.Optional[LinuxVirtualMachineBootDiagnostics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e57000f214777641303bd424ae824ec66eace3e5b49b3a0f258d032eddc4c53(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    admin_username: builtins.str,
    location: builtins.str,
    name: builtins.str,
    network_interface_ids: typing.Sequence[builtins.str],
    os_disk: typing.Union[LinuxVirtualMachineOsDisk, typing.Dict[builtins.str, typing.Any]],
    resource_group_name: builtins.str,
    size: builtins.str,
    additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineAdditionalCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_password: typing.Optional[builtins.str] = None,
    admin_ssh_key: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineAdminSshKey, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_extension_operations: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_set_id: typing.Optional[builtins.str] = None,
    boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineBootDiagnostics, typing.Dict[builtins.str, typing.Any]]] = None,
    computer_name: typing.Optional[builtins.str] = None,
    custom_data: typing.Optional[builtins.str] = None,
    disable_password_authentication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    eviction_policy: typing.Optional[builtins.str] = None,
    extensions_time_budget: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    license_type: typing.Optional[builtins.str] = None,
    max_bid_price: typing.Optional[jsii.Number] = None,
    plan: typing.Optional[typing.Union[LinuxVirtualMachinePlan, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[builtins.str] = None,
    provision_vm_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecret, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_image_id: typing.Optional[builtins.str] = None,
    source_image_reference: typing.Optional[typing.Union[LinuxVirtualMachineSourceImageReference, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572faa8e5767f8f212a37a380479b83bac4390f697a5385edb3b12e4e58dc007(
    *,
    caching: builtins.str,
    storage_account_type: builtins.str,
    diff_disk_settings: typing.Optional[typing.Union[LinuxVirtualMachineOsDiskDiffDiskSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_encryption_set_id: typing.Optional[builtins.str] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c3b13f53fc0ca857b3b1772f422cc2c24f8143a93b4e18982d381667b71bfb(
    *,
    option: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772f4130c9d47ec75f2b5d5e8f7748d0331302a87a397d4b4ec8b68d98e03d44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__002856d48135495f7d483d4f27322270bbe025b0acda89b466a13acf2d702eaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7504eb59d87b812f96b32f80068809ab223139e1f60a54397c77df6ee24945(
    value: typing.Optional[LinuxVirtualMachineOsDiskDiffDiskSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd234fcba6da6aae10e5f4291962124aa184bbd41a6edb5b70f9120641782a8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502d8a3e1dddd26959e4909bd275b1fccb0a341caaee109d16948019d8d9a8a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb38c1befa95f6c4e49bc019e09d9c94145f60a5b33a55526dc4ced5f2dab75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c6a148aacf8d92099937225066bbcc59c6929dec9b3c0de37cd17ea26cbd964(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__010eb976fc231cd306ef4b72a401cc28bcf6fd251d5d6ac9236a752c44673f88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d2e96d9e4e5d64c4b3132aca7c30a598b895e1fb0c361caebe3941adb5cd0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0d95859d1442347dc6f727a39c4ca95aaf56cf951489f2d59b1c931bc8ffe81(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74923ed94a4b29b7922564ede1a0241867476c703b967d5f077b23ba3badfe3e(
    value: typing.Optional[LinuxVirtualMachineOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7e7669d6b849bf33a345fd3f98b4c6cf0c3d2271098b409a9589657d4eca86(
    *,
    name: builtins.str,
    product: builtins.str,
    publisher: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a616da6c052033dc10f0220ec4e7ce05f625f4bcce6433736cb3dd290efb180(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238baad8014d4a469cd9e3820efc1eaa6b2219fd25992ef0cd3e7dc3827d4ad8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3676c7ea449544d2ae2ba3582f0bf3b36ec083ff58b60c1ef6b363bbbecde73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272b59f52bc9743a3c56365a336065ea4ef01580dac9c7d58afbcf8645895c8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0eb623582a375da786173267849c02738ba3a90475166f40cc8fb7d3e8940a8(
    value: typing.Optional[LinuxVirtualMachinePlan],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510dec20be477dcf1321c85d85c8edf1427f20445d3a13014ec3e00858fc838b(
    *,
    certificate: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
    key_vault_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af81364ea3041d30fb8c491b8ff2ed75cf6dc33ddddaa802307e9fff0a951ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c690bda11d343e77fdc5b021a04c0fbae88a79881e4e1fae84fe8d8ca4403d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da81ba754f8be5a2b37d065e2a3851f4c3d4f7ca2e864c8e45ea74fd3968fc63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc68a30f4f875ae160b82c07de26556db36168c3e843919ab41f4a15064bb04f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46d2abbe6a368f05a07e9ff26d75758e7421dac7ba08371400e26c5a5521a8c3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__917d172ca07951d1baa4bd3b45cc1ab926b8c8d9ae2409fded5b0d176cbdbd6c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecretCertificate]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d94ffb6e4b7e2c39cdffa16b299d73162f5f1ae1e83b4ea832d8122d08747ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41b3b4481375781e2a6959c2a442d3db4d551c2f4dc9ca90853dc978eb429de(
    value: typing.Optional[typing.Union[LinuxVirtualMachineSecretCertificate, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722a3596fcf14994b5a9ec2dd745f98a95d871a3f2ffffa6586428b87ec1acdd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d083fde34f332940c8d718a73cbd8f7892b3e83ea5ab60f05411aa58738fcd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d67e7a259ad9b89b6680fd62a607f98c99efdf0bd6a33981c9f1fe8436fe106(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49c142230bbe0faa29389abc8c3d03354fafca753b134597b8bea64fa7ce8fac(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f5b1b8da985df4c785cc8f80c15bf56947742dc7686097f091f2a8337fede8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a2f35c1dd633bd3c47c506dc2072367ba2834a11e54b52097a88b286ad0477(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[LinuxVirtualMachineSecret]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a22d0660ec7a6123288693b188c68c7e9c9c51a1746f66d97bb623a632463f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7352ec38d754ef467d72c5c2da5817bd1c8d28afcd1c6729f74c3ebf1a0231a8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineSecretCertificate, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571dc63f2396a31b9a495918f2c81193032a50e18438fb505ed4e20aa23c522b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d78b41e38fca191a5fa619812ec78044f17066d85ac3d569956d5f743c9923a(
    value: typing.Optional[typing.Union[LinuxVirtualMachineSecret, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1bf92ea23441ef08df7e3381c00395a36bcbe0ffad60f9859fd5c161ca18fb(
    *,
    offer: builtins.str,
    publisher: builtins.str,
    sku: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f638d8c7eac1f2efb5633744304a0724cdcb759bc97791a7c3c2ac4e19bf18c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016fee168b64bc731653f0b8abc04b742958c3ca7c157feef07de0bd6e123f3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2f183c549ede637afce680b393b4e2f7c4e1d86ce4f38bdaed2e91fc8cb0e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758cf49b39db19a4d37eb997e71e269a682be08df0b983f81e41b02b57dc170a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f81b5db356eec65f23dbf5ba407ad4718bcadd95817f89801146fb45d6776c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7239099bc375443162e3977dfeb06367080098c861eae6630de3fd49d65ab5c(
    value: typing.Optional[LinuxVirtualMachineSourceImageReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258c143659d17ad61dfa6c050fe0b6de1b5bbe69ee44bd65863f151f071039fd(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d1b4d77fc0bf52a650f015cfad4646bd93f69b6954762bdb448d709d47206b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca849e0f7091110a899d3b0d04ecca20e56e8ec537394001aae28c5426d8f304(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c943dc761b207d435ab7b9ba4932ffbd50ffccc057e4af7f5d702b393757d16c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8cbdb00acbefef98311224db7554a92c6be73c4afa5f2a8779496e20ca391c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82884eab0e0ba12494f7812684d791e69f071a594114ee3c3abce12cf45d2514(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32855825b10388bd55bb9121e677f108d18c272f72fab46c7318cb4089b182ce(
    value: typing.Optional[typing.Union[LinuxVirtualMachineTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
