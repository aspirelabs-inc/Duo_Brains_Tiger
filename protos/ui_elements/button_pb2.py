# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui_elements/button.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ui_elements.properties import pixel_location_pb2 as ui__elements_dot_properties_dot_pixel__location__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18ui_elements/button.proto\x12\x12\x61spire.ui_elements\x1a+ui_elements/properties/pixel_location.proto\"x\n\x06\x42utton\x12\x12\n\nparent_uid\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12>\n\x08location\x18\x03 \x01(\x0b\x32,.aspire.ui_elements.properties.PixelLocation\x12\r\n\x05value\x18\x04 \x01(\tb\x06proto3')



_BUTTON = DESCRIPTOR.message_types_by_name['Button']
Button = _reflection.GeneratedProtocolMessageType('Button', (_message.Message,), {
  'DESCRIPTOR' : _BUTTON,
  '__module__' : 'ui_elements.button_pb2'
  # @@protoc_insertion_point(class_scope:aspire.ui_elements.Button)
  })
_sym_db.RegisterMessage(Button)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUTTON._serialized_start=93
  _BUTTON._serialized_end=213
# @@protoc_insertion_point(module_scope)
