'''
# `opc_storage_object`

Refer to the Terraform Registory for docs: [`opc_storage_object`](https://www.terraform.io/docs/providers/opc/r/storage_object).
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


class StorageObject(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.storageObject.StorageObject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/storage_object opc_storage_object}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        container: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        copy_from: typing.Optional[builtins.str] = None,
        delete_at: typing.Optional[jsii.Number] = None,
        etag: typing.Optional[builtins.str] = None,
        file: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transfer_encoding: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/storage_object opc_storage_object} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: Name of the storage container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#container StorageObject#container}
        :param name: Name of the storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#name StorageObject#name}
        :param content: Raw content in string-form of the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content StorageObject#content}
        :param content_disposition: Overrides the behavior of the browser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_disposition StorageObject#content_disposition}
        :param content_encoding: Set the content-encoding metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_encoding StorageObject#content_encoding}
        :param content_type: Set the MIME type for the object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_type StorageObject#content_type}
        :param copy_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#copy_from StorageObject#copy_from}.
        :param delete_at: The date and time in UNIX Epoch time stamp format when the system removes the object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#delete_at StorageObject#delete_at}
        :param etag: MD5 checksum value of the request body. Unquoted. Strongly Recommended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#etag StorageObject#etag}
        :param file: File path for the content to use for data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#file StorageObject#file}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#id StorageObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: The object metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#metadata StorageObject#metadata}
        :param transfer_encoding: Sets the transfer encoding. Can only be 'chunked' or Nil, requires Content-Length to be 0 if set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#transfer_encoding StorageObject#transfer_encoding}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0b73200ad4c87e119b0066044792a5e7ffc5fd664137b946d0ab514ba20b25)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageObjectConfig(
            container=container,
            name=name,
            content=content,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_type=content_type,
            copy_from=copy_from,
            delete_at=delete_at,
            etag=etag,
            file=file,
            id=id,
            metadata=metadata,
            transfer_encoding=transfer_encoding,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentDisposition")
    def reset_content_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentDisposition", []))

    @jsii.member(jsii_name="resetContentEncoding")
    def reset_content_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentEncoding", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCopyFrom")
    def reset_copy_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopyFrom", []))

    @jsii.member(jsii_name="resetDeleteAt")
    def reset_delete_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAt", []))

    @jsii.member(jsii_name="resetEtag")
    def reset_etag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtag", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetTransferEncoding")
    def reset_transfer_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransferEncoding", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="acceptRanges")
    def accept_ranges(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceptRanges"))

    @builtins.property
    @jsii.member(jsii_name="contentLength")
    def content_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "contentLength"))

    @builtins.property
    @jsii.member(jsii_name="lastModified")
    def last_modified(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModified"))

    @builtins.property
    @jsii.member(jsii_name="objectManifest")
    def object_manifest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectManifest"))

    @builtins.property
    @jsii.member(jsii_name="timestamp")
    def timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestamp"))

    @builtins.property
    @jsii.member(jsii_name="transactionId")
    def transaction_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transactionId"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="contentDispositionInput")
    def content_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="contentEncodingInput")
    def content_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="copyFromInput")
    def copy_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copyFromInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAtInput")
    def delete_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deleteAtInput"))

    @builtins.property
    @jsii.member(jsii_name="etagInput")
    def etag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "etagInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="transferEncodingInput")
    def transfer_encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transferEncodingInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939b24ca57537658bbb9b1167bae4d76773c7afb60ee7386a522911fccd5b934)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70eb5d9cfa3c97ee16b80405e17b9033907fbf6b70ade2b5644f0d92b5f6975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentDisposition")
    def content_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentDisposition"))

    @content_disposition.setter
    def content_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41a3eea91c84c594027df704954ffa8fefcbd34dd5c50d5ebd84396a569e638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="contentEncoding")
    def content_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentEncoding"))

    @content_encoding.setter
    def content_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36fab29bc5cd43e48afc3bd5980b3a4fca9d7b582e6ce132a011465d4310027)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentEncoding", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47d0a07aefc64034f472cd6b781617c5043e0bb281931ce69f9add66169b1d0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="copyFrom")
    def copy_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copyFrom"))

    @copy_from.setter
    def copy_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ab606f32761ac6227d2134f1f78ca2adb7152a471ada4210de551c6a03bf04e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyFrom", value)

    @builtins.property
    @jsii.member(jsii_name="deleteAt")
    def delete_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deleteAt"))

    @delete_at.setter
    def delete_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b89e1a599144b0e4cf0ddd8a6dec6b3604d6dbc8d754b0f0d219eb25a28dc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAt", value)

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @etag.setter
    def etag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d284d03fda7e5d50d8a55229e0706fb004fd5ea76323399306a47d5a6526c96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "etag", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660002a9ec69b85cc02a2d3160a0e1d5313f6441c365c2fb52e2a5496d9c4b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55cf18ab02212b58ec9f154648c358bb470c97fa282b7f17226105c1549301e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2de9f146ffea4c825050670d7549616f8996d780735f9ca50cf6ea63c818b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5df4bcda4437e3987e6b4a281b44a26060563b1548862354ab32779ebd275ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="transferEncoding")
    def transfer_encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transferEncoding"))

    @transfer_encoding.setter
    def transfer_encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f25727649f69fad3b1d320924310a4be238a53a7f2e4e5951580e3b3c391caf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transferEncoding", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.storageObject.StorageObjectConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "name": "name",
        "content": "content",
        "content_disposition": "contentDisposition",
        "content_encoding": "contentEncoding",
        "content_type": "contentType",
        "copy_from": "copyFrom",
        "delete_at": "deleteAt",
        "etag": "etag",
        "file": "file",
        "id": "id",
        "metadata": "metadata",
        "transfer_encoding": "transferEncoding",
    },
)
class StorageObjectConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        container: builtins.str,
        name: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_disposition: typing.Optional[builtins.str] = None,
        content_encoding: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        copy_from: typing.Optional[builtins.str] = None,
        delete_at: typing.Optional[jsii.Number] = None,
        etag: typing.Optional[builtins.str] = None,
        file: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        transfer_encoding: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: Name of the storage container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#container StorageObject#container}
        :param name: Name of the storage object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#name StorageObject#name}
        :param content: Raw content in string-form of the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content StorageObject#content}
        :param content_disposition: Overrides the behavior of the browser. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_disposition StorageObject#content_disposition}
        :param content_encoding: Set the content-encoding metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_encoding StorageObject#content_encoding}
        :param content_type: Set the MIME type for the object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_type StorageObject#content_type}
        :param copy_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#copy_from StorageObject#copy_from}.
        :param delete_at: The date and time in UNIX Epoch time stamp format when the system removes the object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#delete_at StorageObject#delete_at}
        :param etag: MD5 checksum value of the request body. Unquoted. Strongly Recommended. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#etag StorageObject#etag}
        :param file: File path for the content to use for data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#file StorageObject#file}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#id StorageObject#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: The object metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#metadata StorageObject#metadata}
        :param transfer_encoding: Sets the transfer encoding. Can only be 'chunked' or Nil, requires Content-Length to be 0 if set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#transfer_encoding StorageObject#transfer_encoding}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20bcd8ca9c302a3192e32e4427a1cfdd9c769ec96c4e5fc1d22cd97bd085424a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_disposition", value=content_disposition, expected_type=type_hints["content_disposition"])
            check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument copy_from", value=copy_from, expected_type=type_hints["copy_from"])
            check_type(argname="argument delete_at", value=delete_at, expected_type=type_hints["delete_at"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument transfer_encoding", value=transfer_encoding, expected_type=type_hints["transfer_encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container": container,
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
        if content is not None:
            self._values["content"] = content
        if content_disposition is not None:
            self._values["content_disposition"] = content_disposition
        if content_encoding is not None:
            self._values["content_encoding"] = content_encoding
        if content_type is not None:
            self._values["content_type"] = content_type
        if copy_from is not None:
            self._values["copy_from"] = copy_from
        if delete_at is not None:
            self._values["delete_at"] = delete_at
        if etag is not None:
            self._values["etag"] = etag
        if file is not None:
            self._values["file"] = file
        if id is not None:
            self._values["id"] = id
        if metadata is not None:
            self._values["metadata"] = metadata
        if transfer_encoding is not None:
            self._values["transfer_encoding"] = transfer_encoding

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
    def container(self) -> builtins.str:
        '''Name of the storage container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#container StorageObject#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the storage object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#name StorageObject#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Raw content in string-form of the data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content StorageObject#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_disposition(self) -> typing.Optional[builtins.str]:
        '''Overrides the behavior of the browser.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_disposition StorageObject#content_disposition}
        '''
        result = self._values.get("content_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_encoding(self) -> typing.Optional[builtins.str]:
        '''Set the content-encoding metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_encoding StorageObject#content_encoding}
        '''
        result = self._values.get("content_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Set the MIME type for the object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#content_type StorageObject#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def copy_from(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#copy_from StorageObject#copy_from}.'''
        result = self._values.get("copy_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_at(self) -> typing.Optional[jsii.Number]:
        '''The date and time in UNIX Epoch time stamp format when the system removes the object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#delete_at StorageObject#delete_at}
        '''
        result = self._values.get("delete_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''MD5 checksum value of the request body. Unquoted. Strongly Recommended.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#etag StorageObject#etag}
        '''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        '''File path for the content to use for data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#file StorageObject#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#id StorageObject#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The object metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#metadata StorageObject#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def transfer_encoding(self) -> typing.Optional[builtins.str]:
        '''Sets the transfer encoding. Can only be 'chunked' or Nil, requires Content-Length to be 0 if set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/storage_object#transfer_encoding StorageObject#transfer_encoding}
        '''
        result = self._values.get("transfer_encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageObjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "StorageObject",
    "StorageObjectConfig",
]

publication.publish()

def _typecheckingstub__6f0b73200ad4c87e119b0066044792a5e7ffc5fd664137b946d0ab514ba20b25(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    container: builtins.str,
    name: builtins.str,
    content: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    copy_from: typing.Optional[builtins.str] = None,
    delete_at: typing.Optional[jsii.Number] = None,
    etag: typing.Optional[builtins.str] = None,
    file: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transfer_encoding: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__939b24ca57537658bbb9b1167bae4d76773c7afb60ee7386a522911fccd5b934(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70eb5d9cfa3c97ee16b80405e17b9033907fbf6b70ade2b5644f0d92b5f6975(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41a3eea91c84c594027df704954ffa8fefcbd34dd5c50d5ebd84396a569e638(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36fab29bc5cd43e48afc3bd5980b3a4fca9d7b582e6ce132a011465d4310027(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d0a07aefc64034f472cd6b781617c5043e0bb281931ce69f9add66169b1d0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ab606f32761ac6227d2134f1f78ca2adb7152a471ada4210de551c6a03bf04e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b89e1a599144b0e4cf0ddd8a6dec6b3604d6dbc8d754b0f0d219eb25a28dc4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d284d03fda7e5d50d8a55229e0706fb004fd5ea76323399306a47d5a6526c96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660002a9ec69b85cc02a2d3160a0e1d5313f6441c365c2fb52e2a5496d9c4b5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55cf18ab02212b58ec9f154648c358bb470c97fa282b7f17226105c1549301e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2de9f146ffea4c825050670d7549616f8996d780735f9ca50cf6ea63c818b2c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5df4bcda4437e3987e6b4a281b44a26060563b1548862354ab32779ebd275ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25727649f69fad3b1d320924310a4be238a53a7f2e4e5951580e3b3c391caf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20bcd8ca9c302a3192e32e4427a1cfdd9c769ec96c4e5fc1d22cd97bd085424a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    container: builtins.str,
    name: builtins.str,
    content: typing.Optional[builtins.str] = None,
    content_disposition: typing.Optional[builtins.str] = None,
    content_encoding: typing.Optional[builtins.str] = None,
    content_type: typing.Optional[builtins.str] = None,
    copy_from: typing.Optional[builtins.str] = None,
    delete_at: typing.Optional[jsii.Number] = None,
    etag: typing.Optional[builtins.str] = None,
    file: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    transfer_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
