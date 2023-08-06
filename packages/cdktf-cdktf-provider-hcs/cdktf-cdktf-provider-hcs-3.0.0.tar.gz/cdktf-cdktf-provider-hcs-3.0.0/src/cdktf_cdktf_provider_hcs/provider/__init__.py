'''
# `provider`

Refer to the Terraform Registory for docs: [`hcs`](https://www.terraform.io/docs/providers/hcs).
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


class HcsProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcs.provider.HcsProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcs hcs}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        azure_client_certificate_password: typing.Optional[builtins.str] = None,
        azure_client_certificate_path: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_metadata_host: typing.Optional[builtins.str] = None,
        azure_msi_endpoint: typing.Optional[builtins.str] = None,
        azure_subscription_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hcp_api_domain: typing.Optional[builtins.str] = None,
        hcs_marketplace_product_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcs hcs} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#alias HcsProvider#alias}
        :param azure_client_certificate_password: The password associated with the Azure Client Certificate. For use when authenticating as a Service Principal using a Client Certificate Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_password HcsProvider#azure_client_certificate_password}
        :param azure_client_certificate_path: The path to the Azure Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_path HcsProvider#azure_client_certificate_path}
        :param azure_client_id: The Azure Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_id HcsProvider#azure_client_id}
        :param azure_client_secret: The Azure Client Secret which should be used. For use when authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_secret HcsProvider#azure_client_secret}
        :param azure_environment: The Azure Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_environment HcsProvider#azure_environment}
        :param azure_metadata_host: The hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_metadata_host HcsProvider#azure_metadata_host}
        :param azure_msi_endpoint: The path to a custom endpoint for Azure Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_msi_endpoint HcsProvider#azure_msi_endpoint}
        :param azure_subscription_id: The Azure Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_subscription_id HcsProvider#azure_subscription_id}
        :param azure_tenant_id: The Azure Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_tenant_id HcsProvider#azure_tenant_id}
        :param azure_use_msi: Allowed Azure Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_use_msi HcsProvider#azure_use_msi}
        :param hcp_api_domain: The HashiCorp Cloud Platform API domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcp_api_domain HcsProvider#hcp_api_domain}
        :param hcs_marketplace_product_name: The HashiCorp Consul Service product name on the Azure marketplace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcs_marketplace_product_name HcsProvider#hcs_marketplace_product_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf226bfabee3c16ab384996076993793ecb202c153fcffb3dbb2b88e20d01797)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = HcsProviderConfig(
            alias=alias,
            azure_client_certificate_password=azure_client_certificate_password,
            azure_client_certificate_path=azure_client_certificate_path,
            azure_client_id=azure_client_id,
            azure_client_secret=azure_client_secret,
            azure_environment=azure_environment,
            azure_metadata_host=azure_metadata_host,
            azure_msi_endpoint=azure_msi_endpoint,
            azure_subscription_id=azure_subscription_id,
            azure_tenant_id=azure_tenant_id,
            azure_use_msi=azure_use_msi,
            hcp_api_domain=hcp_api_domain,
            hcs_marketplace_product_name=hcs_marketplace_product_name,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAzureClientCertificatePassword")
    def reset_azure_client_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientCertificatePassword", []))

    @jsii.member(jsii_name="resetAzureClientCertificatePath")
    def reset_azure_client_certificate_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientCertificatePath", []))

    @jsii.member(jsii_name="resetAzureClientId")
    def reset_azure_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientId", []))

    @jsii.member(jsii_name="resetAzureClientSecret")
    def reset_azure_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientSecret", []))

    @jsii.member(jsii_name="resetAzureEnvironment")
    def reset_azure_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureEnvironment", []))

    @jsii.member(jsii_name="resetAzureMetadataHost")
    def reset_azure_metadata_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureMetadataHost", []))

    @jsii.member(jsii_name="resetAzureMsiEndpoint")
    def reset_azure_msi_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureMsiEndpoint", []))

    @jsii.member(jsii_name="resetAzureSubscriptionId")
    def reset_azure_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureSubscriptionId", []))

    @jsii.member(jsii_name="resetAzureTenantId")
    def reset_azure_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureTenantId", []))

    @jsii.member(jsii_name="resetAzureUseMsi")
    def reset_azure_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureUseMsi", []))

    @jsii.member(jsii_name="resetHcpApiDomain")
    def reset_hcp_api_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHcpApiDomain", []))

    @jsii.member(jsii_name="resetHcsMarketplaceProductName")
    def reset_hcs_marketplace_product_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHcsMarketplaceProductName", []))

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
    @jsii.member(jsii_name="azureClientCertificatePasswordInput")
    def azure_client_certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientCertificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientCertificatePathInput")
    def azure_client_certificate_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientCertificatePathInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientIdInput")
    def azure_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientSecretInput")
    def azure_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="azureEnvironmentInput")
    def azure_environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="azureMetadataHostInput")
    def azure_metadata_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureMetadataHostInput"))

    @builtins.property
    @jsii.member(jsii_name="azureMsiEndpointInput")
    def azure_msi_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureMsiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="azureSubscriptionIdInput")
    def azure_subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureSubscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureTenantIdInput")
    def azure_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureUseMsiInput")
    def azure_use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "azureUseMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="hcpApiDomainInput")
    def hcp_api_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hcpApiDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="hcsMarketplaceProductNameInput")
    def hcs_marketplace_product_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hcsMarketplaceProductNameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4caadf331386bd23a6fbdfaaf38dcc3eac1e9cc39eac4c6af103f3fa12cfd327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientCertificatePassword")
    def azure_client_certificate_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientCertificatePassword"))

    @azure_client_certificate_password.setter
    def azure_client_certificate_password(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f680b7034d14c640d0d0a2eec99654160762339f9ad98efb1be6e82f94d270e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientCertificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientCertificatePath")
    def azure_client_certificate_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientCertificatePath"))

    @azure_client_certificate_path.setter
    def azure_client_certificate_path(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a4f238334084823c98ba9805f2fc1752fea703ae1793a120e5d547905edb79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientCertificatePath", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientId")
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientId"))

    @azure_client_id.setter
    def azure_client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c22ab2a48634dd8bd6856b0f38a62f8bae4ea110662840cf1a9c709131cc464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientId", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientSecret")
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecret"))

    @azure_client_secret.setter
    def azure_client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a6c532e36e3f0b8a7546e06be67597a0e80cfcea9b87fdcd8142a7bc4eede9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="azureEnvironment")
    def azure_environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironment"))

    @azure_environment.setter
    def azure_environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97645169a30bdb30b8eef24b887d00e5f397c01a6c7ca6f4720b15218a20e709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="azureMetadataHost")
    def azure_metadata_host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureMetadataHost"))

    @azure_metadata_host.setter
    def azure_metadata_host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a50fefc5b86874809cf7237995e75be29c99f7fb88517f2bdf06dbb51cfdb253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureMetadataHost", value)

    @builtins.property
    @jsii.member(jsii_name="azureMsiEndpoint")
    def azure_msi_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureMsiEndpoint"))

    @azure_msi_endpoint.setter
    def azure_msi_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690538f0e939224112da5e78dd2b223231786d6d495f9ed38975aaada71ad88b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureMsiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="azureSubscriptionId")
    def azure_subscription_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureSubscriptionId"))

    @azure_subscription_id.setter
    def azure_subscription_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081b4cd0ca269cd7eb411587eb047ddd7d4708cd3b6108692430d0926018897d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureSubscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="azureTenantId")
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantId"))

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b01329888ff6d94641005c36af3a25e5b3c6e2794b558f618b6e25bd3179227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="azureUseMsi")
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "azureUseMsi"))

    @azure_use_msi.setter
    def azure_use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d62d4a97fde7be10cf1b3141cceda83d3edb1cfdbdd35c4a14bcd5b35952c861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureUseMsi", value)

    @builtins.property
    @jsii.member(jsii_name="hcpApiDomain")
    def hcp_api_domain(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hcpApiDomain"))

    @hcp_api_domain.setter
    def hcp_api_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7110c941022d2b259b8d45c4877ed380b5105eb12d0d41d69d641b0a70fdf226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hcpApiDomain", value)

    @builtins.property
    @jsii.member(jsii_name="hcsMarketplaceProductName")
    def hcs_marketplace_product_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hcsMarketplaceProductName"))

    @hcs_marketplace_product_name.setter
    def hcs_marketplace_product_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9910b478ba945f62eecce1ca8db121b36e34b10586e9c45fe67bf6d37c2a8c81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hcsMarketplaceProductName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcs.provider.HcsProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "azure_client_certificate_password": "azureClientCertificatePassword",
        "azure_client_certificate_path": "azureClientCertificatePath",
        "azure_client_id": "azureClientId",
        "azure_client_secret": "azureClientSecret",
        "azure_environment": "azureEnvironment",
        "azure_metadata_host": "azureMetadataHost",
        "azure_msi_endpoint": "azureMsiEndpoint",
        "azure_subscription_id": "azureSubscriptionId",
        "azure_tenant_id": "azureTenantId",
        "azure_use_msi": "azureUseMsi",
        "hcp_api_domain": "hcpApiDomain",
        "hcs_marketplace_product_name": "hcsMarketplaceProductName",
    },
)
class HcsProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        azure_client_certificate_password: typing.Optional[builtins.str] = None,
        azure_client_certificate_path: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_metadata_host: typing.Optional[builtins.str] = None,
        azure_msi_endpoint: typing.Optional[builtins.str] = None,
        azure_subscription_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hcp_api_domain: typing.Optional[builtins.str] = None,
        hcs_marketplace_product_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#alias HcsProvider#alias}
        :param azure_client_certificate_password: The password associated with the Azure Client Certificate. For use when authenticating as a Service Principal using a Client Certificate Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_password HcsProvider#azure_client_certificate_password}
        :param azure_client_certificate_path: The path to the Azure Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_path HcsProvider#azure_client_certificate_path}
        :param azure_client_id: The Azure Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_id HcsProvider#azure_client_id}
        :param azure_client_secret: The Azure Client Secret which should be used. For use when authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_secret HcsProvider#azure_client_secret}
        :param azure_environment: The Azure Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_environment HcsProvider#azure_environment}
        :param azure_metadata_host: The hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_metadata_host HcsProvider#azure_metadata_host}
        :param azure_msi_endpoint: The path to a custom endpoint for Azure Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_msi_endpoint HcsProvider#azure_msi_endpoint}
        :param azure_subscription_id: The Azure Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_subscription_id HcsProvider#azure_subscription_id}
        :param azure_tenant_id: The Azure Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_tenant_id HcsProvider#azure_tenant_id}
        :param azure_use_msi: Allowed Azure Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_use_msi HcsProvider#azure_use_msi}
        :param hcp_api_domain: The HashiCorp Cloud Platform API domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcp_api_domain HcsProvider#hcp_api_domain}
        :param hcs_marketplace_product_name: The HashiCorp Consul Service product name on the Azure marketplace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcs_marketplace_product_name HcsProvider#hcs_marketplace_product_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7daeec413a1ea1a80d648e9f8385f97d600dc757cdde224854ecb1d60f466935)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument azure_client_certificate_password", value=azure_client_certificate_password, expected_type=type_hints["azure_client_certificate_password"])
            check_type(argname="argument azure_client_certificate_path", value=azure_client_certificate_path, expected_type=type_hints["azure_client_certificate_path"])
            check_type(argname="argument azure_client_id", value=azure_client_id, expected_type=type_hints["azure_client_id"])
            check_type(argname="argument azure_client_secret", value=azure_client_secret, expected_type=type_hints["azure_client_secret"])
            check_type(argname="argument azure_environment", value=azure_environment, expected_type=type_hints["azure_environment"])
            check_type(argname="argument azure_metadata_host", value=azure_metadata_host, expected_type=type_hints["azure_metadata_host"])
            check_type(argname="argument azure_msi_endpoint", value=azure_msi_endpoint, expected_type=type_hints["azure_msi_endpoint"])
            check_type(argname="argument azure_subscription_id", value=azure_subscription_id, expected_type=type_hints["azure_subscription_id"])
            check_type(argname="argument azure_tenant_id", value=azure_tenant_id, expected_type=type_hints["azure_tenant_id"])
            check_type(argname="argument azure_use_msi", value=azure_use_msi, expected_type=type_hints["azure_use_msi"])
            check_type(argname="argument hcp_api_domain", value=hcp_api_domain, expected_type=type_hints["hcp_api_domain"])
            check_type(argname="argument hcs_marketplace_product_name", value=hcs_marketplace_product_name, expected_type=type_hints["hcs_marketplace_product_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if azure_client_certificate_password is not None:
            self._values["azure_client_certificate_password"] = azure_client_certificate_password
        if azure_client_certificate_path is not None:
            self._values["azure_client_certificate_path"] = azure_client_certificate_path
        if azure_client_id is not None:
            self._values["azure_client_id"] = azure_client_id
        if azure_client_secret is not None:
            self._values["azure_client_secret"] = azure_client_secret
        if azure_environment is not None:
            self._values["azure_environment"] = azure_environment
        if azure_metadata_host is not None:
            self._values["azure_metadata_host"] = azure_metadata_host
        if azure_msi_endpoint is not None:
            self._values["azure_msi_endpoint"] = azure_msi_endpoint
        if azure_subscription_id is not None:
            self._values["azure_subscription_id"] = azure_subscription_id
        if azure_tenant_id is not None:
            self._values["azure_tenant_id"] = azure_tenant_id
        if azure_use_msi is not None:
            self._values["azure_use_msi"] = azure_use_msi
        if hcp_api_domain is not None:
            self._values["hcp_api_domain"] = hcp_api_domain
        if hcs_marketplace_product_name is not None:
            self._values["hcs_marketplace_product_name"] = hcs_marketplace_product_name

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#alias HcsProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_certificate_password(self) -> typing.Optional[builtins.str]:
        '''The password associated with the Azure Client Certificate.

        For use when authenticating as a Service Principal using a Client Certificate

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_password HcsProvider#azure_client_certificate_password}
        '''
        result = self._values.get("azure_client_certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_certificate_path(self) -> typing.Optional[builtins.str]:
        '''The path to the Azure Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_certificate_path HcsProvider#azure_client_certificate_path}
        '''
        result = self._values.get("azure_client_certificate_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        '''The Azure Client ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_id HcsProvider#azure_client_id}
        '''
        result = self._values.get("azure_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        '''The Azure Client Secret which should be used.

        For use when authenticating as a Service Principal using a Client Secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_client_secret HcsProvider#azure_client_secret}
        '''
        result = self._values.get("azure_client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_environment(self) -> typing.Optional[builtins.str]:
        '''The Azure Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_environment HcsProvider#azure_environment}
        '''
        result = self._values.get("azure_environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_metadata_host(self) -> typing.Optional[builtins.str]:
        '''The hostname which should be used for the Azure Metadata Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_metadata_host HcsProvider#azure_metadata_host}
        '''
        result = self._values.get("azure_metadata_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''The path to a custom endpoint for Azure Managed Service Identity - in most circumstances this should be detected automatically.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_msi_endpoint HcsProvider#azure_msi_endpoint}
        '''
        result = self._values.get("azure_msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_subscription_id(self) -> typing.Optional[builtins.str]:
        '''The Azure Subscription ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_subscription_id HcsProvider#azure_subscription_id}
        '''
        result = self._values.get("azure_subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        '''The Azure Tenant ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_tenant_id HcsProvider#azure_tenant_id}
        '''
        result = self._values.get("azure_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allowed Azure Managed Service Identity be used for Authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#azure_use_msi HcsProvider#azure_use_msi}
        '''
        result = self._values.get("azure_use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hcp_api_domain(self) -> typing.Optional[builtins.str]:
        '''The HashiCorp Cloud Platform API domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcp_api_domain HcsProvider#hcp_api_domain}
        '''
        result = self._values.get("hcp_api_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hcs_marketplace_product_name(self) -> typing.Optional[builtins.str]:
        '''The HashiCorp Consul Service product name on the Azure marketplace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs#hcs_marketplace_product_name HcsProvider#hcs_marketplace_product_name}
        '''
        result = self._values.get("hcs_marketplace_product_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HcsProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HcsProvider",
    "HcsProviderConfig",
]

publication.publish()

def _typecheckingstub__cf226bfabee3c16ab384996076993793ecb202c153fcffb3dbb2b88e20d01797(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    azure_client_certificate_password: typing.Optional[builtins.str] = None,
    azure_client_certificate_path: typing.Optional[builtins.str] = None,
    azure_client_id: typing.Optional[builtins.str] = None,
    azure_client_secret: typing.Optional[builtins.str] = None,
    azure_environment: typing.Optional[builtins.str] = None,
    azure_metadata_host: typing.Optional[builtins.str] = None,
    azure_msi_endpoint: typing.Optional[builtins.str] = None,
    azure_subscription_id: typing.Optional[builtins.str] = None,
    azure_tenant_id: typing.Optional[builtins.str] = None,
    azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hcp_api_domain: typing.Optional[builtins.str] = None,
    hcs_marketplace_product_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4caadf331386bd23a6fbdfaaf38dcc3eac1e9cc39eac4c6af103f3fa12cfd327(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f680b7034d14c640d0d0a2eec99654160762339f9ad98efb1be6e82f94d270e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a4f238334084823c98ba9805f2fc1752fea703ae1793a120e5d547905edb79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c22ab2a48634dd8bd6856b0f38a62f8bae4ea110662840cf1a9c709131cc464(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a6c532e36e3f0b8a7546e06be67597a0e80cfcea9b87fdcd8142a7bc4eede9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97645169a30bdb30b8eef24b887d00e5f397c01a6c7ca6f4720b15218a20e709(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50fefc5b86874809cf7237995e75be29c99f7fb88517f2bdf06dbb51cfdb253(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690538f0e939224112da5e78dd2b223231786d6d495f9ed38975aaada71ad88b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081b4cd0ca269cd7eb411587eb047ddd7d4708cd3b6108692430d0926018897d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b01329888ff6d94641005c36af3a25e5b3c6e2794b558f618b6e25bd3179227(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d62d4a97fde7be10cf1b3141cceda83d3edb1cfdbdd35c4a14bcd5b35952c861(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7110c941022d2b259b8d45c4877ed380b5105eb12d0d41d69d641b0a70fdf226(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9910b478ba945f62eecce1ca8db121b36e34b10586e9c45fe67bf6d37c2a8c81(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7daeec413a1ea1a80d648e9f8385f97d600dc757cdde224854ecb1d60f466935(
    *,
    alias: typing.Optional[builtins.str] = None,
    azure_client_certificate_password: typing.Optional[builtins.str] = None,
    azure_client_certificate_path: typing.Optional[builtins.str] = None,
    azure_client_id: typing.Optional[builtins.str] = None,
    azure_client_secret: typing.Optional[builtins.str] = None,
    azure_environment: typing.Optional[builtins.str] = None,
    azure_metadata_host: typing.Optional[builtins.str] = None,
    azure_msi_endpoint: typing.Optional[builtins.str] = None,
    azure_subscription_id: typing.Optional[builtins.str] = None,
    azure_tenant_id: typing.Optional[builtins.str] = None,
    azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hcp_api_domain: typing.Optional[builtins.str] = None,
    hcs_marketplace_product_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
