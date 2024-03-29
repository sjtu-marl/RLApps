# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nxdo_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="nxdo_manager.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x12nxdo_manager.proto\x1a\x1bgoogle/protobuf/empty.proto"\x1c\n\nNXDOString\x12\x0e\n\x06string\x18\x01 \x01(\t"<\n\x16NXDOPlayerAndPolicyNum\x12\x0e\n\x06player\x18\x01 \x01(\x03\x12\x12\n\npolicy_num\x18\x02 \x01(\x03"\x1c\n\nNXDOPlayer\x12\x0e\n\x06player\x18\x01 \x01(\x03".\n\x12NXDOPolicySpecJson\x12\x18\n\x10policy_spec_json\x18\x01 \x01(\t"C\n\x12NXDOPolicySpecList\x12-\n\x10policy_spec_list\x18\x01 \x03(\x0b\x32\x13.NXDOPolicySpecJson"\xa1\x01\n\x19NXDONewBestResponseParams\x12\x37\n\x1ametanash_specs_for_players\x18\x01 \x01(\x0b\x32\x13.NXDOPolicySpecList\x12\x37\n\x1a\x64\x65legate_specs_for_players\x18\x02 \x03(\x0b\x32\x13.NXDOPolicySpecList\x12\x12\n\npolicy_num\x18\x03 \x01(\x03"V\n\x19NXDOPolicyMetadataRequest\x12\x0e\n\x06player\x18\x01 \x01(\x03\x12\x12\n\npolicy_num\x18\x02 \x01(\x03\x12\x15\n\rmetadata_json\x18\x03 \x01(\t""\n\x10NXDOConfirmation\x12\x0e\n\x06result\x18\x01 \x01(\x08"%\n\x0cNXDOMetadata\x12\x15\n\rjson_metadata\x18\x01 \x01(\t2\xd3\x02\n\x0bNXDOManager\x12\x32\n\tGetLogDir\x12\x16.google.protobuf.Empty\x1a\x0b.NXDOString"\x00\x12=\n\x12GetManagerMetaData\x12\x16.google.protobuf.Empty\x1a\r.NXDOMetadata"\x00\x12J\n\x1d\x43laimNewActivePolicyForPlayer\x12\x0b.NXDOPlayer\x1a\x1a.NXDONewBestResponseParams"\x00\x12\x46\n\x13SubmitFinalBRPolicy\x12\x1a.NXDOPolicyMetadataRequest\x1a\x11.NXDOConfirmation"\x00\x12=\n\rIsPolicyFixed\x12\x17.NXDOPlayerAndPolicyNum\x1a\x11.NXDOConfirmation"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)


_NXDOSTRING = _descriptor.Descriptor(
    name="NXDOString",
    full_name="NXDOString",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="string",
            full_name="NXDOString.string",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=51,
    serialized_end=79,
)


_NXDOPLAYERANDPOLICYNUM = _descriptor.Descriptor(
    name="NXDOPlayerAndPolicyNum",
    full_name="NXDOPlayerAndPolicyNum",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="player",
            full_name="NXDOPlayerAndPolicyNum.player",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="policy_num",
            full_name="NXDOPlayerAndPolicyNum.policy_num",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=81,
    serialized_end=141,
)


_NXDOPLAYER = _descriptor.Descriptor(
    name="NXDOPlayer",
    full_name="NXDOPlayer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="player",
            full_name="NXDOPlayer.player",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=143,
    serialized_end=171,
)


_NXDOPOLICYSPECJSON = _descriptor.Descriptor(
    name="NXDOPolicySpecJson",
    full_name="NXDOPolicySpecJson",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="policy_spec_json",
            full_name="NXDOPolicySpecJson.policy_spec_json",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=173,
    serialized_end=219,
)


_NXDOPOLICYSPECLIST = _descriptor.Descriptor(
    name="NXDOPolicySpecList",
    full_name="NXDOPolicySpecList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="policy_spec_list",
            full_name="NXDOPolicySpecList.policy_spec_list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=221,
    serialized_end=288,
)


_NXDONEWBESTRESPONSEPARAMS = _descriptor.Descriptor(
    name="NXDONewBestResponseParams",
    full_name="NXDONewBestResponseParams",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="metanash_specs_for_players",
            full_name="NXDONewBestResponseParams.metanash_specs_for_players",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="delegate_specs_for_players",
            full_name="NXDONewBestResponseParams.delegate_specs_for_players",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="policy_num",
            full_name="NXDONewBestResponseParams.policy_num",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=291,
    serialized_end=452,
)


_NXDOPOLICYMETADATAREQUEST = _descriptor.Descriptor(
    name="NXDOPolicyMetadataRequest",
    full_name="NXDOPolicyMetadataRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="player",
            full_name="NXDOPolicyMetadataRequest.player",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="policy_num",
            full_name="NXDOPolicyMetadataRequest.policy_num",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata_json",
            full_name="NXDOPolicyMetadataRequest.metadata_json",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=454,
    serialized_end=540,
)


_NXDOCONFIRMATION = _descriptor.Descriptor(
    name="NXDOConfirmation",
    full_name="NXDOConfirmation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="result",
            full_name="NXDOConfirmation.result",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=542,
    serialized_end=576,
)


_NXDOMETADATA = _descriptor.Descriptor(
    name="NXDOMetadata",
    full_name="NXDOMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="json_metadata",
            full_name="NXDOMetadata.json_metadata",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=578,
    serialized_end=615,
)

