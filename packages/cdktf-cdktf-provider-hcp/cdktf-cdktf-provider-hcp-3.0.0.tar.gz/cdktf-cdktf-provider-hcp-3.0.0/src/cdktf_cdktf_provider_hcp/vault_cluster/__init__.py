'''
# `hcp_vault_cluster`

Refer to the Terraform Registory for docs: [`hcp_vault_cluster`](https://www.terraform.io/docs/providers/hcp/r/vault_cluster).
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


class VaultCluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster hcp_vault_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        hvn_id: builtins.str,
        audit_log_config: typing.Optional[typing.Union["VaultClusterAuditLogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        major_version_upgrade_config: typing.Optional[typing.Union["VaultClusterMajorVersionUpgradeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        metrics_config: typing.Optional[typing.Union["VaultClusterMetricsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        min_vault_version: typing.Optional[builtins.str] = None,
        paths_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_link: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VaultClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster hcp_vault_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: The ID of the HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#cluster_id VaultCluster#cluster_id}
        :param hvn_id: The ID of the HVN this HCP Vault cluster is associated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#hvn_id VaultCluster#hvn_id}
        :param audit_log_config: audit_log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#audit_log_config VaultCluster#audit_log_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#id VaultCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param major_version_upgrade_config: major_version_upgrade_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#major_version_upgrade_config VaultCluster#major_version_upgrade_config}
        :param metrics_config: metrics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#metrics_config VaultCluster#metrics_config}
        :param min_vault_version: The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#min_vault_version VaultCluster#min_vault_version}
        :param paths_filter: The performance replication `paths filter <https://developer.hashicorp.com/vault/tutorials/cloud-ops/vault-replication-terraform>`_. Applies to performance replication secondaries only and operates in "deny" mode only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#paths_filter VaultCluster#paths_filter}
        :param primary_link: The ``self_link`` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#primary_link VaultCluster#primary_link}
        :param public_endpoint: Denotes that the cluster has a public endpoint. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#public_endpoint VaultCluster#public_endpoint}
        :param tier: Tier of the HCP Vault cluster. Valid options for tiers - ``dev``, ``starter_small``, ``standard_small``, ``standard_medium``, ``standard_large``, ``plus_small``, ``plus_medium``, ``plus_large``. See `pricing information <https://cloud.hashicorp.com/pricing/vault>`_. Changing a cluster's size or tier is only available to admins. See `Scale a cluster <https://registry.terraform.io/providers/hashicorp/hcp/latest/docs/guides/vault-scaling>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#tier VaultCluster#tier}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#timeouts VaultCluster#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0a1b511b563b877d6fa1e39c5fcee395fa5006b8ec1cdc089eaff3f1e18e966)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VaultClusterConfig(
            cluster_id=cluster_id,
            hvn_id=hvn_id,
            audit_log_config=audit_log_config,
            id=id,
            major_version_upgrade_config=major_version_upgrade_config,
            metrics_config=metrics_config,
            min_vault_version=min_vault_version,
            paths_filter=paths_filter,
            primary_link=primary_link,
            public_endpoint=public_endpoint,
            tier=tier,
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

    @jsii.member(jsii_name="putAuditLogConfig")
    def put_audit_log_config(
        self,
        *,
        datadog_api_key: typing.Optional[builtins.str] = None,
        datadog_region: typing.Optional[builtins.str] = None,
        grafana_endpoint: typing.Optional[builtins.str] = None,
        grafana_password: typing.Optional[builtins.str] = None,
        grafana_user: typing.Optional[builtins.str] = None,
        splunk_hecendpoint: typing.Optional[builtins.str] = None,
        splunk_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datadog_api_key: Datadog api key for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        :param datadog_region: Datadog region for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        :param grafana_endpoint: Grafana endpoint for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        :param grafana_password: Grafana password for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        :param grafana_user: Grafana user for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        :param splunk_hecendpoint: Splunk endpoint for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        :param splunk_token: Splunk token for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        value = VaultClusterAuditLogConfig(
            datadog_api_key=datadog_api_key,
            datadog_region=datadog_region,
            grafana_endpoint=grafana_endpoint,
            grafana_password=grafana_password,
            grafana_user=grafana_user,
            splunk_hecendpoint=splunk_hecendpoint,
            splunk_token=splunk_token,
        )

        return typing.cast(None, jsii.invoke(self, "putAuditLogConfig", [value]))

    @jsii.member(jsii_name="putMajorVersionUpgradeConfig")
    def put_major_version_upgrade_config(
        self,
        *,
        upgrade_type: builtins.str,
        maintenance_window_day: typing.Optional[builtins.str] = None,
        maintenance_window_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param upgrade_type: The major upgrade type for the cluster. Valid options for upgrade type - ``AUTOMATIC``, ``SCHEDULED``, ``MANUAL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#upgrade_type VaultCluster#upgrade_type}
        :param maintenance_window_day: The maintenance day of the week for scheduled upgrades. Valid options for maintenance window day - ``MONDAY``, ``TUESDAY``, ``WEDNESDAY``, ``THURSDAY``, ``FRIDAY``, ``SATURDAY``, ``SUNDAY`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_day VaultCluster#maintenance_window_day}
        :param maintenance_window_time: The maintenance time frame for scheduled upgrades. Valid options for maintenance window time - ``WINDOW_12AM_4AM``, ``WINDOW_6AM_10AM``, ``WINDOW_12PM_4PM``, ``WINDOW_6PM_10PM``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_time VaultCluster#maintenance_window_time}
        '''
        value = VaultClusterMajorVersionUpgradeConfig(
            upgrade_type=upgrade_type,
            maintenance_window_day=maintenance_window_day,
            maintenance_window_time=maintenance_window_time,
        )

        return typing.cast(None, jsii.invoke(self, "putMajorVersionUpgradeConfig", [value]))

    @jsii.member(jsii_name="putMetricsConfig")
    def put_metrics_config(
        self,
        *,
        datadog_api_key: typing.Optional[builtins.str] = None,
        datadog_region: typing.Optional[builtins.str] = None,
        grafana_endpoint: typing.Optional[builtins.str] = None,
        grafana_password: typing.Optional[builtins.str] = None,
        grafana_user: typing.Optional[builtins.str] = None,
        splunk_hecendpoint: typing.Optional[builtins.str] = None,
        splunk_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datadog_api_key: Datadog api key for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        :param datadog_region: Datadog region for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        :param grafana_endpoint: Grafana endpoint for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        :param grafana_password: Grafana password for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        :param grafana_user: Grafana user for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        :param splunk_hecendpoint: Splunk endpoint for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        :param splunk_token: Splunk token for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        value = VaultClusterMetricsConfig(
            datadog_api_key=datadog_api_key,
            datadog_region=datadog_region,
            grafana_endpoint=grafana_endpoint,
            grafana_password=grafana_password,
            grafana_user=grafana_user,
            splunk_hecendpoint=splunk_hecendpoint,
            splunk_token=splunk_token,
        )

        return typing.cast(None, jsii.invoke(self, "putMetricsConfig", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#create VaultCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#default VaultCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#delete VaultCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#update VaultCluster#update}.
        '''
        value = VaultClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuditLogConfig")
    def reset_audit_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditLogConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMajorVersionUpgradeConfig")
    def reset_major_version_upgrade_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMajorVersionUpgradeConfig", []))

    @jsii.member(jsii_name="resetMetricsConfig")
    def reset_metrics_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsConfig", []))

    @jsii.member(jsii_name="resetMinVaultVersion")
    def reset_min_vault_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinVaultVersion", []))

    @jsii.member(jsii_name="resetPathsFilter")
    def reset_paths_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathsFilter", []))

    @jsii.member(jsii_name="resetPrimaryLink")
    def reset_primary_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryLink", []))

    @jsii.member(jsii_name="resetPublicEndpoint")
    def reset_public_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicEndpoint", []))

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

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
    @jsii.member(jsii_name="auditLogConfig")
    def audit_log_config(self) -> "VaultClusterAuditLogConfigOutputReference":
        return typing.cast("VaultClusterAuditLogConfigOutputReference", jsii.get(self, "auditLogConfig"))

    @builtins.property
    @jsii.member(jsii_name="cloudProvider")
    def cloud_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudProvider"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="majorVersionUpgradeConfig")
    def major_version_upgrade_config(
        self,
    ) -> "VaultClusterMajorVersionUpgradeConfigOutputReference":
        return typing.cast("VaultClusterMajorVersionUpgradeConfigOutputReference", jsii.get(self, "majorVersionUpgradeConfig"))

    @builtins.property
    @jsii.member(jsii_name="metricsConfig")
    def metrics_config(self) -> "VaultClusterMetricsConfigOutputReference":
        return typing.cast("VaultClusterMetricsConfigOutputReference", jsii.get(self, "metricsConfig"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationId"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VaultClusterTimeoutsOutputReference":
        return typing.cast("VaultClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vaultPrivateEndpointUrl")
    def vault_private_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultPrivateEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="vaultPublicEndpointUrl")
    def vault_public_endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultPublicEndpointUrl"))

    @builtins.property
    @jsii.member(jsii_name="vaultVersion")
    def vault_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultVersion"))

    @builtins.property
    @jsii.member(jsii_name="auditLogConfigInput")
    def audit_log_config_input(self) -> typing.Optional["VaultClusterAuditLogConfig"]:
        return typing.cast(typing.Optional["VaultClusterAuditLogConfig"], jsii.get(self, "auditLogConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hvnIdInput")
    def hvn_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvnIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="majorVersionUpgradeConfigInput")
    def major_version_upgrade_config_input(
        self,
    ) -> typing.Optional["VaultClusterMajorVersionUpgradeConfig"]:
        return typing.cast(typing.Optional["VaultClusterMajorVersionUpgradeConfig"], jsii.get(self, "majorVersionUpgradeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsConfigInput")
    def metrics_config_input(self) -> typing.Optional["VaultClusterMetricsConfig"]:
        return typing.cast(typing.Optional["VaultClusterMetricsConfig"], jsii.get(self, "metricsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="minVaultVersionInput")
    def min_vault_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minVaultVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="pathsFilterInput")
    def paths_filter_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryLinkInput")
    def primary_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="publicEndpointInput")
    def public_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publicEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VaultClusterTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VaultClusterTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28bc1d0d3a11385f69f5b593a33f6d3cc36b251943c87e7d84b71d9f8a55c96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="hvnId")
    def hvn_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvnId"))

    @hvn_id.setter
    def hvn_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8cdedf475d77d4cb3670ceece6593d632a9a72936b6238f2f76aa2514ef4572)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvnId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5c4e2848248807929ac0f0629a93ce153465a1bb489918b844c01429318169b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="minVaultVersion")
    def min_vault_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minVaultVersion"))

    @min_vault_version.setter
    def min_vault_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90a99787bbba8532314d4fd46a461dc8ba4d79f11b79268b61109a69c9385f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minVaultVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pathsFilter")
    def paths_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathsFilter"))

    @paths_filter.setter
    def paths_filter(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c447c3a56ed005d7cea3740b1d9073d95b302c6ca34d5cb42b113743dd43d4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathsFilter", value)

    @builtins.property
    @jsii.member(jsii_name="primaryLink")
    def primary_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLink"))

    @primary_link.setter
    def primary_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acd1ba2389475dbdef88d02a36491fcce5ddc9cb2a19ece1b06b2f06d94ce93c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryLink", value)

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publicEndpoint"))

    @public_endpoint.setter
    def public_endpoint(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__016406781c3e03ebe4828004b44a7c0d843366101b7bba83be5a1eda02278189)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c863274558c2e6fbc79bf383c815279e3522fca7fe37c4616fd7fb98b80fa456)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterAuditLogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "datadog_api_key": "datadogApiKey",
        "datadog_region": "datadogRegion",
        "grafana_endpoint": "grafanaEndpoint",
        "grafana_password": "grafanaPassword",
        "grafana_user": "grafanaUser",
        "splunk_hecendpoint": "splunkHecendpoint",
        "splunk_token": "splunkToken",
    },
)
class VaultClusterAuditLogConfig:
    def __init__(
        self,
        *,
        datadog_api_key: typing.Optional[builtins.str] = None,
        datadog_region: typing.Optional[builtins.str] = None,
        grafana_endpoint: typing.Optional[builtins.str] = None,
        grafana_password: typing.Optional[builtins.str] = None,
        grafana_user: typing.Optional[builtins.str] = None,
        splunk_hecendpoint: typing.Optional[builtins.str] = None,
        splunk_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datadog_api_key: Datadog api key for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        :param datadog_region: Datadog region for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        :param grafana_endpoint: Grafana endpoint for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        :param grafana_password: Grafana password for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        :param grafana_user: Grafana user for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        :param splunk_hecendpoint: Splunk endpoint for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        :param splunk_token: Splunk token for streaming audit logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945e965e9dab450573c42b8a5cc975ed8d0713bf41d459bead13f88051d0a34e)
            check_type(argname="argument datadog_api_key", value=datadog_api_key, expected_type=type_hints["datadog_api_key"])
            check_type(argname="argument datadog_region", value=datadog_region, expected_type=type_hints["datadog_region"])
            check_type(argname="argument grafana_endpoint", value=grafana_endpoint, expected_type=type_hints["grafana_endpoint"])
            check_type(argname="argument grafana_password", value=grafana_password, expected_type=type_hints["grafana_password"])
            check_type(argname="argument grafana_user", value=grafana_user, expected_type=type_hints["grafana_user"])
            check_type(argname="argument splunk_hecendpoint", value=splunk_hecendpoint, expected_type=type_hints["splunk_hecendpoint"])
            check_type(argname="argument splunk_token", value=splunk_token, expected_type=type_hints["splunk_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datadog_api_key is not None:
            self._values["datadog_api_key"] = datadog_api_key
        if datadog_region is not None:
            self._values["datadog_region"] = datadog_region
        if grafana_endpoint is not None:
            self._values["grafana_endpoint"] = grafana_endpoint
        if grafana_password is not None:
            self._values["grafana_password"] = grafana_password
        if grafana_user is not None:
            self._values["grafana_user"] = grafana_user
        if splunk_hecendpoint is not None:
            self._values["splunk_hecendpoint"] = splunk_hecendpoint
        if splunk_token is not None:
            self._values["splunk_token"] = splunk_token

    @builtins.property
    def datadog_api_key(self) -> typing.Optional[builtins.str]:
        '''Datadog api key for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        '''
        result = self._values.get("datadog_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog_region(self) -> typing.Optional[builtins.str]:
        '''Datadog region for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        '''
        result = self._values.get("datadog_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_endpoint(self) -> typing.Optional[builtins.str]:
        '''Grafana endpoint for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        '''
        result = self._values.get("grafana_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_password(self) -> typing.Optional[builtins.str]:
        '''Grafana password for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        '''
        result = self._values.get("grafana_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_user(self) -> typing.Optional[builtins.str]:
        '''Grafana user for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        '''
        result = self._values.get("grafana_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def splunk_hecendpoint(self) -> typing.Optional[builtins.str]:
        '''Splunk endpoint for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        '''
        result = self._values.get("splunk_hecendpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def splunk_token(self) -> typing.Optional[builtins.str]:
        '''Splunk token for streaming audit logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        result = self._values.get("splunk_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultClusterAuditLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VaultClusterAuditLogConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterAuditLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8b875f9e1e5a69e90f3ccbd14774843fdcf1ec3dea2e285c4304b00a740ea8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatadogApiKey")
    def reset_datadog_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadogApiKey", []))

    @jsii.member(jsii_name="resetDatadogRegion")
    def reset_datadog_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadogRegion", []))

    @jsii.member(jsii_name="resetGrafanaEndpoint")
    def reset_grafana_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaEndpoint", []))

    @jsii.member(jsii_name="resetGrafanaPassword")
    def reset_grafana_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaPassword", []))

    @jsii.member(jsii_name="resetGrafanaUser")
    def reset_grafana_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaUser", []))

    @jsii.member(jsii_name="resetSplunkHecendpoint")
    def reset_splunk_hecendpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkHecendpoint", []))

    @jsii.member(jsii_name="resetSplunkToken")
    def reset_splunk_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkToken", []))

    @builtins.property
    @jsii.member(jsii_name="datadogApiKeyInput")
    def datadog_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogRegionInput")
    def datadog_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpointInput")
    def grafana_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaPasswordInput")
    def grafana_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaUserInput")
    def grafana_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaUserInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpointInput")
    def splunk_hecendpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splunkHecendpointInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkTokenInput")
    def splunk_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splunkTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogApiKey")
    def datadog_api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogApiKey"))

    @datadog_api_key.setter
    def datadog_api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b6ffc4fdcdfc68f19b0649b3264f8e211b7e469bd01556c00b2071a18f4583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadogApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="datadogRegion")
    def datadog_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogRegion"))

    @datadog_region.setter
    def datadog_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52584035adf1cf6ac49bc62a4ac84427a1190b4e2a7d5a650d7e74ae236d99e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadogRegion", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpoint")
    def grafana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaEndpoint"))

    @grafana_endpoint.setter
    def grafana_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9d1c04f0203c3a9f08cfaf64b33eb749078f35c5b9cc82332488d49b6209dba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaPassword")
    def grafana_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaPassword"))

    @grafana_password.setter
    def grafana_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9bf93f6ea32ddf32ca74534faaaf7627202436b7312f697895778a1d2d64871)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaPassword", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaUser")
    def grafana_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaUser"))

    @grafana_user.setter
    def grafana_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f9d0b3500812b9094d68925a982d1b6932bbf0ac677a39454abd2a24d756ec4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaUser", value)

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpoint")
    def splunk_hecendpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkHecendpoint"))

    @splunk_hecendpoint.setter
    def splunk_hecendpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a053588ad2844b98959edfef3e01d2d1e9515509c6f776522a4756f7fe6fd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkHecendpoint", value)

    @builtins.property
    @jsii.member(jsii_name="splunkToken")
    def splunk_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkToken"))

    @splunk_token.setter
    def splunk_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7584064c3929586049d8fb7cba2238d2bfb9dab2c965ebaeeea3863eba36bf1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VaultClusterAuditLogConfig]:
        return typing.cast(typing.Optional[VaultClusterAuditLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VaultClusterAuditLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2d391a17055a27cde669c5b609a5fa628c2645bdd1b56018ee38cb2caa8d1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "hvn_id": "hvnId",
        "audit_log_config": "auditLogConfig",
        "id": "id",
        "major_version_upgrade_config": "majorVersionUpgradeConfig",
        "metrics_config": "metricsConfig",
        "min_vault_version": "minVaultVersion",
        "paths_filter": "pathsFilter",
        "primary_link": "primaryLink",
        "public_endpoint": "publicEndpoint",
        "tier": "tier",
        "timeouts": "timeouts",
    },
)
class VaultClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        hvn_id: builtins.str,
        audit_log_config: typing.Optional[typing.Union[VaultClusterAuditLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        major_version_upgrade_config: typing.Optional[typing.Union["VaultClusterMajorVersionUpgradeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        metrics_config: typing.Optional[typing.Union["VaultClusterMetricsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        min_vault_version: typing.Optional[builtins.str] = None,
        paths_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary_link: typing.Optional[builtins.str] = None,
        public_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["VaultClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: The ID of the HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#cluster_id VaultCluster#cluster_id}
        :param hvn_id: The ID of the HVN this HCP Vault cluster is associated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#hvn_id VaultCluster#hvn_id}
        :param audit_log_config: audit_log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#audit_log_config VaultCluster#audit_log_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#id VaultCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param major_version_upgrade_config: major_version_upgrade_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#major_version_upgrade_config VaultCluster#major_version_upgrade_config}
        :param metrics_config: metrics_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#metrics_config VaultCluster#metrics_config}
        :param min_vault_version: The minimum Vault version to use when creating the cluster. If not specified, it is defaulted to the version that is currently recommended by HCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#min_vault_version VaultCluster#min_vault_version}
        :param paths_filter: The performance replication `paths filter <https://developer.hashicorp.com/vault/tutorials/cloud-ops/vault-replication-terraform>`_. Applies to performance replication secondaries only and operates in "deny" mode only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#paths_filter VaultCluster#paths_filter}
        :param primary_link: The ``self_link`` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this HCP Vault Plus tier cluster. If not specified, it is a standalone Plus tier HCP Vault cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#primary_link VaultCluster#primary_link}
        :param public_endpoint: Denotes that the cluster has a public endpoint. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#public_endpoint VaultCluster#public_endpoint}
        :param tier: Tier of the HCP Vault cluster. Valid options for tiers - ``dev``, ``starter_small``, ``standard_small``, ``standard_medium``, ``standard_large``, ``plus_small``, ``plus_medium``, ``plus_large``. See `pricing information <https://cloud.hashicorp.com/pricing/vault>`_. Changing a cluster's size or tier is only available to admins. See `Scale a cluster <https://registry.terraform.io/providers/hashicorp/hcp/latest/docs/guides/vault-scaling>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#tier VaultCluster#tier}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#timeouts VaultCluster#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(audit_log_config, dict):
            audit_log_config = VaultClusterAuditLogConfig(**audit_log_config)
        if isinstance(major_version_upgrade_config, dict):
            major_version_upgrade_config = VaultClusterMajorVersionUpgradeConfig(**major_version_upgrade_config)
        if isinstance(metrics_config, dict):
            metrics_config = VaultClusterMetricsConfig(**metrics_config)
        if isinstance(timeouts, dict):
            timeouts = VaultClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a47be8c3817c70555bc777416f18db7e158d5f4a408d5a70bef49dc6666cf0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument hvn_id", value=hvn_id, expected_type=type_hints["hvn_id"])
            check_type(argname="argument audit_log_config", value=audit_log_config, expected_type=type_hints["audit_log_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument major_version_upgrade_config", value=major_version_upgrade_config, expected_type=type_hints["major_version_upgrade_config"])
            check_type(argname="argument metrics_config", value=metrics_config, expected_type=type_hints["metrics_config"])
            check_type(argname="argument min_vault_version", value=min_vault_version, expected_type=type_hints["min_vault_version"])
            check_type(argname="argument paths_filter", value=paths_filter, expected_type=type_hints["paths_filter"])
            check_type(argname="argument primary_link", value=primary_link, expected_type=type_hints["primary_link"])
            check_type(argname="argument public_endpoint", value=public_endpoint, expected_type=type_hints["public_endpoint"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "hvn_id": hvn_id,
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
        if audit_log_config is not None:
            self._values["audit_log_config"] = audit_log_config
        if id is not None:
            self._values["id"] = id
        if major_version_upgrade_config is not None:
            self._values["major_version_upgrade_config"] = major_version_upgrade_config
        if metrics_config is not None:
            self._values["metrics_config"] = metrics_config
        if min_vault_version is not None:
            self._values["min_vault_version"] = min_vault_version
        if paths_filter is not None:
            self._values["paths_filter"] = paths_filter
        if primary_link is not None:
            self._values["primary_link"] = primary_link
        if public_endpoint is not None:
            self._values["public_endpoint"] = public_endpoint
        if tier is not None:
            self._values["tier"] = tier
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
    def cluster_id(self) -> builtins.str:
        '''The ID of the HCP Vault cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#cluster_id VaultCluster#cluster_id}
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hvn_id(self) -> builtins.str:
        '''The ID of the HVN this HCP Vault cluster is associated to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#hvn_id VaultCluster#hvn_id}
        '''
        result = self._values.get("hvn_id")
        assert result is not None, "Required property 'hvn_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_log_config(self) -> typing.Optional[VaultClusterAuditLogConfig]:
        '''audit_log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#audit_log_config VaultCluster#audit_log_config}
        '''
        result = self._values.get("audit_log_config")
        return typing.cast(typing.Optional[VaultClusterAuditLogConfig], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#id VaultCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def major_version_upgrade_config(
        self,
    ) -> typing.Optional["VaultClusterMajorVersionUpgradeConfig"]:
        '''major_version_upgrade_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#major_version_upgrade_config VaultCluster#major_version_upgrade_config}
        '''
        result = self._values.get("major_version_upgrade_config")
        return typing.cast(typing.Optional["VaultClusterMajorVersionUpgradeConfig"], result)

    @builtins.property
    def metrics_config(self) -> typing.Optional["VaultClusterMetricsConfig"]:
        '''metrics_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#metrics_config VaultCluster#metrics_config}
        '''
        result = self._values.get("metrics_config")
        return typing.cast(typing.Optional["VaultClusterMetricsConfig"], result)

    @builtins.property
    def min_vault_version(self) -> typing.Optional[builtins.str]:
        '''The minimum Vault version to use when creating the cluster.

        If not specified, it is defaulted to the version that is currently recommended by HCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#min_vault_version VaultCluster#min_vault_version}
        '''
        result = self._values.get("min_vault_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paths_filter(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The performance replication `paths filter <https://developer.hashicorp.com/vault/tutorials/cloud-ops/vault-replication-terraform>`_. Applies to performance replication secondaries only and operates in "deny" mode only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#paths_filter VaultCluster#paths_filter}
        '''
        result = self._values.get("paths_filter")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary_link(self) -> typing.Optional[builtins.str]:
        '''The ``self_link`` of the HCP Vault Plus tier cluster which is the primary in the performance replication setup with this HCP Vault Plus tier cluster.

        If not specified, it is a standalone Plus tier HCP Vault cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#primary_link VaultCluster#primary_link}
        '''
        result = self._values.get("primary_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Denotes that the cluster has a public endpoint. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#public_endpoint VaultCluster#public_endpoint}
        '''
        result = self._values.get("public_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''Tier of the HCP Vault cluster.

        Valid options for tiers - ``dev``, ``starter_small``, ``standard_small``, ``standard_medium``, ``standard_large``, ``plus_small``, ``plus_medium``, ``plus_large``. See `pricing information <https://cloud.hashicorp.com/pricing/vault>`_. Changing a cluster's size or tier is only available to admins. See `Scale a cluster <https://registry.terraform.io/providers/hashicorp/hcp/latest/docs/guides/vault-scaling>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#tier VaultCluster#tier}
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VaultClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#timeouts VaultCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VaultClusterTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterMajorVersionUpgradeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "upgrade_type": "upgradeType",
        "maintenance_window_day": "maintenanceWindowDay",
        "maintenance_window_time": "maintenanceWindowTime",
    },
)
class VaultClusterMajorVersionUpgradeConfig:
    def __init__(
        self,
        *,
        upgrade_type: builtins.str,
        maintenance_window_day: typing.Optional[builtins.str] = None,
        maintenance_window_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param upgrade_type: The major upgrade type for the cluster. Valid options for upgrade type - ``AUTOMATIC``, ``SCHEDULED``, ``MANUAL``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#upgrade_type VaultCluster#upgrade_type}
        :param maintenance_window_day: The maintenance day of the week for scheduled upgrades. Valid options for maintenance window day - ``MONDAY``, ``TUESDAY``, ``WEDNESDAY``, ``THURSDAY``, ``FRIDAY``, ``SATURDAY``, ``SUNDAY`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_day VaultCluster#maintenance_window_day}
        :param maintenance_window_time: The maintenance time frame for scheduled upgrades. Valid options for maintenance window time - ``WINDOW_12AM_4AM``, ``WINDOW_6AM_10AM``, ``WINDOW_12PM_4PM``, ``WINDOW_6PM_10PM``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_time VaultCluster#maintenance_window_time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4962f49b844cabab740d8df01f3b70a715d3f1306b60fec54b6272426400d44)
            check_type(argname="argument upgrade_type", value=upgrade_type, expected_type=type_hints["upgrade_type"])
            check_type(argname="argument maintenance_window_day", value=maintenance_window_day, expected_type=type_hints["maintenance_window_day"])
            check_type(argname="argument maintenance_window_time", value=maintenance_window_time, expected_type=type_hints["maintenance_window_time"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "upgrade_type": upgrade_type,
        }
        if maintenance_window_day is not None:
            self._values["maintenance_window_day"] = maintenance_window_day
        if maintenance_window_time is not None:
            self._values["maintenance_window_time"] = maintenance_window_time

    @builtins.property
    def upgrade_type(self) -> builtins.str:
        '''The major upgrade type for the cluster. Valid options for upgrade type - ``AUTOMATIC``, ``SCHEDULED``, ``MANUAL``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#upgrade_type VaultCluster#upgrade_type}
        '''
        result = self._values.get("upgrade_type")
        assert result is not None, "Required property 'upgrade_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_window_day(self) -> typing.Optional[builtins.str]:
        '''The maintenance day of the week for scheduled upgrades.

        Valid options for maintenance window day - ``MONDAY``, ``TUESDAY``, ``WEDNESDAY``, ``THURSDAY``, ``FRIDAY``, ``SATURDAY``, ``SUNDAY``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_day VaultCluster#maintenance_window_day}
        '''
        result = self._values.get("maintenance_window_day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window_time(self) -> typing.Optional[builtins.str]:
        '''The maintenance time frame for scheduled upgrades. Valid options for maintenance window time - ``WINDOW_12AM_4AM``, ``WINDOW_6AM_10AM``, ``WINDOW_12PM_4PM``, ``WINDOW_6PM_10PM``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#maintenance_window_time VaultCluster#maintenance_window_time}
        '''
        result = self._values.get("maintenance_window_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultClusterMajorVersionUpgradeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VaultClusterMajorVersionUpgradeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterMajorVersionUpgradeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__00220fe9e0d944a01da3073321aa1195a8785491ef20ede83c5c9e60456cfccc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaintenanceWindowDay")
    def reset_maintenance_window_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindowDay", []))

    @jsii.member(jsii_name="resetMaintenanceWindowTime")
    def reset_maintenance_window_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindowTime", []))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDayInput")
    def maintenance_window_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowDayInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTimeInput")
    def maintenance_window_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceWindowTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeTypeInput")
    def upgrade_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowDay")
    def maintenance_window_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowDay"))

    @maintenance_window_day.setter
    def maintenance_window_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__731c8b0a131354c50c4187c419df1ca0b4ceae942541b703dccc29bddc2ae24d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowDay", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTime")
    def maintenance_window_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maintenanceWindowTime"))

    @maintenance_window_time.setter
    def maintenance_window_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f434d7fee16e563e0a028d6996e7baa865d83d6283058a983dd31e012a5ee7d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceWindowTime", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeType")
    def upgrade_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeType"))

    @upgrade_type.setter
    def upgrade_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__985cbace5e3cd0b9202218537c218691890d235d32455d4d255ad4bdb2d63fe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VaultClusterMajorVersionUpgradeConfig]:
        return typing.cast(typing.Optional[VaultClusterMajorVersionUpgradeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VaultClusterMajorVersionUpgradeConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73923462dd4285e4699c6c87591575ddc937cd2eac326dd6c048a6d19e1d13e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterMetricsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "datadog_api_key": "datadogApiKey",
        "datadog_region": "datadogRegion",
        "grafana_endpoint": "grafanaEndpoint",
        "grafana_password": "grafanaPassword",
        "grafana_user": "grafanaUser",
        "splunk_hecendpoint": "splunkHecendpoint",
        "splunk_token": "splunkToken",
    },
)
class VaultClusterMetricsConfig:
    def __init__(
        self,
        *,
        datadog_api_key: typing.Optional[builtins.str] = None,
        datadog_region: typing.Optional[builtins.str] = None,
        grafana_endpoint: typing.Optional[builtins.str] = None,
        grafana_password: typing.Optional[builtins.str] = None,
        grafana_user: typing.Optional[builtins.str] = None,
        splunk_hecendpoint: typing.Optional[builtins.str] = None,
        splunk_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datadog_api_key: Datadog api key for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        :param datadog_region: Datadog region for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        :param grafana_endpoint: Grafana endpoint for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        :param grafana_password: Grafana password for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        :param grafana_user: Grafana user for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        :param splunk_hecendpoint: Splunk endpoint for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        :param splunk_token: Splunk token for streaming metrics. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41328d9c30b2160db3534c4e47502c0f13855650febdfb88b239dcb6d6ee814)
            check_type(argname="argument datadog_api_key", value=datadog_api_key, expected_type=type_hints["datadog_api_key"])
            check_type(argname="argument datadog_region", value=datadog_region, expected_type=type_hints["datadog_region"])
            check_type(argname="argument grafana_endpoint", value=grafana_endpoint, expected_type=type_hints["grafana_endpoint"])
            check_type(argname="argument grafana_password", value=grafana_password, expected_type=type_hints["grafana_password"])
            check_type(argname="argument grafana_user", value=grafana_user, expected_type=type_hints["grafana_user"])
            check_type(argname="argument splunk_hecendpoint", value=splunk_hecendpoint, expected_type=type_hints["splunk_hecendpoint"])
            check_type(argname="argument splunk_token", value=splunk_token, expected_type=type_hints["splunk_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datadog_api_key is not None:
            self._values["datadog_api_key"] = datadog_api_key
        if datadog_region is not None:
            self._values["datadog_region"] = datadog_region
        if grafana_endpoint is not None:
            self._values["grafana_endpoint"] = grafana_endpoint
        if grafana_password is not None:
            self._values["grafana_password"] = grafana_password
        if grafana_user is not None:
            self._values["grafana_user"] = grafana_user
        if splunk_hecendpoint is not None:
            self._values["splunk_hecendpoint"] = splunk_hecendpoint
        if splunk_token is not None:
            self._values["splunk_token"] = splunk_token

    @builtins.property
    def datadog_api_key(self) -> typing.Optional[builtins.str]:
        '''Datadog api key for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_api_key VaultCluster#datadog_api_key}
        '''
        result = self._values.get("datadog_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datadog_region(self) -> typing.Optional[builtins.str]:
        '''Datadog region for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#datadog_region VaultCluster#datadog_region}
        '''
        result = self._values.get("datadog_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_endpoint(self) -> typing.Optional[builtins.str]:
        '''Grafana endpoint for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_endpoint VaultCluster#grafana_endpoint}
        '''
        result = self._values.get("grafana_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_password(self) -> typing.Optional[builtins.str]:
        '''Grafana password for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_password VaultCluster#grafana_password}
        '''
        result = self._values.get("grafana_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grafana_user(self) -> typing.Optional[builtins.str]:
        '''Grafana user for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#grafana_user VaultCluster#grafana_user}
        '''
        result = self._values.get("grafana_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def splunk_hecendpoint(self) -> typing.Optional[builtins.str]:
        '''Splunk endpoint for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_hecendpoint VaultCluster#splunk_hecendpoint}
        '''
        result = self._values.get("splunk_hecendpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def splunk_token(self) -> typing.Optional[builtins.str]:
        '''Splunk token for streaming metrics.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#splunk_token VaultCluster#splunk_token}
        '''
        result = self._values.get("splunk_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultClusterMetricsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VaultClusterMetricsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterMetricsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7573747a2312afa8ffc8dafc01025857a8dc813746d0e47c1ba6fbbe8778ac35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatadogApiKey")
    def reset_datadog_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadogApiKey", []))

    @jsii.member(jsii_name="resetDatadogRegion")
    def reset_datadog_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadogRegion", []))

    @jsii.member(jsii_name="resetGrafanaEndpoint")
    def reset_grafana_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaEndpoint", []))

    @jsii.member(jsii_name="resetGrafanaPassword")
    def reset_grafana_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaPassword", []))

    @jsii.member(jsii_name="resetGrafanaUser")
    def reset_grafana_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrafanaUser", []))

    @jsii.member(jsii_name="resetSplunkHecendpoint")
    def reset_splunk_hecendpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkHecendpoint", []))

    @jsii.member(jsii_name="resetSplunkToken")
    def reset_splunk_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSplunkToken", []))

    @builtins.property
    @jsii.member(jsii_name="datadogApiKeyInput")
    def datadog_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogRegionInput")
    def datadog_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datadogRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpointInput")
    def grafana_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaPasswordInput")
    def grafana_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="grafanaUserInput")
    def grafana_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grafanaUserInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpointInput")
    def splunk_hecendpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splunkHecendpointInput"))

    @builtins.property
    @jsii.member(jsii_name="splunkTokenInput")
    def splunk_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "splunkTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="datadogApiKey")
    def datadog_api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogApiKey"))

    @datadog_api_key.setter
    def datadog_api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01774f33baeaf10f919c131dc102f79f36eeff62b05d905990090cc7a031f8a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadogApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="datadogRegion")
    def datadog_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datadogRegion"))

    @datadog_region.setter
    def datadog_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53493b753297becfad9e332d6d76bf38108bc351b6b3e20baddb9bb07893b458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datadogRegion", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaEndpoint")
    def grafana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaEndpoint"))

    @grafana_endpoint.setter
    def grafana_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae544b6a716e103200c258e30bdeecaffec6121c50d96449de5d9b48fbbc24c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaPassword")
    def grafana_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaPassword"))

    @grafana_password.setter
    def grafana_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1064d1abe056bb9b3eb383bd3d0f5cb018fb61bf6744005bc22fc06f26bca5cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaPassword", value)

    @builtins.property
    @jsii.member(jsii_name="grafanaUser")
    def grafana_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grafanaUser"))

    @grafana_user.setter
    def grafana_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc49e4808e51cb5e796669e09cca32630adbb4539a73b19a0900c53fcf47a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grafanaUser", value)

    @builtins.property
    @jsii.member(jsii_name="splunkHecendpoint")
    def splunk_hecendpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkHecendpoint"))

    @splunk_hecendpoint.setter
    def splunk_hecendpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3d1fedf5a113300f4ff7aff7390f5a7677acca337373f048c07ca807be7bd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkHecendpoint", value)

    @builtins.property
    @jsii.member(jsii_name="splunkToken")
    def splunk_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "splunkToken"))

    @splunk_token.setter
    def splunk_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41262da7c69a34522658c9a64fb97b513270eab90b33134705d21e460bf4bf7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VaultClusterMetricsConfig]:
        return typing.cast(typing.Optional[VaultClusterMetricsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VaultClusterMetricsConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2bf482f44b38423d4061abe71c12776c465cb81d41e5ec0fd2fd93519e289f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class VaultClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#create VaultCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#default VaultCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#delete VaultCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#update VaultCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ee5e56e863fb68b056cf0c52c11694127fd2447b2109705c1c013124bc122b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#create VaultCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#default VaultCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#delete VaultCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/hcp/r/vault_cluster#update VaultCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VaultClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VaultClusterTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-hcp.vaultCluster.VaultClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65ecdf217b4bc03cba984541a801600b2d5439419fe5d42ba40ff7ac32ec3333)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db2c8ee9a177a1817b11e58fd9878424e1054d355e3bcb7b746bbe30fa3cbc2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d87e66bf7ba09872850753eb0320a0428faf4ccd45ba0b681c88af537cb66fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b560841a2a171c6555944671bf203111462c74d3d57852b50f20076467171e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__507fb6faf5cecc7fb6c63feaca0dae7ff5b1a3150654d705aecead89ab25793c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VaultClusterTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VaultClusterTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VaultClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc0b876897d7750cc1f48d98ef8fac9b2418b3c42aad84f70d54d171bb85f4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VaultCluster",
    "VaultClusterAuditLogConfig",
    "VaultClusterAuditLogConfigOutputReference",
    "VaultClusterConfig",
    "VaultClusterMajorVersionUpgradeConfig",
    "VaultClusterMajorVersionUpgradeConfigOutputReference",
    "VaultClusterMetricsConfig",
    "VaultClusterMetricsConfigOutputReference",
    "VaultClusterTimeouts",
    "VaultClusterTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__a0a1b511b563b877d6fa1e39c5fcee395fa5006b8ec1cdc089eaff3f1e18e966(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    hvn_id: builtins.str,
    audit_log_config: typing.Optional[typing.Union[VaultClusterAuditLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    major_version_upgrade_config: typing.Optional[typing.Union[VaultClusterMajorVersionUpgradeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    metrics_config: typing.Optional[typing.Union[VaultClusterMetricsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    min_vault_version: typing.Optional[builtins.str] = None,
    paths_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_link: typing.Optional[builtins.str] = None,
    public_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tier: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[VaultClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__c28bc1d0d3a11385f69f5b593a33f6d3cc36b251943c87e7d84b71d9f8a55c96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cdedf475d77d4cb3670ceece6593d632a9a72936b6238f2f76aa2514ef4572(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c4e2848248807929ac0f0629a93ce153465a1bb489918b844c01429318169b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90a99787bbba8532314d4fd46a461dc8ba4d79f11b79268b61109a69c9385f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c447c3a56ed005d7cea3740b1d9073d95b302c6ca34d5cb42b113743dd43d4f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd1ba2389475dbdef88d02a36491fcce5ddc9cb2a19ece1b06b2f06d94ce93c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016406781c3e03ebe4828004b44a7c0d843366101b7bba83be5a1eda02278189(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c863274558c2e6fbc79bf383c815279e3522fca7fe37c4616fd7fb98b80fa456(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945e965e9dab450573c42b8a5cc975ed8d0713bf41d459bead13f88051d0a34e(
    *,
    datadog_api_key: typing.Optional[builtins.str] = None,
    datadog_region: typing.Optional[builtins.str] = None,
    grafana_endpoint: typing.Optional[builtins.str] = None,
    grafana_password: typing.Optional[builtins.str] = None,
    grafana_user: typing.Optional[builtins.str] = None,
    splunk_hecendpoint: typing.Optional[builtins.str] = None,
    splunk_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b875f9e1e5a69e90f3ccbd14774843fdcf1ec3dea2e285c4304b00a740ea8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b6ffc4fdcdfc68f19b0649b3264f8e211b7e469bd01556c00b2071a18f4583(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52584035adf1cf6ac49bc62a4ac84427a1190b4e2a7d5a650d7e74ae236d99e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d1c04f0203c3a9f08cfaf64b33eb749078f35c5b9cc82332488d49b6209dba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9bf93f6ea32ddf32ca74534faaaf7627202436b7312f697895778a1d2d64871(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9d0b3500812b9094d68925a982d1b6932bbf0ac677a39454abd2a24d756ec4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a053588ad2844b98959edfef3e01d2d1e9515509c6f776522a4756f7fe6fd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7584064c3929586049d8fb7cba2238d2bfb9dab2c965ebaeeea3863eba36bf1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2d391a17055a27cde669c5b609a5fa628c2645bdd1b56018ee38cb2caa8d1c(
    value: typing.Optional[VaultClusterAuditLogConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a47be8c3817c70555bc777416f18db7e158d5f4a408d5a70bef49dc6666cf0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_id: builtins.str,
    hvn_id: builtins.str,
    audit_log_config: typing.Optional[typing.Union[VaultClusterAuditLogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    major_version_upgrade_config: typing.Optional[typing.Union[VaultClusterMajorVersionUpgradeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    metrics_config: typing.Optional[typing.Union[VaultClusterMetricsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    min_vault_version: typing.Optional[builtins.str] = None,
    paths_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    primary_link: typing.Optional[builtins.str] = None,
    public_endpoint: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tier: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[VaultClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4962f49b844cabab740d8df01f3b70a715d3f1306b60fec54b6272426400d44(
    *,
    upgrade_type: builtins.str,
    maintenance_window_day: typing.Optional[builtins.str] = None,
    maintenance_window_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00220fe9e0d944a01da3073321aa1195a8785491ef20ede83c5c9e60456cfccc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731c8b0a131354c50c4187c419df1ca0b4ceae942541b703dccc29bddc2ae24d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f434d7fee16e563e0a028d6996e7baa865d83d6283058a983dd31e012a5ee7d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__985cbace5e3cd0b9202218537c218691890d235d32455d4d255ad4bdb2d63fe6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73923462dd4285e4699c6c87591575ddc937cd2eac326dd6c048a6d19e1d13e1(
    value: typing.Optional[VaultClusterMajorVersionUpgradeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41328d9c30b2160db3534c4e47502c0f13855650febdfb88b239dcb6d6ee814(
    *,
    datadog_api_key: typing.Optional[builtins.str] = None,
    datadog_region: typing.Optional[builtins.str] = None,
    grafana_endpoint: typing.Optional[builtins.str] = None,
    grafana_password: typing.Optional[builtins.str] = None,
    grafana_user: typing.Optional[builtins.str] = None,
    splunk_hecendpoint: typing.Optional[builtins.str] = None,
    splunk_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7573747a2312afa8ffc8dafc01025857a8dc813746d0e47c1ba6fbbe8778ac35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01774f33baeaf10f919c131dc102f79f36eeff62b05d905990090cc7a031f8a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53493b753297becfad9e332d6d76bf38108bc351b6b3e20baddb9bb07893b458(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae544b6a716e103200c258e30bdeecaffec6121c50d96449de5d9b48fbbc24c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1064d1abe056bb9b3eb383bd3d0f5cb018fb61bf6744005bc22fc06f26bca5cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc49e4808e51cb5e796669e09cca32630adbb4539a73b19a0900c53fcf47a3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3d1fedf5a113300f4ff7aff7390f5a7677acca337373f048c07ca807be7bd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41262da7c69a34522658c9a64fb97b513270eab90b33134705d21e460bf4bf7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2bf482f44b38423d4061abe71c12776c465cb81d41e5ec0fd2fd93519e289f(
    value: typing.Optional[VaultClusterMetricsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ee5e56e863fb68b056cf0c52c11694127fd2447b2109705c1c013124bc122b(
    *,
    create: typing.Optional[builtins.str] = None,
    default: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ecdf217b4bc03cba984541a801600b2d5439419fe5d42ba40ff7ac32ec3333(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2c8ee9a177a1817b11e58fd9878424e1054d355e3bcb7b746bbe30fa3cbc2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87e66bf7ba09872850753eb0320a0428faf4ccd45ba0b681c88af537cb66fbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b560841a2a171c6555944671bf203111462c74d3d57852b50f20076467171e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__507fb6faf5cecc7fb6c63feaca0dae7ff5b1a3150654d705aecead89ab25793c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc0b876897d7750cc1f48d98ef8fac9b2418b3c42aad84f70d54d171bb85f4a(
    value: typing.Optional[typing.Union[VaultClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
