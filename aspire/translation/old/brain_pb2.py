# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aspire.translation.cell_pb2 as graph_dot_table_dot_cell__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62rain.proto\x12\x0c\x61spire.brain\x1a\x16graph/table/cell.proto\"D\n\x14UserCopyPasteRequest\x12\x16\n\x0e\x66rom_table_uid\x18\x01 \x01(\t\x12\x14\n\x0cto_table_uid\x18\x02 \x01(\t\"@\n\x15UserCopyPasteResponse\x12\'\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x18.aspire.graph.table.Cell\"@\n\x10\x43opyTableRequest\x12\x16\n\x0e\x66rom_table_uid\x18\x01 \x01(\t\x12\x14\n\x0cto_table_uid\x18\x02 \x01(\t\"<\n\x11\x43opyTableResponse\x12\'\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x18.aspire.graph.table.Cell\"!\n\x11UserActionRequest\x12\x0c\n\x04keys\x18\x01 \x03(\t\"\x14\n\x12UserActionResponse2\x80\x02\n\x05\x42rain\x12X\n\rUserCopyPaste\x12\".aspire.brain.UserCopyPasteRequest\x1a#.aspire.brain.UserCopyPasteResponse\x12L\n\tCopyTable\x12\x1e.aspire.brain.CopyTableRequest\x1a\x1f.aspire.brain.CopyTableResponse\x12O\n\nUserAction\x12\x1f.aspire.brain.UserActionRequest\x1a .aspire.brain.UserActionResponseb\x06proto3')



_USERCOPYPASTEREQUEST = DESCRIPTOR.message_types_by_name['UserCopyPasteRequest']
_USERCOPYPASTERESPONSE = DESCRIPTOR.message_types_by_name['UserCopyPasteResponse']
_COPYTABLEREQUEST = DESCRIPTOR.message_types_by_name['CopyTableRequest']
_COPYTABLERESPONSE = DESCRIPTOR.message_types_by_name['CopyTableResponse']
_USERACTIONREQUEST = DESCRIPTOR.message_types_by_name['UserActionRequest']
_USERACTIONRESPONSE = DESCRIPTOR.message_types_by_name['UserActionResponse']
UserCopyPasteRequest = _reflection.GeneratedProtocolMessageType('UserCopyPasteRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERCOPYPASTEREQUEST,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.UserCopyPasteRequest)
  })
_sym_db.RegisterMessage(UserCopyPasteRequest)

UserCopyPasteResponse = _reflection.GeneratedProtocolMessageType('UserCopyPasteResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERCOPYPASTERESPONSE,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.UserCopyPasteResponse)
  })
_sym_db.RegisterMessage(UserCopyPasteResponse)

CopyTableRequest = _reflection.GeneratedProtocolMessageType('CopyTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _COPYTABLEREQUEST,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.CopyTableRequest)
  })
_sym_db.RegisterMessage(CopyTableRequest)

CopyTableResponse = _reflection.GeneratedProtocolMessageType('CopyTableResponse', (_message.Message,), {
  'DESCRIPTOR' : _COPYTABLERESPONSE,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.CopyTableResponse)
  })
_sym_db.RegisterMessage(CopyTableResponse)

UserActionRequest = _reflection.GeneratedProtocolMessageType('UserActionRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERACTIONREQUEST,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.UserActionRequest)
  })
_sym_db.RegisterMessage(UserActionRequest)

UserActionResponse = _reflection.GeneratedProtocolMessageType('UserActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERACTIONRESPONSE,
  '__module__' : 'brain_pb2'
  # @@protoc_insertion_point(class_scope:aspire.brain.UserActionResponse)
  })
_sym_db.RegisterMessage(UserActionResponse)

_BRAIN = DESCRIPTOR.services_by_name['Brain']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERCOPYPASTEREQUEST._serialized_start=53
  _USERCOPYPASTEREQUEST._serialized_end=121
  _USERCOPYPASTERESPONSE._serialized_start=123
  _USERCOPYPASTERESPONSE._serialized_end=187
  _COPYTABLEREQUEST._serialized_start=189
  _COPYTABLEREQUEST._serialized_end=253
  _COPYTABLERESPONSE._serialized_start=255
  _COPYTABLERESPONSE._serialized_end=315
  _USERACTIONREQUEST._serialized_start=317
  _USERACTIONREQUEST._serialized_end=350
  _USERACTIONRESPONSE._serialized_start=352
  _USERACTIONRESPONSE._serialized_end=372
  _BRAIN._serialized_start=375
  _BRAIN._serialized_end=631
# @@protoc_insertion_point(module_scope)
