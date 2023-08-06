'''
# `oraclepaas_application_container`

Refer to the Terraform Registory for docs: [`oraclepaas_application_container`](https://www.terraform.io/docs/providers/oraclepaas/r/application_container).
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


class ApplicationContainer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container oraclepaas_application_container}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        archive_url: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        availability_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        deployment: typing.Optional[typing.Union["ApplicationContainerDeployment", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_file: typing.Optional[builtins.str] = None,
        git_password: typing.Optional[builtins.str] = None,
        git_repository: typing.Optional[builtins.str] = None,
        git_username: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        manifest: typing.Optional[typing.Union["ApplicationContainerManifest", typing.Dict[builtins.str, typing.Any]]] = None,
        manifest_file: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[builtins.str] = None,
        subscription_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationContainerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container oraclepaas_application_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#name ApplicationContainer#name}.
        :param archive_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#archive_url ApplicationContainer#archive_url}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#auth_type ApplicationContainer#auth_type}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#availability_domain ApplicationContainer#availability_domain}.
        :param deployment: deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment ApplicationContainer#deployment}
        :param deployment_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment_file ApplicationContainer#deployment_file}.
        :param git_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_password ApplicationContainer#git_password}.
        :param git_repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_repository ApplicationContainer#git_repository}.
        :param git_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_username ApplicationContainer#git_username}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#id ApplicationContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#load_balancer_subnets ApplicationContainer#load_balancer_subnets}.
        :param manifest: manifest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest ApplicationContainer#manifest}
        :param manifest_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest_file ApplicationContainer#manifest_file}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notification_email ApplicationContainer#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#region ApplicationContainer#region}.
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}.
        :param subscription_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#subscription_type ApplicationContainer#subscription_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#tags ApplicationContainer#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#timeouts ApplicationContainer#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8361d7d5da8c26544198a52dd056c9c0e1871c85215c731a34d9456e979960b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationContainerConfig(
            name=name,
            archive_url=archive_url,
            auth_type=auth_type,
            availability_domain=availability_domain,
            deployment=deployment,
            deployment_file=deployment_file,
            git_password=git_password,
            git_repository=git_repository,
            git_username=git_username,
            id=id,
            load_balancer_subnets=load_balancer_subnets,
            manifest=manifest,
            manifest_file=manifest_file,
            notes=notes,
            notification_email=notification_email,
            region=region,
            runtime=runtime,
            subscription_type=subscription_type,
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

    @jsii.member(jsii_name="putDeployment")
    def put_deployment(
        self,
        *,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instances: typing.Optional[jsii.Number] = None,
        java_system_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        secure_environment: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationContainerDeploymentServices", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#environment ApplicationContainer#environment}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#instances ApplicationContainer#instances}.
        :param java_system_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#java_system_properties ApplicationContainer#java_system_properties}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#memory ApplicationContainer#memory}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param secure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#secure_environment ApplicationContainer#secure_environment}.
        :param services: services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#services ApplicationContainer#services}
        '''
        value = ApplicationContainerDeployment(
            environment=environment,
            instances=instances,
            java_system_properties=java_system_properties,
            memory=memory,
            notes=notes,
            secure_environment=secure_environment,
            services=services,
        )

        return typing.cast(None, jsii.invoke(self, "putDeployment", [value]))

    @jsii.member(jsii_name="putManifest")
    def put_manifest(
        self,
        *,
        clustered: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        command: typing.Optional[builtins.str] = None,
        health_check_endpoint: typing.Optional[builtins.str] = None,
        home: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        release: typing.Optional[typing.Union["ApplicationContainerManifestRelease", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime: typing.Optional[typing.Union["ApplicationContainerManifestRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        shutdown_time: typing.Optional[jsii.Number] = None,
        startup_time: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param clustered: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#clustered ApplicationContainer#clustered}.
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#command ApplicationContainer#command}.
        :param health_check_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#health_check_endpoint ApplicationContainer#health_check_endpoint}.
        :param home: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#home ApplicationContainer#home}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#mode ApplicationContainer#mode}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param release: release block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#release ApplicationContainer#release}
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}
        :param shutdown_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#shutdown_time ApplicationContainer#shutdown_time}.
        :param startup_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#startup_time ApplicationContainer#startup_time}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#type ApplicationContainer#type}.
        '''
        value = ApplicationContainerManifest(
            clustered=clustered,
            command=command,
            health_check_endpoint=health_check_endpoint,
            home=home,
            mode=mode,
            notes=notes,
            release=release,
            runtime=runtime,
            shutdown_time=shutdown_time,
            startup_time=startup_time,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putManifest", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#create ApplicationContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#delete ApplicationContainer#delete}.
        '''
        value = ApplicationContainerTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetArchiveUrl")
    def reset_archive_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUrl", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetAvailabilityDomain")
    def reset_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityDomain", []))

    @jsii.member(jsii_name="resetDeployment")
    def reset_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployment", []))

    @jsii.member(jsii_name="resetDeploymentFile")
    def reset_deployment_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentFile", []))

    @jsii.member(jsii_name="resetGitPassword")
    def reset_git_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitPassword", []))

    @jsii.member(jsii_name="resetGitRepository")
    def reset_git_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitRepository", []))

    @jsii.member(jsii_name="resetGitUsername")
    def reset_git_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitUsername", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancerSubnets")
    def reset_load_balancer_subnets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerSubnets", []))

    @jsii.member(jsii_name="resetManifest")
    def reset_manifest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManifest", []))

    @jsii.member(jsii_name="resetManifestFile")
    def reset_manifest_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManifestFile", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetNotificationEmail")
    def reset_notification_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationEmail", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetSubscriptionType")
    def reset_subscription_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionType", []))

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
    @jsii.member(jsii_name="appUrl")
    def app_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appUrl"))

    @builtins.property
    @jsii.member(jsii_name="deployment")
    def deployment(self) -> "ApplicationContainerDeploymentOutputReference":
        return typing.cast("ApplicationContainerDeploymentOutputReference", jsii.get(self, "deployment"))

    @builtins.property
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> "ApplicationContainerManifestOutputReference":
        return typing.cast("ApplicationContainerManifestOutputReference", jsii.get(self, "manifest"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApplicationContainerTimeoutsOutputReference":
        return typing.cast("ApplicationContainerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrlInput")
    def archive_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "archiveUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomainInput")
    def availability_domain_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "availabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentFileInput")
    def deployment_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentFileInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentInput")
    def deployment_input(self) -> typing.Optional["ApplicationContainerDeployment"]:
        return typing.cast(typing.Optional["ApplicationContainerDeployment"], jsii.get(self, "deploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="gitPasswordInput")
    def git_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="gitRepositoryInput")
    def git_repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="gitUsernameInput")
    def git_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSubnetsInput")
    def load_balancer_subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerSubnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="manifestFileInput")
    def manifest_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manifestFileInput"))

    @builtins.property
    @jsii.member(jsii_name="manifestInput")
    def manifest_input(self) -> typing.Optional["ApplicationContainerManifest"]:
        return typing.cast(typing.Optional["ApplicationContainerManifest"], jsii.get(self, "manifestInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationEmailInput")
    def notification_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionTypeInput")
    def subscription_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApplicationContainerTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApplicationContainerTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrl")
    def archive_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "archiveUrl"))

    @archive_url.setter
    def archive_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7e3e6cfff17be3a95a0e220b56826dfa7ba0008de387963920a7ce7c916636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUrl", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed685120e8254992de4da27d7169339e39fb90490129d02dae3977c337a1a571)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityDomain"))

    @availability_domain.setter
    def availability_domain(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__770ce04f014b7ae0f8f15a19a16d776ee5268904da9847eebcbd8d687c497ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentFile")
    def deployment_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentFile"))

    @deployment_file.setter
    def deployment_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7468b8bcc7746d838cc87555c91c325b1ef2c19ae4117e664998ccb89ea0e86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentFile", value)

    @builtins.property
    @jsii.member(jsii_name="gitPassword")
    def git_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitPassword"))

    @git_password.setter
    def git_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673c3d3f239e8ff00da0524642e04dabe74eca61f3f863a4fb754bd41baa6cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitPassword", value)

    @builtins.property
    @jsii.member(jsii_name="gitRepository")
    def git_repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitRepository"))

    @git_repository.setter
    def git_repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f8a01f6164cf10ddfebc394684cc580f664e72fdbd72a98239cb6ec0385dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitRepository", value)

    @builtins.property
    @jsii.member(jsii_name="gitUsername")
    def git_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitUsername"))

    @git_username.setter
    def git_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0601a4031a50a13c68af0bd41cee1174420b97afde3237e200e69e8e3612d46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitUsername", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e250752444d35fb4bf04d7f42c114d9e7ebdefc0ce0b515ffd5d4a03935bf6d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerSubnets")
    def load_balancer_subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerSubnets"))

    @load_balancer_subnets.setter
    def load_balancer_subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d9497108b41cf2a95b55debbe3c79b8689e457215d026099ce628a631ec2ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerSubnets", value)

    @builtins.property
    @jsii.member(jsii_name="manifestFile")
    def manifest_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manifestFile"))

    @manifest_file.setter
    def manifest_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0daebe302341e3bab3f16baf80af8af2aac2cc2b05f49f4b3313685bb05b923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestFile", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e8ec03bf55d69b6b577dad69a26edbeca1b55822befeb448a2463cc829952f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa47a6b6208440248e08420c497cc4e460bebaa1a8d73fefb5cb328bef426cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="notificationEmail")
    def notification_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationEmail"))

    @notification_email.setter
    def notification_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1daf016f8e402ceefeed903c63939d94b4b022b43f55c73e89989291bb7e2451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0851ac6a6a471d0acf9c4fad6acf312d2e7e699c2d314d6dee2f1e5c86d2611)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e62643a5f9557c375985986984533ef3dd6ca1c74b3f58d55d0c890adc4c394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionType")
    def subscription_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionType"))

    @subscription_type.setter
    def subscription_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6444ccc47a9ae0a153832d6cbdf8c1c80c2f0fcb500309d9f2e4e898f2e2ae6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afca485a7a0bc43616131ca6f0db7c4a6880caffece92009cc455b4beaf0ebe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerConfig",
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
        "archive_url": "archiveUrl",
        "auth_type": "authType",
        "availability_domain": "availabilityDomain",
        "deployment": "deployment",
        "deployment_file": "deploymentFile",
        "git_password": "gitPassword",
        "git_repository": "gitRepository",
        "git_username": "gitUsername",
        "id": "id",
        "load_balancer_subnets": "loadBalancerSubnets",
        "manifest": "manifest",
        "manifest_file": "manifestFile",
        "notes": "notes",
        "notification_email": "notificationEmail",
        "region": "region",
        "runtime": "runtime",
        "subscription_type": "subscriptionType",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ApplicationContainerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        archive_url: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        availability_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
        deployment: typing.Optional[typing.Union["ApplicationContainerDeployment", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_file: typing.Optional[builtins.str] = None,
        git_password: typing.Optional[builtins.str] = None,
        git_repository: typing.Optional[builtins.str] = None,
        git_username: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        manifest: typing.Optional[typing.Union["ApplicationContainerManifest", typing.Dict[builtins.str, typing.Any]]] = None,
        manifest_file: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        notification_email: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[builtins.str] = None,
        subscription_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationContainerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#name ApplicationContainer#name}.
        :param archive_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#archive_url ApplicationContainer#archive_url}.
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#auth_type ApplicationContainer#auth_type}.
        :param availability_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#availability_domain ApplicationContainer#availability_domain}.
        :param deployment: deployment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment ApplicationContainer#deployment}
        :param deployment_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment_file ApplicationContainer#deployment_file}.
        :param git_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_password ApplicationContainer#git_password}.
        :param git_repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_repository ApplicationContainer#git_repository}.
        :param git_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_username ApplicationContainer#git_username}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#id ApplicationContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_subnets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#load_balancer_subnets ApplicationContainer#load_balancer_subnets}.
        :param manifest: manifest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest ApplicationContainer#manifest}
        :param manifest_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest_file ApplicationContainer#manifest_file}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param notification_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notification_email ApplicationContainer#notification_email}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#region ApplicationContainer#region}.
        :param runtime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}.
        :param subscription_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#subscription_type ApplicationContainer#subscription_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#tags ApplicationContainer#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#timeouts ApplicationContainer#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(deployment, dict):
            deployment = ApplicationContainerDeployment(**deployment)
        if isinstance(manifest, dict):
            manifest = ApplicationContainerManifest(**manifest)
        if isinstance(timeouts, dict):
            timeouts = ApplicationContainerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03167c97a957cd9e6ec70c6ad7b64161d6ac14ddcb58e5a196f18822399af9a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument archive_url", value=archive_url, expected_type=type_hints["archive_url"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument availability_domain", value=availability_domain, expected_type=type_hints["availability_domain"])
            check_type(argname="argument deployment", value=deployment, expected_type=type_hints["deployment"])
            check_type(argname="argument deployment_file", value=deployment_file, expected_type=type_hints["deployment_file"])
            check_type(argname="argument git_password", value=git_password, expected_type=type_hints["git_password"])
            check_type(argname="argument git_repository", value=git_repository, expected_type=type_hints["git_repository"])
            check_type(argname="argument git_username", value=git_username, expected_type=type_hints["git_username"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancer_subnets", value=load_balancer_subnets, expected_type=type_hints["load_balancer_subnets"])
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument manifest_file", value=manifest_file, expected_type=type_hints["manifest_file"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument notification_email", value=notification_email, expected_type=type_hints["notification_email"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument subscription_type", value=subscription_type, expected_type=type_hints["subscription_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if archive_url is not None:
            self._values["archive_url"] = archive_url
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if availability_domain is not None:
            self._values["availability_domain"] = availability_domain
        if deployment is not None:
            self._values["deployment"] = deployment
        if deployment_file is not None:
            self._values["deployment_file"] = deployment_file
        if git_password is not None:
            self._values["git_password"] = git_password
        if git_repository is not None:
            self._values["git_repository"] = git_repository
        if git_username is not None:
            self._values["git_username"] = git_username
        if id is not None:
            self._values["id"] = id
        if load_balancer_subnets is not None:
            self._values["load_balancer_subnets"] = load_balancer_subnets
        if manifest is not None:
            self._values["manifest"] = manifest
        if manifest_file is not None:
            self._values["manifest_file"] = manifest_file
        if notes is not None:
            self._values["notes"] = notes
        if notification_email is not None:
            self._values["notification_email"] = notification_email
        if region is not None:
            self._values["region"] = region
        if runtime is not None:
            self._values["runtime"] = runtime
        if subscription_type is not None:
            self._values["subscription_type"] = subscription_type
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#name ApplicationContainer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#archive_url ApplicationContainer#archive_url}.'''
        result = self._values.get("archive_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#auth_type ApplicationContainer#auth_type}.'''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_domain(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#availability_domain ApplicationContainer#availability_domain}.'''
        result = self._values.get("availability_domain")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def deployment(self) -> typing.Optional["ApplicationContainerDeployment"]:
        '''deployment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment ApplicationContainer#deployment}
        '''
        result = self._values.get("deployment")
        return typing.cast(typing.Optional["ApplicationContainerDeployment"], result)

    @builtins.property
    def deployment_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#deployment_file ApplicationContainer#deployment_file}.'''
        result = self._values.get("deployment_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_password ApplicationContainer#git_password}.'''
        result = self._values.get("git_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_repository(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_repository ApplicationContainer#git_repository}.'''
        result = self._values.get("git_repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#git_username ApplicationContainer#git_username}.'''
        result = self._values.get("git_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#id ApplicationContainer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#load_balancer_subnets ApplicationContainer#load_balancer_subnets}.'''
        result = self._values.get("load_balancer_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def manifest(self) -> typing.Optional["ApplicationContainerManifest"]:
        '''manifest block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest ApplicationContainer#manifest}
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Optional["ApplicationContainerManifest"], result)

    @builtins.property
    def manifest_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#manifest_file ApplicationContainer#manifest_file}.'''
        result = self._values.get("manifest_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.'''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notification_email ApplicationContainer#notification_email}.'''
        result = self._values.get("notification_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#region ApplicationContainer#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}.'''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#subscription_type ApplicationContainer#subscription_type}.'''
        result = self._values.get("subscription_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#tags ApplicationContainer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApplicationContainerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#timeouts ApplicationContainer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationContainerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerDeployment",
    jsii_struct_bases=[],
    name_mapping={
        "environment": "environment",
        "instances": "instances",
        "java_system_properties": "javaSystemProperties",
        "memory": "memory",
        "notes": "notes",
        "secure_environment": "secureEnvironment",
        "services": "services",
    },
)
class ApplicationContainerDeployment:
    def __init__(
        self,
        *,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instances: typing.Optional[jsii.Number] = None,
        java_system_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        secure_environment: typing.Optional[typing.Sequence[builtins.str]] = None,
        services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationContainerDeploymentServices", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#environment ApplicationContainer#environment}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#instances ApplicationContainer#instances}.
        :param java_system_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#java_system_properties ApplicationContainer#java_system_properties}.
        :param memory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#memory ApplicationContainer#memory}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param secure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#secure_environment ApplicationContainer#secure_environment}.
        :param services: services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#services ApplicationContainer#services}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f022e172ef6646c4a6d26147ee33c778767468b96dfa2f3e95d34b953418c8ff)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument java_system_properties", value=java_system_properties, expected_type=type_hints["java_system_properties"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument secure_environment", value=secure_environment, expected_type=type_hints["secure_environment"])
            check_type(argname="argument services", value=services, expected_type=type_hints["services"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if environment is not None:
            self._values["environment"] = environment
        if instances is not None:
            self._values["instances"] = instances
        if java_system_properties is not None:
            self._values["java_system_properties"] = java_system_properties
        if memory is not None:
            self._values["memory"] = memory
        if notes is not None:
            self._values["notes"] = notes
        if secure_environment is not None:
            self._values["secure_environment"] = secure_environment
        if services is not None:
            self._values["services"] = services

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#environment ApplicationContainer#environment}.'''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instances(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#instances ApplicationContainer#instances}.'''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def java_system_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#java_system_properties ApplicationContainer#java_system_properties}.'''
        result = self._values.get("java_system_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#memory ApplicationContainer#memory}.'''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.'''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secure_environment(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#secure_environment ApplicationContainer#secure_environment}.'''
        result = self._values.get("secure_environment")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def services(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationContainerDeploymentServices"]]]:
        '''services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#services ApplicationContainer#services}
        '''
        result = self._values.get("services")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationContainerDeploymentServices"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerDeployment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerDeploymentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerDeploymentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9978dbb3703a7381253eaa51f1f8ecbfd863a322c6a434e51c33ad4b79f4bcae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putServices")
    def put_services(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ApplicationContainerDeploymentServices", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006a40252225194dec375d988b36a3261b92445aea97983d347daa5941ec4805)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServices", [value]))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetInstances")
    def reset_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstances", []))

    @jsii.member(jsii_name="resetJavaSystemProperties")
    def reset_java_system_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaSystemProperties", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetSecureEnvironment")
    def reset_secure_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureEnvironment", []))

    @jsii.member(jsii_name="resetServices")
    def reset_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServices", []))

    @builtins.property
    @jsii.member(jsii_name="services")
    def services(self) -> "ApplicationContainerDeploymentServicesList":
        return typing.cast("ApplicationContainerDeploymentServicesList", jsii.get(self, "services"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="javaSystemPropertiesInput")
    def java_system_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "javaSystemPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="secureEnvironmentInput")
    def secure_environment_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secureEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="servicesInput")
    def services_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationContainerDeploymentServices"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ApplicationContainerDeploymentServices"]]], jsii.get(self, "servicesInput"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fe621c4a5ea06b56d950482ff9f1f1930bc9d997559a38378e30d3983ebeb85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1436c47506d790fd6390b7341fe688a3c4f7d5110595a9959b8f3df5cc96a851)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="javaSystemProperties")
    def java_system_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "javaSystemProperties"))

    @java_system_properties.setter
    def java_system_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed8f18a913e7b9e01ba12669900566c2890012b34264aff694b87b7e0b8bd209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaSystemProperties", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f83c85f2f76e3e16114c6654ceb7b31c1af99cca272324d28adceec3a970ee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a2c36f1ac08d995fb64570ce9de4674c80709b1a6efafd96e10b70d02c36fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="secureEnvironment")
    def secure_environment(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secureEnvironment"))

    @secure_environment.setter
    def secure_environment(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1809cf40ff9d594a668a5bd005a5dddd321cb78215c88f9f35166205538189a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationContainerDeployment]:
        return typing.cast(typing.Optional[ApplicationContainerDeployment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationContainerDeployment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdcddc9d3537a1b1f84e01b49d4b288a359278441cf17781d8e6d95a9de95340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerDeploymentServices",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "name": "name",
        "password": "password",
        "type": "type",
        "username": "username",
    },
)
class ApplicationContainerDeploymentServices:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        name: builtins.str,
        password: builtins.str,
        type: builtins.str,
        username: builtins.str,
    ) -> None:
        '''
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#identifier ApplicationContainer#identifier}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#name ApplicationContainer#name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#password ApplicationContainer#password}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#type ApplicationContainer#type}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#username ApplicationContainer#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebdc9f18e191c4da461cd8d0fff12ce7c1b1826bb781cc50989e0c73ed060bb)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
            "name": name,
            "password": password,
            "type": type,
            "username": username,
        }

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#identifier ApplicationContainer#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#name ApplicationContainer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#password ApplicationContainer#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#type ApplicationContainer#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#username ApplicationContainer#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerDeploymentServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerDeploymentServicesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerDeploymentServicesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08a20727afa73251d5a253861e1fbe0fa83a0b4c7a7938fee79aa7f9aebfe6ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApplicationContainerDeploymentServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467abd5a0fa5c6bdf7ba46fceb9ae8bb372479981e1057aae78cc9ac547ed1ed)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApplicationContainerDeploymentServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1054c0462fe8b46443e60faa3628480174d9bcb21619ec7823a8757ce4a83de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87b8a2c1df02d905232cbdbdf0b75e1374774bbc464b6620f674836abb9c8601)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5c741dc6cf46e93fdc10c46bac79a60d90da20ca9bd5914c9c6b1634c513840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationContainerDeploymentServices]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationContainerDeploymentServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationContainerDeploymentServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a64bd50811166f705533152431206f7473213bdece92dde7dd728c3e349ab52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApplicationContainerDeploymentServicesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerDeploymentServicesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1089d0b019465c8f01ff23957a4aa52d4a8791f8e3fc173b0c4ae023273dc58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61fc109d0a8c5fe897f8c5cd4840b2724dc4d912ebc4e5a2083dd94f872023a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62e4abf63fe9ebb449885dc3b5faa19f742d14e903abb76265f99da21fd895ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4cf43ba9520af37982a325bde7b0a0d924b5c04d71fa4de0447fa2786c97e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05dc7a34ba91f24a3c40f7ba099cfe19bd3bbf5536e28936e3dbdfec7ecfae02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef26fdc92ec1fcedf5d2475e330265ce7fe0a73a89bd5e0e5a2735ed24d74a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationContainerDeploymentServices, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationContainerDeploymentServices, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationContainerDeploymentServices, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a4ebcf3c42e6a48d303e99bd39db04b9b3178c5971aa19aeec428a1c058c69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifest",
    jsii_struct_bases=[],
    name_mapping={
        "clustered": "clustered",
        "command": "command",
        "health_check_endpoint": "healthCheckEndpoint",
        "home": "home",
        "mode": "mode",
        "notes": "notes",
        "release": "release",
        "runtime": "runtime",
        "shutdown_time": "shutdownTime",
        "startup_time": "startupTime",
        "type": "type",
    },
)
class ApplicationContainerManifest:
    def __init__(
        self,
        *,
        clustered: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        command: typing.Optional[builtins.str] = None,
        health_check_endpoint: typing.Optional[builtins.str] = None,
        home: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        notes: typing.Optional[builtins.str] = None,
        release: typing.Optional[typing.Union["ApplicationContainerManifestRelease", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime: typing.Optional[typing.Union["ApplicationContainerManifestRuntime", typing.Dict[builtins.str, typing.Any]]] = None,
        shutdown_time: typing.Optional[jsii.Number] = None,
        startup_time: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param clustered: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#clustered ApplicationContainer#clustered}.
        :param command: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#command ApplicationContainer#command}.
        :param health_check_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#health_check_endpoint ApplicationContainer#health_check_endpoint}.
        :param home: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#home ApplicationContainer#home}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#mode ApplicationContainer#mode}.
        :param notes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.
        :param release: release block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#release ApplicationContainer#release}
        :param runtime: runtime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}
        :param shutdown_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#shutdown_time ApplicationContainer#shutdown_time}.
        :param startup_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#startup_time ApplicationContainer#startup_time}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#type ApplicationContainer#type}.
        '''
        if isinstance(release, dict):
            release = ApplicationContainerManifestRelease(**release)
        if isinstance(runtime, dict):
            runtime = ApplicationContainerManifestRuntime(**runtime)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21cef81d12bc88c6137fadc5117eb2a2494a4c68761bbd7a98e0e5cb61ec6fee)
            check_type(argname="argument clustered", value=clustered, expected_type=type_hints["clustered"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument health_check_endpoint", value=health_check_endpoint, expected_type=type_hints["health_check_endpoint"])
            check_type(argname="argument home", value=home, expected_type=type_hints["home"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument notes", value=notes, expected_type=type_hints["notes"])
            check_type(argname="argument release", value=release, expected_type=type_hints["release"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument shutdown_time", value=shutdown_time, expected_type=type_hints["shutdown_time"])
            check_type(argname="argument startup_time", value=startup_time, expected_type=type_hints["startup_time"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if clustered is not None:
            self._values["clustered"] = clustered
        if command is not None:
            self._values["command"] = command
        if health_check_endpoint is not None:
            self._values["health_check_endpoint"] = health_check_endpoint
        if home is not None:
            self._values["home"] = home
        if mode is not None:
            self._values["mode"] = mode
        if notes is not None:
            self._values["notes"] = notes
        if release is not None:
            self._values["release"] = release
        if runtime is not None:
            self._values["runtime"] = runtime
        if shutdown_time is not None:
            self._values["shutdown_time"] = shutdown_time
        if startup_time is not None:
            self._values["startup_time"] = startup_time
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def clustered(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#clustered ApplicationContainer#clustered}.'''
        result = self._values.get("clustered")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def command(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#command ApplicationContainer#command}.'''
        result = self._values.get("command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#health_check_endpoint ApplicationContainer#health_check_endpoint}.'''
        result = self._values.get("health_check_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#home ApplicationContainer#home}.'''
        result = self._values.get("home")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#mode ApplicationContainer#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#notes ApplicationContainer#notes}.'''
        result = self._values.get("notes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release(self) -> typing.Optional["ApplicationContainerManifestRelease"]:
        '''release block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#release ApplicationContainer#release}
        '''
        result = self._values.get("release")
        return typing.cast(typing.Optional["ApplicationContainerManifestRelease"], result)

    @builtins.property
    def runtime(self) -> typing.Optional["ApplicationContainerManifestRuntime"]:
        '''runtime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#runtime ApplicationContainer#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional["ApplicationContainerManifestRuntime"], result)

    @builtins.property
    def shutdown_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#shutdown_time ApplicationContainer#shutdown_time}.'''
        result = self._values.get("shutdown_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def startup_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#startup_time ApplicationContainer#startup_time}.'''
        result = self._values.get("startup_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#type ApplicationContainer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerManifest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerManifestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58c0951be771a697ab163c11f801dad473616c8b243ce7dddc91ad567d489f5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRelease")
    def put_release(
        self,
        *,
        build_attribute: typing.Optional[builtins.str] = None,
        commit: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_attribute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#build ApplicationContainer#build}.
        :param commit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#commit ApplicationContainer#commit}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#version ApplicationContainer#version}.
        '''
        value = ApplicationContainerManifestRelease(
            build_attribute=build_attribute, commit=commit, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putRelease", [value]))

    @jsii.member(jsii_name="putRuntime")
    def put_runtime(self, *, major_version: builtins.str) -> None:
        '''
        :param major_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#major_version ApplicationContainer#major_version}.
        '''
        value = ApplicationContainerManifestRuntime(major_version=major_version)

        return typing.cast(None, jsii.invoke(self, "putRuntime", [value]))

    @jsii.member(jsii_name="resetClustered")
    def reset_clustered(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClustered", []))

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetHealthCheckEndpoint")
    def reset_health_check_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckEndpoint", []))

    @jsii.member(jsii_name="resetHome")
    def reset_home(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHome", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetNotes")
    def reset_notes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotes", []))

    @jsii.member(jsii_name="resetRelease")
    def reset_release(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelease", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetShutdownTime")
    def reset_shutdown_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShutdownTime", []))

    @jsii.member(jsii_name="resetStartupTime")
    def reset_startup_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartupTime", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="release")
    def release(self) -> "ApplicationContainerManifestReleaseOutputReference":
        return typing.cast("ApplicationContainerManifestReleaseOutputReference", jsii.get(self, "release"))

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> "ApplicationContainerManifestRuntimeOutputReference":
        return typing.cast("ApplicationContainerManifestRuntimeOutputReference", jsii.get(self, "runtime"))

    @builtins.property
    @jsii.member(jsii_name="clusteredInput")
    def clustered_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "clusteredInput"))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckEndpointInput")
    def health_check_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="homeInput")
    def home_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="notesInput")
    def notes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notesInput"))

    @builtins.property
    @jsii.member(jsii_name="releaseInput")
    def release_input(self) -> typing.Optional["ApplicationContainerManifestRelease"]:
        return typing.cast(typing.Optional["ApplicationContainerManifestRelease"], jsii.get(self, "releaseInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional["ApplicationContainerManifestRuntime"]:
        return typing.cast(typing.Optional["ApplicationContainerManifestRuntime"], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="shutdownTimeInput")
    def shutdown_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shutdownTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startupTimeInput")
    def startup_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startupTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="clustered")
    def clustered(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "clustered"))

    @clustered.setter
    def clustered(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47ed7278d506cf693d485fea7b9bf1a7f1d8a71b8472d0332b848e49649fc53a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clustered", value)

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "command"))

    @command.setter
    def command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85591363176354dab05bd3626862d5aff2a1c1564fd9b036f48a68b44d68bb86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckEndpoint")
    def health_check_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckEndpoint"))

    @health_check_endpoint.setter
    def health_check_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__176758f2506ab5a6564f8bbf733966a09e1b9af644d243c9793dbd9c0e7ec49b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="home")
    def home(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "home"))

    @home.setter
    def home(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1bff02ded12a794ade8323e198329096c478870e22f46ac82f1a537b79fb91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "home", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c121fdef497d6664513e65ed926ca12f2bf93c3b59df529088d6754ce4110481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="notes")
    def notes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notes"))

    @notes.setter
    def notes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a7b322708a5e3b5426eb37991c6ddf7e72253a49da1dc3ab7f9a79307f2918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notes", value)

    @builtins.property
    @jsii.member(jsii_name="shutdownTime")
    def shutdown_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shutdownTime"))

    @shutdown_time.setter
    def shutdown_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8799e4379802ddf703fbdde227c72a0effe0aa490077d66a1d535297e2b949a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shutdownTime", value)

    @builtins.property
    @jsii.member(jsii_name="startupTime")
    def startup_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startupTime"))

    @startup_time.setter
    def startup_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f400e50570b1b6801acd10e4a9e56fea83b49b5f5ee7fcec5ee6b4a398a95f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startupTime", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0b5cc522f0e772446af96280645cfea06ed3055bb1071052145a868ea5300a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationContainerManifest]:
        return typing.cast(typing.Optional[ApplicationContainerManifest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationContainerManifest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed5d60e7a2449a03df540f4df46f9feccb156c505b7c244c7417f319b249b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifestRelease",
    jsii_struct_bases=[],
    name_mapping={
        "build_attribute": "buildAttribute",
        "commit": "commit",
        "version": "version",
    },
)
class ApplicationContainerManifestRelease:
    def __init__(
        self,
        *,
        build_attribute: typing.Optional[builtins.str] = None,
        commit: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param build_attribute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#build ApplicationContainer#build}.
        :param commit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#commit ApplicationContainer#commit}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#version ApplicationContainer#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45f08cef1a70ac43474f448a57959eef1279d4e481d60eb22d983510a3f99119)
            check_type(argname="argument build_attribute", value=build_attribute, expected_type=type_hints["build_attribute"])
            check_type(argname="argument commit", value=commit, expected_type=type_hints["commit"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if build_attribute is not None:
            self._values["build_attribute"] = build_attribute
        if commit is not None:
            self._values["commit"] = commit
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def build_attribute(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#build ApplicationContainer#build}.'''
        result = self._values.get("build_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#commit ApplicationContainer#commit}.'''
        result = self._values.get("commit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#version ApplicationContainer#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerManifestRelease(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerManifestReleaseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifestReleaseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd0cc88fe68a302b35e3cacf2a977480ad0e26e17c525bd66660c426212f24d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuildAttribute")
    def reset_build_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildAttribute", []))

    @jsii.member(jsii_name="resetCommit")
    def reset_commit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommit", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="buildAttributeInput")
    def build_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="commitInput")
    def commit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="buildAttribute")
    def build_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildAttribute"))

    @build_attribute.setter
    def build_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a869ebce83613e7e2f8755ca9216b027539db7a079787c15f543f0502b2699fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="commit")
    def commit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commit"))

    @commit.setter
    def commit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb771a4fc187cd6866f86f794b1003fe6d8c375c0e4b8231d257930850771b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commit", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f590c94f24ebfa8b0816d28088031508db994d510a9f1370b8fb232d5b8c0f7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationContainerManifestRelease]:
        return typing.cast(typing.Optional[ApplicationContainerManifestRelease], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationContainerManifestRelease],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ab7c1c0ff988f5972c8a184ae87c1eb828e876192c833ed01671253d33ed3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifestRuntime",
    jsii_struct_bases=[],
    name_mapping={"major_version": "majorVersion"},
)
class ApplicationContainerManifestRuntime:
    def __init__(self, *, major_version: builtins.str) -> None:
        '''
        :param major_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#major_version ApplicationContainer#major_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d6df99e55f3f459c6709b5f67cfaa024d75bd1fb9d51cfae4977bddba1a2ea9)
            check_type(argname="argument major_version", value=major_version, expected_type=type_hints["major_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "major_version": major_version,
        }

    @builtins.property
    def major_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#major_version ApplicationContainer#major_version}.'''
        result = self._values.get("major_version")
        assert result is not None, "Required property 'major_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerManifestRuntime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerManifestRuntimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerManifestRuntimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1abec7151b3423cb977a966368a91b91b59da5c613ee4e6ef0f6ece08048f62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="majorVersionInput")
    def major_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "majorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="majorVersion")
    def major_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "majorVersion"))

    @major_version.setter
    def major_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c8cf4ea3b49605ef66d012d8ce4005c31645840806e91498c297d3810cc231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "majorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApplicationContainerManifestRuntime]:
        return typing.cast(typing.Optional[ApplicationContainerManifestRuntime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApplicationContainerManifestRuntime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc983d8863b7b0fb85fc72bb919e6bb3a61898db7333527e7c9de74094a3387a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class ApplicationContainerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#create ApplicationContainer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#delete ApplicationContainer#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aabd76fccaf49db45dfbbda0f2d6f39144d1c4fd5448fa03242223fc30f7c62)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#create ApplicationContainer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas/r/application_container#delete ApplicationContainer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationContainerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationContainerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.applicationContainer.ApplicationContainerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__df33ce3f7f6eacdb03075a99c1b7d6b50a0252689cad0f0443a732e2f15a188c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f1e6eaac42da6492db526e95fdb2e532873dfa4958e9def070f6d4e3f9d5e93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bdc87ad2c0227f980d9037f84c40c3f517918d15eac096782b4877531e88f11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationContainerTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationContainerTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationContainerTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a7c772cfd514f868df916d842bdd6528073ca1cbeb2c176f02f0f99a0fe17c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApplicationContainer",
    "ApplicationContainerConfig",
    "ApplicationContainerDeployment",
    "ApplicationContainerDeploymentOutputReference",
    "ApplicationContainerDeploymentServices",
    "ApplicationContainerDeploymentServicesList",
    "ApplicationContainerDeploymentServicesOutputReference",
    "ApplicationContainerManifest",
    "ApplicationContainerManifestOutputReference",
    "ApplicationContainerManifestRelease",
    "ApplicationContainerManifestReleaseOutputReference",
    "ApplicationContainerManifestRuntime",
    "ApplicationContainerManifestRuntimeOutputReference",
    "ApplicationContainerTimeouts",
    "ApplicationContainerTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__c8361d7d5da8c26544198a52dd056c9c0e1871c85215c731a34d9456e979960b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    archive_url: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    availability_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
    deployment: typing.Optional[typing.Union[ApplicationContainerDeployment, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_file: typing.Optional[builtins.str] = None,
    git_password: typing.Optional[builtins.str] = None,
    git_repository: typing.Optional[builtins.str] = None,
    git_username: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    manifest: typing.Optional[typing.Union[ApplicationContainerManifest, typing.Dict[builtins.str, typing.Any]]] = None,
    manifest_file: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[builtins.str] = None,
    subscription_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ApplicationContainerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__1a7e3e6cfff17be3a95a0e220b56826dfa7ba0008de387963920a7ce7c916636(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed685120e8254992de4da27d7169339e39fb90490129d02dae3977c337a1a571(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770ce04f014b7ae0f8f15a19a16d776ee5268904da9847eebcbd8d687c497ff1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7468b8bcc7746d838cc87555c91c325b1ef2c19ae4117e664998ccb89ea0e86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673c3d3f239e8ff00da0524642e04dabe74eca61f3f863a4fb754bd41baa6cd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38f8a01f6164cf10ddfebc394684cc580f664e72fdbd72a98239cb6ec0385dbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0601a4031a50a13c68af0bd41cee1174420b97afde3237e200e69e8e3612d46e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e250752444d35fb4bf04d7f42c114d9e7ebdefc0ce0b515ffd5d4a03935bf6d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d9497108b41cf2a95b55debbe3c79b8689e457215d026099ce628a631ec2ae(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0daebe302341e3bab3f16baf80af8af2aac2cc2b05f49f4b3313685bb05b923(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e8ec03bf55d69b6b577dad69a26edbeca1b55822befeb448a2463cc829952f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa47a6b6208440248e08420c497cc4e460bebaa1a8d73fefb5cb328bef426cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1daf016f8e402ceefeed903c63939d94b4b022b43f55c73e89989291bb7e2451(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0851ac6a6a471d0acf9c4fad6acf312d2e7e699c2d314d6dee2f1e5c86d2611(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e62643a5f9557c375985986984533ef3dd6ca1c74b3f58d55d0c890adc4c394(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6444ccc47a9ae0a153832d6cbdf8c1c80c2f0fcb500309d9f2e4e898f2e2ae6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afca485a7a0bc43616131ca6f0db7c4a6880caffece92009cc455b4beaf0ebe2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03167c97a957cd9e6ec70c6ad7b64161d6ac14ddcb58e5a196f18822399af9a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    archive_url: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    availability_domain: typing.Optional[typing.Sequence[builtins.str]] = None,
    deployment: typing.Optional[typing.Union[ApplicationContainerDeployment, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_file: typing.Optional[builtins.str] = None,
    git_password: typing.Optional[builtins.str] = None,
    git_repository: typing.Optional[builtins.str] = None,
    git_username: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    load_balancer_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    manifest: typing.Optional[typing.Union[ApplicationContainerManifest, typing.Dict[builtins.str, typing.Any]]] = None,
    manifest_file: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    notification_email: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[builtins.str] = None,
    subscription_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ApplicationContainerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f022e172ef6646c4a6d26147ee33c778767468b96dfa2f3e95d34b953418c8ff(
    *,
    environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    instances: typing.Optional[jsii.Number] = None,
    java_system_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    secure_environment: typing.Optional[typing.Sequence[builtins.str]] = None,
    services: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationContainerDeploymentServices, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9978dbb3703a7381253eaa51f1f8ecbfd863a322c6a434e51c33ad4b79f4bcae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006a40252225194dec375d988b36a3261b92445aea97983d347daa5941ec4805(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ApplicationContainerDeploymentServices, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe621c4a5ea06b56d950482ff9f1f1930bc9d997559a38378e30d3983ebeb85(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1436c47506d790fd6390b7341fe688a3c4f7d5110595a9959b8f3df5cc96a851(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed8f18a913e7b9e01ba12669900566c2890012b34264aff694b87b7e0b8bd209(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f83c85f2f76e3e16114c6654ceb7b31c1af99cca272324d28adceec3a970ee0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a2c36f1ac08d995fb64570ce9de4674c80709b1a6efafd96e10b70d02c36fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1809cf40ff9d594a668a5bd005a5dddd321cb78215c88f9f35166205538189a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdcddc9d3537a1b1f84e01b49d4b288a359278441cf17781d8e6d95a9de95340(
    value: typing.Optional[ApplicationContainerDeployment],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebdc9f18e191c4da461cd8d0fff12ce7c1b1826bb781cc50989e0c73ed060bb(
    *,
    identifier: builtins.str,
    name: builtins.str,
    password: builtins.str,
    type: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a20727afa73251d5a253861e1fbe0fa83a0b4c7a7938fee79aa7f9aebfe6ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467abd5a0fa5c6bdf7ba46fceb9ae8bb372479981e1057aae78cc9ac547ed1ed(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1054c0462fe8b46443e60faa3628480174d9bcb21619ec7823a8757ce4a83de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87b8a2c1df02d905232cbdbdf0b75e1374774bbc464b6620f674836abb9c8601(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c741dc6cf46e93fdc10c46bac79a60d90da20ca9bd5914c9c6b1634c513840(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a64bd50811166f705533152431206f7473213bdece92dde7dd728c3e349ab52(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ApplicationContainerDeploymentServices]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1089d0b019465c8f01ff23957a4aa52d4a8791f8e3fc173b0c4ae023273dc58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61fc109d0a8c5fe897f8c5cd4840b2724dc4d912ebc4e5a2083dd94f872023a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62e4abf63fe9ebb449885dc3b5faa19f742d14e903abb76265f99da21fd895ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4cf43ba9520af37982a325bde7b0a0d924b5c04d71fa4de0447fa2786c97e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05dc7a34ba91f24a3c40f7ba099cfe19bd3bbf5536e28936e3dbdfec7ecfae02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef26fdc92ec1fcedf5d2475e330265ce7fe0a73a89bd5e0e5a2735ed24d74a39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a4ebcf3c42e6a48d303e99bd39db04b9b3178c5971aa19aeec428a1c058c69(
    value: typing.Optional[typing.Union[ApplicationContainerDeploymentServices, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21cef81d12bc88c6137fadc5117eb2a2494a4c68761bbd7a98e0e5cb61ec6fee(
    *,
    clustered: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    command: typing.Optional[builtins.str] = None,
    health_check_endpoint: typing.Optional[builtins.str] = None,
    home: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    notes: typing.Optional[builtins.str] = None,
    release: typing.Optional[typing.Union[ApplicationContainerManifestRelease, typing.Dict[builtins.str, typing.Any]]] = None,
    runtime: typing.Optional[typing.Union[ApplicationContainerManifestRuntime, typing.Dict[builtins.str, typing.Any]]] = None,
    shutdown_time: typing.Optional[jsii.Number] = None,
    startup_time: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58c0951be771a697ab163c11f801dad473616c8b243ce7dddc91ad567d489f5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47ed7278d506cf693d485fea7b9bf1a7f1d8a71b8472d0332b848e49649fc53a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85591363176354dab05bd3626862d5aff2a1c1564fd9b036f48a68b44d68bb86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__176758f2506ab5a6564f8bbf733966a09e1b9af644d243c9793dbd9c0e7ec49b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1bff02ded12a794ade8323e198329096c478870e22f46ac82f1a537b79fb91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c121fdef497d6664513e65ed926ca12f2bf93c3b59df529088d6754ce4110481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a7b322708a5e3b5426eb37991c6ddf7e72253a49da1dc3ab7f9a79307f2918(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8799e4379802ddf703fbdde227c72a0effe0aa490077d66a1d535297e2b949a0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f400e50570b1b6801acd10e4a9e56fea83b49b5f5ee7fcec5ee6b4a398a95f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0b5cc522f0e772446af96280645cfea06ed3055bb1071052145a868ea5300a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed5d60e7a2449a03df540f4df46f9feccb156c505b7c244c7417f319b249b74(
    value: typing.Optional[ApplicationContainerManifest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45f08cef1a70ac43474f448a57959eef1279d4e481d60eb22d983510a3f99119(
    *,
    build_attribute: typing.Optional[builtins.str] = None,
    commit: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0cc88fe68a302b35e3cacf2a977480ad0e26e17c525bd66660c426212f24d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a869ebce83613e7e2f8755ca9216b027539db7a079787c15f543f0502b2699fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb771a4fc187cd6866f86f794b1003fe6d8c375c0e4b8231d257930850771b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f590c94f24ebfa8b0816d28088031508db994d510a9f1370b8fb232d5b8c0f7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ab7c1c0ff988f5972c8a184ae87c1eb828e876192c833ed01671253d33ed3b(
    value: typing.Optional[ApplicationContainerManifestRelease],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6df99e55f3f459c6709b5f67cfaa024d75bd1fb9d51cfae4977bddba1a2ea9(
    *,
    major_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1abec7151b3423cb977a966368a91b91b59da5c613ee4e6ef0f6ece08048f62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c8cf4ea3b49605ef66d012d8ce4005c31645840806e91498c297d3810cc231(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc983d8863b7b0fb85fc72bb919e6bb3a61898db7333527e7c9de74094a3387a(
    value: typing.Optional[ApplicationContainerManifestRuntime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aabd76fccaf49db45dfbbda0f2d6f39144d1c4fd5448fa03242223fc30f7c62(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df33ce3f7f6eacdb03075a99c1b7d6b50a0252689cad0f0443a732e2f15a188c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f1e6eaac42da6492db526e95fdb2e532873dfa4958e9def070f6d4e3f9d5e93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bdc87ad2c0227f980d9037f84c40c3f517918d15eac096782b4877531e88f11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a7c772cfd514f868df916d842bdd6528073ca1cbeb2c176f02f0f99a0fe17c(
    value: typing.Optional[typing.Union[ApplicationContainerTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
