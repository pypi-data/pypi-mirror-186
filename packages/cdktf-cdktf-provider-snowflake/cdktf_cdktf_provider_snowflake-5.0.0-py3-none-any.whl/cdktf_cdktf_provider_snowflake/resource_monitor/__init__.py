'''
# `snowflake_resource_monitor`

Refer to the Terraform Registory for docs: [`snowflake_resource_monitor`](https://www.terraform.io/docs/providers/snowflake/r/resource_monitor).
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


class ResourceMonitor(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.resourceMonitor.ResourceMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor snowflake_resource_monitor}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        credit_quota: typing.Optional[jsii.Number] = None,
        end_timestamp: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notify_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        notify_users: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_for_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        start_timestamp: typing.Optional[builtins.str] = None,
        suspend_immediate_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        suspend_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        warehouses: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor snowflake_resource_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Identifier for the resource monitor; must be unique for your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#name ResourceMonitor#name}
        :param credit_quota: The number of credits allocated monthly to the resource monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#credit_quota ResourceMonitor#credit_quota}
        :param end_timestamp: The date and time when the resource monitor suspends the assigned warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#end_timestamp ResourceMonitor#end_timestamp}
        :param frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#frequency ResourceMonitor#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#id ResourceMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_triggers ResourceMonitor#notify_triggers}
        :param notify_users: Specifies the list of users to receive email notifications on resource monitors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_users ResourceMonitor#notify_users}
        :param set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#set_for_account ResourceMonitor#set_for_account}
        :param start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#start_timestamp ResourceMonitor#start_timestamp}
        :param suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_immediate_triggers ResourceMonitor#suspend_immediate_triggers}
        :param suspend_triggers: A list of percentage thresholds at which to suspend all warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_triggers ResourceMonitor#suspend_triggers}
        :param warehouses: A list of warehouses to apply the resource monitor to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#warehouses ResourceMonitor#warehouses}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b43a9f295b51125a0dc341a3552580e5e5ddea1e35a3201e8b54a8ca99f95b21)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ResourceMonitorConfig(
            name=name,
            credit_quota=credit_quota,
            end_timestamp=end_timestamp,
            frequency=frequency,
            id=id,
            notify_triggers=notify_triggers,
            notify_users=notify_users,
            set_for_account=set_for_account,
            start_timestamp=start_timestamp,
            suspend_immediate_triggers=suspend_immediate_triggers,
            suspend_triggers=suspend_triggers,
            warehouses=warehouses,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCreditQuota")
    def reset_credit_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreditQuota", []))

    @jsii.member(jsii_name="resetEndTimestamp")
    def reset_end_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTimestamp", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotifyTriggers")
    def reset_notify_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyTriggers", []))

    @jsii.member(jsii_name="resetNotifyUsers")
    def reset_notify_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyUsers", []))

    @jsii.member(jsii_name="resetSetForAccount")
    def reset_set_for_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetForAccount", []))

    @jsii.member(jsii_name="resetStartTimestamp")
    def reset_start_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimestamp", []))

    @jsii.member(jsii_name="resetSuspendImmediateTriggers")
    def reset_suspend_immediate_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspendImmediateTriggers", []))

    @jsii.member(jsii_name="resetSuspendTriggers")
    def reset_suspend_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspendTriggers", []))

    @jsii.member(jsii_name="resetWarehouses")
    def reset_warehouses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouses", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creditQuotaInput")
    def credit_quota_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creditQuotaInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimestampInput")
    def end_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyTriggersInput")
    def notify_triggers_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "notifyTriggersInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyUsersInput")
    def notify_users_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notifyUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="setForAccountInput")
    def set_for_account_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "setForAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimestampInput")
    def start_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendImmediateTriggersInput")
    def suspend_immediate_triggers_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "suspendImmediateTriggersInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendTriggersInput")
    def suspend_triggers_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "suspendTriggersInput"))

    @builtins.property
    @jsii.member(jsii_name="warehousesInput")
    def warehouses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "warehousesInput"))

    @builtins.property
    @jsii.member(jsii_name="creditQuota")
    def credit_quota(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creditQuota"))

    @credit_quota.setter
    def credit_quota(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96602caff2c16f75fbba74de405c9c77824284c81393b6f5f5f0bd94ff45eb2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creditQuota", value)

    @builtins.property
    @jsii.member(jsii_name="endTimestamp")
    def end_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTimestamp"))

    @end_timestamp.setter
    def end_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d7deb08041c42bce10f40e8038f28d35285a8bb382453400460d82e154451b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894cd8cacad81cb91f6065b680e30ed3fd543495844a290d7e48e437bb9e33e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9021990c2b184ed0e466635c380fd5a3c070de8dfabcc0b7aea239761b88aa25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24041f919aedf240169256de40993fa94cd711ddc7717db3b69846ccdeacbc5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notifyTriggers")
    def notify_triggers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "notifyTriggers"))

    @notify_triggers.setter
    def notify_triggers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d335b3aacc03c9c38bda997dbddd1fabd0d813654d995556ba749cd16d265704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyTriggers", value)

    @builtins.property
    @jsii.member(jsii_name="notifyUsers")
    def notify_users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notifyUsers"))

    @notify_users.setter
    def notify_users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfaa7d35d7c8a7c7429628e363ed1bef8587571e67236057805a18f0b5cf6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyUsers", value)

    @builtins.property
    @jsii.member(jsii_name="setForAccount")
    def set_for_account(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "setForAccount"))

    @set_for_account.setter
    def set_for_account(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac81392b373fdfddf8efebf3b5016e524b2eeb0615a63811b16cf6d9456e5f9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setForAccount", value)

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTimestamp"))

    @start_timestamp.setter
    def start_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638ac1a05fbd330d55c7d6bee7e08ddb584718264bf2cf67d407684acca021ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="suspendImmediateTriggers")
    def suspend_immediate_triggers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "suspendImmediateTriggers"))

    @suspend_immediate_triggers.setter
    def suspend_immediate_triggers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75116399c93fbfb1b2d3cd5f8fe1a020c4b09067d6875d4e88253c720b45c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspendImmediateTriggers", value)

    @builtins.property
    @jsii.member(jsii_name="suspendTriggers")
    def suspend_triggers(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "suspendTriggers"))

    @suspend_triggers.setter
    def suspend_triggers(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e62685bb7d945ee9f6ba3bc03a39327c5f52a849cfedb53e2730bb94edc77a71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspendTriggers", value)

    @builtins.property
    @jsii.member(jsii_name="warehouses")
    def warehouses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "warehouses"))

    @warehouses.setter
    def warehouses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3ff36e94ab334f26b7fb7501bec87b26a3bda3eb24301ecd772645c6168a26a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouses", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.resourceMonitor.ResourceMonitorConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "credit_quota": "creditQuota",
        "end_timestamp": "endTimestamp",
        "frequency": "frequency",
        "id": "id",
        "notify_triggers": "notifyTriggers",
        "notify_users": "notifyUsers",
        "set_for_account": "setForAccount",
        "start_timestamp": "startTimestamp",
        "suspend_immediate_triggers": "suspendImmediateTriggers",
        "suspend_triggers": "suspendTriggers",
        "warehouses": "warehouses",
    },
)
class ResourceMonitorConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        credit_quota: typing.Optional[jsii.Number] = None,
        end_timestamp: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        notify_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        notify_users: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_for_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        start_timestamp: typing.Optional[builtins.str] = None,
        suspend_immediate_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        suspend_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
        warehouses: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Identifier for the resource monitor; must be unique for your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#name ResourceMonitor#name}
        :param credit_quota: The number of credits allocated monthly to the resource monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#credit_quota ResourceMonitor#credit_quota}
        :param end_timestamp: The date and time when the resource monitor suspends the assigned warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#end_timestamp ResourceMonitor#end_timestamp}
        :param frequency: The frequency interval at which the credit usage resets to 0. If you set a frequency for a resource monitor, you must also set START_TIMESTAMP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#frequency ResourceMonitor#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#id ResourceMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param notify_triggers: A list of percentage thresholds at which to send an alert to subscribed users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_triggers ResourceMonitor#notify_triggers}
        :param notify_users: Specifies the list of users to receive email notifications on resource monitors. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_users ResourceMonitor#notify_users}
        :param set_for_account: Specifies whether the resource monitor should be applied globally to your Snowflake account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#set_for_account ResourceMonitor#set_for_account}
        :param start_timestamp: The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#start_timestamp ResourceMonitor#start_timestamp}
        :param suspend_immediate_triggers: A list of percentage thresholds at which to immediately suspend all warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_immediate_triggers ResourceMonitor#suspend_immediate_triggers}
        :param suspend_triggers: A list of percentage thresholds at which to suspend all warehouses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_triggers ResourceMonitor#suspend_triggers}
        :param warehouses: A list of warehouses to apply the resource monitor to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#warehouses ResourceMonitor#warehouses}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b439086a68ba68e8f0eae072b448ebc95a349a034db77c7cc5c6d98df78a7c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument credit_quota", value=credit_quota, expected_type=type_hints["credit_quota"])
            check_type(argname="argument end_timestamp", value=end_timestamp, expected_type=type_hints["end_timestamp"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notify_triggers", value=notify_triggers, expected_type=type_hints["notify_triggers"])
            check_type(argname="argument notify_users", value=notify_users, expected_type=type_hints["notify_users"])
            check_type(argname="argument set_for_account", value=set_for_account, expected_type=type_hints["set_for_account"])
            check_type(argname="argument start_timestamp", value=start_timestamp, expected_type=type_hints["start_timestamp"])
            check_type(argname="argument suspend_immediate_triggers", value=suspend_immediate_triggers, expected_type=type_hints["suspend_immediate_triggers"])
            check_type(argname="argument suspend_triggers", value=suspend_triggers, expected_type=type_hints["suspend_triggers"])
            check_type(argname="argument warehouses", value=warehouses, expected_type=type_hints["warehouses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if credit_quota is not None:
            self._values["credit_quota"] = credit_quota
        if end_timestamp is not None:
            self._values["end_timestamp"] = end_timestamp
        if frequency is not None:
            self._values["frequency"] = frequency
        if id is not None:
            self._values["id"] = id
        if notify_triggers is not None:
            self._values["notify_triggers"] = notify_triggers
        if notify_users is not None:
            self._values["notify_users"] = notify_users
        if set_for_account is not None:
            self._values["set_for_account"] = set_for_account
        if start_timestamp is not None:
            self._values["start_timestamp"] = start_timestamp
        if suspend_immediate_triggers is not None:
            self._values["suspend_immediate_triggers"] = suspend_immediate_triggers
        if suspend_triggers is not None:
            self._values["suspend_triggers"] = suspend_triggers
        if warehouses is not None:
            self._values["warehouses"] = warehouses

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
    def name(self) -> builtins.str:
        '''Identifier for the resource monitor; must be unique for your account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#name ResourceMonitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credit_quota(self) -> typing.Optional[jsii.Number]:
        '''The number of credits allocated monthly to the resource monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#credit_quota ResourceMonitor#credit_quota}
        '''
        result = self._values.get("credit_quota")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def end_timestamp(self) -> typing.Optional[builtins.str]:
        '''The date and time when the resource monitor suspends the assigned warehouses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#end_timestamp ResourceMonitor#end_timestamp}
        '''
        result = self._values.get("end_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency interval at which the credit usage resets to 0.

        If you set a frequency for a resource monitor, you must also set START_TIMESTAMP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#frequency ResourceMonitor#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#id ResourceMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_triggers(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of percentage thresholds at which to send an alert to subscribed users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_triggers ResourceMonitor#notify_triggers}
        '''
        result = self._values.get("notify_triggers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def notify_users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of users to receive email notifications on resource monitors.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#notify_users ResourceMonitor#notify_users}
        '''
        result = self._values.get("notify_users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set_for_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether the resource monitor should be applied globally to your Snowflake account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#set_for_account ResourceMonitor#set_for_account}
        '''
        result = self._values.get("set_for_account")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def start_timestamp(self) -> typing.Optional[builtins.str]:
        '''The date and time when the resource monitor starts monitoring credit usage for the assigned warehouses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#start_timestamp ResourceMonitor#start_timestamp}
        '''
        result = self._values.get("start_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspend_immediate_triggers(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of percentage thresholds at which to immediately suspend all warehouses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_immediate_triggers ResourceMonitor#suspend_immediate_triggers}
        '''
        result = self._values.get("suspend_immediate_triggers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def suspend_triggers(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of percentage thresholds at which to suspend all warehouses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#suspend_triggers ResourceMonitor#suspend_triggers}
        '''
        result = self._values.get("suspend_triggers")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def warehouses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of warehouses to apply the resource monitor to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/resource_monitor#warehouses ResourceMonitor#warehouses}
        '''
        result = self._values.get("warehouses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ResourceMonitor",
    "ResourceMonitorConfig",
]

publication.publish()

def _typecheckingstub__b43a9f295b51125a0dc341a3552580e5e5ddea1e35a3201e8b54a8ca99f95b21(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    credit_quota: typing.Optional[jsii.Number] = None,
    end_timestamp: typing.Optional[builtins.str] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    notify_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    notify_users: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_for_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    start_timestamp: typing.Optional[builtins.str] = None,
    suspend_immediate_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    suspend_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    warehouses: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__96602caff2c16f75fbba74de405c9c77824284c81393b6f5f5f0bd94ff45eb2f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d7deb08041c42bce10f40e8038f28d35285a8bb382453400460d82e154451b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894cd8cacad81cb91f6065b680e30ed3fd543495844a290d7e48e437bb9e33e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9021990c2b184ed0e466635c380fd5a3c070de8dfabcc0b7aea239761b88aa25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24041f919aedf240169256de40993fa94cd711ddc7717db3b69846ccdeacbc5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d335b3aacc03c9c38bda997dbddd1fabd0d813654d995556ba749cd16d265704(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfaa7d35d7c8a7c7429628e363ed1bef8587571e67236057805a18f0b5cf6d1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac81392b373fdfddf8efebf3b5016e524b2eeb0615a63811b16cf6d9456e5f9d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__638ac1a05fbd330d55c7d6bee7e08ddb584718264bf2cf67d407684acca021ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75116399c93fbfb1b2d3cd5f8fe1a020c4b09067d6875d4e88253c720b45c2d(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62685bb7d945ee9f6ba3bc03a39327c5f52a849cfedb53e2730bb94edc77a71(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3ff36e94ab334f26b7fb7501bec87b26a3bda3eb24301ecd772645c6168a26a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b439086a68ba68e8f0eae072b448ebc95a349a034db77c7cc5c6d98df78a7c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    credit_quota: typing.Optional[jsii.Number] = None,
    end_timestamp: typing.Optional[builtins.str] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    notify_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    notify_users: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_for_account: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    start_timestamp: typing.Optional[builtins.str] = None,
    suspend_immediate_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    suspend_triggers: typing.Optional[typing.Sequence[jsii.Number]] = None,
    warehouses: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
