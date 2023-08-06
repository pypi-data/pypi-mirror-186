'''
# `opc_compute_vpn_endpoint_v2`

Refer to the Terraform Registory for docs: [`opc_compute_vpn_endpoint_v2`](https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2).
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


class ComputeVpnEndpointV2(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2 opc_compute_vpn_endpoint_v2}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        customer_vpn_gateway: builtins.str,
        ip_network: builtins.str,
        name: builtins.str,
        pre_shared_key: builtins.str,
        reachable_routes: typing.Sequence[builtins.str],
        vnic_sets: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ike_identifier: typing.Optional[builtins.str] = None,
        phase_one_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseOneSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        phase_two_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseTwoSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2 opc_compute_vpn_endpoint_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param customer_vpn_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.
        :param pre_shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.
        :param reachable_routes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.
        :param phase_one_settings: phase_one_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        :param phase_two_settings: phase_two_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        :param require_perfect_forward_secrecy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032d6c1dfbc743c448ab50c223c00ab76c0583ae928e9ba726d6759cd3ae7798)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeVpnEndpointV2Config(
            customer_vpn_gateway=customer_vpn_gateway,
            ip_network=ip_network,
            name=name,
            pre_shared_key=pre_shared_key,
            reachable_routes=reachable_routes,
            vnic_sets=vnic_sets,
            description=description,
            enabled=enabled,
            id=id,
            ike_identifier=ike_identifier,
            phase_one_settings=phase_one_settings,
            phase_two_settings=phase_two_settings,
            require_perfect_forward_secrecy=require_perfect_forward_secrecy,
            tags=tags,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPhaseOneSettings")
    def put_phase_one_settings(
        self,
        *,
        dh_group: builtins.str,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        value = ComputeVpnEndpointV2PhaseOneSettings(
            dh_group=dh_group, encryption=encryption, hash=hash, lifetime=lifetime
        )

        return typing.cast(None, jsii.invoke(self, "putPhaseOneSettings", [value]))

    @jsii.member(jsii_name="putPhaseTwoSettings")
    def put_phase_two_settings(
        self,
        *,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        value = ComputeVpnEndpointV2PhaseTwoSettings(
            encryption=encryption, hash=hash, lifetime=lifetime
        )

        return typing.cast(None, jsii.invoke(self, "putPhaseTwoSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.
        '''
        value = ComputeVpnEndpointV2Timeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIkeIdentifier")
    def reset_ike_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIkeIdentifier", []))

    @jsii.member(jsii_name="resetPhaseOneSettings")
    def reset_phase_one_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhaseOneSettings", []))

    @jsii.member(jsii_name="resetPhaseTwoSettings")
    def reset_phase_two_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhaseTwoSettings", []))

    @jsii.member(jsii_name="resetRequirePerfectForwardSecrecy")
    def reset_require_perfect_forward_secrecy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePerfectForwardSecrecy", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="localGatewayIpAddress")
    def local_gateway_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localGatewayIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="localGatewayPrivateIpAddress")
    def local_gateway_private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localGatewayPrivateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="phaseOneSettings")
    def phase_one_settings(
        self,
    ) -> "ComputeVpnEndpointV2PhaseOneSettingsOutputReference":
        return typing.cast("ComputeVpnEndpointV2PhaseOneSettingsOutputReference", jsii.get(self, "phaseOneSettings"))

    @builtins.property
    @jsii.member(jsii_name="phaseTwoSettings")
    def phase_two_settings(
        self,
    ) -> "ComputeVpnEndpointV2PhaseTwoSettingsOutputReference":
        return typing.cast("ComputeVpnEndpointV2PhaseTwoSettingsOutputReference", jsii.get(self, "phaseTwoSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeVpnEndpointV2TimeoutsOutputReference":
        return typing.cast("ComputeVpnEndpointV2TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tunnelStatus")
    def tunnel_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnelStatus"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="customerVpnGatewayInput")
    def customer_vpn_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerVpnGatewayInput"))

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
    @jsii.member(jsii_name="ikeIdentifierInput")
    def ike_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseOneSettingsInput")
    def phase_one_settings_input(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"]:
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"], jsii.get(self, "phaseOneSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseTwoSettingsInput")
    def phase_two_settings_input(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"]:
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"], jsii.get(self, "phaseTwoSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="preSharedKeyInput")
    def pre_shared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preSharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="reachableRoutesInput")
    def reachable_routes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "reachableRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePerfectForwardSecrecyInput")
    def require_perfect_forward_secrecy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requirePerfectForwardSecrecyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicSetsInput")
    def vnic_sets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vnicSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="customerVpnGateway")
    def customer_vpn_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerVpnGateway"))

    @customer_vpn_gateway.setter
    def customer_vpn_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c9a6f95d937e7e1418546e8e216e3a6e038d356cdda8b7780bd952cd45d0b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerVpnGateway", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__153b1a53cda665de050fb0b65e3e0a25cbabe8a304eb65fc34d6dfb3ff3c3101)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6dd70ebb8bf412facaf173aed23dcaeb18d5a0cedb15c9359c0713f3a3bba33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfde3d0489f54aa0dbc3e12fcfb3c8b15413d2629d2d804efa8837e2a7d57b0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIdentifier")
    def ike_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIdentifier"))

    @ike_identifier.setter
    def ike_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ba7421b478d5db56d5fcad6cf16755b1ddca0c8c7cec2e15d8ff042147b089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e96e5b6ee6f0554ea2bcc465dabc62b76f27a5dea961047bee8c6bfcb6f345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21adce51a33a433db6091d9db58dce3af11b5c06f438bdf8f23d13112218a930)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preSharedKey")
    def pre_shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preSharedKey"))

    @pre_shared_key.setter
    def pre_shared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd779c1d93b587834e7b85d410e0e66053a3e7aa5bb08ac1c561e78a9a221147)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preSharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="reachableRoutes")
    def reachable_routes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "reachableRoutes"))

    @reachable_routes.setter
    def reachable_routes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b103a70c256c3b93793c1d24ba4700687cc5e1bce402aa16c3a8e2cfc0159b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reachableRoutes", value)

    @builtins.property
    @jsii.member(jsii_name="requirePerfectForwardSecrecy")
    def require_perfect_forward_secrecy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requirePerfectForwardSecrecy"))

    @require_perfect_forward_secrecy.setter
    def require_perfect_forward_secrecy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64728d226ffb843ece8fe14eb640738daf1b424c7f10774567669ab1e9d1fb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePerfectForwardSecrecy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e2b58960b3823395ca514ce72af6ad28207c75088718c76e8f60d42c6f98b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vnicSets")
    def vnic_sets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vnicSets"))

    @vnic_sets.setter
    def vnic_sets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c6385ef2e0830661e827992c5aff5e28747cb0e7eacf5273a8c87606da7b3c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnicSets", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "customer_vpn_gateway": "customerVpnGateway",
        "ip_network": "ipNetwork",
        "name": "name",
        "pre_shared_key": "preSharedKey",
        "reachable_routes": "reachableRoutes",
        "vnic_sets": "vnicSets",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "ike_identifier": "ikeIdentifier",
        "phase_one_settings": "phaseOneSettings",
        "phase_two_settings": "phaseTwoSettings",
        "require_perfect_forward_secrecy": "requirePerfectForwardSecrecy",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ComputeVpnEndpointV2Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        customer_vpn_gateway: builtins.str,
        ip_network: builtins.str,
        name: builtins.str,
        pre_shared_key: builtins.str,
        reachable_routes: typing.Sequence[builtins.str],
        vnic_sets: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ike_identifier: typing.Optional[builtins.str] = None,
        phase_one_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseOneSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        phase_two_settings: typing.Optional[typing.Union["ComputeVpnEndpointV2PhaseTwoSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeVpnEndpointV2Timeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param customer_vpn_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.
        :param pre_shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.
        :param reachable_routes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.
        :param phase_one_settings: phase_one_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        :param phase_two_settings: phase_two_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        :param require_perfect_forward_secrecy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(phase_one_settings, dict):
            phase_one_settings = ComputeVpnEndpointV2PhaseOneSettings(**phase_one_settings)
        if isinstance(phase_two_settings, dict):
            phase_two_settings = ComputeVpnEndpointV2PhaseTwoSettings(**phase_two_settings)
        if isinstance(timeouts, dict):
            timeouts = ComputeVpnEndpointV2Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a80d9c9653878ebdb842ef35420fb515656501d010f594411f9972c4312c33)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument customer_vpn_gateway", value=customer_vpn_gateway, expected_type=type_hints["customer_vpn_gateway"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pre_shared_key", value=pre_shared_key, expected_type=type_hints["pre_shared_key"])
            check_type(argname="argument reachable_routes", value=reachable_routes, expected_type=type_hints["reachable_routes"])
            check_type(argname="argument vnic_sets", value=vnic_sets, expected_type=type_hints["vnic_sets"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ike_identifier", value=ike_identifier, expected_type=type_hints["ike_identifier"])
            check_type(argname="argument phase_one_settings", value=phase_one_settings, expected_type=type_hints["phase_one_settings"])
            check_type(argname="argument phase_two_settings", value=phase_two_settings, expected_type=type_hints["phase_two_settings"])
            check_type(argname="argument require_perfect_forward_secrecy", value=require_perfect_forward_secrecy, expected_type=type_hints["require_perfect_forward_secrecy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_vpn_gateway": customer_vpn_gateway,
            "ip_network": ip_network,
            "name": name,
            "pre_shared_key": pre_shared_key,
            "reachable_routes": reachable_routes,
            "vnic_sets": vnic_sets,
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
        if ike_identifier is not None:
            self._values["ike_identifier"] = ike_identifier
        if phase_one_settings is not None:
            self._values["phase_one_settings"] = phase_one_settings
        if phase_two_settings is not None:
            self._values["phase_two_settings"] = phase_two_settings
        if require_perfect_forward_secrecy is not None:
            self._values["require_perfect_forward_secrecy"] = require_perfect_forward_secrecy
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def customer_vpn_gateway(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#customer_vpn_gateway ComputeVpnEndpointV2#customer_vpn_gateway}.'''
        result = self._values.get("customer_vpn_gateway")
        assert result is not None, "Required property 'customer_vpn_gateway' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_network(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ip_network ComputeVpnEndpointV2#ip_network}.'''
        result = self._values.get("ip_network")
        assert result is not None, "Required property 'ip_network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#name ComputeVpnEndpointV2#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pre_shared_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#pre_shared_key ComputeVpnEndpointV2#pre_shared_key}.'''
        result = self._values.get("pre_shared_key")
        assert result is not None, "Required property 'pre_shared_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reachable_routes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#reachable_routes ComputeVpnEndpointV2#reachable_routes}.'''
        result = self._values.get("reachable_routes")
        assert result is not None, "Required property 'reachable_routes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vnic_sets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#vnic_sets ComputeVpnEndpointV2#vnic_sets}.'''
        result = self._values.get("vnic_sets")
        assert result is not None, "Required property 'vnic_sets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#description ComputeVpnEndpointV2#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#enabled ComputeVpnEndpointV2#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#id ComputeVpnEndpointV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ike_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#ike_identifier ComputeVpnEndpointV2#ike_identifier}.'''
        result = self._values.get("ike_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phase_one_settings(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"]:
        '''phase_one_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_one_settings ComputeVpnEndpointV2#phase_one_settings}
        '''
        result = self._values.get("phase_one_settings")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseOneSettings"], result)

    @builtins.property
    def phase_two_settings(
        self,
    ) -> typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"]:
        '''phase_two_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#phase_two_settings ComputeVpnEndpointV2#phase_two_settings}
        '''
        result = self._values.get("phase_two_settings")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2PhaseTwoSettings"], result)

    @builtins.property
    def require_perfect_forward_secrecy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#require_perfect_forward_secrecy ComputeVpnEndpointV2#require_perfect_forward_secrecy}.'''
        result = self._values.get("require_perfect_forward_secrecy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#tags ComputeVpnEndpointV2#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeVpnEndpointV2Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#timeouts ComputeVpnEndpointV2#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeVpnEndpointV2Timeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseOneSettings",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "encryption": "encryption",
        "hash": "hash",
        "lifetime": "lifetime",
    },
)
class ComputeVpnEndpointV2PhaseOneSettings:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd19a6fab824d87ad344933815d0948490adc3c4611a197570b01712aa7bb76e)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument hash", value=hash, expected_type=type_hints["hash"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dh_group": dh_group,
            "encryption": encryption,
            "hash": hash,
        }
        if lifetime is not None:
            self._values["lifetime"] = lifetime

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#dh_group ComputeVpnEndpointV2#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.'''
        result = self._values.get("encryption")
        assert result is not None, "Required property 'encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.'''
        result = self._values.get("hash")
        assert result is not None, "Required property 'hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.'''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2PhaseOneSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2PhaseOneSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseOneSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2baa7aa6d8dc2da2246a0845a1bbbbcb00298bd67bcb400ef33cfcbc90df2b1b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hashInput")
    def hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeInput")
    def lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fea15fee4f9008dd27e885d343daf430b0e79df8f54ce40c3ca33d4e7e78601)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0809887270631b90f033f84cfafdd7278985c08a5096da5ec8577f5ec30e89e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hash"))

    @hash.setter
    def hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c67d31cdf72e6ab0e5acb24a10bc6a9cf7ccc9cd8ec972a55293ed50180747ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hash", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0104efc9057ec97f5eb5660bce32f8066e151641d18b79f7b0a76d5bce88b76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeVpnEndpointV2PhaseOneSettings]:
        return typing.cast(typing.Optional[ComputeVpnEndpointV2PhaseOneSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeVpnEndpointV2PhaseOneSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026c51b75487463d9f9a4648f2179617b2b3fe135f5f63c447e202f8d3548143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseTwoSettings",
    jsii_struct_bases=[],
    name_mapping={"encryption": "encryption", "hash": "hash", "lifetime": "lifetime"},
)
class ComputeVpnEndpointV2PhaseTwoSettings:
    def __init__(
        self,
        *,
        encryption: builtins.str,
        hash: builtins.str,
        lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.
        :param hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.
        :param lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1dfa0f602293ea81dcb983d069ae92c212b01e36d018241006505342d9defe)
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument hash", value=hash, expected_type=type_hints["hash"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption": encryption,
            "hash": hash,
        }
        if lifetime is not None:
            self._values["lifetime"] = lifetime

    @builtins.property
    def encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#encryption ComputeVpnEndpointV2#encryption}.'''
        result = self._values.get("encryption")
        assert result is not None, "Required property 'encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#hash ComputeVpnEndpointV2#hash}.'''
        result = self._values.get("hash")
        assert result is not None, "Required property 'hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#lifetime ComputeVpnEndpointV2#lifetime}.'''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2PhaseTwoSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2PhaseTwoSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2PhaseTwoSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d0d3c29ff5fa1c5363a78b66d29a06d1931ffc61eb18ba5ce143b7854e6292c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hashInput")
    def hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeInput")
    def lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19d58a916a240b8efaf704ab1c4ccea83e5e547f7513ed50563be28c608c450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hash"))

    @hash.setter
    def hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d40f11d196a05ed38db7f2df96e232fda418234b2fe0a289fcf5810819910c71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hash", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115c14211a41b342a0a650a9c60a8f2cba3931bbdc6ca843ba7124ac3afd4bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings]:
        return typing.cast(typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9ebf9b2adc1ddb7040aedd499d6db05069fe94c9c0b69c9c0645a8c8f67ed1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeVpnEndpointV2Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6bcd115b1ff9ea10c8af068058c9319b02819cafe1b1f2371a7a0f2958572f9)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#create ComputeVpnEndpointV2#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#delete ComputeVpnEndpointV2#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_vpn_endpoint_v2#update ComputeVpnEndpointV2#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeVpnEndpointV2Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeVpnEndpointV2TimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeVpnEndpointV2.ComputeVpnEndpointV2TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2213ee97847f89e1478a496ba4421da082068a7f71ce47dae16fd9141c877471)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224fb19033470ed0a692a8aee3deb71287302531fc84df993b572479e970690a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1776e9fbb997befc19acd54f5a6790caee85e8b3d6e6d6e8d87b6c99d74f1fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f88d33a03c062de9140941bfacecbfab8df2aca7804994e86dc8acf44d38a66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab1dea2e6c10d8e772e51f0f31e8763a20f761b1f91d0a2ae7ad2d074f5896b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeVpnEndpointV2",
    "ComputeVpnEndpointV2Config",
    "ComputeVpnEndpointV2PhaseOneSettings",
    "ComputeVpnEndpointV2PhaseOneSettingsOutputReference",
    "ComputeVpnEndpointV2PhaseTwoSettings",
    "ComputeVpnEndpointV2PhaseTwoSettingsOutputReference",
    "ComputeVpnEndpointV2Timeouts",
    "ComputeVpnEndpointV2TimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__032d6c1dfbc743c448ab50c223c00ab76c0583ae928e9ba726d6759cd3ae7798(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    customer_vpn_gateway: builtins.str,
    ip_network: builtins.str,
    name: builtins.str,
    pre_shared_key: builtins.str,
    reachable_routes: typing.Sequence[builtins.str],
    vnic_sets: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ike_identifier: typing.Optional[builtins.str] = None,
    phase_one_settings: typing.Optional[typing.Union[ComputeVpnEndpointV2PhaseOneSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    phase_two_settings: typing.Optional[typing.Union[ComputeVpnEndpointV2PhaseTwoSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__d1c9a6f95d937e7e1418546e8e216e3a6e038d356cdda8b7780bd952cd45d0b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153b1a53cda665de050fb0b65e3e0a25cbabe8a304eb65fc34d6dfb3ff3c3101(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6dd70ebb8bf412facaf173aed23dcaeb18d5a0cedb15c9359c0713f3a3bba33(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfde3d0489f54aa0dbc3e12fcfb3c8b15413d2629d2d804efa8837e2a7d57b0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ba7421b478d5db56d5fcad6cf16755b1ddca0c8c7cec2e15d8ff042147b089(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e96e5b6ee6f0554ea2bcc465dabc62b76f27a5dea961047bee8c6bfcb6f345(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21adce51a33a433db6091d9db58dce3af11b5c06f438bdf8f23d13112218a930(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd779c1d93b587834e7b85d410e0e66053a3e7aa5bb08ac1c561e78a9a221147(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b103a70c256c3b93793c1d24ba4700687cc5e1bce402aa16c3a8e2cfc0159b1b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64728d226ffb843ece8fe14eb640738daf1b424c7f10774567669ab1e9d1fb7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e2b58960b3823395ca514ce72af6ad28207c75088718c76e8f60d42c6f98b8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6385ef2e0830661e827992c5aff5e28747cb0e7eacf5273a8c87606da7b3c6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a80d9c9653878ebdb842ef35420fb515656501d010f594411f9972c4312c33(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    customer_vpn_gateway: builtins.str,
    ip_network: builtins.str,
    name: builtins.str,
    pre_shared_key: builtins.str,
    reachable_routes: typing.Sequence[builtins.str],
    vnic_sets: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    ike_identifier: typing.Optional[builtins.str] = None,
    phase_one_settings: typing.Optional[typing.Union[ComputeVpnEndpointV2PhaseOneSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    phase_two_settings: typing.Optional[typing.Union[ComputeVpnEndpointV2PhaseTwoSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    require_perfect_forward_secrecy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd19a6fab824d87ad344933815d0948490adc3c4611a197570b01712aa7bb76e(
    *,
    dh_group: builtins.str,
    encryption: builtins.str,
    hash: builtins.str,
    lifetime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2baa7aa6d8dc2da2246a0845a1bbbbcb00298bd67bcb400ef33cfcbc90df2b1b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fea15fee4f9008dd27e885d343daf430b0e79df8f54ce40c3ca33d4e7e78601(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0809887270631b90f033f84cfafdd7278985c08a5096da5ec8577f5ec30e89e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c67d31cdf72e6ab0e5acb24a10bc6a9cf7ccc9cd8ec972a55293ed50180747ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0104efc9057ec97f5eb5660bce32f8066e151641d18b79f7b0a76d5bce88b76(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026c51b75487463d9f9a4648f2179617b2b3fe135f5f63c447e202f8d3548143(
    value: typing.Optional[ComputeVpnEndpointV2PhaseOneSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1dfa0f602293ea81dcb983d069ae92c212b01e36d018241006505342d9defe(
    *,
    encryption: builtins.str,
    hash: builtins.str,
    lifetime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0d3c29ff5fa1c5363a78b66d29a06d1931ffc61eb18ba5ce143b7854e6292c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19d58a916a240b8efaf704ab1c4ccea83e5e547f7513ed50563be28c608c450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d40f11d196a05ed38db7f2df96e232fda418234b2fe0a289fcf5810819910c71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115c14211a41b342a0a650a9c60a8f2cba3931bbdc6ca843ba7124ac3afd4bfc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9ebf9b2adc1ddb7040aedd499d6db05069fe94c9c0b69c9c0645a8c8f67ed1(
    value: typing.Optional[ComputeVpnEndpointV2PhaseTwoSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6bcd115b1ff9ea10c8af068058c9319b02819cafe1b1f2371a7a0f2958572f9(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2213ee97847f89e1478a496ba4421da082068a7f71ce47dae16fd9141c877471(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224fb19033470ed0a692a8aee3deb71287302531fc84df993b572479e970690a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1776e9fbb997befc19acd54f5a6790caee85e8b3d6e6d6e8d87b6c99d74f1fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f88d33a03c062de9140941bfacecbfab8df2aca7804994e86dc8acf44d38a66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab1dea2e6c10d8e772e51f0f31e8763a20f761b1f91d0a2ae7ad2d074f5896b(
    value: typing.Optional[typing.Union[ComputeVpnEndpointV2Timeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
