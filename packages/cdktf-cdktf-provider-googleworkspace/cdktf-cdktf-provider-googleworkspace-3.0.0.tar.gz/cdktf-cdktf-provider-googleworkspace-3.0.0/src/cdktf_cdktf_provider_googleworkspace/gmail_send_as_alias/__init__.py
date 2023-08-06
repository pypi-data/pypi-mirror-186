'''
# `googleworkspace_gmail_send_as_alias`

Refer to the Terraform Registory for docs: [`googleworkspace_gmail_send_as_alias`](https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias).
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


class GmailSendAsAlias(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.gmailSendAsAlias.GmailSendAsAlias",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias googleworkspace_gmail_send_as_alias}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        primary_email: builtins.str,
        send_as_email: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reply_to_address: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        smtp_msa: typing.Optional[typing.Union["GmailSendAsAliasSmtpMsa", typing.Dict[builtins.str, typing.Any]]] = None,
        treat_as_alias: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias googleworkspace_gmail_send_as_alias} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param primary_email: User's primary email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#primary_email GmailSendAsAlias#primary_email}
        :param send_as_email: The email address that appears in the 'From:' header for mail sent using this alias. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#send_as_email GmailSendAsAlias#send_as_email}
        :param display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#display_name GmailSendAsAlias#display_name}
        :param is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address. Toggling an existing alias' default to false is not possible, another alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to synchronize with remote state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#is_default GmailSendAsAlias#is_default}
        :param reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#reply_to_address GmailSendAsAlias#reply_to_address}
        :param signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#signature GmailSendAsAlias#signature}
        :param smtp_msa: smtp_msa block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#smtp_msa GmailSendAsAlias#smtp_msa}
        :param treat_as_alias: Defaults to ``true``. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#treat_as_alias GmailSendAsAlias#treat_as_alias}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccaefa5ab7e2e0116d07aeff50c57b1c4d830b8c31331007f0168fcf7ce28a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GmailSendAsAliasConfig(
            primary_email=primary_email,
            send_as_email=send_as_email,
            display_name=display_name,
            is_default=is_default,
            reply_to_address=reply_to_address,
            signature=signature,
            smtp_msa=smtp_msa,
            treat_as_alias=treat_as_alias,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putSmtpMsa")
    def put_smtp_msa(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        password: typing.Optional[builtins.str] = None,
        security_mode: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The hostname of the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#host GmailSendAsAlias#host}
        :param port: The port of the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#port GmailSendAsAlias#port}
        :param password: The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#password GmailSendAsAlias#password}
        :param security_mode: Defaults to ``securityModeUnspecified``. The protocol that will be used to secure communication with the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#security_mode GmailSendAsAlias#security_mode}
        :param username: The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#username GmailSendAsAlias#username}
        '''
        value = GmailSendAsAliasSmtpMsa(
            host=host,
            port=port,
            password=password,
            security_mode=security_mode,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putSmtpMsa", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="resetReplyToAddress")
    def reset_reply_to_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyToAddress", []))

    @jsii.member(jsii_name="resetSignature")
    def reset_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignature", []))

    @jsii.member(jsii_name="resetSmtpMsa")
    def reset_smtp_msa(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmtpMsa", []))

    @jsii.member(jsii_name="resetTreatAsAlias")
    def reset_treat_as_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTreatAsAlias", []))

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
    @jsii.member(jsii_name="isPrimary")
    def is_primary(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "isPrimary"))

    @builtins.property
    @jsii.member(jsii_name="smtpMsa")
    def smtp_msa(self) -> "GmailSendAsAliasSmtpMsaOutputReference":
        return typing.cast("GmailSendAsAliasSmtpMsaOutputReference", jsii.get(self, "smtpMsa"))

    @builtins.property
    @jsii.member(jsii_name="verificationStatus")
    def verification_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verificationStatus"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryEmailInput")
    def primary_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToAddressInput")
    def reply_to_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="sendAsEmailInput")
    def send_as_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sendAsEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureInput")
    def signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureInput"))

    @builtins.property
    @jsii.member(jsii_name="smtpMsaInput")
    def smtp_msa_input(self) -> typing.Optional["GmailSendAsAliasSmtpMsa"]:
        return typing.cast(typing.Optional["GmailSendAsAliasSmtpMsa"], jsii.get(self, "smtpMsaInput"))

    @builtins.property
    @jsii.member(jsii_name="treatAsAliasInput")
    def treat_as_alias_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "treatAsAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b992ab897ebaee50668cd8f72ab56c2ccd0743acf8b7514f4c8747b23d8d3ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a84931a3fe86cf083d53a6ef544e4f9327580827a9eee722dcde98ec59b4944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="primaryEmail")
    def primary_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryEmail"))

    @primary_email.setter
    def primary_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecf5357cfa5d8c6bc110bff45d7b58bb02520cce802723be8303ba2ca21ba353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryEmail", value)

    @builtins.property
    @jsii.member(jsii_name="replyToAddress")
    def reply_to_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyToAddress"))

    @reply_to_address.setter
    def reply_to_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e6210b541c6433d644a91b53454e9472cc42ac486e5b93fb08ffda2a6781bf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyToAddress", value)

    @builtins.property
    @jsii.member(jsii_name="sendAsEmail")
    def send_as_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sendAsEmail"))

    @send_as_email.setter
    def send_as_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__858c62cc7d4e5560d9ba39b44e63b207240d210030bbd8cd1fb938166c9ce062)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendAsEmail", value)

    @builtins.property
    @jsii.member(jsii_name="signature")
    def signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signature"))

    @signature.setter
    def signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2eefe3f2a58cb47850cefc4cf318ef6e928dd70dfbd1b8ced233d5ac4bccbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signature", value)

    @builtins.property
    @jsii.member(jsii_name="treatAsAlias")
    def treat_as_alias(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "treatAsAlias"))

    @treat_as_alias.setter
    def treat_as_alias(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15bc870e180d1525162dd3d37b5f1866525c66cea9c303687cc81178e4421830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatAsAlias", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.gmailSendAsAlias.GmailSendAsAliasConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "primary_email": "primaryEmail",
        "send_as_email": "sendAsEmail",
        "display_name": "displayName",
        "is_default": "isDefault",
        "reply_to_address": "replyToAddress",
        "signature": "signature",
        "smtp_msa": "smtpMsa",
        "treat_as_alias": "treatAsAlias",
    },
)
class GmailSendAsAliasConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        primary_email: builtins.str,
        send_as_email: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        reply_to_address: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        smtp_msa: typing.Optional[typing.Union["GmailSendAsAliasSmtpMsa", typing.Dict[builtins.str, typing.Any]]] = None,
        treat_as_alias: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param primary_email: User's primary email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#primary_email GmailSendAsAlias#primary_email}
        :param send_as_email: The email address that appears in the 'From:' header for mail sent using this alias. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#send_as_email GmailSendAsAlias#send_as_email}
        :param display_name: A name that appears in the 'From:' header for mail sent using this alias. For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#display_name GmailSendAsAlias#display_name}
        :param is_default: Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address. Toggling an existing alias' default to false is not possible, another alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to synchronize with remote state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#is_default GmailSendAsAlias#is_default}
        :param reply_to_address: An optional email address that is included in a 'Reply-To:' header for mail sent using this alias. If this is empty, Gmail will not generate a 'Reply-To:' header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#reply_to_address GmailSendAsAlias#reply_to_address}
        :param signature: An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#signature GmailSendAsAlias#signature}
        :param smtp_msa: smtp_msa block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#smtp_msa GmailSendAsAlias#smtp_msa}
        :param treat_as_alias: Defaults to ``true``. Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#treat_as_alias GmailSendAsAlias#treat_as_alias}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(smtp_msa, dict):
            smtp_msa = GmailSendAsAliasSmtpMsa(**smtp_msa)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad61f37f2b22138d22e4742228a80225a7f86ce76ff879a7daa510a3233a9a9d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument primary_email", value=primary_email, expected_type=type_hints["primary_email"])
            check_type(argname="argument send_as_email", value=send_as_email, expected_type=type_hints["send_as_email"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument reply_to_address", value=reply_to_address, expected_type=type_hints["reply_to_address"])
            check_type(argname="argument signature", value=signature, expected_type=type_hints["signature"])
            check_type(argname="argument smtp_msa", value=smtp_msa, expected_type=type_hints["smtp_msa"])
            check_type(argname="argument treat_as_alias", value=treat_as_alias, expected_type=type_hints["treat_as_alias"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "primary_email": primary_email,
            "send_as_email": send_as_email,
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
        if display_name is not None:
            self._values["display_name"] = display_name
        if is_default is not None:
            self._values["is_default"] = is_default
        if reply_to_address is not None:
            self._values["reply_to_address"] = reply_to_address
        if signature is not None:
            self._values["signature"] = signature
        if smtp_msa is not None:
            self._values["smtp_msa"] = smtp_msa
        if treat_as_alias is not None:
            self._values["treat_as_alias"] = treat_as_alias

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
    def primary_email(self) -> builtins.str:
        '''User's primary email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#primary_email GmailSendAsAlias#primary_email}
        '''
        result = self._values.get("primary_email")
        assert result is not None, "Required property 'primary_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def send_as_email(self) -> builtins.str:
        '''The email address that appears in the 'From:' header for mail sent using this alias.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#send_as_email GmailSendAsAlias#send_as_email}
        '''
        result = self._values.get("send_as_email")
        assert result is not None, "Required property 'send_as_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A name that appears in the 'From:' header for mail sent using this alias.

        For custom 'from' addresses, when this is empty, Gmail will populate the 'From:' header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#display_name GmailSendAsAlias#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether this address is selected as the default 'From:' address in situations such as composing a new message or sending a vacation auto-reply.

        Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address. Toggling an existing alias' default to false is not possible, another alias must be added/imported and toggled to true to remove the default from an existing alias. To avoid drift with Terraform, please change the previous default's config to false AFTER a new default is applied and perform a refresh to synchronize with remote state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#is_default GmailSendAsAlias#is_default}
        '''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def reply_to_address(self) -> typing.Optional[builtins.str]:
        '''An optional email address that is included in a 'Reply-To:' header for mail sent using this alias.

        If this is empty, Gmail will not generate a 'Reply-To:' header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#reply_to_address GmailSendAsAlias#reply_to_address}
        '''
        result = self._values.get("reply_to_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature(self) -> typing.Optional[builtins.str]:
        '''An optional HTML signature that is included in messages composed with this alias in the Gmail web UI.

        This signature is added to new emails only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#signature GmailSendAsAlias#signature}
        '''
        result = self._values.get("signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smtp_msa(self) -> typing.Optional["GmailSendAsAliasSmtpMsa"]:
        '''smtp_msa block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#smtp_msa GmailSendAsAlias#smtp_msa}
        '''
        result = self._values.get("smtp_msa")
        return typing.cast(typing.Optional["GmailSendAsAliasSmtpMsa"], result)

    @builtins.property
    def treat_as_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to ``true``.

        Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom 'from' aliases. See https://support.google.com/a/answer/1710338 for help on making this decision

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#treat_as_alias GmailSendAsAlias#treat_as_alias}
        '''
        result = self._values.get("treat_as_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GmailSendAsAliasConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.gmailSendAsAlias.GmailSendAsAliasSmtpMsa",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "port": "port",
        "password": "password",
        "security_mode": "securityMode",
        "username": "username",
    },
)
class GmailSendAsAliasSmtpMsa:
    def __init__(
        self,
        *,
        host: builtins.str,
        port: jsii.Number,
        password: typing.Optional[builtins.str] = None,
        security_mode: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The hostname of the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#host GmailSendAsAlias#host}
        :param port: The port of the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#port GmailSendAsAlias#port}
        :param password: The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#password GmailSendAsAlias#password}
        :param security_mode: Defaults to ``securityModeUnspecified``. The protocol that will be used to secure communication with the SMTP service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#security_mode GmailSendAsAlias#security_mode}
        :param username: The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#username GmailSendAsAlias#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401cb67c55d791db3d1ab76a9f620ce31ea45168de561d0595472b120b23e8cd)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument security_mode", value=security_mode, expected_type=type_hints["security_mode"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host": host,
            "port": port,
        }
        if password is not None:
            self._values["password"] = password
        if security_mode is not None:
            self._values["security_mode"] = security_mode
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def host(self) -> builtins.str:
        '''The hostname of the SMTP service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#host GmailSendAsAlias#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port of the SMTP service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#port GmailSendAsAlias#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password that will be used for authentication with the SMTP service.

        This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#password GmailSendAsAlias#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_mode(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``securityModeUnspecified``. The protocol that will be used to secure communication with the SMTP service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#security_mode GmailSendAsAlias#security_mode}
        '''
        result = self._values.get("security_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username that will be used for authentication with the SMTP service.

        This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/gmail_send_as_alias#username GmailSendAsAlias#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GmailSendAsAliasSmtpMsa(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GmailSendAsAliasSmtpMsaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.gmailSendAsAlias.GmailSendAsAliasSmtpMsaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8fc5a7abfc566ea371b8bf1b82e459eae7ddf75a9abf23a2d4d7a83be7b863b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSecurityMode")
    def reset_security_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityMode", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="securityModeInput")
    def security_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityModeInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c79e0bf0d21ea1f0e1e737e4c474b71c48ecfd23bcd7b6be016843c935aa34ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17fc3f71561dbe39e4ef0d4c7942bb397faac67914d34be6b0c717c77e78464a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9e5ea3239dbc34d19dd1763151c49a1fafd59208cb10c67d6b3a884147697c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="securityMode")
    def security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityMode"))

    @security_mode.setter
    def security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0200d42305fe10b38bba7e91c70b4e862d1dac7ea5a6c8420c087b39beed2dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityMode", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795268cc71219974b37b4fcc0eb1e387bc48ba0555f4e1854eed9b793067872a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GmailSendAsAliasSmtpMsa]:
        return typing.cast(typing.Optional[GmailSendAsAliasSmtpMsa], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GmailSendAsAliasSmtpMsa]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e78210bc755cbc880e40443c06806dd12e14306cd65d3e91dd6e3de93b10a359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GmailSendAsAlias",
    "GmailSendAsAliasConfig",
    "GmailSendAsAliasSmtpMsa",
    "GmailSendAsAliasSmtpMsaOutputReference",
]

publication.publish()

def _typecheckingstub__7ccaefa5ab7e2e0116d07aeff50c57b1c4d830b8c31331007f0168fcf7ce28a6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    primary_email: builtins.str,
    send_as_email: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reply_to_address: typing.Optional[builtins.str] = None,
    signature: typing.Optional[builtins.str] = None,
    smtp_msa: typing.Optional[typing.Union[GmailSendAsAliasSmtpMsa, typing.Dict[builtins.str, typing.Any]]] = None,
    treat_as_alias: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__1b992ab897ebaee50668cd8f72ab56c2ccd0743acf8b7514f4c8747b23d8d3ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a84931a3fe86cf083d53a6ef544e4f9327580827a9eee722dcde98ec59b4944(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf5357cfa5d8c6bc110bff45d7b58bb02520cce802723be8303ba2ca21ba353(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e6210b541c6433d644a91b53454e9472cc42ac486e5b93fb08ffda2a6781bf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858c62cc7d4e5560d9ba39b44e63b207240d210030bbd8cd1fb938166c9ce062(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2eefe3f2a58cb47850cefc4cf318ef6e928dd70dfbd1b8ced233d5ac4bccbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15bc870e180d1525162dd3d37b5f1866525c66cea9c303687cc81178e4421830(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad61f37f2b22138d22e4742228a80225a7f86ce76ff879a7daa510a3233a9a9d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    primary_email: builtins.str,
    send_as_email: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    reply_to_address: typing.Optional[builtins.str] = None,
    signature: typing.Optional[builtins.str] = None,
    smtp_msa: typing.Optional[typing.Union[GmailSendAsAliasSmtpMsa, typing.Dict[builtins.str, typing.Any]]] = None,
    treat_as_alias: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401cb67c55d791db3d1ab76a9f620ce31ea45168de561d0595472b120b23e8cd(
    *,
    host: builtins.str,
    port: jsii.Number,
    password: typing.Optional[builtins.str] = None,
    security_mode: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fc5a7abfc566ea371b8bf1b82e459eae7ddf75a9abf23a2d4d7a83be7b863b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c79e0bf0d21ea1f0e1e737e4c474b71c48ecfd23bcd7b6be016843c935aa34ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17fc3f71561dbe39e4ef0d4c7942bb397faac67914d34be6b0c717c77e78464a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9e5ea3239dbc34d19dd1763151c49a1fafd59208cb10c67d6b3a884147697c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0200d42305fe10b38bba7e91c70b4e862d1dac7ea5a6c8420c087b39beed2dc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795268cc71219974b37b4fcc0eb1e387bc48ba0555f4e1854eed9b793067872a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78210bc755cbc880e40443c06806dd12e14306cd65d3e91dd6e3de93b10a359(
    value: typing.Optional[GmailSendAsAliasSmtpMsa],
) -> None:
    """Type checking stubs"""
    pass
