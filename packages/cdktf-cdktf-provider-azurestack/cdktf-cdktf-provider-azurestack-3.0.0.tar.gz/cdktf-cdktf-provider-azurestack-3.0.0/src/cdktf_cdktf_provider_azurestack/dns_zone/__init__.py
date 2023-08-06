'''
# `azurestack_dns_zone`

Refer to the Terraform Registory for docs: [`azurestack_dns_zone`](https://www.terraform.io/docs/providers/azurestack/r/dns_zone).
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


class DnsZone(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZone",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone azurestack_dns_zone}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        soa_record: typing.Optional[typing.Union["DnsZoneSoaRecord", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DnsZoneTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone azurestack_dns_zone} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#name DnsZone#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#resource_group_name DnsZone#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#id DnsZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param soa_record: soa_record block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#soa_record DnsZone#soa_record}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#timeouts DnsZone#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1645a717eea4240404fa50cbea2c67ed901fcd89a573e68a7fc5c619f448f4d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DnsZoneConfig(
            name=name,
            resource_group_name=resource_group_name,
            id=id,
            soa_record=soa_record,
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

    @jsii.member(jsii_name="putSoaRecord")
    def put_soa_record(
        self,
        *,
        email: builtins.str,
        host_name: builtins.str,
        expire_time: typing.Optional[jsii.Number] = None,
        minimum_ttl: typing.Optional[jsii.Number] = None,
        refresh_time: typing.Optional[jsii.Number] = None,
        retry_time: typing.Optional[jsii.Number] = None,
        serial_number: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#email DnsZone#email}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#host_name DnsZone#host_name}.
        :param expire_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#expire_time DnsZone#expire_time}.
        :param minimum_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#minimum_ttl DnsZone#minimum_ttl}.
        :param refresh_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#refresh_time DnsZone#refresh_time}.
        :param retry_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#retry_time DnsZone#retry_time}.
        :param serial_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#serial_number DnsZone#serial_number}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#ttl DnsZone#ttl}.
        '''
        value = DnsZoneSoaRecord(
            email=email,
            host_name=host_name,
            expire_time=expire_time,
            minimum_ttl=minimum_ttl,
            refresh_time=refresh_time,
            retry_time=retry_time,
            serial_number=serial_number,
            tags=tags,
            ttl=ttl,
        )

        return typing.cast(None, jsii.invoke(self, "putSoaRecord", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#create DnsZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#delete DnsZone#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#read DnsZone#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#update DnsZone#update}.
        '''
        value = DnsZoneTimeouts(create=create, delete=delete, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSoaRecord")
    def reset_soa_record(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoaRecord", []))

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
    @jsii.member(jsii_name="maxNumberOfRecordSets")
    def max_number_of_record_sets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNumberOfRecordSets"))

    @builtins.property
    @jsii.member(jsii_name="nameServers")
    def name_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameServers"))

    @builtins.property
    @jsii.member(jsii_name="numberOfRecordSets")
    def number_of_record_sets(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfRecordSets"))

    @builtins.property
    @jsii.member(jsii_name="soaRecord")
    def soa_record(self) -> "DnsZoneSoaRecordOutputReference":
        return typing.cast("DnsZoneSoaRecordOutputReference", jsii.get(self, "soaRecord"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DnsZoneTimeoutsOutputReference":
        return typing.cast("DnsZoneTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="soaRecordInput")
    def soa_record_input(self) -> typing.Optional["DnsZoneSoaRecord"]:
        return typing.cast(typing.Optional["DnsZoneSoaRecord"], jsii.get(self, "soaRecordInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DnsZoneTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DnsZoneTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aefc903e53e7f3460dec61cbf1760562c28ebb7e5f9bcd9ceb3326e496b45e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860ce9e967589223daa745aaddb2333760ad74df3c597979916c1d9406e64feb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa5205e4b8777c21ac19d34bacccc8a949001f42581fbfd0b5fc2e170a16515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742544d2713414c4eda88468f9f29e44690992fac316df671f46b992aafac850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZoneConfig",
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
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "soa_record": "soaRecord",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class DnsZoneConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        soa_record: typing.Optional[typing.Union["DnsZoneSoaRecord", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DnsZoneTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#name DnsZone#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#resource_group_name DnsZone#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#id DnsZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param soa_record: soa_record block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#soa_record DnsZone#soa_record}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#timeouts DnsZone#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(soa_record, dict):
            soa_record = DnsZoneSoaRecord(**soa_record)
        if isinstance(timeouts, dict):
            timeouts = DnsZoneTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543e9be4d17bd184b4d17d577ba9df2b466379d5d16e6c0e06268155f1868081)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument soa_record", value=soa_record, expected_type=type_hints["soa_record"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if id is not None:
            self._values["id"] = id
        if soa_record is not None:
            self._values["soa_record"] = soa_record
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#name DnsZone#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#resource_group_name DnsZone#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#id DnsZone#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def soa_record(self) -> typing.Optional["DnsZoneSoaRecord"]:
        '''soa_record block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#soa_record DnsZone#soa_record}
        '''
        result = self._values.get("soa_record")
        return typing.cast(typing.Optional["DnsZoneSoaRecord"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DnsZoneTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#timeouts DnsZone#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DnsZoneTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZoneSoaRecord",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "host_name": "hostName",
        "expire_time": "expireTime",
        "minimum_ttl": "minimumTtl",
        "refresh_time": "refreshTime",
        "retry_time": "retryTime",
        "serial_number": "serialNumber",
        "tags": "tags",
        "ttl": "ttl",
    },
)
class DnsZoneSoaRecord:
    def __init__(
        self,
        *,
        email: builtins.str,
        host_name: builtins.str,
        expire_time: typing.Optional[jsii.Number] = None,
        minimum_ttl: typing.Optional[jsii.Number] = None,
        refresh_time: typing.Optional[jsii.Number] = None,
        retry_time: typing.Optional[jsii.Number] = None,
        serial_number: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#email DnsZone#email}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#host_name DnsZone#host_name}.
        :param expire_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#expire_time DnsZone#expire_time}.
        :param minimum_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#minimum_ttl DnsZone#minimum_ttl}.
        :param refresh_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#refresh_time DnsZone#refresh_time}.
        :param retry_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#retry_time DnsZone#retry_time}.
        :param serial_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#serial_number DnsZone#serial_number}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#ttl DnsZone#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb5d876f147d23c38024ca68b3dee92fd64630d94f01be3ff2e47beb41b314f)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument expire_time", value=expire_time, expected_type=type_hints["expire_time"])
            check_type(argname="argument minimum_ttl", value=minimum_ttl, expected_type=type_hints["minimum_ttl"])
            check_type(argname="argument refresh_time", value=refresh_time, expected_type=type_hints["refresh_time"])
            check_type(argname="argument retry_time", value=retry_time, expected_type=type_hints["retry_time"])
            check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
            "host_name": host_name,
        }
        if expire_time is not None:
            self._values["expire_time"] = expire_time
        if minimum_ttl is not None:
            self._values["minimum_ttl"] = minimum_ttl
        if refresh_time is not None:
            self._values["refresh_time"] = refresh_time
        if retry_time is not None:
            self._values["retry_time"] = retry_time
        if serial_number is not None:
            self._values["serial_number"] = serial_number
        if tags is not None:
            self._values["tags"] = tags
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#email DnsZone#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#host_name DnsZone#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expire_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#expire_time DnsZone#expire_time}.'''
        result = self._values.get("expire_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#minimum_ttl DnsZone#minimum_ttl}.'''
        result = self._values.get("minimum_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def refresh_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#refresh_time DnsZone#refresh_time}.'''
        result = self._values.get("refresh_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#retry_time DnsZone#retry_time}.'''
        result = self._values.get("retry_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def serial_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#serial_number DnsZone#serial_number}.'''
        result = self._values.get("serial_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#tags DnsZone#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#ttl DnsZone#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsZoneSoaRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsZoneSoaRecordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZoneSoaRecordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a1c97ed60f13a4e058683f01ec96989c69ad81865bedf95bae89f7f126eb430)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpireTime")
    def reset_expire_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpireTime", []))

    @jsii.member(jsii_name="resetMinimumTtl")
    def reset_minimum_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTtl", []))

    @jsii.member(jsii_name="resetRefreshTime")
    def reset_refresh_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshTime", []))

    @jsii.member(jsii_name="resetRetryTime")
    def reset_retry_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryTime", []))

    @jsii.member(jsii_name="resetSerialNumber")
    def reset_serial_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSerialNumber", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="expireTimeInput")
    def expire_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expireTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTtlInput")
    def minimum_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTimeInput")
    def refresh_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "refreshTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="retryTimeInput")
    def retry_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="serialNumberInput")
    def serial_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serialNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa28f6ae57075cfd77f1fdf2322730593debf855222e8bcd41e6b50010167f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expireTime"))

    @expire_time.setter
    def expire_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeaa13dc4de451846372e286c2b13d5b5a01a778a7868aad3c423669d960b76c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expireTime", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0f27df0cae780ac2abdd005242df997c070ce10ed622735db98bf13139d5b8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTtl")
    def minimum_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumTtl"))

    @minimum_ttl.setter
    def minimum_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe092ea0d070851ed2c0d59d2940493de82bd8621ec149e5d9d9604101f28033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTtl", value)

    @builtins.property
    @jsii.member(jsii_name="refreshTime")
    def refresh_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshTime"))

    @refresh_time.setter
    def refresh_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f402fe85743e5844d9c5c6a102c09e527e671f6b597812dfb1ae9d3edbe06404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshTime", value)

    @builtins.property
    @jsii.member(jsii_name="retryTime")
    def retry_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryTime"))

    @retry_time.setter
    def retry_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__885f134184a95f43b54f6dbf68b8d9d9929dd8edbda66f06c24dda4f05a6e32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryTime", value)

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serialNumber"))

    @serial_number.setter
    def serial_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f1fdd9ee0e68e68e899f8c04c96a6040cfc024429929219f0768485b6281a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serialNumber", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c4c217538c668ab9b2a8200322e9ca813022036d3f3f5ce697f1f927d00643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7514d038ad63c45233bdb5ef2e6f29c9bdda8a521fa5fac806cee6c0685d0a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DnsZoneSoaRecord]:
        return typing.cast(typing.Optional[DnsZoneSoaRecord], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DnsZoneSoaRecord]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e56921d6d0cf214ee3b84285aad6bc406e94387947cea599f71814ac0bbacd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZoneTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DnsZoneTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#create DnsZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#delete DnsZone#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#read DnsZone#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#update DnsZone#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b6c37c9dffe0f651fa6e03b6cc59d752ccb3a1689f9f9b604d735a39ed5309e)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#create DnsZone#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#delete DnsZone#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#read DnsZone#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/dns_zone#update DnsZone#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsZoneTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsZoneTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.dnsZone.DnsZoneTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec1ee5f9df420dedac8e483cf45bf9a1db564732991a48a32b3056ad7b5d5d9a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee4881c3445d550ec5964d07d06a8145ea2a4e4503e149339af3d9cace3217f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabc223a5a42d51a8d066e31ec1ee3dd6f5a3abde88d6f4c11e1e6ef5b5760b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89defc9617f3f30bc75ef6b78c42c64fcbdb9de63741c9a12d3180c2241bf7f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fed261ef1abaae9041143c84c443a8682b81a41d16316bdc19e7a72b13537d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DnsZoneTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DnsZoneTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DnsZoneTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a704ed62350049f2624d5efe41660ec11279443d5963e7ca63594eb72e97dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DnsZone",
    "DnsZoneConfig",
    "DnsZoneSoaRecord",
    "DnsZoneSoaRecordOutputReference",
    "DnsZoneTimeouts",
    "DnsZoneTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__1645a717eea4240404fa50cbea2c67ed901fcd89a573e68a7fc5c619f448f4d6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    soa_record: typing.Optional[typing.Union[DnsZoneSoaRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DnsZoneTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__8aefc903e53e7f3460dec61cbf1760562c28ebb7e5f9bcd9ceb3326e496b45e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860ce9e967589223daa745aaddb2333760ad74df3c597979916c1d9406e64feb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa5205e4b8777c21ac19d34bacccc8a949001f42581fbfd0b5fc2e170a16515(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742544d2713414c4eda88468f9f29e44690992fac316df671f46b992aafac850(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543e9be4d17bd184b4d17d577ba9df2b466379d5d16e6c0e06268155f1868081(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    resource_group_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    soa_record: typing.Optional[typing.Union[DnsZoneSoaRecord, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[DnsZoneTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb5d876f147d23c38024ca68b3dee92fd64630d94f01be3ff2e47beb41b314f(
    *,
    email: builtins.str,
    host_name: builtins.str,
    expire_time: typing.Optional[jsii.Number] = None,
    minimum_ttl: typing.Optional[jsii.Number] = None,
    refresh_time: typing.Optional[jsii.Number] = None,
    retry_time: typing.Optional[jsii.Number] = None,
    serial_number: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ttl: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1c97ed60f13a4e058683f01ec96989c69ad81865bedf95bae89f7f126eb430(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa28f6ae57075cfd77f1fdf2322730593debf855222e8bcd41e6b50010167f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaa13dc4de451846372e286c2b13d5b5a01a778a7868aad3c423669d960b76c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f27df0cae780ac2abdd005242df997c070ce10ed622735db98bf13139d5b8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe092ea0d070851ed2c0d59d2940493de82bd8621ec149e5d9d9604101f28033(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f402fe85743e5844d9c5c6a102c09e527e671f6b597812dfb1ae9d3edbe06404(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__885f134184a95f43b54f6dbf68b8d9d9929dd8edbda66f06c24dda4f05a6e32f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f1fdd9ee0e68e68e899f8c04c96a6040cfc024429929219f0768485b6281a1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c4c217538c668ab9b2a8200322e9ca813022036d3f3f5ce697f1f927d00643(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7514d038ad63c45233bdb5ef2e6f29c9bdda8a521fa5fac806cee6c0685d0a8a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e56921d6d0cf214ee3b84285aad6bc406e94387947cea599f71814ac0bbacd(
    value: typing.Optional[DnsZoneSoaRecord],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6c37c9dffe0f651fa6e03b6cc59d752ccb3a1689f9f9b604d735a39ed5309e(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1ee5f9df420dedac8e483cf45bf9a1db564732991a48a32b3056ad7b5d5d9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4881c3445d550ec5964d07d06a8145ea2a4e4503e149339af3d9cace3217f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabc223a5a42d51a8d066e31ec1ee3dd6f5a3abde88d6f4c11e1e6ef5b5760b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89defc9617f3f30bc75ef6b78c42c64fcbdb9de63741c9a12d3180c2241bf7f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fed261ef1abaae9041143c84c443a8682b81a41d16316bdc19e7a72b13537d77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a704ed62350049f2624d5efe41660ec11279443d5963e7ca63594eb72e97dd(
    value: typing.Optional[typing.Union[DnsZoneTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
