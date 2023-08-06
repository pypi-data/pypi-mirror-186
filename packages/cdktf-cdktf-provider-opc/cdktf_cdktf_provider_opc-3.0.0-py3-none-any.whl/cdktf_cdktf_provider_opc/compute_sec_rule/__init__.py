'''
# `opc_compute_sec_rule`

Refer to the Terraform Registory for docs: [`opc_compute_sec_rule`](https://www.terraform.io/docs/providers/opc/r/compute_sec_rule).
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


class ComputeSecRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeSecRule.ComputeSecRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule opc_compute_sec_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        application: builtins.str,
        destination_list: builtins.str,
        name: builtins.str,
        source_list: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule opc_compute_sec_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#action ComputeSecRule#action}.
        :param application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#application ComputeSecRule#application}.
        :param destination_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#destination_list ComputeSecRule#destination_list}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#name ComputeSecRule#name}.
        :param source_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#source_list ComputeSecRule#source_list}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#description ComputeSecRule#description}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#disabled ComputeSecRule#disabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#id ComputeSecRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf6581c1d8bf753a9727bc5bde3ff4e76860bb28b6028e1f5d3eb9f189ebb4d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeSecRuleConfig(
            action=action,
            application=application,
            destination_list=destination_list,
            name=name,
            source_list=source_list,
            description=description,
            disabled=disabled,
            id=id,
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

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationInput")
    def application_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationListInput")
    def destination_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationListInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceListInput")
    def source_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceListInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c2847899d211348df913a9692a0a9fee8a51c71e325539e3e61c58e2a92492d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "application"))

    @application.setter
    def application(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e37b0aa7e822b3aae8ec912f9c2cd102ad536a5aa7c6b37dfb031f53a412a18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "application", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14189b6eeb1e083f8beac9bd8b187dbd1275c52adbc9dc0820cada04550a22be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationList")
    def destination_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationList"))

    @destination_list.setter
    def destination_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a993dfafebcfda7b43511a4a048d3ece97b1397ea71f84b2dcf4bf461958c47e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationList", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7388d1c470a8020b0d3a1408ffb83ac2cdd14f5a40d854835f12f9fc262dd53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf650d0bd13a2971f7648b70cacfd8dcc44c207738a6f2951bda8d6c19c37d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6726bfcca39e643fccffc43bc4fa8875f30aab8db1391072ea99e9b635744334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceList")
    def source_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceList"))

    @source_list.setter
    def source_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc718098148a0fb67d348e9ad7eaa5293a84517ca41c2b99c5fcb275434f4da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceList", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeSecRule.ComputeSecRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "application": "application",
        "destination_list": "destinationList",
        "name": "name",
        "source_list": "sourceList",
        "description": "description",
        "disabled": "disabled",
        "id": "id",
    },
)
class ComputeSecRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action: builtins.str,
        application: builtins.str,
        destination_list: builtins.str,
        name: builtins.str,
        source_list: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#action ComputeSecRule#action}.
        :param application: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#application ComputeSecRule#application}.
        :param destination_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#destination_list ComputeSecRule#destination_list}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#name ComputeSecRule#name}.
        :param source_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#source_list ComputeSecRule#source_list}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#description ComputeSecRule#description}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#disabled ComputeSecRule#disabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#id ComputeSecRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d53983a591f144a4c70dfa5b6f8191d9dfef75a57cc219947fd4b46c82d282f6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument destination_list", value=destination_list, expected_type=type_hints["destination_list"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_list", value=source_list, expected_type=type_hints["source_list"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "application": application,
            "destination_list": destination_list,
            "name": name,
            "source_list": source_list,
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
        if disabled is not None:
            self._values["disabled"] = disabled
        if id is not None:
            self._values["id"] = id

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
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#action ComputeSecRule#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#application ComputeSecRule#application}.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_list(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#destination_list ComputeSecRule#destination_list}.'''
        result = self._values.get("destination_list")
        assert result is not None, "Required property 'destination_list' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#name ComputeSecRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_list(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#source_list ComputeSecRule#source_list}.'''
        result = self._values.get("source_list")
        assert result is not None, "Required property 'source_list' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#description ComputeSecRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#disabled ComputeSecRule#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_sec_rule#id ComputeSecRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeSecRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComputeSecRule",
    "ComputeSecRuleConfig",
]

publication.publish()

def _typecheckingstub__caf6581c1d8bf753a9727bc5bde3ff4e76860bb28b6028e1f5d3eb9f189ebb4d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    application: builtins.str,
    destination_list: builtins.str,
    name: builtins.str,
    source_list: builtins.str,
    description: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9c2847899d211348df913a9692a0a9fee8a51c71e325539e3e61c58e2a92492d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e37b0aa7e822b3aae8ec912f9c2cd102ad536a5aa7c6b37dfb031f53a412a18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14189b6eeb1e083f8beac9bd8b187dbd1275c52adbc9dc0820cada04550a22be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a993dfafebcfda7b43511a4a048d3ece97b1397ea71f84b2dcf4bf461958c47e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7388d1c470a8020b0d3a1408ffb83ac2cdd14f5a40d854835f12f9fc262dd53(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf650d0bd13a2971f7648b70cacfd8dcc44c207738a6f2951bda8d6c19c37d6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6726bfcca39e643fccffc43bc4fa8875f30aab8db1391072ea99e9b635744334(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc718098148a0fb67d348e9ad7eaa5293a84517ca41c2b99c5fcb275434f4da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53983a591f144a4c70dfa5b6f8191d9dfef75a57cc219947fd4b46c82d282f6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    application: builtins.str,
    destination_list: builtins.str,
    name: builtins.str,
    source_list: builtins.str,
    description: typing.Optional[builtins.str] = None,
    disabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
