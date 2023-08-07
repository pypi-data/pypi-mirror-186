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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import constructs as _constructs_77d1e7e8


class Hello(metaclass=jsii.JSIIMeta, jsii_type="vt-vpc-construct.Hello"):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="sayHello")
    def say_hello(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "sayHello", []))


@jsii.interface(jsii_type="vt-vpc-construct.IStackProps")
class IStackProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="costcenter")
    def costcenter(self) -> builtins.str:
        ...

    @costcenter.setter
    def costcenter(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        ...

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''vpc name.

        :default: solutionName
        '''
        ...

    @name.setter
    def name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="solutionName")
    def solution_name(self) -> builtins.str:
        ...

    @solution_name.setter
    def solution_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> typing.Optional[builtins.str]:
        '''vpc cidr.

        :default: '172.16.0.0/16'
        '''
        ...

    @cidr.setter
    def cidr(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _IStackPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "vt-vpc-construct.IStackProps"

    @builtins.property
    @jsii.member(jsii_name="costcenter")
    def costcenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "costcenter"))

    @costcenter.setter
    def costcenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f046a002114686ee1e14da4aa3823024849dd69a28643ed8c19dc18753a52cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "costcenter", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f88a6858cc5efb2810648126b7fd39e127fddc5fe47f760e20f5b38df5c28dc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''vpc name.

        :default: solutionName
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7b74849b1117931ea3ca28e3e094ac91258c33b2fe52e114ba8cca758a58c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="solutionName")
    def solution_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "solutionName"))

    @solution_name.setter
    def solution_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfca5ad8e32ad5888b542bf25389b587458c09585765907c1233a5e8c7bc6b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "solutionName", value)

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> typing.Optional[builtins.str]:
        '''vpc cidr.

        :default: '172.16.0.0/16'
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd73eaa7e1e7dbeecb06568701dee9bf6e0b8ab9b6a2f093ecf01096abc13715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackProps).__jsii_proxy_class__ = lambda : _IStackPropsProxy


class VTVpc(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="vt-vpc-construct.VTVpc",
):
    def __init__(
        self,
        parent: _aws_cdk_ceddda9d.Stack,
        id: builtins.str,
        props: IStackProps,
    ) -> None:
        '''
        :param parent: -
        :param id: -
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f512aa133aa63b171cc294a4c1dd5845bf6672962e8729694d671b6bb462271e)
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [parent, id, props])

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.Vpc:
        '''API construct.'''
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.Vpc, jsii.get(self, "vpc"))


__all__ = [
    "Hello",
    "IStackProps",
    "VTVpc",
]

publication.publish()

def _typecheckingstub__4f046a002114686ee1e14da4aa3823024849dd69a28643ed8c19dc18753a52cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88a6858cc5efb2810648126b7fd39e127fddc5fe47f760e20f5b38df5c28dc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b74849b1117931ea3ca28e3e094ac91258c33b2fe52e114ba8cca758a58c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfca5ad8e32ad5888b542bf25389b587458c09585765907c1233a5e8c7bc6b2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd73eaa7e1e7dbeecb06568701dee9bf6e0b8ab9b6a2f093ecf01096abc13715(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f512aa133aa63b171cc294a4c1dd5845bf6672962e8729694d671b6bb462271e(
    parent: _aws_cdk_ceddda9d.Stack,
    id: builtins.str,
    props: IStackProps,
) -> None:
    """Type checking stubs"""
    pass
