# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SensorNearData/IndicatorRequest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SensorNearData/IndicatorRequest.proto',
  package='pb.Arbitration',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n%SensorNearData/IndicatorRequest.proto\x12\x0epb.Arbitration\x1a\x0cheader.proto\"\xb6\x01\n\x10IndicatorRequest\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12\x45\n\x11indicator_request\x18\x02 \x01(\x0e\x32*.pb.Arbitration.IndicatorRequest.Indicator\"?\n\tIndicator\x12\n\n\x06IS_OFF\x10\x00\x12\x0b\n\x07IS_LEFT\x10\x01\x12\x0c\n\x08IS_RIGHT\x10\x02\x12\x0b\n\x07IS_BOTH\x10\x03'
  ,
  dependencies=[header__pb2.DESCRIPTOR,])



_INDICATORREQUEST_INDICATOR = _descriptor.EnumDescriptor(
  name='Indicator',
  full_name='pb.Arbitration.IndicatorRequest.Indicator',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IS_OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_LEFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_RIGHT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_BOTH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=191,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_INDICATORREQUEST_INDICATOR)


_INDICATORREQUEST = _descriptor.Descriptor(
  name='IndicatorRequest',
  full_name='pb.Arbitration.IndicatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.Arbitration.IndicatorRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indicator_request', full_name='pb.Arbitration.IndicatorRequest.indicator_request', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INDICATORREQUEST_INDICATOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=254,
)

_INDICATORREQUEST.fields_by_name['header'].message_type = header__pb2._HEADER
_INDICATORREQUEST.fields_by_name['indicator_request'].enum_type = _INDICATORREQUEST_INDICATOR
_INDICATORREQUEST_INDICATOR.containing_type = _INDICATORREQUEST
DESCRIPTOR.message_types_by_name['IndicatorRequest'] = _INDICATORREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndicatorRequest = _reflection.GeneratedProtocolMessageType('IndicatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _INDICATORREQUEST,
  '__module__' : 'SensorNearData.IndicatorRequest_pb2'
  # @@protoc_insertion_point(class_scope:pb.Arbitration.IndicatorRequest)
  })
_sym_db.RegisterMessage(IndicatorRequest)


# @@protoc_insertion_point(module_scope)
