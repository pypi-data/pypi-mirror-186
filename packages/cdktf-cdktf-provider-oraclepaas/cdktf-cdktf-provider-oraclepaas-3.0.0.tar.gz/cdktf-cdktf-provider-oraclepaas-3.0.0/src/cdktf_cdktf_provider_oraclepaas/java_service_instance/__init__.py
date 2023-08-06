'''
# `oraclepaas_java_service_instance`

Refer to the Terraform Registory for docs: [`oraclepaas_java_service_instance`](https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance).
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


class JavaServiceInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance oraclepaas_java_service_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        backups: typing.Union["JavaServiceInstanceBackups", typing.Dict[builtins.str, typing.Any]],
        edition: builtins.str,
        name: builtins.str,
        ssh_public_key: builtins.str,
        weblogic_server: typing.Union["JavaServiceInstanceWeblogicServer", typing.Dict[builtins.str, typing.Any]],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        enable_admin_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        level: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union["JavaServiceInstanceLoadBalancer", typing.Dict[builtins.str, typing.Any]]] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        oracle_traffic_director: typing.Optional[typing.Union["JavaServiceInstanceOracleTrafficDirector", typing.Dict[builtins.str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        service_version: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["JavaServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_identity_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance oraclepaas_java_service_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backups JavaServiceInstance#backups}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#edition JavaServiceInstance#edition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ssh_public_key JavaServiceInstance#ssh_public_key}.
        :param weblogic_server: weblogic_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#weblogic_server JavaServiceInstance#weblogic_server}
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#assign_public_ip JavaServiceInstance#assign_public_ip}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#availability_domain JavaServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_destination JavaServiceInstance#backup_destination}.
        :param bring_your_own_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#bring_your_own_license JavaServiceInstance#bring_your_own_license}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#description JavaServiceInstance#description}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#desired_state JavaServiceInstance#desired_state}.
        :param enable_admin_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#enable_admin_console JavaServiceInstance#enable_admin_console}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#force_delete JavaServiceInstance#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#id JavaServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_network JavaServiceInstance#ip_network}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#level JavaServiceInstance#level}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancer JavaServiceInstance#load_balancer}
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#metering_frequency JavaServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#notification_email JavaServiceInstance#notification_email}.
        :param oracle_traffic_director: oracle_traffic_director block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#oracle_traffic_director JavaServiceInstance#oracle_traffic_director}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#region JavaServiceInstance#region}.
        :param service_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#service_version JavaServiceInstance#service_version}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#snapshot_name JavaServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#source_service_name JavaServiceInstance#source_service_name}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnet JavaServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#timeouts JavaServiceInstance#timeouts}
        :param use_identity_service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_identity_service JavaServiceInstance#use_identity_service}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabaa8d63d8bfa48d610b109cf1a794e0b7155bfdd9acd93ebf64e606464fd09)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = JavaServiceInstanceConfig(
            backups=backups,
            edition=edition,
            name=name,
            ssh_public_key=ssh_public_key,
            weblogic_server=weblogic_server,
            assign_public_ip=assign_public_ip,
            availability_domain=availability_domain,
            backup_destination=backup_destination,
            bring_your_own_license=bring_your_own_license,
            description=description,
            desired_state=desired_state,
            enable_admin_console=enable_admin_console,
            force_delete=force_delete,
            id=id,
            ip_network=ip_network,
            level=level,
            load_balancer=load_balancer,
            metering_frequency=metering_frequency,
            notification_email=notification_email,
            oracle_traffic_director=oracle_traffic_director,
            region=region,
            service_version=service_version,
            snapshot_name=snapshot_name,
            source_service_name=source_service_name,
            subnet=subnet,
            timeouts=timeouts,
            use_identity_service=use_identity_service,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackups")
    def put_backups(
        self,
        *,
        cloud_storage_container: builtins.str,
        auto_generate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        use_oauth_for_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_container JavaServiceInstance#cloud_storage_container}.
        :param auto_generate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#auto_generate JavaServiceInstance#auto_generate}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_password JavaServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_username JavaServiceInstance#cloud_storage_username}.
        :param use_oauth_for_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_oauth_for_storage JavaServiceInstance#use_oauth_for_storage}.
        '''
        value = JavaServiceInstanceBackups(
            cloud_storage_container=cloud_storage_container,
            auto_generate=auto_generate,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
            use_oauth_for_storage=use_oauth_for_storage,
        )

        return typing.cast(None, jsii.invoke(self, "putBackups", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        *,
        load_balancing_policy: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param load_balancing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnets JavaServiceInstance#subnets}.
        '''
        value = JavaServiceInstanceLoadBalancer(
            load_balancing_policy=load_balancing_policy, subnets=subnets
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putOracleTrafficDirector")
    def put_oracle_traffic_director(
        self,
        *,
        admin: typing.Union["JavaServiceInstanceOracleTrafficDirectorAdmin", typing.Dict[builtins.str, typing.Any]],
        shape: builtins.str,
        high_availability: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        listener: typing.Optional[typing.Union["JavaServiceInstanceOracleTrafficDirectorListener", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: admin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.
        :param high_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#high_availability JavaServiceInstance#high_availability}.
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#listener JavaServiceInstance#listener}
        :param load_balancing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.
        '''
        value = JavaServiceInstanceOracleTrafficDirector(
            admin=admin,
            shape=shape,
            high_availability=high_availability,
            ip_reservations=ip_reservations,
            listener=listener,
            load_balancing_policy=load_balancing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putOracleTrafficDirector", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#create JavaServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#delete JavaServiceInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#update JavaServiceInstance#update}.
        '''
        value = JavaServiceInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWeblogicServer")
    def put_weblogic_server(
        self,
        *,
        admin: typing.Union["JavaServiceInstanceWeblogicServerAdmin", typing.Dict[builtins.str, typing.Any]],
        database: typing.Union["JavaServiceInstanceWeblogicServerDatabase", typing.Dict[builtins.str, typing.Any]],
        shape: builtins.str,
        application_database: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["JavaServiceInstanceWeblogicServerApplicationDatabase", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backup_volume_size: typing.Optional[builtins.str] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["JavaServiceInstanceWeblogicServerCluster", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        connect_string: typing.Optional[builtins.str] = None,
        domain: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerDomain", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_servers: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerManagedServers", typing.Dict[builtins.str, typing.Any]]] = None,
        middleware_volume_size: typing.Optional[builtins.str] = None,
        node_manager: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerNodeManager", typing.Dict[builtins.str, typing.Any]]] = None,
        ports: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerPorts", typing.Dict[builtins.str, typing.Any]]] = None,
        upper_stack_product_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: admin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#database JavaServiceInstance#database}
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.
        :param application_database: application_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#application_database JavaServiceInstance#application_database}
        :param backup_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_volume_size JavaServiceInstance#backup_volume_size}.
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster JavaServiceInstance#cluster}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster_name JavaServiceInstance#cluster_name}.
        :param connect_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#connect_string JavaServiceInstance#connect_string}.
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#domain JavaServiceInstance#domain}
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.
        :param managed_servers: managed_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#managed_servers JavaServiceInstance#managed_servers}
        :param middleware_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#middleware_volume_size JavaServiceInstance#middleware_volume_size}.
        :param node_manager: node_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#node_manager JavaServiceInstance#node_manager}
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ports JavaServiceInstance#ports}
        :param upper_stack_product_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#upper_stack_product_name JavaServiceInstance#upper_stack_product_name}.
        '''
        value = JavaServiceInstanceWeblogicServer(
            admin=admin,
            database=database,
            shape=shape,
            application_database=application_database,
            backup_volume_size=backup_volume_size,
            cluster=cluster,
            cluster_name=cluster_name,
            connect_string=connect_string,
            domain=domain,
            ip_reservations=ip_reservations,
            managed_servers=managed_servers,
            middleware_volume_size=middleware_volume_size,
            node_manager=node_manager,
            ports=ports,
            upper_stack_product_name=upper_stack_product_name,
        )

        return typing.cast(None, jsii.invoke(self, "putWeblogicServer", [value]))

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetAvailabilityDomain")
    def reset_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityDomain", []))

    @jsii.member(jsii_name="resetBackupDestination")
    def reset_backup_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupDestination", []))

    @jsii.member(jsii_name="resetBringYourOwnLicense")
    def reset_bring_your_own_license(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBringYourOwnLicense", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetEnableAdminConsole")
    def reset_enable_admin_console(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAdminConsole", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetLevel")
    def reset_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevel", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetMeteringFrequency")
    def reset_metering_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeteringFrequency", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetOracleTrafficDirector")
    def reset_oracle_traffic_director(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOracleTrafficDirector", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetServiceVersion")
    def reset_service_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceVersion", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @jsii.member(jsii_name="resetSourceServiceName")
    def reset_source_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServiceName", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseIdentityService")
    def reset_use_identity_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseIdentityService", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backups")
    def backups(self) -> "JavaServiceInstanceBackupsOutputReference":
        return typing.cast("JavaServiceInstanceBackupsOutputReference", jsii.get(self, "backups"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "JavaServiceInstanceLoadBalancerOutputReference":
        return typing.cast("JavaServiceInstanceLoadBalancerOutputReference", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="oracleTrafficDirector")
    def oracle_traffic_director(
        self,
    ) -> "JavaServiceInstanceOracleTrafficDirectorOutputReference":
        return typing.cast("JavaServiceInstanceOracleTrafficDirectorOutputReference", jsii.get(self, "oracleTrafficDirector"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "JavaServiceInstanceTimeoutsOutputReference":
        return typing.cast("JavaServiceInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="weblogicServer")
    def weblogic_server(self) -> "JavaServiceInstanceWeblogicServerOutputReference":
        return typing.cast("JavaServiceInstanceWeblogicServerOutputReference", jsii.get(self, "weblogicServer"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomainInput")
    def availability_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="backupDestinationInput")
    def backup_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="backupsInput")
    def backups_input(self) -> typing.Optional["JavaServiceInstanceBackups"]:
        return typing.cast(typing.Optional["JavaServiceInstanceBackups"], jsii.get(self, "backupsInput"))

    @builtins.property
    @jsii.member(jsii_name="bringYourOwnLicenseInput")
    def bring_your_own_license_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bringYourOwnLicenseInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="editionInput")
    def edition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "editionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAdminConsoleInput")
    def enable_admin_console_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableAdminConsoleInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(self) -> typing.Optional["JavaServiceInstanceLoadBalancer"]:
        return typing.cast(typing.Optional["JavaServiceInstanceLoadBalancer"], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="meteringFrequencyInput")
    def metering_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meteringFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailInput")
    def notification_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="oracleTrafficDirectorInput")
    def oracle_traffic_director_input(
        self,
    ) -> typing.Optional["JavaServiceInstanceOracleTrafficDirector"]:
        return typing.cast(typing.Optional["JavaServiceInstanceOracleTrafficDirector"], jsii.get(self, "oracleTrafficDirectorInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceVersionInput")
    def service_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceNameInput")
    def source_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["JavaServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["JavaServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useIdentityServiceInput")
    def use_identity_service_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useIdentityServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="weblogicServerInput")
    def weblogic_server_input(
        self,
    ) -> typing.Optional["JavaServiceInstanceWeblogicServer"]:
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServer"], jsii.get(self, "weblogicServerInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793da1444972870a524b7a324275f3fb60e6049132b376000ec6c85012fc2413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__385ad1fa5328324f4e330d9f55e2bad7ac6ed124b4d1a33a9aaadb148cbb4eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="backupDestination")
    def backup_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupDestination"))

    @backup_destination.setter
    def backup_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c10a71f2f534d55693735285d03a77ae625fdd63c58b30a84bb9b4a00b2988d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupDestination", value)

    @builtins.property
    @jsii.member(jsii_name="bringYourOwnLicense")
    def bring_your_own_license(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "bringYourOwnLicense"))

    @bring_your_own_license.setter
    def bring_your_own_license(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c5b4048b4d1e0d4ae39c3c02d7a1529390ec05b43b4a348464a1df8e62ff75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bringYourOwnLicense", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e67021477161ed1405801bae819b96c7131439c5be82dadde70ad3589f42752c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645e2899c3f55c9a954fb930143330453b981e388f2d2fd4f233750c07aba252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00626e08b2b9465d6103fa08e0d423aad2f0a26df16c6ffd6cf1ae68540432f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="enableAdminConsole")
    def enable_admin_console(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableAdminConsole"))

    @enable_admin_console.setter
    def enable_admin_console(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06539b6dc5ece6c7df7063982e6466e13f0cec73ade0af8761ae08f6c61ea992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAdminConsole", value)

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a55bac0e774be3ab1ba30b0156e098ea2c4de0631008a88a92169330f6bff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034dd1f9ca6cd04ba06198c7e3078f515c16d1fc68becbae66b2d3fad2b8b3c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19156f9656de4519fcec624c9371106851efaa31ab2cca4f005f0bd71a25c06c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb0a1d986020e314ac5e3f6ded6abd0b340e0e1689d216abd46d2a2fe6141b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="meteringFrequency")
    def metering_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meteringFrequency"))

    @metering_frequency.setter
    def metering_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b72bbbb8d30b6a8c271cfe0600aa8059f3630acfcb6d620b037832491e0d67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meteringFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac459b4a1ef41e0f4ba520b4929080b6ce73620ae92e9a69439d3a77bc3fac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f8d4745d920dc20f1c8aea2453edd67ec41c4165fdfcf05fa896516f697519)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381f6bb0a5f593e3b947962f9a64909c72e2c401218372bda6f38f734bd008bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="serviceVersion")
    def service_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceVersion"))

    @service_version.setter
    def service_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25049a015c51496742187cdc336986d5b981d3890af99fd88e3099d0cec1f80a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceVersion", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21012e9f8e87447dd9207fd2205bc944f51f92c489f78216f54a528ecfd20137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServiceName")
    def source_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceServiceName"))

    @source_service_name.setter
    def source_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__065b2aea37b103ca29393581e2d4a82180327f014ff54b54ff3842123f6826d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63839f69260fdc7642656fd7bcf840232149978b32c91858c30040ba2694a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeef8d7f3473c6d8ab733f0b86cd2b1d3342b42934225c34beeae5c9cf12d8a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="useIdentityService")
    def use_identity_service(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useIdentityService"))

    @use_identity_service.setter
    def use_identity_service(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c481dbd0b4f253458b5b9bcffe44277827a599b09397109e824934b5252efeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useIdentityService", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceBackups",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "auto_generate": "autoGenerate",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
        "use_oauth_for_storage": "useOauthForStorage",
    },
)
class JavaServiceInstanceBackups:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        auto_generate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        use_oauth_for_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_container JavaServiceInstance#cloud_storage_container}.
        :param auto_generate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#auto_generate JavaServiceInstance#auto_generate}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_password JavaServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_username JavaServiceInstance#cloud_storage_username}.
        :param use_oauth_for_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_oauth_for_storage JavaServiceInstance#use_oauth_for_storage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f6c05a8bec21891b9600aac743922bb5c17839465c85d3e9171f9651f91dd3)
            check_type(argname="argument cloud_storage_container", value=cloud_storage_container, expected_type=type_hints["cloud_storage_container"])
            check_type(argname="argument auto_generate", value=auto_generate, expected_type=type_hints["auto_generate"])
            check_type(argname="argument cloud_storage_password", value=cloud_storage_password, expected_type=type_hints["cloud_storage_password"])
            check_type(argname="argument cloud_storage_username", value=cloud_storage_username, expected_type=type_hints["cloud_storage_username"])
            check_type(argname="argument use_oauth_for_storage", value=use_oauth_for_storage, expected_type=type_hints["use_oauth_for_storage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_storage_container": cloud_storage_container,
        }
        if auto_generate is not None:
            self._values["auto_generate"] = auto_generate
        if cloud_storage_password is not None:
            self._values["cloud_storage_password"] = cloud_storage_password
        if cloud_storage_username is not None:
            self._values["cloud_storage_username"] = cloud_storage_username
        if use_oauth_for_storage is not None:
            self._values["use_oauth_for_storage"] = use_oauth_for_storage

    @builtins.property
    def cloud_storage_container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_container JavaServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_generate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#auto_generate JavaServiceInstance#auto_generate}.'''
        result = self._values.get("auto_generate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_password JavaServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cloud_storage_username JavaServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_oauth_for_storage(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_oauth_for_storage JavaServiceInstance#use_oauth_for_storage}.'''
        result = self._values.get("use_oauth_for_storage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceBackups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceBackupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceBackupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf9e2209bf9fa5dff23c27822b7cfdbe7cc1fb66bb0ae9802832d7b21f03aef4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoGenerate")
    def reset_auto_generate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoGenerate", []))

    @jsii.member(jsii_name="resetCloudStoragePassword")
    def reset_cloud_storage_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePassword", []))

    @jsii.member(jsii_name="resetCloudStorageUsername")
    def reset_cloud_storage_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageUsername", []))

    @jsii.member(jsii_name="resetUseOauthForStorage")
    def reset_use_oauth_for_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseOauthForStorage", []))

    @builtins.property
    @jsii.member(jsii_name="autoGenerateInput")
    def auto_generate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoGenerateInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainerInput")
    def cloud_storage_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStorageContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePasswordInput")
    def cloud_storage_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStoragePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsernameInput")
    def cloud_storage_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudStorageUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="useOauthForStorageInput")
    def use_oauth_for_storage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useOauthForStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="autoGenerate")
    def auto_generate(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoGenerate"))

    @auto_generate.setter
    def auto_generate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c9ba7a7ecaafc3d58081aa9b171f9ad1cd5c3e00b813b1a78c791a889db42c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoGenerate", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @cloud_storage_container.setter
    def cloud_storage_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9d1e684a0e0445cd27c0127a18b525e3ab8a00f6cb518e57e2bd3dfb80757c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333c8bece7b9f1592ce0782eaf33f6640dafda4ed41da97eafd64d3109553942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a75adaf51b666217e54a234dab093f5091ba0e8a15504a54a1302a2124f0cfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageUsername", value)

    @builtins.property
    @jsii.member(jsii_name="useOauthForStorage")
    def use_oauth_for_storage(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useOauthForStorage"))

    @use_oauth_for_storage.setter
    def use_oauth_for_storage(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d6b8d92a250aa95b2983246d96e2e1b759278f9839fef6e724370c7fc29364a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useOauthForStorage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JavaServiceInstanceBackups]:
        return typing.cast(typing.Optional[JavaServiceInstanceBackups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceBackups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a9e7853e3ba752a35437b4a3745123b47a980fc512b854af925cf251a6d33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backups": "backups",
        "edition": "edition",
        "name": "name",
        "ssh_public_key": "sshPublicKey",
        "weblogic_server": "weblogicServer",
        "assign_public_ip": "assignPublicIp",
        "availability_domain": "availabilityDomain",
        "backup_destination": "backupDestination",
        "bring_your_own_license": "bringYourOwnLicense",
        "description": "description",
        "desired_state": "desiredState",
        "enable_admin_console": "enableAdminConsole",
        "force_delete": "forceDelete",
        "id": "id",
        "ip_network": "ipNetwork",
        "level": "level",
        "load_balancer": "loadBalancer",
        "metering_frequency": "meteringFrequency",
        "notification_email": "notificationEmail",
        "oracle_traffic_director": "oracleTrafficDirector",
        "region": "region",
        "service_version": "serviceVersion",
        "snapshot_name": "snapshotName",
        "source_service_name": "sourceServiceName",
        "subnet": "subnet",
        "timeouts": "timeouts",
        "use_identity_service": "useIdentityService",
    },
)
class JavaServiceInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        backups: typing.Union[JavaServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]],
        edition: builtins.str,
        name: builtins.str,
        ssh_public_key: builtins.str,
        weblogic_server: typing.Union["JavaServiceInstanceWeblogicServer", typing.Dict[builtins.str, typing.Any]],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        enable_admin_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        level: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union["JavaServiceInstanceLoadBalancer", typing.Dict[builtins.str, typing.Any]]] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        oracle_traffic_director: typing.Optional[typing.Union["JavaServiceInstanceOracleTrafficDirector", typing.Dict[builtins.str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        service_version: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["JavaServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        use_identity_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backups JavaServiceInstance#backups}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#edition JavaServiceInstance#edition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ssh_public_key JavaServiceInstance#ssh_public_key}.
        :param weblogic_server: weblogic_server block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#weblogic_server JavaServiceInstance#weblogic_server}
        :param assign_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#assign_public_ip JavaServiceInstance#assign_public_ip}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#availability_domain JavaServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_destination JavaServiceInstance#backup_destination}.
        :param bring_your_own_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#bring_your_own_license JavaServiceInstance#bring_your_own_license}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#description JavaServiceInstance#description}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#desired_state JavaServiceInstance#desired_state}.
        :param enable_admin_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#enable_admin_console JavaServiceInstance#enable_admin_console}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#force_delete JavaServiceInstance#force_delete}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#id JavaServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_network JavaServiceInstance#ip_network}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#level JavaServiceInstance#level}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancer JavaServiceInstance#load_balancer}
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#metering_frequency JavaServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#notification_email JavaServiceInstance#notification_email}.
        :param oracle_traffic_director: oracle_traffic_director block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#oracle_traffic_director JavaServiceInstance#oracle_traffic_director}
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#region JavaServiceInstance#region}.
        :param service_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#service_version JavaServiceInstance#service_version}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#snapshot_name JavaServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#source_service_name JavaServiceInstance#source_service_name}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnet JavaServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#timeouts JavaServiceInstance#timeouts}
        :param use_identity_service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_identity_service JavaServiceInstance#use_identity_service}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(backups, dict):
            backups = JavaServiceInstanceBackups(**backups)
        if isinstance(weblogic_server, dict):
            weblogic_server = JavaServiceInstanceWeblogicServer(**weblogic_server)
        if isinstance(load_balancer, dict):
            load_balancer = JavaServiceInstanceLoadBalancer(**load_balancer)
        if isinstance(oracle_traffic_director, dict):
            oracle_traffic_director = JavaServiceInstanceOracleTrafficDirector(**oracle_traffic_director)
        if isinstance(timeouts, dict):
            timeouts = JavaServiceInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2721257bc94fb239084b135f2ee28509955ba4420427c43ed3a5610fcd4ea787)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backups", value=backups, expected_type=type_hints["backups"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument weblogic_server", value=weblogic_server, expected_type=type_hints["weblogic_server"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument backup_destination", value=backup_destination, expected_type=type_hints["backup_destination"])
            check_type(argname="argument bring_your_own_license", value=bring_your_own_license, expected_type=type_hints["bring_your_own_license"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument enable_admin_console", value=enable_admin_console, expected_type=type_hints["enable_admin_console"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument metering_frequency", value=metering_frequency, expected_type=type_hints["metering_frequency"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument oracle_traffic_director", value=oracle_traffic_director, expected_type=type_hints["oracle_traffic_director"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service_version", value=service_version, expected_type=type_hints["service_version"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument source_service_name", value=source_service_name, expected_type=type_hints["source_service_name"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_identity_service", value=use_identity_service, expected_type=type_hints["use_identity_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backups": backups,
            "edition": edition,
            "name": name,
            "ssh_public_key": ssh_public_key,
            "weblogic_server": weblogic_server,
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
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if availability_domain is not None:
            self._values["availability_domain"] = availability_domain
        if backup_destination is not None:
            self._values["backup_destination"] = backup_destination
        if bring_your_own_license is not None:
            self._values["bring_your_own_license"] = bring_your_own_license
        if description is not None:
            self._values["description"] = description
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if enable_admin_console is not None:
            self._values["enable_admin_console"] = enable_admin_console
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if id is not None:
            self._values["id"] = id
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if level is not None:
            self._values["level"] = level
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if metering_frequency is not None:
            self._values["metering_frequency"] = metering_frequency
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if oracle_traffic_director is not None:
            self._values["oracle_traffic_director"] = oracle_traffic_director
        if region is not None:
            self._values["region"] = region
        if service_version is not None:
            self._values["service_version"] = service_version
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if source_service_name is not None:
            self._values["source_service_name"] = source_service_name
        if subnet is not None:
            self._values["subnet"] = subnet
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_identity_service is not None:
            self._values["use_identity_service"] = use_identity_service

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
    def backups(self) -> JavaServiceInstanceBackups:
        '''backups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backups JavaServiceInstance#backups}
        '''
        result = self._values.get("backups")
        assert result is not None, "Required property 'backups' is missing"
        return typing.cast(JavaServiceInstanceBackups, result)

    @builtins.property
    def edition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#edition JavaServiceInstance#edition}.'''
        result = self._values.get("edition")
        assert result is not None, "Required property 'edition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ssh_public_key JavaServiceInstance#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        assert result is not None, "Required property 'ssh_public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weblogic_server(self) -> "JavaServiceInstanceWeblogicServer":
        '''weblogic_server block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#weblogic_server JavaServiceInstance#weblogic_server}
        '''
        result = self._values.get("weblogic_server")
        assert result is not None, "Required property 'weblogic_server' is missing"
        return typing.cast("JavaServiceInstanceWeblogicServer", result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#assign_public_ip JavaServiceInstance#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def availability_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#availability_domain JavaServiceInstance#availability_domain}.'''
        result = self._values.get("availability_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_destination JavaServiceInstance#backup_destination}.'''
        result = self._values.get("backup_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bring_your_own_license(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#bring_your_own_license JavaServiceInstance#bring_your_own_license}.'''
        result = self._values.get("bring_your_own_license")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#description JavaServiceInstance#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#desired_state JavaServiceInstance#desired_state}.'''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_admin_console(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#enable_admin_console JavaServiceInstance#enable_admin_console}.'''
        result = self._values.get("enable_admin_console")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#force_delete JavaServiceInstance#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#id JavaServiceInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_network JavaServiceInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#level JavaServiceInstance#level}.'''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(self) -> typing.Optional["JavaServiceInstanceLoadBalancer"]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancer JavaServiceInstance#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["JavaServiceInstanceLoadBalancer"], result)

    @builtins.property
    def metering_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#metering_frequency JavaServiceInstance#metering_frequency}.'''
        result = self._values.get("metering_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#notification_email JavaServiceInstance#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oracle_traffic_director(
        self,
    ) -> typing.Optional["JavaServiceInstanceOracleTrafficDirector"]:
        '''oracle_traffic_director block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#oracle_traffic_director JavaServiceInstance#oracle_traffic_director}
        '''
        result = self._values.get("oracle_traffic_director")
        return typing.cast(typing.Optional["JavaServiceInstanceOracleTrafficDirector"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#region JavaServiceInstance#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#service_version JavaServiceInstance#service_version}.'''
        result = self._values.get("service_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#snapshot_name JavaServiceInstance#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#source_service_name JavaServiceInstance#source_service_name}.'''
        result = self._values.get("source_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnet JavaServiceInstance#subnet}.'''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["JavaServiceInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#timeouts JavaServiceInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["JavaServiceInstanceTimeouts"], result)

    @builtins.property
    def use_identity_service(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#use_identity_service JavaServiceInstance#use_identity_service}.'''
        result = self._values.get("use_identity_service")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "load_balancing_policy": "loadBalancingPolicy",
        "subnets": "subnets",
    },
)
class JavaServiceInstanceLoadBalancer:
    def __init__(
        self,
        *,
        load_balancing_policy: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param load_balancing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.
        :param subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnets JavaServiceInstance#subnets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5bf32d8c3e02e924d2a38974378b29de1adb964676470763787dac059f8a90f)
            check_type(argname="argument load_balancing_policy", value=load_balancing_policy, expected_type=type_hints["load_balancing_policy"])
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if load_balancing_policy is not None:
            self._values["load_balancing_policy"] = load_balancing_policy
        if subnets is not None:
            self._values["subnets"] = subnets

    @builtins.property
    def load_balancing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.'''
        result = self._values.get("load_balancing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#subnets JavaServiceInstance#subnets}.'''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceLoadBalancerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8df6c27eae8014a4fdf82cef9ad676bc7de372fc64d37f2b001948b10a035e18)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLoadBalancingPolicy")
    def reset_load_balancing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingPolicy", []))

    @jsii.member(jsii_name="resetSubnets")
    def reset_subnets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnets", []))

    @builtins.property
    @jsii.member(jsii_name="adminUrl")
    def admin_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUrl"))

    @builtins.property
    @jsii.member(jsii_name="consoleUrl")
    def console_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consoleUrl"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingPolicyInput")
    def load_balancing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingPolicy")
    def load_balancing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingPolicy"))

    @load_balancing_policy.setter
    def load_balancing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e688780ffd50cf1fee7a447a98cabe7b2b9560183180cdb55d0d44f23200378b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a1d0d5c774f85d4ae8898fe4a7344778776fe24faa840e24d5253c9866471f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JavaServiceInstanceLoadBalancer]:
        return typing.cast(typing.Optional[JavaServiceInstanceLoadBalancer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceLoadBalancer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0191dc24bcae2450bf72a437583a9682a6496aa78d4446563a15e67f43c8e57c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirector",
    jsii_struct_bases=[],
    name_mapping={
        "admin": "admin",
        "shape": "shape",
        "high_availability": "highAvailability",
        "ip_reservations": "ipReservations",
        "listener": "listener",
        "load_balancing_policy": "loadBalancingPolicy",
    },
)
class JavaServiceInstanceOracleTrafficDirector:
    def __init__(
        self,
        *,
        admin: typing.Union["JavaServiceInstanceOracleTrafficDirectorAdmin", typing.Dict[builtins.str, typing.Any]],
        shape: builtins.str,
        high_availability: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        listener: typing.Optional[typing.Union["JavaServiceInstanceOracleTrafficDirectorListener", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: admin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.
        :param high_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#high_availability JavaServiceInstance#high_availability}.
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#listener JavaServiceInstance#listener}
        :param load_balancing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.
        '''
        if isinstance(admin, dict):
            admin = JavaServiceInstanceOracleTrafficDirectorAdmin(**admin)
        if isinstance(listener, dict):
            listener = JavaServiceInstanceOracleTrafficDirectorListener(**listener)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a33e8ac66026c5aa851a1946a36667d7f595c2322ba368041d6e43c436ef636)
            check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument high_availability", value=high_availability, expected_type=type_hints["high_availability"])
            check_type(argname="argument ip_reservations", value=ip_reservations, expected_type=type_hints["ip_reservations"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument load_balancing_policy", value=load_balancing_policy, expected_type=type_hints["load_balancing_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin": admin,
            "shape": shape,
        }
        if high_availability is not None:
            self._values["high_availability"] = high_availability
        if ip_reservations is not None:
            self._values["ip_reservations"] = ip_reservations
        if listener is not None:
            self._values["listener"] = listener
        if load_balancing_policy is not None:
            self._values["load_balancing_policy"] = load_balancing_policy

    @builtins.property
    def admin(self) -> "JavaServiceInstanceOracleTrafficDirectorAdmin":
        '''admin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        '''
        result = self._values.get("admin")
        assert result is not None, "Required property 'admin' is missing"
        return typing.cast("JavaServiceInstanceOracleTrafficDirectorAdmin", result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def high_availability(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#high_availability JavaServiceInstance#high_availability}.'''
        result = self._values.get("high_availability")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ip_reservations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.'''
        result = self._values.get("ip_reservations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def listener(
        self,
    ) -> typing.Optional["JavaServiceInstanceOracleTrafficDirectorListener"]:
        '''listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#listener JavaServiceInstance#listener}
        '''
        result = self._values.get("listener")
        return typing.cast(typing.Optional["JavaServiceInstanceOracleTrafficDirectorListener"], result)

    @builtins.property
    def load_balancing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#load_balancing_policy JavaServiceInstance#load_balancing_policy}.'''
        result = self._values.get("load_balancing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceOracleTrafficDirector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirectorAdmin",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username", "port": "port"},
)
class JavaServiceInstanceOracleTrafficDirectorAdmin:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__241c30e605280a55e9c8a8f7b5bec2d8ffdb017026cfd580445e4d67c4d1492f)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceOracleTrafficDirectorAdmin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceOracleTrafficDirectorAdminOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirectorAdminOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc2d0ddd158a8d83a60d3ebcd66cc53f1237c1256a7aaac34c7d751cfe600300)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4bb83a9b6d9663c8e2dc69e0bd6eb45201993accc9e6f4bad98f2c0a8259620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c54b3a1c316f74f3f9e867b26186f043eeb6458711c6ebfafa96932d393a01b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b3d2887892314781a29681beb037c2fa87bfb6da067629200d5db66f2bf2aab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin]:
        return typing.cast(typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__378313e723c9c1749a1d50c6b40bc0e62b21135eb5eadfe89138d593dfa13dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirectorListener",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "privileged_port": "privilegedPort",
        "privileged_secured_port": "privilegedSecuredPort",
        "secured_port": "securedPort",
    },
)
class JavaServiceInstanceOracleTrafficDirectorListener:
    def __init__(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        privileged_port: typing.Optional[jsii.Number] = None,
        privileged_secured_port: typing.Optional[jsii.Number] = None,
        secured_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param privileged_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_port JavaServiceInstance#privileged_port}.
        :param privileged_secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_port JavaServiceInstance#privileged_secured_port}.
        :param secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905fef95f4809369728b6d7409444cc1e8ddd0fdcb8aa22fb833493a5f541d1e)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument privileged_port", value=privileged_port, expected_type=type_hints["privileged_port"])
            check_type(argname="argument privileged_secured_port", value=privileged_secured_port, expected_type=type_hints["privileged_secured_port"])
            check_type(argname="argument secured_port", value=secured_port, expected_type=type_hints["secured_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if privileged_port is not None:
            self._values["privileged_port"] = privileged_port
        if privileged_secured_port is not None:
            self._values["privileged_secured_port"] = privileged_secured_port
        if secured_port is not None:
            self._values["secured_port"] = secured_port

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_port JavaServiceInstance#privileged_port}.'''
        result = self._values.get("privileged_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged_secured_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_port JavaServiceInstance#privileged_secured_port}.'''
        result = self._values.get("privileged_secured_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def secured_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.'''
        result = self._values.get("secured_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceOracleTrafficDirectorListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceOracleTrafficDirectorListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirectorListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f497ac65a1ec8e610a188f56f411c8f1dba509d88969b86161ff34559ccff800)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPrivilegedPort")
    def reset_privileged_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedPort", []))

    @jsii.member(jsii_name="resetPrivilegedSecuredPort")
    def reset_privileged_secured_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedSecuredPort", []))

    @jsii.member(jsii_name="resetSecuredPort")
    def reset_secured_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecuredPort", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedPortInput")
    def privileged_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privilegedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedSecuredPortInput")
    def privileged_secured_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privilegedSecuredPortInput"))

    @builtins.property
    @jsii.member(jsii_name="securedPortInput")
    def secured_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "securedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98529e32ef3fe27fad168569a3453d682a70b2ea1a506a814e2ae7b229a2df2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedPort")
    def privileged_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privilegedPort"))

    @privileged_port.setter
    def privileged_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe576da923b117b018adf5af440cadca663f3b91988c18da2b8c91ecd5566055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedPort", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedSecuredPort")
    def privileged_secured_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privilegedSecuredPort"))

    @privileged_secured_port.setter
    def privileged_secured_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1754d626f4a74f86607de53a14f5c3788f3214295369f5a02e673b424819be10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedSecuredPort", value)

    @builtins.property
    @jsii.member(jsii_name="securedPort")
    def secured_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "securedPort"))

    @secured_port.setter
    def secured_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf0e37f2f141a453f34e5b017280e14fd39e5a11005016409771e563610790a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securedPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener]:
        return typing.cast(typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986328944d6d1d678730988bfea044d5c64ec7fa0194dd30e593c17de314ca07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class JavaServiceInstanceOracleTrafficDirectorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceOracleTrafficDirectorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72b170966d200c0021168ec4db55f73165eebcbfa903f6178ee44f17cc605908)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdmin")
    def put_admin(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        '''
        value = JavaServiceInstanceOracleTrafficDirectorAdmin(
            password=password, username=username, port=port
        )

        return typing.cast(None, jsii.invoke(self, "putAdmin", [value]))

    @jsii.member(jsii_name="putListener")
    def put_listener(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        privileged_port: typing.Optional[jsii.Number] = None,
        privileged_secured_port: typing.Optional[jsii.Number] = None,
        secured_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param privileged_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_port JavaServiceInstance#privileged_port}.
        :param privileged_secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_port JavaServiceInstance#privileged_secured_port}.
        :param secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.
        '''
        value = JavaServiceInstanceOracleTrafficDirectorListener(
            port=port,
            privileged_port=privileged_port,
            privileged_secured_port=privileged_secured_port,
            secured_port=secured_port,
        )

        return typing.cast(None, jsii.invoke(self, "putListener", [value]))

    @jsii.member(jsii_name="resetHighAvailability")
    def reset_high_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighAvailability", []))

    @jsii.member(jsii_name="resetIpReservations")
    def reset_ip_reservations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpReservations", []))

    @jsii.member(jsii_name="resetListener")
    def reset_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListener", []))

    @jsii.member(jsii_name="resetLoadBalancingPolicy")
    def reset_load_balancing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="admin")
    def admin(self) -> JavaServiceInstanceOracleTrafficDirectorAdminOutputReference:
        return typing.cast(JavaServiceInstanceOracleTrafficDirectorAdminOutputReference, jsii.get(self, "admin"))

    @builtins.property
    @jsii.member(jsii_name="listener")
    def listener(
        self,
    ) -> JavaServiceInstanceOracleTrafficDirectorListenerOutputReference:
        return typing.cast(JavaServiceInstanceOracleTrafficDirectorListenerOutputReference, jsii.get(self, "listener"))

    @builtins.property
    @jsii.member(jsii_name="rootUrl")
    def root_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootUrl"))

    @builtins.property
    @jsii.member(jsii_name="adminInput")
    def admin_input(
        self,
    ) -> typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin]:
        return typing.cast(typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin], jsii.get(self, "adminInput"))

    @builtins.property
    @jsii.member(jsii_name="highAvailabilityInput")
    def high_availability_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "highAvailabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="ipReservationsInput")
    def ip_reservations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipReservationsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerInput")
    def listener_input(
        self,
    ) -> typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener]:
        return typing.cast(typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener], jsii.get(self, "listenerInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingPolicyInput")
    def load_balancing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="highAvailability")
    def high_availability(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "highAvailability"))

    @high_availability.setter
    def high_availability(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d530b638fb33d96fc587bb96cb52b3ceb9603723482bb36f4486f86950dcac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "highAvailability", value)

    @builtins.property
    @jsii.member(jsii_name="ipReservations")
    def ip_reservations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipReservations"))

    @ip_reservations.setter
    def ip_reservations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e949af69d584595778109b957b5bb874b37065c9454b5f99d9ebb6abad14c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipReservations", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingPolicy")
    def load_balancing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingPolicy"))

    @load_balancing_policy.setter
    def load_balancing_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c866e4eb27715c6ce41c1022369ce57b036b9db29e4032cc49a750197eda81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbe60a4219ead223f39f6653d57036e8b994c33752faf741b610f4e646f001b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceOracleTrafficDirector]:
        return typing.cast(typing.Optional[JavaServiceInstanceOracleTrafficDirector], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceOracleTrafficDirector],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58a8181a1204e3c3a3f33ff5cc821b32c049a19e5e120ba072943c92f9d4aa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class JavaServiceInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#create JavaServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#delete JavaServiceInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#update JavaServiceInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0daa175caee32960484845ad6958623d07e6b526f394a66b70144b8f0393a02)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#create JavaServiceInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#delete JavaServiceInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#update JavaServiceInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__baf105956700cf3212c136440075b6a663c576689fa794fb8d36086a58ba56e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2629733e541ed0480ebfd5317b911303552fb14b79bafcd19374bd1b4ec8e720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a1aeb443a46dd7802a4326fd1b086d4391debb6b48be70f4c3c880cd8a0607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0132c7bf15ed00ffd0538bf146ab01888d6d7c01e0a8aee9f6569e4c982775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[JavaServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[JavaServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[JavaServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6dd3cbedade7ab4b4d3e9a856fc8c247b511dc9b20fe0f62ce2aa18b52fe3ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServer",
    jsii_struct_bases=[],
    name_mapping={
        "admin": "admin",
        "database": "database",
        "shape": "shape",
        "application_database": "applicationDatabase",
        "backup_volume_size": "backupVolumeSize",
        "cluster": "cluster",
        "cluster_name": "clusterName",
        "connect_string": "connectString",
        "domain": "domain",
        "ip_reservations": "ipReservations",
        "managed_servers": "managedServers",
        "middleware_volume_size": "middlewareVolumeSize",
        "node_manager": "nodeManager",
        "ports": "ports",
        "upper_stack_product_name": "upperStackProductName",
    },
)
class JavaServiceInstanceWeblogicServer:
    def __init__(
        self,
        *,
        admin: typing.Union["JavaServiceInstanceWeblogicServerAdmin", typing.Dict[builtins.str, typing.Any]],
        database: typing.Union["JavaServiceInstanceWeblogicServerDatabase", typing.Dict[builtins.str, typing.Any]],
        shape: builtins.str,
        application_database: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["JavaServiceInstanceWeblogicServerApplicationDatabase", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backup_volume_size: typing.Optional[builtins.str] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["JavaServiceInstanceWeblogicServerCluster", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        connect_string: typing.Optional[builtins.str] = None,
        domain: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerDomain", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        managed_servers: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerManagedServers", typing.Dict[builtins.str, typing.Any]]] = None,
        middleware_volume_size: typing.Optional[builtins.str] = None,
        node_manager: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerNodeManager", typing.Dict[builtins.str, typing.Any]]] = None,
        ports: typing.Optional[typing.Union["JavaServiceInstanceWeblogicServerPorts", typing.Dict[builtins.str, typing.Any]]] = None,
        upper_stack_product_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin: admin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#database JavaServiceInstance#database}
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.
        :param application_database: application_database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#application_database JavaServiceInstance#application_database}
        :param backup_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_volume_size JavaServiceInstance#backup_volume_size}.
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster JavaServiceInstance#cluster}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster_name JavaServiceInstance#cluster_name}.
        :param connect_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#connect_string JavaServiceInstance#connect_string}.
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#domain JavaServiceInstance#domain}
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.
        :param managed_servers: managed_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#managed_servers JavaServiceInstance#managed_servers}
        :param middleware_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#middleware_volume_size JavaServiceInstance#middleware_volume_size}.
        :param node_manager: node_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#node_manager JavaServiceInstance#node_manager}
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ports JavaServiceInstance#ports}
        :param upper_stack_product_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#upper_stack_product_name JavaServiceInstance#upper_stack_product_name}.
        '''
        if isinstance(admin, dict):
            admin = JavaServiceInstanceWeblogicServerAdmin(**admin)
        if isinstance(database, dict):
            database = JavaServiceInstanceWeblogicServerDatabase(**database)
        if isinstance(domain, dict):
            domain = JavaServiceInstanceWeblogicServerDomain(**domain)
        if isinstance(managed_servers, dict):
            managed_servers = JavaServiceInstanceWeblogicServerManagedServers(**managed_servers)
        if isinstance(node_manager, dict):
            node_manager = JavaServiceInstanceWeblogicServerNodeManager(**node_manager)
        if isinstance(ports, dict):
            ports = JavaServiceInstanceWeblogicServerPorts(**ports)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9cbebc096f258f93eb3cca77de349f1cfc1c0a4c0624a33c16a249e7b1ac970)
            check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument application_database", value=application_database, expected_type=type_hints["application_database"])
            check_type(argname="argument backup_volume_size", value=backup_volume_size, expected_type=type_hints["backup_volume_size"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument connect_string", value=connect_string, expected_type=type_hints["connect_string"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument ip_reservations", value=ip_reservations, expected_type=type_hints["ip_reservations"])
            check_type(argname="argument managed_servers", value=managed_servers, expected_type=type_hints["managed_servers"])
            check_type(argname="argument middleware_volume_size", value=middleware_volume_size, expected_type=type_hints["middleware_volume_size"])
            check_type(argname="argument node_manager", value=node_manager, expected_type=type_hints["node_manager"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument upper_stack_product_name", value=upper_stack_product_name, expected_type=type_hints["upper_stack_product_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin": admin,
            "database": database,
            "shape": shape,
        }
        if application_database is not None:
            self._values["application_database"] = application_database
        if backup_volume_size is not None:
            self._values["backup_volume_size"] = backup_volume_size
        if cluster is not None:
            self._values["cluster"] = cluster
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if connect_string is not None:
            self._values["connect_string"] = connect_string
        if domain is not None:
            self._values["domain"] = domain
        if ip_reservations is not None:
            self._values["ip_reservations"] = ip_reservations
        if managed_servers is not None:
            self._values["managed_servers"] = managed_servers
        if middleware_volume_size is not None:
            self._values["middleware_volume_size"] = middleware_volume_size
        if node_manager is not None:
            self._values["node_manager"] = node_manager
        if ports is not None:
            self._values["ports"] = ports
        if upper_stack_product_name is not None:
            self._values["upper_stack_product_name"] = upper_stack_product_name

    @builtins.property
    def admin(self) -> "JavaServiceInstanceWeblogicServerAdmin":
        '''admin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#admin JavaServiceInstance#admin}
        '''
        result = self._values.get("admin")
        assert result is not None, "Required property 'admin' is missing"
        return typing.cast("JavaServiceInstanceWeblogicServerAdmin", result)

    @builtins.property
    def database(self) -> "JavaServiceInstanceWeblogicServerDatabase":
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#database JavaServiceInstance#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast("JavaServiceInstanceWeblogicServerDatabase", result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_database(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["JavaServiceInstanceWeblogicServerApplicationDatabase"]]]:
        '''application_database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#application_database JavaServiceInstance#application_database}
        '''
        result = self._values.get("application_database")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["JavaServiceInstanceWeblogicServerApplicationDatabase"]]], result)

    @builtins.property
    def backup_volume_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#backup_volume_size JavaServiceInstance#backup_volume_size}.'''
        result = self._values.get("backup_volume_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["JavaServiceInstanceWeblogicServerCluster"]]]:
        '''cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster JavaServiceInstance#cluster}
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["JavaServiceInstanceWeblogicServerCluster"]]], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#cluster_name JavaServiceInstance#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connect_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#connect_string JavaServiceInstance#connect_string}.'''
        result = self._values.get("connect_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional["JavaServiceInstanceWeblogicServerDomain"]:
        '''domain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#domain JavaServiceInstance#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServerDomain"], result)

    @builtins.property
    def ip_reservations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ip_reservations JavaServiceInstance#ip_reservations}.'''
        result = self._values.get("ip_reservations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def managed_servers(
        self,
    ) -> typing.Optional["JavaServiceInstanceWeblogicServerManagedServers"]:
        '''managed_servers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#managed_servers JavaServiceInstance#managed_servers}
        '''
        result = self._values.get("managed_servers")
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServerManagedServers"], result)

    @builtins.property
    def middleware_volume_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#middleware_volume_size JavaServiceInstance#middleware_volume_size}.'''
        result = self._values.get("middleware_volume_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_manager(
        self,
    ) -> typing.Optional["JavaServiceInstanceWeblogicServerNodeManager"]:
        '''node_manager block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#node_manager JavaServiceInstance#node_manager}
        '''
        result = self._values.get("node_manager")
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServerNodeManager"], result)

    @builtins.property
    def ports(self) -> typing.Optional["JavaServiceInstanceWeblogicServerPorts"]:
        '''ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#ports JavaServiceInstance#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServerPorts"], result)

    @builtins.property
    def upper_stack_product_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#upper_stack_product_name JavaServiceInstance#upper_stack_product_name}.'''
        result = self._values.get("upper_stack_product_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerAdmin",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "username": "username",
        "port": "port",
        "secured_port": "securedPort",
    },
)
class JavaServiceInstanceWeblogicServerAdmin:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        port: typing.Optional[jsii.Number] = None,
        secured_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86fca180c73c14b729aeef30e4abfbf6a6033a8d7f3ccd2491e792d4d84ba65)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument secured_port", value=secured_port, expected_type=type_hints["secured_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if port is not None:
            self._values["port"] = port
        if secured_port is not None:
            self._values["secured_port"] = secured_port

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def secured_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.'''
        result = self._values.get("secured_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerAdmin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerAdminOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerAdminOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92061783050ad975609eddd617510349ff55b1125e81f4788f99cb77f7dc03c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetSecuredPort")
    def reset_secured_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecuredPort", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="securedPortInput")
    def secured_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "securedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde95323e66f8c7ebe6eb557509f679298aabc06555331a33205b209e09a9b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a99795641be926180f1551c721050d5ce89ae74fadd2fc8583538eb970e004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="securedPort")
    def secured_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "securedPort"))

    @secured_port.setter
    def secured_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3dbfb001d3910a6d88903ecef6ac8e18e0591d707c8f820faa253268ae96abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securedPort", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53142f79721eddcb082d30cf17cacc59f9ef592668add766d06446d5aba5a77b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JavaServiceInstanceWeblogicServerAdmin]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerAdmin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerAdmin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f35a9590f83297fcf003f4f29795dc61151cd06099037f49f2792e697ef1e9cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerApplicationDatabase",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "username": "username",
        "pdb_name": "pdbName",
    },
)
class JavaServiceInstanceWeblogicServerApplicationDatabase:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        username: builtins.str,
        pdb_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param pdb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#pdb_name JavaServiceInstance#pdb_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__315c86721236dcbc37d02282d9d5243df080d432939bc8f735057cadd548c898)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument pdb_name", value=pdb_name, expected_type=type_hints["pdb_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "password": password,
            "username": username,
        }
        if pdb_name is not None:
            self._values["pdb_name"] = pdb_name

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pdb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#pdb_name JavaServiceInstance#pdb_name}.'''
        result = self._values.get("pdb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerApplicationDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerApplicationDatabaseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerApplicationDatabaseList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c75dcb83849e5800401c8e09006da10203e0a059b5a6515147c8f847afd3615)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "JavaServiceInstanceWeblogicServerApplicationDatabaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7471b70748c3f1e3b407c10e58d1975e9b557fa2be8ccdb14b777f7d1887f027)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JavaServiceInstanceWeblogicServerApplicationDatabaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ffb8cdb938d650f6f6f7482214b40081387f9cd02681ae3017ddeb9e2b0c812)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98c48b605d68453755b6f09f072d64faf72e84d8a26698ccc31e5177adfcab4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aaeaa7175297cd28a018a685b539984ce242de9e1042962b384b9d1196f4123e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4e85a865074d5f041236df9d11e9745ac4aa60323bbd8870573467fa2d9f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class JavaServiceInstanceWeblogicServerApplicationDatabaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerApplicationDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73845062bd05dbe481e4f87123dc87289aa7aa638592730a22fbdb3fe0d06991)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPdbName")
    def reset_pdb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPdbName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pdbNameInput")
    def pdb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__023774c353f18dfbe3d32a739bcaf59d367cb365d223ff89248b7f79f461d672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac200da060f25b711740a8bf1ef420a558874e0532c3feae074f3736bdc2b13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pdbName")
    def pdb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdbName"))

    @pdb_name.setter
    def pdb_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__effe961eedf58480d4ed745cc910c6e941c026312040bfd9c372b8ab45de74bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdbName", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ee1efb89f904c04a8a759e62e6717568afc98e04cc17c48a489f0fec3651baa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32ca66dccd4a3ca41342d8931a98f46021cd24b85c8d18d354d9c66d3ae90455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerCluster",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "path_prefixes": "pathPrefixes",
        "server_count": "serverCount",
        "servers_per_node": "serversPerNode",
        "shape": "shape",
    },
)
class JavaServiceInstanceWeblogicServerCluster:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_count: typing.Optional[jsii.Number] = None,
        servers_per_node: typing.Optional[jsii.Number] = None,
        shape: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#type JavaServiceInstance#type}.
        :param path_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#path_prefixes JavaServiceInstance#path_prefixes}.
        :param server_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#server_count JavaServiceInstance#server_count}.
        :param servers_per_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#servers_per_node JavaServiceInstance#servers_per_node}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d54ecaf75755574ce3006a5c37e29f7706552287b04cb1cd797687d5a6b41b93)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument path_prefixes", value=path_prefixes, expected_type=type_hints["path_prefixes"])
            check_type(argname="argument server_count", value=server_count, expected_type=type_hints["server_count"])
            check_type(argname="argument servers_per_node", value=servers_per_node, expected_type=type_hints["servers_per_node"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if path_prefixes is not None:
            self._values["path_prefixes"] = path_prefixes
        if server_count is not None:
            self._values["server_count"] = server_count
        if servers_per_node is not None:
            self._values["servers_per_node"] = servers_per_node
        if shape is not None:
            self._values["shape"] = shape

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#type JavaServiceInstance#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#path_prefixes JavaServiceInstance#path_prefixes}.'''
        result = self._values.get("path_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#server_count JavaServiceInstance#server_count}.'''
        result = self._values.get("server_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def servers_per_node(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#servers_per_node JavaServiceInstance#servers_per_node}.'''
        result = self._values.get("servers_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shape(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#shape JavaServiceInstance#shape}.'''
        result = self._values.get("shape")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerClusterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerClusterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f6bb7b45fb3ce6d0672703259daab37c7a28e5eecc8c479db26bda725e2e08c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "JavaServiceInstanceWeblogicServerClusterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0feb5211f3d80f43e99cd4b85c94f340e9eb4b9ac4948df7091f21d303c46379)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("JavaServiceInstanceWeblogicServerClusterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c527e046c52d0249562a98eae1ec16556fe5e4b9664ded3d8ef14f94226e29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49a95b4edaa4308e4db03c000df0a9a046790ce2f67f2658eb04181852f7cd9d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f398d6ba79fa133ba01284e7f90ee83fe758ee8c63c5307490fe8e9c6e67ab5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c45d93de4cb8410f344925f9c1d1e1f1f43730b187848050a072769e357c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class JavaServiceInstanceWeblogicServerClusterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerClusterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f941590731357ddb7931ef16d3e5b6adaff7ab0d803e32fadbfe98370681b06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPathPrefixes")
    def reset_path_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixes", []))

    @jsii.member(jsii_name="resetServerCount")
    def reset_server_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerCount", []))

    @jsii.member(jsii_name="resetServersPerNode")
    def reset_servers_per_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServersPerNode", []))

    @jsii.member(jsii_name="resetShape")
    def reset_shape(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShape", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixesInput")
    def path_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="serverCountInput")
    def server_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverCountInput"))

    @builtins.property
    @jsii.member(jsii_name="serversPerNodeInput")
    def servers_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serversPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3146e59d71316aa06f3f07a43a39a72604be7b48c5a63610730a715fa86b8e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixes")
    def path_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathPrefixes"))

    @path_prefixes.setter
    def path_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664aaefd95d9b9815f9da6f35e251a70ebd9d5937fb585d1f4508f4c78026ede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="serverCount")
    def server_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverCount"))

    @server_count.setter
    def server_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9369b7798abfe2dab914fafda61773a20b027ef2e0a21768d8066c926553d67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCount", value)

    @builtins.property
    @jsii.member(jsii_name="serversPerNode")
    def servers_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serversPerNode"))

    @servers_per_node.setter
    def servers_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8658e7dbe425a66c16e4a4df5ef45a631d88d533a7df204b782c207d446068e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serversPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__383f7b669144a181bd3f8450d896f8ca6db5009e49a39cbaa5ce9208ea00ac5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24dc306a71fe5ad284a44666d5136bbf9031ca1299ff65ee7101432b9788c854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerCluster, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerCluster, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerCluster, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f5eff617c8968b709eacf4fd8a0e940a4166a09f8b8bd1b01cac4bfc261792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerDatabase",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "username": "username",
        "name": "name",
        "pdb_name": "pdbName",
    },
)
class JavaServiceInstanceWeblogicServerDatabase:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        name: typing.Optional[builtins.str] = None,
        pdb_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param pdb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#pdb_name JavaServiceInstance#pdb_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b3b3eb6e5954a35a87f0884eafbd06adc480f6d9234720bc3b8717058e5e2b8)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pdb_name", value=pdb_name, expected_type=type_hints["pdb_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if name is not None:
            self._values["name"] = name
        if pdb_name is not None:
            self._values["pdb_name"] = pdb_name

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pdb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#pdb_name JavaServiceInstance#pdb_name}.'''
        result = self._values.get("pdb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerDatabaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__34c0649cf43f67c869b4f1d53f5648764d0b2e2bdb4ef8c74581353b273f9e4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPdbName")
    def reset_pdb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPdbName", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pdbNameInput")
    def pdb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__669d4aec810932900765ec5a9a66985557b2ce7be314bf413cab260ed421912b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__432bfd53e32674376ec21a12a2160686a1aa425d2fe1f7032ac7a22ae0ac8451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="pdbName")
    def pdb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdbName"))

    @pdb_name.setter
    def pdb_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3a4fe425770a7d7c60ef1d5c192e9c4cc9f0d71e923417baf3a49769778aba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdbName", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c564fe96949bf157c02725e81418cef0d0f8014b781227b0e7876470a49d62f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerDatabase]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerDatabase], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerDatabase],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__196f2e8249a143e413d7c17d38a66123b2c177a537ae41abf95f269af0a74887)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerDomain",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "name": "name",
        "partition_count": "partitionCount",
        "volume_size": "volumeSize",
    },
)
class JavaServiceInstanceWeblogicServerDomain:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition_count: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#mode JavaServiceInstance#mode}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#partition_count JavaServiceInstance#partition_count}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#volume_size JavaServiceInstance#volume_size}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3b182ca59bdbe3f43240491639f1be174a13130a74fa763ba3f33970f3639ce)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partition_count", value=partition_count, expected_type=type_hints["partition_count"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if name is not None:
            self._values["name"] = name
        if partition_count is not None:
            self._values["partition_count"] = partition_count
        if volume_size is not None:
            self._values["volume_size"] = volume_size

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#mode JavaServiceInstance#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#partition_count JavaServiceInstance#partition_count}.'''
        result = self._values.get("partition_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#volume_size JavaServiceInstance#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerDomainOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerDomainOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb28c6da7339ebdaaa6ef25532d7e60f3043af083c078816725bd10b3f8daa7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPartitionCount")
    def reset_partition_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionCount", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionCountInput")
    def partition_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionCountInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f9b82017fa3e3dd4f45b704e1ca09987ccd78d851859861bc0c6ff83f60ce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d408856f8117bbbf7a62f4ce104e236eef637eb8714c75f58a6cdbf9de399d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="partitionCount")
    def partition_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partitionCount"))

    @partition_count.setter
    def partition_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1ecdcc110a37c162a6b685ab01e4897fb131282be29a7747d583bc4e256e7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionCount", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2589f89cd1f93581790055258e1e50fd8a0a20511a1293e9766c34eaae95e722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerDomain]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerDomain], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerDomain],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad80927cb98762de3f6edd6d3f486cadc2050af95694b9e8ba8ce4722493293b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerManagedServers",
    jsii_struct_bases=[],
    name_mapping={
        "initial_heap_size": "initialHeapSize",
        "initial_permanent_generation": "initialPermanentGeneration",
        "jvm_args": "jvmArgs",
        "max_heap_size": "maxHeapSize",
        "max_permanent_generation": "maxPermanentGeneration",
        "overwrite_jvm_args": "overwriteJvmArgs",
        "server_count": "serverCount",
    },
)
class JavaServiceInstanceWeblogicServerManagedServers:
    def __init__(
        self,
        *,
        initial_heap_size: typing.Optional[jsii.Number] = None,
        initial_permanent_generation: typing.Optional[jsii.Number] = None,
        jvm_args: typing.Optional[builtins.str] = None,
        max_heap_size: typing.Optional[jsii.Number] = None,
        max_permanent_generation: typing.Optional[jsii.Number] = None,
        overwrite_jvm_args: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param initial_heap_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_heap_size JavaServiceInstance#initial_heap_size}.
        :param initial_permanent_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_permanent_generation JavaServiceInstance#initial_permanent_generation}.
        :param jvm_args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#jvm_args JavaServiceInstance#jvm_args}.
        :param max_heap_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_heap_size JavaServiceInstance#max_heap_size}.
        :param max_permanent_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_permanent_generation JavaServiceInstance#max_permanent_generation}.
        :param overwrite_jvm_args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#overwrite_jvm_args JavaServiceInstance#overwrite_jvm_args}.
        :param server_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#server_count JavaServiceInstance#server_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f93028a71062f998b37d3fbadb1ad3bc4bf252863319d3298e14712ce056a01)
            check_type(argname="argument initial_heap_size", value=initial_heap_size, expected_type=type_hints["initial_heap_size"])
            check_type(argname="argument initial_permanent_generation", value=initial_permanent_generation, expected_type=type_hints["initial_permanent_generation"])
            check_type(argname="argument jvm_args", value=jvm_args, expected_type=type_hints["jvm_args"])
            check_type(argname="argument max_heap_size", value=max_heap_size, expected_type=type_hints["max_heap_size"])
            check_type(argname="argument max_permanent_generation", value=max_permanent_generation, expected_type=type_hints["max_permanent_generation"])
            check_type(argname="argument overwrite_jvm_args", value=overwrite_jvm_args, expected_type=type_hints["overwrite_jvm_args"])
            check_type(argname="argument server_count", value=server_count, expected_type=type_hints["server_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if initial_heap_size is not None:
            self._values["initial_heap_size"] = initial_heap_size
        if initial_permanent_generation is not None:
            self._values["initial_permanent_generation"] = initial_permanent_generation
        if jvm_args is not None:
            self._values["jvm_args"] = jvm_args
        if max_heap_size is not None:
            self._values["max_heap_size"] = max_heap_size
        if max_permanent_generation is not None:
            self._values["max_permanent_generation"] = max_permanent_generation
        if overwrite_jvm_args is not None:
            self._values["overwrite_jvm_args"] = overwrite_jvm_args
        if server_count is not None:
            self._values["server_count"] = server_count

    @builtins.property
    def initial_heap_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_heap_size JavaServiceInstance#initial_heap_size}.'''
        result = self._values.get("initial_heap_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_permanent_generation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_permanent_generation JavaServiceInstance#initial_permanent_generation}.'''
        result = self._values.get("initial_permanent_generation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def jvm_args(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#jvm_args JavaServiceInstance#jvm_args}.'''
        result = self._values.get("jvm_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_heap_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_heap_size JavaServiceInstance#max_heap_size}.'''
        result = self._values.get("max_heap_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_permanent_generation(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_permanent_generation JavaServiceInstance#max_permanent_generation}.'''
        result = self._values.get("max_permanent_generation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def overwrite_jvm_args(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#overwrite_jvm_args JavaServiceInstance#overwrite_jvm_args}.'''
        result = self._values.get("overwrite_jvm_args")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def server_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#server_count JavaServiceInstance#server_count}.'''
        result = self._values.get("server_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerManagedServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerManagedServersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerManagedServersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fef345546f20e7895bf62361f04c95e29e961b47c767ac964e2c12429a2be7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInitialHeapSize")
    def reset_initial_heap_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialHeapSize", []))

    @jsii.member(jsii_name="resetInitialPermanentGeneration")
    def reset_initial_permanent_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPermanentGeneration", []))

    @jsii.member(jsii_name="resetJvmArgs")
    def reset_jvm_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJvmArgs", []))

    @jsii.member(jsii_name="resetMaxHeapSize")
    def reset_max_heap_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeapSize", []))

    @jsii.member(jsii_name="resetMaxPermanentGeneration")
    def reset_max_permanent_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPermanentGeneration", []))

    @jsii.member(jsii_name="resetOverwriteJvmArgs")
    def reset_overwrite_jvm_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwriteJvmArgs", []))

    @jsii.member(jsii_name="resetServerCount")
    def reset_server_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerCount", []))

    @builtins.property
    @jsii.member(jsii_name="initialHeapSizeInput")
    def initial_heap_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialHeapSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="initialPermanentGenerationInput")
    def initial_permanent_generation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialPermanentGenerationInput"))

    @builtins.property
    @jsii.member(jsii_name="jvmArgsInput")
    def jvm_args_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jvmArgsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeapSizeInput")
    def max_heap_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxHeapSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPermanentGenerationInput")
    def max_permanent_generation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPermanentGenerationInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteJvmArgsInput")
    def overwrite_jvm_args_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overwriteJvmArgsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverCountInput")
    def server_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serverCountInput"))

    @builtins.property
    @jsii.member(jsii_name="initialHeapSize")
    def initial_heap_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialHeapSize"))

    @initial_heap_size.setter
    def initial_heap_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2245e665d54454396ee99a8198c198b08dad11401e69e5dd2bd169f424c01cb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialHeapSize", value)

    @builtins.property
    @jsii.member(jsii_name="initialPermanentGeneration")
    def initial_permanent_generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialPermanentGeneration"))

    @initial_permanent_generation.setter
    def initial_permanent_generation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be7b793c76289a757fc64d8985c993675797d458ebbc6602f47beea80160dbfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialPermanentGeneration", value)

    @builtins.property
    @jsii.member(jsii_name="jvmArgs")
    def jvm_args(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jvmArgs"))

    @jvm_args.setter
    def jvm_args(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cdeed62437eae132cc811846c749b229d171b081e168c0e6f2d455e0a14f938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jvmArgs", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeapSize")
    def max_heap_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxHeapSize"))

    @max_heap_size.setter
    def max_heap_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bdddf0a83959438abdaffa1ba87cfef536b8d6363862a3d6def13c958232d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeapSize", value)

    @builtins.property
    @jsii.member(jsii_name="maxPermanentGeneration")
    def max_permanent_generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPermanentGeneration"))

    @max_permanent_generation.setter
    def max_permanent_generation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220c9eccc6982acc11f8d90100a39128ad316f595c2f7eb917f7fecd30d88367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPermanentGeneration", value)

    @builtins.property
    @jsii.member(jsii_name="overwriteJvmArgs")
    def overwrite_jvm_args(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overwriteJvmArgs"))

    @overwrite_jvm_args.setter
    def overwrite_jvm_args(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7987d87cf52b952337d19079a4edc55584374c0d3ee1e703ee17dedc653810b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwriteJvmArgs", value)

    @builtins.property
    @jsii.member(jsii_name="serverCount")
    def server_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serverCount"))

    @server_count.setter
    def server_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eefd04ce3ca69a97abbed935adf2ac8adbb196c2d7557591051bf3b9a14ce89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerManagedServers]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerManagedServers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerManagedServers],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6663fee7fbfc147d342c9fddf93e652ad6e63a5f923e0a110c772a713082ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerNodeManager",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "port": "port", "username": "username"},
)
class JavaServiceInstanceWeblogicServerNodeManager:
    def __init__(
        self,
        *,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af8ba00b1b29bce9cbf8a826820c5290285810e62f883ef2f84faf5ec957b12)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerNodeManager(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerNodeManagerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerNodeManagerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd1b7b5ac5dffdd1e1bd9c5c05fa0e7055211e672a6505432a3fe873c8711594)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b8787b3faa96766ddce7cd39fe4025b2e99f973cd54d4b1fcc9565138cace0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b00755878be74af212c23026b98d4563598c7d418de02917a90e0088e85d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03cab4408ff967e78635b7761be6375c5b92a50e7dbc043602c3b93c6d97a5ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerNodeManager]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerNodeManager], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerNodeManager],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6e7634eefb4b6162ec15234fcd922bdb4bfe614918cd2db34c1202db9f06a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class JavaServiceInstanceWeblogicServerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e08da735734946bfb667254ac12c851f4e182d06b0cb39d2becd7f5f2ec96af2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdmin")
    def put_admin(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        port: typing.Optional[jsii.Number] = None,
        secured_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param secured_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#secured_port JavaServiceInstance#secured_port}.
        '''
        value = JavaServiceInstanceWeblogicServerAdmin(
            password=password, username=username, port=port, secured_port=secured_port
        )

        return typing.cast(None, jsii.invoke(self, "putAdmin", [value]))

    @jsii.member(jsii_name="putApplicationDatabase")
    def put_application_database(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a32417420cd2eb2838f41413941a419b37307fbf7e3001888d45ebbf5b4a0d7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplicationDatabase", [value]))

    @jsii.member(jsii_name="putCluster")
    def put_cluster(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerCluster, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e8f84b8a26bae104568ae7e94b1d9e56518d0a0e5c6abf98d3740bea602138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCluster", [value]))

    @jsii.member(jsii_name="putDatabase")
    def put_database(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        name: typing.Optional[builtins.str] = None,
        pdb_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param pdb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#pdb_name JavaServiceInstance#pdb_name}.
        '''
        value = JavaServiceInstanceWeblogicServerDatabase(
            password=password, username=username, name=name, pdb_name=pdb_name
        )

        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="putDomain")
    def put_domain(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partition_count: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#mode JavaServiceInstance#mode}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#name JavaServiceInstance#name}.
        :param partition_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#partition_count JavaServiceInstance#partition_count}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#volume_size JavaServiceInstance#volume_size}.
        '''
        value = JavaServiceInstanceWeblogicServerDomain(
            mode=mode,
            name=name,
            partition_count=partition_count,
            volume_size=volume_size,
        )

        return typing.cast(None, jsii.invoke(self, "putDomain", [value]))

    @jsii.member(jsii_name="putManagedServers")
    def put_managed_servers(
        self,
        *,
        initial_heap_size: typing.Optional[jsii.Number] = None,
        initial_permanent_generation: typing.Optional[jsii.Number] = None,
        jvm_args: typing.Optional[builtins.str] = None,
        max_heap_size: typing.Optional[jsii.Number] = None,
        max_permanent_generation: typing.Optional[jsii.Number] = None,
        overwrite_jvm_args: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param initial_heap_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_heap_size JavaServiceInstance#initial_heap_size}.
        :param initial_permanent_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#initial_permanent_generation JavaServiceInstance#initial_permanent_generation}.
        :param jvm_args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#jvm_args JavaServiceInstance#jvm_args}.
        :param max_heap_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_heap_size JavaServiceInstance#max_heap_size}.
        :param max_permanent_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#max_permanent_generation JavaServiceInstance#max_permanent_generation}.
        :param overwrite_jvm_args: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#overwrite_jvm_args JavaServiceInstance#overwrite_jvm_args}.
        :param server_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#server_count JavaServiceInstance#server_count}.
        '''
        value = JavaServiceInstanceWeblogicServerManagedServers(
            initial_heap_size=initial_heap_size,
            initial_permanent_generation=initial_permanent_generation,
            jvm_args=jvm_args,
            max_heap_size=max_heap_size,
            max_permanent_generation=max_permanent_generation,
            overwrite_jvm_args=overwrite_jvm_args,
            server_count=server_count,
        )

        return typing.cast(None, jsii.invoke(self, "putManagedServers", [value]))

    @jsii.member(jsii_name="putNodeManager")
    def put_node_manager(
        self,
        *,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#password JavaServiceInstance#password}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#port JavaServiceInstance#port}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#username JavaServiceInstance#username}.
        '''
        value = JavaServiceInstanceWeblogicServerNodeManager(
            password=password, port=port, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putNodeManager", [value]))

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        *,
        content_port: typing.Optional[jsii.Number] = None,
        deployment_channel_port: typing.Optional[jsii.Number] = None,
        privileged_content_port: typing.Optional[jsii.Number] = None,
        privileged_secured_content_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#content_port JavaServiceInstance#content_port}.
        :param deployment_channel_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#deployment_channel_port JavaServiceInstance#deployment_channel_port}.
        :param privileged_content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_content_port JavaServiceInstance#privileged_content_port}.
        :param privileged_secured_content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_content_port JavaServiceInstance#privileged_secured_content_port}.
        '''
        value = JavaServiceInstanceWeblogicServerPorts(
            content_port=content_port,
            deployment_channel_port=deployment_channel_port,
            privileged_content_port=privileged_content_port,
            privileged_secured_content_port=privileged_secured_content_port,
        )

        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="resetApplicationDatabase")
    def reset_application_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationDatabase", []))

    @jsii.member(jsii_name="resetBackupVolumeSize")
    def reset_backup_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupVolumeSize", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetConnectString")
    def reset_connect_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectString", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetIpReservations")
    def reset_ip_reservations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpReservations", []))

    @jsii.member(jsii_name="resetManagedServers")
    def reset_managed_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServers", []))

    @jsii.member(jsii_name="resetMiddlewareVolumeSize")
    def reset_middleware_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMiddlewareVolumeSize", []))

    @jsii.member(jsii_name="resetNodeManager")
    def reset_node_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeManager", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @jsii.member(jsii_name="resetUpperStackProductName")
    def reset_upper_stack_product_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpperStackProductName", []))

    @builtins.property
    @jsii.member(jsii_name="admin")
    def admin(self) -> JavaServiceInstanceWeblogicServerAdminOutputReference:
        return typing.cast(JavaServiceInstanceWeblogicServerAdminOutputReference, jsii.get(self, "admin"))

    @builtins.property
    @jsii.member(jsii_name="applicationDatabase")
    def application_database(
        self,
    ) -> JavaServiceInstanceWeblogicServerApplicationDatabaseList:
        return typing.cast(JavaServiceInstanceWeblogicServerApplicationDatabaseList, jsii.get(self, "applicationDatabase"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> JavaServiceInstanceWeblogicServerClusterList:
        return typing.cast(JavaServiceInstanceWeblogicServerClusterList, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> JavaServiceInstanceWeblogicServerDatabaseOutputReference:
        return typing.cast(JavaServiceInstanceWeblogicServerDatabaseOutputReference, jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> JavaServiceInstanceWeblogicServerDomainOutputReference:
        return typing.cast(JavaServiceInstanceWeblogicServerDomainOutputReference, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="managedServers")
    def managed_servers(
        self,
    ) -> JavaServiceInstanceWeblogicServerManagedServersOutputReference:
        return typing.cast(JavaServiceInstanceWeblogicServerManagedServersOutputReference, jsii.get(self, "managedServers"))

    @builtins.property
    @jsii.member(jsii_name="nodeManager")
    def node_manager(
        self,
    ) -> JavaServiceInstanceWeblogicServerNodeManagerOutputReference:
        return typing.cast(JavaServiceInstanceWeblogicServerNodeManagerOutputReference, jsii.get(self, "nodeManager"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "JavaServiceInstanceWeblogicServerPortsOutputReference":
        return typing.cast("JavaServiceInstanceWeblogicServerPortsOutputReference", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="rootUrl")
    def root_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootUrl"))

    @builtins.property
    @jsii.member(jsii_name="adminInput")
    def admin_input(self) -> typing.Optional[JavaServiceInstanceWeblogicServerAdmin]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerAdmin], jsii.get(self, "adminInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationDatabaseInput")
    def application_database_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]], jsii.get(self, "applicationDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="backupVolumeSizeInput")
    def backup_volume_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connectStringInput")
    def connect_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectStringInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerDatabase]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerDatabase], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[JavaServiceInstanceWeblogicServerDomain]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerDomain], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="ipReservationsInput")
    def ip_reservations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipReservationsInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServersInput")
    def managed_servers_input(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerManagedServers]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerManagedServers], jsii.get(self, "managedServersInput"))

    @builtins.property
    @jsii.member(jsii_name="middlewareVolumeSizeInput")
    def middleware_volume_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "middlewareVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeManagerInput")
    def node_manager_input(
        self,
    ) -> typing.Optional[JavaServiceInstanceWeblogicServerNodeManager]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerNodeManager], jsii.get(self, "nodeManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional["JavaServiceInstanceWeblogicServerPorts"]:
        return typing.cast(typing.Optional["JavaServiceInstanceWeblogicServerPorts"], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="upperStackProductNameInput")
    def upper_stack_product_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upperStackProductNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backupVolumeSize")
    def backup_volume_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupVolumeSize"))

    @backup_volume_size.setter
    def backup_volume_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd4c5c30d7213f9c6c5a360e0cd54f0fa1607da030020ed899ef8bb5914b462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13276d008965230402331cb151d4f22c3c4bbfe2f089d0b6e0f91ddda00b3016)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="connectString")
    def connect_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectString"))

    @connect_string.setter
    def connect_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__152a1fdd65d9d24eea4c782241ed48c56683e43739403480aeaddef9838aa01f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectString", value)

    @builtins.property
    @jsii.member(jsii_name="ipReservations")
    def ip_reservations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipReservations"))

    @ip_reservations.setter
    def ip_reservations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f95533256997e86262f00b55bb834c82118d76cadd818654e80c45efbc0768)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipReservations", value)

    @builtins.property
    @jsii.member(jsii_name="middlewareVolumeSize")
    def middleware_volume_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "middlewareVolumeSize"))

    @middleware_volume_size.setter
    def middleware_volume_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dabc551ce75aa5b22c8cef9068f884ab9d9f6e6f76fd69779556d7c5a49d525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "middlewareVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e06f21e07a77bdc381ff769f9b25697f2bc3b22688ec0d7bdd74296d3e6969e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="upperStackProductName")
    def upper_stack_product_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upperStackProductName"))

    @upper_stack_product_name.setter
    def upper_stack_product_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2048e323f2668e0f9f10ec00a2260e12f4df225af9af34deef3b10e16ef7c172)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upperStackProductName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JavaServiceInstanceWeblogicServer]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104413b49a0a8fb794d29e12e08c7fbf300c4d5e6d6bd90b7c1829cc344c4386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerPorts",
    jsii_struct_bases=[],
    name_mapping={
        "content_port": "contentPort",
        "deployment_channel_port": "deploymentChannelPort",
        "privileged_content_port": "privilegedContentPort",
        "privileged_secured_content_port": "privilegedSecuredContentPort",
    },
)
class JavaServiceInstanceWeblogicServerPorts:
    def __init__(
        self,
        *,
        content_port: typing.Optional[jsii.Number] = None,
        deployment_channel_port: typing.Optional[jsii.Number] = None,
        privileged_content_port: typing.Optional[jsii.Number] = None,
        privileged_secured_content_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#content_port JavaServiceInstance#content_port}.
        :param deployment_channel_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#deployment_channel_port JavaServiceInstance#deployment_channel_port}.
        :param privileged_content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_content_port JavaServiceInstance#privileged_content_port}.
        :param privileged_secured_content_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_content_port JavaServiceInstance#privileged_secured_content_port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c0b7013f7803bd409c54620f0a6818b3847a72087aec8f46c0b6588956728d)
            check_type(argname="argument content_port", value=content_port, expected_type=type_hints["content_port"])
            check_type(argname="argument deployment_channel_port", value=deployment_channel_port, expected_type=type_hints["deployment_channel_port"])
            check_type(argname="argument privileged_content_port", value=privileged_content_port, expected_type=type_hints["privileged_content_port"])
            check_type(argname="argument privileged_secured_content_port", value=privileged_secured_content_port, expected_type=type_hints["privileged_secured_content_port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content_port is not None:
            self._values["content_port"] = content_port
        if deployment_channel_port is not None:
            self._values["deployment_channel_port"] = deployment_channel_port
        if privileged_content_port is not None:
            self._values["privileged_content_port"] = privileged_content_port
        if privileged_secured_content_port is not None:
            self._values["privileged_secured_content_port"] = privileged_secured_content_port

    @builtins.property
    def content_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#content_port JavaServiceInstance#content_port}.'''
        result = self._values.get("content_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deployment_channel_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#deployment_channel_port JavaServiceInstance#deployment_channel_port}.'''
        result = self._values.get("deployment_channel_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged_content_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_content_port JavaServiceInstance#privileged_content_port}.'''
        result = self._values.get("privileged_content_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def privileged_secured_content_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/java_service_instance#privileged_secured_content_port JavaServiceInstance#privileged_secured_content_port}.'''
        result = self._values.get("privileged_secured_content_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JavaServiceInstanceWeblogicServerPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class JavaServiceInstanceWeblogicServerPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.javaServiceInstance.JavaServiceInstanceWeblogicServerPortsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae5058e805b17d2e33ad2cadc78cbdbb16e24f4c92fca6eff5ba9d501735450f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContentPort")
    def reset_content_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentPort", []))

    @jsii.member(jsii_name="resetDeploymentChannelPort")
    def reset_deployment_channel_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentChannelPort", []))

    @jsii.member(jsii_name="resetPrivilegedContentPort")
    def reset_privileged_content_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedContentPort", []))

    @jsii.member(jsii_name="resetPrivilegedSecuredContentPort")
    def reset_privileged_secured_content_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegedSecuredContentPort", []))

    @builtins.property
    @jsii.member(jsii_name="contentPortInput")
    def content_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "contentPortInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentChannelPortInput")
    def deployment_channel_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentChannelPortInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedContentPortInput")
    def privileged_content_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privilegedContentPortInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedSecuredContentPortInput")
    def privileged_secured_content_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "privilegedSecuredContentPortInput"))

    @builtins.property
    @jsii.member(jsii_name="contentPort")
    def content_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "contentPort"))

    @content_port.setter
    def content_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b62ce9b9b04283e8806ce8486b4ba7fbdf99ee0d82d27eb336db821607ed9e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentPort", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentChannelPort")
    def deployment_channel_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentChannelPort"))

    @deployment_channel_port.setter
    def deployment_channel_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27086b1d2baee13af4294a559da0e40967a9364acbb9568a52736ec617815a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentChannelPort", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedContentPort")
    def privileged_content_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privilegedContentPort"))

    @privileged_content_port.setter
    def privileged_content_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a19a3523fa49750a01fd131415be92578489b6d610cb37e139c9093a99970d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedContentPort", value)

    @builtins.property
    @jsii.member(jsii_name="privilegedSecuredContentPort")
    def privileged_secured_content_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "privilegedSecuredContentPort"))

    @privileged_secured_content_port.setter
    def privileged_secured_content_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09d135c8ea9c020d42d3983eee20a1f4fc9f8d90f213d98d3dc6f968bfe187bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilegedSecuredContentPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[JavaServiceInstanceWeblogicServerPorts]:
        return typing.cast(typing.Optional[JavaServiceInstanceWeblogicServerPorts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[JavaServiceInstanceWeblogicServerPorts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a22a8f765ffa8e4d0eaf16939d753c279a0b40ba25b36807ba0665da0fbf73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "JavaServiceInstance",
    "JavaServiceInstanceBackups",
    "JavaServiceInstanceBackupsOutputReference",
    "JavaServiceInstanceConfig",
    "JavaServiceInstanceLoadBalancer",
    "JavaServiceInstanceLoadBalancerOutputReference",
    "JavaServiceInstanceOracleTrafficDirector",
    "JavaServiceInstanceOracleTrafficDirectorAdmin",
    "JavaServiceInstanceOracleTrafficDirectorAdminOutputReference",
    "JavaServiceInstanceOracleTrafficDirectorListener",
    "JavaServiceInstanceOracleTrafficDirectorListenerOutputReference",
    "JavaServiceInstanceOracleTrafficDirectorOutputReference",
    "JavaServiceInstanceTimeouts",
    "JavaServiceInstanceTimeoutsOutputReference",
    "JavaServiceInstanceWeblogicServer",
    "JavaServiceInstanceWeblogicServerAdmin",
    "JavaServiceInstanceWeblogicServerAdminOutputReference",
    "JavaServiceInstanceWeblogicServerApplicationDatabase",
    "JavaServiceInstanceWeblogicServerApplicationDatabaseList",
    "JavaServiceInstanceWeblogicServerApplicationDatabaseOutputReference",
    "JavaServiceInstanceWeblogicServerCluster",
    "JavaServiceInstanceWeblogicServerClusterList",
    "JavaServiceInstanceWeblogicServerClusterOutputReference",
    "JavaServiceInstanceWeblogicServerDatabase",
    "JavaServiceInstanceWeblogicServerDatabaseOutputReference",
    "JavaServiceInstanceWeblogicServerDomain",
    "JavaServiceInstanceWeblogicServerDomainOutputReference",
    "JavaServiceInstanceWeblogicServerManagedServers",
    "JavaServiceInstanceWeblogicServerManagedServersOutputReference",
    "JavaServiceInstanceWeblogicServerNodeManager",
    "JavaServiceInstanceWeblogicServerNodeManagerOutputReference",
    "JavaServiceInstanceWeblogicServerOutputReference",
    "JavaServiceInstanceWeblogicServerPorts",
    "JavaServiceInstanceWeblogicServerPortsOutputReference",
]

publication.publish()

def _typecheckingstub__eabaa8d63d8bfa48d610b109cf1a794e0b7155bfdd9acd93ebf64e606464fd09(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    backups: typing.Union[JavaServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]],
    edition: builtins.str,
    name: builtins.str,
    ssh_public_key: builtins.str,
    weblogic_server: typing.Union[JavaServiceInstanceWeblogicServer, typing.Dict[builtins.str, typing.Any]],
    assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_domain: typing.Optional[builtins.str] = None,
    backup_destination: typing.Optional[builtins.str] = None,
    bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    enable_admin_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    level: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[JavaServiceInstanceLoadBalancer, typing.Dict[builtins.str, typing.Any]]] = None,
    metering_frequency: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    oracle_traffic_director: typing.Optional[typing.Union[JavaServiceInstanceOracleTrafficDirector, typing.Dict[builtins.str, typing.Any]]] = None,
    region: typing.Optional[builtins.str] = None,
    service_version: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    source_service_name: typing.Optional[builtins.str] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[JavaServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_identity_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__793da1444972870a524b7a324275f3fb60e6049132b376000ec6c85012fc2413(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__385ad1fa5328324f4e330d9f55e2bad7ac6ed124b4d1a33a9aaadb148cbb4eba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c10a71f2f534d55693735285d03a77ae625fdd63c58b30a84bb9b4a00b2988d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c5b4048b4d1e0d4ae39c3c02d7a1529390ec05b43b4a348464a1df8e62ff75(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67021477161ed1405801bae819b96c7131439c5be82dadde70ad3589f42752c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645e2899c3f55c9a954fb930143330453b981e388f2d2fd4f233750c07aba252(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00626e08b2b9465d6103fa08e0d423aad2f0a26df16c6ffd6cf1ae68540432f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06539b6dc5ece6c7df7063982e6466e13f0cec73ade0af8761ae08f6c61ea992(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a55bac0e774be3ab1ba30b0156e098ea2c4de0631008a88a92169330f6bff7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034dd1f9ca6cd04ba06198c7e3078f515c16d1fc68becbae66b2d3fad2b8b3c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19156f9656de4519fcec624c9371106851efaa31ab2cca4f005f0bd71a25c06c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb0a1d986020e314ac5e3f6ded6abd0b340e0e1689d216abd46d2a2fe6141b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b72bbbb8d30b6a8c271cfe0600aa8059f3630acfcb6d620b037832491e0d67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac459b4a1ef41e0f4ba520b4929080b6ce73620ae92e9a69439d3a77bc3fac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f8d4745d920dc20f1c8aea2453edd67ec41c4165fdfcf05fa896516f697519(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381f6bb0a5f593e3b947962f9a64909c72e2c401218372bda6f38f734bd008bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25049a015c51496742187cdc336986d5b981d3890af99fd88e3099d0cec1f80a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21012e9f8e87447dd9207fd2205bc944f51f92c489f78216f54a528ecfd20137(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__065b2aea37b103ca29393581e2d4a82180327f014ff54b54ff3842123f6826d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63839f69260fdc7642656fd7bcf840232149978b32c91858c30040ba2694a04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeef8d7f3473c6d8ab733f0b86cd2b1d3342b42934225c34beeae5c9cf12d8a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c481dbd0b4f253458b5b9bcffe44277827a599b09397109e824934b5252efeb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f6c05a8bec21891b9600aac743922bb5c17839465c85d3e9171f9651f91dd3(
    *,
    cloud_storage_container: builtins.str,
    auto_generate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cloud_storage_password: typing.Optional[builtins.str] = None,
    cloud_storage_username: typing.Optional[builtins.str] = None,
    use_oauth_for_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9e2209bf9fa5dff23c27822b7cfdbe7cc1fb66bb0ae9802832d7b21f03aef4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c9ba7a7ecaafc3d58081aa9b171f9ad1cd5c3e00b813b1a78c791a889db42c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9d1e684a0e0445cd27c0127a18b525e3ab8a00f6cb518e57e2bd3dfb80757c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333c8bece7b9f1592ce0782eaf33f6640dafda4ed41da97eafd64d3109553942(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a75adaf51b666217e54a234dab093f5091ba0e8a15504a54a1302a2124f0cfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6b8d92a250aa95b2983246d96e2e1b759278f9839fef6e724370c7fc29364a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a9e7853e3ba752a35437b4a3745123b47a980fc512b854af925cf251a6d33(
    value: typing.Optional[JavaServiceInstanceBackups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2721257bc94fb239084b135f2ee28509955ba4420427c43ed3a5610fcd4ea787(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backups: typing.Union[JavaServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]],
    edition: builtins.str,
    name: builtins.str,
    ssh_public_key: builtins.str,
    weblogic_server: typing.Union[JavaServiceInstanceWeblogicServer, typing.Dict[builtins.str, typing.Any]],
    assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    availability_domain: typing.Optional[builtins.str] = None,
    backup_destination: typing.Optional[builtins.str] = None,
    bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    enable_admin_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    level: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[JavaServiceInstanceLoadBalancer, typing.Dict[builtins.str, typing.Any]]] = None,
    metering_frequency: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    oracle_traffic_director: typing.Optional[typing.Union[JavaServiceInstanceOracleTrafficDirector, typing.Dict[builtins.str, typing.Any]]] = None,
    region: typing.Optional[builtins.str] = None,
    service_version: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    source_service_name: typing.Optional[builtins.str] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[JavaServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    use_identity_service: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5bf32d8c3e02e924d2a38974378b29de1adb964676470763787dac059f8a90f(
    *,
    load_balancing_policy: typing.Optional[builtins.str] = None,
    subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df6c27eae8014a4fdf82cef9ad676bc7de372fc64d37f2b001948b10a035e18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e688780ffd50cf1fee7a447a98cabe7b2b9560183180cdb55d0d44f23200378b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a1d0d5c774f85d4ae8898fe4a7344778776fe24faa840e24d5253c9866471f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0191dc24bcae2450bf72a437583a9682a6496aa78d4446563a15e67f43c8e57c(
    value: typing.Optional[JavaServiceInstanceLoadBalancer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a33e8ac66026c5aa851a1946a36667d7f595c2322ba368041d6e43c436ef636(
    *,
    admin: typing.Union[JavaServiceInstanceOracleTrafficDirectorAdmin, typing.Dict[builtins.str, typing.Any]],
    shape: builtins.str,
    high_availability: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
    listener: typing.Optional[typing.Union[JavaServiceInstanceOracleTrafficDirectorListener, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancing_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__241c30e605280a55e9c8a8f7b5bec2d8ffdb017026cfd580445e4d67c4d1492f(
    *,
    password: builtins.str,
    username: builtins.str,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc2d0ddd158a8d83a60d3ebcd66cc53f1237c1256a7aaac34c7d751cfe600300(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4bb83a9b6d9663c8e2dc69e0bd6eb45201993accc9e6f4bad98f2c0a8259620(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54b3a1c316f74f3f9e867b26186f043eeb6458711c6ebfafa96932d393a01b9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b3d2887892314781a29681beb037c2fa87bfb6da067629200d5db66f2bf2aab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378313e723c9c1749a1d50c6b40bc0e62b21135eb5eadfe89138d593dfa13dd6(
    value: typing.Optional[JavaServiceInstanceOracleTrafficDirectorAdmin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905fef95f4809369728b6d7409444cc1e8ddd0fdcb8aa22fb833493a5f541d1e(
    *,
    port: typing.Optional[jsii.Number] = None,
    privileged_port: typing.Optional[jsii.Number] = None,
    privileged_secured_port: typing.Optional[jsii.Number] = None,
    secured_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f497ac65a1ec8e610a188f56f411c8f1dba509d88969b86161ff34559ccff800(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98529e32ef3fe27fad168569a3453d682a70b2ea1a506a814e2ae7b229a2df2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe576da923b117b018adf5af440cadca663f3b91988c18da2b8c91ecd5566055(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1754d626f4a74f86607de53a14f5c3788f3214295369f5a02e673b424819be10(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf0e37f2f141a453f34e5b017280e14fd39e5a11005016409771e563610790a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986328944d6d1d678730988bfea044d5c64ec7fa0194dd30e593c17de314ca07(
    value: typing.Optional[JavaServiceInstanceOracleTrafficDirectorListener],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b170966d200c0021168ec4db55f73165eebcbfa903f6178ee44f17cc605908(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d530b638fb33d96fc587bb96cb52b3ceb9603723482bb36f4486f86950dcac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e949af69d584595778109b957b5bb874b37065c9454b5f99d9ebb6abad14c25(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c866e4eb27715c6ce41c1022369ce57b036b9db29e4032cc49a750197eda81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbe60a4219ead223f39f6653d57036e8b994c33752faf741b610f4e646f001b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58a8181a1204e3c3a3f33ff5cc821b32c049a19e5e120ba072943c92f9d4aa4(
    value: typing.Optional[JavaServiceInstanceOracleTrafficDirector],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0daa175caee32960484845ad6958623d07e6b526f394a66b70144b8f0393a02(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf105956700cf3212c136440075b6a663c576689fa794fb8d36086a58ba56e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2629733e541ed0480ebfd5317b911303552fb14b79bafcd19374bd1b4ec8e720(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a1aeb443a46dd7802a4326fd1b086d4391debb6b48be70f4c3c880cd8a0607(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0132c7bf15ed00ffd0538bf146ab01888d6d7c01e0a8aee9f6569e4c982775(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6dd3cbedade7ab4b4d3e9a856fc8c247b511dc9b20fe0f62ce2aa18b52fe3ad(
    value: typing.Optional[typing.Union[JavaServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9cbebc096f258f93eb3cca77de349f1cfc1c0a4c0624a33c16a249e7b1ac970(
    *,
    admin: typing.Union[JavaServiceInstanceWeblogicServerAdmin, typing.Dict[builtins.str, typing.Any]],
    database: typing.Union[JavaServiceInstanceWeblogicServerDatabase, typing.Dict[builtins.str, typing.Any]],
    shape: builtins.str,
    application_database: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backup_volume_size: typing.Optional[builtins.str] = None,
    cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    connect_string: typing.Optional[builtins.str] = None,
    domain: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerDomain, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
    managed_servers: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerManagedServers, typing.Dict[builtins.str, typing.Any]]] = None,
    middleware_volume_size: typing.Optional[builtins.str] = None,
    node_manager: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerNodeManager, typing.Dict[builtins.str, typing.Any]]] = None,
    ports: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerPorts, typing.Dict[builtins.str, typing.Any]]] = None,
    upper_stack_product_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86fca180c73c14b729aeef30e4abfbf6a6033a8d7f3ccd2491e792d4d84ba65(
    *,
    password: builtins.str,
    username: builtins.str,
    port: typing.Optional[jsii.Number] = None,
    secured_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92061783050ad975609eddd617510349ff55b1125e81f4788f99cb77f7dc03c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde95323e66f8c7ebe6eb557509f679298aabc06555331a33205b209e09a9b54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a99795641be926180f1551c721050d5ce89ae74fadd2fc8583538eb970e004(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3dbfb001d3910a6d88903ecef6ac8e18e0591d707c8f820faa253268ae96abe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53142f79721eddcb082d30cf17cacc59f9ef592668add766d06446d5aba5a77b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f35a9590f83297fcf003f4f29795dc61151cd06099037f49f2792e697ef1e9cb(
    value: typing.Optional[JavaServiceInstanceWeblogicServerAdmin],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__315c86721236dcbc37d02282d9d5243df080d432939bc8f735057cadd548c898(
    *,
    name: builtins.str,
    password: builtins.str,
    username: builtins.str,
    pdb_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c75dcb83849e5800401c8e09006da10203e0a059b5a6515147c8f847afd3615(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7471b70748c3f1e3b407c10e58d1975e9b557fa2be8ccdb14b777f7d1887f027(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ffb8cdb938d650f6f6f7482214b40081387f9cd02681ae3017ddeb9e2b0c812(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c48b605d68453755b6f09f072d64faf72e84d8a26698ccc31e5177adfcab4b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaeaa7175297cd28a018a685b539984ce242de9e1042962b384b9d1196f4123e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4e85a865074d5f041236df9d11e9745ac4aa60323bbd8870573467fa2d9f25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerApplicationDatabase]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73845062bd05dbe481e4f87123dc87289aa7aa638592730a22fbdb3fe0d06991(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023774c353f18dfbe3d32a739bcaf59d367cb365d223ff89248b7f79f461d672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac200da060f25b711740a8bf1ef420a558874e0532c3feae074f3736bdc2b13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__effe961eedf58480d4ed745cc910c6e941c026312040bfd9c372b8ab45de74bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee1efb89f904c04a8a759e62e6717568afc98e04cc17c48a489f0fec3651baa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32ca66dccd4a3ca41342d8931a98f46021cd24b85c8d18d354d9c66d3ae90455(
    value: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54ecaf75755574ce3006a5c37e29f7706552287b04cb1cd797687d5a6b41b93(
    *,
    name: builtins.str,
    type: builtins.str,
    path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_count: typing.Optional[jsii.Number] = None,
    servers_per_node: typing.Optional[jsii.Number] = None,
    shape: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6bb7b45fb3ce6d0672703259daab37c7a28e5eecc8c479db26bda725e2e08c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0feb5211f3d80f43e99cd4b85c94f340e9eb4b9ac4948df7091f21d303c46379(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c527e046c52d0249562a98eae1ec16556fe5e4b9664ded3d8ef14f94226e29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a95b4edaa4308e4db03c000df0a9a046790ce2f67f2658eb04181852f7cd9d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f398d6ba79fa133ba01284e7f90ee83fe758ee8c63c5307490fe8e9c6e67ab5c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c45d93de4cb8410f344925f9c1d1e1f1f43730b187848050a072769e357c7b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[JavaServiceInstanceWeblogicServerCluster]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f941590731357ddb7931ef16d3e5b6adaff7ab0d803e32fadbfe98370681b06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3146e59d71316aa06f3f07a43a39a72604be7b48c5a63610730a715fa86b8e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__664aaefd95d9b9815f9da6f35e251a70ebd9d5937fb585d1f4508f4c78026ede(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9369b7798abfe2dab914fafda61773a20b027ef2e0a21768d8066c926553d67(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8658e7dbe425a66c16e4a4df5ef45a631d88d533a7df204b782c207d446068e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__383f7b669144a181bd3f8450d896f8ca6db5009e49a39cbaa5ce9208ea00ac5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24dc306a71fe5ad284a44666d5136bbf9031ca1299ff65ee7101432b9788c854(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f5eff617c8968b709eacf4fd8a0e940a4166a09f8b8bd1b01cac4bfc261792(
    value: typing.Optional[typing.Union[JavaServiceInstanceWeblogicServerCluster, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3b3eb6e5954a35a87f0884eafbd06adc480f6d9234720bc3b8717058e5e2b8(
    *,
    password: builtins.str,
    username: builtins.str,
    name: typing.Optional[builtins.str] = None,
    pdb_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c0649cf43f67c869b4f1d53f5648764d0b2e2bdb4ef8c74581353b273f9e4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669d4aec810932900765ec5a9a66985557b2ce7be314bf413cab260ed421912b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432bfd53e32674376ec21a12a2160686a1aa425d2fe1f7032ac7a22ae0ac8451(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3a4fe425770a7d7c60ef1d5c192e9c4cc9f0d71e923417baf3a49769778aba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c564fe96949bf157c02725e81418cef0d0f8014b781227b0e7876470a49d62f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__196f2e8249a143e413d7c17d38a66123b2c177a537ae41abf95f269af0a74887(
    value: typing.Optional[JavaServiceInstanceWeblogicServerDatabase],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b182ca59bdbe3f43240491639f1be174a13130a74fa763ba3f33970f3639ce(
    *,
    mode: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    partition_count: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb28c6da7339ebdaaa6ef25532d7e60f3043af083c078816725bd10b3f8daa7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f9b82017fa3e3dd4f45b704e1ca09987ccd78d851859861bc0c6ff83f60ce3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d408856f8117bbbf7a62f4ce104e236eef637eb8714c75f58a6cdbf9de399d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1ecdcc110a37c162a6b685ab01e4897fb131282be29a7747d583bc4e256e7f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2589f89cd1f93581790055258e1e50fd8a0a20511a1293e9766c34eaae95e722(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad80927cb98762de3f6edd6d3f486cadc2050af95694b9e8ba8ce4722493293b(
    value: typing.Optional[JavaServiceInstanceWeblogicServerDomain],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f93028a71062f998b37d3fbadb1ad3bc4bf252863319d3298e14712ce056a01(
    *,
    initial_heap_size: typing.Optional[jsii.Number] = None,
    initial_permanent_generation: typing.Optional[jsii.Number] = None,
    jvm_args: typing.Optional[builtins.str] = None,
    max_heap_size: typing.Optional[jsii.Number] = None,
    max_permanent_generation: typing.Optional[jsii.Number] = None,
    overwrite_jvm_args: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fef345546f20e7895bf62361f04c95e29e961b47c767ac964e2c12429a2be7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2245e665d54454396ee99a8198c198b08dad11401e69e5dd2bd169f424c01cb8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7b793c76289a757fc64d8985c993675797d458ebbc6602f47beea80160dbfa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdeed62437eae132cc811846c749b229d171b081e168c0e6f2d455e0a14f938(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bdddf0a83959438abdaffa1ba87cfef536b8d6363862a3d6def13c958232d21(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220c9eccc6982acc11f8d90100a39128ad316f595c2f7eb917f7fecd30d88367(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7987d87cf52b952337d19079a4edc55584374c0d3ee1e703ee17dedc653810b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eefd04ce3ca69a97abbed935adf2ac8adbb196c2d7557591051bf3b9a14ce89(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6663fee7fbfc147d342c9fddf93e652ad6e63a5f923e0a110c772a713082ce(
    value: typing.Optional[JavaServiceInstanceWeblogicServerManagedServers],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af8ba00b1b29bce9cbf8a826820c5290285810e62f883ef2f84faf5ec957b12(
    *,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1b7b5ac5dffdd1e1bd9c5c05fa0e7055211e672a6505432a3fe873c8711594(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b8787b3faa96766ddce7cd39fe4025b2e99f973cd54d4b1fcc9565138cace0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b00755878be74af212c23026b98d4563598c7d418de02917a90e0088e85d8d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cab4408ff967e78635b7761be6375c5b92a50e7dbc043602c3b93c6d97a5ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6e7634eefb4b6162ec15234fcd922bdb4bfe614918cd2db34c1202db9f06a1(
    value: typing.Optional[JavaServiceInstanceWeblogicServerNodeManager],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08da735734946bfb667254ac12c851f4e182d06b0cb39d2becd7f5f2ec96af2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32417420cd2eb2838f41413941a419b37307fbf7e3001888d45ebbf5b4a0d7a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerApplicationDatabase, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e8f84b8a26bae104568ae7e94b1d9e56518d0a0e5c6abf98d3740bea602138(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[JavaServiceInstanceWeblogicServerCluster, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd4c5c30d7213f9c6c5a360e0cd54f0fa1607da030020ed899ef8bb5914b462(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13276d008965230402331cb151d4f22c3c4bbfe2f089d0b6e0f91ddda00b3016(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152a1fdd65d9d24eea4c782241ed48c56683e43739403480aeaddef9838aa01f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f95533256997e86262f00b55bb834c82118d76cadd818654e80c45efbc0768(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dabc551ce75aa5b22c8cef9068f884ab9d9f6e6f76fd69779556d7c5a49d525(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e06f21e07a77bdc381ff769f9b25697f2bc3b22688ec0d7bdd74296d3e6969e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2048e323f2668e0f9f10ec00a2260e12f4df225af9af34deef3b10e16ef7c172(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104413b49a0a8fb794d29e12e08c7fbf300c4d5e6d6bd90b7c1829cc344c4386(
    value: typing.Optional[JavaServiceInstanceWeblogicServer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c0b7013f7803bd409c54620f0a6818b3847a72087aec8f46c0b6588956728d(
    *,
    content_port: typing.Optional[jsii.Number] = None,
    deployment_channel_port: typing.Optional[jsii.Number] = None,
    privileged_content_port: typing.Optional[jsii.Number] = None,
    privileged_secured_content_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae5058e805b17d2e33ad2cadc78cbdbb16e24f4c92fca6eff5ba9d501735450f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b62ce9b9b04283e8806ce8486b4ba7fbdf99ee0d82d27eb336db821607ed9e5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27086b1d2baee13af4294a559da0e40967a9364acbb9568a52736ec617815a5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a19a3523fa49750a01fd131415be92578489b6d610cb37e139c9093a99970d4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d135c8ea9c020d42d3983eee20a1f4fc9f8d90f213d98d3dc6f968bfe187bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a22a8f765ffa8e4d0eaf16939d753c279a0b40ba25b36807ba0665da0fbf73(
    value: typing.Optional[JavaServiceInstanceWeblogicServerPorts],
) -> None:
    """Type checking stubs"""
    pass
