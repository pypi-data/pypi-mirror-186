'''
# `googleworkspace_schema`

Refer to the Terraform Registory for docs: [`googleworkspace_schema`](https://www.terraform.io/docs/providers/googleworkspace/r/schema).
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


class Schema(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.schema.Schema",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema googleworkspace_schema}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        fields: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SchemaFields", typing.Dict[builtins.str, typing.Any]]]],
        schema_name: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SchemaTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema googleworkspace_schema} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param fields: fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#fields Schema#fields}
        :param schema_name: The schema's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#schema_name Schema#schema_name}
        :param display_name: Display name for the schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#display_name Schema#display_name}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#timeouts Schema#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f57e409bc9e180388903f9cbfa4a217bc249c9d49ff06fa6f5beb5e9f17ce6c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SchemaConfig(
            fields=fields,
            schema_name=schema_name,
            display_name=display_name,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putFields")
    def put_fields(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SchemaFields", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f906152db91100e4e062b394bcabe1f04699aaef950bbf5790cb8c7c54bc0db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFields", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#create Schema#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#delete Schema#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#update Schema#update}.
        '''
        value = SchemaTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="fields")
    def fields(self) -> "SchemaFieldsList":
        return typing.cast("SchemaFieldsList", jsii.get(self, "fields"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SchemaTimeoutsOutputReference":
        return typing.cast("SchemaTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SchemaFields"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SchemaFields"]]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SchemaTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SchemaTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c946acdf41bc3f8a2584104525d6346831df0572d69d1ef116dece6113c073dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6212eb55f07f58c9d081432c93134995c40902ea1d7de60a0ca54e1c7367cfaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "fields": "fields",
        "schema_name": "schemaName",
        "display_name": "displayName",
        "timeouts": "timeouts",
    },
)
class SchemaConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        fields: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SchemaFields", typing.Dict[builtins.str, typing.Any]]]],
        schema_name: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SchemaTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param fields: fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#fields Schema#fields}
        :param schema_name: The schema's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#schema_name Schema#schema_name}
        :param display_name: Display name for the schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#display_name Schema#display_name}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#timeouts Schema#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SchemaTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ff78547b6eff3387c9f5ef2f7fd8f25e395e58f78942737836def977d5428d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fields": fields,
            "schema_name": schema_name,
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def fields(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SchemaFields"]]:
        '''fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#fields Schema#fields}
        '''
        result = self._values.get("fields")
        assert result is not None, "Required property 'fields' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SchemaFields"]], result)

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The schema's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#schema_name Schema#schema_name}
        '''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Display name for the schema.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#display_name Schema#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SchemaTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#timeouts Schema#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SchemaTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaFields",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "field_type": "fieldType",
        "display_name": "displayName",
        "indexed": "indexed",
        "multi_valued": "multiValued",
        "numeric_indexing_spec": "numericIndexingSpec",
        "read_access_type": "readAccessType",
    },
)
class SchemaFields:
    def __init__(
        self,
        *,
        field_name: builtins.str,
        field_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        indexed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        multi_valued: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        numeric_indexing_spec: typing.Optional[typing.Union["SchemaFieldsNumericIndexingSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        read_access_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param field_name: The name of the field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#field_name Schema#field_name}
        :param field_type: The type of the field. Acceptable values are: - ``BOOL`` - ``DATE`` - ``DOUBLE`` - ``EMAIL`` - ``INT64`` - ``PHONE`` - ``STRING``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#field_type Schema#field_type}
        :param display_name: Display Name of the field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#display_name Schema#display_name}
        :param indexed: Defaults to ``true``. Boolean specifying whether the field is indexed or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#indexed Schema#indexed}
        :param multi_valued: Defaults to ``false``. A boolean specifying whether this is a multi-valued field or not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#multi_valued Schema#multi_valued}
        :param numeric_indexing_spec: numeric_indexing_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#numeric_indexing_spec Schema#numeric_indexing_spec}
        :param read_access_type: Defaults to ``ALL_DOMAIN_USERS``. Specifies who can view values of this field. See Retrieve users as a non-administrator for more information. Acceptable values are: - ``ADMINS_AND_SELF`` - ``ALL_DOMAIN_USERS`` Note: It may take up to 24 hours for changes to this field to be reflected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#read_access_type Schema#read_access_type}
        '''
        if isinstance(numeric_indexing_spec, dict):
            numeric_indexing_spec = SchemaFieldsNumericIndexingSpec(**numeric_indexing_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8934ed407a451b552ff825d45ee02bd93c849440bb3a94e35e7bef74bb93041f)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument field_type", value=field_type, expected_type=type_hints["field_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument indexed", value=indexed, expected_type=type_hints["indexed"])
            check_type(argname="argument multi_valued", value=multi_valued, expected_type=type_hints["multi_valued"])
            check_type(argname="argument numeric_indexing_spec", value=numeric_indexing_spec, expected_type=type_hints["numeric_indexing_spec"])
            check_type(argname="argument read_access_type", value=read_access_type, expected_type=type_hints["read_access_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "field_type": field_type,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if indexed is not None:
            self._values["indexed"] = indexed
        if multi_valued is not None:
            self._values["multi_valued"] = multi_valued
        if numeric_indexing_spec is not None:
            self._values["numeric_indexing_spec"] = numeric_indexing_spec
        if read_access_type is not None:
            self._values["read_access_type"] = read_access_type

    @builtins.property
    def field_name(self) -> builtins.str:
        '''The name of the field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#field_name Schema#field_name}
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_type(self) -> builtins.str:
        '''The type of the field. Acceptable values are:  - ``BOOL`` - ``DATE`` - ``DOUBLE`` - ``EMAIL`` - ``INT64`` - ``PHONE`` - ``STRING``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#field_type Schema#field_type}
        '''
        result = self._values.get("field_type")
        assert result is not None, "Required property 'field_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Display Name of the field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#display_name Schema#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def indexed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to ``true``. Boolean specifying whether the field is indexed or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#indexed Schema#indexed}
        '''
        result = self._values.get("indexed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def multi_valued(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Defaults to ``false``. A boolean specifying whether this is a multi-valued field or not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#multi_valued Schema#multi_valued}
        '''
        result = self._values.get("multi_valued")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def numeric_indexing_spec(
        self,
    ) -> typing.Optional["SchemaFieldsNumericIndexingSpec"]:
        '''numeric_indexing_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#numeric_indexing_spec Schema#numeric_indexing_spec}
        '''
        result = self._values.get("numeric_indexing_spec")
        return typing.cast(typing.Optional["SchemaFieldsNumericIndexingSpec"], result)

    @builtins.property
    def read_access_type(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``ALL_DOMAIN_USERS``.

        Specifies who can view values of this field. See Retrieve users as a non-administrator for more information. Acceptable values are:

        - ``ADMINS_AND_SELF``
        - ``ALL_DOMAIN_USERS``
          Note: It may take up to 24 hours for changes to this field to be reflected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#read_access_type Schema#read_access_type}
        '''
        result = self._values.get("read_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SchemaFieldsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaFieldsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3c360a374efccc442b5e203d7606d2a3219c0862cd04d4af190bd775b673879)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SchemaFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f42104b82bd5135c25d4e58c3a2ceb1098c00083279c98d38623cf8521e16b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SchemaFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1343d5b3e3b824622c50f1744ddc3cfa39f9075a7dddab0910a20d465efa5c49)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c14a5490c63bbd9440ccf4a4af81659b5fc656b0dcb81c6fa44df4ba4fdc415)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fee567c61162f92dd3620093fdf0fca67be48d182da1fb5baec481436bd83e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SchemaFields]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SchemaFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SchemaFields]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d705836b8fabf91cd27281548f5b2a1320c8a0cb9fbda36f5eca9a5e059af535)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaFieldsNumericIndexingSpec",
    jsii_struct_bases=[],
    name_mapping={"max_value": "maxValue", "min_value": "minValue"},
)
class SchemaFieldsNumericIndexingSpec:
    def __init__(
        self,
        *,
        max_value: typing.Optional[jsii.Number] = None,
        min_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_value: Maximum value of this field. This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#max_value Schema#max_value}
        :param min_value: Minimum value of this field. This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#min_value Schema#min_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f01c5833492802fc650c270f65de994b60e6bc1776456ed3dca56dbf4225e1)
            check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
            check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_value is not None:
            self._values["max_value"] = max_value
        if min_value is not None:
            self._values["min_value"] = min_value

    @builtins.property
    def max_value(self) -> typing.Optional[jsii.Number]:
        '''Maximum value of this field.

        This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#max_value Schema#max_value}
        '''
        result = self._values.get("max_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_value(self) -> typing.Optional[jsii.Number]:
        '''Minimum value of this field.

        This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#min_value Schema#min_value}
        '''
        result = self._values.get("min_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaFieldsNumericIndexingSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SchemaFieldsNumericIndexingSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaFieldsNumericIndexingSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__698ecf84a29925b88f4ececa98ca80e13fcde1f7ec5a6e160a65b7cea58b97d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxValue")
    def reset_max_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxValue", []))

    @jsii.member(jsii_name="resetMinValue")
    def reset_min_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinValue", []))

    @builtins.property
    @jsii.member(jsii_name="maxValueInput")
    def max_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxValueInput"))

    @builtins.property
    @jsii.member(jsii_name="minValueInput")
    def min_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minValueInput"))

    @builtins.property
    @jsii.member(jsii_name="maxValue")
    def max_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxValue"))

    @max_value.setter
    def max_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e0b99d27645fb051b96ee15ed93ed5a0aa75c2623db4414def4eaf46652fb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxValue", value)

    @builtins.property
    @jsii.member(jsii_name="minValue")
    def min_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minValue"))

    @min_value.setter
    def min_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1817963ef890917270ab5c39f1bbe747d9550cae80e1481701b76fa5fee28065)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SchemaFieldsNumericIndexingSpec]:
        return typing.cast(typing.Optional[SchemaFieldsNumericIndexingSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SchemaFieldsNumericIndexingSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8580a65522488fbb1999d9b2c01990c786bbbf21aebb2a82c3bd50a7bbc4a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SchemaFieldsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaFieldsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bb50dc45e3a95500a5e994fcec2cc4056a52fe762ac4933fcd81369e890e029)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNumericIndexingSpec")
    def put_numeric_indexing_spec(
        self,
        *,
        max_value: typing.Optional[jsii.Number] = None,
        min_value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_value: Maximum value of this field. This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#max_value Schema#max_value}
        :param min_value: Minimum value of this field. This is meant to be indicative rather than enforced. Values outside this range will still be indexed, but search may not be as performant. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#min_value Schema#min_value}
        '''
        value = SchemaFieldsNumericIndexingSpec(
            max_value=max_value, min_value=min_value
        )

        return typing.cast(None, jsii.invoke(self, "putNumericIndexingSpec", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetIndexed")
    def reset_indexed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexed", []))

    @jsii.member(jsii_name="resetMultiValued")
    def reset_multi_valued(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiValued", []))

    @jsii.member(jsii_name="resetNumericIndexingSpec")
    def reset_numeric_indexing_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumericIndexingSpec", []))

    @jsii.member(jsii_name="resetReadAccessType")
    def reset_read_access_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadAccessType", []))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="fieldId")
    def field_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldId"))

    @builtins.property
    @jsii.member(jsii_name="numericIndexingSpec")
    def numeric_indexing_spec(self) -> SchemaFieldsNumericIndexingSpecOutputReference:
        return typing.cast(SchemaFieldsNumericIndexingSpecOutputReference, jsii.get(self, "numericIndexingSpec"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldNameInput")
    def field_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldTypeInput")
    def field_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="indexedInput")
    def indexed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "indexedInput"))

    @builtins.property
    @jsii.member(jsii_name="multiValuedInput")
    def multi_valued_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "multiValuedInput"))

    @builtins.property
    @jsii.member(jsii_name="numericIndexingSpecInput")
    def numeric_indexing_spec_input(
        self,
    ) -> typing.Optional[SchemaFieldsNumericIndexingSpec]:
        return typing.cast(typing.Optional[SchemaFieldsNumericIndexingSpec], jsii.get(self, "numericIndexingSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="readAccessTypeInput")
    def read_access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readAccessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c757f4d4aad2fa6618532a28ea3b74ef338c04bbd9b7df1a85154a5a8dc9057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="fieldName")
    def field_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldName"))

    @field_name.setter
    def field_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e63cff10cbd470bc78ef034fd154217f0e0831fb58b3184c02ec2803d4b87e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldName", value)

    @builtins.property
    @jsii.member(jsii_name="fieldType")
    def field_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldType"))

    @field_type.setter
    def field_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a54169a4f2665e055e3273ca2318f1dae90aad583652a93a025f683ccb87f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldType", value)

    @builtins.property
    @jsii.member(jsii_name="indexed")
    def indexed(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "indexed"))

    @indexed.setter
    def indexed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eb6b6b1933c649a6fd130706c274d6dce3538a3b41c54c48ba5d43b8f029603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexed", value)

    @builtins.property
    @jsii.member(jsii_name="multiValued")
    def multi_valued(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "multiValued"))

    @multi_valued.setter
    def multi_valued(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26e84fb64ec7a0fdc827059fdfe93f57231007478f6afc1897daf78e86944f26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiValued", value)

    @builtins.property
    @jsii.member(jsii_name="readAccessType")
    def read_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readAccessType"))

    @read_access_type.setter
    def read_access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a406aa8d145e3f2aaeabd125301307f18457268c8da0b0d31ef06a2e89fe99cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readAccessType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SchemaFields, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SchemaFields, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SchemaFields, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e68dca953f375ff6b1e3574b2fe99ad4c5f37449c00439ccd6b1aa35b3aac8b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class SchemaTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#create Schema#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#delete Schema#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#update Schema#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cf2df377dbc9b06f603d16ad9e766ea4035886d1fa1c8c4cf884f796796d892)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#create Schema#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#delete Schema#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/schema#update Schema#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SchemaTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.schema.SchemaTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c9cb56025dbeb989630b14537e38521a31eeb97590db5efd41fc23952c3f2ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6218d4ffcdb8c4351fead4032c12671f18731c8f08447f5ad53bcf2bb539cbf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ab233cc6f4ce232056c181b71a5fc3160bcb3a6ec7fc15e66c759471275db41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f43bfcb9de674b29ff65cec2b14655ba87d6fe72e4027a9ff34717263002a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SchemaTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SchemaTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SchemaTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0e9b16e453e0b68cc84bca628dd4670ff3587531caa2f58fc8b724938002d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Schema",
    "SchemaConfig",
    "SchemaFields",
    "SchemaFieldsList",
    "SchemaFieldsNumericIndexingSpec",
    "SchemaFieldsNumericIndexingSpecOutputReference",
    "SchemaFieldsOutputReference",
    "SchemaTimeouts",
    "SchemaTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6f57e409bc9e180388903f9cbfa4a217bc249c9d49ff06fa6f5beb5e9f17ce6c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    fields: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SchemaFields, typing.Dict[builtins.str, typing.Any]]]],
    schema_name: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SchemaTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__f906152db91100e4e062b394bcabe1f04699aaef950bbf5790cb8c7c54bc0db4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SchemaFields, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c946acdf41bc3f8a2584104525d6346831df0572d69d1ef116dece6113c073dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6212eb55f07f58c9d081432c93134995c40902ea1d7de60a0ca54e1c7367cfaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ff78547b6eff3387c9f5ef2f7fd8f25e395e58f78942737836def977d5428d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fields: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SchemaFields, typing.Dict[builtins.str, typing.Any]]]],
    schema_name: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SchemaTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8934ed407a451b552ff825d45ee02bd93c849440bb3a94e35e7bef74bb93041f(
    *,
    field_name: builtins.str,
    field_type: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    indexed: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    multi_valued: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    numeric_indexing_spec: typing.Optional[typing.Union[SchemaFieldsNumericIndexingSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    read_access_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c360a374efccc442b5e203d7606d2a3219c0862cd04d4af190bd775b673879(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f42104b82bd5135c25d4e58c3a2ceb1098c00083279c98d38623cf8521e16b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1343d5b3e3b824622c50f1744ddc3cfa39f9075a7dddab0910a20d465efa5c49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c14a5490c63bbd9440ccf4a4af81659b5fc656b0dcb81c6fa44df4ba4fdc415(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fee567c61162f92dd3620093fdf0fca67be48d182da1fb5baec481436bd83e5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d705836b8fabf91cd27281548f5b2a1320c8a0cb9fbda36f5eca9a5e059af535(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SchemaFields]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f01c5833492802fc650c270f65de994b60e6bc1776456ed3dca56dbf4225e1(
    *,
    max_value: typing.Optional[jsii.Number] = None,
    min_value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__698ecf84a29925b88f4ececa98ca80e13fcde1f7ec5a6e160a65b7cea58b97d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e0b99d27645fb051b96ee15ed93ed5a0aa75c2623db4414def4eaf46652fb5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1817963ef890917270ab5c39f1bbe747d9550cae80e1481701b76fa5fee28065(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8580a65522488fbb1999d9b2c01990c786bbbf21aebb2a82c3bd50a7bbc4a8(
    value: typing.Optional[SchemaFieldsNumericIndexingSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb50dc45e3a95500a5e994fcec2cc4056a52fe762ac4933fcd81369e890e029(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c757f4d4aad2fa6618532a28ea3b74ef338c04bbd9b7df1a85154a5a8dc9057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e63cff10cbd470bc78ef034fd154217f0e0831fb58b3184c02ec2803d4b87e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a54169a4f2665e055e3273ca2318f1dae90aad583652a93a025f683ccb87f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eb6b6b1933c649a6fd130706c274d6dce3538a3b41c54c48ba5d43b8f029603(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26e84fb64ec7a0fdc827059fdfe93f57231007478f6afc1897daf78e86944f26(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a406aa8d145e3f2aaeabd125301307f18457268c8da0b0d31ef06a2e89fe99cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e68dca953f375ff6b1e3574b2fe99ad4c5f37449c00439ccd6b1aa35b3aac8b3(
    value: typing.Optional[typing.Union[SchemaFields, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cf2df377dbc9b06f603d16ad9e766ea4035886d1fa1c8c4cf884f796796d892(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9cb56025dbeb989630b14537e38521a31eeb97590db5efd41fc23952c3f2ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6218d4ffcdb8c4351fead4032c12671f18731c8f08447f5ad53bcf2bb539cbf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ab233cc6f4ce232056c181b71a5fc3160bcb3a6ec7fc15e66c759471275db41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f43bfcb9de674b29ff65cec2b14655ba87d6fe72e4027a9ff34717263002a37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0e9b16e453e0b68cc84bca628dd4670ff3587531caa2f58fc8b724938002d6(
    value: typing.Optional[typing.Union[SchemaTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
