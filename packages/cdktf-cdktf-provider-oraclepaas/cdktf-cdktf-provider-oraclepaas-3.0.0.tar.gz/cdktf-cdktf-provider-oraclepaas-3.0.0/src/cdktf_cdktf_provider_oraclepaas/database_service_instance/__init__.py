'''
# `oraclepaas_database_service_instance`

Refer to the Terraform Registory for docs: [`oraclepaas_database_service_instance`](https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance).
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


class DatabaseServiceInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance oraclepaas_database_service_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database_configuration: typing.Union["DatabaseServiceInstanceDatabaseConfiguration", typing.Dict[builtins.str, typing.Any]],
        edition: builtins.str,
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        subscription_type: builtins.str,
        version: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union["DatabaseServiceInstanceBackups", typing.Dict[builtins.str, typing.Any]]] = None,
        bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_access_rules: typing.Optional[typing.Union["DatabaseServiceInstanceDefaultAccessRules", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        high_performance_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hybrid_disaster_recovery: typing.Optional[typing.Union["DatabaseServiceInstanceHybridDisasterRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        instantiate_from_backup: typing.Optional[typing.Union["DatabaseServiceInstanceInstantiateFromBackup", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_network: typing.Optional[builtins.str] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        level: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        standby: typing.Optional[typing.Union["DatabaseServiceInstanceStandby", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DatabaseServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance oraclepaas_database_service_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_configuration: database_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_configuration DatabaseServiceInstance#database_configuration}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#edition DatabaseServiceInstance#edition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#name DatabaseServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#shape DatabaseServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ssh_public_key DatabaseServiceInstance#ssh_public_key}.
        :param subscription_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subscription_type DatabaseServiceInstance#subscription_type}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#version DatabaseServiceInstance#version}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backups DatabaseServiceInstance#backups}
        :param bring_your_own_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#bring_your_own_license DatabaseServiceInstance#bring_your_own_license}.
        :param default_access_rules: default_access_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#default_access_rules DatabaseServiceInstance#default_access_rules}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#description DatabaseServiceInstance#description}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#desired_state DatabaseServiceInstance#desired_state}.
        :param high_performance_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#high_performance_storage DatabaseServiceInstance#high_performance_storage}.
        :param hybrid_disaster_recovery: hybrid_disaster_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#hybrid_disaster_recovery DatabaseServiceInstance#hybrid_disaster_recovery}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#id DatabaseServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instantiate_from_backup: instantiate_from_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#instantiate_from_backup DatabaseServiceInstance#instantiate_from_backup}
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_network DatabaseServiceInstance#ip_network}.
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_reservations DatabaseServiceInstance#ip_reservations}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#level DatabaseServiceInstance#level}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#notification_email DatabaseServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#region DatabaseServiceInstance#region}.
        :param standby: standby block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#standby DatabaseServiceInstance#standby}
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timeouts DatabaseServiceInstance#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa73e3345bc57a92cb55c5471318dd7e91661635157f348786bc0edbeed5407d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatabaseServiceInstanceConfig(
            database_configuration=database_configuration,
            edition=edition,
            name=name,
            shape=shape,
            ssh_public_key=ssh_public_key,
            subscription_type=subscription_type,
            version=version,
            availability_domain=availability_domain,
            backups=backups,
            bring_your_own_license=bring_your_own_license,
            default_access_rules=default_access_rules,
            description=description,
            desired_state=desired_state,
            high_performance_storage=high_performance_storage,
            hybrid_disaster_recovery=hybrid_disaster_recovery,
            id=id,
            instantiate_from_backup=instantiate_from_backup,
            ip_network=ip_network,
            ip_reservations=ip_reservations,
            level=level,
            notification_email=notification_email,
            region=region,
            standby=standby,
            subnet=subnet,
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

    @jsii.member(jsii_name="putBackups")
    def put_backups(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        create_if_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create_if_missing DatabaseServiceInstance#create_if_missing}.
        '''
        value = DatabaseServiceInstanceBackups(
            cloud_storage_container=cloud_storage_container,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
            create_if_missing=create_if_missing,
        )

        return typing.cast(None, jsii.invoke(self, "putBackups", [value]))

    @jsii.member(jsii_name="putDatabaseConfiguration")
    def put_database_configuration(
        self,
        *,
        admin_password: builtins.str,
        usable_storage: jsii.Number,
        backup_destination: typing.Optional[builtins.str] = None,
        backup_storage_volume_size: typing.Optional[jsii.Number] = None,
        character_set: typing.Optional[builtins.str] = None,
        data_storage_volume_size: typing.Optional[jsii.Number] = None,
        db_demo: typing.Optional[builtins.str] = None,
        disaster_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failover_database: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        golden_gate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        is_rac: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        national_character_set: typing.Optional[builtins.str] = None,
        pdb_name: typing.Optional[builtins.str] = None,
        sid: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#admin_password DatabaseServiceInstance#admin_password}.
        :param usable_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#usable_storage DatabaseServiceInstance#usable_storage}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_destination DatabaseServiceInstance#backup_destination}.
        :param backup_storage_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_storage_volume_size DatabaseServiceInstance#backup_storage_volume_size}.
        :param character_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#character_set DatabaseServiceInstance#character_set}.
        :param data_storage_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#data_storage_volume_size DatabaseServiceInstance#data_storage_volume_size}.
        :param db_demo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#db_demo DatabaseServiceInstance#db_demo}.
        :param disaster_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#disaster_recovery DatabaseServiceInstance#disaster_recovery}.
        :param failover_database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#failover_database DatabaseServiceInstance#failover_database}.
        :param golden_gate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#golden_gate DatabaseServiceInstance#golden_gate}.
        :param is_rac: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#is_rac DatabaseServiceInstance#is_rac}.
        :param national_character_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#national_character_set DatabaseServiceInstance#national_character_set}.
        :param pdb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#pdb_name DatabaseServiceInstance#pdb_name}.
        :param sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#sid DatabaseServiceInstance#sid}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#snapshot_name DatabaseServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#source_service_name DatabaseServiceInstance#source_service_name}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timezone DatabaseServiceInstance#timezone}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#type DatabaseServiceInstance#type}.
        '''
        value = DatabaseServiceInstanceDatabaseConfiguration(
            admin_password=admin_password,
            usable_storage=usable_storage,
            backup_destination=backup_destination,
            backup_storage_volume_size=backup_storage_volume_size,
            character_set=character_set,
            data_storage_volume_size=data_storage_volume_size,
            db_demo=db_demo,
            disaster_recovery=disaster_recovery,
            failover_database=failover_database,
            golden_gate=golden_gate,
            is_rac=is_rac,
            national_character_set=national_character_set,
            pdb_name=pdb_name,
            sid=sid,
            snapshot_name=snapshot_name,
            source_service_name=source_service_name,
            timezone=timezone,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putDatabaseConfiguration", [value]))

    @jsii.member(jsii_name="putDefaultAccessRules")
    def put_default_access_rules(
        self,
        *,
        enable_db_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_db_express: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_em_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_http: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_http_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rac_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rac_ons: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_scan_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_ssh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_db_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_console DatabaseServiceInstance#enable_db_console}.
        :param enable_db_express: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_express DatabaseServiceInstance#enable_db_express}.
        :param enable_db_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_listener DatabaseServiceInstance#enable_db_listener}.
        :param enable_em_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_em_console DatabaseServiceInstance#enable_em_console}.
        :param enable_http: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http DatabaseServiceInstance#enable_http}.
        :param enable_http_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http_ssl DatabaseServiceInstance#enable_http_ssl}.
        :param enable_rac_db_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_db_listener DatabaseServiceInstance#enable_rac_db_listener}.
        :param enable_rac_ons: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_ons DatabaseServiceInstance#enable_rac_ons}.
        :param enable_scan_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_scan_listener DatabaseServiceInstance#enable_scan_listener}.
        :param enable_ssh: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_ssh DatabaseServiceInstance#enable_ssh}.
        '''
        value = DatabaseServiceInstanceDefaultAccessRules(
            enable_db_console=enable_db_console,
            enable_db_express=enable_db_express,
            enable_db_listener=enable_db_listener,
            enable_em_console=enable_em_console,
            enable_http=enable_http,
            enable_http_ssl=enable_http_ssl,
            enable_rac_db_listener=enable_rac_db_listener,
            enable_rac_ons=enable_rac_ons,
            enable_scan_listener=enable_scan_listener,
            enable_ssh=enable_ssh,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultAccessRules", [value]))

    @jsii.member(jsii_name="putHybridDisasterRecovery")
    def put_hybrid_disaster_recovery(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        '''
        value = DatabaseServiceInstanceHybridDisasterRecovery(
            cloud_storage_container=cloud_storage_container,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
        )

        return typing.cast(None, jsii.invoke(self, "putHybridDisasterRecovery", [value]))

    @jsii.member(jsii_name="putInstantiateFromBackup")
    def put_instantiate_from_backup(
        self,
        *,
        cloud_storage_container: builtins.str,
        database_id: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        decryption_key: typing.Optional[builtins.str] = None,
        on_premise: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_id: typing.Optional[builtins.str] = None,
        wallet_file_content: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_id DatabaseServiceInstance#database_id}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        :param decryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#decryption_key DatabaseServiceInstance#decryption_key}.
        :param on_premise: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#on_premise DatabaseServiceInstance#on_premise}.
        :param service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#service_id DatabaseServiceInstance#service_id}.
        :param wallet_file_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#wallet_file_content DatabaseServiceInstance#wallet_file_content}.
        '''
        value = DatabaseServiceInstanceInstantiateFromBackup(
            cloud_storage_container=cloud_storage_container,
            database_id=database_id,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
            decryption_key=decryption_key,
            on_premise=on_premise,
            service_id=service_id,
            wallet_file_content=wallet_file_content,
        )

        return typing.cast(None, jsii.invoke(self, "putInstantiateFromBackup", [value]))

    @jsii.member(jsii_name="putStandby")
    def put_standby(
        self,
        *,
        availability_domain: builtins.str,
        subnet: builtins.str,
    ) -> None:
        '''
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.
        '''
        value = DatabaseServiceInstanceStandby(
            availability_domain=availability_domain, subnet=subnet
        )

        return typing.cast(None, jsii.invoke(self, "putStandby", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create DatabaseServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#delete DatabaseServiceInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#update DatabaseServiceInstance#update}.
        '''
        value = DatabaseServiceInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAvailabilityDomain")
    def reset_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityDomain", []))

    @jsii.member(jsii_name="resetBackups")
    def reset_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackups", []))

    @jsii.member(jsii_name="resetBringYourOwnLicense")
    def reset_bring_your_own_license(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBringYourOwnLicense", []))

    @jsii.member(jsii_name="resetDefaultAccessRules")
    def reset_default_access_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAccessRules", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetHighPerformanceStorage")
    def reset_high_performance_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighPerformanceStorage", []))

    @jsii.member(jsii_name="resetHybridDisasterRecovery")
    def reset_hybrid_disaster_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHybridDisasterRecovery", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstantiateFromBackup")
    def reset_instantiate_from_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstantiateFromBackup", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetIpReservations")
    def reset_ip_reservations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpReservations", []))

    @jsii.member(jsii_name="resetLevel")
    def reset_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevel", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetStandby")
    def reset_standby(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandby", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

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
    @jsii.member(jsii_name="backups")
    def backups(self) -> "DatabaseServiceInstanceBackupsOutputReference":
        return typing.cast("DatabaseServiceInstanceBackupsOutputReference", jsii.get(self, "backups"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @builtins.property
    @jsii.member(jsii_name="computeSiteName")
    def compute_site_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computeSiteName"))

    @builtins.property
    @jsii.member(jsii_name="databaseConfiguration")
    def database_configuration(
        self,
    ) -> "DatabaseServiceInstanceDatabaseConfigurationOutputReference":
        return typing.cast("DatabaseServiceInstanceDatabaseConfigurationOutputReference", jsii.get(self, "databaseConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dbaasMonitorUrl")
    def dbaas_monitor_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbaasMonitorUrl"))

    @builtins.property
    @jsii.member(jsii_name="defaultAccessRules")
    def default_access_rules(
        self,
    ) -> "DatabaseServiceInstanceDefaultAccessRulesOutputReference":
        return typing.cast("DatabaseServiceInstanceDefaultAccessRulesOutputReference", jsii.get(self, "defaultAccessRules"))

    @builtins.property
    @jsii.member(jsii_name="emUrl")
    def em_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emUrl"))

    @builtins.property
    @jsii.member(jsii_name="glassfishUrl")
    def glassfish_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "glassfishUrl"))

    @builtins.property
    @jsii.member(jsii_name="hybridDisasterRecovery")
    def hybrid_disaster_recovery(
        self,
    ) -> "DatabaseServiceInstanceHybridDisasterRecoveryOutputReference":
        return typing.cast("DatabaseServiceInstanceHybridDisasterRecoveryOutputReference", jsii.get(self, "hybridDisasterRecovery"))

    @builtins.property
    @jsii.member(jsii_name="identityDomain")
    def identity_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityDomain"))

    @builtins.property
    @jsii.member(jsii_name="instantiateFromBackup")
    def instantiate_from_backup(
        self,
    ) -> "DatabaseServiceInstanceInstantiateFromBackupOutputReference":
        return typing.cast("DatabaseServiceInstanceInstantiateFromBackupOutputReference", jsii.get(self, "instantiateFromBackup"))

    @builtins.property
    @jsii.member(jsii_name="standby")
    def standby(self) -> "DatabaseServiceInstanceStandbyOutputReference":
        return typing.cast("DatabaseServiceInstanceStandbyOutputReference", jsii.get(self, "standby"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DatabaseServiceInstanceTimeoutsOutputReference":
        return typing.cast("DatabaseServiceInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomainInput")
    def availability_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="backupsInput")
    def backups_input(self) -> typing.Optional["DatabaseServiceInstanceBackups"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceBackups"], jsii.get(self, "backupsInput"))

    @builtins.property
    @jsii.member(jsii_name="bringYourOwnLicenseInput")
    def bring_your_own_license_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "bringYourOwnLicenseInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseConfigurationInput")
    def database_configuration_input(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceDatabaseConfiguration"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceDatabaseConfiguration"], jsii.get(self, "databaseConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAccessRulesInput")
    def default_access_rules_input(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceDefaultAccessRules"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceDefaultAccessRules"], jsii.get(self, "defaultAccessRulesInput"))

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
    @jsii.member(jsii_name="highPerformanceStorageInput")
    def high_performance_storage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "highPerformanceStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="hybridDisasterRecoveryInput")
    def hybrid_disaster_recovery_input(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceHybridDisasterRecovery"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceHybridDisasterRecovery"], jsii.get(self, "hybridDisasterRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instantiateFromBackupInput")
    def instantiate_from_backup_input(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceInstantiateFromBackup"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceInstantiateFromBackup"], jsii.get(self, "instantiateFromBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="ipReservationsInput")
    def ip_reservations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipReservationsInput"))

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailInput")
    def notification_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeyInput")
    def ssh_public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="standbyInput")
    def standby_input(self) -> typing.Optional["DatabaseServiceInstanceStandby"]:
        return typing.cast(typing.Optional["DatabaseServiceInstanceStandby"], jsii.get(self, "standbyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionTypeInput")
    def subscription_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DatabaseServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DatabaseServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51cb440b977cdb514ba8edd18e6174b2f6d843161716129d0d172dc27bebb6e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__9bef6d59a8528132c6a5c10418c924454d1155d2bc75cbc8398ad22ccc861a6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bringYourOwnLicense", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262b32b9aa830bd48ec3e8d613a9a6f7898b88e3e9d5a0815a79b265da2fee94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a484712c9ef3c2295f5816f940a1c8d684da90cd1c575967688121b3f5f2ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc50b45ab556bfd2c96176a4249e3f60b8369cf0ca37a373ab960bd0c8ce0411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="highPerformanceStorage")
    def high_performance_storage(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "highPerformanceStorage"))

    @high_performance_storage.setter
    def high_performance_storage(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894070b110cfcac47ea66ec2a57a8af6e88710341e7955e3c251f8e9820d777f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "highPerformanceStorage", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bef5afe8a9c52ab3c847f5b77871c533e25558794b0899c0f29a68c093721fd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__807626eff852236fd01e30dcf2a4dd4e24a04411c6cdd439bb0409be46d69a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="ipReservations")
    def ip_reservations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipReservations"))

    @ip_reservations.setter
    def ip_reservations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38477cbc7d5eff468025818cdd6967657afb7eab7e8c8b0f98a6d5dd53e48745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipReservations", value)

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c55be471b42f22de7dd985a91a7b6ed5fcc8b7ef47945d7168ba166f4d9cf5a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c33f86f0cb5cb47b901be0bd0536a2c71ac21e2621030159403c0a4e40f3af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0756adc3990f35fd762c56b94506a8c3fc63fdf1d2bc2c6fe2e676fca6fefff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57feadaa6cba84b3cc27a1146383e42fa50f39e95c7a8e056513cd32e5aef2b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbe38dba8afa82a574116d20e9f2f96a8b392b9c856407f3dcb5e2674c3d9ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43605d831243fe51821a9c0a28c26dc30c03e0b0afc8b911911f16082c3aa9ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca93c644004ee94be928111105e70a46cd386192eb6ec1ee1340b14983983198)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionType")
    def subscription_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionType"))

    @subscription_type.setter
    def subscription_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b64b3bb5f85c06a857b70fc26445ad0b71f56cc487c742a3e2d0eb83a15eeb2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionType", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e539c31ca3d45ec2ccc9bb2e8cf377cd49d581babc35ffc32a6e6937093d7fa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceBackups",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
        "create_if_missing": "createIfMissing",
    },
)
class DatabaseServiceInstanceBackups:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        create_if_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create_if_missing DatabaseServiceInstance#create_if_missing}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db875cae9cdc0dda352651b3890ae5ec4e460ddbced51614cdd0a01c6075474)
            check_type(argname="argument cloud_storage_container", value=cloud_storage_container, expected_type=type_hints["cloud_storage_container"])
            check_type(argname="argument cloud_storage_password", value=cloud_storage_password, expected_type=type_hints["cloud_storage_password"])
            check_type(argname="argument cloud_storage_username", value=cloud_storage_username, expected_type=type_hints["cloud_storage_username"])
            check_type(argname="argument create_if_missing", value=create_if_missing, expected_type=type_hints["create_if_missing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_storage_container": cloud_storage_container,
        }
        if cloud_storage_password is not None:
            self._values["cloud_storage_password"] = cloud_storage_password
        if cloud_storage_username is not None:
            self._values["cloud_storage_username"] = cloud_storage_username
        if create_if_missing is not None:
            self._values["create_if_missing"] = create_if_missing

    @builtins.property
    def cloud_storage_container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_if_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create_if_missing DatabaseServiceInstance#create_if_missing}.'''
        result = self._values.get("create_if_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceBackups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceBackupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceBackupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9c80f6b4e1eeb22d028a58c23f7dc26ba1abfa5e420f4da430e780888af678a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudStoragePassword")
    def reset_cloud_storage_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePassword", []))

    @jsii.member(jsii_name="resetCloudStorageUsername")
    def reset_cloud_storage_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageUsername", []))

    @jsii.member(jsii_name="resetCreateIfMissing")
    def reset_create_if_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateIfMissing", []))

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
    @jsii.member(jsii_name="createIfMissingInput")
    def create_if_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "createIfMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @cloud_storage_container.setter
    def cloud_storage_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e22bc388a25f47d7030f06ac5661e1513d42328689a451f67117b6d47d23e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9673783138cb0bff360d45f7b963924bed96ad0f003d5863b135d5d39b99e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98b1f8209ebb2ef4b05f0796e0b5aec9616ab30305da3bd38922316541c1da0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageUsername", value)

    @builtins.property
    @jsii.member(jsii_name="createIfMissing")
    def create_if_missing(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "createIfMissing"))

    @create_if_missing.setter
    def create_if_missing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8f028aba71095f35a73b8cf00ff4c859db079a85a49ebcb98f8a51dd7c6fdc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIfMissing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseServiceInstanceBackups]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceBackups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceBackups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24edaa2c8d06fac4fdf69186d7a4d8c72ecb2db6268367d79442c5dff1876f24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_configuration": "databaseConfiguration",
        "edition": "edition",
        "name": "name",
        "shape": "shape",
        "ssh_public_key": "sshPublicKey",
        "subscription_type": "subscriptionType",
        "version": "version",
        "availability_domain": "availabilityDomain",
        "backups": "backups",
        "bring_your_own_license": "bringYourOwnLicense",
        "default_access_rules": "defaultAccessRules",
        "description": "description",
        "desired_state": "desiredState",
        "high_performance_storage": "highPerformanceStorage",
        "hybrid_disaster_recovery": "hybridDisasterRecovery",
        "id": "id",
        "instantiate_from_backup": "instantiateFromBackup",
        "ip_network": "ipNetwork",
        "ip_reservations": "ipReservations",
        "level": "level",
        "notification_email": "notificationEmail",
        "region": "region",
        "standby": "standby",
        "subnet": "subnet",
        "timeouts": "timeouts",
    },
)
class DatabaseServiceInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database_configuration: typing.Union["DatabaseServiceInstanceDatabaseConfiguration", typing.Dict[builtins.str, typing.Any]],
        edition: builtins.str,
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        subscription_type: builtins.str,
        version: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union[DatabaseServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
        bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        default_access_rules: typing.Optional[typing.Union["DatabaseServiceInstanceDefaultAccessRules", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_state: typing.Optional[builtins.str] = None,
        high_performance_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        hybrid_disaster_recovery: typing.Optional[typing.Union["DatabaseServiceInstanceHybridDisasterRecovery", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        instantiate_from_backup: typing.Optional[typing.Union["DatabaseServiceInstanceInstantiateFromBackup", typing.Dict[builtins.str, typing.Any]]] = None,
        ip_network: typing.Optional[builtins.str] = None,
        ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
        level: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        standby: typing.Optional[typing.Union["DatabaseServiceInstanceStandby", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DatabaseServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_configuration: database_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_configuration DatabaseServiceInstance#database_configuration}
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#edition DatabaseServiceInstance#edition}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#name DatabaseServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#shape DatabaseServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ssh_public_key DatabaseServiceInstance#ssh_public_key}.
        :param subscription_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subscription_type DatabaseServiceInstance#subscription_type}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#version DatabaseServiceInstance#version}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backups DatabaseServiceInstance#backups}
        :param bring_your_own_license: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#bring_your_own_license DatabaseServiceInstance#bring_your_own_license}.
        :param default_access_rules: default_access_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#default_access_rules DatabaseServiceInstance#default_access_rules}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#description DatabaseServiceInstance#description}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#desired_state DatabaseServiceInstance#desired_state}.
        :param high_performance_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#high_performance_storage DatabaseServiceInstance#high_performance_storage}.
        :param hybrid_disaster_recovery: hybrid_disaster_recovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#hybrid_disaster_recovery DatabaseServiceInstance#hybrid_disaster_recovery}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#id DatabaseServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instantiate_from_backup: instantiate_from_backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#instantiate_from_backup DatabaseServiceInstance#instantiate_from_backup}
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_network DatabaseServiceInstance#ip_network}.
        :param ip_reservations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_reservations DatabaseServiceInstance#ip_reservations}.
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#level DatabaseServiceInstance#level}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#notification_email DatabaseServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#region DatabaseServiceInstance#region}.
        :param standby: standby block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#standby DatabaseServiceInstance#standby}
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timeouts DatabaseServiceInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(database_configuration, dict):
            database_configuration = DatabaseServiceInstanceDatabaseConfiguration(**database_configuration)
        if isinstance(backups, dict):
            backups = DatabaseServiceInstanceBackups(**backups)
        if isinstance(default_access_rules, dict):
            default_access_rules = DatabaseServiceInstanceDefaultAccessRules(**default_access_rules)
        if isinstance(hybrid_disaster_recovery, dict):
            hybrid_disaster_recovery = DatabaseServiceInstanceHybridDisasterRecovery(**hybrid_disaster_recovery)
        if isinstance(instantiate_from_backup, dict):
            instantiate_from_backup = DatabaseServiceInstanceInstantiateFromBackup(**instantiate_from_backup)
        if isinstance(standby, dict):
            standby = DatabaseServiceInstanceStandby(**standby)
        if isinstance(timeouts, dict):
            timeouts = DatabaseServiceInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e955c443bb288e6d32a8a4b725d45921c3abc7c249e736b6082db3defa98be7a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_configuration", value=database_configuration, expected_type=type_hints["database_configuration"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument subscription_type", value=subscription_type, expected_type=type_hints["subscription_type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument backups", value=backups, expected_type=type_hints["backups"])
            check_type(argname="argument bring_your_own_license", value=bring_your_own_license, expected_type=type_hints["bring_your_own_license"])
            check_type(argname="argument default_access_rules", value=default_access_rules, expected_type=type_hints["default_access_rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument high_performance_storage", value=high_performance_storage, expected_type=type_hints["high_performance_storage"])
            check_type(argname="argument hybrid_disaster_recovery", value=hybrid_disaster_recovery, expected_type=type_hints["hybrid_disaster_recovery"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instantiate_from_backup", value=instantiate_from_backup, expected_type=type_hints["instantiate_from_backup"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument ip_reservations", value=ip_reservations, expected_type=type_hints["ip_reservations"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument standby", value=standby, expected_type=type_hints["standby"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_configuration": database_configuration,
            "edition": edition,
            "name": name,
            "shape": shape,
            "ssh_public_key": ssh_public_key,
            "subscription_type": subscription_type,
            "version": version,
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
        if availability_domain is not None:
            self._values["availability_domain"] = availability_domain
        if backups is not None:
            self._values["backups"] = backups
        if bring_your_own_license is not None:
            self._values["bring_your_own_license"] = bring_your_own_license
        if default_access_rules is not None:
            self._values["default_access_rules"] = default_access_rules
        if description is not None:
            self._values["description"] = description
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if high_performance_storage is not None:
            self._values["high_performance_storage"] = high_performance_storage
        if hybrid_disaster_recovery is not None:
            self._values["hybrid_disaster_recovery"] = hybrid_disaster_recovery
        if id is not None:
            self._values["id"] = id
        if instantiate_from_backup is not None:
            self._values["instantiate_from_backup"] = instantiate_from_backup
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if ip_reservations is not None:
            self._values["ip_reservations"] = ip_reservations
        if level is not None:
            self._values["level"] = level
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if region is not None:
            self._values["region"] = region
        if standby is not None:
            self._values["standby"] = standby
        if subnet is not None:
            self._values["subnet"] = subnet
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
    def database_configuration(self) -> "DatabaseServiceInstanceDatabaseConfiguration":
        '''database_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_configuration DatabaseServiceInstance#database_configuration}
        '''
        result = self._values.get("database_configuration")
        assert result is not None, "Required property 'database_configuration' is missing"
        return typing.cast("DatabaseServiceInstanceDatabaseConfiguration", result)

    @builtins.property
    def edition(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#edition DatabaseServiceInstance#edition}.'''
        result = self._values.get("edition")
        assert result is not None, "Required property 'edition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#name DatabaseServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#shape DatabaseServiceInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ssh_public_key DatabaseServiceInstance#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        assert result is not None, "Required property 'ssh_public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subscription_type DatabaseServiceInstance#subscription_type}.'''
        result = self._values.get("subscription_type")
        assert result is not None, "Required property 'subscription_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#version DatabaseServiceInstance#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.'''
        result = self._values.get("availability_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backups(self) -> typing.Optional[DatabaseServiceInstanceBackups]:
        '''backups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backups DatabaseServiceInstance#backups}
        '''
        result = self._values.get("backups")
        return typing.cast(typing.Optional[DatabaseServiceInstanceBackups], result)

    @builtins.property
    def bring_your_own_license(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#bring_your_own_license DatabaseServiceInstance#bring_your_own_license}.'''
        result = self._values.get("bring_your_own_license")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def default_access_rules(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceDefaultAccessRules"]:
        '''default_access_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#default_access_rules DatabaseServiceInstance#default_access_rules}
        '''
        result = self._values.get("default_access_rules")
        return typing.cast(typing.Optional["DatabaseServiceInstanceDefaultAccessRules"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#description DatabaseServiceInstance#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#desired_state DatabaseServiceInstance#desired_state}.'''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def high_performance_storage(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#high_performance_storage DatabaseServiceInstance#high_performance_storage}.'''
        result = self._values.get("high_performance_storage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def hybrid_disaster_recovery(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceHybridDisasterRecovery"]:
        '''hybrid_disaster_recovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#hybrid_disaster_recovery DatabaseServiceInstance#hybrid_disaster_recovery}
        '''
        result = self._values.get("hybrid_disaster_recovery")
        return typing.cast(typing.Optional["DatabaseServiceInstanceHybridDisasterRecovery"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#id DatabaseServiceInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instantiate_from_backup(
        self,
    ) -> typing.Optional["DatabaseServiceInstanceInstantiateFromBackup"]:
        '''instantiate_from_backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#instantiate_from_backup DatabaseServiceInstance#instantiate_from_backup}
        '''
        result = self._values.get("instantiate_from_backup")
        return typing.cast(typing.Optional["DatabaseServiceInstanceInstantiateFromBackup"], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_network DatabaseServiceInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_reservations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#ip_reservations DatabaseServiceInstance#ip_reservations}.'''
        result = self._values.get("ip_reservations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#level DatabaseServiceInstance#level}.'''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#notification_email DatabaseServiceInstance#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#region DatabaseServiceInstance#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standby(self) -> typing.Optional["DatabaseServiceInstanceStandby"]:
        '''standby block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#standby DatabaseServiceInstance#standby}
        '''
        result = self._values.get("standby")
        return typing.cast(typing.Optional["DatabaseServiceInstanceStandby"], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.'''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DatabaseServiceInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timeouts DatabaseServiceInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DatabaseServiceInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceDatabaseConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "admin_password": "adminPassword",
        "usable_storage": "usableStorage",
        "backup_destination": "backupDestination",
        "backup_storage_volume_size": "backupStorageVolumeSize",
        "character_set": "characterSet",
        "data_storage_volume_size": "dataStorageVolumeSize",
        "db_demo": "dbDemo",
        "disaster_recovery": "disasterRecovery",
        "failover_database": "failoverDatabase",
        "golden_gate": "goldenGate",
        "is_rac": "isRac",
        "national_character_set": "nationalCharacterSet",
        "pdb_name": "pdbName",
        "sid": "sid",
        "snapshot_name": "snapshotName",
        "source_service_name": "sourceServiceName",
        "timezone": "timezone",
        "type": "type",
    },
)
class DatabaseServiceInstanceDatabaseConfiguration:
    def __init__(
        self,
        *,
        admin_password: builtins.str,
        usable_storage: jsii.Number,
        backup_destination: typing.Optional[builtins.str] = None,
        backup_storage_volume_size: typing.Optional[jsii.Number] = None,
        character_set: typing.Optional[builtins.str] = None,
        data_storage_volume_size: typing.Optional[jsii.Number] = None,
        db_demo: typing.Optional[builtins.str] = None,
        disaster_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        failover_database: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        golden_gate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        is_rac: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        national_character_set: typing.Optional[builtins.str] = None,
        pdb_name: typing.Optional[builtins.str] = None,
        sid: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#admin_password DatabaseServiceInstance#admin_password}.
        :param usable_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#usable_storage DatabaseServiceInstance#usable_storage}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_destination DatabaseServiceInstance#backup_destination}.
        :param backup_storage_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_storage_volume_size DatabaseServiceInstance#backup_storage_volume_size}.
        :param character_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#character_set DatabaseServiceInstance#character_set}.
        :param data_storage_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#data_storage_volume_size DatabaseServiceInstance#data_storage_volume_size}.
        :param db_demo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#db_demo DatabaseServiceInstance#db_demo}.
        :param disaster_recovery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#disaster_recovery DatabaseServiceInstance#disaster_recovery}.
        :param failover_database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#failover_database DatabaseServiceInstance#failover_database}.
        :param golden_gate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#golden_gate DatabaseServiceInstance#golden_gate}.
        :param is_rac: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#is_rac DatabaseServiceInstance#is_rac}.
        :param national_character_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#national_character_set DatabaseServiceInstance#national_character_set}.
        :param pdb_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#pdb_name DatabaseServiceInstance#pdb_name}.
        :param sid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#sid DatabaseServiceInstance#sid}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#snapshot_name DatabaseServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#source_service_name DatabaseServiceInstance#source_service_name}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timezone DatabaseServiceInstance#timezone}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#type DatabaseServiceInstance#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c082223846b1d1d20195b0cf7d00a76b618d11d08cc1b8e408d87b982919bb3)
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument usable_storage", value=usable_storage, expected_type=type_hints["usable_storage"])
            check_type(argname="argument backup_destination", value=backup_destination, expected_type=type_hints["backup_destination"])
            check_type(argname="argument backup_storage_volume_size", value=backup_storage_volume_size, expected_type=type_hints["backup_storage_volume_size"])
            check_type(argname="argument character_set", value=character_set, expected_type=type_hints["character_set"])
            check_type(argname="argument data_storage_volume_size", value=data_storage_volume_size, expected_type=type_hints["data_storage_volume_size"])
            check_type(argname="argument db_demo", value=db_demo, expected_type=type_hints["db_demo"])
            check_type(argname="argument disaster_recovery", value=disaster_recovery, expected_type=type_hints["disaster_recovery"])
            check_type(argname="argument failover_database", value=failover_database, expected_type=type_hints["failover_database"])
            check_type(argname="argument golden_gate", value=golden_gate, expected_type=type_hints["golden_gate"])
            check_type(argname="argument is_rac", value=is_rac, expected_type=type_hints["is_rac"])
            check_type(argname="argument national_character_set", value=national_character_set, expected_type=type_hints["national_character_set"])
            check_type(argname="argument pdb_name", value=pdb_name, expected_type=type_hints["pdb_name"])
            check_type(argname="argument sid", value=sid, expected_type=type_hints["sid"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument source_service_name", value=source_service_name, expected_type=type_hints["source_service_name"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_password": admin_password,
            "usable_storage": usable_storage,
        }
        if backup_destination is not None:
            self._values["backup_destination"] = backup_destination
        if backup_storage_volume_size is not None:
            self._values["backup_storage_volume_size"] = backup_storage_volume_size
        if character_set is not None:
            self._values["character_set"] = character_set
        if data_storage_volume_size is not None:
            self._values["data_storage_volume_size"] = data_storage_volume_size
        if db_demo is not None:
            self._values["db_demo"] = db_demo
        if disaster_recovery is not None:
            self._values["disaster_recovery"] = disaster_recovery
        if failover_database is not None:
            self._values["failover_database"] = failover_database
        if golden_gate is not None:
            self._values["golden_gate"] = golden_gate
        if is_rac is not None:
            self._values["is_rac"] = is_rac
        if national_character_set is not None:
            self._values["national_character_set"] = national_character_set
        if pdb_name is not None:
            self._values["pdb_name"] = pdb_name
        if sid is not None:
            self._values["sid"] = sid
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if source_service_name is not None:
            self._values["source_service_name"] = source_service_name
        if timezone is not None:
            self._values["timezone"] = timezone
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#admin_password DatabaseServiceInstance#admin_password}.'''
        result = self._values.get("admin_password")
        assert result is not None, "Required property 'admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def usable_storage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#usable_storage DatabaseServiceInstance#usable_storage}.'''
        result = self._values.get("usable_storage")
        assert result is not None, "Required property 'usable_storage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def backup_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_destination DatabaseServiceInstance#backup_destination}.'''
        result = self._values.get("backup_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_storage_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#backup_storage_volume_size DatabaseServiceInstance#backup_storage_volume_size}.'''
        result = self._values.get("backup_storage_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def character_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#character_set DatabaseServiceInstance#character_set}.'''
        result = self._values.get("character_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_storage_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#data_storage_volume_size DatabaseServiceInstance#data_storage_volume_size}.'''
        result = self._values.get("data_storage_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def db_demo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#db_demo DatabaseServiceInstance#db_demo}.'''
        result = self._values.get("db_demo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disaster_recovery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#disaster_recovery DatabaseServiceInstance#disaster_recovery}.'''
        result = self._values.get("disaster_recovery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def failover_database(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#failover_database DatabaseServiceInstance#failover_database}.'''
        result = self._values.get("failover_database")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def golden_gate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#golden_gate DatabaseServiceInstance#golden_gate}.'''
        result = self._values.get("golden_gate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def is_rac(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#is_rac DatabaseServiceInstance#is_rac}.'''
        result = self._values.get("is_rac")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def national_character_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#national_character_set DatabaseServiceInstance#national_character_set}.'''
        result = self._values.get("national_character_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pdb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#pdb_name DatabaseServiceInstance#pdb_name}.'''
        result = self._values.get("pdb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#sid DatabaseServiceInstance#sid}.'''
        result = self._values.get("sid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#snapshot_name DatabaseServiceInstance#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#source_service_name DatabaseServiceInstance#source_service_name}.'''
        result = self._values.get("source_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#timezone DatabaseServiceInstance#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#type DatabaseServiceInstance#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceDatabaseConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceDatabaseConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceDatabaseConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__419c7600b2efb70b5ee366a27d10ce2818f6c2c9b5757cdbe42925bee9988b32)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBackupDestination")
    def reset_backup_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupDestination", []))

    @jsii.member(jsii_name="resetBackupStorageVolumeSize")
    def reset_backup_storage_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupStorageVolumeSize", []))

    @jsii.member(jsii_name="resetCharacterSet")
    def reset_character_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCharacterSet", []))

    @jsii.member(jsii_name="resetDataStorageVolumeSize")
    def reset_data_storage_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataStorageVolumeSize", []))

    @jsii.member(jsii_name="resetDbDemo")
    def reset_db_demo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbDemo", []))

    @jsii.member(jsii_name="resetDisasterRecovery")
    def reset_disaster_recovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisasterRecovery", []))

    @jsii.member(jsii_name="resetFailoverDatabase")
    def reset_failover_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverDatabase", []))

    @jsii.member(jsii_name="resetGoldenGate")
    def reset_golden_gate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoldenGate", []))

    @jsii.member(jsii_name="resetIsRac")
    def reset_is_rac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsRac", []))

    @jsii.member(jsii_name="resetNationalCharacterSet")
    def reset_national_character_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNationalCharacterSet", []))

    @jsii.member(jsii_name="resetPdbName")
    def reset_pdb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPdbName", []))

    @jsii.member(jsii_name="resetSid")
    def reset_sid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSid", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @jsii.member(jsii_name="resetSourceServiceName")
    def reset_source_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServiceName", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="backupDestinationInput")
    def backup_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="backupStorageVolumeSizeInput")
    def backup_storage_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupStorageVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="characterSetInput")
    def character_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "characterSetInput"))

    @builtins.property
    @jsii.member(jsii_name="dataStorageVolumeSizeInput")
    def data_storage_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataStorageVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="dbDemoInput")
    def db_demo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbDemoInput"))

    @builtins.property
    @jsii.member(jsii_name="disasterRecoveryInput")
    def disaster_recovery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disasterRecoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverDatabaseInput")
    def failover_database_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failoverDatabaseInput"))

    @builtins.property
    @jsii.member(jsii_name="goldenGateInput")
    def golden_gate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "goldenGateInput"))

    @builtins.property
    @jsii.member(jsii_name="isRacInput")
    def is_rac_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isRacInput"))

    @builtins.property
    @jsii.member(jsii_name="nationalCharacterSetInput")
    def national_character_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nationalCharacterSetInput"))

    @builtins.property
    @jsii.member(jsii_name="pdbNameInput")
    def pdb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sidInput")
    def sid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sidInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceNameInput")
    def source_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usableStorageInput")
    def usable_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "usableStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d138ad5aa93141713bfee265bb9ed20c0d909d385f25868f3ef079e9543973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="backupDestination")
    def backup_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupDestination"))

    @backup_destination.setter
    def backup_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a6e33524f98404d68af1947999c592810be1fed29853354b9f560038d2b9c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupDestination", value)

    @builtins.property
    @jsii.member(jsii_name="backupStorageVolumeSize")
    def backup_storage_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupStorageVolumeSize"))

    @backup_storage_volume_size.setter
    def backup_storage_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26d4eaa1c0fa3c9d5387e380710e9285986f2d28660cf432f71142e07d6ea83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupStorageVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="characterSet")
    def character_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "characterSet"))

    @character_set.setter
    def character_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a288838c21e483ddbdfeb132039f33ab189f28619373f9e1fe3861bf45ea5e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "characterSet", value)

    @builtins.property
    @jsii.member(jsii_name="dataStorageVolumeSize")
    def data_storage_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataStorageVolumeSize"))

    @data_storage_volume_size.setter
    def data_storage_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95619456b02cbe133430da5ae2d9e562e4fb1ae80621f968bc4bdd2bfdce03f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataStorageVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="dbDemo")
    def db_demo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbDemo"))

    @db_demo.setter
    def db_demo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aeb4f45a23d6f5b9ace7861dca8ca7e290382a34665e48fb6d6b1c079372f52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbDemo", value)

    @builtins.property
    @jsii.member(jsii_name="disasterRecovery")
    def disaster_recovery(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disasterRecovery"))

    @disaster_recovery.setter
    def disaster_recovery(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd7eb3db0845b819486e824149d8fb4b9b04c8163bd5790cc8f37794a7f23cd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disasterRecovery", value)

    @builtins.property
    @jsii.member(jsii_name="failoverDatabase")
    def failover_database(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failoverDatabase"))

    @failover_database.setter
    def failover_database(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19bae9ad6cf66d91cdef183ebff19981d11f4f480dc81e304f4d459526b2247f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverDatabase", value)

    @builtins.property
    @jsii.member(jsii_name="goldenGate")
    def golden_gate(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "goldenGate"))

    @golden_gate.setter
    def golden_gate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d85c158f7fa5ffe498623ce1e52442ca7f2921e6d6f2333b021bec73768d3a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "goldenGate", value)

    @builtins.property
    @jsii.member(jsii_name="isRac")
    def is_rac(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isRac"))

    @is_rac.setter
    def is_rac(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e13dbdbd580510e51b27becaa93ae9f159b9cf8c70384ede9f612d1c2772cf84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isRac", value)

    @builtins.property
    @jsii.member(jsii_name="nationalCharacterSet")
    def national_character_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nationalCharacterSet"))

    @national_character_set.setter
    def national_character_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82dadb2aa1bd04609a8b6fba80e49b5492abb897ed9fccd63f89c5af8e4b4a82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nationalCharacterSet", value)

    @builtins.property
    @jsii.member(jsii_name="pdbName")
    def pdb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdbName"))

    @pdb_name.setter
    def pdb_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef82ee905507536c86a4342e6c86867fc884b9becd48725518e9cb24cc19ef9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdbName", value)

    @builtins.property
    @jsii.member(jsii_name="sid")
    def sid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sid"))

    @sid.setter
    def sid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0c0c62976199630e1af52982de101d848c653771c66c576d03c0256b1098b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sid", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94a0ada516ecc7c49dc9b249dc6d2ef46708a1d6df8e47d33c0dc59aa5343d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServiceName")
    def source_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceServiceName"))

    @source_service_name.setter
    def source_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b933bc985cc7f53f52c8b380b8ee1f8db8ebd1d021361b1b82f4f9a1d72eebce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__849049f1ef2e0f56de0de5c99f03ba37bc2a91637a72922c039c0fd0dfec200a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8098fbdb18a06d90472691b09a1fb9cd44dc6986961e6bb02a6c77a94f1a0c01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usableStorage")
    def usable_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "usableStorage"))

    @usable_storage.setter
    def usable_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e2fb8f15c1869c66cdd1ce17a9d3a1e866effef6c8f4f6a84cb93ad7d6be1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usableStorage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseServiceInstanceDatabaseConfiguration]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceDatabaseConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceDatabaseConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e9e0db842f9fa4c58596e84abc1d72c7d117b47b1b9a9bf7a565fe811ac9eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceDefaultAccessRules",
    jsii_struct_bases=[],
    name_mapping={
        "enable_db_console": "enableDbConsole",
        "enable_db_express": "enableDbExpress",
        "enable_db_listener": "enableDbListener",
        "enable_em_console": "enableEmConsole",
        "enable_http": "enableHttp",
        "enable_http_ssl": "enableHttpSsl",
        "enable_rac_db_listener": "enableRacDbListener",
        "enable_rac_ons": "enableRacOns",
        "enable_scan_listener": "enableScanListener",
        "enable_ssh": "enableSsh",
    },
)
class DatabaseServiceInstanceDefaultAccessRules:
    def __init__(
        self,
        *,
        enable_db_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_db_express: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_em_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_http: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_http_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rac_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_rac_ons: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_scan_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_ssh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_db_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_console DatabaseServiceInstance#enable_db_console}.
        :param enable_db_express: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_express DatabaseServiceInstance#enable_db_express}.
        :param enable_db_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_listener DatabaseServiceInstance#enable_db_listener}.
        :param enable_em_console: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_em_console DatabaseServiceInstance#enable_em_console}.
        :param enable_http: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http DatabaseServiceInstance#enable_http}.
        :param enable_http_ssl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http_ssl DatabaseServiceInstance#enable_http_ssl}.
        :param enable_rac_db_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_db_listener DatabaseServiceInstance#enable_rac_db_listener}.
        :param enable_rac_ons: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_ons DatabaseServiceInstance#enable_rac_ons}.
        :param enable_scan_listener: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_scan_listener DatabaseServiceInstance#enable_scan_listener}.
        :param enable_ssh: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_ssh DatabaseServiceInstance#enable_ssh}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f23f70907781e536434b0d32dbadc5045201e31124a06352777102f7751918d5)
            check_type(argname="argument enable_db_console", value=enable_db_console, expected_type=type_hints["enable_db_console"])
            check_type(argname="argument enable_db_express", value=enable_db_express, expected_type=type_hints["enable_db_express"])
            check_type(argname="argument enable_db_listener", value=enable_db_listener, expected_type=type_hints["enable_db_listener"])
            check_type(argname="argument enable_em_console", value=enable_em_console, expected_type=type_hints["enable_em_console"])
            check_type(argname="argument enable_http", value=enable_http, expected_type=type_hints["enable_http"])
            check_type(argname="argument enable_http_ssl", value=enable_http_ssl, expected_type=type_hints["enable_http_ssl"])
            check_type(argname="argument enable_rac_db_listener", value=enable_rac_db_listener, expected_type=type_hints["enable_rac_db_listener"])
            check_type(argname="argument enable_rac_ons", value=enable_rac_ons, expected_type=type_hints["enable_rac_ons"])
            check_type(argname="argument enable_scan_listener", value=enable_scan_listener, expected_type=type_hints["enable_scan_listener"])
            check_type(argname="argument enable_ssh", value=enable_ssh, expected_type=type_hints["enable_ssh"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_db_console is not None:
            self._values["enable_db_console"] = enable_db_console
        if enable_db_express is not None:
            self._values["enable_db_express"] = enable_db_express
        if enable_db_listener is not None:
            self._values["enable_db_listener"] = enable_db_listener
        if enable_em_console is not None:
            self._values["enable_em_console"] = enable_em_console
        if enable_http is not None:
            self._values["enable_http"] = enable_http
        if enable_http_ssl is not None:
            self._values["enable_http_ssl"] = enable_http_ssl
        if enable_rac_db_listener is not None:
            self._values["enable_rac_db_listener"] = enable_rac_db_listener
        if enable_rac_ons is not None:
            self._values["enable_rac_ons"] = enable_rac_ons
        if enable_scan_listener is not None:
            self._values["enable_scan_listener"] = enable_scan_listener
        if enable_ssh is not None:
            self._values["enable_ssh"] = enable_ssh

    @builtins.property
    def enable_db_console(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_console DatabaseServiceInstance#enable_db_console}.'''
        result = self._values.get("enable_db_console")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_db_express(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_express DatabaseServiceInstance#enable_db_express}.'''
        result = self._values.get("enable_db_express")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_db_listener(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_db_listener DatabaseServiceInstance#enable_db_listener}.'''
        result = self._values.get("enable_db_listener")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_em_console(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_em_console DatabaseServiceInstance#enable_em_console}.'''
        result = self._values.get("enable_em_console")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_http(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http DatabaseServiceInstance#enable_http}.'''
        result = self._values.get("enable_http")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_http_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_http_ssl DatabaseServiceInstance#enable_http_ssl}.'''
        result = self._values.get("enable_http_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_rac_db_listener(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_db_listener DatabaseServiceInstance#enable_rac_db_listener}.'''
        result = self._values.get("enable_rac_db_listener")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_rac_ons(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_rac_ons DatabaseServiceInstance#enable_rac_ons}.'''
        result = self._values.get("enable_rac_ons")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_scan_listener(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_scan_listener DatabaseServiceInstance#enable_scan_listener}.'''
        result = self._values.get("enable_scan_listener")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_ssh(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#enable_ssh DatabaseServiceInstance#enable_ssh}.'''
        result = self._values.get("enable_ssh")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceDefaultAccessRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceDefaultAccessRulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceDefaultAccessRulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e26dbb3708d258a7ad6cd615592b6119a2aa73ef166f1b2468f048a360f61cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableDbConsole")
    def reset_enable_db_console(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDbConsole", []))

    @jsii.member(jsii_name="resetEnableDbExpress")
    def reset_enable_db_express(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDbExpress", []))

    @jsii.member(jsii_name="resetEnableDbListener")
    def reset_enable_db_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDbListener", []))

    @jsii.member(jsii_name="resetEnableEmConsole")
    def reset_enable_em_console(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEmConsole", []))

    @jsii.member(jsii_name="resetEnableHttp")
    def reset_enable_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttp", []))

    @jsii.member(jsii_name="resetEnableHttpSsl")
    def reset_enable_http_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttpSsl", []))

    @jsii.member(jsii_name="resetEnableRacDbListener")
    def reset_enable_rac_db_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRacDbListener", []))

    @jsii.member(jsii_name="resetEnableRacOns")
    def reset_enable_rac_ons(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRacOns", []))

    @jsii.member(jsii_name="resetEnableScanListener")
    def reset_enable_scan_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableScanListener", []))

    @jsii.member(jsii_name="resetEnableSsh")
    def reset_enable_ssh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSsh", []))

    @builtins.property
    @jsii.member(jsii_name="enableDbConsoleInput")
    def enable_db_console_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDbConsoleInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDbExpressInput")
    def enable_db_express_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDbExpressInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDbListenerInput")
    def enable_db_listener_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableDbListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEmConsoleInput")
    def enable_em_console_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEmConsoleInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpInput")
    def enable_http_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableHttpInput"))

    @builtins.property
    @jsii.member(jsii_name="enableHttpSslInput")
    def enable_http_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableHttpSslInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRacDbListenerInput")
    def enable_rac_db_listener_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableRacDbListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRacOnsInput")
    def enable_rac_ons_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableRacOnsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableScanListenerInput")
    def enable_scan_listener_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableScanListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSshInput")
    def enable_ssh_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableSshInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDbConsole")
    def enable_db_console(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDbConsole"))

    @enable_db_console.setter
    def enable_db_console(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9260e63659ca8f94a86c40e2e2ca4b6ce1b3a5a1c1ee990ee43b20e1c9f11c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDbConsole", value)

    @builtins.property
    @jsii.member(jsii_name="enableDbExpress")
    def enable_db_express(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDbExpress"))

    @enable_db_express.setter
    def enable_db_express(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0ce8b097af766711b38c8e07d2456f2688f9f95c89a77f3e02dc4cf9f8ab65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDbExpress", value)

    @builtins.property
    @jsii.member(jsii_name="enableDbListener")
    def enable_db_listener(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableDbListener"))

    @enable_db_listener.setter
    def enable_db_listener(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c494d9405e58e5ed93b39da5130ac38b8d88a89cb5a72a72f23e3771afcde23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDbListener", value)

    @builtins.property
    @jsii.member(jsii_name="enableEmConsole")
    def enable_em_console(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEmConsole"))

    @enable_em_console.setter
    def enable_em_console(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a17020af9941a6a860f5b8cae10bbcbf2c800fd2f45b65821edd2f45a5a89b3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEmConsole", value)

    @builtins.property
    @jsii.member(jsii_name="enableHttp")
    def enable_http(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableHttp"))

    @enable_http.setter
    def enable_http(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cf3e647eaa75103a903df67720ed6fcb4e071667a98d600e9e46552b9b90711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttp", value)

    @builtins.property
    @jsii.member(jsii_name="enableHttpSsl")
    def enable_http_ssl(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableHttpSsl"))

    @enable_http_ssl.setter
    def enable_http_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c73dd671730913bdb49db15dc95a4b535fc1d298d82dc5c4383020034ec6f63f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttpSsl", value)

    @builtins.property
    @jsii.member(jsii_name="enableRacDbListener")
    def enable_rac_db_listener(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableRacDbListener"))

    @enable_rac_db_listener.setter
    def enable_rac_db_listener(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca3f00de18220b19da3710026b8a2817891cf1c6683192dc3fe0aab1806a0709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRacDbListener", value)

    @builtins.property
    @jsii.member(jsii_name="enableRacOns")
    def enable_rac_ons(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableRacOns"))

    @enable_rac_ons.setter
    def enable_rac_ons(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57ba5df361ebc47194c6e74c193c207a2dca2e6d25d44157c43bd22a8b1b6dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRacOns", value)

    @builtins.property
    @jsii.member(jsii_name="enableScanListener")
    def enable_scan_listener(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableScanListener"))

    @enable_scan_listener.setter
    def enable_scan_listener(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e345f2356e7495a598d73d52a595db7001aba164679d0d6e195bd5dc63633ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableScanListener", value)

    @builtins.property
    @jsii.member(jsii_name="enableSsh")
    def enable_ssh(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableSsh"))

    @enable_ssh.setter
    def enable_ssh(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbf4839936bdff75c22e44d928873868c21215a168333f851a12c3f1e872a8a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSsh", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseServiceInstanceDefaultAccessRules]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceDefaultAccessRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceDefaultAccessRules],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc695b898e3a4979a120241ca76484b55e0f2c2063eb7faee24d951f9c5c8ecb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceHybridDisasterRecovery",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
    },
)
class DatabaseServiceInstanceHybridDisasterRecovery:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6db5b9559352375885eb4c3de01963cf0de01cd32bb1007a6f88bc850b1c0f)
            check_type(argname="argument cloud_storage_container", value=cloud_storage_container, expected_type=type_hints["cloud_storage_container"])
            check_type(argname="argument cloud_storage_password", value=cloud_storage_password, expected_type=type_hints["cloud_storage_password"])
            check_type(argname="argument cloud_storage_username", value=cloud_storage_username, expected_type=type_hints["cloud_storage_username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_storage_container": cloud_storage_container,
        }
        if cloud_storage_password is not None:
            self._values["cloud_storage_password"] = cloud_storage_password
        if cloud_storage_username is not None:
            self._values["cloud_storage_username"] = cloud_storage_username

    @builtins.property
    def cloud_storage_container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceHybridDisasterRecovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceHybridDisasterRecoveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceHybridDisasterRecoveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0217efb48b5920515e7a86b3324e756ed7d3a72329596c9adaacef106f7c9985)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudStoragePassword")
    def reset_cloud_storage_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePassword", []))

    @jsii.member(jsii_name="resetCloudStorageUsername")
    def reset_cloud_storage_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageUsername", []))

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
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @cloud_storage_container.setter
    def cloud_storage_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cddad8438fea1659fff6cf01689d6048376d06e85ea912ba8a15df2d12e6de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b18e8da3c02f8d4d80700e71d4b3f8dee3c184e9b2feb411e861c979802551a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc0877728bdd350e3ca57af338f967ccc6712559a6ef102a09c97e70a6f8ee92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseServiceInstanceHybridDisasterRecovery]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceHybridDisasterRecovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceHybridDisasterRecovery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa4265676b3b301fbde0b87ea66a616c4dd5867d3f9cd8eab0c9ab9b4cedbfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceInstantiateFromBackup",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "database_id": "databaseId",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
        "decryption_key": "decryptionKey",
        "on_premise": "onPremise",
        "service_id": "serviceId",
        "wallet_file_content": "walletFileContent",
    },
)
class DatabaseServiceInstanceInstantiateFromBackup:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        database_id: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        decryption_key: typing.Optional[builtins.str] = None,
        on_premise: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_id: typing.Optional[builtins.str] = None,
        wallet_file_content: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.
        :param database_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_id DatabaseServiceInstance#database_id}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.
        :param decryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#decryption_key DatabaseServiceInstance#decryption_key}.
        :param on_premise: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#on_premise DatabaseServiceInstance#on_premise}.
        :param service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#service_id DatabaseServiceInstance#service_id}.
        :param wallet_file_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#wallet_file_content DatabaseServiceInstance#wallet_file_content}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24f4e3e238a474abf6f04756f1c5a6e433d055ce29795ac5062285b0abb0498)
            check_type(argname="argument cloud_storage_container", value=cloud_storage_container, expected_type=type_hints["cloud_storage_container"])
            check_type(argname="argument database_id", value=database_id, expected_type=type_hints["database_id"])
            check_type(argname="argument cloud_storage_password", value=cloud_storage_password, expected_type=type_hints["cloud_storage_password"])
            check_type(argname="argument cloud_storage_username", value=cloud_storage_username, expected_type=type_hints["cloud_storage_username"])
            check_type(argname="argument decryption_key", value=decryption_key, expected_type=type_hints["decryption_key"])
            check_type(argname="argument on_premise", value=on_premise, expected_type=type_hints["on_premise"])
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
            check_type(argname="argument wallet_file_content", value=wallet_file_content, expected_type=type_hints["wallet_file_content"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_storage_container": cloud_storage_container,
            "database_id": database_id,
        }
        if cloud_storage_password is not None:
            self._values["cloud_storage_password"] = cloud_storage_password
        if cloud_storage_username is not None:
            self._values["cloud_storage_username"] = cloud_storage_username
        if decryption_key is not None:
            self._values["decryption_key"] = decryption_key
        if on_premise is not None:
            self._values["on_premise"] = on_premise
        if service_id is not None:
            self._values["service_id"] = service_id
        if wallet_file_content is not None:
            self._values["wallet_file_content"] = wallet_file_content

    @builtins.property
    def cloud_storage_container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_container DatabaseServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#database_id DatabaseServiceInstance#database_id}.'''
        result = self._values.get("database_id")
        assert result is not None, "Required property 'database_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_password DatabaseServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#cloud_storage_username DatabaseServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def decryption_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#decryption_key DatabaseServiceInstance#decryption_key}.'''
        result = self._values.get("decryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_premise(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#on_premise DatabaseServiceInstance#on_premise}.'''
        result = self._values.get("on_premise")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#service_id DatabaseServiceInstance#service_id}.'''
        result = self._values.get("service_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wallet_file_content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#wallet_file_content DatabaseServiceInstance#wallet_file_content}.'''
        result = self._values.get("wallet_file_content")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceInstantiateFromBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceInstantiateFromBackupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceInstantiateFromBackupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f330d1c49aa81fd36c81c5c8a487b75327fe8098ff5798ff7fb8a3f9b4ac2eb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCloudStoragePassword")
    def reset_cloud_storage_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStoragePassword", []))

    @jsii.member(jsii_name="resetCloudStorageUsername")
    def reset_cloud_storage_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudStorageUsername", []))

    @jsii.member(jsii_name="resetDecryptionKey")
    def reset_decryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecryptionKey", []))

    @jsii.member(jsii_name="resetOnPremise")
    def reset_on_premise(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnPremise", []))

    @jsii.member(jsii_name="resetServiceId")
    def reset_service_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceId", []))

    @jsii.member(jsii_name="resetWalletFileContent")
    def reset_wallet_file_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWalletFileContent", []))

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
    @jsii.member(jsii_name="databaseIdInput")
    def database_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseIdInput"))

    @builtins.property
    @jsii.member(jsii_name="decryptionKeyInput")
    def decryption_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "decryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="onPremiseInput")
    def on_premise_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "onPremiseInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdInput")
    def service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="walletFileContentInput")
    def wallet_file_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "walletFileContentInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudStorageContainer")
    def cloud_storage_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageContainer"))

    @cloud_storage_container.setter
    def cloud_storage_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab4ca97a2731be2a41889997842674bc24bd8a33df7ecac7a020042c493b3aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda07fd1b547741f6b6fc1fc44b83c74300491703ba7accf8a3c76ace19c552f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e66747ad496323be4f28445715cec68e8ebd0d14d2fc41b072187c6cebb345f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageUsername", value)

    @builtins.property
    @jsii.member(jsii_name="databaseId")
    def database_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseId"))

    @database_id.setter
    def database_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e398a11e124c1894ce4a4e83cc4cff554d5d083adbbe77f5ff79cba0e3659f9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseId", value)

    @builtins.property
    @jsii.member(jsii_name="decryptionKey")
    def decryption_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decryptionKey"))

    @decryption_key.setter
    def decryption_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c1f6d1509ac4cd8c3fd2fa90bf6d39f187c188ffd08b3cfa6177f00ecbda3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="onPremise")
    def on_premise(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "onPremise"))

    @on_premise.setter
    def on_premise(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc92e69e955243ca2c6ba98ce71fe56feef0153051b07fe81939455049678009)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onPremise", value)

    @builtins.property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @service_id.setter
    def service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__447957bcb58815e2a3f31e45ec227edef505b1dc3d58f78ae8fa3bce1ef19813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceId", value)

    @builtins.property
    @jsii.member(jsii_name="walletFileContent")
    def wallet_file_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "walletFileContent"))

    @wallet_file_content.setter
    def wallet_file_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d50a2f0c53af71c76b70aef232441eca4ec14c8b748e145f66c559d49cb92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "walletFileContent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DatabaseServiceInstanceInstantiateFromBackup]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceInstantiateFromBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceInstantiateFromBackup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__732c43fa544bc4af9b4af8e7de492e7dfa5b82fea1d8344d0dcf164f4e70e2c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceStandby",
    jsii_struct_bases=[],
    name_mapping={"availability_domain": "availabilityDomain", "subnet": "subnet"},
)
class DatabaseServiceInstanceStandby:
    def __init__(
        self,
        *,
        availability_domain: builtins.str,
        subnet: builtins.str,
    ) -> None:
        '''
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ff08eeabdc0b6bad85014d1158d0233a97d13fa94065420b1c6478ddb9ddfe)
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_domain": availability_domain,
            "subnet": subnet,
        }

    @builtins.property
    def availability_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#availability_domain DatabaseServiceInstance#availability_domain}.'''
        result = self._values.get("availability_domain")
        assert result is not None, "Required property 'availability_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#subnet DatabaseServiceInstance#subnet}.'''
        result = self._values.get("subnet")
        assert result is not None, "Required property 'subnet' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceStandby(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceStandbyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceStandbyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c4cb35eae37142e32011288f806260908cdddde87fde3412fa6e2239db354c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="availabilityDomainInput")
    def availability_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a8447109a8f0aafa5dd8f8a95259f9a62d86b2e5949e7f1f30bb255b12790d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed8b40922da820dec1ea66e0930779c0636e08601f95d0293b30f666fe5c0bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatabaseServiceInstanceStandby]:
        return typing.cast(typing.Optional[DatabaseServiceInstanceStandby], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatabaseServiceInstanceStandby],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8dd0fd8a6418e110caade22457c2fc9a504cc586a14e76ef47ecfde302e041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class DatabaseServiceInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create DatabaseServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#delete DatabaseServiceInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#update DatabaseServiceInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4103b2cc3e1f622a491c042f0dc70c8eb5a925cdb2be6481926b2bc26886dcb7)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#create DatabaseServiceInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#delete DatabaseServiceInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/database_service_instance#update DatabaseServiceInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseServiceInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatabaseServiceInstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.databaseServiceInstance.DatabaseServiceInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a4d5e4306cfe22adb1a5f6f8e7430d7d66fd3be828b89e216a5c1fb8ba8ef7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c81c264f2ee673b4fbc7dd2ed7fd739434439ac24b1e4ff5c1f2196c6058f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7854c3aeb771365eea388bf62b7045e0105c64ce51fbad5d2d601460186b1e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8aed5d6ed7c25b6ecab7989750d93ae91b938d5d00a67d4edf6505115cf185c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f626ad2da6316b83e94c43a5024032941ecb3f41e66aa86498f908753625da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatabaseServiceInstance",
    "DatabaseServiceInstanceBackups",
    "DatabaseServiceInstanceBackupsOutputReference",
    "DatabaseServiceInstanceConfig",
    "DatabaseServiceInstanceDatabaseConfiguration",
    "DatabaseServiceInstanceDatabaseConfigurationOutputReference",
    "DatabaseServiceInstanceDefaultAccessRules",
    "DatabaseServiceInstanceDefaultAccessRulesOutputReference",
    "DatabaseServiceInstanceHybridDisasterRecovery",
    "DatabaseServiceInstanceHybridDisasterRecoveryOutputReference",
    "DatabaseServiceInstanceInstantiateFromBackup",
    "DatabaseServiceInstanceInstantiateFromBackupOutputReference",
    "DatabaseServiceInstanceStandby",
    "DatabaseServiceInstanceStandbyOutputReference",
    "DatabaseServiceInstanceTimeouts",
    "DatabaseServiceInstanceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__aa73e3345bc57a92cb55c5471318dd7e91661635157f348786bc0edbeed5407d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database_configuration: typing.Union[DatabaseServiceInstanceDatabaseConfiguration, typing.Dict[builtins.str, typing.Any]],
    edition: builtins.str,
    name: builtins.str,
    shape: builtins.str,
    ssh_public_key: builtins.str,
    subscription_type: builtins.str,
    version: builtins.str,
    availability_domain: typing.Optional[builtins.str] = None,
    backups: typing.Optional[typing.Union[DatabaseServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
    bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_access_rules: typing.Optional[typing.Union[DatabaseServiceInstanceDefaultAccessRules, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    high_performance_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hybrid_disaster_recovery: typing.Optional[typing.Union[DatabaseServiceInstanceHybridDisasterRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    instantiate_from_backup: typing.Optional[typing.Union[DatabaseServiceInstanceInstantiateFromBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_network: typing.Optional[builtins.str] = None,
    ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
    level: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    standby: typing.Optional[typing.Union[DatabaseServiceInstanceStandby, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__51cb440b977cdb514ba8edd18e6174b2f6d843161716129d0d172dc27bebb6e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bef6d59a8528132c6a5c10418c924454d1155d2bc75cbc8398ad22ccc861a6e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262b32b9aa830bd48ec3e8d613a9a6f7898b88e3e9d5a0815a79b265da2fee94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a484712c9ef3c2295f5816f940a1c8d684da90cd1c575967688121b3f5f2ffe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc50b45ab556bfd2c96176a4249e3f60b8369cf0ca37a373ab960bd0c8ce0411(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894070b110cfcac47ea66ec2a57a8af6e88710341e7955e3c251f8e9820d777f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bef5afe8a9c52ab3c847f5b77871c533e25558794b0899c0f29a68c093721fd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807626eff852236fd01e30dcf2a4dd4e24a04411c6cdd439bb0409be46d69a4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38477cbc7d5eff468025818cdd6967657afb7eab7e8c8b0f98a6d5dd53e48745(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c55be471b42f22de7dd985a91a7b6ed5fcc8b7ef47945d7168ba166f4d9cf5a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c33f86f0cb5cb47b901be0bd0536a2c71ac21e2621030159403c0a4e40f3af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0756adc3990f35fd762c56b94506a8c3fc63fdf1d2bc2c6fe2e676fca6fefff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57feadaa6cba84b3cc27a1146383e42fa50f39e95c7a8e056513cd32e5aef2b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbe38dba8afa82a574116d20e9f2f96a8b392b9c856407f3dcb5e2674c3d9ff3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43605d831243fe51821a9c0a28c26dc30c03e0b0afc8b911911f16082c3aa9ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca93c644004ee94be928111105e70a46cd386192eb6ec1ee1340b14983983198(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64b3bb5f85c06a857b70fc26445ad0b71f56cc487c742a3e2d0eb83a15eeb2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e539c31ca3d45ec2ccc9bb2e8cf377cd49d581babc35ffc32a6e6937093d7fa6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db875cae9cdc0dda352651b3890ae5ec4e460ddbced51614cdd0a01c6075474(
    *,
    cloud_storage_container: builtins.str,
    cloud_storage_password: typing.Optional[builtins.str] = None,
    cloud_storage_username: typing.Optional[builtins.str] = None,
    create_if_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c80f6b4e1eeb22d028a58c23f7dc26ba1abfa5e420f4da430e780888af678a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e22bc388a25f47d7030f06ac5661e1513d42328689a451f67117b6d47d23e0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9673783138cb0bff360d45f7b963924bed96ad0f003d5863b135d5d39b99e2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98b1f8209ebb2ef4b05f0796e0b5aec9616ab30305da3bd38922316541c1da0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f028aba71095f35a73b8cf00ff4c859db079a85a49ebcb98f8a51dd7c6fdc6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24edaa2c8d06fac4fdf69186d7a4d8c72ecb2db6268367d79442c5dff1876f24(
    value: typing.Optional[DatabaseServiceInstanceBackups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e955c443bb288e6d32a8a4b725d45921c3abc7c249e736b6082db3defa98be7a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database_configuration: typing.Union[DatabaseServiceInstanceDatabaseConfiguration, typing.Dict[builtins.str, typing.Any]],
    edition: builtins.str,
    name: builtins.str,
    shape: builtins.str,
    ssh_public_key: builtins.str,
    subscription_type: builtins.str,
    version: builtins.str,
    availability_domain: typing.Optional[builtins.str] = None,
    backups: typing.Optional[typing.Union[DatabaseServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
    bring_your_own_license: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    default_access_rules: typing.Optional[typing.Union[DatabaseServiceInstanceDefaultAccessRules, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    high_performance_storage: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    hybrid_disaster_recovery: typing.Optional[typing.Union[DatabaseServiceInstanceHybridDisasterRecovery, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    instantiate_from_backup: typing.Optional[typing.Union[DatabaseServiceInstanceInstantiateFromBackup, typing.Dict[builtins.str, typing.Any]]] = None,
    ip_network: typing.Optional[builtins.str] = None,
    ip_reservations: typing.Optional[typing.Sequence[builtins.str]] = None,
    level: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    standby: typing.Optional[typing.Union[DatabaseServiceInstanceStandby, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c082223846b1d1d20195b0cf7d00a76b618d11d08cc1b8e408d87b982919bb3(
    *,
    admin_password: builtins.str,
    usable_storage: jsii.Number,
    backup_destination: typing.Optional[builtins.str] = None,
    backup_storage_volume_size: typing.Optional[jsii.Number] = None,
    character_set: typing.Optional[builtins.str] = None,
    data_storage_volume_size: typing.Optional[jsii.Number] = None,
    db_demo: typing.Optional[builtins.str] = None,
    disaster_recovery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    failover_database: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    golden_gate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    is_rac: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    national_character_set: typing.Optional[builtins.str] = None,
    pdb_name: typing.Optional[builtins.str] = None,
    sid: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    source_service_name: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419c7600b2efb70b5ee366a27d10ce2818f6c2c9b5757cdbe42925bee9988b32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d138ad5aa93141713bfee265bb9ed20c0d909d385f25868f3ef079e9543973(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6e33524f98404d68af1947999c592810be1fed29853354b9f560038d2b9c2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26d4eaa1c0fa3c9d5387e380710e9285986f2d28660cf432f71142e07d6ea83(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a288838c21e483ddbdfeb132039f33ab189f28619373f9e1fe3861bf45ea5e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95619456b02cbe133430da5ae2d9e562e4fb1ae80621f968bc4bdd2bfdce03f7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aeb4f45a23d6f5b9ace7861dca8ca7e290382a34665e48fb6d6b1c079372f52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd7eb3db0845b819486e824149d8fb4b9b04c8163bd5790cc8f37794a7f23cd4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19bae9ad6cf66d91cdef183ebff19981d11f4f480dc81e304f4d459526b2247f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d85c158f7fa5ffe498623ce1e52442ca7f2921e6d6f2333b021bec73768d3a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e13dbdbd580510e51b27becaa93ae9f159b9cf8c70384ede9f612d1c2772cf84(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82dadb2aa1bd04609a8b6fba80e49b5492abb897ed9fccd63f89c5af8e4b4a82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef82ee905507536c86a4342e6c86867fc884b9becd48725518e9cb24cc19ef9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0c0c62976199630e1af52982de101d848c653771c66c576d03c0256b1098b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a0ada516ecc7c49dc9b249dc6d2ef46708a1d6df8e47d33c0dc59aa5343d16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b933bc985cc7f53f52c8b380b8ee1f8db8ebd1d021361b1b82f4f9a1d72eebce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__849049f1ef2e0f56de0de5c99f03ba37bc2a91637a72922c039c0fd0dfec200a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8098fbdb18a06d90472691b09a1fb9cd44dc6986961e6bb02a6c77a94f1a0c01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e2fb8f15c1869c66cdd1ce17a9d3a1e866effef6c8f4f6a84cb93ad7d6be1f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e9e0db842f9fa4c58596e84abc1d72c7d117b47b1b9a9bf7a565fe811ac9eb(
    value: typing.Optional[DatabaseServiceInstanceDatabaseConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23f70907781e536434b0d32dbadc5045201e31124a06352777102f7751918d5(
    *,
    enable_db_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_db_express: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_em_console: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_http: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_http_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_rac_db_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_rac_ons: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_scan_listener: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_ssh: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e26dbb3708d258a7ad6cd615592b6119a2aa73ef166f1b2468f048a360f61cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9260e63659ca8f94a86c40e2e2ca4b6ce1b3a5a1c1ee990ee43b20e1c9f11c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0ce8b097af766711b38c8e07d2456f2688f9f95c89a77f3e02dc4cf9f8ab65(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c494d9405e58e5ed93b39da5130ac38b8d88a89cb5a72a72f23e3771afcde23(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17020af9941a6a860f5b8cae10bbcbf2c800fd2f45b65821edd2f45a5a89b3a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf3e647eaa75103a903df67720ed6fcb4e071667a98d600e9e46552b9b90711(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c73dd671730913bdb49db15dc95a4b535fc1d298d82dc5c4383020034ec6f63f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca3f00de18220b19da3710026b8a2817891cf1c6683192dc3fe0aab1806a0709(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57ba5df361ebc47194c6e74c193c207a2dca2e6d25d44157c43bd22a8b1b6dc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e345f2356e7495a598d73d52a595db7001aba164679d0d6e195bd5dc63633ace(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbf4839936bdff75c22e44d928873868c21215a168333f851a12c3f1e872a8a1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc695b898e3a4979a120241ca76484b55e0f2c2063eb7faee24d951f9c5c8ecb(
    value: typing.Optional[DatabaseServiceInstanceDefaultAccessRules],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6db5b9559352375885eb4c3de01963cf0de01cd32bb1007a6f88bc850b1c0f(
    *,
    cloud_storage_container: builtins.str,
    cloud_storage_password: typing.Optional[builtins.str] = None,
    cloud_storage_username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0217efb48b5920515e7a86b3324e756ed7d3a72329596c9adaacef106f7c9985(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cddad8438fea1659fff6cf01689d6048376d06e85ea912ba8a15df2d12e6de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b18e8da3c02f8d4d80700e71d4b3f8dee3c184e9b2feb411e861c979802551a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc0877728bdd350e3ca57af338f967ccc6712559a6ef102a09c97e70a6f8ee92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa4265676b3b301fbde0b87ea66a616c4dd5867d3f9cd8eab0c9ab9b4cedbfe(
    value: typing.Optional[DatabaseServiceInstanceHybridDisasterRecovery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24f4e3e238a474abf6f04756f1c5a6e433d055ce29795ac5062285b0abb0498(
    *,
    cloud_storage_container: builtins.str,
    database_id: builtins.str,
    cloud_storage_password: typing.Optional[builtins.str] = None,
    cloud_storage_username: typing.Optional[builtins.str] = None,
    decryption_key: typing.Optional[builtins.str] = None,
    on_premise: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service_id: typing.Optional[builtins.str] = None,
    wallet_file_content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f330d1c49aa81fd36c81c5c8a487b75327fe8098ff5798ff7fb8a3f9b4ac2eb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab4ca97a2731be2a41889997842674bc24bd8a33df7ecac7a020042c493b3aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda07fd1b547741f6b6fc1fc44b83c74300491703ba7accf8a3c76ace19c552f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e66747ad496323be4f28445715cec68e8ebd0d14d2fc41b072187c6cebb345f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e398a11e124c1894ce4a4e83cc4cff554d5d083adbbe77f5ff79cba0e3659f9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c1f6d1509ac4cd8c3fd2fa90bf6d39f187c188ffd08b3cfa6177f00ecbda3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc92e69e955243ca2c6ba98ce71fe56feef0153051b07fe81939455049678009(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447957bcb58815e2a3f31e45ec227edef505b1dc3d58f78ae8fa3bce1ef19813(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d50a2f0c53af71c76b70aef232441eca4ec14c8b748e145f66c559d49cb92c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732c43fa544bc4af9b4af8e7de492e7dfa5b82fea1d8344d0dcf164f4e70e2c6(
    value: typing.Optional[DatabaseServiceInstanceInstantiateFromBackup],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ff08eeabdc0b6bad85014d1158d0233a97d13fa94065420b1c6478ddb9ddfe(
    *,
    availability_domain: builtins.str,
    subnet: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4cb35eae37142e32011288f806260908cdddde87fde3412fa6e2239db354c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a8447109a8f0aafa5dd8f8a95259f9a62d86b2e5949e7f1f30bb255b12790d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed8b40922da820dec1ea66e0930779c0636e08601f95d0293b30f666fe5c0bd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8dd0fd8a6418e110caade22457c2fc9a504cc586a14e76ef47ecfde302e041(
    value: typing.Optional[DatabaseServiceInstanceStandby],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4103b2cc3e1f622a491c042f0dc70c8eb5a925cdb2be6481926b2bc26886dcb7(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a4d5e4306cfe22adb1a5f6f8e7430d7d66fd3be828b89e216a5c1fb8ba8ef7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c81c264f2ee673b4fbc7dd2ed7fd739434439ac24b1e4ff5c1f2196c6058f83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7854c3aeb771365eea388bf62b7045e0105c64ce51fbad5d2d601460186b1e6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8aed5d6ed7c25b6ecab7989750d93ae91b938d5d00a67d4edf6505115cf185c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f626ad2da6316b83e94c43a5024032941ecb3f41e66aa86498f908753625da3(
    value: typing.Optional[typing.Union[DatabaseServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
