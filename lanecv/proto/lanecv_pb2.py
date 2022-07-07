# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lanecv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lanecv.proto',
  package='acap',
  syntax='proto3',
  serialized_pb=_b('\n\x0clanecv.proto\x12\x04\x61\x63\x61p\"2\n\x0bLaneMessage\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x12\x13\n\x0borientation\x18\x02 \x01(\x01\";\n\x10MultiLaneMessage\x12\'\n\x0claneMessages\x18\x01 \x03(\x0b\x32\x11.acap.LaneMessageB!\n\nacap.modelB\x13LaneMessageProtocolb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LANEMESSAGE = _descriptor.Descriptor(
  name='LaneMessage',
  full_name='acap.LaneMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='acap.LaneMessage.offset', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='acap.LaneMessage.orientation', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=72,
)


_MULTILANEMESSAGE = _descriptor.Descriptor(
  name='MultiLaneMessage',
  full_name='acap.MultiLaneMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='laneMessages', full_name='acap.MultiLaneMessage.laneMessages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=133,
)

_MULTILANEMESSAGE.fields_by_name['laneMessages'].message_type = _LANEMESSAGE
DESCRIPTOR.message_types_by_name['LaneMessage'] = _LANEMESSAGE
DESCRIPTOR.message_types_by_name['MultiLaneMessage'] = _MULTILANEMESSAGE

LaneMessage = _reflection.GeneratedProtocolMessageType('LaneMessage', (_message.Message,), dict(
  DESCRIPTOR = _LANEMESSAGE,
  __module__ = 'lanecv_pb2'
  # @@protoc_insertion_point(class_scope:acap.LaneMessage)
  ))
_sym_db.RegisterMessage(LaneMessage)

MultiLaneMessage = _reflection.GeneratedProtocolMessageType('MultiLaneMessage', (_message.Message,), dict(
  DESCRIPTOR = _MULTILANEMESSAGE,
  __module__ = 'lanecv_pb2'
  # @@protoc_insertion_point(class_scope:acap.MultiLaneMessage)
  ))
_sym_db.RegisterMessage(MultiLaneMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\nacap.modelB\023LaneMessageProtocol'))
# @@protoc_insertion_point(module_scope)