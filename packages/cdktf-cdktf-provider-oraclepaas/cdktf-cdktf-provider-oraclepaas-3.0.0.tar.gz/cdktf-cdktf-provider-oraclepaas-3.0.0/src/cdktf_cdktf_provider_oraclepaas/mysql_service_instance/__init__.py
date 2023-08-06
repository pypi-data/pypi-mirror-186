'''
# `oraclepaas_mysql_service_instance`

Refer to the Terraform Registory for docs: [`oraclepaas_mysql_service_instance`](https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance).
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


class MysqlServiceInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance oraclepaas_mysql_service_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mysql_configuration: typing.Union["MysqlServiceInstanceMysqlConfiguration", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union["MysqlServiceInstanceBackups", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vm_user: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance oraclepaas_mysql_service_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mysql_configuration: mysql_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        :param vm_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__080e8493600a06bc7a4f88093d69b09055c60a1afd83a9df3aa7bb069e423514)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MysqlServiceInstanceConfig(
            mysql_configuration=mysql_configuration,
            name=name,
            shape=shape,
            ssh_public_key=ssh_public_key,
            availability_domain=availability_domain,
            backup_destination=backup_destination,
            backups=backups,
            description=description,
            id=id,
            ip_network=ip_network,
            metering_frequency=metering_frequency,
            notification_email=notification_email,
            region=region,
            subnet=subnet,
            timeouts=timeouts,
            vm_user=vm_user,
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
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.
        '''
        value = MysqlServiceInstanceBackups(
            cloud_storage_container=cloud_storage_container,
            cloud_storage_password=cloud_storage_password,
            cloud_storage_username=cloud_storage_username,
            create_if_missing=create_if_missing,
        )

        return typing.cast(None, jsii.invoke(self, "putBackups", [value]))

    @jsii.member(jsii_name="putMysqlConfiguration")
    def put_mysql_configuration(
        self,
        *,
        db_name: typing.Optional[builtins.str] = None,
        db_storage: typing.Optional[jsii.Number] = None,
        enterprise_monitor_configuration: typing.Optional[typing.Union["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        mysql_charset: typing.Optional[builtins.str] = None,
        mysql_collation: typing.Optional[builtins.str] = None,
        mysql_password: typing.Optional[builtins.str] = None,
        mysql_port: typing.Optional[jsii.Number] = None,
        mysql_username: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.
        :param db_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.
        :param enterprise_monitor_configuration: enterprise_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        :param mysql_charset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.
        :param mysql_collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.
        :param mysql_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.
        :param mysql_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.
        :param mysql_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.
        '''
        value = MysqlServiceInstanceMysqlConfiguration(
            db_name=db_name,
            db_storage=db_storage,
            enterprise_monitor_configuration=enterprise_monitor_configuration,
            mysql_charset=mysql_charset,
            mysql_collation=mysql_collation,
            mysql_password=mysql_password,
            mysql_port=mysql_port,
            mysql_username=mysql_username,
            snapshot_name=snapshot_name,
            source_service_name=source_service_name,
        )

        return typing.cast(None, jsii.invoke(self, "putMysqlConfiguration", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.
        '''
        value = MysqlServiceInstanceTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAvailabilityDomain")
    def reset_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityDomain", []))

    @jsii.member(jsii_name="resetBackupDestination")
    def reset_backup_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupDestination", []))

    @jsii.member(jsii_name="resetBackups")
    def reset_backups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackups", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetMeteringFrequency")
    def reset_metering_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeteringFrequency", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVmUser")
    def reset_vm_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmUser", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backups")
    def backups(self) -> "MysqlServiceInstanceBackupsOutputReference":
        return typing.cast("MysqlServiceInstanceBackupsOutputReference", jsii.get(self, "backups"))

    @builtins.property
    @jsii.member(jsii_name="baseReleaseVersion")
    def base_release_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseReleaseVersion"))

    @builtins.property
    @jsii.member(jsii_name="emUrl")
    def em_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emUrl"))

    @builtins.property
    @jsii.member(jsii_name="mysqlConfiguration")
    def mysql_configuration(
        self,
    ) -> "MysqlServiceInstanceMysqlConfigurationOutputReference":
        return typing.cast("MysqlServiceInstanceMysqlConfigurationOutputReference", jsii.get(self, "mysqlConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="releaseVersion")
    def release_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "releaseVersion"))

    @builtins.property
    @jsii.member(jsii_name="serviceVersion")
    def service_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceVersion"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MysqlServiceInstanceTimeoutsOutputReference":
        return typing.cast("MysqlServiceInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    def backups_input(self) -> typing.Optional["MysqlServiceInstanceBackups"]:
        return typing.cast(typing.Optional["MysqlServiceInstanceBackups"], jsii.get(self, "backupsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="meteringFrequencyInput")
    def metering_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meteringFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlConfigurationInput")
    def mysql_configuration_input(
        self,
    ) -> typing.Optional["MysqlServiceInstanceMysqlConfiguration"]:
        return typing.cast(typing.Optional["MysqlServiceInstanceMysqlConfiguration"], jsii.get(self, "mysqlConfigurationInput"))

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
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmUserInput")
    def vm_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmUserInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d76ef00074bc4482923b1de26c3ee6ebf8d0f3860387784e362c9d0babe57491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="backupDestination")
    def backup_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupDestination"))

    @backup_destination.setter
    def backup_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc57945e7fb3ff0d51e19b6b8c85a235da5281cdf2236a4b8ff5d6c59dc07d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupDestination", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b60a8753b02ffb321260cf979cee0b7970dce73f6640e894823fe659397e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8e960ee2582e1e3922a1810cd5a40ee53257265bd430d80065545ecd037775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43bf71ff63f06211b4d143fd3724b886a5877b6f143298547f72f9b46ae3f11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="meteringFrequency")
    def metering_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meteringFrequency"))

    @metering_frequency.setter
    def metering_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ef7c28a9a58d0f1557beee3532c7358916d743c603888d5e69efaa19e91a57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meteringFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82bdc077a229f4de6dfed0c0885674194ae8f5dfd2403c78b10e4bc44a99ce0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ceae310c62032039ea29c6d14cbe8ab7736c283abc56bc2496b32a007e7fe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69766d6bc3b3604874023de2b74cbc1cfc98a71e999ba3681504feb1b68cffc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c1a542cc8c38c20f8d87e95f0a9405e5c7983cd1ebeb64870dc2b444a033f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fd30a42ff2ad3f5dda1fc8fce8ccc082eeb393eeb1af296d089eb4241593b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKey", value)

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c5ee6ee2dec02bb45735385e3f103d0350455f509bbba96a833d4327f9bc7cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value)

    @builtins.property
    @jsii.member(jsii_name="vmUser")
    def vm_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmUser"))

    @vm_user.setter
    def vm_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ce2bb4f388f5cf6298835a16e6b1802883d9817038bc8231923829eed77a2cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmUser", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceBackups",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_storage_container": "cloudStorageContainer",
        "cloud_storage_password": "cloudStoragePassword",
        "cloud_storage_username": "cloudStorageUsername",
        "create_if_missing": "createIfMissing",
    },
)
class MysqlServiceInstanceBackups:
    def __init__(
        self,
        *,
        cloud_storage_container: builtins.str,
        cloud_storage_password: typing.Optional[builtins.str] = None,
        cloud_storage_username: typing.Optional[builtins.str] = None,
        create_if_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloud_storage_container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.
        :param cloud_storage_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.
        :param cloud_storage_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.
        :param create_if_missing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da69a93c1e07db467a3f29d92cf7bead710542f04a7b2795500ce5bf8dc33b4)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_container MysqlServiceInstance#cloud_storage_container}.'''
        result = self._values.get("cloud_storage_container")
        assert result is not None, "Required property 'cloud_storage_container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_storage_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_password MysqlServiceInstance#cloud_storage_password}.'''
        result = self._values.get("cloud_storage_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_storage_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#cloud_storage_username MysqlServiceInstance#cloud_storage_username}.'''
        result = self._values.get("cloud_storage_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_if_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create_if_missing MysqlServiceInstance#create_if_missing}.'''
        result = self._values.get("create_if_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceBackups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceBackupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceBackupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69de2adf403ffc5f865650de4a8ea9955e4826b48815396a676d94ffbf94db24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90255132cace426c6aa2609f17cbd5a9d315acfe1f58d77bdf7f13b042ac4811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStorageContainer", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStoragePassword")
    def cloud_storage_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStoragePassword"))

    @cloud_storage_password.setter
    def cloud_storage_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53ef637201cf122268d96c62b979bacc01b93d7499c0b950f932af8de30364d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudStoragePassword", value)

    @builtins.property
    @jsii.member(jsii_name="cloudStorageUsername")
    def cloud_storage_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudStorageUsername"))

    @cloud_storage_username.setter
    def cloud_storage_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7667afb796ad6f698c4b37606459fba953621a1dc100e5015673d34ad91308f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3eb7941bda38c977088f28713fe3559f4330c42defc1d30d845902e4fb6a423b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIfMissing", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MysqlServiceInstanceBackups]:
        return typing.cast(typing.Optional[MysqlServiceInstanceBackups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceBackups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27771853f2e964da8ac1078fd6b4451f83501b7f767128da5e3a7bccf4b9e13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mysql_configuration": "mysqlConfiguration",
        "name": "name",
        "shape": "shape",
        "ssh_public_key": "sshPublicKey",
        "availability_domain": "availabilityDomain",
        "backup_destination": "backupDestination",
        "backups": "backups",
        "description": "description",
        "id": "id",
        "ip_network": "ipNetwork",
        "metering_frequency": "meteringFrequency",
        "notification_email": "notificationEmail",
        "region": "region",
        "subnet": "subnet",
        "timeouts": "timeouts",
        "vm_user": "vmUser",
    },
)
class MysqlServiceInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        mysql_configuration: typing.Union["MysqlServiceInstanceMysqlConfiguration", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        shape: builtins.str,
        ssh_public_key: builtins.str,
        availability_domain: typing.Optional[builtins.str] = None,
        backup_destination: typing.Optional[builtins.str] = None,
        backups: typing.Optional[typing.Union[MysqlServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        metering_frequency: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MysqlServiceInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vm_user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mysql_configuration: mysql_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.
        :param ssh_public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.
        :param backup_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.
        :param backups: backups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.
        :param metering_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.
        :param subnet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        :param vm_user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(mysql_configuration, dict):
            mysql_configuration = MysqlServiceInstanceMysqlConfiguration(**mysql_configuration)
        if isinstance(backups, dict):
            backups = MysqlServiceInstanceBackups(**backups)
        if isinstance(timeouts, dict):
            timeouts = MysqlServiceInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931cbde9228035994084a878ed25cc466a3c05db49df986d92064d9a783d5d8a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mysql_configuration", value=mysql_configuration, expected_type=type_hints["mysql_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument ssh_public_key", value=ssh_public_key, expected_type=type_hints["ssh_public_key"])
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument backup_destination", value=backup_destination, expected_type=type_hints["backup_destination"])
            check_type(argname="argument backups", value=backups, expected_type=type_hints["backups"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument metering_frequency", value=metering_frequency, expected_type=type_hints["metering_frequency"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vm_user", value=vm_user, expected_type=type_hints["vm_user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mysql_configuration": mysql_configuration,
            "name": name,
            "shape": shape,
            "ssh_public_key": ssh_public_key,
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
        if backup_destination is not None:
            self._values["backup_destination"] = backup_destination
        if backups is not None:
            self._values["backups"] = backups
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if metering_frequency is not None:
            self._values["metering_frequency"] = metering_frequency
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if region is not None:
            self._values["region"] = region
        if subnet is not None:
            self._values["subnet"] = subnet
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vm_user is not None:
            self._values["vm_user"] = vm_user

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
    def mysql_configuration(self) -> "MysqlServiceInstanceMysqlConfiguration":
        '''mysql_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_configuration MysqlServiceInstance#mysql_configuration}
        '''
        result = self._values.get("mysql_configuration")
        assert result is not None, "Required property 'mysql_configuration' is missing"
        return typing.cast("MysqlServiceInstanceMysqlConfiguration", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#name MysqlServiceInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#shape MysqlServiceInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ssh_public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ssh_public_key MysqlServiceInstance#ssh_public_key}.'''
        result = self._values.get("ssh_public_key")
        assert result is not None, "Required property 'ssh_public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#availability_domain MysqlServiceInstance#availability_domain}.'''
        result = self._values.get("availability_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backup_destination MysqlServiceInstance#backup_destination}.'''
        result = self._values.get("backup_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backups(self) -> typing.Optional[MysqlServiceInstanceBackups]:
        '''backups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#backups MysqlServiceInstance#backups}
        '''
        result = self._values.get("backups")
        return typing.cast(typing.Optional[MysqlServiceInstanceBackups], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#description MysqlServiceInstance#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#id MysqlServiceInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#ip_network MysqlServiceInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metering_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#metering_frequency MysqlServiceInstance#metering_frequency}.'''
        result = self._values.get("metering_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#notification_email MysqlServiceInstance#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#region MysqlServiceInstance#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#subnet MysqlServiceInstance#subnet}.'''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MysqlServiceInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#timeouts MysqlServiceInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MysqlServiceInstanceTimeouts"], result)

    @builtins.property
    def vm_user(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#vm_user MysqlServiceInstance#vm_user}.'''
        result = self._values.get("vm_user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "db_name": "dbName",
        "db_storage": "dbStorage",
        "enterprise_monitor_configuration": "enterpriseMonitorConfiguration",
        "mysql_charset": "mysqlCharset",
        "mysql_collation": "mysqlCollation",
        "mysql_password": "mysqlPassword",
        "mysql_port": "mysqlPort",
        "mysql_username": "mysqlUsername",
        "snapshot_name": "snapshotName",
        "source_service_name": "sourceServiceName",
    },
)
class MysqlServiceInstanceMysqlConfiguration:
    def __init__(
        self,
        *,
        db_name: typing.Optional[builtins.str] = None,
        db_storage: typing.Optional[jsii.Number] = None,
        enterprise_monitor_configuration: typing.Optional[typing.Union["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        mysql_charset: typing.Optional[builtins.str] = None,
        mysql_collation: typing.Optional[builtins.str] = None,
        mysql_password: typing.Optional[builtins.str] = None,
        mysql_port: typing.Optional[jsii.Number] = None,
        mysql_username: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        source_service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param db_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.
        :param db_storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.
        :param enterprise_monitor_configuration: enterprise_monitor_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        :param mysql_charset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.
        :param mysql_collation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.
        :param mysql_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.
        :param mysql_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.
        :param mysql_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.
        :param snapshot_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.
        :param source_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.
        '''
        if isinstance(enterprise_monitor_configuration, dict):
            enterprise_monitor_configuration = MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(**enterprise_monitor_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9528811a849a6a52ab7e10120e01d2f55332125120fedcdf92eb3f47d11b4875)
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument db_storage", value=db_storage, expected_type=type_hints["db_storage"])
            check_type(argname="argument enterprise_monitor_configuration", value=enterprise_monitor_configuration, expected_type=type_hints["enterprise_monitor_configuration"])
            check_type(argname="argument mysql_charset", value=mysql_charset, expected_type=type_hints["mysql_charset"])
            check_type(argname="argument mysql_collation", value=mysql_collation, expected_type=type_hints["mysql_collation"])
            check_type(argname="argument mysql_password", value=mysql_password, expected_type=type_hints["mysql_password"])
            check_type(argname="argument mysql_port", value=mysql_port, expected_type=type_hints["mysql_port"])
            check_type(argname="argument mysql_username", value=mysql_username, expected_type=type_hints["mysql_username"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument source_service_name", value=source_service_name, expected_type=type_hints["source_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if db_name is not None:
            self._values["db_name"] = db_name
        if db_storage is not None:
            self._values["db_storage"] = db_storage
        if enterprise_monitor_configuration is not None:
            self._values["enterprise_monitor_configuration"] = enterprise_monitor_configuration
        if mysql_charset is not None:
            self._values["mysql_charset"] = mysql_charset
        if mysql_collation is not None:
            self._values["mysql_collation"] = mysql_collation
        if mysql_password is not None:
            self._values["mysql_password"] = mysql_password
        if mysql_port is not None:
            self._values["mysql_port"] = mysql_port
        if mysql_username is not None:
            self._values["mysql_username"] = mysql_username
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if source_service_name is not None:
            self._values["source_service_name"] = source_service_name

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_name MysqlServiceInstance#db_name}.'''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_storage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#db_storage MysqlServiceInstance#db_storage}.'''
        result = self._values.get("db_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enterprise_monitor_configuration(
        self,
    ) -> typing.Optional["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration"]:
        '''enterprise_monitor_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#enterprise_monitor_configuration MysqlServiceInstance#enterprise_monitor_configuration}
        '''
        result = self._values.get("enterprise_monitor_configuration")
        return typing.cast(typing.Optional["MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration"], result)

    @builtins.property
    def mysql_charset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_charset MysqlServiceInstance#mysql_charset}.'''
        result = self._values.get("mysql_charset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_collation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_collation MysqlServiceInstance#mysql_collation}.'''
        result = self._values.get("mysql_collation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_password MysqlServiceInstance#mysql_password}.'''
        result = self._values.get("mysql_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mysql_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_port MysqlServiceInstance#mysql_port}.'''
        result = self._values.get("mysql_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mysql_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#mysql_username MysqlServiceInstance#mysql_username}.'''
        result = self._values.get("mysql_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#snapshot_name MysqlServiceInstance#snapshot_name}.'''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#source_service_name MysqlServiceInstance#source_service_name}.'''
        result = self._values.get("source_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceMysqlConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "em_agent_password": "emAgentPassword",
        "em_agent_username": "emAgentUsername",
        "em_password": "emPassword",
        "em_port": "emPort",
        "em_username": "emUsername",
    },
)
class MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration:
    def __init__(
        self,
        *,
        em_agent_password: typing.Optional[builtins.str] = None,
        em_agent_username: typing.Optional[builtins.str] = None,
        em_password: typing.Optional[builtins.str] = None,
        em_port: typing.Optional[jsii.Number] = None,
        em_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param em_agent_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.
        :param em_agent_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.
        :param em_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.
        :param em_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.
        :param em_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e59e4377b4d0b20eecb3cd05d8e6dddb40fbe7f90143c2df778dedd2a33ca1b)
            check_type(argname="argument em_agent_password", value=em_agent_password, expected_type=type_hints["em_agent_password"])
            check_type(argname="argument em_agent_username", value=em_agent_username, expected_type=type_hints["em_agent_username"])
            check_type(argname="argument em_password", value=em_password, expected_type=type_hints["em_password"])
            check_type(argname="argument em_port", value=em_port, expected_type=type_hints["em_port"])
            check_type(argname="argument em_username", value=em_username, expected_type=type_hints["em_username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if em_agent_password is not None:
            self._values["em_agent_password"] = em_agent_password
        if em_agent_username is not None:
            self._values["em_agent_username"] = em_agent_username
        if em_password is not None:
            self._values["em_password"] = em_password
        if em_port is not None:
            self._values["em_port"] = em_port
        if em_username is not None:
            self._values["em_username"] = em_username

    @builtins.property
    def em_agent_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.'''
        result = self._values.get("em_agent_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_agent_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.'''
        result = self._values.get("em_agent_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.'''
        result = self._values.get("em_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def em_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.'''
        result = self._values.get("em_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def em_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.'''
        result = self._values.get("em_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84097b45f71c0b6e736ab64cf57b909355044902413a9b2d81db6e60a522c104)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmAgentPassword")
    def reset_em_agent_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmAgentPassword", []))

    @jsii.member(jsii_name="resetEmAgentUsername")
    def reset_em_agent_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmAgentUsername", []))

    @jsii.member(jsii_name="resetEmPassword")
    def reset_em_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmPassword", []))

    @jsii.member(jsii_name="resetEmPort")
    def reset_em_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmPort", []))

    @jsii.member(jsii_name="resetEmUsername")
    def reset_em_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmUsername", []))

    @builtins.property
    @jsii.member(jsii_name="emAgentPasswordInput")
    def em_agent_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emAgentPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="emAgentUsernameInput")
    def em_agent_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emAgentUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="emPasswordInput")
    def em_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="emPortInput")
    def em_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "emPortInput"))

    @builtins.property
    @jsii.member(jsii_name="emUsernameInput")
    def em_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="emAgentPassword")
    def em_agent_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emAgentPassword"))

    @em_agent_password.setter
    def em_agent_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e927622829744167b727aeb44240c64a60d650c93654da4a4c2ba60ad7583f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emAgentPassword", value)

    @builtins.property
    @jsii.member(jsii_name="emAgentUsername")
    def em_agent_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emAgentUsername"))

    @em_agent_username.setter
    def em_agent_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e9fb168d2032d077f2b63f67a6aa5c437b12e0261e82d4038df9dddb51f9b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emAgentUsername", value)

    @builtins.property
    @jsii.member(jsii_name="emPassword")
    def em_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emPassword"))

    @em_password.setter
    def em_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f4dad05b6e2f468613b889ae23d81a9dfe67143a4fe39df694b38e15b352ddb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emPassword", value)

    @builtins.property
    @jsii.member(jsii_name="emPort")
    def em_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "emPort"))

    @em_port.setter
    def em_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8c034ca97836cc21ef99d21d575de9fdc2f0c7ca8932dc2dc4da6574a70f35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emPort", value)

    @builtins.property
    @jsii.member(jsii_name="emUsername")
    def em_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emUsername"))

    @em_username.setter
    def em_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec55678d95ff04d8f638d0c2e469267447046bbb5e65d566eef47461b6e04fe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7850c4de0e35d00529c8cd1125d4ba780867abf3b9c3e42a9c624a31a13f7a21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MysqlServiceInstanceMysqlConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceMysqlConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fddfb9095ae299522234022b513af9bd210f2bf5c4575844b653d3bad1ac0c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEnterpriseMonitorConfiguration")
    def put_enterprise_monitor_configuration(
        self,
        *,
        em_agent_password: typing.Optional[builtins.str] = None,
        em_agent_username: typing.Optional[builtins.str] = None,
        em_password: typing.Optional[builtins.str] = None,
        em_port: typing.Optional[jsii.Number] = None,
        em_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param em_agent_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_password MysqlServiceInstance#em_agent_password}.
        :param em_agent_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_agent_username MysqlServiceInstance#em_agent_username}.
        :param em_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_password MysqlServiceInstance#em_password}.
        :param em_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_port MysqlServiceInstance#em_port}.
        :param em_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#em_username MysqlServiceInstance#em_username}.
        '''
        value = MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration(
            em_agent_password=em_agent_password,
            em_agent_username=em_agent_username,
            em_password=em_password,
            em_port=em_port,
            em_username=em_username,
        )

        return typing.cast(None, jsii.invoke(self, "putEnterpriseMonitorConfiguration", [value]))

    @jsii.member(jsii_name="resetDbName")
    def reset_db_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbName", []))

    @jsii.member(jsii_name="resetDbStorage")
    def reset_db_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbStorage", []))

    @jsii.member(jsii_name="resetEnterpriseMonitorConfiguration")
    def reset_enterprise_monitor_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnterpriseMonitorConfiguration", []))

    @jsii.member(jsii_name="resetMysqlCharset")
    def reset_mysql_charset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlCharset", []))

    @jsii.member(jsii_name="resetMysqlCollation")
    def reset_mysql_collation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlCollation", []))

    @jsii.member(jsii_name="resetMysqlPassword")
    def reset_mysql_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlPassword", []))

    @jsii.member(jsii_name="resetMysqlPort")
    def reset_mysql_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlPort", []))

    @jsii.member(jsii_name="resetMysqlUsername")
    def reset_mysql_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlUsername", []))

    @jsii.member(jsii_name="resetSnapshotName")
    def reset_snapshot_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotName", []))

    @jsii.member(jsii_name="resetSourceServiceName")
    def reset_source_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="connectString")
    def connect_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectString"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseMonitorConfiguration")
    def enterprise_monitor_configuration(
        self,
    ) -> MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference:
        return typing.cast(MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference, jsii.get(self, "enterpriseMonitorConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddress")
    def public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbStorageInput")
    def db_storage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dbStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="enterpriseMonitorConfigurationInput")
    def enterprise_monitor_configuration_input(
        self,
    ) -> typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration], jsii.get(self, "enterpriseMonitorConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlCharsetInput")
    def mysql_charset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlCharsetInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlCollationInput")
    def mysql_collation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlCollationInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlPasswordInput")
    def mysql_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlPortInput")
    def mysql_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mysqlPortInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlUsernameInput")
    def mysql_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotNameInput")
    def snapshot_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceNameInput")
    def source_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__052ec5770e7c0de49aed64e8cb130514485959513b3a20a4a3dfec7cb5f77e96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="dbStorage")
    def db_storage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dbStorage"))

    @db_storage.setter
    def db_storage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6fd184087d8b573f4861d9a81dc61340a2b9848de70fe8146edaf95be8a06c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbStorage", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlCharset")
    def mysql_charset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlCharset"))

    @mysql_charset.setter
    def mysql_charset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2458ac9885501edff66eeb63c2d295147254753edc6f1b2b587ec9fce333948c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlCharset", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlCollation")
    def mysql_collation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlCollation"))

    @mysql_collation.setter
    def mysql_collation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b270ecd53b3601d459e25f608bc7ffbc1faaaa069aed4832e01b5dabda3d5d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlCollation", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlPassword")
    def mysql_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlPassword"))

    @mysql_password.setter
    def mysql_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c520626e85c15fe12cb1cdd0f02de0f5756152b2dfe4e62260a81271ae1ec75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlPassword", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlPort")
    def mysql_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mysqlPort"))

    @mysql_port.setter
    def mysql_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7d6960e77b69463549a4601deb9773a00f6b6d6d1a3394fbb53f07404f069b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlPort", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlUsername")
    def mysql_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mysqlUsername"))

    @mysql_username.setter
    def mysql_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455becb3b6395c222da54d2229cf9433aeb2299f9c063838e9433a9d8ce26273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlUsername", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53cda1e0e222cb72944a012e0df30f6708adc120cc28c9b716b97f2fdcf2e2d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServiceName")
    def source_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceServiceName"))

    @source_service_name.setter
    def source_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2521123b40e5510535e4aeb38b746d7d6288955e5532a43fa88d206ee413dc31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MysqlServiceInstanceMysqlConfiguration]:
        return typing.cast(typing.Optional[MysqlServiceInstanceMysqlConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MysqlServiceInstanceMysqlConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e6c8dc5b71fd198f4d8fa26bb67d60adfd5e176724275a7445556111ccefec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class MysqlServiceInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257d79dbfaf6d6140e05df71bd03ce28cf7bceee5c371b65d18d7059f18cf531)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#create MysqlServiceInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/mysql_service_instance#delete MysqlServiceInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MysqlServiceInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MysqlServiceInstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.mysqlServiceInstance.MysqlServiceInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c752b753f3796361731ebce6bf7f33e9144560c45a5185b74a8d8d00ebc2a6a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68335f5aa8a02a6e9827ee2f57cd8906a9621ec5a296644d6acab53589f6b02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab58e386c2b3ac385e7399eb6c489cfb0e64c9538ea7e7709e1394809873149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638364a78a5cda2b10973d30eb313d58f55a7b3f9950a08186e09b1fb221cd73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MysqlServiceInstance",
    "MysqlServiceInstanceBackups",
    "MysqlServiceInstanceBackupsOutputReference",
    "MysqlServiceInstanceConfig",
    "MysqlServiceInstanceMysqlConfiguration",
    "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration",
    "MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfigurationOutputReference",
    "MysqlServiceInstanceMysqlConfigurationOutputReference",
    "MysqlServiceInstanceTimeouts",
    "MysqlServiceInstanceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__080e8493600a06bc7a4f88093d69b09055c60a1afd83a9df3aa7bb069e423514(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mysql_configuration: typing.Union[MysqlServiceInstanceMysqlConfiguration, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    shape: builtins.str,
    ssh_public_key: builtins.str,
    availability_domain: typing.Optional[builtins.str] = None,
    backup_destination: typing.Optional[builtins.str] = None,
    backups: typing.Optional[typing.Union[MysqlServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    metering_frequency: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vm_user: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d76ef00074bc4482923b1de26c3ee6ebf8d0f3860387784e362c9d0babe57491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc57945e7fb3ff0d51e19b6b8c85a235da5281cdf2236a4b8ff5d6c59dc07d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b60a8753b02ffb321260cf979cee0b7970dce73f6640e894823fe659397e10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8e960ee2582e1e3922a1810cd5a40ee53257265bd430d80065545ecd037775(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b43bf71ff63f06211b4d143fd3724b886a5877b6f143298547f72f9b46ae3f11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ef7c28a9a58d0f1557beee3532c7358916d743c603888d5e69efaa19e91a57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82bdc077a229f4de6dfed0c0885674194ae8f5dfd2403c78b10e4bc44a99ce0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ceae310c62032039ea29c6d14cbe8ab7736c283abc56bc2496b32a007e7fe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69766d6bc3b3604874023de2b74cbc1cfc98a71e999ba3681504feb1b68cffc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c1a542cc8c38c20f8d87e95f0a9405e5c7983cd1ebeb64870dc2b444a033f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fd30a42ff2ad3f5dda1fc8fce8ccc082eeb393eeb1af296d089eb4241593b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5ee6ee2dec02bb45735385e3f103d0350455f509bbba96a833d4327f9bc7cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce2bb4f388f5cf6298835a16e6b1802883d9817038bc8231923829eed77a2cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da69a93c1e07db467a3f29d92cf7bead710542f04a7b2795500ce5bf8dc33b4(
    *,
    cloud_storage_container: builtins.str,
    cloud_storage_password: typing.Optional[builtins.str] = None,
    cloud_storage_username: typing.Optional[builtins.str] = None,
    create_if_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69de2adf403ffc5f865650de4a8ea9955e4826b48815396a676d94ffbf94db24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90255132cace426c6aa2609f17cbd5a9d315acfe1f58d77bdf7f13b042ac4811(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53ef637201cf122268d96c62b979bacc01b93d7499c0b950f932af8de30364d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7667afb796ad6f698c4b37606459fba953621a1dc100e5015673d34ad91308f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb7941bda38c977088f28713fe3559f4330c42defc1d30d845902e4fb6a423b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27771853f2e964da8ac1078fd6b4451f83501b7f767128da5e3a7bccf4b9e13(
    value: typing.Optional[MysqlServiceInstanceBackups],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931cbde9228035994084a878ed25cc466a3c05db49df986d92064d9a783d5d8a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mysql_configuration: typing.Union[MysqlServiceInstanceMysqlConfiguration, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    shape: builtins.str,
    ssh_public_key: builtins.str,
    availability_domain: typing.Optional[builtins.str] = None,
    backup_destination: typing.Optional[builtins.str] = None,
    backups: typing.Optional[typing.Union[MysqlServiceInstanceBackups, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    metering_frequency: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    subnet: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vm_user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9528811a849a6a52ab7e10120e01d2f55332125120fedcdf92eb3f47d11b4875(
    *,
    db_name: typing.Optional[builtins.str] = None,
    db_storage: typing.Optional[jsii.Number] = None,
    enterprise_monitor_configuration: typing.Optional[typing.Union[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    mysql_charset: typing.Optional[builtins.str] = None,
    mysql_collation: typing.Optional[builtins.str] = None,
    mysql_password: typing.Optional[builtins.str] = None,
    mysql_port: typing.Optional[jsii.Number] = None,
    mysql_username: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    source_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e59e4377b4d0b20eecb3cd05d8e6dddb40fbe7f90143c2df778dedd2a33ca1b(
    *,
    em_agent_password: typing.Optional[builtins.str] = None,
    em_agent_username: typing.Optional[builtins.str] = None,
    em_password: typing.Optional[builtins.str] = None,
    em_port: typing.Optional[jsii.Number] = None,
    em_username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84097b45f71c0b6e736ab64cf57b909355044902413a9b2d81db6e60a522c104(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e927622829744167b727aeb44240c64a60d650c93654da4a4c2ba60ad7583f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e9fb168d2032d077f2b63f67a6aa5c437b12e0261e82d4038df9dddb51f9b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f4dad05b6e2f468613b889ae23d81a9dfe67143a4fe39df694b38e15b352ddb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8c034ca97836cc21ef99d21d575de9fdc2f0c7ca8932dc2dc4da6574a70f35(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec55678d95ff04d8f638d0c2e469267447046bbb5e65d566eef47461b6e04fe8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7850c4de0e35d00529c8cd1125d4ba780867abf3b9c3e42a9c624a31a13f7a21(
    value: typing.Optional[MysqlServiceInstanceMysqlConfigurationEnterpriseMonitorConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fddfb9095ae299522234022b513af9bd210f2bf5c4575844b653d3bad1ac0c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052ec5770e7c0de49aed64e8cb130514485959513b3a20a4a3dfec7cb5f77e96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6fd184087d8b573f4861d9a81dc61340a2b9848de70fe8146edaf95be8a06c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2458ac9885501edff66eeb63c2d295147254753edc6f1b2b587ec9fce333948c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b270ecd53b3601d459e25f608bc7ffbc1faaaa069aed4832e01b5dabda3d5d9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c520626e85c15fe12cb1cdd0f02de0f5756152b2dfe4e62260a81271ae1ec75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7d6960e77b69463549a4601deb9773a00f6b6d6d1a3394fbb53f07404f069b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455becb3b6395c222da54d2229cf9433aeb2299f9c063838e9433a9d8ce26273(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53cda1e0e222cb72944a012e0df30f6708adc120cc28c9b716b97f2fdcf2e2d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2521123b40e5510535e4aeb38b746d7d6288955e5532a43fa88d206ee413dc31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e6c8dc5b71fd198f4d8fa26bb67d60adfd5e176724275a7445556111ccefec(
    value: typing.Optional[MysqlServiceInstanceMysqlConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257d79dbfaf6d6140e05df71bd03ce28cf7bceee5c371b65d18d7059f18cf531(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c752b753f3796361731ebce6bf7f33e9144560c45a5185b74a8d8d00ebc2a6a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68335f5aa8a02a6e9827ee2f57cd8906a9621ec5a296644d6acab53589f6b02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab58e386c2b3ac385e7399eb6c489cfb0e64c9538ea7e7709e1394809873149(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638364a78a5cda2b10973d30eb313d58f55a7b3f9950a08186e09b1fb221cd73(
    value: typing.Optional[typing.Union[MysqlServiceInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
