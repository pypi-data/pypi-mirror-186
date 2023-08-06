'''
# `provider`

Refer to the Terraform Registory for docs: [`azurestack`](https://www.terraform.io/docs/providers/azurestack).
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


class AzurestackProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack azurestack}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        features: typing.Union["AzurestackProviderFeatures", typing.Dict[builtins.str, typing.Any]],
        alias: typing.Optional[builtins.str] = None,
        arm_endpoint: typing.Optional[builtins.str] = None,
        auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata_host: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        skip_provider_registration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack azurestack} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        :param arm_endpoint: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        :param auxiliary_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.
        :param client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        :param client_id: The Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        :param client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        :param disable_correlation_request_id: This will disable the x-ms-correlation-request-id header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        :param environment: The Cloud Environment which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        :param metadata_host: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        :param msi_endpoint: The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        :param skip_provider_registration: Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        :param subscription_id: The Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        :param tenant_id: The Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        :param use_msi: Allowed Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428634929d9a0769a631ca657a927c9a82708246fb14d86de901db6853a28a75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AzurestackProviderConfig(
            features=features,
            alias=alias,
            arm_endpoint=arm_endpoint,
            auxiliary_tenant_ids=auxiliary_tenant_ids,
            client_certificate_password=client_certificate_password,
            client_certificate_path=client_certificate_path,
            client_id=client_id,
            client_secret=client_secret,
            disable_correlation_request_id=disable_correlation_request_id,
            environment=environment,
            metadata_host=metadata_host,
            msi_endpoint=msi_endpoint,
            skip_provider_registration=skip_provider_registration,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            use_msi=use_msi,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetArmEndpoint")
    def reset_arm_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArmEndpoint", []))

    @jsii.member(jsii_name="resetAuxiliaryTenantIds")
    def reset_auxiliary_tenant_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuxiliaryTenantIds", []))

    @jsii.member(jsii_name="resetClientCertificatePassword")
    def reset_client_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePassword", []))

    @jsii.member(jsii_name="resetClientCertificatePath")
    def reset_client_certificate_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePath", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetDisableCorrelationRequestId")
    def reset_disable_correlation_request_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableCorrelationRequestId", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetMetadataHost")
    def reset_metadata_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataHost", []))

    @jsii.member(jsii_name="resetMsiEndpoint")
    def reset_msi_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiEndpoint", []))

    @jsii.member(jsii_name="resetSkipProviderRegistration")
    def reset_skip_provider_registration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipProviderRegistration", []))

    @jsii.member(jsii_name="resetSubscriptionId")
    def reset_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @jsii.member(jsii_name="resetUseMsi")
    def reset_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseMsi", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="armEndpointInput")
    def arm_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "armEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="auxiliaryTenantIdsInput")
    def auxiliary_tenant_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auxiliaryTenantIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePasswordInput")
    def client_certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePathInput")
    def client_certificate_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="disableCorrelationRequestIdInput")
    def disable_correlation_request_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableCorrelationRequestIdInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="featuresInput")
    def features_input(self) -> typing.Optional["AzurestackProviderFeatures"]:
        return typing.cast(typing.Optional["AzurestackProviderFeatures"], jsii.get(self, "featuresInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataHostInput")
    def metadata_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataHostInput"))

    @builtins.property
    @jsii.member(jsii_name="msiEndpointInput")
    def msi_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="skipProviderRegistrationInput")
    def skip_provider_registration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipProviderRegistrationInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useMsiInput")
    def use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff7ab2110a39c26c96860c0a4e31c7862686b528ec67dd561e3fc9e919e0e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="armEndpoint")
    def arm_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "armEndpoint"))

    @arm_endpoint.setter
    def arm_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c25cfc2c433bd49b8f503640a6182db1cbed417c7def6a0a9f7e6f6f0c2fd0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "armEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="auxiliaryTenantIds")
    def auxiliary_tenant_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auxiliaryTenantIds"))

    @auxiliary_tenant_ids.setter
    def auxiliary_tenant_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d57d62ab4365ec27bf83fa281b650474e224324aec78481ced056eda909ca4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auxiliaryTenantIds", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePassword")
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePassword"))

    @client_certificate_password.setter
    def client_certificate_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a345d4d1d86b3f030e09b056a4e5a66eda70c118e414cfb9cfbd301ac6c7d93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePath")
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePath"))

    @client_certificate_path.setter
    def client_certificate_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f57d449cb825937e7e40b41f675a445403f6fe273851da45674deb708bef6b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff703924232fea474dc45e29724b7ec59432c7eae57784b7d7050137575305e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33eb25126d87b3b1ee8bce5ef3cce334fbf0faddbbfa696a783c31e1194b841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="disableCorrelationRequestId")
    def disable_correlation_request_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableCorrelationRequestId"))

    @disable_correlation_request_id.setter
    def disable_correlation_request_id(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a50968557b69125bfd557bbe55447bba88521eb2de007716b02b1a2d06ca9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableCorrelationRequestId", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575b80a8bf97e804aeeafb024c61c047ded29e9ab0b82ba3bccce65a47b11e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(self) -> typing.Optional["AzurestackProviderFeatures"]:
        return typing.cast(typing.Optional["AzurestackProviderFeatures"], jsii.get(self, "features"))

    @features.setter
    def features(self, value: typing.Optional["AzurestackProviderFeatures"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38aae7f9cae0426b19186497f1123a3f9300628d4054b9b7f3afef96c2e754b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "features", value)

    @builtins.property
    @jsii.member(jsii_name="metadataHost")
    def metadata_host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataHost"))

    @metadata_host.setter
    def metadata_host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b7b3dc3969fed92e0e76637e40b6411f6560e3086252054ba33522c2594ca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataHost", value)

    @builtins.property
    @jsii.member(jsii_name="msiEndpoint")
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpoint"))

    @msi_endpoint.setter
    def msi_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9baa89435048858e83126fed4b13bd782e0fc22a7f4ca7ce1d7676d9a8210fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "msiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="skipProviderRegistration")
    def skip_provider_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipProviderRegistration"))

    @skip_provider_registration.setter
    def skip_provider_registration(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8ad69bf48dfe565c80c8a4f20787d5885d1f8c30caf569c22f29c3e9d0b2991)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipProviderRegistration", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc02226416ebc3681a1ee959d2f1d0a69beb1d017f6234f8e0cebf9bc19dcb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe0a8ea91691f03c8cac6ea5898cb839fbfcc230c4baeee388ccf19e879f622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="useMsi")
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useMsi"))

    @use_msi.setter
    def use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba07eb5e0dab2261d511aab8758e8870beb60dd810ba78d5b041d26cd3089b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useMsi", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "features": "features",
        "alias": "alias",
        "arm_endpoint": "armEndpoint",
        "auxiliary_tenant_ids": "auxiliaryTenantIds",
        "client_certificate_password": "clientCertificatePassword",
        "client_certificate_path": "clientCertificatePath",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "disable_correlation_request_id": "disableCorrelationRequestId",
        "environment": "environment",
        "metadata_host": "metadataHost",
        "msi_endpoint": "msiEndpoint",
        "skip_provider_registration": "skipProviderRegistration",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "use_msi": "useMsi",
    },
)
class AzurestackProviderConfig:
    def __init__(
        self,
        *,
        features: typing.Union["AzurestackProviderFeatures", typing.Dict[builtins.str, typing.Any]],
        alias: typing.Optional[builtins.str] = None,
        arm_endpoint: typing.Optional[builtins.str] = None,
        auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata_host: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        skip_provider_registration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        :param arm_endpoint: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        :param auxiliary_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.
        :param client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        :param client_id: The Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        :param client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        :param disable_correlation_request_id: This will disable the x-ms-correlation-request-id header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        :param environment: The Cloud Environment which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        :param metadata_host: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        :param msi_endpoint: The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        :param skip_provider_registration: Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        :param subscription_id: The Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        :param tenant_id: The Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        :param use_msi: Allowed Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        if isinstance(features, dict):
            features = AzurestackProviderFeatures(**features)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab56d5e589ceff3c24c196bd8c9a6e099fa45f1fdd70c9d3c743411f36b6af54)
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument arm_endpoint", value=arm_endpoint, expected_type=type_hints["arm_endpoint"])
            check_type(argname="argument auxiliary_tenant_ids", value=auxiliary_tenant_ids, expected_type=type_hints["auxiliary_tenant_ids"])
            check_type(argname="argument client_certificate_password", value=client_certificate_password, expected_type=type_hints["client_certificate_password"])
            check_type(argname="argument client_certificate_path", value=client_certificate_path, expected_type=type_hints["client_certificate_path"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument disable_correlation_request_id", value=disable_correlation_request_id, expected_type=type_hints["disable_correlation_request_id"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument metadata_host", value=metadata_host, expected_type=type_hints["metadata_host"])
            check_type(argname="argument msi_endpoint", value=msi_endpoint, expected_type=type_hints["msi_endpoint"])
            check_type(argname="argument skip_provider_registration", value=skip_provider_registration, expected_type=type_hints["skip_provider_registration"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument use_msi", value=use_msi, expected_type=type_hints["use_msi"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "features": features,
        }
        if alias is not None:
            self._values["alias"] = alias
        if arm_endpoint is not None:
            self._values["arm_endpoint"] = arm_endpoint
        if auxiliary_tenant_ids is not None:
            self._values["auxiliary_tenant_ids"] = auxiliary_tenant_ids
        if client_certificate_password is not None:
            self._values["client_certificate_password"] = client_certificate_password
        if client_certificate_path is not None:
            self._values["client_certificate_path"] = client_certificate_path
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if disable_correlation_request_id is not None:
            self._values["disable_correlation_request_id"] = disable_correlation_request_id
        if environment is not None:
            self._values["environment"] = environment
        if metadata_host is not None:
            self._values["metadata_host"] = metadata_host
        if msi_endpoint is not None:
            self._values["msi_endpoint"] = msi_endpoint
        if skip_provider_registration is not None:
            self._values["skip_provider_registration"] = skip_provider_registration
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_msi is not None:
            self._values["use_msi"] = use_msi

    @builtins.property
    def features(self) -> "AzurestackProviderFeatures":
        '''features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        '''
        result = self._values.get("features")
        assert result is not None, "Required property 'features' is missing"
        return typing.cast("AzurestackProviderFeatures", result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arm_endpoint(self) -> typing.Optional[builtins.str]:
        '''The Hostname which should be used for the Azure Metadata Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        '''
        result = self._values.get("arm_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auxiliary_tenant_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.'''
        result = self._values.get("auxiliary_tenant_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        '''The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        '''
        result = self._values.get("client_certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        '''The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        '''
        result = self._values.get("client_certificate_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''The Client ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_correlation_request_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''This will disable the x-ms-correlation-request-id header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        '''
        result = self._values.get("disable_correlation_request_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The Cloud Environment which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_host(self) -> typing.Optional[builtins.str]:
        '''The Hostname which should be used for the Azure Metadata Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        '''
        result = self._values.get("metadata_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        '''
        result = self._values.get("msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_provider_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        '''
        result = self._values.get("skip_provider_registration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''The Subscription ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        '''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''The Tenant ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allowed Managed Service Identity be used for Authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        result = self._values.get("use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "resource_group": "resourceGroup",
        "virtual_machine": "virtualMachine",
        "virtual_machine_scale_set": "virtualMachineScaleSet",
    },
)
class AzurestackProviderFeatures:
    def __init__(
        self,
        *,
        resource_group: typing.Optional[typing.Union["AzurestackProviderFeaturesResourceGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["AzurestackProviderFeaturesVirtualMachine", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_machine_scale_set: typing.Optional[typing.Union["AzurestackProviderFeaturesVirtualMachineScaleSet", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource_group: resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#resource_group AzurestackProvider#resource_group}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine AzurestackProvider#virtual_machine}
        :param virtual_machine_scale_set: virtual_machine_scale_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine_scale_set AzurestackProvider#virtual_machine_scale_set}
        '''
        if isinstance(resource_group, dict):
            resource_group = AzurestackProviderFeaturesResourceGroup(**resource_group)
        if isinstance(virtual_machine, dict):
            virtual_machine = AzurestackProviderFeaturesVirtualMachine(**virtual_machine)
        if isinstance(virtual_machine_scale_set, dict):
            virtual_machine_scale_set = AzurestackProviderFeaturesVirtualMachineScaleSet(**virtual_machine_scale_set)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0356635c9144901f2f9d010b57f779be27c9869f9affce2d4ab0968073ff4440)
            check_type(argname="argument resource_group", value=resource_group, expected_type=type_hints["resource_group"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
            check_type(argname="argument virtual_machine_scale_set", value=virtual_machine_scale_set, expected_type=type_hints["virtual_machine_scale_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resource_group is not None:
            self._values["resource_group"] = resource_group
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine
        if virtual_machine_scale_set is not None:
            self._values["virtual_machine_scale_set"] = virtual_machine_scale_set

    @builtins.property
    def resource_group(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesResourceGroup"]:
        '''resource_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#resource_group AzurestackProvider#resource_group}
        '''
        result = self._values.get("resource_group")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesResourceGroup"], result)

    @builtins.property
    def virtual_machine(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesVirtualMachine"]:
        '''virtual_machine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine AzurestackProvider#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesVirtualMachine"], result)

    @builtins.property
    def virtual_machine_scale_set(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesVirtualMachineScaleSet"]:
        '''virtual_machine_scale_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine_scale_set AzurestackProvider#virtual_machine_scale_set}
        '''
        result = self._values.get("virtual_machine_scale_set")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesVirtualMachineScaleSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesResourceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "prevent_deletion_if_contains_resources": "preventDeletionIfContainsResources",
    },
)
class AzurestackProviderFeaturesResourceGroup:
    def __init__(
        self,
        *,
        prevent_deletion_if_contains_resources: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param prevent_deletion_if_contains_resources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#prevent_deletion_if_contains_resources AzurestackProvider#prevent_deletion_if_contains_resources}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24b9743b5bf0ddac4d61b4c41b7b607738125098a789fc51aca617c425bff91)
            check_type(argname="argument prevent_deletion_if_contains_resources", value=prevent_deletion_if_contains_resources, expected_type=type_hints["prevent_deletion_if_contains_resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if prevent_deletion_if_contains_resources is not None:
            self._values["prevent_deletion_if_contains_resources"] = prevent_deletion_if_contains_resources

    @builtins.property
    def prevent_deletion_if_contains_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#prevent_deletion_if_contains_resources AzurestackProvider#prevent_deletion_if_contains_resources}.'''
        result = self._values.get("prevent_deletion_if_contains_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesResourceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesVirtualMachine",
    jsii_struct_bases=[],
    name_mapping={
        "delete_os_disk_on_deletion": "deleteOsDiskOnDeletion",
        "graceful_shutdown": "gracefulShutdown",
        "skip_shutdown_and_force_delete": "skipShutdownAndForceDelete",
    },
)
class AzurestackProviderFeaturesVirtualMachine:
    def __init__(
        self,
        *,
        delete_os_disk_on_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        graceful_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        skip_shutdown_and_force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param delete_os_disk_on_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#delete_os_disk_on_deletion AzurestackProvider#delete_os_disk_on_deletion}.
        :param graceful_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#graceful_shutdown AzurestackProvider#graceful_shutdown}.
        :param skip_shutdown_and_force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_shutdown_and_force_delete AzurestackProvider#skip_shutdown_and_force_delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197106d0f388929af78df8a7bf2097b4809f77b326c9c1a98e39860fa3861539)
            check_type(argname="argument delete_os_disk_on_deletion", value=delete_os_disk_on_deletion, expected_type=type_hints["delete_os_disk_on_deletion"])
            check_type(argname="argument graceful_shutdown", value=graceful_shutdown, expected_type=type_hints["graceful_shutdown"])
            check_type(argname="argument skip_shutdown_and_force_delete", value=skip_shutdown_and_force_delete, expected_type=type_hints["skip_shutdown_and_force_delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delete_os_disk_on_deletion is not None:
            self._values["delete_os_disk_on_deletion"] = delete_os_disk_on_deletion
        if graceful_shutdown is not None:
            self._values["graceful_shutdown"] = graceful_shutdown
        if skip_shutdown_and_force_delete is not None:
            self._values["skip_shutdown_and_force_delete"] = skip_shutdown_and_force_delete

    @builtins.property
    def delete_os_disk_on_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#delete_os_disk_on_deletion AzurestackProvider#delete_os_disk_on_deletion}.'''
        result = self._values.get("delete_os_disk_on_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def graceful_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#graceful_shutdown AzurestackProvider#graceful_shutdown}.'''
        result = self._values.get("graceful_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def skip_shutdown_and_force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_shutdown_and_force_delete AzurestackProvider#skip_shutdown_and_force_delete}.'''
        result = self._values.get("skip_shutdown_and_force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesVirtualMachine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesVirtualMachineScaleSet",
    jsii_struct_bases=[],
    name_mapping={
        "roll_instances_when_required": "rollInstancesWhenRequired",
        "force_delete": "forceDelete",
        "scale_to_zero_before_deletion": "scaleToZeroBeforeDeletion",
    },
)
class AzurestackProviderFeaturesVirtualMachineScaleSet:
    def __init__(
        self,
        *,
        roll_instances_when_required: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        scale_to_zero_before_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param roll_instances_when_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#roll_instances_when_required AzurestackProvider#roll_instances_when_required}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#force_delete AzurestackProvider#force_delete}.
        :param scale_to_zero_before_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#scale_to_zero_before_deletion AzurestackProvider#scale_to_zero_before_deletion}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242da45b74f1f059b7e59230ab23055606c34334267280496735e40bcf738276)
            check_type(argname="argument roll_instances_when_required", value=roll_instances_when_required, expected_type=type_hints["roll_instances_when_required"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument scale_to_zero_before_deletion", value=scale_to_zero_before_deletion, expected_type=type_hints["scale_to_zero_before_deletion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "roll_instances_when_required": roll_instances_when_required,
        }
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if scale_to_zero_before_deletion is not None:
            self._values["scale_to_zero_before_deletion"] = scale_to_zero_before_deletion

    @builtins.property
    def roll_instances_when_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#roll_instances_when_required AzurestackProvider#roll_instances_when_required}.'''
        result = self._values.get("roll_instances_when_required")
        assert result is not None, "Required property 'roll_instances_when_required' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#force_delete AzurestackProvider#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def scale_to_zero_before_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#scale_to_zero_before_deletion AzurestackProvider#scale_to_zero_before_deletion}.'''
        result = self._values.get("scale_to_zero_before_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesVirtualMachineScaleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzurestackProvider",
    "AzurestackProviderConfig",
    "AzurestackProviderFeatures",
    "AzurestackProviderFeaturesResourceGroup",
    "AzurestackProviderFeaturesVirtualMachine",
    "AzurestackProviderFeaturesVirtualMachineScaleSet",
]

publication.publish()

def _typecheckingstub__428634929d9a0769a631ca657a927c9a82708246fb14d86de901db6853a28a75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    features: typing.Union[AzurestackProviderFeatures, typing.Dict[builtins.str, typing.Any]],
    alias: typing.Optional[builtins.str] = None,
    arm_endpoint: typing.Optional[builtins.str] = None,
    auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_certificate_password: typing.Optional[builtins.str] = None,
    client_certificate_path: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata_host: typing.Optional[builtins.str] = None,
    msi_endpoint: typing.Optional[builtins.str] = None,
    skip_provider_registration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subscription_id: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
    use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff7ab2110a39c26c96860c0a4e31c7862686b528ec67dd561e3fc9e919e0e01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c25cfc2c433bd49b8f503640a6182db1cbed417c7def6a0a9f7e6f6f0c2fd0d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d57d62ab4365ec27bf83fa281b650474e224324aec78481ced056eda909ca4d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a345d4d1d86b3f030e09b056a4e5a66eda70c118e414cfb9cfbd301ac6c7d93(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f57d449cb825937e7e40b41f675a445403f6fe273851da45674deb708bef6b7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff703924232fea474dc45e29724b7ec59432c7eae57784b7d7050137575305e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33eb25126d87b3b1ee8bce5ef3cce334fbf0faddbbfa696a783c31e1194b841(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a50968557b69125bfd557bbe55447bba88521eb2de007716b02b1a2d06ca9a(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575b80a8bf97e804aeeafb024c61c047ded29e9ab0b82ba3bccce65a47b11e1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38aae7f9cae0426b19186497f1123a3f9300628d4054b9b7f3afef96c2e754b7(
    value: typing.Optional[AzurestackProviderFeatures],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b7b3dc3969fed92e0e76637e40b6411f6560e3086252054ba33522c2594ca5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9baa89435048858e83126fed4b13bd782e0fc22a7f4ca7ce1d7676d9a8210fd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ad69bf48dfe565c80c8a4f20787d5885d1f8c30caf569c22f29c3e9d0b2991(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc02226416ebc3681a1ee959d2f1d0a69beb1d017f6234f8e0cebf9bc19dcb4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe0a8ea91691f03c8cac6ea5898cb839fbfcc230c4baeee388ccf19e879f622(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba07eb5e0dab2261d511aab8758e8870beb60dd810ba78d5b041d26cd3089b4(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab56d5e589ceff3c24c196bd8c9a6e099fa45f1fdd70c9d3c743411f36b6af54(
    *,
    features: typing.Union[AzurestackProviderFeatures, typing.Dict[builtins.str, typing.Any]],
    alias: typing.Optional[builtins.str] = None,
    arm_endpoint: typing.Optional[builtins.str] = None,
    auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    client_certificate_password: typing.Optional[builtins.str] = None,
    client_certificate_path: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    environment: typing.Optional[builtins.str] = None,
    metadata_host: typing.Optional[builtins.str] = None,
    msi_endpoint: typing.Optional[builtins.str] = None,
    skip_provider_registration: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subscription_id: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
    use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0356635c9144901f2f9d010b57f779be27c9869f9affce2d4ab0968073ff4440(
    *,
    resource_group: typing.Optional[typing.Union[AzurestackProviderFeaturesResourceGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_machine: typing.Optional[typing.Union[AzurestackProviderFeaturesVirtualMachine, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_machine_scale_set: typing.Optional[typing.Union[AzurestackProviderFeaturesVirtualMachineScaleSet, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24b9743b5bf0ddac4d61b4c41b7b607738125098a789fc51aca617c425bff91(
    *,
    prevent_deletion_if_contains_resources: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197106d0f388929af78df8a7bf2097b4809f77b326c9c1a98e39860fa3861539(
    *,
    delete_os_disk_on_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    graceful_shutdown: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    skip_shutdown_and_force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242da45b74f1f059b7e59230ab23055606c34334267280496735e40bcf738276(
    *,
    roll_instances_when_required: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    scale_to_zero_before_deletion: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
