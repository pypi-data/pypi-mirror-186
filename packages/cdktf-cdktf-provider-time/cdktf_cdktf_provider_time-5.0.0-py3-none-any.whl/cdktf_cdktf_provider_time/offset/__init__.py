'''
# `time_offset`

Refer to the Terraform Registory for docs: [`time_offset`](https://www.terraform.io/docs/providers/time/r/offset).
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


class Offset(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-time.offset.Offset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/time/r/offset time_offset}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        base_rfc3339: typing.Optional[builtins.str] = None,
        offset_days: typing.Optional[jsii.Number] = None,
        offset_hours: typing.Optional[jsii.Number] = None,
        offset_minutes: typing.Optional[jsii.Number] = None,
        offset_months: typing.Optional[jsii.Number] = None,
        offset_seconds: typing.Optional[jsii.Number] = None,
        offset_years: typing.Optional[jsii.Number] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/time/r/offset time_offset} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param base_rfc3339: Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#base_rfc3339 Offset#base_rfc3339}
        :param offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_days Offset#offset_days}
        :param offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_hours Offset#offset_hours}
        :param offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_minutes Offset#offset_minutes}
        :param offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_months Offset#offset_months}
        :param offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_seconds Offset#offset_seconds}
        :param offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_years Offset#offset_years}
        :param triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#triggers Offset#triggers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9fd7695f5711af9175b6ca233a8c5337da7099d808f3a23892d8573c984dc4a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = OffsetConfig(
            base_rfc3339=base_rfc3339,
            offset_days=offset_days,
            offset_hours=offset_hours,
            offset_minutes=offset_minutes,
            offset_months=offset_months,
            offset_seconds=offset_seconds,
            offset_years=offset_years,
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

    @jsii.member(jsii_name="resetBaseRfc3339")
    def reset_base_rfc3339(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseRfc3339", []))

    @jsii.member(jsii_name="resetOffsetDays")
    def reset_offset_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetDays", []))

    @jsii.member(jsii_name="resetOffsetHours")
    def reset_offset_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetHours", []))

    @jsii.member(jsii_name="resetOffsetMinutes")
    def reset_offset_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetMinutes", []))

    @jsii.member(jsii_name="resetOffsetMonths")
    def reset_offset_months(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetMonths", []))

    @jsii.member(jsii_name="resetOffsetSeconds")
    def reset_offset_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetSeconds", []))

    @jsii.member(jsii_name="resetOffsetYears")
    def reset_offset_years(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffsetYears", []))

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
    @jsii.member(jsii_name="rfc3339")
    def rfc3339(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rfc3339"))

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
    @jsii.member(jsii_name="baseRfc3339Input")
    def base_rfc3339_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseRfc3339Input"))

    @builtins.property
    @jsii.member(jsii_name="offsetDaysInput")
    def offset_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetHoursInput")
    def offset_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetMinutesInput")
    def offset_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetMonthsInput")
    def offset_months_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetMonthsInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetSecondsInput")
    def offset_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="offsetYearsInput")
    def offset_years_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "offsetYearsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="baseRfc3339")
    def base_rfc3339(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseRfc3339"))

    @base_rfc3339.setter
    def base_rfc3339(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a4af860be4e58401c9698981c01bd1c82fcec4a7539c864b48ccf7aeb25487c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseRfc3339", value)

    @builtins.property
    @jsii.member(jsii_name="offsetDays")
    def offset_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetDays"))

    @offset_days.setter
    def offset_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb1efc778cac1673b0f13e8aa17c46965cd1f36449cc2b40e83b524bd2d1bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetDays", value)

    @builtins.property
    @jsii.member(jsii_name="offsetHours")
    def offset_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetHours"))

    @offset_hours.setter
    def offset_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e5d6128232ac059e5ac00f3f098654f67e5908f60e29c77916c961f44fe015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetHours", value)

    @builtins.property
    @jsii.member(jsii_name="offsetMinutes")
    def offset_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetMinutes"))

    @offset_minutes.setter
    def offset_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b53c427051faaf1e36a3a821674ecfe93187a389931f6af828c5564f8d0da3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="offsetMonths")
    def offset_months(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetMonths"))

    @offset_months.setter
    def offset_months(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__497a6e1847696753a51e0bf32fdd7ebc3f208cd7daf42532c474a4faf75e6b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetMonths", value)

    @builtins.property
    @jsii.member(jsii_name="offsetSeconds")
    def offset_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetSeconds"))

    @offset_seconds.setter
    def offset_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b2eb3d616af6a153ee62eaa309c9c11fd5a4842f93c02acbd19ecb238a466d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="offsetYears")
    def offset_years(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "offsetYears"))

    @offset_years.setter
    def offset_years(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08020f118f604906a7cdefe1d788c2f8456e068846ac2dd2a3e85d3083cf3538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offsetYears", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20e040223711affb7161dc7486fa5242186665aec4fca6b2b47a0a05f958468)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-time.offset.OffsetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "base_rfc3339": "baseRfc3339",
        "offset_days": "offsetDays",
        "offset_hours": "offsetHours",
        "offset_minutes": "offsetMinutes",
        "offset_months": "offsetMonths",
        "offset_seconds": "offsetSeconds",
        "offset_years": "offsetYears",
        "triggers": "triggers",
    },
)
class OffsetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        base_rfc3339: typing.Optional[builtins.str] = None,
        offset_days: typing.Optional[jsii.Number] = None,
        offset_hours: typing.Optional[jsii.Number] = None,
        offset_minutes: typing.Optional[jsii.Number] = None,
        offset_months: typing.Optional[jsii.Number] = None,
        offset_seconds: typing.Optional[jsii.Number] = None,
        offset_years: typing.Optional[jsii.Number] = None,
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
        :param base_rfc3339: Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#base_rfc3339 Offset#base_rfc3339}
        :param offset_days: Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_days Offset#offset_days}
        :param offset_hours: Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_hours Offset#offset_hours}
        :param offset_minutes: Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_minutes Offset#offset_minutes}
        :param offset_months: Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_months Offset#offset_months}
        :param offset_seconds: Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_seconds Offset#offset_seconds}
        :param offset_years: Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_years Offset#offset_years}
        :param triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See `the main provider documentation <../index.md>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#triggers Offset#triggers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129647c305336dbf1cae2ce70d04cb6a6fee40863714fac62a4bfe71187fa828)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument base_rfc3339", value=base_rfc3339, expected_type=type_hints["base_rfc3339"])
            check_type(argname="argument offset_days", value=offset_days, expected_type=type_hints["offset_days"])
            check_type(argname="argument offset_hours", value=offset_hours, expected_type=type_hints["offset_hours"])
            check_type(argname="argument offset_minutes", value=offset_minutes, expected_type=type_hints["offset_minutes"])
            check_type(argname="argument offset_months", value=offset_months, expected_type=type_hints["offset_months"])
            check_type(argname="argument offset_seconds", value=offset_seconds, expected_type=type_hints["offset_seconds"])
            check_type(argname="argument offset_years", value=offset_years, expected_type=type_hints["offset_years"])
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
        if base_rfc3339 is not None:
            self._values["base_rfc3339"] = base_rfc3339
        if offset_days is not None:
            self._values["offset_days"] = offset_days
        if offset_hours is not None:
            self._values["offset_hours"] = offset_hours
        if offset_minutes is not None:
            self._values["offset_minutes"] = offset_minutes
        if offset_months is not None:
            self._values["offset_months"] = offset_months
        if offset_seconds is not None:
            self._values["offset_seconds"] = offset_seconds
        if offset_years is not None:
            self._values["offset_years"] = offset_years
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
    def base_rfc3339(self) -> typing.Optional[builtins.str]:
        '''Base timestamp in `RFC3339 <https://datatracker.ietf.org/doc/html/rfc3339#section-5.8>`_ format (see `RFC3339 time string <https://tools.ietf.org/html/rfc3339#section-5.8>`_ e.g., ``YYYY-MM-DDTHH:MM:SSZ``). Defaults to the current time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#base_rfc3339 Offset#base_rfc3339}
        '''
        result = self._values.get("base_rfc3339")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offset_days(self) -> typing.Optional[jsii.Number]:
        '''Number of days to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_days Offset#offset_days}
        '''
        result = self._values.get("offset_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset_hours(self) -> typing.Optional[jsii.Number]:
        '''Number of hours to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_hours Offset#offset_hours}
        '''
        result = self._values.get("offset_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset_minutes(self) -> typing.Optional[jsii.Number]:
        '''Number of minutes to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_minutes Offset#offset_minutes}
        '''
        result = self._values.get("offset_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset_months(self) -> typing.Optional[jsii.Number]:
        '''Number of months to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_months Offset#offset_months}
        '''
        result = self._values.get("offset_months")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_seconds Offset#offset_seconds}
        '''
        result = self._values.get("offset_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offset_years(self) -> typing.Optional[jsii.Number]:
        '''Number of years to offset the base timestamp. At least one of the 'offset_' arguments must be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#offset_years Offset#offset_years}
        '''
        result = self._values.get("offset_years")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved.

        See `the main provider documentation <../index.md>`_ for more information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/time/r/offset#triggers Offset#triggers}
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OffsetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Offset",
    "OffsetConfig",
]

