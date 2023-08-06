'''
# `salesforce_user`

Refer to the Terraform Registory for docs: [`salesforce_user`](https://www.terraform.io/docs/providers/salesforce/r/user).
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


class User(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-salesforce.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/salesforce/r/user salesforce_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: builtins.str,
        email: builtins.str,
        last_name: builtins.str,
        profile_id: builtins.str,
        username: builtins.str,
        email_encoding_key: typing.Optional[builtins.str] = None,
        language_locale_key: typing.Optional[builtins.str] = None,
        locale_sid_key: typing.Optional[builtins.str] = None,
        reset_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        time_zone_sid_key: typing.Optional[builtins.str] = None,
        user_role_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/salesforce/r/user salesforce_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: The user’s alias. For example, jsmith. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#alias User#alias}
        :param email: The user’s email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email User#email}
        :param last_name: The user’s last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#last_name User#last_name}
        :param profile_id: ID of the user’s Profile. Use this value to cache metadata based on profile. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#profile_id User#profile_id}
        :param username: Contains the name that a user enters to log in to the API or the user interface. The value for this field must be in the form of an email address, using all lowercase characters. It must also be unique across all organizations. If you try to create or update a User with a duplicate value for this field, the operation is rejected. Each inserted User also counts as a license. Every organization has a maximum number of licenses. If you attempt to exceed the maximum number of licenses by inserting User records, the create request is rejected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#username User#username}
        :param email_encoding_key: The email encoding for the user, such as ISO-8859-1 or UTF-8. Defaults to UTF-8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email_encoding_key User#email_encoding_key}
        :param language_locale_key: The user’s language. Defaults to en_US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#language_locale_key User#language_locale_key}
        :param locale_sid_key: The value of the field affects formatting and parsing of values, especially numeric values, in the user interface. It doesn’t affect the API. The field values are named according to the language, and the country if necessary, using two-letter ISO codes. The set of names is based on the ISO standard. You can also manually set a user’s locale in the user interface, and then use that value for inserting or updating other users via the API. Defaults to en_US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#locale_sid_key User#locale_sid_key}
        :param reset_password: Reset password and send an email to the user. No reset is performed if this field is omitted, is false, or was true and remained true on subsequent apply. Please set to false and then true in subsequent applies, or have it set to true on create to trigger the reset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#reset_password User#reset_password}
        :param time_zone_sid_key: A User time zone affects the offset used when displaying or entering times in the user interface. But the API doesn’t use a User time zone when querying or setting values. Values for this field are named using region and key city, according to ISO standards. You can also manually set one User time zone in the user interface, and then use that value for creating or updating other User records via the API. Defaults to America/New_York. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#time_zone_sid_key User#time_zone_sid_key}
        :param user_role_id: ID of the user’s UserRole. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#user_role_id User#user_role_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3fcadec94117073fc55da8bf89a3fc01be723b874f8921ad4f0fdaba22f63d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = UserConfig(
            alias=alias,
            email=email,
            last_name=last_name,
            profile_id=profile_id,
            username=username,
            email_encoding_key=email_encoding_key,
            language_locale_key=language_locale_key,
            locale_sid_key=locale_sid_key,
            reset_password=reset_password,
            time_zone_sid_key=time_zone_sid_key,
            user_role_id=user_role_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetEmailEncodingKey")
    def reset_email_encoding_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailEncodingKey", []))

    @jsii.member(jsii_name="resetLanguageLocaleKey")
    def reset_language_locale_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageLocaleKey", []))

    @jsii.member(jsii_name="resetLocaleSidKey")
    def reset_locale_sid_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocaleSidKey", []))

    @jsii.member(jsii_name="resetResetPassword")
    def reset_reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetPassword", []))

    @jsii.member(jsii_name="resetTimeZoneSidKey")
    def reset_time_zone_sid_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZoneSidKey", []))

    @jsii.member(jsii_name="resetUserRoleId")
    def reset_user_role_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserRoleId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="emailEncodingKeyInput")
    def email_encoding_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailEncodingKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="languageLocaleKeyInput")
    def language_locale_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageLocaleKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastNameInput"))

    @builtins.property
    @jsii.member(jsii_name="localeSidKeyInput")
    def locale_sid_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localeSidKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resetPasswordInput")
    def reset_password_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "resetPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneSidKeyInput")
    def time_zone_sid_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneSidKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="userRoleIdInput")
    def user_role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userRoleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7389e89d6e4b5db0f5b19552d830ee553c7c96a0d0a955c50bd201fd275ac1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd2c98407afeeeb81f6f1b90dd2cf0c19b40063c927905e58c0ea919be127e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailEncodingKey")
    def email_encoding_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailEncodingKey"))

    @email_encoding_key.setter
    def email_encoding_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a5ae8b7805d7a42624a7dcdadd017ff6daa179e246df805b5d735e9889d09c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailEncodingKey", value)

    @builtins.property
    @jsii.member(jsii_name="languageLocaleKey")
    def language_locale_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageLocaleKey"))

    @language_locale_key.setter
    def language_locale_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95838a84b8d5bef0e183b0f8353556906ae62868d703cc238a577091992d7331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageLocaleKey", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442dbbe9533529027844e4090182c2f9e949a5550c7bd6988bbf48596aa75413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="localeSidKey")
    def locale_sid_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localeSidKey"))

    @locale_sid_key.setter
    def locale_sid_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__130df2733026e705845653a7ec490bff6b704cb2fc6b66ac9c311c86fb0c4e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localeSidKey", value)

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2978499d00f13fc6eb20a55079fc21b1e4f2c63ca645abfc5ff717d82c18243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="resetPassword")
    def reset_password(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "resetPassword"))

    @reset_password.setter
    def reset_password(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bace032defc93b10e8e53af59883d9c7c20727027112293f9de880ce25138db0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resetPassword", value)

    @builtins.property
    @jsii.member(jsii_name="timeZoneSidKey")
    def time_zone_sid_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZoneSidKey"))

    @time_zone_sid_key.setter
    def time_zone_sid_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63045abf1a69e724d3e134bb522d47a8c33571ace86e7bb57e4dc05440fbbe39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZoneSidKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aaf7430a1cb638ade4482166a3635141a0dfdf8f2cc6c3f5905a508a9c1ab80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="userRoleId")
    def user_role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userRoleId"))

    @user_role_id.setter
    def user_role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27fa95790617bc657397f30633120d285757cf0a237e311c83812da0065f26f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRoleId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-salesforce.user.UserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alias": "alias",
        "email": "email",
        "last_name": "lastName",
        "profile_id": "profileId",
        "username": "username",
        "email_encoding_key": "emailEncodingKey",
        "language_locale_key": "languageLocaleKey",
        "locale_sid_key": "localeSidKey",
        "reset_password": "resetPassword",
        "time_zone_sid_key": "timeZoneSidKey",
        "user_role_id": "userRoleId",
    },
)
class UserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        alias: builtins.str,
        email: builtins.str,
        last_name: builtins.str,
        profile_id: builtins.str,
        username: builtins.str,
        email_encoding_key: typing.Optional[builtins.str] = None,
        language_locale_key: typing.Optional[builtins.str] = None,
        locale_sid_key: typing.Optional[builtins.str] = None,
        reset_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        time_zone_sid_key: typing.Optional[builtins.str] = None,
        user_role_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param alias: The user’s alias. For example, jsmith. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#alias User#alias}
        :param email: The user’s email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email User#email}
        :param last_name: The user’s last name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#last_name User#last_name}
        :param profile_id: ID of the user’s Profile. Use this value to cache metadata based on profile. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#profile_id User#profile_id}
        :param username: Contains the name that a user enters to log in to the API or the user interface. The value for this field must be in the form of an email address, using all lowercase characters. It must also be unique across all organizations. If you try to create or update a User with a duplicate value for this field, the operation is rejected. Each inserted User also counts as a license. Every organization has a maximum number of licenses. If you attempt to exceed the maximum number of licenses by inserting User records, the create request is rejected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#username User#username}
        :param email_encoding_key: The email encoding for the user, such as ISO-8859-1 or UTF-8. Defaults to UTF-8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email_encoding_key User#email_encoding_key}
        :param language_locale_key: The user’s language. Defaults to en_US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#language_locale_key User#language_locale_key}
        :param locale_sid_key: The value of the field affects formatting and parsing of values, especially numeric values, in the user interface. It doesn’t affect the API. The field values are named according to the language, and the country if necessary, using two-letter ISO codes. The set of names is based on the ISO standard. You can also manually set a user’s locale in the user interface, and then use that value for inserting or updating other users via the API. Defaults to en_US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#locale_sid_key User#locale_sid_key}
        :param reset_password: Reset password and send an email to the user. No reset is performed if this field is omitted, is false, or was true and remained true on subsequent apply. Please set to false and then true in subsequent applies, or have it set to true on create to trigger the reset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#reset_password User#reset_password}
        :param time_zone_sid_key: A User time zone affects the offset used when displaying or entering times in the user interface. But the API doesn’t use a User time zone when querying or setting values. Values for this field are named using region and key city, according to ISO standards. You can also manually set one User time zone in the user interface, and then use that value for creating or updating other User records via the API. Defaults to America/New_York. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#time_zone_sid_key User#time_zone_sid_key}
        :param user_role_id: ID of the user’s UserRole. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#user_role_id User#user_role_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258da2adb5f434d4c71fb0b2646bf9976b10dd70457167daa77d33c15d4a9f52)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument email_encoding_key", value=email_encoding_key, expected_type=type_hints["email_encoding_key"])
            check_type(argname="argument language_locale_key", value=language_locale_key, expected_type=type_hints["language_locale_key"])
            check_type(argname="argument locale_sid_key", value=locale_sid_key, expected_type=type_hints["locale_sid_key"])
            check_type(argname="argument reset_password", value=reset_password, expected_type=type_hints["reset_password"])
            check_type(argname="argument time_zone_sid_key", value=time_zone_sid_key, expected_type=type_hints["time_zone_sid_key"])
            check_type(argname="argument user_role_id", value=user_role_id, expected_type=type_hints["user_role_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
            "email": email,
            "last_name": last_name,
            "profile_id": profile_id,
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
        if email_encoding_key is not None:
            self._values["email_encoding_key"] = email_encoding_key
        if language_locale_key is not None:
            self._values["language_locale_key"] = language_locale_key
        if locale_sid_key is not None:
            self._values["locale_sid_key"] = locale_sid_key
        if reset_password is not None:
            self._values["reset_password"] = reset_password
        if time_zone_sid_key is not None:
            self._values["time_zone_sid_key"] = time_zone_sid_key
        if user_role_id is not None:
            self._values["user_role_id"] = user_role_id

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
    def alias(self) -> builtins.str:
        '''The user’s alias. For example, jsmith.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#alias User#alias}
        '''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The user’s email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email User#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def last_name(self) -> builtins.str:
        '''The user’s last name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#last_name User#last_name}
        '''
        result = self._values.get("last_name")
        assert result is not None, "Required property 'last_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''ID of the user’s Profile. Use this value to cache metadata based on profile.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#profile_id User#profile_id}
        '''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Contains the name that a user enters to log in to the API or the user interface.

        The value for this field must be in the form of an email address, using all lowercase characters. It must also be unique across all organizations. If you try to create or update a User with a duplicate value for this field, the operation is rejected. Each inserted User also counts as a license. Every organization has a maximum number of licenses. If you attempt to exceed the maximum number of licenses by inserting User records, the create request is rejected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#username User#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_encoding_key(self) -> typing.Optional[builtins.str]:
        '''The email encoding for the user, such as ISO-8859-1 or UTF-8. Defaults to UTF-8.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#email_encoding_key User#email_encoding_key}
        '''
        result = self._values.get("email_encoding_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_locale_key(self) -> typing.Optional[builtins.str]:
        '''The user’s language. Defaults to en_US.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#language_locale_key User#language_locale_key}
        '''
        result = self._values.get("language_locale_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locale_sid_key(self) -> typing.Optional[builtins.str]:
        '''The value of the field affects formatting and parsing of values, especially numeric values, in the user interface.

        It doesn’t affect the API. The field values are named according to the language, and the country if necessary, using two-letter ISO codes. The set of names is based on the ISO standard. You can also manually set a user’s locale in the user interface, and then use that value for inserting or updating other users via the API. Defaults to en_US.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#locale_sid_key User#locale_sid_key}
        '''
        result = self._values.get("locale_sid_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reset_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Reset password and send an email to the user.

        No reset is performed if this field is omitted, is false, or was true and remained true on subsequent apply. Please set to false and then true in subsequent applies, or have it set to true on create to trigger the reset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#reset_password User#reset_password}
        '''
        result = self._values.get("reset_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def time_zone_sid_key(self) -> typing.Optional[builtins.str]:
        '''A User time zone affects the offset used when displaying or entering times in the user interface.

        But the API doesn’t use a User time zone when querying or setting values. Values for this field are named using region and key city, according to ISO standards. You can also manually set one User time zone in the user interface, and then use that value for creating or updating other User records via the API. Defaults to America/New_York.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#time_zone_sid_key User#time_zone_sid_key}
        '''
        result = self._values.get("time_zone_sid_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_role_id(self) -> typing.Optional[builtins.str]:
        '''ID of the user’s UserRole.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/salesforce/r/user#user_role_id User#user_role_id}
        '''
        result = self._values.get("user_role_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "User",
    "UserConfig",
]

publication.publish()

def _typecheckingstub__c3fcadec94117073fc55da8bf89a3fc01be723b874f8921ad4f0fdaba22f63d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: builtins.str,
    email: builtins.str,
    last_name: builtins.str,
    profile_id: builtins.str,
    username: builtins.str,
    email_encoding_key: typing.Optional[builtins.str] = None,
    language_locale_key: typing.Optional[builtins.str] = None,
    locale_sid_key: typing.Optional[builtins.str] = None,
    reset_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    time_zone_sid_key: typing.Optional[builtins.str] = None,
    user_role_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e7389e89d6e4b5db0f5b19552d830ee553c7c96a0d0a955c50bd201fd275ac1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd2c98407afeeeb81f6f1b90dd2cf0c19b40063c927905e58c0ea919be127e4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a5ae8b7805d7a42624a7dcdadd017ff6daa179e246df805b5d735e9889d09c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95838a84b8d5bef0e183b0f8353556906ae62868d703cc238a577091992d7331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442dbbe9533529027844e4090182c2f9e949a5550c7bd6988bbf48596aa75413(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130df2733026e705845653a7ec490bff6b704cb2fc6b66ac9c311c86fb0c4e2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2978499d00f13fc6eb20a55079fc21b1e4f2c63ca645abfc5ff717d82c18243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bace032defc93b10e8e53af59883d9c7c20727027112293f9de880ce25138db0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63045abf1a69e724d3e134bb522d47a8c33571ace86e7bb57e4dc05440fbbe39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aaf7430a1cb638ade4482166a3635141a0dfdf8f2cc6c3f5905a508a9c1ab80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27fa95790617bc657397f30633120d285757cf0a237e311c83812da0065f26f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258da2adb5f434d4c71fb0b2646bf9976b10dd70457167daa77d33c15d4a9f52(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    alias: builtins.str,
    email: builtins.str,
    last_name: builtins.str,
    profile_id: builtins.str,
    username: builtins.str,
    email_encoding_key: typing.Optional[builtins.str] = None,
    language_locale_key: typing.Optional[builtins.str] = None,
    locale_sid_key: typing.Optional[builtins.str] = None,
    reset_password: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    time_zone_sid_key: typing.Optional[builtins.str] = None,
    user_role_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
