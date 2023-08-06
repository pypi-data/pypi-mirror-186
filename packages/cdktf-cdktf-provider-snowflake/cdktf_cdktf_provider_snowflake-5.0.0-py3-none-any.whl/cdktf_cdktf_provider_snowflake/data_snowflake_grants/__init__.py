'''
# `data_snowflake_grants`

Refer to the Terraform Registory for docs: [`data_snowflake_grants`](https://www.terraform.io/docs/providers/snowflake/d/grants).
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


class DataSnowflakeGrants(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrants",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/d/grants snowflake_grants}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        future_grants_in: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsIn", typing.Dict[builtins.str, typing.Any]]] = None,
        future_grants_to: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_of: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsOf", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_on: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsOn", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_to: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/d/grants snowflake_grants} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param future_grants_in: future_grants_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_in DataSnowflakeGrants#future_grants_in}
        :param future_grants_to: future_grants_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_to DataSnowflakeGrants#future_grants_to}
        :param grants_of: grants_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_of DataSnowflakeGrants#grants_of}
        :param grants_on: grants_on block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_on DataSnowflakeGrants#grants_on}
        :param grants_to: grants_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_to DataSnowflakeGrants#grants_to}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#id DataSnowflakeGrants#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b9d486bb52c343b1b5722f352df3657bfda918ea5e791dd0b8a85d8c5c58f8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataSnowflakeGrantsConfig(
            future_grants_in=future_grants_in,
            future_grants_to=future_grants_to,
            grants_of=grants_of,
            grants_on=grants_on,
            grants_to=grants_to,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFutureGrantsIn")
    def put_future_grants_in(
        self,
        *,
        database: typing.Optional[builtins.str] = None,
        schema: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsInSchema", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database: Lists all privileges on new (i.e. future) objects of a specified type in the database granted to a role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database DataSnowflakeGrants#database}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema DataSnowflakeGrants#schema}
        '''
        value = DataSnowflakeGrantsFutureGrantsIn(database=database, schema=schema)

        return typing.cast(None, jsii.invoke(self, "putFutureGrantsIn", [value]))

    @jsii.member(jsii_name="putFutureGrantsTo")
    def put_future_grants_to(self, *, role: builtins.str) -> None:
        '''
        :param role: Lists all privileges on new (i.e. future) objects of a specified type in a database or schema granted to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        '''
        value = DataSnowflakeGrantsFutureGrantsTo(role=role)

        return typing.cast(None, jsii.invoke(self, "putFutureGrantsTo", [value]))

    @jsii.member(jsii_name="putGrantsOf")
    def put_grants_of(
        self,
        *,
        role: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role: Lists all users and roles to which the role has been granted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        :param share: Lists all the accounts for the share and indicates the accounts that are using the share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        '''
        value = DataSnowflakeGrantsGrantsOf(role=role, share=share)

        return typing.cast(None, jsii.invoke(self, "putGrantsOf", [value]))

    @jsii.member(jsii_name="putGrantsOn")
    def put_grants_on(
        self,
        *,
        account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_name: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: Object hierarchy to list privileges on. The only valid value is: ACCOUNT. Setting this attribute lists all the account-level (i.e. global) privileges that have been granted to roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#account DataSnowflakeGrants#account}
        :param object_name: Name of object to list privileges on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_name DataSnowflakeGrants#object_name}
        :param object_type: Type of object to list privileges on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_type DataSnowflakeGrants#object_type}
        '''
        value = DataSnowflakeGrantsGrantsOn(
            account=account, object_name=object_name, object_type=object_type
        )

        return typing.cast(None, jsii.invoke(self, "putGrantsOn", [value]))

    @jsii.member(jsii_name="putGrantsTo")
    def put_grants_to(
        self,
        *,
        role: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role: Lists all privileges and roles granted to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        :param share: Lists all the privileges granted to the share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        :param user: Lists all the roles granted to the user. Note that the PUBLIC role, which is automatically available to every user, is not listed Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#user DataSnowflakeGrants#user}
        '''
        value = DataSnowflakeGrantsGrantsTo(role=role, share=share, user=user)

        return typing.cast(None, jsii.invoke(self, "putGrantsTo", [value]))

    @jsii.member(jsii_name="resetFutureGrantsIn")
    def reset_future_grants_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFutureGrantsIn", []))

    @jsii.member(jsii_name="resetFutureGrantsTo")
    def reset_future_grants_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFutureGrantsTo", []))

    @jsii.member(jsii_name="resetGrantsOf")
    def reset_grants_of(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantsOf", []))

    @jsii.member(jsii_name="resetGrantsOn")
    def reset_grants_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantsOn", []))

    @jsii.member(jsii_name="resetGrantsTo")
    def reset_grants_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrantsTo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="futureGrantsIn")
    def future_grants_in(self) -> "DataSnowflakeGrantsFutureGrantsInOutputReference":
        return typing.cast("DataSnowflakeGrantsFutureGrantsInOutputReference", jsii.get(self, "futureGrantsIn"))

    @builtins.property
    @jsii.member(jsii_name="futureGrantsTo")
    def future_grants_to(self) -> "DataSnowflakeGrantsFutureGrantsToOutputReference":
        return typing.cast("DataSnowflakeGrantsFutureGrantsToOutputReference", jsii.get(self, "futureGrantsTo"))

    @builtins.property
    @jsii.member(jsii_name="grants")
    def grants(self) -> "DataSnowflakeGrantsGrantsList":
        return typing.cast("DataSnowflakeGrantsGrantsList", jsii.get(self, "grants"))

    @builtins.property
    @jsii.member(jsii_name="grantsOf")
    def grants_of(self) -> "DataSnowflakeGrantsGrantsOfOutputReference":
        return typing.cast("DataSnowflakeGrantsGrantsOfOutputReference", jsii.get(self, "grantsOf"))

    @builtins.property
    @jsii.member(jsii_name="grantsOn")
    def grants_on(self) -> "DataSnowflakeGrantsGrantsOnOutputReference":
        return typing.cast("DataSnowflakeGrantsGrantsOnOutputReference", jsii.get(self, "grantsOn"))

    @builtins.property
    @jsii.member(jsii_name="grantsTo")
    def grants_to(self) -> "DataSnowflakeGrantsGrantsToOutputReference":
        return typing.cast("DataSnowflakeGrantsGrantsToOutputReference", jsii.get(self, "grantsTo"))

    @builtins.property
    @jsii.member(jsii_name="futureGrantsInInput")
    def future_grants_in_input(
        self,
    ) -> typing.Optional["DataSnowflakeGrantsFutureGrantsIn"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsIn"], jsii.get(self, "futureGrantsInInput"))

    @builtins.property
    @jsii.member(jsii_name="futureGrantsToInput")
    def future_grants_to_input(
        self,
    ) -> typing.Optional["DataSnowflakeGrantsFutureGrantsTo"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsTo"], jsii.get(self, "futureGrantsToInput"))

    @builtins.property
    @jsii.member(jsii_name="grantsOfInput")
    def grants_of_input(self) -> typing.Optional["DataSnowflakeGrantsGrantsOf"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsOf"], jsii.get(self, "grantsOfInput"))

    @builtins.property
    @jsii.member(jsii_name="grantsOnInput")
    def grants_on_input(self) -> typing.Optional["DataSnowflakeGrantsGrantsOn"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsOn"], jsii.get(self, "grantsOnInput"))

    @builtins.property
    @jsii.member(jsii_name="grantsToInput")
    def grants_to_input(self) -> typing.Optional["DataSnowflakeGrantsGrantsTo"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsTo"], jsii.get(self, "grantsToInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b6ab463cb939bc6c4921b2d03f2c3d59205e9bf6c618a3977081d043b71d43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "future_grants_in": "futureGrantsIn",
        "future_grants_to": "futureGrantsTo",
        "grants_of": "grantsOf",
        "grants_on": "grantsOn",
        "grants_to": "grantsTo",
        "id": "id",
    },
)
class DataSnowflakeGrantsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        future_grants_in: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsIn", typing.Dict[builtins.str, typing.Any]]] = None,
        future_grants_to: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_of: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsOf", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_on: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsOn", typing.Dict[builtins.str, typing.Any]]] = None,
        grants_to: typing.Optional[typing.Union["DataSnowflakeGrantsGrantsTo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param future_grants_in: future_grants_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_in DataSnowflakeGrants#future_grants_in}
        :param future_grants_to: future_grants_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_to DataSnowflakeGrants#future_grants_to}
        :param grants_of: grants_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_of DataSnowflakeGrants#grants_of}
        :param grants_on: grants_on block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_on DataSnowflakeGrants#grants_on}
        :param grants_to: grants_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_to DataSnowflakeGrants#grants_to}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#id DataSnowflakeGrants#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(future_grants_in, dict):
            future_grants_in = DataSnowflakeGrantsFutureGrantsIn(**future_grants_in)
        if isinstance(future_grants_to, dict):
            future_grants_to = DataSnowflakeGrantsFutureGrantsTo(**future_grants_to)
        if isinstance(grants_of, dict):
            grants_of = DataSnowflakeGrantsGrantsOf(**grants_of)
        if isinstance(grants_on, dict):
            grants_on = DataSnowflakeGrantsGrantsOn(**grants_on)
        if isinstance(grants_to, dict):
            grants_to = DataSnowflakeGrantsGrantsTo(**grants_to)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf0a4906d3fe6eddb1150c13c7b7f6f05f1947983d097030454b28587eb9166)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument future_grants_in", value=future_grants_in, expected_type=type_hints["future_grants_in"])
            check_type(argname="argument future_grants_to", value=future_grants_to, expected_type=type_hints["future_grants_to"])
            check_type(argname="argument grants_of", value=grants_of, expected_type=type_hints["grants_of"])
            check_type(argname="argument grants_on", value=grants_on, expected_type=type_hints["grants_on"])
            check_type(argname="argument grants_to", value=grants_to, expected_type=type_hints["grants_to"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if future_grants_in is not None:
            self._values["future_grants_in"] = future_grants_in
        if future_grants_to is not None:
            self._values["future_grants_to"] = future_grants_to
        if grants_of is not None:
            self._values["grants_of"] = grants_of
        if grants_on is not None:
            self._values["grants_on"] = grants_on
        if grants_to is not None:
            self._values["grants_to"] = grants_to
        if id is not None:
            self._values["id"] = id

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
    def future_grants_in(self) -> typing.Optional["DataSnowflakeGrantsFutureGrantsIn"]:
        '''future_grants_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_in DataSnowflakeGrants#future_grants_in}
        '''
        result = self._values.get("future_grants_in")
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsIn"], result)

    @builtins.property
    def future_grants_to(self) -> typing.Optional["DataSnowflakeGrantsFutureGrantsTo"]:
        '''future_grants_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#future_grants_to DataSnowflakeGrants#future_grants_to}
        '''
        result = self._values.get("future_grants_to")
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsTo"], result)

    @builtins.property
    def grants_of(self) -> typing.Optional["DataSnowflakeGrantsGrantsOf"]:
        '''grants_of block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_of DataSnowflakeGrants#grants_of}
        '''
        result = self._values.get("grants_of")
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsOf"], result)

    @builtins.property
    def grants_on(self) -> typing.Optional["DataSnowflakeGrantsGrantsOn"]:
        '''grants_on block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_on DataSnowflakeGrants#grants_on}
        '''
        result = self._values.get("grants_on")
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsOn"], result)

    @builtins.property
    def grants_to(self) -> typing.Optional["DataSnowflakeGrantsGrantsTo"]:
        '''grants_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#grants_to DataSnowflakeGrants#grants_to}
        '''
        result = self._values.get("grants_to")
        return typing.cast(typing.Optional["DataSnowflakeGrantsGrantsTo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#id DataSnowflakeGrants#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsIn",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "schema": "schema"},
)
class DataSnowflakeGrantsFutureGrantsIn:
    def __init__(
        self,
        *,
        database: typing.Optional[builtins.str] = None,
        schema: typing.Optional[typing.Union["DataSnowflakeGrantsFutureGrantsInSchema", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database: Lists all privileges on new (i.e. future) objects of a specified type in the database granted to a role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database DataSnowflakeGrants#database}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema DataSnowflakeGrants#schema}
        '''
        if isinstance(schema, dict):
            schema = DataSnowflakeGrantsFutureGrantsInSchema(**schema)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6add772fc9f6e2557f64ed071c05bc8901170952fc3d31d8cae895a579c98d05)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if database is not None:
            self._values["database"] = database
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Lists all privileges on new (i.e. future) objects of a specified type in the database granted to a role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database DataSnowflakeGrants#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional["DataSnowflakeGrantsFutureGrantsInSchema"]:
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema DataSnowflakeGrants#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsInSchema"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsFutureGrantsIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsFutureGrantsInOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsInOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12b6fdb1a1fa344b92ecb7596eda37c97bf9603a106629a2ab76f760a2674eea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        *,
        schema_name: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schema_name: The name of the schema to list all privileges of new (ie. future) objects granted to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema_name DataSnowflakeGrants#schema_name}
        :param database_name: The database in which the scehma resides. Optional when querying a schema in the current database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database_name DataSnowflakeGrants#database_name}
        '''
        value = DataSnowflakeGrantsFutureGrantsInSchema(
            schema_name=schema_name, database_name=database_name
        )

        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "DataSnowflakeGrantsFutureGrantsInSchemaOutputReference":
        return typing.cast("DataSnowflakeGrantsFutureGrantsInSchemaOutputReference", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional["DataSnowflakeGrantsFutureGrantsInSchema"]:
        return typing.cast(typing.Optional["DataSnowflakeGrantsFutureGrantsInSchema"], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c986ce0b2ccb7726cb916cdb4c5e6512e50a611251855546d0c7899964f7e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsFutureGrantsIn]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsFutureGrantsIn], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsFutureGrantsIn],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cdd0c3010c25252ee14b090928587023ed5ca018a5971ccc11219a64ecf3abf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsInSchema",
    jsii_struct_bases=[],
    name_mapping={"schema_name": "schemaName", "database_name": "databaseName"},
)
class DataSnowflakeGrantsFutureGrantsInSchema:
    def __init__(
        self,
        *,
        schema_name: builtins.str,
        database_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schema_name: The name of the schema to list all privileges of new (ie. future) objects granted to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema_name DataSnowflakeGrants#schema_name}
        :param database_name: The database in which the scehma resides. Optional when querying a schema in the current database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database_name DataSnowflakeGrants#database_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67ab974c8d60d60afd154c0111699c31476637362e36c385431fc4c71007bd1b)
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_name": schema_name,
        }
        if database_name is not None:
            self._values["database_name"] = database_name

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The name of the schema to list all privileges of new (ie. future) objects granted to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#schema_name DataSnowflakeGrants#schema_name}
        '''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The database in which the scehma resides. Optional when querying a schema in the current database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#database_name DataSnowflakeGrants#database_name}
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsFutureGrantsInSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsFutureGrantsInSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsInSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a302de6528f30480dd9a3f47e7c8b07317095dc027e0ab95446fb62a6bb8bf3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba13f2114fb4289d53dd13ab3b3548c05b2ea71442f221059a5cd139f5df215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe64932c21b66065007c0db6660fba7c6754c264002223324a63d7f84e53cfe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataSnowflakeGrantsFutureGrantsInSchema]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsFutureGrantsInSchema], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsFutureGrantsInSchema],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34961faea3fc1cae420784bc72ad0847e41ea233fcd7f1b3cf4a997dcc9762e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsTo",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class DataSnowflakeGrantsFutureGrantsTo:
    def __init__(self, *, role: builtins.str) -> None:
        '''
        :param role: Lists all privileges on new (i.e. future) objects of a specified type in a database or schema granted to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62cbddd0dddbbb1aa34b3be4a548a8d20ab655e7446e2792811fa28177828626)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
        }

    @builtins.property
    def role(self) -> builtins.str:
        '''Lists all privileges on new (i.e. future) objects of a specified type in a database or schema granted to the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsFutureGrantsTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsFutureGrantsToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsFutureGrantsToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bf56548dc2c9ec3c5e1dff2f7589f3846b31a584bfb9797bcd7062c20960ba3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80292c76fa4bc0e590d10e2dbf9203c91daf0f8a7e8dd40273b1e5eef82be582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsFutureGrantsTo]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsFutureGrantsTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsFutureGrantsTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3de9fa64d2e4e54003cd08885b19654b8c1604c822aab3012ed17f5e393c08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrants",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataSnowflakeGrantsGrants:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsGrants(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsGrantsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9736895833f0e74f89cf597ff972f86578297fb241b0254e53c85d6671a3c13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataSnowflakeGrantsGrantsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e381e5fdca848632d80e9d78f3497a522fb4daf6fd0578f433316c8cc88218ec)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataSnowflakeGrantsGrantsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b81561afc74a3527c38928dc4b37a9798782534db78b8bc986fcbc986774d77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c340a35685de6c9713a062a4b0e4b1eb3b86acc4c14083e23ebfa4ed62003c74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34634ace5f6d7d32cc4105d3b64ece77ecaa63d02477f8a7ebd8675bea486c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsOf",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "share": "share"},
)
class DataSnowflakeGrantsGrantsOf:
    def __init__(
        self,
        *,
        role: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role: Lists all users and roles to which the role has been granted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        :param share: Lists all the accounts for the share and indicates the accounts that are using the share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95efc5e8313d2bdc6fe257f92f6f248a8672529b18ea534401d5723be8d2bfc4)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument share", value=share, expected_type=type_hints["share"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role
        if share is not None:
            self._values["share"] = share

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Lists all users and roles to which the role has been granted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share(self) -> typing.Optional[builtins.str]:
        '''Lists all the accounts for the share and indicates the accounts that are using the share.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        '''
        result = self._values.get("share")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsGrantsOf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsGrantsOfOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsOfOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0900815e70dab3f8362f553eb0f16757b30b8cb3031b9ee6dc0eec06706641bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetShare")
    def reset_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShare", []))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="shareInput")
    def share_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareInput"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae2af30a2564fda38ab9d559f2e9c233d1596fc72e0ecfebd4ab0d34fdf7051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="share")
    def share(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "share"))

    @share.setter
    def share(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110e0389cb249dd18c2e3ff5f433fc54306da6e090c7b71a36b4658f191553e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "share", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsGrantsOf]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsGrantsOf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsGrantsOf],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f0c37d981aa9b785968fa942d955163016db6d817f781bc52e9ba3d2e8d94d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsOn",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "object_name": "objectName",
        "object_type": "objectType",
    },
)
class DataSnowflakeGrantsGrantsOn:
    def __init__(
        self,
        *,
        account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        object_name: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account: Object hierarchy to list privileges on. The only valid value is: ACCOUNT. Setting this attribute lists all the account-level (i.e. global) privileges that have been granted to roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#account DataSnowflakeGrants#account}
        :param object_name: Name of object to list privileges on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_name DataSnowflakeGrants#object_name}
        :param object_type: Type of object to list privileges on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_type DataSnowflakeGrants#object_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494e1f51c43d12d6d0f22a8cefcc81823594b516338949a3f1172638f3952782)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if object_name is not None:
            self._values["object_name"] = object_name
        if object_type is not None:
            self._values["object_type"] = object_type

    @builtins.property
    def account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Object hierarchy to list privileges on.

        The only valid value is: ACCOUNT. Setting this attribute lists all the account-level (i.e. global) privileges that have been granted to roles.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#account DataSnowflakeGrants#account}
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def object_name(self) -> typing.Optional[builtins.str]:
        '''Name of object to list privileges on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_name DataSnowflakeGrants#object_name}
        '''
        result = self._values.get("object_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_type(self) -> typing.Optional[builtins.str]:
        '''Type of object to list privileges on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#object_type DataSnowflakeGrants#object_type}
        '''
        result = self._values.get("object_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsGrantsOn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsGrantsOnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsOnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52a828ed0e4cd83b2359fe383a2b88857d632795c10d5ea80b11893fbe5a774a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccount")
    def reset_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccount", []))

    @jsii.member(jsii_name="resetObjectName")
    def reset_object_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectName", []))

    @jsii.member(jsii_name="resetObjectType")
    def reset_object_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectType", []))

    @builtins.property
    @jsii.member(jsii_name="accountInput")
    def account_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "accountInput"))

    @builtins.property
    @jsii.member(jsii_name="objectNameInput")
    def object_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeInput")
    def object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "account"))

    @account.setter
    def account(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577cfb629d074b7609a06034630b2d81f7675cedb39f0fdc033897f21c60aeaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="objectName")
    def object_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectName"))

    @object_name.setter
    def object_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d5d5c26c431390d9bb11afe625823508a1606b5970906aeed341837090ff7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectName", value)

    @builtins.property
    @jsii.member(jsii_name="objectType")
    def object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectType"))

    @object_type.setter
    def object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27b5da73672c06c2e01bb0ff7be3502a88d9f5ff0a11fd7709a4ad6dc0db8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsGrantsOn]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsGrantsOn], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsGrantsOn],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9874114891d3c62d1c3cbd63c1004d02ad32c050b0d5350dff3d3b9c04b42183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataSnowflakeGrantsGrantsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e283504259eef30fbd7b63fe519456723a8d58a3aaafe7d22cc7b0d3edda691d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="grantedBy")
    def granted_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantedBy"))

    @builtins.property
    @jsii.member(jsii_name="grantedOn")
    def granted_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantedOn"))

    @builtins.property
    @jsii.member(jsii_name="grantedTo")
    def granted_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grantedTo"))

    @builtins.property
    @jsii.member(jsii_name="granteeName")
    def grantee_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "granteeName"))

    @builtins.property
    @jsii.member(jsii_name="grantOption")
    def grant_option(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "grantOption"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="privilege")
    def privilege(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privilege"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsGrants]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsGrants], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataSnowflakeGrantsGrants]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b8cde1e0660086babbf373477dce6fe7848425d06de49e30d939b286fe4c82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsTo",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "share": "share", "user": "user"},
)
class DataSnowflakeGrantsGrantsTo:
    def __init__(
        self,
        *,
        role: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role: Lists all privileges and roles granted to the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        :param share: Lists all the privileges granted to the share. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        :param user: Lists all the roles granted to the user. Note that the PUBLIC role, which is automatically available to every user, is not listed Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#user DataSnowflakeGrants#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2eedaed67e4ee063f550fc9f66388e5593bcf9159d4c662c2a09cc0dae1434)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument share", value=share, expected_type=type_hints["share"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role
        if share is not None:
            self._values["share"] = share
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Lists all privileges and roles granted to the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#role DataSnowflakeGrants#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share(self) -> typing.Optional[builtins.str]:
        '''Lists all the privileges granted to the share.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#share DataSnowflakeGrants#share}
        '''
        result = self._values.get("share")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''Lists all the roles granted to the user.

        Note that the PUBLIC role, which is automatically available to every user, is not listed

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/d/grants#user DataSnowflakeGrants#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSnowflakeGrantsGrantsTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSnowflakeGrantsGrantsToOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.dataSnowflakeGrants.DataSnowflakeGrantsGrantsToOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c73c3fd916f566ab17cd02c28c3a3f73ffb418ffd3784a8f375eef438b6c45c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetShare")
    def reset_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShare", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="shareInput")
    def share_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b917d8ec1e046e9c117e81ce24b1bf3ed72736e0f128cfab16519af0c4e6e7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="share")
    def share(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "share"))

    @share.setter
    def share(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d737ab07f5a7ad6d61daa9e242cb1ec9501f0d71a7aa55888844f7cc162527ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "share", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2434c36ca400ddafe1272520632c80d61ca4f489f243e14d9cb5ad88f5c80e36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataSnowflakeGrantsGrantsTo]:
        return typing.cast(typing.Optional[DataSnowflakeGrantsGrantsTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataSnowflakeGrantsGrantsTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48af9ca0ba283c2d8c4bc1e78c1efe681adea6f2cd49b2052c175f99c7f6028a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataSnowflakeGrants",
    "DataSnowflakeGrantsConfig",
    "DataSnowflakeGrantsFutureGrantsIn",
    "DataSnowflakeGrantsFutureGrantsInOutputReference",
    "DataSnowflakeGrantsFutureGrantsInSchema",
    "DataSnowflakeGrantsFutureGrantsInSchemaOutputReference",
    "DataSnowflakeGrantsFutureGrantsTo",
    "DataSnowflakeGrantsFutureGrantsToOutputReference",
    "DataSnowflakeGrantsGrants",
    "DataSnowflakeGrantsGrantsList",
    "DataSnowflakeGrantsGrantsOf",
    "DataSnowflakeGrantsGrantsOfOutputReference",
    "DataSnowflakeGrantsGrantsOn",
    "DataSnowflakeGrantsGrantsOnOutputReference",
    "DataSnowflakeGrantsGrantsOutputReference",
    "DataSnowflakeGrantsGrantsTo",
    "DataSnowflakeGrantsGrantsToOutputReference",
]

publication.publish()

def _typecheckingstub__15b9d486bb52c343b1b5722f352df3657bfda918ea5e791dd0b8a85d8c5c58f8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    future_grants_in: typing.Optional[typing.Union[DataSnowflakeGrantsFutureGrantsIn, typing.Dict[builtins.str, typing.Any]]] = None,
    future_grants_to: typing.Optional[typing.Union[DataSnowflakeGrantsFutureGrantsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_of: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsOf, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_on: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsOn, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_to: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b9b6ab463cb939bc6c4921b2d03f2c3d59205e9bf6c618a3977081d043b71d43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf0a4906d3fe6eddb1150c13c7b7f6f05f1947983d097030454b28587eb9166(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    future_grants_in: typing.Optional[typing.Union[DataSnowflakeGrantsFutureGrantsIn, typing.Dict[builtins.str, typing.Any]]] = None,
    future_grants_to: typing.Optional[typing.Union[DataSnowflakeGrantsFutureGrantsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_of: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsOf, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_on: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsOn, typing.Dict[builtins.str, typing.Any]]] = None,
    grants_to: typing.Optional[typing.Union[DataSnowflakeGrantsGrantsTo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6add772fc9f6e2557f64ed071c05bc8901170952fc3d31d8cae895a579c98d05(
    *,
    database: typing.Optional[builtins.str] = None,
    schema: typing.Optional[typing.Union[DataSnowflakeGrantsFutureGrantsInSchema, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b6fdb1a1fa344b92ecb7596eda37c97bf9603a106629a2ab76f760a2674eea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c986ce0b2ccb7726cb916cdb4c5e6512e50a611251855546d0c7899964f7e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cdd0c3010c25252ee14b090928587023ed5ca018a5971ccc11219a64ecf3abf(
    value: typing.Optional[DataSnowflakeGrantsFutureGrantsIn],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ab974c8d60d60afd154c0111699c31476637362e36c385431fc4c71007bd1b(
    *,
    schema_name: builtins.str,
    database_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a302de6528f30480dd9a3f47e7c8b07317095dc027e0ab95446fb62a6bb8bf3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba13f2114fb4289d53dd13ab3b3548c05b2ea71442f221059a5cd139f5df215(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe64932c21b66065007c0db6660fba7c6754c264002223324a63d7f84e53cfe7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34961faea3fc1cae420784bc72ad0847e41ea233fcd7f1b3cf4a997dcc9762e0(
    value: typing.Optional[DataSnowflakeGrantsFutureGrantsInSchema],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62cbddd0dddbbb1aa34b3be4a548a8d20ab655e7446e2792811fa28177828626(
    *,
    role: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf56548dc2c9ec3c5e1dff2f7589f3846b31a584bfb9797bcd7062c20960ba3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80292c76fa4bc0e590d10e2dbf9203c91daf0f8a7e8dd40273b1e5eef82be582(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3de9fa64d2e4e54003cd08885b19654b8c1604c822aab3012ed17f5e393c08(
    value: typing.Optional[DataSnowflakeGrantsFutureGrantsTo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9736895833f0e74f89cf597ff972f86578297fb241b0254e53c85d6671a3c13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e381e5fdca848632d80e9d78f3497a522fb4daf6fd0578f433316c8cc88218ec(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b81561afc74a3527c38928dc4b37a9798782534db78b8bc986fcbc986774d77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c340a35685de6c9713a062a4b0e4b1eb3b86acc4c14083e23ebfa4ed62003c74(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34634ace5f6d7d32cc4105d3b64ece77ecaa63d02477f8a7ebd8675bea486c28(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95efc5e8313d2bdc6fe257f92f6f248a8672529b18ea534401d5723be8d2bfc4(
    *,
    role: typing.Optional[builtins.str] = None,
    share: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0900815e70dab3f8362f553eb0f16757b30b8cb3031b9ee6dc0eec06706641bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae2af30a2564fda38ab9d559f2e9c233d1596fc72e0ecfebd4ab0d34fdf7051(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110e0389cb249dd18c2e3ff5f433fc54306da6e090c7b71a36b4658f191553e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f0c37d981aa9b785968fa942d955163016db6d817f781bc52e9ba3d2e8d94d(
    value: typing.Optional[DataSnowflakeGrantsGrantsOf],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494e1f51c43d12d6d0f22a8cefcc81823594b516338949a3f1172638f3952782(
    *,
    account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    object_name: typing.Optional[builtins.str] = None,
    object_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a828ed0e4cd83b2359fe383a2b88857d632795c10d5ea80b11893fbe5a774a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577cfb629d074b7609a06034630b2d81f7675cedb39f0fdc033897f21c60aeaf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d5d5c26c431390d9bb11afe625823508a1606b5970906aeed341837090ff7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27b5da73672c06c2e01bb0ff7be3502a88d9f5ff0a11fd7709a4ad6dc0db8c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9874114891d3c62d1c3cbd63c1004d02ad32c050b0d5350dff3d3b9c04b42183(
    value: typing.Optional[DataSnowflakeGrantsGrantsOn],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e283504259eef30fbd7b63fe519456723a8d58a3aaafe7d22cc7b0d3edda691d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b8cde1e0660086babbf373477dce6fe7848425d06de49e30d939b286fe4c82(
    value: typing.Optional[DataSnowflakeGrantsGrants],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2eedaed67e4ee063f550fc9f66388e5593bcf9159d4c662c2a09cc0dae1434(
    *,
    role: typing.Optional[builtins.str] = None,
    share: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c73c3fd916f566ab17cd02c28c3a3f73ffb418ffd3784a8f375eef438b6c45c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b917d8ec1e046e9c117e81ce24b1bf3ed72736e0f128cfab16519af0c4e6e7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d737ab07f5a7ad6d61daa9e242cb1ec9501f0d71a7aa55888844f7cc162527ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2434c36ca400ddafe1272520632c80d61ca4f489f243e14d9cb5ad88f5c80e36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48af9ca0ba283c2d8c4bc1e78c1efe681adea6f2cd49b2052c175f99c7f6028a(
    value: typing.Optional[DataSnowflakeGrantsGrantsTo],
) -> None:
    """Type checking stubs"""
    pass
