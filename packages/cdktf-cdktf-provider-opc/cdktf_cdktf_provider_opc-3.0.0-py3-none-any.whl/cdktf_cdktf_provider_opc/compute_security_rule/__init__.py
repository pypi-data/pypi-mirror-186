'''
# `opc_compute_security_rule`

Refer to the Terraform Registory for docs: [`opc_compute_security_rule`](https://www.terraform.io/docs/providers/opc/r/compute_security_rule).
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


class ComputeSecurityRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeSecurityRule.ComputeSecurityRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule opc_compute_security_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        flow_direction: builtins.str,
        name: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dst_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        dst_vnic_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        security_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_vnic_set: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule opc_compute_security_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param flow_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#flow_direction ComputeSecurityRule#flow_direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#name ComputeSecurityRule#name}.
        :param acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#acl ComputeSecurityRule#acl}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#description ComputeSecurityRule#description}.
        :param dst_ip_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_ip_address_prefixes ComputeSecurityRule#dst_ip_address_prefixes}.
        :param dst_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_vnic_set ComputeSecurityRule#dst_vnic_set}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#enabled ComputeSecurityRule#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#id ComputeSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#security_protocols ComputeSecurityRule#security_protocols}.
        :param src_ip_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_ip_address_prefixes ComputeSecurityRule#src_ip_address_prefixes}.
        :param src_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_vnic_set ComputeSecurityRule#src_vnic_set}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#tags ComputeSecurityRule#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84469fe342caeeb18aa5a7bc077a08ffb817dca6b0e76ccd311a113fbad55e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeSecurityRuleConfig(
            flow_direction=flow_direction,
            name=name,
            acl=acl,
            description=description,
            dst_ip_address_prefixes=dst_ip_address_prefixes,
            dst_vnic_set=dst_vnic_set,
            enabled=enabled,
            id=id,
            security_protocols=security_protocols,
            src_ip_address_prefixes=src_ip_address_prefixes,
            src_vnic_set=src_vnic_set,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAcl")
    def reset_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcl", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDstIpAddressPrefixes")
    def reset_dst_ip_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDstIpAddressPrefixes", []))

    @jsii.member(jsii_name="resetDstVnicSet")
    def reset_dst_vnic_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDstVnicSet", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurityProtocols")
    def reset_security_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityProtocols", []))

    @jsii.member(jsii_name="resetSrcIpAddressPrefixes")
    def reset_src_ip_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcIpAddressPrefixes", []))

    @jsii.member(jsii_name="resetSrcVnicSet")
    def reset_src_vnic_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcVnicSet", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="aclInput")
    def acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aclInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dstIpAddressPrefixesInput")
    def dst_ip_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dstIpAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="dstVnicSetInput")
    def dst_vnic_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dstVnicSetInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="flowDirectionInput")
    def flow_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityProtocolsInput")
    def security_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="srcIpAddressPrefixesInput")
    def src_ip_address_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "srcIpAddressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="srcVnicSetInput")
    def src_vnic_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "srcVnicSetInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="acl")
    def acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acl"))

    @acl.setter
    def acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aefdcb93520bfc865d68730dff5411b95090205025a4dba2f759f51ec330657a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acl", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24874231cf0d79ed1779efca1b8877378ec09292c4acc860bbfbfd54a43730ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dstIpAddressPrefixes")
    def dst_ip_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dstIpAddressPrefixes"))

    @dst_ip_address_prefixes.setter
    def dst_ip_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e7b3793ec182eaa09ebd88889ac4b0fcc5b8904c310ff124daac718e229fce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dstIpAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="dstVnicSet")
    def dst_vnic_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dstVnicSet"))

    @dst_vnic_set.setter
    def dst_vnic_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4bb9f0f8126b2c54d4ffeaac44be163a43bf8e102d1e47ac71e487b0a3332ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dstVnicSet", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__ae71bea7bb35fcd65c00bdc2ca0113db0d12c35dfe92c95d54d1849bcdd394bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="flowDirection")
    def flow_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "flowDirection"))

    @flow_direction.setter
    def flow_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4602ab3396a2b8c945ca98132372348287500b072124655d6317f88cd6a4485d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowDirection", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd2a34667279f2f5b99b6c93f7802380eacd6538b2a3425c0fd46c82fa6ff95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e636465f0a69ed2588e54d522875a167caa7a8bb309cac9af5f348837e29dadc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="securityProtocols")
    def security_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityProtocols"))

    @security_protocols.setter
    def security_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3a9ac7ec2149b6c49868aef9528221ab876dc5e4fea68a9b23465061c4978e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="srcIpAddressPrefixes")
    def src_ip_address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "srcIpAddressPrefixes"))

    @src_ip_address_prefixes.setter
    def src_ip_address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fae6fa5bb09b9e016f21bef93e6b01b16d491ec2b1b7817671ecbba2e9bc05a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "srcIpAddressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="srcVnicSet")
    def src_vnic_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "srcVnicSet"))

    @src_vnic_set.setter
    def src_vnic_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a880966f4387d0983aa8ce0388f97514f419fc1dbb1671699996f197e5060cc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "srcVnicSet", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86cf07845c50d6a989eb0c5be9a8d91b028fadbb9afb6fac258bef2fe84a3fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeSecurityRule.ComputeSecurityRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "flow_direction": "flowDirection",
        "name": "name",
        "acl": "acl",
        "description": "description",
        "dst_ip_address_prefixes": "dstIpAddressPrefixes",
        "dst_vnic_set": "dstVnicSet",
        "enabled": "enabled",
        "id": "id",
        "security_protocols": "securityProtocols",
        "src_ip_address_prefixes": "srcIpAddressPrefixes",
        "src_vnic_set": "srcVnicSet",
        "tags": "tags",
    },
)
class ComputeSecurityRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        flow_direction: builtins.str,
        name: builtins.str,
        acl: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dst_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        dst_vnic_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        security_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        src_vnic_set: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param flow_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#flow_direction ComputeSecurityRule#flow_direction}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#name ComputeSecurityRule#name}.
        :param acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#acl ComputeSecurityRule#acl}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#description ComputeSecurityRule#description}.
        :param dst_ip_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_ip_address_prefixes ComputeSecurityRule#dst_ip_address_prefixes}.
        :param dst_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_vnic_set ComputeSecurityRule#dst_vnic_set}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#enabled ComputeSecurityRule#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#id ComputeSecurityRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#security_protocols ComputeSecurityRule#security_protocols}.
        :param src_ip_address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_ip_address_prefixes ComputeSecurityRule#src_ip_address_prefixes}.
        :param src_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_vnic_set ComputeSecurityRule#src_vnic_set}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#tags ComputeSecurityRule#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc302ef219b3593c268520b7d5fd481149ffa41d2b986acc53016ed5863c116a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument flow_direction", value=flow_direction, expected_type=type_hints["flow_direction"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument acl", value=acl, expected_type=type_hints["acl"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dst_ip_address_prefixes", value=dst_ip_address_prefixes, expected_type=type_hints["dst_ip_address_prefixes"])
            check_type(argname="argument dst_vnic_set", value=dst_vnic_set, expected_type=type_hints["dst_vnic_set"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security_protocols", value=security_protocols, expected_type=type_hints["security_protocols"])
            check_type(argname="argument src_ip_address_prefixes", value=src_ip_address_prefixes, expected_type=type_hints["src_ip_address_prefixes"])
            check_type(argname="argument src_vnic_set", value=src_vnic_set, expected_type=type_hints["src_vnic_set"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_direction": flow_direction,
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
        if acl is not None:
            self._values["acl"] = acl
        if description is not None:
            self._values["description"] = description
        if dst_ip_address_prefixes is not None:
            self._values["dst_ip_address_prefixes"] = dst_ip_address_prefixes
        if dst_vnic_set is not None:
            self._values["dst_vnic_set"] = dst_vnic_set
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if security_protocols is not None:
            self._values["security_protocols"] = security_protocols
        if src_ip_address_prefixes is not None:
            self._values["src_ip_address_prefixes"] = src_ip_address_prefixes
        if src_vnic_set is not None:
            self._values["src_vnic_set"] = src_vnic_set
        if tags is not None:
            self._values["tags"] = tags

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
    def flow_direction(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#flow_direction ComputeSecurityRule#flow_direction}.'''
        result = self._values.get("flow_direction")
        assert result is not None, "Required property 'flow_direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#name ComputeSecurityRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#acl ComputeSecurityRule#acl}.'''
        result = self._values.get("acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#description ComputeSecurityRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dst_ip_address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_ip_address_prefixes ComputeSecurityRule#dst_ip_address_prefixes}.'''
        result = self._values.get("dst_ip_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dst_vnic_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#dst_vnic_set ComputeSecurityRule#dst_vnic_set}.'''
        result = self._values.get("dst_vnic_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#enabled ComputeSecurityRule#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#id ComputeSecurityRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#security_protocols ComputeSecurityRule#security_protocols}.'''
        result = self._values.get("security_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def src_ip_address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_ip_address_prefixes ComputeSecurityRule#src_ip_address_prefixes}.'''
        result = self._values.get("src_ip_address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def src_vnic_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#src_vnic_set ComputeSecurityRule#src_vnic_set}.'''
        result = self._values.get("src_vnic_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_security_rule#tags ComputeSecurityRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecurityRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComputeSecurityRule",
    "ComputeSecurityRuleConfig",
]

publication.publish()

def _typecheckingstub__d84469fe342caeeb18aa5a7bc077a08ffb817dca6b0e76ccd311a113fbad55e9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    flow_direction: builtins.str,
    name: builtins.str,
    acl: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dst_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    dst_vnic_set: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    security_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_vnic_set: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__aefdcb93520bfc865d68730dff5411b95090205025a4dba2f759f51ec330657a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24874231cf0d79ed1779efca1b8877378ec09292c4acc860bbfbfd54a43730ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e7b3793ec182eaa09ebd88889ac4b0fcc5b8904c310ff124daac718e229fce3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bb9f0f8126b2c54d4ffeaac44be163a43bf8e102d1e47ac71e487b0a3332ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae71bea7bb35fcd65c00bdc2ca0113db0d12c35dfe92c95d54d1849bcdd394bc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4602ab3396a2b8c945ca98132372348287500b072124655d6317f88cd6a4485d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd2a34667279f2f5b99b6c93f7802380eacd6538b2a3425c0fd46c82fa6ff95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e636465f0a69ed2588e54d522875a167caa7a8bb309cac9af5f348837e29dadc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3a9ac7ec2149b6c49868aef9528221ab876dc5e4fea68a9b23465061c4978e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fae6fa5bb09b9e016f21bef93e6b01b16d491ec2b1b7817671ecbba2e9bc05a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a880966f4387d0983aa8ce0388f97514f419fc1dbb1671699996f197e5060cc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86cf07845c50d6a989eb0c5be9a8d91b028fadbb9afb6fac258bef2fe84a3fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc302ef219b3593c268520b7d5fd481149ffa41d2b986acc53016ed5863c116a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    flow_direction: builtins.str,
    name: builtins.str,
    acl: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dst_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    dst_vnic_set: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    security_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_ip_address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    src_vnic_set: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
