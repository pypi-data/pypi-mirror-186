from validate.v1 import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class CreateInventoryObjectRequest(_message.Message):
    __slots__ = ["column", "datastore_id", "db", "object_type", "schema", "sub_column", "table"]
    class Column(_message.Message):
        __slots__ = ["data_type", "name", "path"]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        data_type: str
        name: str
        path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...
    class Db(_message.Message):
        __slots__ = ["name", "path"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class Schema(_message.Message):
        __slots__ = ["name", "path"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class SubColumn(_message.Message):
        __slots__ = ["name", "path", "sub_type"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        path: str
        sub_type: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., sub_type: _Optional[str] = ...) -> None: ...
    class Table(_message.Message):
        __slots__ = ["name", "path"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
    DB_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SUB_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    column: CreateInventoryObjectRequest.Column
    datastore_id: str
    db: CreateInventoryObjectRequest.Db
    object_type: str
    schema: CreateInventoryObjectRequest.Schema
    sub_column: CreateInventoryObjectRequest.SubColumn
    table: CreateInventoryObjectRequest.Table
    def __init__(self, datastore_id: _Optional[str] = ..., object_type: _Optional[str] = ..., db: _Optional[_Union[CreateInventoryObjectRequest.Db, _Mapping]] = ..., schema: _Optional[_Union[CreateInventoryObjectRequest.Schema, _Mapping]] = ..., table: _Optional[_Union[CreateInventoryObjectRequest.Table, _Mapping]] = ..., column: _Optional[_Union[CreateInventoryObjectRequest.Column, _Mapping]] = ..., sub_column: _Optional[_Union[CreateInventoryObjectRequest.SubColumn, _Mapping]] = ...) -> None: ...

class CreateInventoryObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateInventoryTagRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateInventoryTagResponse(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: Tag
    def __init__(self, tag: _Optional[_Union[Tag, _Mapping]] = ...) -> None: ...

class DeleteInventoryObjectRequest(_message.Message):
    __slots__ = ["datastore_id", "path"]
    DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    datastore_id: str
    path: str
    def __init__(self, datastore_id: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class DeleteInventoryObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteInventoryTagRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteInventoryTagResponse(_message.Message):
    __slots__ = ["tags"]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInventoryFlatRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInventoryFlatResponse(_message.Message):
    __slots__ = ["inventory"]
    class Column(_message.Message):
        __slots__ = ["alias", "created_at", "data_label", "data_type", "data_type_oid", "datastore_id", "datastore_name", "name", "path", "table_attribute_number", "table_path", "table_physical_id", "tags", "updated_at", "validated"]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_LABEL_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_OID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TABLE_ATTRIBUTE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
        TABLE_PHYSICAL_ID_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        VALIDATED_FIELD_NUMBER: _ClassVar[int]
        alias: str
        created_at: int
        data_label: str
        data_type: str
        data_type_oid: int
        datastore_id: str
        datastore_name: str
        name: str
        path: str
        table_attribute_number: int
        table_path: str
        table_physical_id: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        updated_at: int
        validated: bool
        def __init__(self, created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., datastore_id: _Optional[str] = ..., datastore_name: _Optional[str] = ..., path: _Optional[str] = ..., table_physical_id: _Optional[str] = ..., table_attribute_number: _Optional[int] = ..., name: _Optional[str] = ..., alias: _Optional[str] = ..., table_path: _Optional[str] = ..., data_label: _Optional[str] = ..., data_type: _Optional[str] = ..., data_type_oid: _Optional[int] = ..., validated: bool = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    inventory: _containers.RepeatedCompositeFieldContainer[GetInventoryFlatResponse.Column]
    def __init__(self, inventory: _Optional[_Iterable[_Union[GetInventoryFlatResponse.Column, _Mapping]]] = ...) -> None: ...

class GetInventoryHierarchicalRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInventoryHierarchicalResponse(_message.Message):
    __slots__ = ["inventory"]
    class Column(_message.Message):
        __slots__ = ["hstores", "name", "path", "table_path"]
        HSTORES_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
        hstores: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.SubColumn]
        name: str
        path: str
        table_path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., table_path: _Optional[str] = ..., hstores: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.SubColumn, _Mapping]]] = ...) -> None: ...
    class Datastore(_message.Message):
        __slots__ = ["dbs", "id", "name"]
        DBS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        dbs: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Db]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., dbs: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Db, _Mapping]]] = ...) -> None: ...
    class Db(_message.Message):
        __slots__ = ["datastore_id", "name", "path", "schemas", "tables"]
        DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SCHEMAS_FIELD_NUMBER: _ClassVar[int]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        datastore_id: str
        name: str
        path: str
        schemas: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Schema]
        tables: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Table]
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., datastore_id: _Optional[str] = ..., schemas: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Schema, _Mapping]]] = ..., tables: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Table, _Mapping]]] = ...) -> None: ...
    class Schema(_message.Message):
        __slots__ = ["db_path", "name", "path", "tables"]
        DB_PATH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        db_path: str
        name: str
        path: str
        tables: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Table]
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., db_path: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Table, _Mapping]]] = ...) -> None: ...
    class SubColumn(_message.Message):
        __slots__ = ["column_path", "name", "path"]
        COLUMN_PATH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        column_path: str
        name: str
        path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., column_path: _Optional[str] = ...) -> None: ...
    class Table(_message.Message):
        __slots__ = ["columns", "db_path", "name", "path", "schema_path"]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        DB_PATH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_PATH_FIELD_NUMBER: _ClassVar[int]
        columns: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Column]
        db_path: str
        name: str
        path: str
        schema_path: str
        def __init__(self, path: _Optional[str] = ..., name: _Optional[str] = ..., db_path: _Optional[str] = ..., schema_path: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Column, _Mapping]]] = ...) -> None: ...
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    inventory: _containers.RepeatedCompositeFieldContainer[GetInventoryHierarchicalResponse.Datastore]
    def __init__(self, inventory: _Optional[_Iterable[_Union[GetInventoryHierarchicalResponse.Datastore, _Mapping]]] = ...) -> None: ...

class GetInventoryTagsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetInventoryTagsResponse(_message.Message):
    __slots__ = ["tags"]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ["created_at", "id", "name"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    created_at: int
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[int] = ...) -> None: ...

class UpdateColumnDataLabelRequest(_message.Message):
    __slots__ = ["data_label", "datastore_id", "path"]
    DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_LABEL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    data_label: str
    datastore_id: str
    path: str
    def __init__(self, datastore_id: _Optional[str] = ..., path: _Optional[str] = ..., data_label: _Optional[str] = ...) -> None: ...

class UpdateColumnDataLabelResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateColumnLockStatusRequest(_message.Message):
    __slots__ = ["datastore_id", "path", "validated"]
    DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_FIELD_NUMBER: _ClassVar[int]
    datastore_id: str
    path: str
    validated: bool
    def __init__(self, datastore_id: _Optional[str] = ..., path: _Optional[str] = ..., validated: bool = ...) -> None: ...

class UpdateColumnLockStatusResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateInventoryObjectTagsRequest(_message.Message):
    __slots__ = ["datastore_id", "path", "tags"]
    DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    datastore_id: str
    path: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, datastore_id: _Optional[str] = ..., path: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateInventoryObjectTagsResponse(_message.Message):
    __slots__ = ["object"]
    class InventoryObject(_message.Message):
        __slots__ = ["created_at", "data_label", "data_store_name", "data_type", "datastore_id", "db_path", "name", "path", "schema_path", "table_attribute_number", "table_path", "tags", "type", "updated_at", "validated"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DATASTORE_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_LABEL_FIELD_NUMBER: _ClassVar[int]
        DATA_STORE_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        DB_PATH_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_PATH_FIELD_NUMBER: _ClassVar[int]
        TABLE_ATTRIBUTE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        VALIDATED_FIELD_NUMBER: _ClassVar[int]
        created_at: int
        data_label: str
        data_store_name: str
        data_type: str
        datastore_id: str
        db_path: str
        name: str
        path: str
        schema_path: str
        table_attribute_number: int
        table_path: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        type: str
        updated_at: int
        validated: bool
        def __init__(self, datastore_id: _Optional[str] = ..., type: _Optional[str] = ..., path: _Optional[str] = ..., db_path: _Optional[str] = ..., table_path: _Optional[str] = ..., schema_path: _Optional[str] = ..., table_attribute_number: _Optional[int] = ..., data_type: _Optional[str] = ..., data_label: _Optional[str] = ..., updated_at: _Optional[int] = ..., created_at: _Optional[int] = ..., data_store_name: _Optional[str] = ..., name: _Optional[str] = ..., validated: bool = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: UpdateInventoryObjectTagsResponse.InventoryObject
    def __init__(self, object: _Optional[_Union[UpdateInventoryObjectTagsResponse.InventoryObject, _Mapping]] = ...) -> None: ...
