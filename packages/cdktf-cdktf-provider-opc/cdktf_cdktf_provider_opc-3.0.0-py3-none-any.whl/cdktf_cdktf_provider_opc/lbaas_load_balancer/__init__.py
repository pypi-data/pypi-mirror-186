'''
# `opc_lbaas_load_balancer`

Refer to the Terraform Registory for docs: [`opc_lbaas_load_balancer`](https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer).
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


class LbaasLoadBalancer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasLoadBalancer.LbaasLoadBalancer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer opc_lbaas_load_balancer}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        region: builtins.str,
        scheme: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        parent_load_balancer: typing.Optional[builtins.str] = None,
        permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        permitted_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_pool: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer opc_lbaas_load_balancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#name LbaasLoadBalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#region LbaasLoadBalancer#region}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#scheme LbaasLoadBalancer#scheme}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#description LbaasLoadBalancer#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#enabled LbaasLoadBalancer#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#id LbaasLoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#ip_network LbaasLoadBalancer#ip_network}.
        :param parent_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#parent_load_balancer LbaasLoadBalancer#parent_load_balancer}.
        :param permitted_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_clients LbaasLoadBalancer#permitted_clients}.
        :param permitted_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_methods LbaasLoadBalancer#permitted_methods}.
        :param policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#policies LbaasLoadBalancer#policies}.
        :param server_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#server_pool LbaasLoadBalancer#server_pool}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#tags LbaasLoadBalancer#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58c68bc30162e29a54235fa8a62ac1f77cef91bcc19a3700ad2498fef7af177)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbaasLoadBalancerConfig(
            name=name,
            region=region,
            scheme=scheme,
            description=description,
            enabled=enabled,
            id=id,
            ip_network=ip_network,
            parent_load_balancer=parent_load_balancer,
            permitted_clients=permitted_clients,
            permitted_methods=permitted_methods,
            policies=policies,
            server_pool=server_pool,
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

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetParentLoadBalancer")
    def reset_parent_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentLoadBalancer", []))

    @jsii.member(jsii_name="resetPermittedClients")
    def reset_permitted_clients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermittedClients", []))

    @jsii.member(jsii_name="resetPermittedMethods")
    def reset_permitted_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermittedMethods", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @jsii.member(jsii_name="resetServerPool")
    def reset_server_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerPool", []))

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
    @jsii.member(jsii_name="balancerVips")
    def balancer_vips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "balancerVips"))

    @builtins.property
    @jsii.member(jsii_name="canonicalHostName")
    def canonical_host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "canonicalHostName"))

    @builtins.property
    @jsii.member(jsii_name="cloudgateCapable")
    def cloudgate_capable(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cloudgateCapable"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentLoadBalancerInput")
    def parent_load_balancer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentLoadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="permittedClientsInput")
    def permitted_clients_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permittedClientsInput"))

    @builtins.property
    @jsii.member(jsii_name="permittedMethodsInput")
    def permitted_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permittedMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverPoolInput")
    def server_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9992ed88e7995bd64d81cc75119da8086385779dcd8cc3858f2b4f4ca70bb79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1e8715966ed5b5dc063fc020da62919dcb68cfe46980325e260b726d679e5b7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9377f8065994934d29cb964bc8ef415885f80b607a40f61a6e3f7d6784e12e5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a923853d37e48dc4c2a88974fd73e9bf8f8526de5e9e6b0f8f41c64b75482ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f242763b6a3e4cf0dbbcc09c313e657bed9090bd051a84d4f67471c375690380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentLoadBalancer")
    def parent_load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentLoadBalancer"))

    @parent_load_balancer.setter
    def parent_load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__060db9720b8d8395871c39810a4bc6bbdfa728fd5fbd5b95fad73342f40da1ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentLoadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="permittedClients")
    def permitted_clients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permittedClients"))

    @permitted_clients.setter
    def permitted_clients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19d9883162a5c567e2d4a933b221ce46eba2e21f6911c5b8c1802bf7000779d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permittedClients", value)

    @builtins.property
    @jsii.member(jsii_name="permittedMethods")
    def permitted_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permittedMethods"))

    @permitted_methods.setter
    def permitted_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0705b06faac2e557f7d6b91e95164bfcd3a8cfae255dc73f649d45e192d29727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permittedMethods", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cff960b205f8c2398b78edb6d11403693f7a0c511cc6ea801d4b4c19e257039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1805abbe2aaccad69bc5c748ae7cda077e2c3509dfdbe5fd0378c52e52aeb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f9311bda976180b46f59f86e808c443681f4961e9e93b05bd2e59f1d6b2b727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="serverPool")
    def server_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverPool"))

    @server_pool.setter
    def server_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f5ff2ac3117d74fc28ae89e76d424fa67729d9232da594aac180aa52906c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverPool", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbfff3a0507b6403394f6533b9a0bf72a3bdda179a8d809a9bfed2a93092b0e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasLoadBalancer.LbaasLoadBalancerConfig",
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
        "region": "region",
        "scheme": "scheme",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "ip_network": "ipNetwork",
        "parent_load_balancer": "parentLoadBalancer",
        "permitted_clients": "permittedClients",
        "permitted_methods": "permittedMethods",
        "policies": "policies",
        "server_pool": "serverPool",
        "tags": "tags",
    },
)
class LbaasLoadBalancerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        region: builtins.str,
        scheme: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        parent_load_balancer: typing.Optional[builtins.str] = None,
        permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
        permitted_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_pool: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#name LbaasLoadBalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#region LbaasLoadBalancer#region}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#scheme LbaasLoadBalancer#scheme}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#description LbaasLoadBalancer#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#enabled LbaasLoadBalancer#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#id LbaasLoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#ip_network LbaasLoadBalancer#ip_network}.
        :param parent_load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#parent_load_balancer LbaasLoadBalancer#parent_load_balancer}.
        :param permitted_clients: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_clients LbaasLoadBalancer#permitted_clients}.
        :param permitted_methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_methods LbaasLoadBalancer#permitted_methods}.
        :param policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#policies LbaasLoadBalancer#policies}.
        :param server_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#server_pool LbaasLoadBalancer#server_pool}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#tags LbaasLoadBalancer#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3005d1497cdd6201663a36ebaaa81579469756828bfb3909506a692ec2a1ab3f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument parent_load_balancer", value=parent_load_balancer, expected_type=type_hints["parent_load_balancer"])
            check_type(argname="argument permitted_clients", value=permitted_clients, expected_type=type_hints["permitted_clients"])
            check_type(argname="argument permitted_methods", value=permitted_methods, expected_type=type_hints["permitted_methods"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument server_pool", value=server_pool, expected_type=type_hints["server_pool"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "region": region,
            "scheme": scheme,
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
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if parent_load_balancer is not None:
            self._values["parent_load_balancer"] = parent_load_balancer
        if permitted_clients is not None:
            self._values["permitted_clients"] = permitted_clients
        if permitted_methods is not None:
            self._values["permitted_methods"] = permitted_methods
        if policies is not None:
            self._values["policies"] = policies
        if server_pool is not None:
            self._values["server_pool"] = server_pool
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#name LbaasLoadBalancer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#region LbaasLoadBalancer#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheme(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#scheme LbaasLoadBalancer#scheme}.'''
        result = self._values.get("scheme")
        assert result is not None, "Required property 'scheme' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#description LbaasLoadBalancer#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#enabled LbaasLoadBalancer#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#id LbaasLoadBalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#ip_network LbaasLoadBalancer#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_load_balancer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#parent_load_balancer LbaasLoadBalancer#parent_load_balancer}.'''
        result = self._values.get("parent_load_balancer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permitted_clients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_clients LbaasLoadBalancer#permitted_clients}.'''
        result = self._values.get("permitted_clients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permitted_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#permitted_methods LbaasLoadBalancer#permitted_methods}.'''
        result = self._values.get("permitted_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#policies LbaasLoadBalancer#policies}.'''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_pool(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#server_pool LbaasLoadBalancer#server_pool}.'''
        result = self._values.get("server_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_load_balancer#tags LbaasLoadBalancer#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasLoadBalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LbaasLoadBalancer",
    "LbaasLoadBalancerConfig",
]

publication.publish()

def _typecheckingstub__a58c68bc30162e29a54235fa8a62ac1f77cef91bcc19a3700ad2498fef7af177(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    region: builtins.str,
    scheme: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    parent_load_balancer: typing.Optional[builtins.str] = None,
    permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    permitted_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_pool: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f9992ed88e7995bd64d81cc75119da8086385779dcd8cc3858f2b4f4ca70bb79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8715966ed5b5dc063fc020da62919dcb68cfe46980325e260b726d679e5b7f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9377f8065994934d29cb964bc8ef415885f80b607a40f61a6e3f7d6784e12e5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a923853d37e48dc4c2a88974fd73e9bf8f8526de5e9e6b0f8f41c64b75482ace(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f242763b6a3e4cf0dbbcc09c313e657bed9090bd051a84d4f67471c375690380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060db9720b8d8395871c39810a4bc6bbdfa728fd5fbd5b95fad73342f40da1ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19d9883162a5c567e2d4a933b221ce46eba2e21f6911c5b8c1802bf7000779d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0705b06faac2e557f7d6b91e95164bfcd3a8cfae255dc73f649d45e192d29727(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cff960b205f8c2398b78edb6d11403693f7a0c511cc6ea801d4b4c19e257039(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1805abbe2aaccad69bc5c748ae7cda077e2c3509dfdbe5fd0378c52e52aeb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f9311bda976180b46f59f86e808c443681f4961e9e93b05bd2e59f1d6b2b727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f5ff2ac3117d74fc28ae89e76d424fa67729d9232da594aac180aa52906c2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbfff3a0507b6403394f6533b9a0bf72a3bdda179a8d809a9bfed2a93092b0e2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3005d1497cdd6201663a36ebaaa81579469756828bfb3909506a692ec2a1ab3f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    region: builtins.str,
    scheme: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    parent_load_balancer: typing.Optional[builtins.str] = None,
    permitted_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    permitted_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_pool: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
