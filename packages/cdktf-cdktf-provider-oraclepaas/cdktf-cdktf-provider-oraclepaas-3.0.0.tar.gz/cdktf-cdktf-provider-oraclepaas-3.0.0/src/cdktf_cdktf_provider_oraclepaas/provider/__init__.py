'''
# `provider`

Refer to the Terraform Registory for docs: [`oraclepaas`](https://www.terraform.io/docs/providers/oraclepaas).
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


class OraclepaasProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-oraclepaas.provider.OraclepaasProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/oraclepaas oraclepaas}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identity_domain: builtins.str,
        password: builtins.str,
        user: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        application_endpoint: typing.Optional[builtins.str] = None,
        database_endpoint: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        java_endpoint: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        mysql_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/oraclepaas oraclepaas} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_domain: The OPAAS identity domain for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#identity_domain OraclepaasProvider#identity_domain}
        :param password: The user password for OPAAS API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#password OraclepaasProvider#password}
        :param user: The user name for OPAAS API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#user OraclepaasProvider#user}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#alias OraclepaasProvider#alias}
        :param application_endpoint: The HTTP endpoint for the Oracle Application operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#application_endpoint OraclepaasProvider#application_endpoint}
        :param database_endpoint: The HTTP endpoint for Oracle Database operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#database_endpoint OraclepaasProvider#database_endpoint}
        :param insecure: Skip TLS Verification for self-signed certificates. Should only be used if absolutely required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#insecure OraclepaasProvider#insecure}
        :param java_endpoint: The HTTP endpoint for Oracle Java operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#java_endpoint OraclepaasProvider#java_endpoint}
        :param max_retries: Maximum number retries to wait for a successful response when operating on resources within OPAAS (defaults to 1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#max_retries OraclepaasProvider#max_retries}
        :param mysql_endpoint: The HTTP endpoint for Oracle MySQL operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#mysql_endpoint OraclepaasProvider#mysql_endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd1e7e516dd8bd0cd036abeaf45b9cabb3becd25c14cfba0ba8459e9673acdc7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = OraclepaasProviderConfig(
            identity_domain=identity_domain,
            password=password,
            user=user,
            alias=alias,
            application_endpoint=application_endpoint,
            database_endpoint=database_endpoint,
            insecure=insecure,
            java_endpoint=java_endpoint,
            max_retries=max_retries,
            mysql_endpoint=mysql_endpoint,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApplicationEndpoint")
    def reset_application_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationEndpoint", []))

    @jsii.member(jsii_name="resetDatabaseEndpoint")
    def reset_database_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseEndpoint", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetJavaEndpoint")
    def reset_java_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJavaEndpoint", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @jsii.member(jsii_name="resetMysqlEndpoint")
    def reset_mysql_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMysqlEndpoint", []))

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
    @jsii.member(jsii_name="applicationEndpointInput")
    def application_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseEndpointInput")
    def database_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="identityDomainInput")
    def identity_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="javaEndpointInput")
    def java_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="mysqlEndpointInput")
    def mysql_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398bca405f31f1d0c10ecea7b6c8f301838a59ce5b0c16d85c021b1a6ac75b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="applicationEndpoint")
    def application_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationEndpoint"))

    @application_endpoint.setter
    def application_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b087a628719349999822a64fbae4f3dd82d9a7077f01a7f251ca389b7da0a297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="databaseEndpoint")
    def database_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseEndpoint"))

    @database_endpoint.setter
    def database_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb7a231ffc48b4e53e45cad5ec408062d91c0dba640347d03e10c26dcba3b15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="identityDomain")
    def identity_domain(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityDomain"))

    @identity_domain.setter
    def identity_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8b9ecc4979a0ea4f9a68c05f3d1834bb45d69d4e65668230628a7cdfb3590a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d5abc81d7f311cfcde784d951d4ebd4f685db3ccfd6c4427a8740ff5a6d59c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="javaEndpoint")
    def java_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "javaEndpoint"))

    @java_endpoint.setter
    def java_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def06ad63aef6b5cc5c5496f7d6929b5a3496bea92de55600e6a3379a7337209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "javaEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537bc67479cf9418a38a155a045dea5b43adf79839868defe991ce8d66430fca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="mysqlEndpoint")
    def mysql_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mysqlEndpoint"))

    @mysql_endpoint.setter
    def mysql_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90bd1f3f30c8841813e7438d33d1773945e004797d748435077edbe374e6028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mysqlEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74cdc16bf10a807153af86b32e40a913a210761b3717a7f525a1b25c0dd201a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "user"))

    @user.setter
    def user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf562fe7de0116ea4c1bfc3c70745f82c35815b18a3f6e9df8a40ccc0a14df1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-oraclepaas.provider.OraclepaasProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "identity_domain": "identityDomain",
        "password": "password",
        "user": "user",
        "alias": "alias",
        "application_endpoint": "applicationEndpoint",
        "database_endpoint": "databaseEndpoint",
        "insecure": "insecure",
        "java_endpoint": "javaEndpoint",
        "max_retries": "maxRetries",
        "mysql_endpoint": "mysqlEndpoint",
    },
)
class OraclepaasProviderConfig:
    def __init__(
        self,
        *,
        identity_domain: builtins.str,
        password: builtins.str,
        user: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        application_endpoint: typing.Optional[builtins.str] = None,
        database_endpoint: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        java_endpoint: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        mysql_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identity_domain: The OPAAS identity domain for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#identity_domain OraclepaasProvider#identity_domain}
        :param password: The user password for OPAAS API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#password OraclepaasProvider#password}
        :param user: The user name for OPAAS API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#user OraclepaasProvider#user}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#alias OraclepaasProvider#alias}
        :param application_endpoint: The HTTP endpoint for the Oracle Application operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#application_endpoint OraclepaasProvider#application_endpoint}
        :param database_endpoint: The HTTP endpoint for Oracle Database operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#database_endpoint OraclepaasProvider#database_endpoint}
        :param insecure: Skip TLS Verification for self-signed certificates. Should only be used if absolutely required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#insecure OraclepaasProvider#insecure}
        :param java_endpoint: The HTTP endpoint for Oracle Java operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#java_endpoint OraclepaasProvider#java_endpoint}
        :param max_retries: Maximum number retries to wait for a successful response when operating on resources within OPAAS (defaults to 1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#max_retries OraclepaasProvider#max_retries}
        :param mysql_endpoint: The HTTP endpoint for Oracle MySQL operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#mysql_endpoint OraclepaasProvider#mysql_endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95c82febe1fdc8d74ce8b49bd65d4de04b46a5de7261b61a7ab8727a76712c0)
            check_type(argname="argument identity_domain", value=identity_domain, expected_type=type_hints["identity_domain"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument application_endpoint", value=application_endpoint, expected_type=type_hints["application_endpoint"])
            check_type(argname="argument database_endpoint", value=database_endpoint, expected_type=type_hints["database_endpoint"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument java_endpoint", value=java_endpoint, expected_type=type_hints["java_endpoint"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument mysql_endpoint", value=mysql_endpoint, expected_type=type_hints["mysql_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_domain": identity_domain,
            "password": password,
            "user": user,
        }
        if alias is not None:
            self._values["alias"] = alias
        if application_endpoint is not None:
            self._values["application_endpoint"] = application_endpoint
        if database_endpoint is not None:
            self._values["database_endpoint"] = database_endpoint
        if insecure is not None:
            self._values["insecure"] = insecure
        if java_endpoint is not None:
            self._values["java_endpoint"] = java_endpoint
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if mysql_endpoint is not None:
            self._values["mysql_endpoint"] = mysql_endpoint

    @builtins.property
    def identity_domain(self) -> builtins.str:
        '''The OPAAS identity domain for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#identity_domain OraclepaasProvider#identity_domain}
        '''
        result = self._values.get("identity_domain")
        assert result is not None, "Required property 'identity_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The user password for OPAAS API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#password OraclepaasProvider#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''The user name for OPAAS API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#user OraclepaasProvider#user}
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#alias OraclepaasProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for the Oracle Application operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#application_endpoint OraclepaasProvider#application_endpoint}
        '''
        result = self._values.get("application_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for Oracle Database operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#database_endpoint OraclepaasProvider#database_endpoint}
        '''
        result = self._values.get("database_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip TLS Verification for self-signed certificates. Should only be used if absolutely required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#insecure OraclepaasProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def java_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for Oracle Java operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#java_endpoint OraclepaasProvider#java_endpoint}
        '''
        result = self._values.get("java_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''Maximum number retries to wait for a successful response when operating on resources within OPAAS (defaults to 1).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#max_retries OraclepaasProvider#max_retries}
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mysql_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for Oracle MySQL operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/oraclepaas#mysql_endpoint OraclepaasProvider#mysql_endpoint}
        '''
        result = self._values.get("mysql_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OraclepaasProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OraclepaasProvider",
    "OraclepaasProviderConfig",
]

publication.publish()

def _typecheckingstub__cd1e7e516dd8bd0cd036abeaf45b9cabb3becd25c14cfba0ba8459e9673acdc7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_domain: builtins.str,
    password: builtins.str,
    user: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    application_endpoint: typing.Optional[builtins.str] = None,
    database_endpoint: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    java_endpoint: typing.Optional[builtins.str] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    mysql_endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398bca405f31f1d0c10ecea7b6c8f301838a59ce5b0c16d85c021b1a6ac75b1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b087a628719349999822a64fbae4f3dd82d9a7077f01a7f251ca389b7da0a297(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb7a231ffc48b4e53e45cad5ec408062d91c0dba640347d03e10c26dcba3b15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8b9ecc4979a0ea4f9a68c05f3d1834bb45d69d4e65668230628a7cdfb3590a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d5abc81d7f311cfcde784d951d4ebd4f685db3ccfd6c4427a8740ff5a6d59c(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def06ad63aef6b5cc5c5496f7d6929b5a3496bea92de55600e6a3379a7337209(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537bc67479cf9418a38a155a045dea5b43adf79839868defe991ce8d66430fca(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90bd1f3f30c8841813e7438d33d1773945e004797d748435077edbe374e6028(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74cdc16bf10a807153af86b32e40a913a210761b3717a7f525a1b25c0dd201a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf562fe7de0116ea4c1bfc3c70745f82c35815b18a3f6e9df8a40ccc0a14df1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a95c82febe1fdc8d74ce8b49bd65d4de04b46a5de7261b61a7ab8727a76712c0(
    *,
    identity_domain: builtins.str,
    password: builtins.str,
    user: builtins.str,
    alias: typing.Optional[builtins.str] = None,
    application_endpoint: typing.Optional[builtins.str] = None,
    database_endpoint: typing.Optional[builtins.str] = None,
    insecure: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    java_endpoint: typing.Optional[builtins.str] = None,
    max_retries: typing.Optional[jsii.Number] = None,
    mysql_endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
