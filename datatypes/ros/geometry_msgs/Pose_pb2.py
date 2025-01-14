# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ros/geometry_msgs/Pose.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from datatypes.ros.geometry_msgs import Point_pb2 as ros_dot_geometry__msgs_dot_Point__pb2
from datatypes.ros.geometry_msgs import Quaternion_pb2 as ros_dot_geometry__msgs_dot_Quaternion__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ros/geometry_msgs/Pose.proto',
  package='ros.geometry_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cros/geometry_msgs/Pose.proto\x12\x11ros.geometry_msgs\x1a\x1dros/geometry_msgs/Point.proto\x1a\"ros/geometry_msgs/Quaternion.proto\"f\n\x04Pose\x12*\n\x08position\x18\x01 \x01(\x0b\x32\x18.ros.geometry_msgs.Point\x12\x32\n\x0borientation\x18\x02 \x01(\x0b\x32\x1d.ros.geometry_msgs.Quaternionb\x06proto3'
  ,
  dependencies=[ros_dot_geometry__msgs_dot_Point__pb2.DESCRIPTOR,ros_dot_geometry__msgs_dot_Quaternion__pb2.DESCRIPTOR,])




_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='ros.geometry_msgs.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='ros.geometry_msgs.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='ros.geometry_msgs.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=220,
)

_POSE.fields_by_name['position'].message_type = ros_dot_geometry__msgs_dot_Point__pb2._POINT
_POSE.fields_by_name['orientation'].message_type = ros_dot_geometry__msgs_dot_Quaternion__pb2._QUATERNION
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'ros.geometry_msgs.Pose_pb2'
  # @@protoc_insertion_point(class_scope:ros.geometry_msgs.Pose)
  })
_sym_db.RegisterMessage(Pose)


# @@protoc_insertion_point(module_scope)
