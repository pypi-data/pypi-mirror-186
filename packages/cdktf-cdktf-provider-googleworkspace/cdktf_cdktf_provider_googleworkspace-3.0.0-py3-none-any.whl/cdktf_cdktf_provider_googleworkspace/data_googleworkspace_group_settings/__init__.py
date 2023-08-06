'''
# `data_googleworkspace_group_settings`

Refer to the Terraform Registory for docs: [`data_googleworkspace_group_settings`](https://www.terraform.io/docs/providers/googleworkspace/d/group_settings).
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


class DataGoogleworkspaceGroupSettings(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.dataGoogleworkspaceGroupSettings.DataGoogleworkspaceGroupSettings",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings googleworkspace_group_settings}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        email: builtins.str,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings googleworkspace_group_settings} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa8c98dc9b07d967443fbe8fc66b53a4b35fc6477e3d11d6ff966bc233d8ca3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataGoogleworkspaceGroupSettingsConfig(
            email=email,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowExternalMembers")
    def allow_external_members(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowExternalMembers"))

    @builtins.property
    @jsii.member(jsii_name="allowWebPosting")
    def allow_web_posting(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "allowWebPosting"))

    @builtins.property
    @jsii.member(jsii_name="archiveOnly")
    def archive_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "archiveOnly"))

    @builtins.property
    @jsii.member(jsii_name="customFooterText")
    def custom_footer_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customFooterText"))

    @builtins.property
    @jsii.member(jsii_name="customReplyTo")
    def custom_reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customReplyTo"))

    @builtins.property
    @jsii.member(jsii_name="customRolesEnabledForSettingsToBeMerged")
    def custom_roles_enabled_for_settings_to_be_merged(
        self,
    ) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "customRolesEnabledForSettingsToBeMerged"))

    @builtins.property
    @jsii.member(jsii_name="defaultMessageDenyNotificationText")
    def default_message_deny_notification_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultMessageDenyNotificationText"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="enableCollaborativeInbox")
    def enable_collaborative_inbox(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enableCollaborativeInbox"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="includeCustomFooter")
    def include_custom_footer(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeCustomFooter"))

    @builtins.property
    @jsii.member(jsii_name="includeInGlobalAddressList")
    def include_in_global_address_list(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeInGlobalAddressList"))

    @builtins.property
    @jsii.member(jsii_name="isArchived")
    def is_archived(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "isArchived"))

    @builtins.property
    @jsii.member(jsii_name="membersCanPostAsTheGroup")
    def members_can_post_as_the_group(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "membersCanPostAsTheGroup"))

    @builtins.property
    @jsii.member(jsii_name="messageModerationLevel")
    def message_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageModerationLevel"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="primaryLanguage")
    def primary_language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryLanguage"))

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @builtins.property
    @jsii.member(jsii_name="sendMessageDenyNotification")
    def send_message_deny_notification(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "sendMessageDenyNotification"))

    @builtins.property
    @jsii.member(jsii_name="spamModerationLevel")
    def spam_moderation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spamModerationLevel"))

    @builtins.property
    @jsii.member(jsii_name="whoCanAssistContent")
    def who_can_assist_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanAssistContent"))

    @builtins.property
    @jsii.member(jsii_name="whoCanContactOwner")
    def who_can_contact_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanContactOwner"))

    @builtins.property
    @jsii.member(jsii_name="whoCanDiscoverGroup")
    def who_can_discover_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanDiscoverGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanJoin")
    def who_can_join(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanJoin"))

    @builtins.property
    @jsii.member(jsii_name="whoCanLeaveGroup")
    def who_can_leave_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanLeaveGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateContent")
    def who_can_moderate_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateContent"))

    @builtins.property
    @jsii.member(jsii_name="whoCanModerateMembers")
    def who_can_moderate_members(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanModerateMembers"))

    @builtins.property
    @jsii.member(jsii_name="whoCanPostMessage")
    def who_can_post_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanPostMessage"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewGroup")
    def who_can_view_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewGroup"))

    @builtins.property
    @jsii.member(jsii_name="whoCanViewMembership")
    def who_can_view_membership(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whoCanViewMembership"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499307009e849631b20ad11a7b7c19a71f0157cfd4bb95c5a652e67afd7fbb01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.dataGoogleworkspaceGroupSettings.DataGoogleworkspaceGroupSettingsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "email": "email",
    },
)
class DataGoogleworkspaceGroupSettingsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        email: builtins.str,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: The group's email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0340a19dcf3715e7df9e15d43f751c22bfc053ebbc25dd3f495534350a31cdc5)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
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
    def email(self) -> builtins.str:
        '''The group's email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/d/group_settings#email DataGoogleworkspaceGroupSettings#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleworkspaceGroupSettingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGoogleworkspaceGroupSettings",
    "DataGoogleworkspaceGroupSettingsConfig",
]

publication.publish()

def _typecheckingstub__0fa8c98dc9b07d967443fbe8fc66b53a4b35fc6477e3d11d6ff966bc233d8ca3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    email: builtins.str,
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

def _typecheckingstub__499307009e849631b20ad11a7b7c19a71f0157cfd4bb95c5a652e67afd7fbb01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0340a19dcf3715e7df9e15d43f751c22bfc053ebbc25dd3f495534350a31cdc5(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    email: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
