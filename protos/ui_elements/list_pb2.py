# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui_elements/list.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ui_elements.properties import pixel_location_pb2 as ui__elements_dot_properties_dot_pixel__location__pb2
from ui_elements import text_pb2 as ui__elements_dot_text__pb2
from ui_elements import link_pb2 as ui__elements_dot_link__pb2
from ui_elements import button_pb2 as ui__elements_dot_button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ui_elements/list.proto\x12\x12\x61spire.ui_elements\x1a+ui_elements/properties/pixel_location.proto\x1a\x16ui_elements/text.proto\x1a\x16ui_elements/link.proto\x1a\x18ui_elements/button.proto\"h\n\x04List\x12\x12\n\nparent_uid\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x31\n\x08\x65lements\x18\x04 \x03(\x0b\x32\x1f.aspire.ui_elements.ListElement\"H\n\x0bListElement\x12\x39\n\tlist_data\x18\x01 \x03(\x0b\x32&.aspire.ui_elements.ListElementObjects\"\xa0\x01\n\x12ListElementObjects\x12(\n\x04text\x18\x01 \x01(\x0b\x32\x18.aspire.ui_elements.TextH\x00\x12(\n\x04link\x18\x02 \x01(\x0b\x32\x18.aspire.ui_elements.LinkH\x00\x12,\n\x06\x62utton\x18\x03 \x01(\x0b\x32\x1a.aspire.ui_elements.ButtonH\x00\x42\x08\n\x06Objectb\x06proto3')



_LIST = DESCRIPTOR.message_types_by_name['List']
_LISTELEMENT = DESCRIPTOR.message_types_by_name['ListElement']
_LISTELEMENTOBJECTS = DESCRIPTOR.message_types_by_name['ListElementObjects']
List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
  'DESCRIPTOR' : _LIST,
  '__module__' : 'ui_elements.list_pb2'
  # @@protoc_insertion_point(class_scope:aspire.ui_elements.List)
  })
_sym_db.RegisterMessage(List)

ListElement = _reflection.GeneratedProtocolMessageType('ListElement', (_message.Message,), {
  'DESCRIPTOR' : _LISTELEMENT,
  '__module__' : 'ui_elements.list_pb2'
  # @@protoc_insertion_point(class_scope:aspire.ui_elements.ListElement)
  })
_sym_db.RegisterMessage(ListElement)

ListElementObjects = _reflection.GeneratedProtocolMessageType('ListElementObjects', (_message.Message,), {
  'DESCRIPTOR' : _LISTELEMENTOBJECTS,
  '__module__' : 'ui_elements.list_pb2'
  # @@protoc_insertion_point(class_scope:aspire.ui_elements.ListElementObjects)
  })
_sym_db.RegisterMessage(ListElementObjects)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIST._serialized_start=165
  _LIST._serialized_end=269
  _LISTELEMENT._serialized_start=271
  _LISTELEMENT._serialized_end=343
  _LISTELEMENTOBJECTS._serialized_start=346
  _LISTELEMENTOBJECTS._serialized_end=506
# @@protoc_insertion_point(module_scope)
