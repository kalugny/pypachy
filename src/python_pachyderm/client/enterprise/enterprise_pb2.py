# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/enterprise/enterprise.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/enterprise/enterprise.proto',
  package='enterprise',
  syntax='proto3',
  serialized_pb=_b('\n\"client/enterprise/enterprise.proto\x12\nenterprise\x1a\x1fgoogle/protobuf/timestamp.proto\"X\n\x10\x45nterpriseRecord\x12\x17\n\x0f\x61\x63tivation_code\x18\x01 \x01(\t\x12+\n\x07\x65xpires\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\tTokenInfo\x12+\n\x07\x65xpires\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"W\n\x0f\x41\x63tivateRequest\x12\x17\n\x0f\x61\x63tivation_code\x18\x01 \x01(\t\x12+\n\x07\x65xpires\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"7\n\x10\x41\x63tivateResponse\x12#\n\x04info\x18\x01 \x01(\x0b\x32\x15.enterprise.TokenInfo\"\x11\n\x0fGetStateRequest\"Y\n\x10GetStateResponse\x12 \n\x05state\x18\x01 \x01(\x0e\x32\x11.enterprise.State\x12#\n\x04info\x18\x02 \x01(\x0b\x32\x15.enterprise.TokenInfo\"\x13\n\x11\x44\x65\x61\x63tivateRequest\"\x14\n\x12\x44\x65\x61\x63tivateResponse**\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02\x32\xe6\x01\n\x03\x41PI\x12G\n\x08\x41\x63tivate\x12\x1b.enterprise.ActivateRequest\x1a\x1c.enterprise.ActivateResponse\"\x00\x12G\n\x08GetState\x12\x1b.enterprise.GetStateRequest\x1a\x1c.enterprise.GetStateResponse\"\x00\x12M\n\nDeactivate\x12\x1d.enterprise.DeactivateRequest\x1a\x1e.enterprise.DeactivateResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='enterprise.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=530,
  serialized_end=572,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
NONE = 0
ACTIVE = 1
EXPIRED = 2



_ENTERPRISERECORD = _descriptor.Descriptor(
  name='EnterpriseRecord',
  full_name='enterprise.EnterpriseRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='enterprise.EnterpriseRecord.activation_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='enterprise.EnterpriseRecord.expires', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=83,
  serialized_end=171,
)


_TOKENINFO = _descriptor.Descriptor(
  name='TokenInfo',
  full_name='enterprise.TokenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='expires', full_name='enterprise.TokenInfo.expires', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=173,
  serialized_end=229,
)


_ACTIVATEREQUEST = _descriptor.Descriptor(
  name='ActivateRequest',
  full_name='enterprise.ActivateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activation_code', full_name='enterprise.ActivateRequest.activation_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='enterprise.ActivateRequest.expires', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=231,
  serialized_end=318,
)


_ACTIVATERESPONSE = _descriptor.Descriptor(
  name='ActivateResponse',
  full_name='enterprise.ActivateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='enterprise.ActivateResponse.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=320,
  serialized_end=375,
)


_GETSTATEREQUEST = _descriptor.Descriptor(
  name='GetStateRequest',
  full_name='enterprise.GetStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=377,
  serialized_end=394,
)


_GETSTATERESPONSE = _descriptor.Descriptor(
  name='GetStateResponse',
  full_name='enterprise.GetStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='enterprise.GetStateResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='enterprise.GetStateResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=396,
  serialized_end=485,
)


_DEACTIVATEREQUEST = _descriptor.Descriptor(
  name='DeactivateRequest',
  full_name='enterprise.DeactivateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=487,
  serialized_end=506,
)


_DEACTIVATERESPONSE = _descriptor.Descriptor(
  name='DeactivateResponse',
  full_name='enterprise.DeactivateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=508,
  serialized_end=528,
)

_ENTERPRISERECORD.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TOKENINFO.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACTIVATEREQUEST.fields_by_name['expires'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACTIVATERESPONSE.fields_by_name['info'].message_type = _TOKENINFO
_GETSTATERESPONSE.fields_by_name['state'].enum_type = _STATE
_GETSTATERESPONSE.fields_by_name['info'].message_type = _TOKENINFO
DESCRIPTOR.message_types_by_name['EnterpriseRecord'] = _ENTERPRISERECORD
DESCRIPTOR.message_types_by_name['TokenInfo'] = _TOKENINFO
DESCRIPTOR.message_types_by_name['ActivateRequest'] = _ACTIVATEREQUEST
DESCRIPTOR.message_types_by_name['ActivateResponse'] = _ACTIVATERESPONSE
DESCRIPTOR.message_types_by_name['GetStateRequest'] = _GETSTATEREQUEST
DESCRIPTOR.message_types_by_name['GetStateResponse'] = _GETSTATERESPONSE
DESCRIPTOR.message_types_by_name['DeactivateRequest'] = _DEACTIVATEREQUEST
DESCRIPTOR.message_types_by_name['DeactivateResponse'] = _DEACTIVATERESPONSE
DESCRIPTOR.enum_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnterpriseRecord = _reflection.GeneratedProtocolMessageType('EnterpriseRecord', (_message.Message,), dict(
  DESCRIPTOR = _ENTERPRISERECORD,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.EnterpriseRecord)
  ))
_sym_db.RegisterMessage(EnterpriseRecord)

TokenInfo = _reflection.GeneratedProtocolMessageType('TokenInfo', (_message.Message,), dict(
  DESCRIPTOR = _TOKENINFO,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.TokenInfo)
  ))
_sym_db.RegisterMessage(TokenInfo)

ActivateRequest = _reflection.GeneratedProtocolMessageType('ActivateRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVATEREQUEST,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.ActivateRequest)
  ))
_sym_db.RegisterMessage(ActivateRequest)

ActivateResponse = _reflection.GeneratedProtocolMessageType('ActivateResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACTIVATERESPONSE,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.ActivateResponse)
  ))
_sym_db.RegisterMessage(ActivateResponse)

GetStateRequest = _reflection.GeneratedProtocolMessageType('GetStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATEREQUEST,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.GetStateRequest)
  ))
_sym_db.RegisterMessage(GetStateRequest)

GetStateResponse = _reflection.GeneratedProtocolMessageType('GetStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATERESPONSE,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.GetStateResponse)
  ))
_sym_db.RegisterMessage(GetStateResponse)

DeactivateRequest = _reflection.GeneratedProtocolMessageType('DeactivateRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEACTIVATEREQUEST,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.DeactivateRequest)
  ))
_sym_db.RegisterMessage(DeactivateRequest)

DeactivateResponse = _reflection.GeneratedProtocolMessageType('DeactivateResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEACTIVATERESPONSE,
  __module__ = 'client.enterprise.enterprise_pb2'
  # @@protoc_insertion_point(class_scope:enterprise.DeactivateResponse)
  ))
_sym_db.RegisterMessage(DeactivateResponse)



_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='enterprise.API',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=575,
  serialized_end=805,
  methods=[
  _descriptor.MethodDescriptor(
    name='Activate',
    full_name='enterprise.API.Activate',
    index=0,
    containing_service=None,
    input_type=_ACTIVATEREQUEST,
    output_type=_ACTIVATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='enterprise.API.GetState',
    index=1,
    containing_service=None,
    input_type=_GETSTATEREQUEST,
    output_type=_GETSTATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Deactivate',
    full_name='enterprise.API.Deactivate',
    index=2,
    containing_service=None,
    input_type=_DEACTIVATEREQUEST,
    output_type=_DEACTIVATERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)