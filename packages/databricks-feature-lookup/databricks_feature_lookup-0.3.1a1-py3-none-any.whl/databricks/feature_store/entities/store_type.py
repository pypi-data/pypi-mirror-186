from typing import Any

from databricks.feature_store.entities._proto_enum_entity import _ProtoEnumEntity
from databricks.feature_store.protos.feature_store_serving_pb2 import (
    StoreType as ProtoStoreType,
)


class StoreType(_ProtoEnumEntity):
    """Online store types."""

    AURORA_MYSQL = ProtoStoreType.Value("AURORA_MYSQL")
    SQL_SERVER = ProtoStoreType.Value("SQL_SERVER")
    MYSQL = ProtoStoreType.Value("MYSQL")
    DYNAMODB = ProtoStoreType.Value("DYNAMODB")
    COSMOSDB = ProtoStoreType.Value("COSMOSDB")

    @classmethod
    def _enum_type(cls) -> Any:
        return ProtoStoreType