_NXDOPOLICYSPECLIST.fields_by_name[
    "policy_spec_list"
].message_type = _NXDOPOLICYSPECJSON
_NXDONEWBESTRESPONSEPARAMS.fields_by_name[
    "metanash_specs_for_players"
].message_type = _NXDOPOLICYSPECLIST
_NXDONEWBESTRESPONSEPARAMS.fields_by_name[
    "delegate_specs_for_players"
].message_type = _NXDOPOLICYSPECLIST
DESCRIPTOR.message_types_by_name["NXDOString"] = _NXDOSTRING
DESCRIPTOR.message_types_by_name["NXDOPlayerAndPolicyNum"] = _NXDOPLAYERANDPOLICYNUM
DESCRIPTOR.message_types_by_name["NXDOPlayer"] = _NXDOPLAYER
DESCRIPTOR.message_types_by_name["NXDOPolicySpecJson"] = _NXDOPOLICYSPECJSON
DESCRIPTOR.message_types_by_name["NXDOPolicySpecList"] = _NXDOPOLICYSPECLIST
DESCRIPTOR.message_types_by_name[
    "NXDONewBestResponseParams"
] = _NXDONEWBESTRESPONSEPARAMS
DESCRIPTOR.message_types_by_name[
    "NXDOPolicyMetadataRequest"
] = _NXDOPOLICYMETADATAREQUEST
DESCRIPTOR.message_types_by_name["NXDOConfirmation"] = _NXDOCONFIRMATION
DESCRIPTOR.message_types_by_name["NXDOMetadata"] = _NXDOMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NXDOString = _reflection.GeneratedProtocolMessageType(
    "NXDOString",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOSTRING,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOString)
    },
)
_sym_db.RegisterMessage(NXDOString)

NXDOPlayerAndPolicyNum = _reflection.GeneratedProtocolMessageType(
    "NXDOPlayerAndPolicyNum",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOPLAYERANDPOLICYNUM,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOPlayerAndPolicyNum)
    },
)
_sym_db.RegisterMessage(NXDOPlayerAndPolicyNum)

NXDOPlayer = _reflection.GeneratedProtocolMessageType(
    "NXDOPlayer",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOPLAYER,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOPlayer)
    },
)
_sym_db.RegisterMessage(NXDOPlayer)

NXDOPolicySpecJson = _reflection.GeneratedProtocolMessageType(
    "NXDOPolicySpecJson",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOPOLICYSPECJSON,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOPolicySpecJson)
    },
)
_sym_db.RegisterMessage(NXDOPolicySpecJson)

NXDOPolicySpecList = _reflection.GeneratedProtocolMessageType(
    "NXDOPolicySpecList",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOPOLICYSPECLIST,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOPolicySpecList)
    },
)
_sym_db.RegisterMessage(NXDOPolicySpecList)

NXDONewBestResponseParams = _reflection.GeneratedProtocolMessageType(
    "NXDONewBestResponseParams",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDONEWBESTRESPONSEPARAMS,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDONewBestResponseParams)
    },
)
_sym_db.RegisterMessage(NXDONewBestResponseParams)

NXDOPolicyMetadataRequest = _reflection.GeneratedProtocolMessageType(
    "NXDOPolicyMetadataRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOPOLICYMETADATAREQUEST,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOPolicyMetadataRequest)
    },
)
_sym_db.RegisterMessage(NXDOPolicyMetadataRequest)

NXDOConfirmation = _reflection.GeneratedProtocolMessageType(
    "NXDOConfirmation",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOCONFIRMATION,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOConfirmation)
    },
)
_sym_db.RegisterMessage(NXDOConfirmation)

NXDOMetadata = _reflection.GeneratedProtocolMessageType(
    "NXDOMetadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _NXDOMETADATA,
        "__module__": "nxdo_manager_pb2"
        # @@protoc_insertion_point(class_scope:NXDOMetadata)
    },
)
_sym_db.RegisterMessage(NXDOMetadata)


_NXDOMANAGER = _descriptor.ServiceDescriptor(
    name="NXDOManager",
    full_name="NXDOManager",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=618,
    serialized_end=957,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetLogDir",
            full_name="NXDOManager.GetLogDir",
            index=0,
            containing_service=None,
            input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            output_type=_NXDOSTRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetManagerMetaData",
            full_name="NXDOManager.GetManagerMetaData",
            index=1,
            containing_service=None,
            input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            output_type=_NXDOMETADATA,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ClaimNewActivePolicyForPlayer",
            full_name="NXDOManager.ClaimNewActivePolicyForPlayer",
            index=2,
            containing_service=None,
            input_type=_NXDOPLAYER,
            output_type=_NXDONEWBESTRESPONSEPARAMS,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="SubmitFinalBRPolicy",
            full_name="NXDOManager.SubmitFinalBRPolicy",
            index=3,
            containing_service=None,
            input_type=_NXDOPOLICYMETADATAREQUEST,
            output_type=_NXDOCONFIRMATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="IsPolicyFixed",
            full_name="NXDOManager.IsPolicyFixed",
            index=4,
            containing_service=None,
            input_type=_NXDOPLAYERANDPOLICYNUM,
            output_type=_NXDOCONFIRMATION,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_NXDOMANAGER)

DESCRIPTOR.services_by_name["NXDOManager"] = _NXDOMANAGER

# @@protoc_insertion_point(module_scope)
