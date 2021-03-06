# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: books.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='books.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x62ooks.proto\"1\n\x0cGenreRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\"Q\n\x12\x42ookRecommendation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t2B\n\x0fRecommendations\x12/\n\tRecommend\x12\r.GenreRequest\x1a\x13.BookRecommendationb\x06proto3'
)




_GENREREQUEST = _descriptor.Descriptor(
  name='GenreRequest',
  full_name='GenreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='GenreRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='GenreRequest.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=15,
  serialized_end=64,
)


_BOOKRECOMMENDATION = _descriptor.Descriptor(
  name='BookRecommendation',
  full_name='BookRecommendation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BookRecommendation.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='BookRecommendation.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='BookRecommendation.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='BookRecommendation.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=66,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['GenreRequest'] = _GENREREQUEST
DESCRIPTOR.message_types_by_name['BookRecommendation'] = _BOOKRECOMMENDATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenreRequest = _reflection.GeneratedProtocolMessageType('GenreRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENREREQUEST,
  '__module__' : 'books_pb2'
  # @@protoc_insertion_point(class_scope:GenreRequest)
  })
_sym_db.RegisterMessage(GenreRequest)

BookRecommendation = _reflection.GeneratedProtocolMessageType('BookRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRECOMMENDATION,
  '__module__' : 'books_pb2'
  # @@protoc_insertion_point(class_scope:BookRecommendation)
  })
_sym_db.RegisterMessage(BookRecommendation)



_RECOMMENDATIONS = _descriptor.ServiceDescriptor(
  name='Recommendations',
  full_name='Recommendations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=149,
  serialized_end=215,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recommend',
    full_name='Recommendations.Recommend',
    index=0,
    containing_service=None,
    input_type=_GENREREQUEST,
    output_type=_BOOKRECOMMENDATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATIONS)

DESCRIPTOR.services_by_name['Recommendations'] = _RECOMMENDATIONS

# @@protoc_insertion_point(module_scope)
