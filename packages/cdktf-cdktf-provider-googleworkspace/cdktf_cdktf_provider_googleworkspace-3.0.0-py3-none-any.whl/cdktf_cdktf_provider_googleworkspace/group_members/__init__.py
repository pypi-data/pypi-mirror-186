'''
# `googleworkspace_group_members`

Refer to the Terraform Registory for docs: [`googleworkspace_group_members`](https://www.terraform.io/docs/providers/googleworkspace/r/group_members).
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


class GroupMembers(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.groupMembers.GroupMembers",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members googleworkspace_group_members}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        group_id: builtins.str,
        members: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GroupMembersMembers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members googleworkspace_group_members} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#group_id GroupMembers#group_id}
        :param members: members block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#members GroupMembers#members}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98bdeab906eb606ee9cae66f5695ba2abc83bf5e1f651447f63bbc596364231)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GroupMembersConfig(
            group_id=group_id,
            members=members,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putMembers")
    def put_members(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GroupMembersMembers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe636fded937c94681ec16fec9e860036dd80a8eccc5d59cff636308322c867)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMembers", [value]))

    @jsii.member(jsii_name="resetMembers")
    def reset_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> "GroupMembersMembersList":
        return typing.cast("GroupMembersMembersList", jsii.get(self, "members"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GroupMembersMembers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GroupMembersMembers"]]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cac95223b8c94aa9ba13be68029734731152dd7063c94c875f5a3e2ecad162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.groupMembers.GroupMembersConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_id": "groupId",
        "members": "members",
    },
)
class GroupMembersConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_id: builtins.str,
        members: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GroupMembersMembers", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_id: Identifies the group in the API request. The value can be the group's email address, group alias, or the unique group ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#group_id GroupMembers#group_id}
        :param members: members block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#members GroupMembers#members}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7324ea6ab584c1852e3d0b497aec340920bc1adc90f83313de2994669286ca9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
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
        if members is not None:
            self._values["members"] = members

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
    def group_id(self) -> builtins.str:
        '''Identifies the group in the API request.

        The value can be the group's email address, group alias, or the unique group ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#group_id GroupMembers#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def members(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GroupMembersMembers"]]]:
        '''members block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#members GroupMembers#members}
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GroupMembersMembers"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupMembersConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.groupMembers.GroupMembersMembers",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "delivery_settings": "deliverySettings",
        "role": "role",
        "type": "type",
    },
)
class GroupMembersMembers:
    def __init__(
        self,
        *,
        email: builtins.str,
        delivery_settings: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: The member's email address. A member can be a user or another group. This property isrequired when adding a member to a group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API automatically reflects the email address changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#email GroupMembers#email}
        :param delivery_settings: Defaults to ``ALL_MAIL``. Defines mail delivery preferences of member. Acceptable values are: - ``ALL_MAIL``: All messages, delivered as soon as they arrive. - ``DAILY``: No more than one message a day. - ``DIGEST``: Up to 25 messages bundled into a single message. - ``DISABLED``: Remove subscription. - ``NONE``: No messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#delivery_settings GroupMembers#delivery_settings}
        :param role: Defaults to ``MEMBER``. The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a member of group2, group2 cannot be a member of group1. Acceptable values are: - ``MANAGER``: This role is only available if the Google Groups for Business is enabled using the Admin Console. A ``MANAGER`` role can do everything done by an ``OWNER`` role except make a member an ``OWNER`` or delete the group. A group can have multiple ``MANAGER`` members. - ``MEMBER``: This role can subscribe to a group, view discussion archives, and view the group's membership list. - ``OWNER``: This role can send messages to the group, add or remove members, change member roles, change group's settings, and delete the group. An OWNER must be a member of the group. A group can have more than one OWNER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#role GroupMembers#role}
        :param type: Defaults to ``USER``. The type of group member. Acceptable values are: - ``CUSTOMER``: The member represents all users in a domain. An email address is not returned and the ID returned is the customer ID. - ``GROUP``: The member is another group. - ``USER``: The member is a user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#type GroupMembers#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7965971c3835dfd95742a1ed8eb53ca6c8bfc206a8aa8c299cd59ef2d690feb2)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument delivery_settings", value=delivery_settings, expected_type=type_hints["delivery_settings"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
        }
        if delivery_settings is not None:
            self._values["delivery_settings"] = delivery_settings
        if role is not None:
            self._values["role"] = role
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def email(self) -> builtins.str:
        '''The member's email address.

        A member can be a user or another group. This property isrequired when adding a member to a group. The email must be unique and cannot be an alias of another group. If the email address is changed, the API automatically reflects the email address changes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#email GroupMembers#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_settings(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_MAIL``.

        Defines mail delivery preferences of member. Acceptable values are:

        - ``ALL_MAIL``: All messages, delivered as soon as they arrive.
        - ``DAILY``: No more than one message a day.
        - ``DIGEST``: Up to 25 messages bundled into a single message.
        - ``DISABLED``: Remove subscription.
        - ``NONE``: No messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#delivery_settings GroupMembers#delivery_settings}
        '''
        result = self._values.get("delivery_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``MEMBER``.

        The member's role in a group. The API returns an error for cycles in group memberships. For example, if group1 is a member of group2, group2 cannot be a member of group1. Acceptable values are:

        - ``MANAGER``: This role is only available if the Google Groups for Business is enabled using the Admin Console. A ``MANAGER`` role can do everything done by an ``OWNER`` role except make a member an ``OWNER`` or delete the group. A group can have multiple ``MANAGER`` members.
        - ``MEMBER``: This role can subscribe to a group, view discussion archives, and view the group's membership list.
        - ``OWNER``: This role can send messages to the group, add or remove members, change member roles, change group's settings, and delete the group. An OWNER must be a member of the group. A group can have more than one OWNER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#role GroupMembers#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``USER``.

        The type of group member. Acceptable values are:

        - ``CUSTOMER``: The member represents all users in a domain. An email address is not returned and the ID returned is the customer ID.
        - ``GROUP``: The member is another group.
        - ``USER``: The member is a user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/group_members#type GroupMembers#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupMembersMembers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupMembersMembersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.groupMembers.GroupMembersMembersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__59348f5e2387936001312c26551b893073729a68e7bd72de72ceaf5956415444)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GroupMembersMembersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccff58f374defb85acb0ae5b6c0e4a083ef5a3de253e23e0517ec1a651a86a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GroupMembersMembersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57efb0aae012e5da21dbe895e9a6622a3ea72e9e8ff3764798b31861b131847c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88eceeb21436510961c5124525c7a650753dc1d801e9067edc487e804ab22100)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d17216a25ea5166154631791f403928cd1e8d87a7cff7758dbc0a3ca85899b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GroupMembersMembers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GroupMembersMembers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GroupMembersMembers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564563b5989e3859ba9d6a172f5c3963de485ba517cedde902008b9b1ea72520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GroupMembersMembersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.groupMembers.GroupMembersMembersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8942b50b3365c7a2f53b4ae696adc6949d004bae55a878b7a33560dd256d94bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDeliverySettings")
    def reset_delivery_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliverySettings", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="deliverySettingsInput")
    def delivery_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliverySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="deliverySettings")
    def delivery_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliverySettings"))

    @delivery_settings.setter
    def delivery_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f003e12b8604fe1187ed76d238ee7dc341eefd80794accb0d7d558fe33e1ea71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliverySettings", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad08b643f251fa27d97e9b9b3ad3dd175e4c4be3a7b32a472f36a0d5455ac48d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7757c0af9ad7530f91a0bad4a0987a00e8f724554cb66df6b197b407fcead5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72cd3de5477721535a7885e15cb1f928ba439af3aedcfdc74f4ce3689d3aeb9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupMembersMembers, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupMembersMembers, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupMembersMembers, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6f74ef246e9613b11764b872f63e2ab03f680c26ca4a3d66bf6b54a6bb378a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GroupMembers",
    "GroupMembersConfig",
    "GroupMembersMembers",
    "GroupMembersMembersList",
    "GroupMembersMembersOutputReference",
]

publication.publish()

def _typecheckingstub__a98bdeab906eb606ee9cae66f5695ba2abc83bf5e1f651447f63bbc596364231(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    group_id: builtins.str,
    members: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GroupMembersMembers, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__1fe636fded937c94681ec16fec9e860036dd80a8eccc5d59cff636308322c867(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GroupMembersMembers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cac95223b8c94aa9ba13be68029734731152dd7063c94c875f5a3e2ecad162(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7324ea6ab584c1852e3d0b497aec340920bc1adc90f83313de2994669286ca9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    group_id: builtins.str,
    members: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GroupMembersMembers, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7965971c3835dfd95742a1ed8eb53ca6c8bfc206a8aa8c299cd59ef2d690feb2(
    *,
    email: builtins.str,
    delivery_settings: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59348f5e2387936001312c26551b893073729a68e7bd72de72ceaf5956415444(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccff58f374defb85acb0ae5b6c0e4a083ef5a3de253e23e0517ec1a651a86a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57efb0aae012e5da21dbe895e9a6622a3ea72e9e8ff3764798b31861b131847c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88eceeb21436510961c5124525c7a650753dc1d801e9067edc487e804ab22100(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d17216a25ea5166154631791f403928cd1e8d87a7cff7758dbc0a3ca85899b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564563b5989e3859ba9d6a172f5c3963de485ba517cedde902008b9b1ea72520(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GroupMembersMembers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8942b50b3365c7a2f53b4ae696adc6949d004bae55a878b7a33560dd256d94bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f003e12b8604fe1187ed76d238ee7dc341eefd80794accb0d7d558fe33e1ea71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad08b643f251fa27d97e9b9b3ad3dd175e4c4be3a7b32a472f36a0d5455ac48d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7757c0af9ad7530f91a0bad4a0987a00e8f724554cb66df6b197b407fcead5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72cd3de5477721535a7885e15cb1f928ba439af3aedcfdc74f4ce3689d3aeb9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6f74ef246e9613b11764b872f63e2ab03f680c26ca4a3d66bf6b54a6bb378a(
    value: typing.Optional[typing.Union[GroupMembersMembers, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
