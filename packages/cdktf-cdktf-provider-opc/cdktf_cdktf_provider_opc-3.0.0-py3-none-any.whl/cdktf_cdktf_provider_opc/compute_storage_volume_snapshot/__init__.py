'''
# `opc_compute_storage_volume_snapshot`

Refer to the Terraform Registory for docs: [`opc_compute_storage_volume_snapshot`](https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot).
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


class ComputeStorageVolumeSnapshot(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeStorageVolumeSnapshot.ComputeStorageVolumeSnapshot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot opc_compute_storage_volume_snapshot}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        volume_name: builtins.str,
        collocated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parent_volume_bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeStorageVolumeSnapshotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot opc_compute_storage_volume_snapshot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param volume_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#volume_name ComputeStorageVolumeSnapshot#volume_name}.
        :param collocated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#collocated ComputeStorageVolumeSnapshot#collocated}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#description ComputeStorageVolumeSnapshot#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#id ComputeStorageVolumeSnapshot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#name ComputeStorageVolumeSnapshot#name}.
        :param parent_volume_bootable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#parent_volume_bootable ComputeStorageVolumeSnapshot#parent_volume_bootable}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#tags ComputeStorageVolumeSnapshot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#timeouts ComputeStorageVolumeSnapshot#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0054509edb8a06a2c1ad77945db7ba1f51f329d133b4d6042de88ed9d8081c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeStorageVolumeSnapshotConfig(
            volume_name=volume_name,
            collocated=collocated,
            description=description,
            id=id,
            name=name,
            parent_volume_bootable=parent_volume_bootable,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#create ComputeStorageVolumeSnapshot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#delete ComputeStorageVolumeSnapshot#delete}.
        '''
        value = ComputeStorageVolumeSnapshotTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCollocated")
    def reset_collocated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCollocated", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetParentVolumeBootable")
    def reset_parent_volume_bootable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentVolumeBootable", []))

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
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @builtins.property
    @jsii.member(jsii_name="machineImageName")
    def machine_image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineImageName"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="property")
    def property(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "property"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @builtins.property
    @jsii.member(jsii_name="snapshotTimestamp")
    def snapshot_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="statusDetail")
    def status_detail(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusDetail"))

    @builtins.property
    @jsii.member(jsii_name="statusTimestamp")
    def status_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeStorageVolumeSnapshotTimeoutsOutputReference":
        return typing.cast("ComputeStorageVolumeSnapshotTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="collocatedInput")
    def collocated_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "collocatedInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentVolumeBootableInput")
    def parent_volume_bootable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "parentVolumeBootableInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeStorageVolumeSnapshotTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeStorageVolumeSnapshotTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeNameInput")
    def volume_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="collocated")
    def collocated(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "collocated"))

    @collocated.setter
    def collocated(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038e2a1ee47d2342c89f14628bc0ba5e743bc86d774ca5800e89581ef0fe327f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collocated", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59cdb10b9f429ba7b5973f8e2097e2504e4c7e14aa01b1d3bbbaa16c2db7e3f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f22b335acc0563f8af74de76fa90e155b0f83c696f0cf869ef825706bc4ef3fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac69a622addf44b814aad2c34765c9245d5bff3008d7ed5f2c7a87fee646781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentVolumeBootable")
    def parent_volume_bootable(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "parentVolumeBootable"))

    @parent_volume_bootable.setter
    def parent_volume_bootable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d98340e6b8059d76a524df4c7cff4c46fac46b96b5b0e53d3712d34cc0cb00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentVolumeBootable", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b66befcb318e93afb5747192c3f0d4f89819e8fc5dcc51b6c87c963576b5e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="volumeName")
    def volume_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeName"))

    @volume_name.setter
    def volume_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1879a84119c4bf1c9a2ceb7ac934af0e60152a66d39e7e47c5d2e569cfbd8d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeStorageVolumeSnapshot.ComputeStorageVolumeSnapshotConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "volume_name": "volumeName",
        "collocated": "collocated",
        "description": "description",
        "id": "id",
        "name": "name",
        "parent_volume_bootable": "parentVolumeBootable",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ComputeStorageVolumeSnapshotConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        volume_name: builtins.str,
        collocated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parent_volume_bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeStorageVolumeSnapshotTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param volume_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#volume_name ComputeStorageVolumeSnapshot#volume_name}.
        :param collocated: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#collocated ComputeStorageVolumeSnapshot#collocated}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#description ComputeStorageVolumeSnapshot#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#id ComputeStorageVolumeSnapshot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#name ComputeStorageVolumeSnapshot#name}.
        :param parent_volume_bootable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#parent_volume_bootable ComputeStorageVolumeSnapshot#parent_volume_bootable}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#tags ComputeStorageVolumeSnapshot#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#timeouts ComputeStorageVolumeSnapshot#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ComputeStorageVolumeSnapshotTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389e39838ee074a232fb6fe16cad8242ec932f1b07a4107765fe01b091a3e644)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument volume_name", value=volume_name, expected_type=type_hints["volume_name"])
            check_type(argname="argument collocated", value=collocated, expected_type=type_hints["collocated"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_volume_bootable", value=parent_volume_bootable, expected_type=type_hints["parent_volume_bootable"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_name": volume_name,
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
        if collocated is not None:
            self._values["collocated"] = collocated
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if parent_volume_bootable is not None:
            self._values["parent_volume_bootable"] = parent_volume_bootable
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
    def volume_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#volume_name ComputeStorageVolumeSnapshot#volume_name}.'''
        result = self._values.get("volume_name")
        assert result is not None, "Required property 'volume_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collocated(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#collocated ComputeStorageVolumeSnapshot#collocated}.'''
        result = self._values.get("collocated")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#description ComputeStorageVolumeSnapshot#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#id ComputeStorageVolumeSnapshot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#name ComputeStorageVolumeSnapshot#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_volume_bootable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#parent_volume_bootable ComputeStorageVolumeSnapshot#parent_volume_bootable}.'''
        result = self._values.get("parent_volume_bootable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#tags ComputeStorageVolumeSnapshot#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeStorageVolumeSnapshotTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#timeouts ComputeStorageVolumeSnapshot#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeStorageVolumeSnapshotTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeStorageVolumeSnapshotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeStorageVolumeSnapshot.ComputeStorageVolumeSnapshotTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class ComputeStorageVolumeSnapshotTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#create ComputeStorageVolumeSnapshot#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#delete ComputeStorageVolumeSnapshot#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__060dd60d06680da8e2f235edfabfd996e74c4953cb44d2f5674867f80a379431)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#create ComputeStorageVolumeSnapshot#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_snapshot#delete ComputeStorageVolumeSnapshot#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeStorageVolumeSnapshotTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeStorageVolumeSnapshotTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeStorageVolumeSnapshot.ComputeStorageVolumeSnapshotTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c49451fab02d7bf59644ca017c8bced1c385522bfb18b198659350aa956c2574)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2594f5fe6885b514ff0b48f98f45100de09c23fe60d7c7404777cbcc37d54b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ead65da46bc0f6de0acadd4d5ad30c8e7fd2d8a8e115841264ecdad3406d8ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4ae4d4ace0bd395d5ef4237ae1bff328560a32fc6a9b1d65cb5ee877cf7131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeStorageVolumeSnapshot",
    "ComputeStorageVolumeSnapshotConfig",
    "ComputeStorageVolumeSnapshotTimeouts",
    "ComputeStorageVolumeSnapshotTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__d0054509edb8a06a2c1ad77945db7ba1f51f329d133b4d6042de88ed9d8081c8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    volume_name: builtins.str,
    collocated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parent_volume_bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__038e2a1ee47d2342c89f14628bc0ba5e743bc86d774ca5800e89581ef0fe327f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59cdb10b9f429ba7b5973f8e2097e2504e4c7e14aa01b1d3bbbaa16c2db7e3f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f22b335acc0563f8af74de76fa90e155b0f83c696f0cf869ef825706bc4ef3fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac69a622addf44b814aad2c34765c9245d5bff3008d7ed5f2c7a87fee646781(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d98340e6b8059d76a524df4c7cff4c46fac46b96b5b0e53d3712d34cc0cb00(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b66befcb318e93afb5747192c3f0d4f89819e8fc5dcc51b6c87c963576b5e0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1879a84119c4bf1c9a2ceb7ac934af0e60152a66d39e7e47c5d2e569cfbd8d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389e39838ee074a232fb6fe16cad8242ec932f1b07a4107765fe01b091a3e644(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    volume_name: builtins.str,
    collocated: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parent_volume_bootable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060dd60d06680da8e2f235edfabfd996e74c4953cb44d2f5674867f80a379431(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c49451fab02d7bf59644ca017c8bced1c385522bfb18b198659350aa956c2574(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2594f5fe6885b514ff0b48f98f45100de09c23fe60d7c7404777cbcc37d54b74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ead65da46bc0f6de0acadd4d5ad30c8e7fd2d8a8e115841264ecdad3406d8ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4ae4d4ace0bd395d5ef4237ae1bff328560a32fc6a9b1d65cb5ee877cf7131(
    value: typing.Optional[typing.Union[ComputeStorageVolumeSnapshotTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
