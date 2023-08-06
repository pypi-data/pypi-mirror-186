'''
# replace this
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

from ._jsii import *

import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import constructs as _constructs_77d1e7e8


class AzIdToNameMapping(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@renovosolutions/cdk-library-multi-account-az-mapping.AzIdToNameMapping",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        az_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        ssm_parameter_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param az_ids: The target AZ IDs for mapping. Defaults to values for 3 zones in us-east-1. Default: ['use1-az2', 'use1-az4', 'use1-az6']
        :param log_retention: The number of days to retain log events in CloudWatch logs. Defaults to 30 days. Default: logs.RetentionDays.ONE_MONTH
        :param ssm_parameter_prefix: The prefix to use for the SSM parameter names. Defaults to ``/az-mapping/``. Default: '/az-mapping/'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f8e01f1331094aea4f29fcdf1c20c5b0d4600dafd77865a5c3bfc70a4779f1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AzIdToNameMappingProps(
            az_ids=az_ids,
            log_retention=log_retention,
            ssm_parameter_prefix=ssm_parameter_prefix,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(self) -> builtins.str:
        '''The resulting mapping of AZ IDs to names.'''
        return typing.cast(builtins.str, jsii.get(self, "mapping"))


@jsii.data_type(
    jsii_type="@renovosolutions/cdk-library-multi-account-az-mapping.AzIdToNameMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "az_ids": "azIds",
        "log_retention": "logRetention",
        "ssm_parameter_prefix": "ssmParameterPrefix",
    },
)
class AzIdToNameMappingProps:
    def __init__(
        self,
        *,
        az_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        ssm_parameter_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The properties of a new AZ ID to name mapping.

        :param az_ids: The target AZ IDs for mapping. Defaults to values for 3 zones in us-east-1. Default: ['use1-az2', 'use1-az4', 'use1-az6']
        :param log_retention: The number of days to retain log events in CloudWatch logs. Defaults to 30 days. Default: logs.RetentionDays.ONE_MONTH
        :param ssm_parameter_prefix: The prefix to use for the SSM parameter names. Defaults to ``/az-mapping/``. Default: '/az-mapping/'
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c15575ce63eee4acf10333bc7c3ac0aabb639dfb8e41183cddd7e624e1931e)
            check_type(argname="argument az_ids", value=az_ids, expected_type=type_hints["az_ids"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument ssm_parameter_prefix", value=ssm_parameter_prefix, expected_type=type_hints["ssm_parameter_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if az_ids is not None:
            self._values["az_ids"] = az_ids
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if ssm_parameter_prefix is not None:
            self._values["ssm_parameter_prefix"] = ssm_parameter_prefix

    @builtins.property
    def az_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The target AZ IDs for mapping.

        Defaults to values for 3 zones in us-east-1.

        :default: ['use1-az2', 'use1-az4', 'use1-az6']
        '''
        result = self._values.get("az_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''The number of days to retain log events in CloudWatch logs.

        Defaults to 30 days.

        :default: logs.RetentionDays.ONE_MONTH
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays], result)

    @builtins.property
    def ssm_parameter_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix to use for the SSM parameter names.

        Defaults to ``/az-mapping/``.

        :default: '/az-mapping/'
        '''
        result = self._values.get("ssm_parameter_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzIdToNameMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzIdToNameMapping",
    "AzIdToNameMappingProps",
]

publication.publish()

def _typecheckingstub__7f8e01f1331094aea4f29fcdf1c20c5b0d4600dafd77865a5c3bfc70a4779f1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    az_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    ssm_parameter_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c15575ce63eee4acf10333bc7c3ac0aabb639dfb8e41183cddd7e624e1931e(
    *,
    az_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    ssm_parameter_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
