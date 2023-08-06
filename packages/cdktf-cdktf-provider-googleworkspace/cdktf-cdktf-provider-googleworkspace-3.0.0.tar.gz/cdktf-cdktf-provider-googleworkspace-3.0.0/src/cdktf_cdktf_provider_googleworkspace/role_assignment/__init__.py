'''
# `googleworkspace_role_assignment`

Refer to the Terraform Registory for docs: [`googleworkspace_role_assignment`](https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment).
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


class RoleAssignment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.roleAssignment.RoleAssignment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment googleworkspace_role_assignment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assigned_to: builtins.str,
        role_id: builtins.str,
        org_unit_id: typing.Optional[builtins.str] = None,
        scope_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment googleworkspace_role_assignment} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param assigned_to: The unique ID of the user this role is assigned to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#assigned_to RoleAssignment#assigned_to}
        :param role_id: The ID of the role that is assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#role_id RoleAssignment#role_id}
        :param org_unit_id: If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this role is restricted to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#org_unit_id RoleAssignment#org_unit_id}
        :param scope_type: Defaults to ``CUSTOMER``. The scope in which this role is assigned. Valid values are : - ``CUSTOMER`` - ``ORG_UNIT``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#scope_type RoleAssignment#scope_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe78321c028b57f999cf44a6ac38004ddedc7abfee18b4b0bba25cf92c70aa01)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = RoleAssignmentConfig(
            assigned_to=assigned_to,
            role_id=role_id,
            org_unit_id=org_unit_id,
            scope_type=scope_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetOrgUnitId")
    def reset_org_unit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgUnitId", []))

    @jsii.member(jsii_name="resetScopeType")
    def reset_scope_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScopeType", []))

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
    @jsii.member(jsii_name="assignedToInput")
    def assigned_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assignedToInput"))

    @builtins.property
    @jsii.member(jsii_name="orgUnitIdInput")
    def org_unit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orgUnitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleIdInput")
    def role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeTypeInput")
    def scope_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="assignedTo")
    def assigned_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assignedTo"))

    @assigned_to.setter
    def assigned_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83bdf86d842a75b11be2fc9ffd880c0f6658720e4febcf630492570019b44b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignedTo", value)

    @builtins.property
    @jsii.member(jsii_name="orgUnitId")
    def org_unit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgUnitId"))

    @org_unit_id.setter
    def org_unit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3faaccc3f56d1f3ae3b84bb09f56a9534256e40afd58de163f1a5965d8b2cac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgUnitId", value)

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @role_id.setter
    def role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5c8e9d3162e1fd25cd5a76c7a913256ea1075be26055ef3b5665241bfed355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleId", value)

    @builtins.property
    @jsii.member(jsii_name="scopeType")
    def scope_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scopeType"))

    @scope_type.setter
    def scope_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe8da3a8ac65364453fd44d06f431d08053c71e6ba3e797899d5339174ec6b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.roleAssignment.RoleAssignmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "assigned_to": "assignedTo",
        "role_id": "roleId",
        "org_unit_id": "orgUnitId",
        "scope_type": "scopeType",
    },
)
class RoleAssignmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        assigned_to: builtins.str,
        role_id: builtins.str,
        org_unit_id: typing.Optional[builtins.str] = None,
        scope_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param assigned_to: The unique ID of the user this role is assigned to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#assigned_to RoleAssignment#assigned_to}
        :param role_id: The ID of the role that is assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#role_id RoleAssignment#role_id}
        :param org_unit_id: If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this role is restricted to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#org_unit_id RoleAssignment#org_unit_id}
        :param scope_type: Defaults to ``CUSTOMER``. The scope in which this role is assigned. Valid values are : - ``CUSTOMER`` - ``ORG_UNIT``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#scope_type RoleAssignment#scope_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da5b2725ba89d2618ee7d93b3b77332fc7d669083b9bac176f99558297d3d55)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument assigned_to", value=assigned_to, expected_type=type_hints["assigned_to"])
            check_type(argname="argument role_id", value=role_id, expected_type=type_hints["role_id"])
            check_type(argname="argument org_unit_id", value=org_unit_id, expected_type=type_hints["org_unit_id"])
            check_type(argname="argument scope_type", value=scope_type, expected_type=type_hints["scope_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assigned_to": assigned_to,
            "role_id": role_id,
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
        if org_unit_id is not None:
            self._values["org_unit_id"] = org_unit_id
        if scope_type is not None:
            self._values["scope_type"] = scope_type

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
    def assigned_to(self) -> builtins.str:
        '''The unique ID of the user this role is assigned to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#assigned_to RoleAssignment#assigned_to}
        '''
        result = self._values.get("assigned_to")
        assert result is not None, "Required property 'assigned_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_id(self) -> builtins.str:
        '''The ID of the role that is assigned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#role_id RoleAssignment#role_id}
        '''
        result = self._values.get("role_id")
        assert result is not None, "Required property 'role_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_unit_id(self) -> typing.Optional[builtins.str]:
        '''If the role is restricted to an organization unit, this contains the ID for the organization unit the exercise of this role is restricted to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#org_unit_id RoleAssignment#org_unit_id}
        '''
        result = self._values.get("org_unit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope_type(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``CUSTOMER``. The scope in which this role is assigned. Valid values are : - ``CUSTOMER`` - ``ORG_UNIT``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/role_assignment#scope_type RoleAssignment#scope_type}
        '''
        result = self._values.get("scope_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleAssignmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RoleAssignment",
    "RoleAssignmentConfig",
]

publication.publish()

def _typecheckingstub__fe78321c028b57f999cf44a6ac38004ddedc7abfee18b4b0bba25cf92c70aa01(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assigned_to: builtins.str,
    role_id: builtins.str,
    org_unit_id: typing.Optional[builtins.str] = None,
    scope_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d83bdf86d842a75b11be2fc9ffd880c0f6658720e4febcf630492570019b44b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3faaccc3f56d1f3ae3b84bb09f56a9534256e40afd58de163f1a5965d8b2cac0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5c8e9d3162e1fd25cd5a76c7a913256ea1075be26055ef3b5665241bfed355(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe8da3a8ac65364453fd44d06f431d08053c71e6ba3e797899d5339174ec6b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da5b2725ba89d2618ee7d93b3b77332fc7d669083b9bac176f99558297d3d55(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    assigned_to: builtins.str,
    role_id: builtins.str,
    org_unit_id: typing.Optional[builtins.str] = None,
    scope_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
