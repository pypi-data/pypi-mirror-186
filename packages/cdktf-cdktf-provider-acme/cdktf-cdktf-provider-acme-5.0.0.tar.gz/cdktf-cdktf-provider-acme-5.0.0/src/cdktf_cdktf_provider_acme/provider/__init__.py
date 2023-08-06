'''
# `provider`

Refer to the Terraform Registory for docs: [`acme`](https://www.terraform.io/docs/providers/acme).
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


class AcmeProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-acme.provider.AcmeProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/acme acme}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        server_url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/acme acme} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param server_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#server_url AcmeProvider#server_url}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#alias AcmeProvider#alias}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b41f1cfd2f69f148a1ffa9489a0356740a2fca8caf9435966ab85b72ef8cf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AcmeProviderConfig(server_url=server_url, alias=alias)

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="serverUrlInput")
    def server_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2608580cffa3b270678729a6e973a889d39144b4f9468be8e10feab1264b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverUrl"))

    @server_url.setter
    def server_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d23f0deee9208896e3210b425656534026cd64d82b6248f6c70c8a974741ee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverUrl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-acme.provider.AcmeProviderConfig",
    jsii_struct_bases=[],
    name_mapping={"server_url": "serverUrl", "alias": "alias"},
)
class AcmeProviderConfig:
    def __init__(
        self,
        *,
        server_url: builtins.str,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#server_url AcmeProvider#server_url}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#alias AcmeProvider#alias}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14fb200adff3faac440042b42f3464d33fee1f86988eb85120dabf0d40f7d490)
            check_type(argname="argument server_url", value=server_url, expected_type=type_hints["server_url"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "server_url": server_url,
        }
        if alias is not None:
            self._values["alias"] = alias

    @builtins.property
    def server_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#server_url AcmeProvider#server_url}.'''
        result = self._values.get("server_url")
        assert result is not None, "Required property 'server_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/acme#alias AcmeProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcmeProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AcmeProvider",
    "AcmeProviderConfig",
]

publication.publish()

def _typecheckingstub__96b41f1cfd2f69f148a1ffa9489a0356740a2fca8caf9435966ab85b72ef8cf6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    server_url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2608580cffa3b270678729a6e973a889d39144b4f9468be8e10feab1264b96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d23f0deee9208896e3210b425656534026cd64d82b6248f6c70c8a974741ee6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14fb200adff3faac440042b42f3464d33fee1f86988eb85120dabf0d40f7d490(
    *,
    server_url: builtins.str,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
