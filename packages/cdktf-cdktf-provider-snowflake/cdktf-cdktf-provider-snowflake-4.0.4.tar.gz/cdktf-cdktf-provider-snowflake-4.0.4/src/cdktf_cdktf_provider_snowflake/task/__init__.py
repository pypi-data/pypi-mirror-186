'''
# `snowflake_task`

Refer to the Terraform Registory for docs: [`snowflake_task`](https://www.terraform.io/docs/providers/snowflake/r/task).
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


class Task(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.task.Task",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/task snowflake_task}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        sql_statement: builtins.str,
        after: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_overlapping_execution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        error_integration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        session_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_task_managed_initial_warehouse_size: typing.Optional[builtins.str] = None,
        user_task_timeout_ms: typing.Optional[jsii.Number] = None,
        warehouse: typing.Optional[builtins.str] = None,
        when: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/task snowflake_task} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database: The database in which to create the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#database Task#database}
        :param name: Specifies the identifier for the task; must be unique for the database and schema in which the task is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#name Task#name}
        :param schema: The schema in which to create the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schema Task#schema}
        :param sql_statement: Any single SQL statement, or a call to a stored procedure, executed when the task runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#sql_statement Task#sql_statement}
        :param after: Specifies one or more predecessor tasks for the current task. Use this option to create a DAG of tasks or add this task to an existing DAG. A DAG is a series of tasks that starts with a scheduled root task and is linked together by dependencies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#after Task#after}
        :param allow_overlapping_execution: By default, Snowflake ensures that only one instance of a particular DAG is allowed to run at a time, setting the parameter value to TRUE permits DAG runs to overlap. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#allow_overlapping_execution Task#allow_overlapping_execution}
        :param comment: Specifies a comment for the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#comment Task#comment}
        :param enabled: Specifies if the task should be started (enabled) after creation or should remain suspended (default). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#enabled Task#enabled}
        :param error_integration: Specifies the name of the notification integration used for error notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#error_integration Task#error_integration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#id Task#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: The schedule for periodically running the task. This can be a cron or interval in minutes. (Conflict with after). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schedule Task#schedule}
        :param session_parameters: Specifies session parameters to set for the session when the task runs. A task supports all session parameters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#session_parameters Task#session_parameters}
        :param user_task_managed_initial_warehouse_size: Specifies the size of the compute resources to provision for the first run of the task, before a task history is available for Snowflake to determine an ideal size. Once a task has successfully completed a few runs, Snowflake ignores this parameter setting. (Conflicts with warehouse) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_managed_initial_warehouse_size Task#user_task_managed_initial_warehouse_size}
        :param user_task_timeout_ms: Specifies the time limit on a single run of the task before it times out (in milliseconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_timeout_ms Task#user_task_timeout_ms}
        :param warehouse: The warehouse the task will use. Omit this parameter to use Snowflake-managed compute resources for runs of this task. (Conflicts with user_task_managed_initial_warehouse_size) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#warehouse Task#warehouse}
        :param when: Specifies a Boolean SQL expression; multiple conditions joined with AND/OR are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#when Task#when}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ea4604358bdf109eaf78f231f37e685f614aef5f8076778e9130b15f8df16b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TaskConfig(
            database=database,
            name=name,
            schema=schema,
            sql_statement=sql_statement,
            after=after,
            allow_overlapping_execution=allow_overlapping_execution,
            comment=comment,
            enabled=enabled,
            error_integration=error_integration,
            id=id,
            schedule=schedule,
            session_parameters=session_parameters,
            user_task_managed_initial_warehouse_size=user_task_managed_initial_warehouse_size,
            user_task_timeout_ms=user_task_timeout_ms,
            warehouse=warehouse,
            when=when,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAfter")
    def reset_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAfter", []))

    @jsii.member(jsii_name="resetAllowOverlappingExecution")
    def reset_allow_overlapping_execution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOverlappingExecution", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetErrorIntegration")
    def reset_error_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorIntegration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetSessionParameters")
    def reset_session_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionParameters", []))

    @jsii.member(jsii_name="resetUserTaskManagedInitialWarehouseSize")
    def reset_user_task_managed_initial_warehouse_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserTaskManagedInitialWarehouseSize", []))

    @jsii.member(jsii_name="resetUserTaskTimeoutMs")
    def reset_user_task_timeout_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserTaskTimeoutMs", []))

    @jsii.member(jsii_name="resetWarehouse")
    def reset_warehouse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouse", []))

    @jsii.member(jsii_name="resetWhen")
    def reset_when(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhen", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="afterInput")
    def after_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "afterInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOverlappingExecutionInput")
    def allow_overlapping_execution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowOverlappingExecutionInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="errorIntegrationInput")
    def error_integration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionParametersInput")
    def session_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sessionParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlStatementInput")
    def sql_statement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="userTaskManagedInitialWarehouseSizeInput")
    def user_task_managed_initial_warehouse_size_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userTaskManagedInitialWarehouseSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="userTaskTimeoutMsInput")
    def user_task_timeout_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userTaskTimeoutMsInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseInput")
    def warehouse_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseInput"))

    @builtins.property
    @jsii.member(jsii_name="whenInput")
    def when_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whenInput"))

    @builtins.property
    @jsii.member(jsii_name="after")
    def after(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "after"))

    @after.setter
    def after(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4f67b7c6aaa0dff726ba8906da170893801767daeb8594a67d27e29b4a8211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "after", value)

    @builtins.property
    @jsii.member(jsii_name="allowOverlappingExecution")
    def allow_overlapping_execution(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowOverlappingExecution"))

    @allow_overlapping_execution.setter
    def allow_overlapping_execution(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f45ea20a892361fea1f1a00ce23bf3fa2158ed4ff73473407f678b7e4d1966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOverlappingExecution", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a460ab85bdbee1b5b7d1afc2c85e737dcbf0fc049e53145eb43bcf5ac51fd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4663644f15e776aad0efb661ea515bf94c94a51357321a4b8454a61781655a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2247d9788dbb42ee801c5b9a3a4cbcd60643da236b230d1318fe35452c83e18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="errorIntegration")
    def error_integration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorIntegration"))

    @error_integration.setter
    def error_integration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e5eb20156b6371eea9d6150bb1904bc23049ba1e4170cbe9d97564bce3a4e32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorIntegration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b64b3bfe9c82317b45a085e9ac53577abd6c2d6c42bdfb4c9b5a38702f7a0cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35fdd161201488a3a65a8e3aab9a6810d45e1ad46cfb37cb179a616f85b3e1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da000ee29f8f079c870bb409ad042a8a1513ea08b68f0d4479b3de449ffbcab7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e414d304fb0b5b56fb9ac7ec2de77f79a7b509fa1f0697c776dea0112c26c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="sessionParameters")
    def session_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sessionParameters"))

    @session_parameters.setter
    def session_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ee9d403c6c3c46f39d289d514fda51527112bca9f27d3b12b1aa15ed3a71167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionParameters", value)

    @builtins.property
    @jsii.member(jsii_name="sqlStatement")
    def sql_statement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlStatement"))

    @sql_statement.setter
    def sql_statement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5b278cd40c077dc3d408636838637868d09b900fc1e63409db65d40e5f8eccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlStatement", value)

    @builtins.property
    @jsii.member(jsii_name="userTaskManagedInitialWarehouseSize")
    def user_task_managed_initial_warehouse_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userTaskManagedInitialWarehouseSize"))

    @user_task_managed_initial_warehouse_size.setter
    def user_task_managed_initial_warehouse_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd215a5b4794e793060b5f7cdaed15f6c4510f3c30f92263bf2dc02b2d7cc17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userTaskManagedInitialWarehouseSize", value)

    @builtins.property
    @jsii.member(jsii_name="userTaskTimeoutMs")
    def user_task_timeout_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userTaskTimeoutMs"))

    @user_task_timeout_ms.setter
    def user_task_timeout_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6add217094f96be1fdbd877c03c3acfb12531a10388192bbfa81d39cd144bd42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userTaskTimeoutMs", value)

    @builtins.property
    @jsii.member(jsii_name="warehouse")
    def warehouse(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouse"))

    @warehouse.setter
    def warehouse(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff6240dc59b88cc8128ed2cadcd5ef1616adff3e1f28ea512a868bf98f628315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouse", value)

    @builtins.property
    @jsii.member(jsii_name="when")
    def when(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "when"))

    @when.setter
    def when(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9cca6129d7883e1890cfab97ecfe18908703485c2bb1ddb9f98ca4f633a8dfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "when", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.task.TaskConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database": "database",
        "name": "name",
        "schema": "schema",
        "sql_statement": "sqlStatement",
        "after": "after",
        "allow_overlapping_execution": "allowOverlappingExecution",
        "comment": "comment",
        "enabled": "enabled",
        "error_integration": "errorIntegration",
        "id": "id",
        "schedule": "schedule",
        "session_parameters": "sessionParameters",
        "user_task_managed_initial_warehouse_size": "userTaskManagedInitialWarehouseSize",
        "user_task_timeout_ms": "userTaskTimeoutMs",
        "warehouse": "warehouse",
        "when": "when",
    },
)
class TaskConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        sql_statement: builtins.str,
        after: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_overlapping_execution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        error_integration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        session_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_task_managed_initial_warehouse_size: typing.Optional[builtins.str] = None,
        user_task_timeout_ms: typing.Optional[jsii.Number] = None,
        warehouse: typing.Optional[builtins.str] = None,
        when: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database: The database in which to create the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#database Task#database}
        :param name: Specifies the identifier for the task; must be unique for the database and schema in which the task is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#name Task#name}
        :param schema: The schema in which to create the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schema Task#schema}
        :param sql_statement: Any single SQL statement, or a call to a stored procedure, executed when the task runs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#sql_statement Task#sql_statement}
        :param after: Specifies one or more predecessor tasks for the current task. Use this option to create a DAG of tasks or add this task to an existing DAG. A DAG is a series of tasks that starts with a scheduled root task and is linked together by dependencies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#after Task#after}
        :param allow_overlapping_execution: By default, Snowflake ensures that only one instance of a particular DAG is allowed to run at a time, setting the parameter value to TRUE permits DAG runs to overlap. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#allow_overlapping_execution Task#allow_overlapping_execution}
        :param comment: Specifies a comment for the task. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#comment Task#comment}
        :param enabled: Specifies if the task should be started (enabled) after creation or should remain suspended (default). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#enabled Task#enabled}
        :param error_integration: Specifies the name of the notification integration used for error notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#error_integration Task#error_integration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#id Task#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: The schedule for periodically running the task. This can be a cron or interval in minutes. (Conflict with after). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schedule Task#schedule}
        :param session_parameters: Specifies session parameters to set for the session when the task runs. A task supports all session parameters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#session_parameters Task#session_parameters}
        :param user_task_managed_initial_warehouse_size: Specifies the size of the compute resources to provision for the first run of the task, before a task history is available for Snowflake to determine an ideal size. Once a task has successfully completed a few runs, Snowflake ignores this parameter setting. (Conflicts with warehouse) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_managed_initial_warehouse_size Task#user_task_managed_initial_warehouse_size}
        :param user_task_timeout_ms: Specifies the time limit on a single run of the task before it times out (in milliseconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_timeout_ms Task#user_task_timeout_ms}
        :param warehouse: The warehouse the task will use. Omit this parameter to use Snowflake-managed compute resources for runs of this task. (Conflicts with user_task_managed_initial_warehouse_size) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#warehouse Task#warehouse}
        :param when: Specifies a Boolean SQL expression; multiple conditions joined with AND/OR are supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#when Task#when}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3b33c946381b3c9a032b7570564a1e2078f7d125b95b09f4d234e236ac1b576)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument sql_statement", value=sql_statement, expected_type=type_hints["sql_statement"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument allow_overlapping_execution", value=allow_overlapping_execution, expected_type=type_hints["allow_overlapping_execution"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument error_integration", value=error_integration, expected_type=type_hints["error_integration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument session_parameters", value=session_parameters, expected_type=type_hints["session_parameters"])
            check_type(argname="argument user_task_managed_initial_warehouse_size", value=user_task_managed_initial_warehouse_size, expected_type=type_hints["user_task_managed_initial_warehouse_size"])
            check_type(argname="argument user_task_timeout_ms", value=user_task_timeout_ms, expected_type=type_hints["user_task_timeout_ms"])
            check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
            check_type(argname="argument when", value=when, expected_type=type_hints["when"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database": database,
            "name": name,
            "schema": schema,
            "sql_statement": sql_statement,
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
        if after is not None:
            self._values["after"] = after
        if allow_overlapping_execution is not None:
            self._values["allow_overlapping_execution"] = allow_overlapping_execution
        if comment is not None:
            self._values["comment"] = comment
        if enabled is not None:
            self._values["enabled"] = enabled
        if error_integration is not None:
            self._values["error_integration"] = error_integration
        if id is not None:
            self._values["id"] = id
        if schedule is not None:
            self._values["schedule"] = schedule
        if session_parameters is not None:
            self._values["session_parameters"] = session_parameters
        if user_task_managed_initial_warehouse_size is not None:
            self._values["user_task_managed_initial_warehouse_size"] = user_task_managed_initial_warehouse_size
        if user_task_timeout_ms is not None:
            self._values["user_task_timeout_ms"] = user_task_timeout_ms
        if warehouse is not None:
            self._values["warehouse"] = warehouse
        if when is not None:
            self._values["when"] = when

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
    def database(self) -> builtins.str:
        '''The database in which to create the task.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#database Task#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the task;

        must be unique for the database and schema in which the task is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#name Task#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the task.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schema Task#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_statement(self) -> builtins.str:
        '''Any single SQL statement, or a call to a stored procedure, executed when the task runs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#sql_statement Task#sql_statement}
        '''
        result = self._values.get("sql_statement")
        assert result is not None, "Required property 'sql_statement' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies one or more predecessor tasks for the current task.

        Use this option to create a DAG of tasks or add this task to an existing DAG. A DAG is a series of tasks that starts with a scheduled root task and is linked together by dependencies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#after Task#after}
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_overlapping_execution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''By default, Snowflake ensures that only one instance of a particular DAG is allowed to run at a time, setting the parameter value to TRUE permits DAG runs to overlap.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#allow_overlapping_execution Task#allow_overlapping_execution}
        '''
        result = self._values.get("allow_overlapping_execution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the task.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#comment Task#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies if the task should be started (enabled) after creation or should remain suspended (default).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#enabled Task#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def error_integration(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the notification integration used for error notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#error_integration Task#error_integration}
        '''
        result = self._values.get("error_integration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#id Task#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''The schedule for periodically running the task. This can be a cron or interval in minutes. (Conflict with after).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#schedule Task#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies session parameters to set for the session when the task runs. A task supports all session parameters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#session_parameters Task#session_parameters}
        '''
        result = self._values.get("session_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_task_managed_initial_warehouse_size(self) -> typing.Optional[builtins.str]:
        '''Specifies the size of the compute resources to provision for the first run of the task, before a task history is available for Snowflake to determine an ideal size.

        Once a task has successfully completed a few runs, Snowflake ignores this parameter setting. (Conflicts with warehouse)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_managed_initial_warehouse_size Task#user_task_managed_initial_warehouse_size}
        '''
        result = self._values.get("user_task_managed_initial_warehouse_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_task_timeout_ms(self) -> typing.Optional[jsii.Number]:
        '''Specifies the time limit on a single run of the task before it times out (in milliseconds).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#user_task_timeout_ms Task#user_task_timeout_ms}
        '''
        result = self._values.get("user_task_timeout_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warehouse(self) -> typing.Optional[builtins.str]:
        '''The warehouse the task will use.

        Omit this parameter to use Snowflake-managed compute resources for runs of this task. (Conflicts with user_task_managed_initial_warehouse_size)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#warehouse Task#warehouse}
        '''
        result = self._values.get("warehouse")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def when(self) -> typing.Optional[builtins.str]:
        '''Specifies a Boolean SQL expression; multiple conditions joined with AND/OR are supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/task#when Task#when}
        '''
        result = self._values.get("when")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Task",
    "TaskConfig",
]

publication.publish()

def _typecheckingstub__c9ea4604358bdf109eaf78f231f37e685f614aef5f8076778e9130b15f8df16b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    database: builtins.str,
    name: builtins.str,
    schema: builtins.str,
    sql_statement: builtins.str,
    after: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_overlapping_execution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    error_integration: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    session_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_task_managed_initial_warehouse_size: typing.Optional[builtins.str] = None,
    user_task_timeout_ms: typing.Optional[jsii.Number] = None,
    warehouse: typing.Optional[builtins.str] = None,
    when: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__cd4f67b7c6aaa0dff726ba8906da170893801767daeb8594a67d27e29b4a8211(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f45ea20a892361fea1f1a00ce23bf3fa2158ed4ff73473407f678b7e4d1966(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a460ab85bdbee1b5b7d1afc2c85e737dcbf0fc049e53145eb43bcf5ac51fd64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4663644f15e776aad0efb661ea515bf94c94a51357321a4b8454a61781655a8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2247d9788dbb42ee801c5b9a3a4cbcd60643da236b230d1318fe35452c83e18(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5eb20156b6371eea9d6150bb1904bc23049ba1e4170cbe9d97564bce3a4e32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64b3bfe9c82317b45a085e9ac53577abd6c2d6c42bdfb4c9b5a38702f7a0cdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35fdd161201488a3a65a8e3aab9a6810d45e1ad46cfb37cb179a616f85b3e1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da000ee29f8f079c870bb409ad042a8a1513ea08b68f0d4479b3de449ffbcab7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e414d304fb0b5b56fb9ac7ec2de77f79a7b509fa1f0697c776dea0112c26c67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ee9d403c6c3c46f39d289d514fda51527112bca9f27d3b12b1aa15ed3a71167(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5b278cd40c077dc3d408636838637868d09b900fc1e63409db65d40e5f8eccf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd215a5b4794e793060b5f7cdaed15f6c4510f3c30f92263bf2dc02b2d7cc17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6add217094f96be1fdbd877c03c3acfb12531a10388192bbfa81d39cd144bd42(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6240dc59b88cc8128ed2cadcd5ef1616adff3e1f28ea512a868bf98f628315(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cca6129d7883e1890cfab97ecfe18908703485c2bb1ddb9f98ca4f633a8dfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3b33c946381b3c9a032b7570564a1e2078f7d125b95b09f4d234e236ac1b576(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    database: builtins.str,
    name: builtins.str,
    schema: builtins.str,
    sql_statement: builtins.str,
    after: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_overlapping_execution: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    error_integration: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    session_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_task_managed_initial_warehouse_size: typing.Optional[builtins.str] = None,
    user_task_timeout_ms: typing.Optional[jsii.Number] = None,
    warehouse: typing.Optional[builtins.str] = None,
    when: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
