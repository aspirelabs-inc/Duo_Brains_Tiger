# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graph/graph.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aspire.translation.table_pb2 as graph_dot_table_dot_table__pb2

import aspire.translation.list_pb2 as ui__elements_dot_list__pb2
import aspire.translation.button_pb2 as ui__elements_dot_button__pb2
import aspire.translation.link_pb2 as ui__elements_dot_link__pb2
import aspire.translation.text_pb2 as ui__elements_dot_text__pb2

#from ui_elements import list_pb2 as ui__elements_dot_list__pb2
#from ui_elements import button_pb2 as ui__elements_dot_button__pb2
#from ui_elements import link_pb2 as ui__elements_dot_link__pb2
#from ui_elements import text_pb2 as ui__elements_dot_text__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11graph/graph.proto\x12\x0c\x61spire.graph\x1a\x17graph/table/table.proto\x1a\x16ui_elements/list.proto\x1a\x18ui_elements/button.proto\x1a\x16ui_elements/link.proto\x1a\x16ui_elements/text.proto\"\xee\x01\n\nAddRequest\x12(\n\x04list\x18\x01 \x01(\x0b\x32\x18.aspire.ui_elements.ListH\x00\x12(\n\x04text\x18\x02 \x01(\x0b\x32\x18.aspire.ui_elements.TextH\x00\x12(\n\x04link\x18\x03 \x01(\x0b\x32\x18.aspire.ui_elements.LinkH\x00\x12,\n\x06\x62utton\x18\x04 \x01(\x0b\x32\x1a.aspire.ui_elements.ButtonH\x00\x12*\n\x05table\x18\x05 \x01(\x0b\x32\x19.aspire.graph.table.TableH\x00\x42\x08\n\x06Object\"\r\n\x0b\x41\x64\x64Response\"\xf1\x01\n\rUpdateRequest\x12(\n\x04list\x18\x01 \x01(\x0b\x32\x18.aspire.ui_elements.ListH\x00\x12(\n\x04text\x18\x02 \x01(\x0b\x32\x18.aspire.ui_elements.TextH\x00\x12(\n\x04link\x18\x03 \x01(\x0b\x32\x18.aspire.ui_elements.LinkH\x00\x12,\n\x06\x62utton\x18\x04 \x01(\x0b\x32\x1a.aspire.ui_elements.ButtonH\x00\x12*\n\x05table\x18\x05 \x01(\x0b\x32\x19.aspire.graph.table.TableH\x00\x42\x08\n\x06Object\"\x10\n\x0eUpdateResponse2\x88\x01\n\x05Graph\x12:\n\x03\x41\x64\x64\x12\x18.aspire.graph.AddRequest\x1a\x19.aspire.graph.AddResponse\x12\x43\n\x06Update\x12\x1b.aspire.graph.UpdateRequest\x1a\x1c.aspire.graph.UpdateResponseb\x06proto3')



_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_ADDRESPONSE = DESCRIPTOR.message_types_by_name['AddResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateResponse']
AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'graph.graph_pb2'
  # @@protoc_insertion_point(class_scope:aspire.graph.AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'graph.graph_pb2'
  # @@protoc_insertion_point(class_scope:aspire.graph.AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'graph.graph_pb2'
  # @@protoc_insertion_point(class_scope:aspire.graph.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'graph.graph_pb2'
  # @@protoc_insertion_point(class_scope:aspire.graph.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

_GRAPH = DESCRIPTOR.services_by_name['Graph']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=159
  _ADDREQUEST._serialized_end=397
  _ADDRESPONSE._serialized_start=399
  _ADDRESPONSE._serialized_end=412
  _UPDATEREQUEST._serialized_start=415
  _UPDATEREQUEST._serialized_end=656
  _UPDATERESPONSE._serialized_start=658
  _UPDATERESPONSE._serialized_end=674
  _GRAPH._serialized_start=677
  _GRAPH._serialized_end=813
# @@protoc_insertion_point(module_scope)
