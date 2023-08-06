'''
# `azurestack_image`

Refer to the Terraform Registory for docs: [`azurestack_image`](https://www.terraform.io/docs/providers/azurestack/r/image).
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


class Image(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.image.Image",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/image azurestack_image}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImageDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        os_disk: typing.Optional[typing.Union["ImageOsDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        source_virtual_machine_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ImageTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/image azurestack_image} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#location Image#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#name Image#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#resource_group_name Image#resource_group_name}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#data_disk Image#data_disk}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#id Image#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_disk Image#os_disk}
        :param source_virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#source_virtual_machine_id Image#source_virtual_machine_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#tags Image#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#timeouts Image#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9213f9063146711fba0bdfcdbb7da00417ceda242ec17bc143e0d8e6a2f242)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ImageConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            data_disk=data_disk,
            id=id,
            os_disk=os_disk,
            source_virtual_machine_id=source_virtual_machine_id,
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

    @jsii.member(jsii_name="putDataDisk")
    def put_data_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImageDataDisk", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4caa24d7f3cba509c639ce9c2e94c4f664626c1338023f7770b93ad604bf9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataDisk", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        blob_uri: typing.Optional[builtins.str] = None,
        caching: typing.Optional[builtins.str] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        os_state: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        size_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param blob_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#blob_uri Image#blob_uri}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#caching Image#caching}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#managed_disk_id Image#managed_disk_id}.
        :param os_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_state Image#os_state}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_type Image#os_type}.
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#size_gb Image#size_gb}.
        '''
        value = ImageOsDisk(
            blob_uri=blob_uri,
            caching=caching,
            managed_disk_id=managed_disk_id,
            os_state=os_state,
            os_type=os_type,
            size_gb=size_gb,
        )

        return typing.cast(None, jsii.invoke(self, "putOsDisk", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#create Image#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#delete Image#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#read Image#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#update Image#update}.
        '''
        value = ImageTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDataDisk")
    def reset_data_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataDisk", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOsDisk")
    def reset_os_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDisk", []))

    @jsii.member(jsii_name="resetSourceVirtualMachineId")
    def reset_source_virtual_machine_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceVirtualMachineId", []))

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
    @jsii.member(jsii_name="dataDisk")
    def data_disk(self) -> "ImageDataDiskList":
        return typing.cast("ImageDataDiskList", jsii.get(self, "dataDisk"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "ImageOsDiskOutputReference":
        return typing.cast("ImageOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ImageTimeoutsOutputReference":
        return typing.cast("ImageTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskInput")
    def data_disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImageDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImageDataDisk"]]], jsii.get(self, "dataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["ImageOsDisk"]:
        return typing.cast(typing.Optional["ImageOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVirtualMachineIdInput")
    def source_virtual_machine_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVirtualMachineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ImageTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ImageTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e58773a60566fd87ce149176923555b8caced0ed404c395a335f771f40cec79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0faad0e291f17de0253cb5d0c64ed4f6afa1cb6b2b34bb1a47409c639191e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95531487c3b1b5a1eb3d9c0f146ab1aac2050b4aa0d36c487f3322a1893fa1a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1e95dd01cd14065ff1038a706748f8d41e3a3b46ab6cd19a327abd8ce83eaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVirtualMachineId")
    def source_virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVirtualMachineId"))

    @source_virtual_machine_id.setter
    def source_virtual_machine_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a48fb1f17e766862f58629cd2c318249cbce0c6e6ae37d7b2752f0d339cfdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVirtualMachineId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b2940c362f679276be4a2d6580c99bc1fea6abe325284e2ae48334a6d335a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.image.ImageConfig",
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
        "resource_group_name": "resourceGroupName",
        "data_disk": "dataDisk",
        "id": "id",
        "os_disk": "osDisk",
        "source_virtual_machine_id": "sourceVirtualMachineId",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ImageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ImageDataDisk", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        os_disk: typing.Optional[typing.Union["ImageOsDisk", typing.Dict[builtins.str, typing.Any]]] = None,
        source_virtual_machine_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ImageTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#location Image#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#name Image#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#resource_group_name Image#resource_group_name}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#data_disk Image#data_disk}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#id Image#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_disk Image#os_disk}
        :param source_virtual_machine_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#source_virtual_machine_id Image#source_virtual_machine_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#tags Image#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#timeouts Image#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = ImageOsDisk(**os_disk)
        if isinstance(timeouts, dict):
            timeouts = ImageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa21a2131513d8b6398ef3f97410e205ec334df537cc73fad2ae81651be85a7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument data_disk", value=data_disk, expected_type=type_hints["data_disk"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument source_virtual_machine_id", value=source_virtual_machine_id, expected_type=type_hints["source_virtual_machine_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
            "name": name,
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
        if data_disk is not None:
            self._values["data_disk"] = data_disk
        if id is not None:
            self._values["id"] = id
        if os_disk is not None:
            self._values["os_disk"] = os_disk
        if source_virtual_machine_id is not None:
            self._values["source_virtual_machine_id"] = source_virtual_machine_id
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#location Image#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#name Image#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#resource_group_name Image#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImageDataDisk"]]]:
        '''data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#data_disk Image#data_disk}
        '''
        result = self._values.get("data_disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ImageDataDisk"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#id Image#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_disk(self) -> typing.Optional["ImageOsDisk"]:
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_disk Image#os_disk}
        '''
        result = self._values.get("os_disk")
        return typing.cast(typing.Optional["ImageOsDisk"], result)

    @builtins.property
    def source_virtual_machine_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#source_virtual_machine_id Image#source_virtual_machine_id}.'''
        result = self._values.get("source_virtual_machine_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#tags Image#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ImageTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#timeouts Image#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ImageTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.image.ImageDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "blob_uri": "blobUri",
        "caching": "caching",
        "lun": "lun",
        "managed_disk_id": "managedDiskId",
        "size_gb": "sizeGb",
    },
)
class ImageDataDisk:
    def __init__(
        self,
        *,
        blob_uri: typing.Optional[builtins.str] = None,
        caching: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        size_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param blob_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#blob_uri Image#blob_uri}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#caching Image#caching}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#lun Image#lun}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#managed_disk_id Image#managed_disk_id}.
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#size_gb Image#size_gb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64dbc8e8f28a3716e2439b30fb1e1a76e8cd0d06bc7222c301e5e3094f841ae)
            check_type(argname="argument blob_uri", value=blob_uri, expected_type=type_hints["blob_uri"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument managed_disk_id", value=managed_disk_id, expected_type=type_hints["managed_disk_id"])
            check_type(argname="argument size_gb", value=size_gb, expected_type=type_hints["size_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if blob_uri is not None:
            self._values["blob_uri"] = blob_uri
        if caching is not None:
            self._values["caching"] = caching
        if lun is not None:
            self._values["lun"] = lun
        if managed_disk_id is not None:
            self._values["managed_disk_id"] = managed_disk_id
        if size_gb is not None:
            self._values["size_gb"] = size_gb

    @builtins.property
    def blob_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#blob_uri Image#blob_uri}.'''
        result = self._values.get("blob_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#caching Image#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#lun Image#lun}.'''
        result = self._values.get("lun")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#managed_disk_id Image#managed_disk_id}.'''
        result = self._values.get("managed_disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#size_gb Image#size_gb}.'''
        result = self._values.get("size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageDataDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.image.ImageDataDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7177131d42344646b1564bb4e50f94df460681f7f7059d2f211fcd3bf6ff16c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ImageDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876115770cc7aa8d0917cdd601b98c4201f5fba7cbbf87db2b0a923670334ef3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ImageDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d04e7e0834405b4a5240f67e8192767a7f0ca210f256fa44ec3a463a620a129)
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
            type_hints = typing.get_type_hints(_typecheckingstub__758c83d869af5d31170660dc8573c98c5e0fa6fa1a6ec90dc5d1420f016803c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__335a4fc42994b24198a51803510d14119c4446bf132aa665c1e32c2f79e3ab4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImageDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImageDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImageDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773a304beef9cf626deac9aced26c21f8ebfd783298445950d0d7a56fc322381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ImageDataDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.image.ImageDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64c0cf2bb7e1fdf17b61a1f3dd66525bb484025b7edcd6528a49ce31fcace968)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBlobUri")
    def reset_blob_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobUri", []))

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetManagedDiskId")
    def reset_managed_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskId", []))

    @jsii.member(jsii_name="resetSizeGb")
    def reset_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeGb", []))

    @builtins.property
    @jsii.member(jsii_name="blobUriInput")
    def blob_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobUriInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskIdInput")
    def managed_disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeGbInput")
    def size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="blobUri")
    def blob_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobUri"))

    @blob_uri.setter
    def blob_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22384e866a948df4756c7cd8990813d70e96bdb9b46465df55fe02b670bd3531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobUri", value)

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510c7b42ce95de49a0a9315077bb95dbb218696b1839ae5000c7df4be8cb93f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32107ff7db54328dc873f6ac1c668b354fcef46961fecf14749d51994c0b0c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskId")
    def managed_disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskId"))

    @managed_disk_id.setter
    def managed_disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__114e6e6cc404e18be5e4eaa1773c29c4103e0a3304a133a32fad837d93b851de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskId", value)

    @builtins.property
    @jsii.member(jsii_name="sizeGb")
    def size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGb"))

    @size_gb.setter
    def size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f607f99ccb14f877905c4d7d194965dc9b2b55f21f82ffc0b4c1eea75e3fc4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ImageDataDisk, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ImageDataDisk, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ImageDataDisk, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b460aa35b249d4425710edc64be0a4494eb88115f45d7a9f700b57d5775cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.image.ImageOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "blob_uri": "blobUri",
        "caching": "caching",
        "managed_disk_id": "managedDiskId",
        "os_state": "osState",
        "os_type": "osType",
        "size_gb": "sizeGb",
    },
)
class ImageOsDisk:
    def __init__(
        self,
        *,
        blob_uri: typing.Optional[builtins.str] = None,
        caching: typing.Optional[builtins.str] = None,
        managed_disk_id: typing.Optional[builtins.str] = None,
        os_state: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        size_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param blob_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#blob_uri Image#blob_uri}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#caching Image#caching}.
        :param managed_disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#managed_disk_id Image#managed_disk_id}.
        :param os_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_state Image#os_state}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_type Image#os_type}.
        :param size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#size_gb Image#size_gb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf04c11fe9d30689a734be42dbcb1a6d21e6c3f35fcaf4f34d91bda9ba67dfed)
            check_type(argname="argument blob_uri", value=blob_uri, expected_type=type_hints["blob_uri"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument managed_disk_id", value=managed_disk_id, expected_type=type_hints["managed_disk_id"])
            check_type(argname="argument os_state", value=os_state, expected_type=type_hints["os_state"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument size_gb", value=size_gb, expected_type=type_hints["size_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if blob_uri is not None:
            self._values["blob_uri"] = blob_uri
        if caching is not None:
            self._values["caching"] = caching
        if managed_disk_id is not None:
            self._values["managed_disk_id"] = managed_disk_id
        if os_state is not None:
            self._values["os_state"] = os_state
        if os_type is not None:
            self._values["os_type"] = os_type
        if size_gb is not None:
            self._values["size_gb"] = size_gb

    @builtins.property
    def blob_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#blob_uri Image#blob_uri}.'''
        result = self._values.get("blob_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#caching Image#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#managed_disk_id Image#managed_disk_id}.'''
        result = self._values.get("managed_disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_state Image#os_state}.'''
        result = self._values.get("os_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#os_type Image#os_type}.'''
        result = self._values.get("os_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#size_gb Image#size_gb}.'''
        result = self._values.get("size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageOsDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.image.ImageOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__29f416d4aee0f978f162e9b68a4cee5c92e144b9fffcec6851d76f882dd2313f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBlobUri")
    def reset_blob_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobUri", []))

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetManagedDiskId")
    def reset_managed_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskId", []))

    @jsii.member(jsii_name="resetOsState")
    def reset_os_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsState", []))

    @jsii.member(jsii_name="resetOsType")
    def reset_os_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsType", []))

    @jsii.member(jsii_name="resetSizeGb")
    def reset_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeGb", []))

    @builtins.property
    @jsii.member(jsii_name="blobUriInput")
    def blob_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobUriInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskIdInput")
    def managed_disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="osStateInput")
    def os_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osStateInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeGbInput")
    def size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="blobUri")
    def blob_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobUri"))

    @blob_uri.setter
    def blob_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb32d09f4c505f96941ce648417d30d6008d06bb908a557b73b4272ceafcde65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobUri", value)

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4107998546d4797faaa5e276aece589497dc27c060f518c3d7d29823b1f4749)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskId")
    def managed_disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskId"))

    @managed_disk_id.setter
    def managed_disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a21635053f3ca2a6400f27c7c002fc9376e73deb9b3de4763a601d90a4d683)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskId", value)

    @builtins.property
    @jsii.member(jsii_name="osState")
    def os_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osState"))

    @os_state.setter
    def os_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98bf8226dc9fe011e041b568d63cfee2e7fc29d10916c5485acfad2aeaa828af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osState", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f2b969e97a74818c1e9627c20d4edb6516f78921480f66d27893991997f2e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="sizeGb")
    def size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeGb"))

    @size_gb.setter
    def size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8b508a56aaab19ced8e83af02f8899b6971e2e75e588560636967fa38b892c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ImageOsDisk]:
        return typing.cast(typing.Optional[ImageOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ImageOsDisk]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14466b3c8aca6a22d1ff38c732213874077c6dadf82c2367eceff3058deb1271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.image.ImageTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ImageTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#create Image#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#delete Image#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#read Image#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#update Image#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c905c1ba12d6c48171188b5a584273e06413682231090a2a3f12869598281b96)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#create Image#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#delete Image#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#read Image#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/image#update Image#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.image.ImageTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8446ec7063060d9b003925905b422c46ebc129aca98e4e45168e98db550d2b4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50a5c8711bce483133a693a632bad6bed14bfbe15a7358a4cba9bf90742608e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eccd6a333ec4d94320033848c4dbd57ecdd91728768be45b398e2f6becaef02d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__701ebf902c3e95d2675d6b603010eecec1ff88fe08547f221f75b273c80401e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86ebd5434cfeb1c1c466e9ede8fc8d83d49b626314cd898b283d32a25fbcc0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ImageTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ImageTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ImageTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8970688c2f1d75d529626d05359210731fd19ded13b251bf1bbf425958de88b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Image",
    "ImageConfig",
    "ImageDataDisk",
    "ImageDataDiskList",
    "ImageDataDiskOutputReference",
    "ImageOsDisk",
    "ImageOsDiskOutputReference",
    "ImageTimeouts",
    "ImageTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__0a9213f9063146711fba0bdfcdbb7da00417ceda242ec17bc143e0d8e6a2f242(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    location: builtins.str,
    name: builtins.str,
    resource_group_name: builtins.str,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImageDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    os_disk: typing.Optional[typing.Union[ImageOsDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    source_virtual_machine_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ImageTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__ae4caa24d7f3cba509c639ce9c2e94c4f664626c1338023f7770b93ad604bf9f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImageDataDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58773a60566fd87ce149176923555b8caced0ed404c395a335f771f40cec79f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0faad0e291f17de0253cb5d0c64ed4f6afa1cb6b2b34bb1a47409c639191e8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95531487c3b1b5a1eb3d9c0f146ab1aac2050b4aa0d36c487f3322a1893fa1a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1e95dd01cd14065ff1038a706748f8d41e3a3b46ab6cd19a327abd8ce83eaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a48fb1f17e766862f58629cd2c318249cbce0c6e6ae37d7b2752f0d339cfdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b2940c362f679276be4a2d6580c99bc1fea6abe325284e2ae48334a6d335a6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa21a2131513d8b6398ef3f97410e205ec334df537cc73fad2ae81651be85a7(
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
    resource_group_name: builtins.str,
    data_disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ImageDataDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    os_disk: typing.Optional[typing.Union[ImageOsDisk, typing.Dict[builtins.str, typing.Any]]] = None,
    source_virtual_machine_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ImageTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64dbc8e8f28a3716e2439b30fb1e1a76e8cd0d06bc7222c301e5e3094f841ae(
    *,
    blob_uri: typing.Optional[builtins.str] = None,
    caching: typing.Optional[builtins.str] = None,
    lun: typing.Optional[jsii.Number] = None,
    managed_disk_id: typing.Optional[builtins.str] = None,
    size_gb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7177131d42344646b1564bb4e50f94df460681f7f7059d2f211fcd3bf6ff16c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876115770cc7aa8d0917cdd601b98c4201f5fba7cbbf87db2b0a923670334ef3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d04e7e0834405b4a5240f67e8192767a7f0ca210f256fa44ec3a463a620a129(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__758c83d869af5d31170660dc8573c98c5e0fa6fa1a6ec90dc5d1420f016803c3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__335a4fc42994b24198a51803510d14119c4446bf132aa665c1e32c2f79e3ab4b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773a304beef9cf626deac9aced26c21f8ebfd783298445950d0d7a56fc322381(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ImageDataDisk]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c0cf2bb7e1fdf17b61a1f3dd66525bb484025b7edcd6528a49ce31fcace968(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22384e866a948df4756c7cd8990813d70e96bdb9b46465df55fe02b670bd3531(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510c7b42ce95de49a0a9315077bb95dbb218696b1839ae5000c7df4be8cb93f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32107ff7db54328dc873f6ac1c668b354fcef46961fecf14749d51994c0b0c06(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114e6e6cc404e18be5e4eaa1773c29c4103e0a3304a133a32fad837d93b851de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f607f99ccb14f877905c4d7d194965dc9b2b55f21f82ffc0b4c1eea75e3fc4f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b460aa35b249d4425710edc64be0a4494eb88115f45d7a9f700b57d5775cf8(
    value: typing.Optional[typing.Union[ImageDataDisk, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf04c11fe9d30689a734be42dbcb1a6d21e6c3f35fcaf4f34d91bda9ba67dfed(
    *,
    blob_uri: typing.Optional[builtins.str] = None,
    caching: typing.Optional[builtins.str] = None,
    managed_disk_id: typing.Optional[builtins.str] = None,
    os_state: typing.Optional[builtins.str] = None,
    os_type: typing.Optional[builtins.str] = None,
    size_gb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f416d4aee0f978f162e9b68a4cee5c92e144b9fffcec6851d76f882dd2313f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb32d09f4c505f96941ce648417d30d6008d06bb908a557b73b4272ceafcde65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4107998546d4797faaa5e276aece589497dc27c060f518c3d7d29823b1f4749(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a21635053f3ca2a6400f27c7c002fc9376e73deb9b3de4763a601d90a4d683(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98bf8226dc9fe011e041b568d63cfee2e7fc29d10916c5485acfad2aeaa828af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f2b969e97a74818c1e9627c20d4edb6516f78921480f66d27893991997f2e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8b508a56aaab19ced8e83af02f8899b6971e2e75e588560636967fa38b892c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14466b3c8aca6a22d1ff38c732213874077c6dadf82c2367eceff3058deb1271(
    value: typing.Optional[ImageOsDisk],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c905c1ba12d6c48171188b5a584273e06413682231090a2a3f12869598281b96(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8446ec7063060d9b003925905b422c46ebc129aca98e4e45168e98db550d2b4b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a5c8711bce483133a693a632bad6bed14bfbe15a7358a4cba9bf90742608e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccd6a333ec4d94320033848c4dbd57ecdd91728768be45b398e2f6becaef02d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__701ebf902c3e95d2675d6b603010eecec1ff88fe08547f221f75b273c80401e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86ebd5434cfeb1c1c466e9ede8fc8d83d49b626314cd898b283d32a25fbcc0f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8970688c2f1d75d529626d05359210731fd19ded13b251bf1bbf425958de88b7(
    value: typing.Optional[typing.Union[ImageTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
