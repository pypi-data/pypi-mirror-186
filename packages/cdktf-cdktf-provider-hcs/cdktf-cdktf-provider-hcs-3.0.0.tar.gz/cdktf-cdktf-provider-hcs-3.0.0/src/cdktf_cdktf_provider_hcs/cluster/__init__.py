'''
# `hcs_cluster`

Refer to the Terraform Registory for docs: [`hcs_cluster`](https://www.terraform.io/docs/providers/hcs/r/cluster).
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


class Cluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcs.cluster.Cluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcs/r/cluster hcs_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_mode: builtins.str,
        email: builtins.str,
        managed_application_name: builtins.str,
        resource_group_name: builtins.str,
        audit_logging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        audit_log_storage_container_url: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        consul_datacenter: typing.Optional[builtins.str] = None,
        consul_external_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        consul_federation_token: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        min_consul_version: typing.Optional[builtins.str] = None,
        plan_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vnet_cidr: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcs/r/cluster hcs_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_mode: The mode of the cluster ('Development' or 'Production'). Development clusters only have a single Consul server. Production clusters are fully supported, full featured, and deploy with a minimum of three hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_mode Cluster#cluster_mode}
        :param email: The contact email for the primary owner of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#email Cluster#email}
        :param managed_application_name: The name of the HCS Azure Managed Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_application_name Cluster#managed_application_name}
        :param resource_group_name: The name of the Resource Group in which the HCS Azure Managed Application belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#resource_group_name Cluster#resource_group_name}
        :param audit_logging_enabled: Enables Consul audit logging for the cluster resource. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_logging_enabled Cluster#audit_logging_enabled}
        :param audit_log_storage_container_url: The url of the Azure blob storage container to write audit logs to if ``audit_logging_enabled`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_log_storage_container_url Cluster#audit_log_storage_container_url}
        :param cluster_name: The name of the cluster Managed Resource. If not specified, it is defaulted to the value of ``managed_application_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_name Cluster#cluster_name}
        :param consul_datacenter: The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``managed_application_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_datacenter Cluster#consul_datacenter}
        :param consul_external_endpoint: Denotes that the cluster has an external endpoint for the Consul UI. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_external_endpoint Cluster#consul_external_endpoint}
        :param consul_federation_token: The token used to join a federation of Consul clusters. If the cluster is not part of a federation, this field will be empty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_federation_token Cluster#consul_federation_token}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The Azure region that the cluster is deployed to. If not specified, it is defaulted to the region of the Resource Group the Managed Application belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#location Cluster#location}
        :param managed_resource_group_name: The name of the Managed Resource Group in which the cluster resources belong. If not specified, it is defaulted to the value of ``managed_application_name`` with 'mrg-' prepended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_resource_group_name Cluster#managed_resource_group_name}
        :param min_consul_version: The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#min_consul_version Cluster#min_consul_version}
        :param plan_name: The name of the Azure Marketplace HCS plan for the cluster. If not specified, it will default to the current HCS default plan (see the ``hcs_plan_defaults`` data source). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#plan_name Cluster#plan_name}
        :param tags: A mapping of tags to assign to the HCS Azure Managed Application resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#tags Cluster#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#timeouts Cluster#timeouts}
        :param vnet_cidr: The VNET CIDR range of the Consul cluster. Defaults to ``172.25.16.0/24``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#vnet_cidr Cluster#vnet_cidr}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bd78262670745cabdabe4c3d61502937a233a4f0d53dac1548a82c14fe462b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ClusterConfig(
            cluster_mode=cluster_mode,
            email=email,
            managed_application_name=managed_application_name,
            resource_group_name=resource_group_name,
            audit_logging_enabled=audit_logging_enabled,
            audit_log_storage_container_url=audit_log_storage_container_url,
            cluster_name=cluster_name,
            consul_datacenter=consul_datacenter,
            consul_external_endpoint=consul_external_endpoint,
            consul_federation_token=consul_federation_token,
            id=id,
            location=location,
            managed_resource_group_name=managed_resource_group_name,
            min_consul_version=min_consul_version,
            plan_name=plan_name,
            tags=tags,
            timeouts=timeouts,
            vnet_cidr=vnet_cidr,
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
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#create Cluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#default Cluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#update Cluster#update}.
        '''
        value = ClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuditLoggingEnabled")
    def reset_audit_logging_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLoggingEnabled", []))

    @jsii.member(jsii_name="resetAuditLogStorageContainerUrl")
    def reset_audit_log_storage_container_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogStorageContainerUrl", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetConsulDatacenter")
    def reset_consul_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulDatacenter", []))

    @jsii.member(jsii_name="resetConsulExternalEndpoint")
    def reset_consul_external_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulExternalEndpoint", []))

    @jsii.member(jsii_name="resetConsulFederationToken")
    def reset_consul_federation_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulFederationToken", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetManagedResourceGroupName")
    def reset_managed_resource_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedResourceGroupName", []))

    @jsii.member(jsii_name="resetMinConsulVersion")
    def reset_min_consul_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinConsulVersion", []))

    @jsii.member(jsii_name="resetPlanName")
    def reset_plan_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlanName", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVnetCidr")
    def reset_vnet_cidr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnetCidr", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="blobContainerName")
    def blob_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobContainerName"))

    @builtins.property
    @jsii.member(jsii_name="consulAutomaticUpgrades")
    def consul_automatic_upgrades(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "consulAutomaticUpgrades"))

    @builtins.property
    @jsii.member(jsii_name="consulCaFile")
    def consul_ca_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulCaFile"))

    @builtins.property
    @jsii.member(jsii_name="consulClusterId")
    def consul_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulClusterId"))

    @builtins.property
    @jsii.member(jsii_name="consulConfigFile")
    def consul_config_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulConfigFile"))

    @builtins.property
    @jsii.member(jsii_name="consulConnect")
    def consul_connect(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "consulConnect"))

    @builtins.property
    @jsii.member(jsii_name="consulExternalEndpointUrl")
    def consul_external_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulExternalEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="consulPrivateEndpointUrl")
    def consul_private_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulPrivateEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="consulRootTokenAccessorId")
    def consul_root_token_accessor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulRootTokenAccessorId"))

    @builtins.property
    @jsii.member(jsii_name="consulRootTokenSecretId")
    def consul_root_token_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulRootTokenSecretId"))

    @builtins.property
    @jsii.member(jsii_name="consulSnapshotInterval")
    def consul_snapshot_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulSnapshotInterval"))

    @builtins.property
    @jsii.member(jsii_name="consulSnapshotRetention")
    def consul_snapshot_retention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulSnapshotRetention"))

    @builtins.property
    @jsii.member(jsii_name="consulVersion")
    def consul_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulVersion"))

    @builtins.property
    @jsii.member(jsii_name="managedApplicationId")
    def managed_application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="managedIdentityName")
    def managed_identity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedIdentityName"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountResourceGroup")
    def storage_account_resource_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountResourceGroup"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ClusterTimeoutsOutputReference":
        return typing.cast("ClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vnetId")
    def vnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetId"))

    @builtins.property
    @jsii.member(jsii_name="vnetName")
    def vnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetName"))

    @builtins.property
    @jsii.member(jsii_name="vnetResourceGroupName")
    def vnet_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetResourceGroupName"))

    @builtins.property
    @jsii.member(jsii_name="auditLoggingEnabledInput")
    def audit_logging_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "auditLoggingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLogStorageContainerUrlInput")
    def audit_log_storage_container_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditLogStorageContainerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterModeInput")
    def cluster_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterModeInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="consulDatacenterInput")
    def consul_datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulDatacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="consulExternalEndpointInput")
    def consul_external_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "consulExternalEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="consulFederationTokenInput")
    def consul_federation_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulFederationTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedApplicationNameInput")
    def managed_application_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedApplicationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupNameInput")
    def managed_resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedResourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minConsulVersionInput")
    def min_consul_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minConsulVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="planNameInput")
    def plan_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ClusterTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ClusterTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vnetCidrInput")
    def vnet_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnetCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="auditLoggingEnabled")
    def audit_logging_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "auditLoggingEnabled"))

    @audit_logging_enabled.setter
    def audit_logging_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61f2b971afc5d497e52bff0eb4798fc71f0ebf67048e7f2c7a06df9258bdbc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLoggingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="auditLogStorageContainerUrl")
    def audit_log_storage_container_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auditLogStorageContainerUrl"))

    @audit_log_storage_container_url.setter
    def audit_log_storage_container_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8864c904b7eee6e84f35129f396efde2521f94b718ca4ce463e016291a0fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditLogStorageContainerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="clusterMode")
    def cluster_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterMode"))

    @cluster_mode.setter
    def cluster_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be4aeb44371e737efd4f88f247804fec869deda8630c3334ff22a44c8cd9d46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterMode", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ab7ac84e3d9438f7ef55edf36950057e16ea6678a3fc7a32fb26b3a19378beb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="consulDatacenter")
    def consul_datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulDatacenter"))

    @consul_datacenter.setter
    def consul_datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6843bfdc8071d86dff0a1ce6422ddaadb09600e33ce91cf293d84088de6d4dc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulDatacenter", value)

    @builtins.property
    @jsii.member(jsii_name="consulExternalEndpoint")
    def consul_external_endpoint(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "consulExternalEndpoint"))

    @consul_external_endpoint.setter
    def consul_external_endpoint(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2538c4b4664b932d16b5cc092f0d12c8fe2f6f08ec98b0127c39aba112c23b63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulExternalEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="consulFederationToken")
    def consul_federation_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulFederationToken"))

    @consul_federation_token.setter
    def consul_federation_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2018d6bcfe2373a48023d4d0b7ba1ad38834318f4f9a79f666775a9d84a2af40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulFederationToken", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cadb6051f972ad78f339d41a2f0e838913848f22b1936eb9bae49ed69d3bd82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5369a943f27b627eccb397ac7caaabd577ab7b3a3144a431c205971ca10e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c0be4ab051cf42c2bac165b8969bf8cd79e2736ea1ba4dbd591cb340c47eeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedApplicationName")
    def managed_application_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedApplicationName"))

    @managed_application_name.setter
    def managed_application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87eeee610b162cd69ae315803f13107e4c024a0c2b7721e89e6d02f631003199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedApplicationName", value)

    @builtins.property
    @jsii.member(jsii_name="managedResourceGroupName")
    def managed_resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedResourceGroupName"))

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d20791bda4c732b938f819a3974a1f3186846df826ae4e367f8d5c3c50731a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedResourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="minConsulVersion")
    def min_consul_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minConsulVersion"))

    @min_consul_version.setter
    def min_consul_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7543e2af621965465cbbebfb1a14c05dc564a5c2772a82b72c2553a87f06a89f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minConsulVersion", value)

    @builtins.property
    @jsii.member(jsii_name="planName")
    def plan_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "planName"))

    @plan_name.setter
    def plan_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ad7c476e94ca495354ec692087d932131711f26606455d7e7fac9da6f34c82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de0731309a7641ed1d20399d54005f56aa8a67059797c895fdddeba159edc3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__829d4478f7b614cb5275f18b5f671b1d77d8ad9af51669f4a28fb47c4bc1649e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vnetCidr")
    def vnet_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnetCidr"))

    @vnet_cidr.setter
    def vnet_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc6a57b432c7f3325751b353d2ee7b7e97834f35c2515a5afa96c23f0f67af2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnetCidr", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcs.cluster.ClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_mode": "clusterMode",
        "email": "email",
        "managed_application_name": "managedApplicationName",
        "resource_group_name": "resourceGroupName",
        "audit_logging_enabled": "auditLoggingEnabled",
        "audit_log_storage_container_url": "auditLogStorageContainerUrl",
        "cluster_name": "clusterName",
        "consul_datacenter": "consulDatacenter",
        "consul_external_endpoint": "consulExternalEndpoint",
        "consul_federation_token": "consulFederationToken",
        "id": "id",
        "location": "location",
        "managed_resource_group_name": "managedResourceGroupName",
        "min_consul_version": "minConsulVersion",
        "plan_name": "planName",
        "tags": "tags",
        "timeouts": "timeouts",
        "vnet_cidr": "vnetCidr",
    },
)
class ClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_mode: builtins.str,
        email: builtins.str,
        managed_application_name: builtins.str,
        resource_group_name: builtins.str,
        audit_logging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        audit_log_storage_container_url: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        consul_datacenter: typing.Optional[builtins.str] = None,
        consul_external_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        consul_federation_token: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        managed_resource_group_name: typing.Optional[builtins.str] = None,
        min_consul_version: typing.Optional[builtins.str] = None,
        plan_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vnet_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_mode: The mode of the cluster ('Development' or 'Production'). Development clusters only have a single Consul server. Production clusters are fully supported, full featured, and deploy with a minimum of three hosts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_mode Cluster#cluster_mode}
        :param email: The contact email for the primary owner of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#email Cluster#email}
        :param managed_application_name: The name of the HCS Azure Managed Application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_application_name Cluster#managed_application_name}
        :param resource_group_name: The name of the Resource Group in which the HCS Azure Managed Application belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#resource_group_name Cluster#resource_group_name}
        :param audit_logging_enabled: Enables Consul audit logging for the cluster resource. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_logging_enabled Cluster#audit_logging_enabled}
        :param audit_log_storage_container_url: The url of the Azure blob storage container to write audit logs to if ``audit_logging_enabled`` is ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_log_storage_container_url Cluster#audit_log_storage_container_url}
        :param cluster_name: The name of the cluster Managed Resource. If not specified, it is defaulted to the value of ``managed_application_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_name Cluster#cluster_name}
        :param consul_datacenter: The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``managed_application_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_datacenter Cluster#consul_datacenter}
        :param consul_external_endpoint: Denotes that the cluster has an external endpoint for the Consul UI. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_external_endpoint Cluster#consul_external_endpoint}
        :param consul_federation_token: The token used to join a federation of Consul clusters. If the cluster is not part of a federation, this field will be empty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_federation_token Cluster#consul_federation_token}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The Azure region that the cluster is deployed to. If not specified, it is defaulted to the region of the Resource Group the Managed Application belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#location Cluster#location}
        :param managed_resource_group_name: The name of the Managed Resource Group in which the cluster resources belong. If not specified, it is defaulted to the value of ``managed_application_name`` with 'mrg-' prepended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_resource_group_name Cluster#managed_resource_group_name}
        :param min_consul_version: The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently recommended by HCS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#min_consul_version Cluster#min_consul_version}
        :param plan_name: The name of the Azure Marketplace HCS plan for the cluster. If not specified, it will default to the current HCS default plan (see the ``hcs_plan_defaults`` data source). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#plan_name Cluster#plan_name}
        :param tags: A mapping of tags to assign to the HCS Azure Managed Application resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#tags Cluster#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#timeouts Cluster#timeouts}
        :param vnet_cidr: The VNET CIDR range of the Consul cluster. Defaults to ``172.25.16.0/24``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#vnet_cidr Cluster#vnet_cidr}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c63368dfdd2ff38e35ab9bb268933364f25c1ab1479d0d08849b566e1aba6d57)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_mode", value=cluster_mode, expected_type=type_hints["cluster_mode"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument managed_application_name", value=managed_application_name, expected_type=type_hints["managed_application_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument audit_logging_enabled", value=audit_logging_enabled, expected_type=type_hints["audit_logging_enabled"])
            check_type(argname="argument audit_log_storage_container_url", value=audit_log_storage_container_url, expected_type=type_hints["audit_log_storage_container_url"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument consul_datacenter", value=consul_datacenter, expected_type=type_hints["consul_datacenter"])
            check_type(argname="argument consul_external_endpoint", value=consul_external_endpoint, expected_type=type_hints["consul_external_endpoint"])
            check_type(argname="argument consul_federation_token", value=consul_federation_token, expected_type=type_hints["consul_federation_token"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument managed_resource_group_name", value=managed_resource_group_name, expected_type=type_hints["managed_resource_group_name"])
            check_type(argname="argument min_consul_version", value=min_consul_version, expected_type=type_hints["min_consul_version"])
            check_type(argname="argument plan_name", value=plan_name, expected_type=type_hints["plan_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vnet_cidr", value=vnet_cidr, expected_type=type_hints["vnet_cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_mode": cluster_mode,
            "email": email,
            "managed_application_name": managed_application_name,
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
        if audit_logging_enabled is not None:
            self._values["audit_logging_enabled"] = audit_logging_enabled
        if audit_log_storage_container_url is not None:
            self._values["audit_log_storage_container_url"] = audit_log_storage_container_url
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if consul_datacenter is not None:
            self._values["consul_datacenter"] = consul_datacenter
        if consul_external_endpoint is not None:
            self._values["consul_external_endpoint"] = consul_external_endpoint
        if consul_federation_token is not None:
            self._values["consul_federation_token"] = consul_federation_token
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if managed_resource_group_name is not None:
            self._values["managed_resource_group_name"] = managed_resource_group_name
        if min_consul_version is not None:
            self._values["min_consul_version"] = min_consul_version
        if plan_name is not None:
            self._values["plan_name"] = plan_name
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vnet_cidr is not None:
            self._values["vnet_cidr"] = vnet_cidr

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
    def cluster_mode(self) -> builtins.str:
        '''The mode of the cluster ('Development' or 'Production').

        Development clusters only have a single Consul server. Production clusters are fully supported, full featured, and deploy with a minimum of three hosts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_mode Cluster#cluster_mode}
        '''
        result = self._values.get("cluster_mode")
        assert result is not None, "Required property 'cluster_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The contact email for the primary owner of the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#email Cluster#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_application_name(self) -> builtins.str:
        '''The name of the HCS Azure Managed Application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_application_name Cluster#managed_application_name}
        '''
        result = self._values.get("managed_application_name")
        assert result is not None, "Required property 'managed_application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''The name of the Resource Group in which the HCS Azure Managed Application belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#resource_group_name Cluster#resource_group_name}
        '''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_logging_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enables Consul audit logging for the cluster resource. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_logging_enabled Cluster#audit_logging_enabled}
        '''
        result = self._values.get("audit_logging_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def audit_log_storage_container_url(self) -> typing.Optional[builtins.str]:
        '''The url of the Azure blob storage container to write audit logs to if ``audit_logging_enabled`` is ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#audit_log_storage_container_url Cluster#audit_log_storage_container_url}
        '''
        result = self._values.get("audit_log_storage_container_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster Managed Resource. If not specified, it is defaulted to the value of ``managed_application_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#cluster_name Cluster#cluster_name}
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consul_datacenter(self) -> typing.Optional[builtins.str]:
        '''The Consul data center name of the cluster. If not specified, it is defaulted to the value of ``managed_application_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_datacenter Cluster#consul_datacenter}
        '''
        result = self._values.get("consul_datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consul_external_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Denotes that the cluster has an external endpoint for the Consul UI. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_external_endpoint Cluster#consul_external_endpoint}
        '''
        result = self._values.get("consul_external_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def consul_federation_token(self) -> typing.Optional[builtins.str]:
        '''The token used to join a federation of Consul clusters.

        If the cluster is not part of a federation, this field will be empty.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#consul_federation_token Cluster#consul_federation_token}
        '''
        result = self._values.get("consul_federation_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#id Cluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The Azure region that the cluster is deployed to.

        If not specified, it is defaulted to the region of the Resource Group the Managed Application belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#location Cluster#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_resource_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Managed Resource Group in which the cluster resources belong.

        If not specified, it is defaulted to the value of ``managed_application_name`` with 'mrg-' prepended.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#managed_resource_group_name Cluster#managed_resource_group_name}
        '''
        result = self._values.get("managed_resource_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_consul_version(self) -> typing.Optional[builtins.str]:
        '''The minimum Consul version of the cluster.

        If not specified, it is defaulted to the version that is currently recommended by HCS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#min_consul_version Cluster#min_consul_version}
        '''
        result = self._values.get("min_consul_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Azure Marketplace HCS plan for the cluster.

        If not specified, it will default to the current HCS default plan (see the ``hcs_plan_defaults`` data source).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#plan_name Cluster#plan_name}
        '''
        result = self._values.get("plan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of tags to assign to the HCS Azure Managed Application resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#tags Cluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#timeouts Cluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ClusterTimeouts"], result)

    @builtins.property
    def vnet_cidr(self) -> typing.Optional[builtins.str]:
        '''The VNET CIDR range of the Consul cluster. Defaults to ``172.25.16.0/24``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#vnet_cidr Cluster#vnet_cidr}
        '''
        result = self._values.get("vnet_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcs.cluster.ClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class ClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#create Cluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#default Cluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#update Cluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb1c8914ba141a3043ca4f69a745e8abe29b095e34a214799e108d8e8f0fb58)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#create Cluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#default Cluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#delete Cluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcs/r/cluster#update Cluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcs.cluster.ClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0861885c7eb140b70ba6d7fd64a74ce29ec867d591c1f3274a2816ba4dc0525)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d536a364d5137beb81f68e0b089fb28dc6eb096d6bc3af303e8ff27c411bf35e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de59ea3ab5d9df7563b5b66534374f83ecbdae6ada22a6ebe3b63ca76504b94b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee95c3607ed9a40697bfa2bdc5789f36621bff56550266b488681f8cab095bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb40b284054309441ba5035116bc4918b2103e014e5c97f773446ddb83300124)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2590e918fdb8fb35850f27bd146f2711e3add5ebd0b4a4b90c4987735bff60b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Cluster",
    "ClusterConfig",
    "ClusterTimeouts",
    "ClusterTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__0bd78262670745cabdabe4c3d61502937a233a4f0d53dac1548a82c14fe462b4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_mode: builtins.str,
    email: builtins.str,
    managed_application_name: builtins.str,
    resource_group_name: builtins.str,
    audit_logging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    audit_log_storage_container_url: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    consul_datacenter: typing.Optional[builtins.str] = None,
    consul_external_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    consul_federation_token: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    managed_resource_group_name: typing.Optional[builtins.str] = None,
    min_consul_version: typing.Optional[builtins.str] = None,
    plan_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vnet_cidr: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a61f2b971afc5d497e52bff0eb4798fc71f0ebf67048e7f2c7a06df9258bdbc7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8864c904b7eee6e84f35129f396efde2521f94b718ca4ce463e016291a0fba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4aeb44371e737efd4f88f247804fec869deda8630c3334ff22a44c8cd9d46e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ab7ac84e3d9438f7ef55edf36950057e16ea6678a3fc7a32fb26b3a19378beb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6843bfdc8071d86dff0a1ce6422ddaadb09600e33ce91cf293d84088de6d4dc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2538c4b4664b932d16b5cc092f0d12c8fe2f6f08ec98b0127c39aba112c23b63(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2018d6bcfe2373a48023d4d0b7ba1ad38834318f4f9a79f666775a9d84a2af40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cadb6051f972ad78f339d41a2f0e838913848f22b1936eb9bae49ed69d3bd82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5369a943f27b627eccb397ac7caaabd577ab7b3a3144a431c205971ca10e4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c0be4ab051cf42c2bac165b8969bf8cd79e2736ea1ba4dbd591cb340c47eeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87eeee610b162cd69ae315803f13107e4c024a0c2b7721e89e6d02f631003199(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d20791bda4c732b938f819a3974a1f3186846df826ae4e367f8d5c3c50731a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7543e2af621965465cbbebfb1a14c05dc564a5c2772a82b72c2553a87f06a89f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ad7c476e94ca495354ec692087d932131711f26606455d7e7fac9da6f34c82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de0731309a7641ed1d20399d54005f56aa8a67059797c895fdddeba159edc3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__829d4478f7b614cb5275f18b5f671b1d77d8ad9af51669f4a28fb47c4bc1649e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc6a57b432c7f3325751b353d2ee7b7e97834f35c2515a5afa96c23f0f67af2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c63368dfdd2ff38e35ab9bb268933364f25c1ab1479d0d08849b566e1aba6d57(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_mode: builtins.str,
    email: builtins.str,
    managed_application_name: builtins.str,
    resource_group_name: builtins.str,
    audit_logging_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    audit_log_storage_container_url: typing.Optional[builtins.str] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    consul_datacenter: typing.Optional[builtins.str] = None,
    consul_external_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    consul_federation_token: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    managed_resource_group_name: typing.Optional[builtins.str] = None,
    min_consul_version: typing.Optional[builtins.str] = None,
    plan_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vnet_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb1c8914ba141a3043ca4f69a745e8abe29b095e34a214799e108d8e8f0fb58(
    *,
    create: typing.Optional[builtins.str] = None,
    default: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0861885c7eb140b70ba6d7fd64a74ce29ec867d591c1f3274a2816ba4dc0525(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d536a364d5137beb81f68e0b089fb28dc6eb096d6bc3af303e8ff27c411bf35e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de59ea3ab5d9df7563b5b66534374f83ecbdae6ada22a6ebe3b63ca76504b94b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee95c3607ed9a40697bfa2bdc5789f36621bff56550266b488681f8cab095bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb40b284054309441ba5035116bc4918b2103e014e5c97f773446ddb83300124(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2590e918fdb8fb35850f27bd146f2711e3add5ebd0b4a4b90c4987735bff60b8(
    value: typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
