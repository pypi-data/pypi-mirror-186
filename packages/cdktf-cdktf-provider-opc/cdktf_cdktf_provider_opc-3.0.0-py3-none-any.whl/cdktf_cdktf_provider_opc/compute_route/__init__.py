'''
# `opc_compute_route`

Refer to the Terraform Registory for docs: [`opc_compute_route`](https://www.terraform.io/docs/providers/opc/r/compute_route).
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


class ComputeRoute(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeRoute.ComputeRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_route opc_compute_route}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ip_address_prefix: builtins.str,
        name: builtins.str,
        next_hop_vnic_set: builtins.str,
        admin_distance: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_route opc_compute_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#ip_address_prefix ComputeRoute#ip_address_prefix}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#name ComputeRoute#name}.
        :param next_hop_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#next_hop_vnic_set ComputeRoute#next_hop_vnic_set}.
        :param admin_distance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#admin_distance ComputeRoute#admin_distance}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#description ComputeRoute#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#id ComputeRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#tags ComputeRoute#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__757773248feb6157990e250c4f277d84a1ed7a70e13e4917078cb09c0f02de02)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeRouteConfig(
            ip_address_prefix=ip_address_prefix,
            name=name,
            next_hop_vnic_set=next_hop_vnic_set,
            admin_distance=admin_distance,
            description=description,
            id=id,
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

    @jsii.member(jsii_name="resetAdminDistance")
    def reset_admin_distance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminDistance", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="adminDistanceInput")
    def admin_distance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "adminDistanceInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressPrefixInput")
    def ip_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopVnicSetInput")
    def next_hop_vnic_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopVnicSetInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="adminDistance")
    def admin_distance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "adminDistance"))

    @admin_distance.setter
    def admin_distance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4815c2b214bbc7abca339957c0d5e4716eb85116236127b93bd09ab2c49e7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminDistance", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d8ed0d9398c5a9938e64050ac3797e1d0c4f1180ec2919278baea7f9a39be1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__483fb9b1e3528ba26297fc954bd1dbd4e65ddc578f422c29c4671448838da0a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddressPrefix")
    def ip_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddressPrefix"))

    @ip_address_prefix.setter
    def ip_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660c804bc579b519781ab61dbb8649059c974b00881c5b5929207434d02f0fc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__016305a8db229067643c7c5a527b1ae411c44ce78338c5563dcc91827882f6c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopVnicSet")
    def next_hop_vnic_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopVnicSet"))

    @next_hop_vnic_set.setter
    def next_hop_vnic_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14acf9d591aa4ae72dbb946a36452f735f2b1ff4e6de21765b13830656f40042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopVnicSet", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de2ad3c2f871b463e512ff9dfba0e20e2e246ea298b2a656749e70dddc68cbd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeRoute.ComputeRouteConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ip_address_prefix": "ipAddressPrefix",
        "name": "name",
        "next_hop_vnic_set": "nextHopVnicSet",
        "admin_distance": "adminDistance",
        "description": "description",
        "id": "id",
        "tags": "tags",
    },
)
class ComputeRouteConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ip_address_prefix: builtins.str,
        name: builtins.str,
        next_hop_vnic_set: builtins.str,
        admin_distance: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param ip_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#ip_address_prefix ComputeRoute#ip_address_prefix}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#name ComputeRoute#name}.
        :param next_hop_vnic_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#next_hop_vnic_set ComputeRoute#next_hop_vnic_set}.
        :param admin_distance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#admin_distance ComputeRoute#admin_distance}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#description ComputeRoute#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#id ComputeRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#tags ComputeRoute#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d21970563bfb727d0d4af9417500df2274f0ef3bb19d61d4cc610d8558a18d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ip_address_prefix", value=ip_address_prefix, expected_type=type_hints["ip_address_prefix"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument next_hop_vnic_set", value=next_hop_vnic_set, expected_type=type_hints["next_hop_vnic_set"])
            check_type(argname="argument admin_distance", value=admin_distance, expected_type=type_hints["admin_distance"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_address_prefix": ip_address_prefix,
            "name": name,
            "next_hop_vnic_set": next_hop_vnic_set,
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
        if admin_distance is not None:
            self._values["admin_distance"] = admin_distance
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
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
    def ip_address_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#ip_address_prefix ComputeRoute#ip_address_prefix}.'''
        result = self._values.get("ip_address_prefix")
        assert result is not None, "Required property 'ip_address_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#name ComputeRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def next_hop_vnic_set(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#next_hop_vnic_set ComputeRoute#next_hop_vnic_set}.'''
        result = self._values.get("next_hop_vnic_set")
        assert result is not None, "Required property 'next_hop_vnic_set' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_distance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#admin_distance ComputeRoute#admin_distance}.'''
        result = self._values.get("admin_distance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#description ComputeRoute#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#id ComputeRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_route#tags ComputeRoute#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComputeRoute",
    "ComputeRouteConfig",
]

publication.publish()

def _typecheckingstub__757773248feb6157990e250c4f277d84a1ed7a70e13e4917078cb09c0f02de02(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ip_address_prefix: builtins.str,
    name: builtins.str,
    next_hop_vnic_set: builtins.str,
    admin_distance: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4c4815c2b214bbc7abca339957c0d5e4716eb85116236127b93bd09ab2c49e7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d8ed0d9398c5a9938e64050ac3797e1d0c4f1180ec2919278baea7f9a39be1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483fb9b1e3528ba26297fc954bd1dbd4e65ddc578f422c29c4671448838da0a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660c804bc579b519781ab61dbb8649059c974b00881c5b5929207434d02f0fc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016305a8db229067643c7c5a527b1ae411c44ce78338c5563dcc91827882f6c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14acf9d591aa4ae72dbb946a36452f735f2b1ff4e6de21765b13830656f40042(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de2ad3c2f871b463e512ff9dfba0e20e2e246ea298b2a656749e70dddc68cbd2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d21970563bfb727d0d4af9417500df2274f0ef3bb19d61d4cc610d8558a18d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ip_address_prefix: builtins.str,
    name: builtins.str,
    next_hop_vnic_set: builtins.str,
    admin_distance: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
