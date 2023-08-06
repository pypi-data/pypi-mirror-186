'''
# `provider`

Refer to the Terraform Registory for docs: [`googleworkspace`](https://www.terraform.io/docs/providers/googleworkspace).
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


class GoogleworkspaceProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.provider.GoogleworkspaceProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace googleworkspace}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        customer_id: typing.Optional[builtins.str] = None,
        impersonated_user_email: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace googleworkspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_token: A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the ``Authorization: Bearer`` token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to ``credentials``, and ignores the ``oauth_scopes`` field. If both are specified, ``access_token`` will be used over the ``credentials`` field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#access_token GoogleworkspaceProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#alias GoogleworkspaceProvider#alias}
        :param credentials: Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud Console). If not provided, the application default credentials will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#credentials GoogleworkspaceProvider#credentials}
        :param customer_id: The customer id provided with your Google Workspace subscription. It is found in the admin console under Account Settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#customer_id GoogleworkspaceProvider#customer_id}
        :param impersonated_user_email: The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API. ``impersonated_user_email`` is required for all services except group and user management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#impersonated_user_email GoogleworkspaceProvider#impersonated_user_email}
        :param oauth_scopes: The list of the scopes required for your application (for a list of possible scopes, see `Authorize requests <https://developers.google.com/admin-sdk/directory/v1/guides/authorizing>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#oauth_scopes GoogleworkspaceProvider#oauth_scopes}
        :param service_account: The service account used to create the provided ``access_token`` if authenticating using the ``access_token`` method and needing to impersonate a user. This service account will require the GCP role ``Service Account Token Creator`` if needing to impersonate a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#service_account GoogleworkspaceProvider#service_account}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5894dbbe4a2e3483e12acedce8a4b906b3a6a5d70aaec75b32c6df7b5c108f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GoogleworkspaceProviderConfig(
            access_token=access_token,
            alias=alias,
            credentials=credentials,
            customer_id=customer_id,
            impersonated_user_email=impersonated_user_email,
            oauth_scopes=oauth_scopes,
            service_account=service_account,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetCustomerId")
    def reset_customer_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerId", []))

    @jsii.member(jsii_name="resetImpersonatedUserEmail")
    def reset_impersonated_user_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImpersonatedUserEmail", []))

    @jsii.member(jsii_name="resetOauthScopes")
    def reset_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauthScopes", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="customerIdInput")
    def customer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="impersonatedUserEmailInput")
    def impersonated_user_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "impersonatedUserEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthScopesInput")
    def oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b7d8f9ad6db34874059439e40231e46dec1c4f89a1169247643001328619ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5ee2507d6e3b4e4f203dce88cefff26e5b9a90042c0a398bbb0141c1f2933c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e7891a9badc4e4612bd42d92e6ae1dfecf0364ec89cd833c9a218e4cbd4d71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="customerId")
    def customer_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerId"))

    @customer_id.setter
    def customer_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc86efd21dc0afb7266b59777007298dcee758926f068e9ea8f0d63740bd365b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerId", value)

    @builtins.property
    @jsii.member(jsii_name="impersonatedUserEmail")
    def impersonated_user_email(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "impersonatedUserEmail"))

    @impersonated_user_email.setter
    def impersonated_user_email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a70065c352d307633d0615b378826f4c1f3c4d838900eaad9ca863a12e84cf0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "impersonatedUserEmail", value)

    @builtins.property
    @jsii.member(jsii_name="oauthScopes")
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "oauthScopes"))

    @oauth_scopes.setter
    def oauth_scopes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4e7ced0ecf5e6fcb10add2ce7983375d9ffa36b1cddb98c5ad6fe029b632e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e44916287e909eefe50bc2fb7583f09efd5d8bcf2a873c2efc2b0c8b83a519a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.provider.GoogleworkspaceProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "alias": "alias",
        "credentials": "credentials",
        "customer_id": "customerId",
        "impersonated_user_email": "impersonatedUserEmail",
        "oauth_scopes": "oauthScopes",
        "service_account": "serviceAccount",
    },
)
class GoogleworkspaceProviderConfig:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        customer_id: typing.Optional[builtins.str] = None,
        impersonated_user_email: typing.Optional[builtins.str] = None,
        oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the ``Authorization: Bearer`` token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to ``credentials``, and ignores the ``oauth_scopes`` field. If both are specified, ``access_token`` will be used over the ``credentials`` field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#access_token GoogleworkspaceProvider#access_token}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#alias GoogleworkspaceProvider#alias}
        :param credentials: Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud Console). If not provided, the application default credentials will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#credentials GoogleworkspaceProvider#credentials}
        :param customer_id: The customer id provided with your Google Workspace subscription. It is found in the admin console under Account Settings. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#customer_id GoogleworkspaceProvider#customer_id}
        :param impersonated_user_email: The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API. ``impersonated_user_email`` is required for all services except group and user management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#impersonated_user_email GoogleworkspaceProvider#impersonated_user_email}
        :param oauth_scopes: The list of the scopes required for your application (for a list of possible scopes, see `Authorize requests <https://developers.google.com/admin-sdk/directory/v1/guides/authorizing>`_). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#oauth_scopes GoogleworkspaceProvider#oauth_scopes}
        :param service_account: The service account used to create the provided ``access_token`` if authenticating using the ``access_token`` method and needing to impersonate a user. This service account will require the GCP role ``Service Account Token Creator`` if needing to impersonate a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#service_account GoogleworkspaceProvider#service_account}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87b160856daefd564e852cb8095627bf815b9a8d8f80d11185d6d55195627b1d)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument customer_id", value=customer_id, expected_type=type_hints["customer_id"])
            check_type(argname="argument impersonated_user_email", value=impersonated_user_email, expected_type=type_hints["impersonated_user_email"])
            check_type(argname="argument oauth_scopes", value=oauth_scopes, expected_type=type_hints["oauth_scopes"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if alias is not None:
            self._values["alias"] = alias
        if credentials is not None:
            self._values["credentials"] = credentials
        if customer_id is not None:
            self._values["customer_id"] = customer_id
        if impersonated_user_email is not None:
            self._values["impersonated_user_email"] = impersonated_user_email
        if oauth_scopes is not None:
            self._values["oauth_scopes"] = oauth_scopes
        if service_account is not None:
            self._values["service_account"] = service_account

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the ``Authorization: Bearer`` token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to ``credentials``, and ignores the ``oauth_scopes`` field. If both are specified, ``access_token`` will be used over the ``credentials`` field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#access_token GoogleworkspaceProvider#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#alias GoogleworkspaceProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud Console).

        If not provided, the application default credentials will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#credentials GoogleworkspaceProvider#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_id(self) -> typing.Optional[builtins.str]:
        '''The customer id provided with your Google Workspace subscription. It is found in the admin console under Account Settings.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#customer_id GoogleworkspaceProvider#customer_id}
        '''
        result = self._values.get("customer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def impersonated_user_email(self) -> typing.Optional[builtins.str]:
        '''The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API.

        ``impersonated_user_email`` is required for all services except group and user management.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#impersonated_user_email GoogleworkspaceProvider#impersonated_user_email}
        '''
        result = self._values.get("impersonated_user_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of the scopes required for your application (for a list of possible scopes, see `Authorize requests <https://developers.google.com/admin-sdk/directory/v1/guides/authorizing>`_).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#oauth_scopes GoogleworkspaceProvider#oauth_scopes}
        '''
        result = self._values.get("oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The service account used to create the provided ``access_token`` if authenticating using the ``access_token`` method and needing to impersonate a user.

        This service account will require the GCP role ``Service Account Token Creator`` if needing to impersonate a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace#service_account GoogleworkspaceProvider#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleworkspaceProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GoogleworkspaceProvider",
    "GoogleworkspaceProviderConfig",
]

