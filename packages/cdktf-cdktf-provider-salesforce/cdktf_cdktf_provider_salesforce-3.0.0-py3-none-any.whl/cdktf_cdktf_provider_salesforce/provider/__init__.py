'''
# `provider`

Refer to the Terraform Registory for docs: [`salesforce`](https://www.terraform.io/docs/providers/salesforce).
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


class SalesforceProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-salesforce.provider.SalesforceProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/salesforce salesforce}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_version: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        login_url: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/salesforce salesforce} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#alias SalesforceProvider#alias}
        :param api_version: API version of the salesforce org in the format in the format: MAJOR.MINOR (please omit any leading 'v'). The provider requires at least version 53.0. Can be specified with the environment variable SALESFORCE_API_VERSION. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#api_version SalesforceProvider#api_version}
        :param client_id: Client ID of the connected app. Corresponds to Consumer Key in the user interface. Can be specified with the environment variable SALESFORCE_CLIENT_ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#client_id SalesforceProvider#client_id}
        :param login_url: Directs the authentication request, defaults to the production endpoint https://login.salesforce.com, should be set to https://test.salesforce.com for sandbox organizations. Can be specified with the environment variable SALESFORCE_LOGIN_URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#login_url SalesforceProvider#login_url}
        :param private_key: Private Key associated to the public certificate that was uploaded to the connected app. This may point to a file location or be set directly. This should not be confused with the Consumer Secret in the user interface. Can be specified with the environment variable SALESFORCE_PRIVATE_KEY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#private_key SalesforceProvider#private_key}
        :param username: Salesforce Username of a System Administrator like user for the provider to authenticate as. Can be specified with the environment variable SALESFORCE_USERNAME. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#username SalesforceProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6435db0c50ddf76c4bce67d0322dfda080f6bcc1f0cabb9a44cc080d4ad548)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SalesforceProviderConfig(
            alias=alias,
            api_version=api_version,
            client_id=client_id,
            login_url=login_url,
            private_key=private_key,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetLoginUrl")
    def reset_login_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginUrl", []))

    @jsii.member(jsii_name="resetPrivateKey")
    def reset_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKey", []))

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
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="loginUrlInput")
    def login_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__244076854417a1531f4264381a7c0d323722a54a688ad7d1822de780ab4f1a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f206ddbe648f80b8613d3dfa5069da2e7813f744cab3c83fb945c424226e24b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a8e15019969189c4868308547332e1a02b46b8850f7afae8b7c4e53f63a360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="loginUrl")
    def login_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginUrl"))

    @login_url.setter
    def login_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0633e368c2a434e95e15a04e5a8685672106ac7ca8817c63c5c229f4ea057b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginUrl", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d570547870746dc743236f5af0b5a5a98c44739b136e71bf29f64f009f2c796)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e71c86fa4fdee14d0546ad55d18854b0356b5803dd00323b85adbe3acd51183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-salesforce.provider.SalesforceProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "api_version": "apiVersion",
        "client_id": "clientId",
        "login_url": "loginUrl",
        "private_key": "privateKey",
        "username": "username",
    },
)
class SalesforceProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_version: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        login_url: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#alias SalesforceProvider#alias}
        :param api_version: API version of the salesforce org in the format in the format: MAJOR.MINOR (please omit any leading 'v'). The provider requires at least version 53.0. Can be specified with the environment variable SALESFORCE_API_VERSION. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#api_version SalesforceProvider#api_version}
        :param client_id: Client ID of the connected app. Corresponds to Consumer Key in the user interface. Can be specified with the environment variable SALESFORCE_CLIENT_ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#client_id SalesforceProvider#client_id}
        :param login_url: Directs the authentication request, defaults to the production endpoint https://login.salesforce.com, should be set to https://test.salesforce.com for sandbox organizations. Can be specified with the environment variable SALESFORCE_LOGIN_URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#login_url SalesforceProvider#login_url}
        :param private_key: Private Key associated to the public certificate that was uploaded to the connected app. This may point to a file location or be set directly. This should not be confused with the Consumer Secret in the user interface. Can be specified with the environment variable SALESFORCE_PRIVATE_KEY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#private_key SalesforceProvider#private_key}
        :param username: Salesforce Username of a System Administrator like user for the provider to authenticate as. Can be specified with the environment variable SALESFORCE_USERNAME. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#username SalesforceProvider#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cccb7e72f3dacefeb9dfd2e21c25145b46807a24109c64dbbf0c080fa8caeff)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument login_url", value=login_url, expected_type=type_hints["login_url"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_version is not None:
            self._values["api_version"] = api_version
        if client_id is not None:
            self._values["client_id"] = client_id
        if login_url is not None:
            self._values["login_url"] = login_url
        if private_key is not None:
            self._values["private_key"] = private_key
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#alias SalesforceProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the salesforce org in the format in the format: MAJOR.MINOR (please omit any leading 'v'). The provider requires at least version 53.0. Can be specified with the environment variable SALESFORCE_API_VERSION.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#api_version SalesforceProvider#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Client ID of the connected app.

        Corresponds to Consumer Key in the user interface. Can be specified with the environment variable SALESFORCE_CLIENT_ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#client_id SalesforceProvider#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_url(self) -> typing.Optional[builtins.str]:
        '''Directs the authentication request, defaults to the production endpoint https://login.salesforce.com, should be set to https://test.salesforce.com for sandbox organizations. Can be specified with the environment variable SALESFORCE_LOGIN_URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#login_url SalesforceProvider#login_url}
        '''
        result = self._values.get("login_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''Private Key associated to the public certificate that was uploaded to the connected app.

        This may point to a file location or be set directly. This should not be confused with the Consumer Secret in the user interface. Can be specified with the environment variable SALESFORCE_PRIVATE_KEY.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#private_key SalesforceProvider#private_key}
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Salesforce Username of a System Administrator like user for the provider to authenticate as.

        Can be specified with the environment variable SALESFORCE_USERNAME.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce#username SalesforceProvider#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SalesforceProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SalesforceProvider",
    "SalesforceProviderConfig",
]

publication.publish()

def _typecheckingstub__9a6435db0c50ddf76c4bce67d0322dfda080f6bcc1f0cabb9a44cc080d4ad548(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    api_version: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    login_url: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244076854417a1531f4264381a7c0d323722a54a688ad7d1822de780ab4f1a94(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f206ddbe648f80b8613d3dfa5069da2e7813f744cab3c83fb945c424226e24b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a8e15019969189c4868308547332e1a02b46b8850f7afae8b7c4e53f63a360(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0633e368c2a434e95e15a04e5a8685672106ac7ca8817c63c5c229f4ea057b3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d570547870746dc743236f5af0b5a5a98c44739b136e71bf29f64f009f2c796(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e71c86fa4fdee14d0546ad55d18854b0356b5803dd00323b85adbe3acd51183(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cccb7e72f3dacefeb9dfd2e21c25145b46807a24109c64dbbf0c080fa8caeff(
    *,
    alias: typing.Optional[builtins.str] = None,
    api_version: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    login_url: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
