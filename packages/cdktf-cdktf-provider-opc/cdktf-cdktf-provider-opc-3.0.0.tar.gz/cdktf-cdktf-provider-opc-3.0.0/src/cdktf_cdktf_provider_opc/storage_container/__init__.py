'''
# `opc_storage_container`

Refer to the Terraform Registory for docs: [`opc_storage_container`](https://www.terraform.io/docs/providers/opc/r/storage_container).
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


class StorageContainer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.storageContainer.StorageContainer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/storage_container opc_storage_container}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        max_age: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        primary_key: typing.Optional[builtins.str] = None,
        quota_bytes: typing.Optional[jsii.Number] = None,
        quota_count: typing.Optional[jsii.Number] = None,
        read_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
        secondary_key: typing.Optional[builtins.str] = None,
        write_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/storage_container opc_storage_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#name StorageContainer#name}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#allowed_origins StorageContainer#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#exposed_headers StorageContainer#exposed_headers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#id StorageContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#max_age StorageContainer#max_age}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#metadata StorageContainer#metadata}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#primary_key StorageContainer#primary_key}.
        :param quota_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_bytes StorageContainer#quota_bytes}.
        :param quota_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_count StorageContainer#quota_count}.
        :param read_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#read_acls StorageContainer#read_acls}.
        :param secondary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#secondary_key StorageContainer#secondary_key}.
        :param write_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#write_acls StorageContainer#write_acls}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1248ae43e102d437754ae12ab0a46f5d63b221b64c3eb5bef23c95abff0051)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageContainerConfig(
            name=name,
            allowed_origins=allowed_origins,
            exposed_headers=exposed_headers,
            id=id,
            max_age=max_age,
            metadata=metadata,
            primary_key=primary_key,
            quota_bytes=quota_bytes,
            quota_count=quota_count,
            read_acls=read_acls,
            secondary_key=secondary_key,
            write_acls=write_acls,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowedOrigins")
    def reset_allowed_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOrigins", []))

    @jsii.member(jsii_name="resetExposedHeaders")
    def reset_exposed_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposedHeaders", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @jsii.member(jsii_name="resetQuotaBytes")
    def reset_quota_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuotaBytes", []))

    @jsii.member(jsii_name="resetQuotaCount")
    def reset_quota_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuotaCount", []))

    @jsii.member(jsii_name="resetReadAcls")
    def reset_read_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadAcls", []))

    @jsii.member(jsii_name="resetSecondaryKey")
    def reset_secondary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryKey", []))

    @jsii.member(jsii_name="resetWriteAcls")
    def reset_write_acls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcls", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedOriginsInput")
    def allowed_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedHeadersInput")
    def exposed_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="quotaBytesInput")
    def quota_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "quotaBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="quotaCountInput")
    def quota_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "quotaCountInput"))

    @builtins.property
    @jsii.member(jsii_name="readAclsInput")
    def read_acls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "readAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryKeyInput")
    def secondary_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAclsInput")
    def write_acls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "writeAclsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOrigins"))

    @allowed_origins.setter
    def allowed_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6360b2a5771afdc06c0411bd2c19fca2e6bf891de3922e19eb537cabfe1472e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOrigins", value)

    @builtins.property
    @jsii.member(jsii_name="exposedHeaders")
    def exposed_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposedHeaders"))

    @exposed_headers.setter
    def exposed_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32532c009e2e181b284d298285d9f05e47802f7850e666021dd0506dc84bc73e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposedHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b19a247ccf170ac10bc54c3ba58ffdbf93c4ad7c8aff14dcc44b988bd4eefc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede864c522349fb617b2fbe0bc2d248f450e79f6aae6047cc79f785acd119461)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8fbed91aa9179773e5b177c0995b5c0b2452749f8a197ab1df9ed8046c0ca7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b39ef1d316c37a049b0ccfb8d85698d35ecc76929d5875471a9484f230a09b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3143483f491690e9024dd561fe6ceeaab7beb0573d2f037cd0b5631dd306aa14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="quotaBytes")
    def quota_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quotaBytes"))

    @quota_bytes.setter
    def quota_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2490ee59f0e7700d8b9fdd8c2bce6f1768730e51e1a28cb9dfd51331cfebb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quotaBytes", value)

    @builtins.property
    @jsii.member(jsii_name="quotaCount")
    def quota_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quotaCount"))

    @quota_count.setter
    def quota_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9babbdfa53010dac054d5206aa1bf732772922d5b594f877db3b9792909b75e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quotaCount", value)

    @builtins.property
    @jsii.member(jsii_name="readAcls")
    def read_acls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readAcls"))

    @read_acls.setter
    def read_acls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b004c315ae53f484fc6028cd81ffa6558c040596d8e1068d14901f6d8b7b8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readAcls", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryKey")
    def secondary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryKey"))

    @secondary_key.setter
    def secondary_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955474cf2cf9028185f50913370dc8447105208d81bc28380b100a9662397fd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="writeAcls")
    def write_acls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "writeAcls"))

    @write_acls.setter
    def write_acls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f358513d31b5402f53e534843738a75328b2b018a879ae5488cdf24cf66495b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcls", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.storageContainer.StorageContainerConfig",
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
        "allowed_origins": "allowedOrigins",
        "exposed_headers": "exposedHeaders",
        "id": "id",
        "max_age": "maxAge",
        "metadata": "metadata",
        "primary_key": "primaryKey",
        "quota_bytes": "quotaBytes",
        "quota_count": "quotaCount",
        "read_acls": "readAcls",
        "secondary_key": "secondaryKey",
        "write_acls": "writeAcls",
    },
)
class StorageContainerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        max_age: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        primary_key: typing.Optional[builtins.str] = None,
        quota_bytes: typing.Optional[jsii.Number] = None,
        quota_count: typing.Optional[jsii.Number] = None,
        read_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
        secondary_key: typing.Optional[builtins.str] = None,
        write_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#name StorageContainer#name}.
        :param allowed_origins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#allowed_origins StorageContainer#allowed_origins}.
        :param exposed_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#exposed_headers StorageContainer#exposed_headers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#id StorageContainer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_age: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#max_age StorageContainer#max_age}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#metadata StorageContainer#metadata}.
        :param primary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#primary_key StorageContainer#primary_key}.
        :param quota_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_bytes StorageContainer#quota_bytes}.
        :param quota_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_count StorageContainer#quota_count}.
        :param read_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#read_acls StorageContainer#read_acls}.
        :param secondary_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#secondary_key StorageContainer#secondary_key}.
        :param write_acls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#write_acls StorageContainer#write_acls}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__202a136d7340e16924413893ab84fd01bd097bfb95c2e9c24b40243bd1c1470f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_origins", value=allowed_origins, expected_type=type_hints["allowed_origins"])
            check_type(argname="argument exposed_headers", value=exposed_headers, expected_type=type_hints["exposed_headers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
            check_type(argname="argument quota_bytes", value=quota_bytes, expected_type=type_hints["quota_bytes"])
            check_type(argname="argument quota_count", value=quota_count, expected_type=type_hints["quota_count"])
            check_type(argname="argument read_acls", value=read_acls, expected_type=type_hints["read_acls"])
            check_type(argname="argument secondary_key", value=secondary_key, expected_type=type_hints["secondary_key"])
            check_type(argname="argument write_acls", value=write_acls, expected_type=type_hints["write_acls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if allowed_origins is not None:
            self._values["allowed_origins"] = allowed_origins
        if exposed_headers is not None:
            self._values["exposed_headers"] = exposed_headers
        if id is not None:
            self._values["id"] = id
        if max_age is not None:
            self._values["max_age"] = max_age
        if metadata is not None:
            self._values["metadata"] = metadata
        if primary_key is not None:
            self._values["primary_key"] = primary_key
        if quota_bytes is not None:
            self._values["quota_bytes"] = quota_bytes
        if quota_count is not None:
            self._values["quota_count"] = quota_count
        if read_acls is not None:
            self._values["read_acls"] = read_acls
        if secondary_key is not None:
            self._values["secondary_key"] = secondary_key
        if write_acls is not None:
            self._values["write_acls"] = write_acls

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#name StorageContainer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#allowed_origins StorageContainer#allowed_origins}.'''
        result = self._values.get("allowed_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exposed_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#exposed_headers StorageContainer#exposed_headers}.'''
        result = self._values.get("exposed_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#id StorageContainer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#max_age StorageContainer#max_age}.'''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#metadata StorageContainer#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def primary_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#primary_key StorageContainer#primary_key}.'''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quota_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_bytes StorageContainer#quota_bytes}.'''
        result = self._values.get("quota_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def quota_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#quota_count StorageContainer#quota_count}.'''
        result = self._values.get("quota_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_acls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#read_acls StorageContainer#read_acls}.'''
        result = self._values.get("read_acls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secondary_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#secondary_key StorageContainer#secondary_key}.'''
        result = self._values.get("secondary_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_acls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_container#write_acls StorageContainer#write_acls}.'''
        result = self._values.get("write_acls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StorageContainer",
    "StorageContainerConfig",
]

publication.publish()

def _typecheckingstub__df1248ae43e102d437754ae12ab0a46f5d63b221b64c3eb5bef23c95abff0051(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    max_age: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    primary_key: typing.Optional[builtins.str] = None,
    quota_bytes: typing.Optional[jsii.Number] = None,
    quota_count: typing.Optional[jsii.Number] = None,
    read_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
    secondary_key: typing.Optional[builtins.str] = None,
    write_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__6360b2a5771afdc06c0411bd2c19fca2e6bf891de3922e19eb537cabfe1472e0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32532c009e2e181b284d298285d9f05e47802f7850e666021dd0506dc84bc73e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b19a247ccf170ac10bc54c3ba58ffdbf93c4ad7c8aff14dcc44b988bd4eefc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede864c522349fb617b2fbe0bc2d248f450e79f6aae6047cc79f785acd119461(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8fbed91aa9179773e5b177c0995b5c0b2452749f8a197ab1df9ed8046c0ca7a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b39ef1d316c37a049b0ccfb8d85698d35ecc76929d5875471a9484f230a09b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3143483f491690e9024dd561fe6ceeaab7beb0573d2f037cd0b5631dd306aa14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2490ee59f0e7700d8b9fdd8c2bce6f1768730e51e1a28cb9dfd51331cfebb8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9babbdfa53010dac054d5206aa1bf732772922d5b594f877db3b9792909b75e8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b004c315ae53f484fc6028cd81ffa6558c040596d8e1068d14901f6d8b7b8c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955474cf2cf9028185f50913370dc8447105208d81bc28380b100a9662397fd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f358513d31b5402f53e534843738a75328b2b018a879ae5488cdf24cf66495b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__202a136d7340e16924413893ab84fd01bd097bfb95c2e9c24b40243bd1c1470f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    allowed_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    exposed_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    max_age: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    primary_key: typing.Optional[builtins.str] = None,
    quota_bytes: typing.Optional[jsii.Number] = None,
    quota_count: typing.Optional[jsii.Number] = None,
    read_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
    secondary_key: typing.Optional[builtins.str] = None,
    write_acls: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