publication.publish()

def _typecheckingstub__b9fd7695f5711af9175b6ca233a8c5337da7099d808f3a23892d8573c984dc4a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    base_rfc3339: typing.Optional[builtins.str] = None,
    offset_days: typing.Optional[jsii.Number] = None,
    offset_hours: typing.Optional[jsii.Number] = None,
    offset_minutes: typing.Optional[jsii.Number] = None,
    offset_months: typing.Optional[jsii.Number] = None,
    offset_seconds: typing.Optional[jsii.Number] = None,
    offset_years: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__8a4af860be4e58401c9698981c01bd1c82fcec4a7539c864b48ccf7aeb25487c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb1efc778cac1673b0f13e8aa17c46965cd1f36449cc2b40e83b524bd2d1bbb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e5d6128232ac059e5ac00f3f098654f67e5908f60e29c77916c961f44fe015(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b53c427051faaf1e36a3a821674ecfe93187a389931f6af828c5564f8d0da3a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497a6e1847696753a51e0bf32fdd7ebc3f208cd7daf42532c474a4faf75e6b22(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b2eb3d616af6a153ee62eaa309c9c11fd5a4842f93c02acbd19ecb238a466d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08020f118f604906a7cdefe1d788c2f8456e068846ac2dd2a3e85d3083cf3538(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20e040223711affb7161dc7486fa5242186665aec4fca6b2b47a0a05f958468(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129647c305336dbf1cae2ce70d04cb6a6fee40863714fac62a4bfe71187fa828(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    base_rfc3339: typing.Optional[builtins.str] = None,
    offset_days: typing.Optional[jsii.Number] = None,
    offset_hours: typing.Optional[jsii.Number] = None,
    offset_minutes: typing.Optional[jsii.Number] = None,
    offset_months: typing.Optional[jsii.Number] = None,
    offset_seconds: typing.Optional[jsii.Number] = None,
    offset_years: typing.Optional[jsii.Number] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
