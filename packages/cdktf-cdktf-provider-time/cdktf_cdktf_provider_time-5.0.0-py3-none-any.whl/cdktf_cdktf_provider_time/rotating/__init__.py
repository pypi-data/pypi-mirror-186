'''
# `time_rotating`

Refer to the Terraform Registory for docs: [`time_rotating`](https://www.terraform.io/docs/providers/time/r/rotating).
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


class Rotating(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-time.rotating.Rotating",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/time/r/rotating time_rotating}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rfc3339: typing.Optional[builtins.str] = None,
        rotation_days: typing.Optional[jsii.Number] = None,
        rotation_hours: typing.Optional[jsii.Number] = None,
        rotation_minutes: typing.Optional[jsii.Number] = None,
        rotation_months: typing.Optional[jsii.Number] = None,
        rotation_rfc3339: typing.Optional[builtins.str] = None,
        rotation_years: typing.Optional[jsii.Number] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/time/r/rotating time_rotating} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param rfc3339: Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rfc3339 Rotating#rfc3339}
        :param rotation_days: Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_days Rotating#rotation_days}
        :param rotation_hours: Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_hours Rotating#rotation_hours}
        :param rotation_minutes: Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_minutes Rotating#rotation_minutes}
        :param rotation_months: Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_months Rotating#rotation_months}
        :param rotation_rfc3339: Configure the rotation timestamp with an `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format of the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_rfc3339 Rotating#rotation_rfc3339}
        :param rotation_years: Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_years Rotating#rotation_years}
        :param triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#triggers Rotating#triggers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c13281499aa3e710a3456226c42baeb53ca697f298f0c2613a29a084996063)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = RotatingConfig(
            rfc3339=rfc3339,
            rotation_days=rotation_days,
            rotation_hours=rotation_hours,
            rotation_minutes=rotation_minutes,
            rotation_months=rotation_months,
            rotation_rfc3339=rotation_rfc3339,
            rotation_years=rotation_years,
            triggers=triggers,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetRfc3339")
    def reset_rfc3339(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRfc3339", []))

    @jsii.member(jsii_name="resetRotationDays")
    def reset_rotation_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationDays", []))

    @jsii.member(jsii_name="resetRotationHours")
    def reset_rotation_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationHours", []))

    @jsii.member(jsii_name="resetRotationMinutes")
    def reset_rotation_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationMinutes", []))

    @jsii.member(jsii_name="resetRotationMonths")
    def reset_rotation_months(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationMonths", []))

    @jsii.member(jsii_name="resetRotationRfc3339")
    def reset_rotation_rfc3339(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationRfc3339", []))

    @jsii.member(jsii_name="resetRotationYears")
    def reset_rotation_years(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRotationYears", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="day")
    def day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "day"))

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hour"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minute"))

    @builtins.property
    @jsii.member(jsii_name="month")
    def month(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "month"))

    @builtins.property
    @jsii.member(jsii_name="second")
    def second(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "second"))

    @builtins.property
    @jsii.member(jsii_name="unix")
    def unix(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unix"))

    @builtins.property
    @jsii.member(jsii_name="year")
    def year(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "year"))

    @builtins.property
    @jsii.member(jsii_name="rfc3339Input")
    def rfc3339_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rfc3339Input"))

    @builtins.property
    @jsii.member(jsii_name="rotationDaysInput")
    def rotation_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationHoursInput")
    def rotation_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationMinutesInput")
    def rotation_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationMonthsInput")
    def rotation_months_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationMonthsInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationRfc3339Input")
    def rotation_rfc3339_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationRfc3339Input"))

    @builtins.property
    @jsii.member(jsii_name="rotationYearsInput")
    def rotation_years_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rotationYearsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="rfc3339")
    def rfc3339(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rfc3339"))

    @rfc3339.setter
    def rfc3339(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4967d467cc02b26dab5414c05bcdbc7404457e5c47224e66a01225a2a0bd2a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rfc3339", value)

    @builtins.property
    @jsii.member(jsii_name="rotationDays")
    def rotation_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rotationDays"))

    @rotation_days.setter
    def rotation_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543509ee679bd2e33479050070db33c86685a0d98717c4d7293fb4c38423c26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationDays", value)

    @builtins.property
    @jsii.member(jsii_name="rotationHours")
    def rotation_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rotationHours"))

    @rotation_hours.setter
    def rotation_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ed6a079eabe0b2503ff289ce39e7ae0e51feffc7259d7df99c53a8309a8305a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationHours", value)

    @builtins.property
    @jsii.member(jsii_name="rotationMinutes")
    def rotation_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rotationMinutes"))

    @rotation_minutes.setter
    def rotation_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4572e905d3c72bf0dfa63d5827a6ed96520049295162278331c5291ea1dd33a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="rotationMonths")
    def rotation_months(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rotationMonths"))

    @rotation_months.setter
    def rotation_months(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b1586326d522ac41981f5bcf4e4a351499d8056001632cd42db056f4e46d4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationMonths", value)

    @builtins.property
    @jsii.member(jsii_name="rotationRfc3339")
    def rotation_rfc3339(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationRfc3339"))

    @rotation_rfc3339.setter
    def rotation_rfc3339(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017c5b2b86a809e5a853108e031902e325aaa6b64a0011a2bfb40355b60a6ce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationRfc3339", value)

    @builtins.property
    @jsii.member(jsii_name="rotationYears")
    def rotation_years(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rotationYears"))

    @rotation_years.setter
    def rotation_years(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9019e6a2889b4f88d1384d46ff180cc25752553f222e37e5589448cbe80c94d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationYears", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d9f47289987e468ec84d3f0b48ca78434d1451277bdb259d77429932149c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-time.rotating.RotatingConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "rfc3339": "rfc3339",
        "rotation_days": "rotationDays",
        "rotation_hours": "rotationHours",
        "rotation_minutes": "rotationMinutes",
        "rotation_months": "rotationMonths",
        "rotation_rfc3339": "rotationRfc3339",
        "rotation_years": "rotationYears",
        "triggers": "triggers",
    },
)
class RotatingConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        rfc3339: typing.Optional[builtins.str] = None,
        rotation_days: typing.Optional[jsii.Number] = None,
        rotation_hours: typing.Optional[jsii.Number] = None,
        rotation_minutes: typing.Optional[jsii.Number] = None,
        rotation_months: typing.Optional[jsii.Number] = None,
        rotation_rfc3339: typing.Optional[builtins.str] = None,
        rotation_years: typing.Optional[jsii.Number] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param rfc3339: Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rfc3339 Rotating#rfc3339}
        :param rotation_days: Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_days Rotating#rotation_days}
        :param rotation_hours: Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_hours Rotating#rotation_hours}
        :param rotation_minutes: Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_minutes Rotating#rotation_minutes}
        :param rotation_months: Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_months Rotating#rotation_months}
        :param rotation_rfc3339: Configure the rotation timestamp with an `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format of the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_rfc3339 Rotating#rotation_rfc3339}
        :param rotation_years: Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_years Rotating#rotation_years}
        :param triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#triggers Rotating#triggers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ff127dfa3aa123c42955f732770508fb130fcb2094145ead1fd7fbe2809aa7e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument rfc3339", value=rfc3339, expected_type=type_hints["rfc3339"])
            check_type(argname="argument rotation_days", value=rotation_days, expected_type=type_hints["rotation_days"])
            check_type(argname="argument rotation_hours", value=rotation_hours, expected_type=type_hints["rotation_hours"])
            check_type(argname="argument rotation_minutes", value=rotation_minutes, expected_type=type_hints["rotation_minutes"])
            check_type(argname="argument rotation_months", value=rotation_months, expected_type=type_hints["rotation_months"])
            check_type(argname="argument rotation_rfc3339", value=rotation_rfc3339, expected_type=type_hints["rotation_rfc3339"])
            check_type(argname="argument rotation_years", value=rotation_years, expected_type=type_hints["rotation_years"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
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
        if rfc3339 is not None:
            self._values["rfc3339"] = rfc3339
        if rotation_days is not None:
            self._values["rotation_days"] = rotation_days
        if rotation_hours is not None:
            self._values["rotation_hours"] = rotation_hours
        if rotation_minutes is not None:
            self._values["rotation_minutes"] = rotation_minutes
        if rotation_months is not None:
            self._values["rotation_months"] = rotation_months
        if rotation_rfc3339 is not None:
            self._values["rotation_rfc3339"] = rotation_rfc3339
        if rotation_years is not None:
            self._values["rotation_years"] = rotation_years
        if triggers is not None:
            self._values["triggers"] = triggers

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
    def rfc3339(self) -> typing.Optional[builtins.str]:
        '''Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rfc3339 Rotating#rfc3339}
        '''
        result = self._values.get("rfc3339")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days to add to the base timestamp to configure the rotation timestamp.

        When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_days Rotating#rotation_days}
        '''
        result = self._values.get("rotation_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rotation_hours(self) -> typing.Optional[jsii.Number]:
        '''Number of hours to add to the base timestamp to configure the rotation timestamp.

        When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_hours Rotating#rotation_hours}
        '''
        result = self._values.get("rotation_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rotation_minutes(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes to add to the base timestamp to configure the rotation timestamp.

        When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_minutes Rotating#rotation_minutes}
        '''
        result = self._values.get("rotation_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rotation_months(self) -> typing.Optional[jsii.Number]:
        '''Number of months to add to the base timestamp to configure the rotation timestamp.

        When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_months Rotating#rotation_months}
        '''
        result = self._values.get("rotation_months")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rotation_rfc3339(self) -> typing.Optional[builtins.str]:
        '''Configure the rotation timestamp with an `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format of the offset timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_rfc3339 Rotating#rotation_rfc3339}
        '''
        result = self._values.get("rotation_rfc3339")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotation_years(self) -> typing.Optional[jsii.Number]:
        '''Number of years to add to the base timestamp to configure the rotation timestamp.

        When the current time has passed the rotation timestamp, the resource will trigger recreation. At least one of the 'rotation_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#rotation_years Rotating#rotation_years}
        '''
        result = self._values.get("rotation_years")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved.

        These conditions recreate the resource in addition to other rotation arguments. See `the main provider documentation <../index.md>`_ for more information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/rotating#triggers Rotating#triggers}
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RotatingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Rotating",
    "RotatingConfig",
]

publication.publish()

def _typecheckingstub__c8c13281499aa3e710a3456226c42baeb53ca697f298f0c2613a29a084996063(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rfc3339: typing.Optional[builtins.str] = None,
    rotation_days: typing.Optional[jsii.Number] = None,
    rotation_hours: typing.Optional[jsii.Number] = None,
    rotation_minutes: typing.Optional[jsii.Number] = None,
    rotation_months: typing.Optional[jsii.Number] = None,
    rotation_rfc3339: typing.Optional[builtins.str] = None,
    rotation_years: typing.Optional[jsii.Number] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__4967d467cc02b26dab5414c05bcdbc7404457e5c47224e66a01225a2a0bd2a72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543509ee679bd2e33479050070db33c86685a0d98717c4d7293fb4c38423c26d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed6a079eabe0b2503ff289ce39e7ae0e51feffc7259d7df99c53a8309a8305a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4572e905d3c72bf0dfa63d5827a6ed96520049295162278331c5291ea1dd33a0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b1586326d522ac41981f5bcf4e4a351499d8056001632cd42db056f4e46d4d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017c5b2b86a809e5a853108e031902e325aaa6b64a0011a2bfb40355b60a6ce0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9019e6a2889b4f88d1384d46ff180cc25752553f222e37e5589448cbe80c94d7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d9f47289987e468ec84d3f0b48ca78434d1451277bdb259d77429932149c45(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ff127dfa3aa123c42955f732770508fb130fcb2094145ead1fd7fbe2809aa7e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    rfc3339: typing.Optional[builtins.str] = None,
    rotation_days: typing.Optional[jsii.Number] = None,
    rotation_hours: typing.Optional[jsii.Number] = None,
    rotation_minutes: typing.Optional[jsii.Number] = None,
    rotation_months: typing.Optional[jsii.Number] = None,
    rotation_rfc3339: typing.Optional[builtins.str] = None,
    rotation_years: typing.Optional[jsii.Number] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
