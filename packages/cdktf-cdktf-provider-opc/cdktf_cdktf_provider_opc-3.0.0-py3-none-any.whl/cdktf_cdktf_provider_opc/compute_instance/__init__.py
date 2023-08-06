'''
# `opc_compute_instance`

Refer to the Terraform Registory for docs: [`opc_compute_instance`](https://www.terraform.io/docs/providers/opc/r/compute_instance).
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


class ComputeInstance(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_instance opc_compute_instance}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        shape: builtins.str,
        boot_order: typing.Optional[typing.Sequence[jsii.Number]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_list: typing.Optional[builtins.str] = None,
        instance_attributes: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        networking_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceNetworkingInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reverse_dns: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceStorage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_instance opc_compute_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#name ComputeInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#shape ComputeInstance#shape}.
        :param boot_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#boot_order ComputeInstance#boot_order}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#desired_state ComputeInstance#desired_state}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#hostname ComputeInstance#hostname}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#id ComputeInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#image_list ComputeInstance#image_list}.
        :param instance_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#instance_attributes ComputeInstance#instance_attributes}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#label ComputeInstance#label}.
        :param networking_info: networking_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#networking_info ComputeInstance#networking_info}
        :param reverse_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#reverse_dns ComputeInstance#reverse_dns}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ssh_keys ComputeInstance#ssh_keys}.
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#storage ComputeInstance#storage}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#tags ComputeInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#timeouts ComputeInstance#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1f9d9569172a334152605f1b1d3de9d61612930c1705859bf00f2b844e75bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeInstanceConfig(
            name=name,
            shape=shape,
            boot_order=boot_order,
            desired_state=desired_state,
            hostname=hostname,
            id=id,
            image_list=image_list,
            instance_attributes=instance_attributes,
            label=label,
            networking_info=networking_info,
            reverse_dns=reverse_dns,
            ssh_keys=ssh_keys,
            storage=storage,
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

    @jsii.member(jsii_name="putNetworkingInfo")
    def put_networking_info(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceNetworkingInfo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4032f444fa038227e1e2ddfe4df03fe82bc9a70e8e037b79899ea6a8bef6e0e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkingInfo", [value]))

    @jsii.member(jsii_name="putStorage")
    def put_storage(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceStorage", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e28570bfea6d6053633cf6b99b7ee7538ad060ef60c0939c5ed074c122316746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorage", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#create ComputeInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#delete ComputeInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#update ComputeInstance#update}.
        '''
        value = ComputeInstanceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBootOrder")
    def reset_boot_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootOrder", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageList")
    def reset_image_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageList", []))

    @jsii.member(jsii_name="resetInstanceAttributes")
    def reset_instance_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceAttributes", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetNetworkingInfo")
    def reset_networking_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkingInfo", []))

    @jsii.member(jsii_name="resetReverseDns")
    def reset_reverse_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseDns", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

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
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="entry")
    def entry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "entry"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="imageFormat")
    def image_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageFormat"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="networkingInfo")
    def networking_info(self) -> "ComputeInstanceNetworkingInfoList":
        return typing.cast("ComputeInstanceNetworkingInfoList", jsii.get(self, "networkingInfo"))

    @builtins.property
    @jsii.member(jsii_name="placementRequirements")
    def placement_requirements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "placementRequirements"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @builtins.property
    @jsii.member(jsii_name="quotaReservation")
    def quota_reservation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quotaReservation"))

    @builtins.property
    @jsii.member(jsii_name="relationships")
    def relationships(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "relationships"))

    @builtins.property
    @jsii.member(jsii_name="resolvers")
    def resolvers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resolvers"))

    @builtins.property
    @jsii.member(jsii_name="site")
    def site(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "site"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> "ComputeInstanceStorageList":
        return typing.cast("ComputeInstanceStorageList", jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeInstanceTimeoutsOutputReference":
        return typing.cast("ComputeInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vcable")
    def vcable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vcable"))

    @builtins.property
    @jsii.member(jsii_name="virtio")
    def virtio(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "virtio"))

    @builtins.property
    @jsii.member(jsii_name="vncAddress")
    def vnc_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vncAddress"))

    @builtins.property
    @jsii.member(jsii_name="bootOrderInput")
    def boot_order_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "bootOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageListInput")
    def image_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageListInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceAttributesInput")
    def instance_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkingInfoInput")
    def networking_info_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceNetworkingInfo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceNetworkingInfo"]]], jsii.get(self, "networkingInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseDnsInput")
    def reverse_dns_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "reverseDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceStorage"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceStorage"]]], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeInstanceTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeInstanceTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootOrder")
    def boot_order(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "bootOrder"))

    @boot_order.setter
    def boot_order(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb91d779912d0665fb89f675f8facfd2ac1bf4f0502a0b1c7f98440a0eb9fb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootOrder", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e9e112a508ee2323b6fb95d218225f80e59ef37b83a14e59b28dc35610eb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfac291dd1eb12af5788ccba3368fc3f2a47dfbc1c7b56803ac11c0afaeeceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2906182c2456e3aadc6ebb00d7b3a295815b98f2e4807cf6c2de16f59c7d3e35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageList")
    def image_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageList"))

    @image_list.setter
    def image_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd4c8cbf5f8ee29f3e40715a60d2b3428a7fe8bc8bef7f983da5a11476259fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageList", value)

    @builtins.property
    @jsii.member(jsii_name="instanceAttributes")
    def instance_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceAttributes"))

    @instance_attributes.setter
    def instance_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5eee0fef528bff8987d4a8fc4cc6273dde4d59ee649d1e23270f387f8ded25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93de8f7a5ce04d9de0f18825c3cb88eaad029b04c08428603441ee8429c03551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1a4b8c781db0aab14dd82d21bb80bea20bea5caba9fa403de5646aabf08a9b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reverseDns")
    def reverse_dns(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "reverseDns"))

    @reverse_dns.setter
    def reverse_dns(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952737bf51e7e443b749b0b0e7a56a49c27dd526a964d57396be935f98010634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverseDns", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55de556cb60f71a63b38a637339c5a746bb9b134ce698c060d42e4213bc7d4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d396398ac9ffc226dbe37768e722e5dd957d61d3970b02f72095db70ecfdf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49b7ce9a1cba26a21058a6496a702458b97476a26fc6e3af2351d5eebe1147ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceConfig",
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
        "shape": "shape",
        "boot_order": "bootOrder",
        "desired_state": "desiredState",
        "hostname": "hostname",
        "id": "id",
        "image_list": "imageList",
        "instance_attributes": "instanceAttributes",
        "label": "label",
        "networking_info": "networkingInfo",
        "reverse_dns": "reverseDns",
        "ssh_keys": "sshKeys",
        "storage": "storage",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ComputeInstanceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        shape: builtins.str,
        boot_order: typing.Optional[typing.Sequence[jsii.Number]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_list: typing.Optional[builtins.str] = None,
        instance_attributes: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        networking_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceNetworkingInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        reverse_dns: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ComputeInstanceStorage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeInstanceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#name ComputeInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#shape ComputeInstance#shape}.
        :param boot_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#boot_order ComputeInstance#boot_order}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#desired_state ComputeInstance#desired_state}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#hostname ComputeInstance#hostname}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#id ComputeInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#image_list ComputeInstance#image_list}.
        :param instance_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#instance_attributes ComputeInstance#instance_attributes}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#label ComputeInstance#label}.
        :param networking_info: networking_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#networking_info ComputeInstance#networking_info}
        :param reverse_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#reverse_dns ComputeInstance#reverse_dns}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ssh_keys ComputeInstance#ssh_keys}.
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#storage ComputeInstance#storage}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#tags ComputeInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#timeouts ComputeInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ComputeInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bbdf9dad0555ab4dbe2aa518911a9e8a2fb6184c7dae3c0049b3302e625fb10)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument boot_order", value=boot_order, expected_type=type_hints["boot_order"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_list", value=image_list, expected_type=type_hints["image_list"])
            check_type(argname="argument instance_attributes", value=instance_attributes, expected_type=type_hints["instance_attributes"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument networking_info", value=networking_info, expected_type=type_hints["networking_info"])
            check_type(argname="argument reverse_dns", value=reverse_dns, expected_type=type_hints["reverse_dns"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "shape": shape,
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
        if boot_order is not None:
            self._values["boot_order"] = boot_order
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if hostname is not None:
            self._values["hostname"] = hostname
        if id is not None:
            self._values["id"] = id
        if image_list is not None:
            self._values["image_list"] = image_list
        if instance_attributes is not None:
            self._values["instance_attributes"] = instance_attributes
        if label is not None:
            self._values["label"] = label
        if networking_info is not None:
            self._values["networking_info"] = networking_info
        if reverse_dns is not None:
            self._values["reverse_dns"] = reverse_dns
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if storage is not None:
            self._values["storage"] = storage
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#name ComputeInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#shape ComputeInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def boot_order(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#boot_order ComputeInstance#boot_order}.'''
        result = self._values.get("boot_order")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#desired_state ComputeInstance#desired_state}.'''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#hostname ComputeInstance#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#id ComputeInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_list(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#image_list ComputeInstance#image_list}.'''
        result = self._values.get("image_list")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#instance_attributes ComputeInstance#instance_attributes}.'''
        result = self._values.get("instance_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#label ComputeInstance#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networking_info(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceNetworkingInfo"]]]:
        '''networking_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#networking_info ComputeInstance#networking_info}
        '''
        result = self._values.get("networking_info")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceNetworkingInfo"]]], result)

    @builtins.property
    def reverse_dns(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#reverse_dns ComputeInstance#reverse_dns}.'''
        result = self._values.get("reverse_dns")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ssh_keys ComputeInstance#ssh_keys}.'''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceStorage"]]]:
        '''storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#storage ComputeInstance#storage}
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ComputeInstanceStorage"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#tags ComputeInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#timeouts ComputeInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceNetworkingInfo",
    jsii_struct_bases=[],
    name_mapping={
        "index": "index",
        "dns": "dns",
        "ip_address": "ipAddress",
        "ip_network": "ipNetwork",
        "is_default_gateway": "isDefaultGateway",
        "mac_address": "macAddress",
        "name_servers": "nameServers",
        "nat": "nat",
        "search_domains": "searchDomains",
        "sec_lists": "secLists",
        "shared_network": "sharedNetwork",
        "vnic": "vnic",
        "vnic_sets": "vnicSets",
    },
)
class ComputeInstanceNetworkingInfo:
    def __init__(
        self,
        *,
        index: jsii.Number,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        is_default_gateway: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mac_address: typing.Optional[builtins.str] = None,
        name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        nat: typing.Optional[typing.Sequence[builtins.str]] = None,
        search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        sec_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        shared_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        vnic: typing.Optional[builtins.str] = None,
        vnic_sets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#index ComputeInstance#index}.
        :param dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#dns ComputeInstance#dns}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ip_address ComputeInstance#ip_address}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ip_network ComputeInstance#ip_network}.
        :param is_default_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#is_default_gateway ComputeInstance#is_default_gateway}.
        :param mac_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#mac_address ComputeInstance#mac_address}.
        :param name_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#name_servers ComputeInstance#name_servers}.
        :param nat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#nat ComputeInstance#nat}.
        :param search_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#search_domains ComputeInstance#search_domains}.
        :param sec_lists: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#sec_lists ComputeInstance#sec_lists}.
        :param shared_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#shared_network ComputeInstance#shared_network}.
        :param vnic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#vnic ComputeInstance#vnic}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#vnic_sets ComputeInstance#vnic_sets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d1b656c22e0891804bf763c9dd1a3e2e792163731fcf86e225bf008ba2a770)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument is_default_gateway", value=is_default_gateway, expected_type=type_hints["is_default_gateway"])
            check_type(argname="argument mac_address", value=mac_address, expected_type=type_hints["mac_address"])
            check_type(argname="argument name_servers", value=name_servers, expected_type=type_hints["name_servers"])
            check_type(argname="argument nat", value=nat, expected_type=type_hints["nat"])
            check_type(argname="argument search_domains", value=search_domains, expected_type=type_hints["search_domains"])
            check_type(argname="argument sec_lists", value=sec_lists, expected_type=type_hints["sec_lists"])
            check_type(argname="argument shared_network", value=shared_network, expected_type=type_hints["shared_network"])
            check_type(argname="argument vnic", value=vnic, expected_type=type_hints["vnic"])
            check_type(argname="argument vnic_sets", value=vnic_sets, expected_type=type_hints["vnic_sets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index": index,
        }
        if dns is not None:
            self._values["dns"] = dns
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if is_default_gateway is not None:
            self._values["is_default_gateway"] = is_default_gateway
        if mac_address is not None:
            self._values["mac_address"] = mac_address
        if name_servers is not None:
            self._values["name_servers"] = name_servers
        if nat is not None:
            self._values["nat"] = nat
        if search_domains is not None:
            self._values["search_domains"] = search_domains
        if sec_lists is not None:
            self._values["sec_lists"] = sec_lists
        if shared_network is not None:
            self._values["shared_network"] = shared_network
        if vnic is not None:
            self._values["vnic"] = vnic
        if vnic_sets is not None:
            self._values["vnic_sets"] = vnic_sets

    @builtins.property
    def index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#index ComputeInstance#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#dns ComputeInstance#dns}.'''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ip_address ComputeInstance#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#ip_network ComputeInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default_gateway(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#is_default_gateway ComputeInstance#is_default_gateway}.'''
        result = self._values.get("is_default_gateway")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def mac_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#mac_address ComputeInstance#mac_address}.'''
        result = self._values.get("mac_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#name_servers ComputeInstance#name_servers}.'''
        result = self._values.get("name_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def nat(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#nat ComputeInstance#nat}.'''
        result = self._values.get("nat")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#search_domains ComputeInstance#search_domains}.'''
        result = self._values.get("search_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sec_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#sec_lists ComputeInstance#sec_lists}.'''
        result = self._values.get("sec_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shared_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#shared_network ComputeInstance#shared_network}.'''
        result = self._values.get("shared_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def vnic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#vnic ComputeInstance#vnic}.'''
        result = self._values.get("vnic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vnic_sets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#vnic_sets ComputeInstance#vnic_sets}.'''
        result = self._values.get("vnic_sets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeInstanceNetworkingInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeInstanceNetworkingInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceNetworkingInfoList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2f37253535353b6f4cf3b317cda569eb0451fa605dd0c2ca5568f8e660a519c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ComputeInstanceNetworkingInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db5451c9654fb071123edee575ece9b363e92871280c34a670deffb36f1efb0a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeInstanceNetworkingInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00af9def1783ad6463f4c0ac1ca1de692d9b82870b7c816bdacdf2b8d71616c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585c209f66ff60e29a63bde7fc21896a8a751a53f847481a2349871a48dd20fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6a49dda13f6c200d7474e8c223ac727c2f5a3dde27d948affbcb708b1533064)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceNetworkingInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceNetworkingInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceNetworkingInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f14b124c100bb33ed1c753e803f7da17339c8f4576b859a7666ee0d301e94ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeInstanceNetworkingInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceNetworkingInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646d74d36d603ce9f75ec3500e22f78ff2d00a27dc465fb56c043d0890dab54b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetIsDefaultGateway")
    def reset_is_default_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefaultGateway", []))

    @jsii.member(jsii_name="resetMacAddress")
    def reset_mac_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacAddress", []))

    @jsii.member(jsii_name="resetNameServers")
    def reset_name_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameServers", []))

    @jsii.member(jsii_name="resetNat")
    def reset_nat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNat", []))

    @jsii.member(jsii_name="resetSearchDomains")
    def reset_search_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchDomains", []))

    @jsii.member(jsii_name="resetSecLists")
    def reset_sec_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecLists", []))

    @jsii.member(jsii_name="resetSharedNetwork")
    def reset_shared_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedNetwork", []))

    @jsii.member(jsii_name="resetVnic")
    def reset_vnic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnic", []))

    @jsii.member(jsii_name="resetVnicSets")
    def reset_vnic_sets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnicSets", []))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultGatewayInput")
    def is_default_gateway_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="macAddressInput")
    def mac_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameServersInput")
    def name_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameServersInput"))

    @builtins.property
    @jsii.member(jsii_name="natInput")
    def nat_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "natInput"))

    @builtins.property
    @jsii.member(jsii_name="searchDomainsInput")
    def search_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="secListsInput")
    def sec_lists_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secListsInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedNetworkInput")
    def shared_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sharedNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicInput")
    def vnic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnicInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicSetsInput")
    def vnic_sets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vnicSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dns"))

    @dns.setter
    def dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b65761df1679f281484b82c31793d6f1c5ab63d2aff6999297babbf581ffd39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dns", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "index"))

    @index.setter
    def index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bc6c092628c1f47336146897beaa38c15d7e9c2e67b3705a63955e1e0980d04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef49e5bb0ff4d430a74892a115d3cecf438a69376b246899f4c5ef67295fcaea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19031dfb4fc2b14cc06799d20a8374a643b65cee1871f7ef4cfbd73b7b01485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="isDefaultGateway")
    def is_default_gateway(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefaultGateway"))

    @is_default_gateway.setter
    def is_default_gateway(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41a89df558a7ae8bdba31fbde85ab7897d3514968c1f8f3a0c2304f34505c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefaultGateway", value)

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @mac_address.setter
    def mac_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630c5d0fe87141837fb36dd9f789da1347b063d59b13fe0f544bddd37e98eeef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macAddress", value)

    @builtins.property
    @jsii.member(jsii_name="nameServers")
    def name_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameServers"))

    @name_servers.setter
    def name_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09755a450d8435b2207c04637626d88c4ac4ba3ac5dbec874b62f2f86b7fd730)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameServers", value)

    @builtins.property
    @jsii.member(jsii_name="nat")
    def nat(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nat"))

    @nat.setter
    def nat(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6ecf2128558f07514a13fe774ebd5f981cec5355c73f344d1da4eb01c8816a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nat", value)

    @builtins.property
    @jsii.member(jsii_name="searchDomains")
    def search_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searchDomains"))

    @search_domains.setter
    def search_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e69dbf887838dc1c919c3532e4abed14dfbbdec851b24eadf23928c6076f3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchDomains", value)

    @builtins.property
    @jsii.member(jsii_name="secLists")
    def sec_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secLists"))

    @sec_lists.setter
    def sec_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1975a67985fcfe57f086593cb7e6de900ab55b0ca6b0c2348dcfbcbb0211273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secLists", value)

    @builtins.property
    @jsii.member(jsii_name="sharedNetwork")
    def shared_network(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sharedNetwork"))

    @shared_network.setter
    def shared_network(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9a2792d0cf2647f0f58bd35f7518e4bc23c1709116d962cf9e1cff0b5841be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="vnic")
    def vnic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnic"))

    @vnic.setter
    def vnic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db17796638893074400f0a50acb98a508db680e43ef3e4dfd7ffcb5a1664a3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnic", value)

    @builtins.property
    @jsii.member(jsii_name="vnicSets")
    def vnic_sets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vnicSets"))

    @vnic_sets.setter
    def vnic_sets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c266d027cbe1999e0e92ccf932ea1b27f6c568c47dcf3ebc0ff600aec5c0a06e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnicSets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeInstanceNetworkingInfo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeInstanceNetworkingInfo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeInstanceNetworkingInfo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7066a92df56674cd7696223f6801004d2e7bd782d7ef925d1a215328205c350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceStorage",
    jsii_struct_bases=[],
    name_mapping={"index": "index", "volume": "volume"},
)
class ComputeInstanceStorage:
    def __init__(self, *, index: jsii.Number, volume: builtins.str) -> None:
        '''
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#index ComputeInstance#index}.
        :param volume: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#volume ComputeInstance#volume}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ff0a61a1ffd3a8692fdc04198a292f7d8fee31aaee2f21878336fd4d152cbf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index": index,
            "volume": volume,
        }

    @builtins.property
    def index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#index ComputeInstance#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#volume ComputeInstance#volume}.'''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeInstanceStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeInstanceStorageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceStorageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd2906cbb4bbe02a06a1f0df9e34fd471a10f8d791cc70a9f6547389e1b696e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ComputeInstanceStorageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9862fd63ce89947e390ad94e7a10279b9092d19e5be95233aa7bb23d764ae1b6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeInstanceStorageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a599306f120b69d42ac7c20d35daf105e3e0d3983886956e85d80ebf41c092)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702ef0974b9941cdde89df9869aafc2b89f9a4297bfffedf41a9828ac0e26ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef3bbbdc0276ea6d79be91efce045a7b31ad5d30deaa35ff760c62ffc4274e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceStorage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceStorage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceStorage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda817fe473cbe90de7ed860003b9fb12fb3a0e88c7b9ee918f9973d0e702047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeInstanceStorageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceStorageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17ce7a06ebca774c8d7050451df9a8eb7a1337fd56531aaf0c1331cc2e6dd64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "index"))

    @index.setter
    def index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe23169f788752ae741e50a37919492df5392e202a240b29d59485e0c6cc530e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f13ed56b1e516574758e6ec562bc1ce1c2151e0e26e7b72e0cc5ebca06945e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeInstanceStorage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeInstanceStorage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeInstanceStorage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cde692448d853289f40c9fe2f12a0595390da7a1ac22534c2ceb3bfa295f71e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#create ComputeInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#delete ComputeInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#update ComputeInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1bad5e72264d6cbd27f7ca042f0ada94f60608c22523cad327f4daa88bed5d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#create ComputeInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#delete ComputeInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_instance#update ComputeInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeInstanceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeInstance.ComputeInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bae28578f2b71d687f6231f2862fd13fda040fb6027d1a71952767daf6bf3ebd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2f1781eb49b267e84c197731bfd217870c5ca1bbc2c9e9d727d7fbf11b527e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aebac9b0a9bf27b3af8f978f1c9cf4f5f8dfc7935307ff64349b4205425ded6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a012d9f749d9c0a5fb6bafdd2254dee6badc8e4a2a048274ea98fec1f2da94c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeInstanceTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeInstanceTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ea8451dd1ff6ee8caf1e92f5964d49cb6676d17b310174c629811fa76ca1c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeInstance",
    "ComputeInstanceConfig",
    "ComputeInstanceNetworkingInfo",
    "ComputeInstanceNetworkingInfoList",
    "ComputeInstanceNetworkingInfoOutputReference",
    "ComputeInstanceStorage",
    "ComputeInstanceStorageList",
    "ComputeInstanceStorageOutputReference",
    "ComputeInstanceTimeouts",
    "ComputeInstanceTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__6c1f9d9569172a334152605f1b1d3de9d61612930c1705859bf00f2b844e75bd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    shape: builtins.str,
    boot_order: typing.Optional[typing.Sequence[jsii.Number]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_list: typing.Optional[builtins.str] = None,
    instance_attributes: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    networking_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceNetworkingInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    reverse_dns: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceStorage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__4032f444fa038227e1e2ddfe4df03fe82bc9a70e8e037b79899ea6a8bef6e0e7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceNetworkingInfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28570bfea6d6053633cf6b99b7ee7538ad060ef60c0939c5ed074c122316746(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceStorage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb91d779912d0665fb89f675f8facfd2ac1bf4f0502a0b1c7f98440a0eb9fb7(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e9e112a508ee2323b6fb95d218225f80e59ef37b83a14e59b28dc35610eb05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfac291dd1eb12af5788ccba3368fc3f2a47dfbc1c7b56803ac11c0afaeeceb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2906182c2456e3aadc6ebb00d7b3a295815b98f2e4807cf6c2de16f59c7d3e35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4c8cbf5f8ee29f3e40715a60d2b3428a7fe8bc8bef7f983da5a11476259fc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5eee0fef528bff8987d4a8fc4cc6273dde4d59ee649d1e23270f387f8ded25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93de8f7a5ce04d9de0f18825c3cb88eaad029b04c08428603441ee8429c03551(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1a4b8c781db0aab14dd82d21bb80bea20bea5caba9fa403de5646aabf08a9b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952737bf51e7e443b749b0b0e7a56a49c27dd526a964d57396be935f98010634(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55de556cb60f71a63b38a637339c5a746bb9b134ce698c060d42e4213bc7d4b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d396398ac9ffc226dbe37768e722e5dd957d61d3970b02f72095db70ecfdf0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49b7ce9a1cba26a21058a6496a702458b97476a26fc6e3af2351d5eebe1147ac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bbdf9dad0555ab4dbe2aa518911a9e8a2fb6184c7dae3c0049b3302e625fb10(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    shape: builtins.str,
    boot_order: typing.Optional[typing.Sequence[jsii.Number]] = None,
    desired_state: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    image_list: typing.Optional[builtins.str] = None,
    instance_attributes: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    networking_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceNetworkingInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    reverse_dns: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ComputeInstanceStorage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeInstanceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d1b656c22e0891804bf763c9dd1a3e2e792163731fcf86e225bf008ba2a770(
    *,
    index: jsii.Number,
    dns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    ip_network: typing.Optional[builtins.str] = None,
    is_default_gateway: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mac_address: typing.Optional[builtins.str] = None,
    name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    nat: typing.Optional[typing.Sequence[builtins.str]] = None,
    search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    sec_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
    shared_network: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    vnic: typing.Optional[builtins.str] = None,
    vnic_sets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f37253535353b6f4cf3b317cda569eb0451fa605dd0c2ca5568f8e660a519c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db5451c9654fb071123edee575ece9b363e92871280c34a670deffb36f1efb0a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00af9def1783ad6463f4c0ac1ca1de692d9b82870b7c816bdacdf2b8d71616c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585c209f66ff60e29a63bde7fc21896a8a751a53f847481a2349871a48dd20fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6a49dda13f6c200d7474e8c223ac727c2f5a3dde27d948affbcb708b1533064(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f14b124c100bb33ed1c753e803f7da17339c8f4576b859a7666ee0d301e94ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceNetworkingInfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646d74d36d603ce9f75ec3500e22f78ff2d00a27dc465fb56c043d0890dab54b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b65761df1679f281484b82c31793d6f1c5ab63d2aff6999297babbf581ffd39(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc6c092628c1f47336146897beaa38c15d7e9c2e67b3705a63955e1e0980d04(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef49e5bb0ff4d430a74892a115d3cecf438a69376b246899f4c5ef67295fcaea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19031dfb4fc2b14cc06799d20a8374a643b65cee1871f7ef4cfbd73b7b01485(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41a89df558a7ae8bdba31fbde85ab7897d3514968c1f8f3a0c2304f34505c53(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630c5d0fe87141837fb36dd9f789da1347b063d59b13fe0f544bddd37e98eeef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09755a450d8435b2207c04637626d88c4ac4ba3ac5dbec874b62f2f86b7fd730(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6ecf2128558f07514a13fe774ebd5f981cec5355c73f344d1da4eb01c8816a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e69dbf887838dc1c919c3532e4abed14dfbbdec851b24eadf23928c6076f3e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1975a67985fcfe57f086593cb7e6de900ab55b0ca6b0c2348dcfbcbb0211273(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9a2792d0cf2647f0f58bd35f7518e4bc23c1709116d962cf9e1cff0b5841be(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db17796638893074400f0a50acb98a508db680e43ef3e4dfd7ffcb5a1664a3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c266d027cbe1999e0e92ccf932ea1b27f6c568c47dcf3ebc0ff600aec5c0a06e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7066a92df56674cd7696223f6801004d2e7bd782d7ef925d1a215328205c350(
    value: typing.Optional[typing.Union[ComputeInstanceNetworkingInfo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ff0a61a1ffd3a8692fdc04198a292f7d8fee31aaee2f21878336fd4d152cbf(
    *,
    index: jsii.Number,
    volume: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd2906cbb4bbe02a06a1f0df9e34fd471a10f8d791cc70a9f6547389e1b696e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9862fd63ce89947e390ad94e7a10279b9092d19e5be95233aa7bb23d764ae1b6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a599306f120b69d42ac7c20d35daf105e3e0d3983886956e85d80ebf41c092(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702ef0974b9941cdde89df9869aafc2b89f9a4297bfffedf41a9828ac0e26ed3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef3bbbdc0276ea6d79be91efce045a7b31ad5d30deaa35ff760c62ffc4274e58(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda817fe473cbe90de7ed860003b9fb12fb3a0e88c7b9ee918f9973d0e702047(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ComputeInstanceStorage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17ce7a06ebca774c8d7050451df9a8eb7a1337fd56531aaf0c1331cc2e6dd64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe23169f788752ae741e50a37919492df5392e202a240b29d59485e0c6cc530e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f13ed56b1e516574758e6ec562bc1ce1c2151e0e26e7b72e0cc5ebca06945e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cde692448d853289f40c9fe2f12a0595390da7a1ac22534c2ceb3bfa295f71e(
    value: typing.Optional[typing.Union[ComputeInstanceStorage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1bad5e72264d6cbd27f7ca042f0ada94f60608c22523cad327f4daa88bed5d(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae28578f2b71d687f6231f2862fd13fda040fb6027d1a71952767daf6bf3ebd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f1781eb49b267e84c197731bfd217870c5ca1bbc2c9e9d727d7fbf11b527e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aebac9b0a9bf27b3af8f978f1c9cf4f5f8dfc7935307ff64349b4205425ded6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a012d9f749d9c0a5fb6bafdd2254dee6badc8e4a2a048274ea98fec1f2da94c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ea8451dd1ff6ee8caf1e92f5964d49cb6676d17b310174c629811fa76ca1c5(
    value: typing.Optional[typing.Union[ComputeInstanceTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
