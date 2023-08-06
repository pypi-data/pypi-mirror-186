'''
# `upcloud_managed_database_user`

Refer to the Terraform Registory for docs: [`upcloud_managed_database_user`](https://www.terraform.io/docs/providers/upcloud/r/managed_database_user).
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


class ManagedDatabaseUser(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUser",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user upcloud_managed_database_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        service: builtins.str,
        username: builtins.str,
        authentication: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        pg_access_control: typing.Optional[typing.Union["ManagedDatabaseUserPgAccessControl", typing.Dict[builtins.str, typing.Any]]] = None,
        redis_access_control: typing.Optional[typing.Union["ManagedDatabaseUserRedisAccessControl", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user upcloud_managed_database_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service: Service's UUID for which this user belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#service ManagedDatabaseUser#service}
        :param username: Name of the database user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#username ManagedDatabaseUser#username}
        :param authentication: MySQL only, authentication type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#authentication ManagedDatabaseUser#authentication}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#id ManagedDatabaseUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for the database user. Defaults to a random value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#password ManagedDatabaseUser#password}
        :param pg_access_control: pg_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#pg_access_control ManagedDatabaseUser#pg_access_control}
        :param redis_access_control: redis_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#redis_access_control ManagedDatabaseUser#redis_access_control}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284705db217200be03c68231d6206d89ab6b5c942fa6aa0a91e5f854d83bc8b6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedDatabaseUserConfig(
            service=service,
            username=username,
            authentication=authentication,
            id=id,
            password=password,
            pg_access_control=pg_access_control,
            redis_access_control=redis_access_control,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPgAccessControl")
    def put_pg_access_control(
        self,
        *,
        allow_replication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_replication: Grant replication privilege. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#allow_replication ManagedDatabaseUser#allow_replication}
        '''
        value = ManagedDatabaseUserPgAccessControl(allow_replication=allow_replication)

        return typing.cast(None, jsii.invoke(self, "putPgAccessControl", [value]))

    @jsii.member(jsii_name="putRedisAccessControl")
    def put_redis_access_control(
        self,
        *,
        categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param categories: Set access control to all commands in specified categories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#categories ManagedDatabaseUser#categories}
        :param channels: Set access control to Pub/Sub channels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#channels ManagedDatabaseUser#channels}
        :param commands: Set access control to commands. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#commands ManagedDatabaseUser#commands}
        :param keys: Set access control to keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#keys ManagedDatabaseUser#keys}
        '''
        value = ManagedDatabaseUserRedisAccessControl(
            categories=categories, channels=channels, commands=commands, keys=keys
        )

        return typing.cast(None, jsii.invoke(self, "putRedisAccessControl", [value]))

    @jsii.member(jsii_name="resetAuthentication")
    def reset_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthentication", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPgAccessControl")
    def reset_pg_access_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPgAccessControl", []))

    @jsii.member(jsii_name="resetRedisAccessControl")
    def reset_redis_access_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedisAccessControl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="pgAccessControl")
    def pg_access_control(self) -> "ManagedDatabaseUserPgAccessControlOutputReference":
        return typing.cast("ManagedDatabaseUserPgAccessControlOutputReference", jsii.get(self, "pgAccessControl"))

    @builtins.property
    @jsii.member(jsii_name="redisAccessControl")
    def redis_access_control(
        self,
    ) -> "ManagedDatabaseUserRedisAccessControlOutputReference":
        return typing.cast("ManagedDatabaseUserRedisAccessControlOutputReference", jsii.get(self, "redisAccessControl"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="pgAccessControlInput")
    def pg_access_control_input(
        self,
    ) -> typing.Optional["ManagedDatabaseUserPgAccessControl"]:
        return typing.cast(typing.Optional["ManagedDatabaseUserPgAccessControl"], jsii.get(self, "pgAccessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="redisAccessControlInput")
    def redis_access_control_input(
        self,
    ) -> typing.Optional["ManagedDatabaseUserRedisAccessControl"]:
        return typing.cast(typing.Optional["ManagedDatabaseUserRedisAccessControl"], jsii.get(self, "redisAccessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authentication"))

    @authentication.setter
    def authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59524d6ec28e1e91e2660a7a825733751c8f6ccf1b6b7ace9eacc505d796901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authentication", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__279d5d1ce136b75e6c2fe00e42d73f303c19db8b2a872db680552e387797902c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0bc67b2dd690e0235e63664dc77e9295886fea48c10eba2f30b039f0b5f455b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb1244dc41c138e20749cc2e50d2739b25a0c3a573a7655784fe3a48e8b7c2a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9047a597e672fcf3a034119577335b53b918a8ad3b654540e8d13c08a894eeb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "service": "service",
        "username": "username",
        "authentication": "authentication",
        "id": "id",
        "password": "password",
        "pg_access_control": "pgAccessControl",
        "redis_access_control": "redisAccessControl",
    },
)
class ManagedDatabaseUserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        service: builtins.str,
        username: builtins.str,
        authentication: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        pg_access_control: typing.Optional[typing.Union["ManagedDatabaseUserPgAccessControl", typing.Dict[builtins.str, typing.Any]]] = None,
        redis_access_control: typing.Optional[typing.Union["ManagedDatabaseUserRedisAccessControl", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param service: Service's UUID for which this user belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#service ManagedDatabaseUser#service}
        :param username: Name of the database user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#username ManagedDatabaseUser#username}
        :param authentication: MySQL only, authentication type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#authentication ManagedDatabaseUser#authentication}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#id ManagedDatabaseUser#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for the database user. Defaults to a random value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#password ManagedDatabaseUser#password}
        :param pg_access_control: pg_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#pg_access_control ManagedDatabaseUser#pg_access_control}
        :param redis_access_control: redis_access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#redis_access_control ManagedDatabaseUser#redis_access_control}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(pg_access_control, dict):
            pg_access_control = ManagedDatabaseUserPgAccessControl(**pg_access_control)
        if isinstance(redis_access_control, dict):
            redis_access_control = ManagedDatabaseUserRedisAccessControl(**redis_access_control)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a7f5c785cc0e125e8ded59bfd094c26884e099fe8129734900f6faab61a108)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument pg_access_control", value=pg_access_control, expected_type=type_hints["pg_access_control"])
            check_type(argname="argument redis_access_control", value=redis_access_control, expected_type=type_hints["redis_access_control"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service": service,
            "username": username,
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
        if authentication is not None:
            self._values["authentication"] = authentication
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if pg_access_control is not None:
            self._values["pg_access_control"] = pg_access_control
        if redis_access_control is not None:
            self._values["redis_access_control"] = redis_access_control

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
    def service(self) -> builtins.str:
        '''Service's UUID for which this user belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#service ManagedDatabaseUser#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Name of the database user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#username ManagedDatabaseUser#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication(self) -> typing.Optional[builtins.str]:
        '''MySQL only, authentication type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#authentication ManagedDatabaseUser#authentication}
        '''
        result = self._values.get("authentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#id ManagedDatabaseUser#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for the database user. Defaults to a random value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#password ManagedDatabaseUser#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pg_access_control(
        self,
    ) -> typing.Optional["ManagedDatabaseUserPgAccessControl"]:
        '''pg_access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#pg_access_control ManagedDatabaseUser#pg_access_control}
        '''
        result = self._values.get("pg_access_control")
        return typing.cast(typing.Optional["ManagedDatabaseUserPgAccessControl"], result)

    @builtins.property
    def redis_access_control(
        self,
    ) -> typing.Optional["ManagedDatabaseUserRedisAccessControl"]:
        '''redis_access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#redis_access_control ManagedDatabaseUser#redis_access_control}
        '''
        result = self._values.get("redis_access_control")
        return typing.cast(typing.Optional["ManagedDatabaseUserRedisAccessControl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUserPgAccessControl",
    jsii_struct_bases=[],
    name_mapping={"allow_replication": "allowReplication"},
)
class ManagedDatabaseUserPgAccessControl:
    def __init__(
        self,
        *,
        allow_replication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param allow_replication: Grant replication privilege. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#allow_replication ManagedDatabaseUser#allow_replication}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34e6b56dbd319319ed29790d55c8592357d86f9b7c8e8c14a5c4d70a6787a4f)
            check_type(argname="argument allow_replication", value=allow_replication, expected_type=type_hints["allow_replication"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_replication is not None:
            self._values["allow_replication"] = allow_replication

    @builtins.property
    def allow_replication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Grant replication privilege.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#allow_replication ManagedDatabaseUser#allow_replication}
        '''
        result = self._values.get("allow_replication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseUserPgAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabaseUserPgAccessControlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUserPgAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85fcf89643ce491d5750a1564e2b960c17139df7539f861e2865332a05483b5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowReplication")
    def reset_allow_replication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowReplication", []))

    @builtins.property
    @jsii.member(jsii_name="allowReplicationInput")
    def allow_replication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowReplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="allowReplication")
    def allow_replication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowReplication"))

    @allow_replication.setter
    def allow_replication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64766b07261271a83f0b99c9b5994c07b319be03b24ec0486adc7ddcb458552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReplication", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabaseUserPgAccessControl]:
        return typing.cast(typing.Optional[ManagedDatabaseUserPgAccessControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseUserPgAccessControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef37ebe78b06916a552ac2271f6287ba8f91f8248730c96c7d6d23c8258132c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUserRedisAccessControl",
    jsii_struct_bases=[],
    name_mapping={
        "categories": "categories",
        "channels": "channels",
        "commands": "commands",
        "keys": "keys",
    },
)
class ManagedDatabaseUserRedisAccessControl:
    def __init__(
        self,
        *,
        categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        commands: typing.Optional[typing.Sequence[builtins.str]] = None,
        keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param categories: Set access control to all commands in specified categories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#categories ManagedDatabaseUser#categories}
        :param channels: Set access control to Pub/Sub channels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#channels ManagedDatabaseUser#channels}
        :param commands: Set access control to commands. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#commands ManagedDatabaseUser#commands}
        :param keys: Set access control to keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#keys ManagedDatabaseUser#keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27204462f8812754fabbce2e4daa3352d018e15b121d6d94fd8c33a5f838827b)
            check_type(argname="argument categories", value=categories, expected_type=type_hints["categories"])
            check_type(argname="argument channels", value=channels, expected_type=type_hints["channels"])
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if categories is not None:
            self._values["categories"] = categories
        if channels is not None:
            self._values["channels"] = channels
        if commands is not None:
            self._values["commands"] = commands
        if keys is not None:
            self._values["keys"] = keys

    @builtins.property
    def categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set access control to all commands in specified categories.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#categories ManagedDatabaseUser#categories}
        '''
        result = self._values.get("categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def channels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set access control to Pub/Sub channels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#channels ManagedDatabaseUser#channels}
        '''
        result = self._values.get("channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def commands(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set access control to commands.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#commands ManagedDatabaseUser#commands}
        '''
        result = self._values.get("commands")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set access control to keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/managed_database_user#keys ManagedDatabaseUser#keys}
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDatabaseUserRedisAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDatabaseUserRedisAccessControlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.managedDatabaseUser.ManagedDatabaseUserRedisAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcba167a39f5e86f09c3bccf00f992717ef7610341786884fb1248dd2fc63013)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCategories")
    def reset_categories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategories", []))

    @jsii.member(jsii_name="resetChannels")
    def reset_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannels", []))

    @jsii.member(jsii_name="resetCommands")
    def reset_commands(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommands", []))

    @jsii.member(jsii_name="resetKeys")
    def reset_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeys", []))

    @builtins.property
    @jsii.member(jsii_name="categoriesInput")
    def categories_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "categoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="channelsInput")
    def channels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "channelsInput"))

    @builtins.property
    @jsii.member(jsii_name="commandsInput")
    def commands_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandsInput"))

    @builtins.property
    @jsii.member(jsii_name="keysInput")
    def keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keysInput"))

    @builtins.property
    @jsii.member(jsii_name="categories")
    def categories(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "categories"))

    @categories.setter
    def categories(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db6bd21eb82626e594a17d964f006f6367c63796a9e1fcf5900809d75d75495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categories", value)

    @builtins.property
    @jsii.member(jsii_name="channels")
    def channels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "channels"))

    @channels.setter
    def channels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8835379e24928fde409b267f4d2324f2f982d9481187765ee87591af7141b3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channels", value)

    @builtins.property
    @jsii.member(jsii_name="commands")
    def commands(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "commands"))

    @commands.setter
    def commands(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea598cedaad8f42680bdfe823440cac795ce1b73a7d8eb3122c1765355bf47cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commands", value)

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @keys.setter
    def keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe3f4c7b7b94e1cef4f758a0146dd6b964648a85bbcb4676d7f99c66ef9069d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDatabaseUserRedisAccessControl]:
        return typing.cast(typing.Optional[ManagedDatabaseUserRedisAccessControl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDatabaseUserRedisAccessControl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__339df3f9580cdaa83ea424d213c30eb13df0c7142e732aa0a5fa3d7a2238d0b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedDatabaseUser",
    "ManagedDatabaseUserConfig",
    "ManagedDatabaseUserPgAccessControl",
    "ManagedDatabaseUserPgAccessControlOutputReference",
    "ManagedDatabaseUserRedisAccessControl",
    "ManagedDatabaseUserRedisAccessControlOutputReference",
]

publication.publish()

def _typecheckingstub__284705db217200be03c68231d6206d89ab6b5c942fa6aa0a91e5f854d83bc8b6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    service: builtins.str,
    username: builtins.str,
    authentication: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    pg_access_control: typing.Optional[typing.Union[ManagedDatabaseUserPgAccessControl, typing.Dict[builtins.str, typing.Any]]] = None,
    redis_access_control: typing.Optional[typing.Union[ManagedDatabaseUserRedisAccessControl, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__b59524d6ec28e1e91e2660a7a825733751c8f6ccf1b6b7ace9eacc505d796901(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__279d5d1ce136b75e6c2fe00e42d73f303c19db8b2a872db680552e387797902c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0bc67b2dd690e0235e63664dc77e9295886fea48c10eba2f30b039f0b5f455b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1244dc41c138e20749cc2e50d2739b25a0c3a573a7655784fe3a48e8b7c2a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9047a597e672fcf3a034119577335b53b918a8ad3b654540e8d13c08a894eeb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a7f5c785cc0e125e8ded59bfd094c26884e099fe8129734900f6faab61a108(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    service: builtins.str,
    username: builtins.str,
    authentication: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    pg_access_control: typing.Optional[typing.Union[ManagedDatabaseUserPgAccessControl, typing.Dict[builtins.str, typing.Any]]] = None,
    redis_access_control: typing.Optional[typing.Union[ManagedDatabaseUserRedisAccessControl, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34e6b56dbd319319ed29790d55c8592357d86f9b7c8e8c14a5c4d70a6787a4f(
    *,
    allow_replication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fcf89643ce491d5750a1564e2b960c17139df7539f861e2865332a05483b5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64766b07261271a83f0b99c9b5994c07b319be03b24ec0486adc7ddcb458552(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef37ebe78b06916a552ac2271f6287ba8f91f8248730c96c7d6d23c8258132c(
    value: typing.Optional[ManagedDatabaseUserPgAccessControl],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27204462f8812754fabbce2e4daa3352d018e15b121d6d94fd8c33a5f838827b(
    *,
    categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    channels: typing.Optional[typing.Sequence[builtins.str]] = None,
    commands: typing.Optional[typing.Sequence[builtins.str]] = None,
    keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcba167a39f5e86f09c3bccf00f992717ef7610341786884fb1248dd2fc63013(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db6bd21eb82626e594a17d964f006f6367c63796a9e1fcf5900809d75d75495(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8835379e24928fde409b267f4d2324f2f982d9481187765ee87591af7141b3b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea598cedaad8f42680bdfe823440cac795ce1b73a7d8eb3122c1765355bf47cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe3f4c7b7b94e1cef4f758a0146dd6b964648a85bbcb4676d7f99c66ef9069d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339df3f9580cdaa83ea424d213c30eb13df0c7142e732aa0a5fa3d7a2238d0b8(
    value: typing.Optional[ManagedDatabaseUserRedisAccessControl],
) -> None:
    """Type checking stubs"""
    pass
