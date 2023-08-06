'''
# `opc_lbaas_listener`

Refer to the Terraform Registory for docs: [`opc_lbaas_listener`](https://www.terraform.io/docs/providers/opc/r/lbaas_listener).
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


class LbaasListener(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasListener.LbaasListener",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener opc_lbaas_listener}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        balancer_protocol: builtins.str,
        load_balancer: builtins.str,
        name: builtins.str,
        port: jsii.Number,
        server_protocol: builtins.str,
        certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_pool: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener opc_lbaas_listener} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param balancer_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#balancer_protocol LbaasListener#balancer_protocol}.
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#load_balancer LbaasListener#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#name LbaasListener#name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#port LbaasListener#port}.
        :param server_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_protocol LbaasListener#server_protocol}.
        :param certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#certificates LbaasListener#certificates}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#enabled LbaasListener#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#id LbaasListener#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#path_prefixes LbaasListener#path_prefixes}.
        :param policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#policies LbaasListener#policies}.
        :param server_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_pool LbaasListener#server_pool}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#tags LbaasListener#tags}.
        :param virtual_hosts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#virtual_hosts LbaasListener#virtual_hosts}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72f325c094bbd103228a7428374a7cb4946f3503fe56cf60ab84c6dcab7e482)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbaasListenerConfig(
            balancer_protocol=balancer_protocol,
            load_balancer=load_balancer,
            name=name,
            port=port,
            server_protocol=server_protocol,
            certificates=certificates,
            enabled=enabled,
            id=id,
            path_prefixes=path_prefixes,
            policies=policies,
            server_pool=server_pool,
            tags=tags,
            virtual_hosts=virtual_hosts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCertificates")
    def reset_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificates", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPathPrefixes")
    def reset_path_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPrefixes", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @jsii.member(jsii_name="resetServerPool")
    def reset_server_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerPool", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetVirtualHosts")
    def reset_virtual_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualHosts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="operationDetails")
    def operation_details(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationDetails"))

    @builtins.property
    @jsii.member(jsii_name="parentListener")
    def parent_listener(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentListener"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="balancerProtocolInput")
    def balancer_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancerProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatesInput")
    def certificates_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificatesInput"))

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
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixesInput")
    def path_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="serverPoolInput")
    def server_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="serverProtocolInput")
    def server_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHostsInput")
    def virtual_hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "virtualHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="balancerProtocol")
    def balancer_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancerProtocol"))

    @balancer_protocol.setter
    def balancer_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e32c52f7789a08b82fefeb300ed98ab6105d80bef719197fdd4f4dbfcf304d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancerProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="certificates")
    def certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificates"))

    @certificates.setter
    def certificates(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19eee491570c1939a2032bdcd924d021b1f9cb1061f9ba0b48663648dde6a9f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificates", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__761632ef8b585ea4117624830fa4d765902beaa5ec28038c9952f84494635ba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c0dc4c1823fc9dbdbd59d6db2014ed3d3648402f3d2acd25ba63043a3398b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancer"))

    @load_balancer.setter
    def load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a15ea1a3f30eea66fca67a6ea82200a7b4d3029a7684ca48dfc9fd8330e7414c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b7940559294fcc2dff3b305dcc7a58649eec424a066e28bd6db91d36e263ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pathPrefixes")
    def path_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pathPrefixes"))

    @path_prefixes.setter
    def path_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d24961ca864671ea25603fb8e393a7c72102017e33f50f698b4dba9e7501e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8176f7d0fdeb11941d7285260acb9e2790e6f6ac3cc3ab17117eb145a33c4a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b82b1c4fd742e7859e19f1935476058caeb4dc83c3fe68b18c9a43623b4c5ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="serverPool")
    def server_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverPool"))

    @server_pool.setter
    def server_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e681b6d11e38b568e138d43a03f744f368adb37d0a1679625a59aef681ee93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverPool", value)

    @builtins.property
    @jsii.member(jsii_name="serverProtocol")
    def server_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverProtocol"))

    @server_protocol.setter
    def server_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e28a5599e666b39defcc3a3ea3ca0d014b5f5ad7f51ac8dacb815e4589e116e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a16ce7af7c835fd67776b1af9cf59a5a07e81c78ff6af3d407504d4e88b49cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHosts")
    def virtual_hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "virtualHosts"))

    @virtual_hosts.setter
    def virtual_hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c7a8a54e9da12f7896f50fde282a3c116cbf5d528bf3019ce8fc746b1a2d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHosts", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasListener.LbaasListenerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "balancer_protocol": "balancerProtocol",
        "load_balancer": "loadBalancer",
        "name": "name",
        "port": "port",
        "server_protocol": "serverProtocol",
        "certificates": "certificates",
        "enabled": "enabled",
        "id": "id",
        "path_prefixes": "pathPrefixes",
        "policies": "policies",
        "server_pool": "serverPool",
        "tags": "tags",
        "virtual_hosts": "virtualHosts",
    },
)
class LbaasListenerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        balancer_protocol: builtins.str,
        load_balancer: builtins.str,
        name: builtins.str,
        port: jsii.Number,
        server_protocol: builtins.str,
        certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_pool: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        virtual_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param balancer_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#balancer_protocol LbaasListener#balancer_protocol}.
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#load_balancer LbaasListener#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#name LbaasListener#name}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#port LbaasListener#port}.
        :param server_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_protocol LbaasListener#server_protocol}.
        :param certificates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#certificates LbaasListener#certificates}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#enabled LbaasListener#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#id LbaasListener#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#path_prefixes LbaasListener#path_prefixes}.
        :param policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#policies LbaasListener#policies}.
        :param server_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_pool LbaasListener#server_pool}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#tags LbaasListener#tags}.
        :param virtual_hosts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#virtual_hosts LbaasListener#virtual_hosts}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f377f0d4b0f6d05ab1733b01d50708be77abb6a8be76f1cbe90c3e674c3a3a7b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument balancer_protocol", value=balancer_protocol, expected_type=type_hints["balancer_protocol"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument server_protocol", value=server_protocol, expected_type=type_hints["server_protocol"])
            check_type(argname="argument certificates", value=certificates, expected_type=type_hints["certificates"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path_prefixes", value=path_prefixes, expected_type=type_hints["path_prefixes"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument server_pool", value=server_pool, expected_type=type_hints["server_pool"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument virtual_hosts", value=virtual_hosts, expected_type=type_hints["virtual_hosts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "balancer_protocol": balancer_protocol,
            "load_balancer": load_balancer,
            "name": name,
            "port": port,
            "server_protocol": server_protocol,
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
        if certificates is not None:
            self._values["certificates"] = certificates
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if path_prefixes is not None:
            self._values["path_prefixes"] = path_prefixes
        if policies is not None:
            self._values["policies"] = policies
        if server_pool is not None:
            self._values["server_pool"] = server_pool
        if tags is not None:
            self._values["tags"] = tags
        if virtual_hosts is not None:
            self._values["virtual_hosts"] = virtual_hosts

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
    def balancer_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#balancer_protocol LbaasListener#balancer_protocol}.'''
        result = self._values.get("balancer_protocol")
        assert result is not None, "Required property 'balancer_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#load_balancer LbaasListener#load_balancer}.'''
        result = self._values.get("load_balancer")
        assert result is not None, "Required property 'load_balancer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#name LbaasListener#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#port LbaasListener#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def server_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_protocol LbaasListener#server_protocol}.'''
        result = self._values.get("server_protocol")
        assert result is not None, "Required property 'server_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificates(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#certificates LbaasListener#certificates}.'''
        result = self._values.get("certificates")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#enabled LbaasListener#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#id LbaasListener#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#path_prefixes LbaasListener#path_prefixes}.'''
        result = self._values.get("path_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#policies LbaasListener#policies}.'''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_pool(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#server_pool LbaasListener#server_pool}.'''
        result = self._values.get("server_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#tags LbaasListener#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def virtual_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_listener#virtual_hosts LbaasListener#virtual_hosts}.'''
        result = self._values.get("virtual_hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasListenerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LbaasListener",
    "LbaasListenerConfig",
]

publication.publish()

def _typecheckingstub__c72f325c094bbd103228a7428374a7cb4946f3503fe56cf60ab84c6dcab7e482(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    balancer_protocol: builtins.str,
    load_balancer: builtins.str,
    name: builtins.str,
    port: jsii.Number,
    server_protocol: builtins.str,
    certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_pool: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    virtual_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__b8e32c52f7789a08b82fefeb300ed98ab6105d80bef719197fdd4f4dbfcf304d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19eee491570c1939a2032bdcd924d021b1f9cb1061f9ba0b48663648dde6a9f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761632ef8b585ea4117624830fa4d765902beaa5ec28038c9952f84494635ba0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c0dc4c1823fc9dbdbd59d6db2014ed3d3648402f3d2acd25ba63043a3398b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15ea1a3f30eea66fca67a6ea82200a7b4d3029a7684ca48dfc9fd8330e7414c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7940559294fcc2dff3b305dcc7a58649eec424a066e28bd6db91d36e263ae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d24961ca864671ea25603fb8e393a7c72102017e33f50f698b4dba9e7501e8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8176f7d0fdeb11941d7285260acb9e2790e6f6ac3cc3ab17117eb145a33c4a5e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b82b1c4fd742e7859e19f1935476058caeb4dc83c3fe68b18c9a43623b4c5ad(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e681b6d11e38b568e138d43a03f744f368adb37d0a1679625a59aef681ee93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28a5599e666b39defcc3a3ea3ca0d014b5f5ad7f51ac8dacb815e4589e116e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a16ce7af7c835fd67776b1af9cf59a5a07e81c78ff6af3d407504d4e88b49cd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6c7a8a54e9da12f7896f50fde282a3c116cbf5d528bf3019ce8fc746b1a2d69(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f377f0d4b0f6d05ab1733b01d50708be77abb6a8be76f1cbe90c3e674c3a3a7b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    balancer_protocol: builtins.str,
    load_balancer: builtins.str,
    name: builtins.str,
    port: jsii.Number,
    server_protocol: builtins.str,
    certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    path_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    server_pool: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    virtual_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
