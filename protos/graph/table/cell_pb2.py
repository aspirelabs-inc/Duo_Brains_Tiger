# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graph/table/cell.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from graph.table import coordinates_pb2 as graph_dot_table_dot_coordinates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16graph/table/cell.proto\x12\x12\x61spire.graph.table\x1a\x1dgraph/table/coordinates.proto\"X\n\x04\x43\x65ll\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x34\n\x0b\x63oordinates\x18\x02 \x01(\x0b\x32\x1f.aspire.graph.table.Coordinates\x12\r\n\x05value\x18\x03 \x01(\tb\x06proto3')



_CELL = DESCRIPTOR.message_types_by_name['Cell']
Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), {
  'DESCRIPTOR' : _CELL,
  '__module__' : 'graph.table.cell_pb2'
  # @@protoc_insertion_point(class_scope:aspire.graph.table.Cell)
  })
_sym_db.RegisterMessage(Cell)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CELL._serialized_start=77
  _CELL._serialized_end=165
# @@protoc_insertion_point(module_scope)