publication.publish()

def _typecheckingstub__ba5894dbbe4a2e3483e12acedce8a4b906b3a6a5d70aaec75b32c6df7b5c108f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[builtins.str] = None,
    customer_id: typing.Optional[builtins.str] = None,
    impersonated_user_email: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b7d8f9ad6db34874059439e40231e46dec1c4f89a1169247643001328619ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5ee2507d6e3b4e4f203dce88cefff26e5b9a90042c0a398bbb0141c1f2933c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e7891a9badc4e4612bd42d92e6ae1dfecf0364ec89cd833c9a218e4cbd4d71(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc86efd21dc0afb7266b59777007298dcee758926f068e9ea8f0d63740bd365b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a70065c352d307633d0615b378826f4c1f3c4d838900eaad9ca863a12e84cf0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e7ced0ecf5e6fcb10add2ce7983375d9ffa36b1cddb98c5ad6fe029b632e58(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e44916287e909eefe50bc2fb7583f09efd5d8bcf2a873c2efc2b0c8b83a519a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87b160856daefd564e852cb8095627bf815b9a8d8f80d11185d6d55195627b1d(
    *,
    access_token: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[builtins.str] = None,
    customer_id: typing.Optional[builtins.str] = None,
    impersonated_user_email: typing.Optional[builtins.str] = None,
    oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
