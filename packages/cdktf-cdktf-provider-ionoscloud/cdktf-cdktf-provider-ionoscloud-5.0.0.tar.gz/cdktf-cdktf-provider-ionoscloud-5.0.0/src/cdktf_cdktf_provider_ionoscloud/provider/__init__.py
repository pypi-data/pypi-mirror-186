'''
# `provider`

Refer to the Terraform Registory for docs: [`ionoscloud`](https://www.terraform.io/docs/providers/ionoscloud).
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


class IonoscloudProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.provider.IonoscloudProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud ionoscloud}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud ionoscloud} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#alias IonoscloudProvider#alias}
        :param endpoint: IonosCloud REST API URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#endpoint IonoscloudProvider#endpoint}
        :param password: IonosCloud password for API operations. If token is provided, token is preferred. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#password IonoscloudProvider#password}
        :param retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#retries IonoscloudProvider#retries}.
        :param token: IonosCloud bearer token for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#token IonoscloudProvider#token}
        :param username: IonosCloud username for API operations. If token is provided, token is preferred. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#username IonoscloudProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38f2041b94295b16711785593401416f25c4a3e355c8cb5a7bc004e641bef70a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = IonoscloudProviderConfig(
            alias=alias,
            endpoint=endpoint,
            password=password,
            retries=retries,
            token=token,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

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
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc713bc27c8dfe27e7799690f13443fd5dd6efd4901475b5897bdffd46a7981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6184b695e5f884c9e57a50857ff1b8f049eda1d32234e389c8696ffad1a2a33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3fe1152e2b1210c998d02721b63d7e2155fca0583d06dcae170e5f133b0b6ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b51433d24f003a0c2b4866c3e2bf22104b139d1d3f369efa55427f3efe8d22f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1453d57758943a30efd04c767d55b6a08818e37c1b205c7a630936b8f414a64c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda90a08b13a3a588cca05d821c62aa50f0f78c003b85f6c464606655a0550fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.provider.IonoscloudProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "endpoint": "endpoint",
        "password": "password",
        "retries": "retries",
        "token": "token",
        "username": "username",
    },
)
class IonoscloudProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#alias IonoscloudProvider#alias}
        :param endpoint: IonosCloud REST API URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#endpoint IonoscloudProvider#endpoint}
        :param password: IonosCloud password for API operations. If token is provided, token is preferred. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#password IonoscloudProvider#password}
        :param retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#retries IonoscloudProvider#retries}.
        :param token: IonosCloud bearer token for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#token IonoscloudProvider#token}
        :param username: IonosCloud username for API operations. If token is provided, token is preferred. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#username IonoscloudProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7034268ca4ebaaca1f7a9b600ff4f747d12ffd7016ff14156955e864b080c358)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if password is not None:
            self._values["password"] = password
        if retries is not None:
            self._values["retries"] = retries
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#alias IonoscloudProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''IonosCloud REST API URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#endpoint IonoscloudProvider#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''IonosCloud password for API operations. If token is provided, token is preferred.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#password IonoscloudProvider#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#retries IonoscloudProvider#retries}.'''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''IonosCloud bearer token for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#token IonoscloudProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''IonosCloud username for API operations. If token is provided, token is preferred.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud#username IonoscloudProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IonoscloudProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IonoscloudProvider",
    "IonoscloudProviderConfig",
]

publication.publish()

def _typecheckingstub__38f2041b94295b16711785593401416f25c4a3e355c8cb5a7bc004e641bef70a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    retries: typing.Optional[jsii.Number] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc713bc27c8dfe27e7799690f13443fd5dd6efd4901475b5897bdffd46a7981(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6184b695e5f884c9e57a50857ff1b8f049eda1d32234e389c8696ffad1a2a33(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3fe1152e2b1210c998d02721b63d7e2155fca0583d06dcae170e5f133b0b6ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b51433d24f003a0c2b4866c3e2bf22104b139d1d3f369efa55427f3efe8d22f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1453d57758943a30efd04c767d55b6a08818e37c1b205c7a630936b8f414a64c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda90a08b13a3a588cca05d821c62aa50f0f78c003b85f6c464606655a0550fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7034268ca4ebaaca1f7a9b600ff4f747d12ffd7016ff14156955e864b080c358(
    *,
    alias: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    retries: typing.Optional[jsii.Number] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
