'''
# `opc_lbaas_server_pool`

Refer to the Terraform Registory for docs: [`opc_lbaas_server_pool`](https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool).
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


class LbaasServerPool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasServerPool.LbaasServerPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool opc_lbaas_server_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        load_balancer: builtins.str,
        name: builtins.str,
        servers: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[typing.Union["LbaasServerPoolHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        vnic_set: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool opc_lbaas_server_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#load_balancer LbaasServerPool#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#name LbaasServerPool#name}.
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#servers LbaasServerPool#servers}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#health_check LbaasServerPool#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#id LbaasServerPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#tags LbaasServerPool#tags}.
        :param vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#vnic_set LbaasServerPool#vnic_set}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__426441446a3bd9ac03bdda1d683dcef3763daf310c7f1bcc78e94d13efd14358)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbaasServerPoolConfig(
            load_balancer=load_balancer,
            name=name,
            servers=servers,
            enabled=enabled,
            health_check=health_check,
            id=id,
            tags=tags,
            vnic_set=vnic_set,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        accepted_return_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accepted_return_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#accepted_return_codes LbaasServerPool#accepted_return_codes}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#healthy_threshold LbaasServerPool#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#interval LbaasServerPool#interval}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#path LbaasServerPool#path}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#timeout LbaasServerPool#timeout}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#type LbaasServerPool#type}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#unhealthy_threshold LbaasServerPool#unhealthy_threshold}.
        '''
        value = LbaasServerPoolHealthCheck(
            accepted_return_codes=accepted_return_codes,
            enabled=enabled,
            healthy_threshold=healthy_threshold,
            interval=interval,
            path=path,
            timeout=timeout,
            type=type,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetVnicSet")
    def reset_vnic_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnicSet", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="consumers")
    def consumers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consumers"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> "LbaasServerPoolHealthCheckOutputReference":
        return typing.cast("LbaasServerPoolHealthCheckOutputReference", jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="operationDetails")
    def operation_details(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "operationDetails"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional["LbaasServerPoolHealthCheck"]:
        return typing.cast(typing.Optional["LbaasServerPoolHealthCheck"], jsii.get(self, "healthCheckInput"))

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
    @jsii.member(jsii_name="serversInput")
    def servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serversInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicSetInput")
    def vnic_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnicSetInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f5031384bdfd85bbd1972857293a0e66690ea81cb6e0df04c67e7f5ac47a61e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c1fbfefaf05b197a1fcb50b7afca071c2be534ed229797f192bf8985fae941)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancer"))

    @load_balancer.setter
    def load_balancer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a9988f8d7d93c4b414aa08c331f86daad86c1b00c56c2902e54c1110cdaef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancer", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2753beda193806c9aad6eb2e592807ed784b3bf3e709fa00da1768348171b0fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="servers")
    def servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servers"))

    @servers.setter
    def servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dcf4dbaaac28e8e7bcd874499f09e1e9632d6e5556d47c75520b7fe56ec9da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servers", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79987ea933ac464f327310731319893ab7ff55979ffa882de47fed6dc6c19cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vnicSet")
    def vnic_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnicSet"))

    @vnic_set.setter
    def vnic_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7ac02c2d5d8231cd779bca613c59c91263cf31c7c4756140ff74b03b8c3cc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnicSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasServerPool.LbaasServerPoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "load_balancer": "loadBalancer",
        "name": "name",
        "servers": "servers",
        "enabled": "enabled",
        "health_check": "healthCheck",
        "id": "id",
        "tags": "tags",
        "vnic_set": "vnicSet",
    },
)
class LbaasServerPoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        load_balancer: builtins.str,
        name: builtins.str,
        servers: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check: typing.Optional[typing.Union["LbaasServerPoolHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        vnic_set: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param load_balancer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#load_balancer LbaasServerPool#load_balancer}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#name LbaasServerPool#name}.
        :param servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#servers LbaasServerPool#servers}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#health_check LbaasServerPool#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#id LbaasServerPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#tags LbaasServerPool#tags}.
        :param vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#vnic_set LbaasServerPool#vnic_set}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(health_check, dict):
            health_check = LbaasServerPoolHealthCheck(**health_check)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e87f32d150074e77d497cddcfeff7069c0a542d459a4adf0f78485c2eb6e6e1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument servers", value=servers, expected_type=type_hints["servers"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vnic_set", value=vnic_set, expected_type=type_hints["vnic_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer": load_balancer,
            "name": name,
            "servers": servers,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if health_check is not None:
            self._values["health_check"] = health_check
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if vnic_set is not None:
            self._values["vnic_set"] = vnic_set

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
    def load_balancer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#load_balancer LbaasServerPool#load_balancer}.'''
        result = self._values.get("load_balancer")
        assert result is not None, "Required property 'load_balancer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#name LbaasServerPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def servers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#servers LbaasServerPool#servers}.'''
        result = self._values.get("servers")
        assert result is not None, "Required property 'servers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check(self) -> typing.Optional["LbaasServerPoolHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#health_check LbaasServerPool#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["LbaasServerPoolHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#id LbaasServerPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#tags LbaasServerPool#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vnic_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#vnic_set LbaasServerPool#vnic_set}.'''
        result = self._values.get("vnic_set")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasServerPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.lbaasServerPool.LbaasServerPoolHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "accepted_return_codes": "acceptedReturnCodes",
        "enabled": "enabled",
        "healthy_threshold": "healthyThreshold",
        "interval": "interval",
        "path": "path",
        "timeout": "timeout",
        "type": "type",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class LbaasServerPoolHealthCheck:
    def __init__(
        self,
        *,
        accepted_return_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param accepted_return_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#accepted_return_codes LbaasServerPool#accepted_return_codes}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#healthy_threshold LbaasServerPool#healthy_threshold}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#interval LbaasServerPool#interval}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#path LbaasServerPool#path}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#timeout LbaasServerPool#timeout}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#type LbaasServerPool#type}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#unhealthy_threshold LbaasServerPool#unhealthy_threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4acc25ee01d043273044c064b0007325acdc340563e7d4edc3780d15be5718b)
            check_type(argname="argument accepted_return_codes", value=accepted_return_codes, expected_type=type_hints["accepted_return_codes"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if accepted_return_codes is not None:
            self._values["accepted_return_codes"] = accepted_return_codes
        if enabled is not None:
            self._values["enabled"] = enabled
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if interval is not None:
            self._values["interval"] = interval
        if path is not None:
            self._values["path"] = path
        if timeout is not None:
            self._values["timeout"] = timeout
        if type is not None:
            self._values["type"] = type
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def accepted_return_codes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#accepted_return_codes LbaasServerPool#accepted_return_codes}.'''
        result = self._values.get("accepted_return_codes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#enabled LbaasServerPool#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#healthy_threshold LbaasServerPool#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#interval LbaasServerPool#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#path LbaasServerPool#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#timeout LbaasServerPool#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#type LbaasServerPool#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/lbaas_server_pool#unhealthy_threshold LbaasServerPool#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbaasServerPoolHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbaasServerPoolHealthCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.lbaasServerPool.LbaasServerPoolHealthCheckOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed78a32e459720b9d56f15a972f5e00a1a30bad5efd4333bba9c1c1fdc0599a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAcceptedReturnCodes")
    def reset_accepted_return_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptedReturnCodes", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="acceptedReturnCodesInput")
    def accepted_return_codes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceptedReturnCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="acceptedReturnCodes")
    def accepted_return_codes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceptedReturnCodes"))

    @accepted_return_codes.setter
    def accepted_return_codes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4817c143acf902d1a9d1be2af35c4d656dcf474602ff6a5c3516be6a01884987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptedReturnCodes", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__ab7324cca2e6688507a9b964a9ace319d84ae2141231734dfc4e8de8559a7247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bf082c68e2e2485574df38b027c862791882fed55510ebb332641da818aec10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27a2bfbde14e65dd2efd05667290dc81ae1aea7e378a9a1d59a2dd36c579eb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5c9390d27a93c18c0a07ead6e227bc93cd7650e2edc38c33d104747d5d3f42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab6bb6d930b29c95d2b462714698642c35ac25a411358aef95b9975a5ec6333)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfcb438b86f64551c12756962a540bf9ffbbe14dfecf5177059d986c74027466)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5aa95f837f5e577d6894f2c2579a4003d04bcd4d66e31533414ce592c33d85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbaasServerPoolHealthCheck]:
        return typing.cast(typing.Optional[LbaasServerPoolHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LbaasServerPoolHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e7648ec1fe335d91ae8908a1cba4c078fb2f528e46e5228259b4f36db63654)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbaasServerPool",
    "LbaasServerPoolConfig",
    "LbaasServerPoolHealthCheck",
    "LbaasServerPoolHealthCheckOutputReference",
]

publication.publish()

def _typecheckingstub__426441446a3bd9ac03bdda1d683dcef3763daf310c7f1bcc78e94d13efd14358(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    load_balancer: builtins.str,
    name: builtins.str,
    servers: typing.Sequence[builtins.str],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[typing.Union[LbaasServerPoolHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    vnic_set: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f5031384bdfd85bbd1972857293a0e66690ea81cb6e0df04c67e7f5ac47a61e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c1fbfefaf05b197a1fcb50b7afca071c2be534ed229797f192bf8985fae941(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a9988f8d7d93c4b414aa08c331f86daad86c1b00c56c2902e54c1110cdaef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2753beda193806c9aad6eb2e592807ed784b3bf3e709fa00da1768348171b0fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dcf4dbaaac28e8e7bcd874499f09e1e9632d6e5556d47c75520b7fe56ec9da9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79987ea933ac464f327310731319893ab7ff55979ffa882de47fed6dc6c19cc3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7ac02c2d5d8231cd779bca613c59c91263cf31c7c4756140ff74b03b8c3cc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e87f32d150074e77d497cddcfeff7069c0a542d459a4adf0f78485c2eb6e6e1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    load_balancer: builtins.str,
    name: builtins.str,
    servers: typing.Sequence[builtins.str],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check: typing.Optional[typing.Union[LbaasServerPoolHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    vnic_set: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4acc25ee01d043273044c064b0007325acdc340563e7d4edc3780d15be5718b(
    *,
    accepted_return_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed78a32e459720b9d56f15a972f5e00a1a30bad5efd4333bba9c1c1fdc0599a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4817c143acf902d1a9d1be2af35c4d656dcf474602ff6a5c3516be6a01884987(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7324cca2e6688507a9b964a9ace319d84ae2141231734dfc4e8de8559a7247(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf082c68e2e2485574df38b027c862791882fed55510ebb332641da818aec10(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27a2bfbde14e65dd2efd05667290dc81ae1aea7e378a9a1d59a2dd36c579eb0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5c9390d27a93c18c0a07ead6e227bc93cd7650e2edc38c33d104747d5d3f42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab6bb6d930b29c95d2b462714698642c35ac25a411358aef95b9975a5ec6333(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcb438b86f64551c12756962a540bf9ffbbe14dfecf5177059d986c74027466(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5aa95f837f5e577d6894f2c2579a4003d04bcd4d66e31533414ce592c33d85e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e7648ec1fe335d91ae8908a1cba4c078fb2f528e46e5228259b4f36db63654(
    value: typing.Optional[LbaasServerPoolHealthCheck],
) -> None:
    """Type checking stubs"""
    pass
