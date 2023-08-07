"""
Defines the LookupCosmosDbEngine class, which is used to perform lookups on Cosmos DB online stores.
"""

import functools
import logging
from typing import Any, List

import numpy as np
import pandas as pd
from azure.cosmos import CosmosClient
from azure.cosmos.exceptions import CosmosResourceNotFoundError

from databricks.feature_store.entities.online_feature_table import OnlineFeatureTable
from databricks.feature_store.entities.query_mode import QueryMode
from databricks.feature_store.lookup_engine.lookup_engine import LookupEngine
from databricks.feature_store.utils.cosmosdb_type_utils import (
    COSMOSDB_DATA_TYPE_CONVERTER_FACTORY,
)
from databricks.feature_store.utils.cosmosdb_utils import (
    FEATURE_STORE_SENTINEL_ID_VALUE,
    PARTITION_KEY,
    PATHS,
    PRIMARY_KEY_PROPERTY_NAME_VALUE,
    is_read_item_not_found_error,
    to_cosmosdb_primary_key,
)

_logger = logging.getLogger(__name__)


class LookupCosmosDbEngine(LookupEngine):
    def __init__(
        self, online_feature_table: OnlineFeatureTable, authorization_key: str
    ):
        """
        :param online_feature_table: OnlineFeatureTable to look up feature values from.
        :param authorization_key: Uses this authorization key to authenticate with Cosmos DB.
        """
        # The online feature table name is of the format database_name.container_name.
        self.online_table_name = online_feature_table.online_feature_table_name
        self.database_name, self.container_name = self.online_table_name.split(".")

        # Retrieve the relevant configuration and helpers needed for lookup.
        self.account_uri = online_feature_table.online_store.extra_configs.account_uri
        self.query_mode = online_feature_table.online_store.query_mode
        self.timestamp_keys = online_feature_table.timestamp_keys
        self.primary_keys_to_type_converter = {
            pk.name: COSMOSDB_DATA_TYPE_CONVERTER_FACTORY.get_converter(pk)
            for pk in online_feature_table.primary_keys
        }
        self.features_to_type_converter = {
            feature.name: COSMOSDB_DATA_TYPE_CONVERTER_FACTORY.get_converter(feature)
            for feature in online_feature_table.features
        }

        # Initialize the CosmosClient used for lookup.
        self._client = CosmosClient(self.account_uri, authorization_key)
        self._database_client = self._client.get_database_client(self.database_name)
        self._container_client = self._database_client.get_container_client(
            self.container_name
        )
        self._validate_online_feature_table()

    def _validate_online_feature_table(
        self,
    ) -> None:
        # Check that the online container exists and retrieve its details.
        # Otherwise, a CosmosResourceNotFoundError exception is thrown.
        container_desc = self._container_client.read()

        # All container descriptions contain the partition key and paths. Check the partition key is as expected.
        partition_key_paths = container_desc[PARTITION_KEY][PATHS]
        if partition_key_paths != [f"/{PRIMARY_KEY_PROPERTY_NAME_VALUE}"]:
            raise ValueError(
                f"Online Table {self.online_table_name} primary key schema is not configured properly."
            )

    def lookup_features(
        self, lookup_df: pd.DataFrame, feature_names: List[str]
    ) -> pd.DataFrame:
        query = functools.partial(self._run_lookup_cosmosdb_query, feature_names)
        feature_df = lookup_df.apply(query, axis=1, result_type="expand")
        feature_df.columns = feature_names
        return feature_df

    def _lookup_primary_key(self, cosmosdb_primary_key: str):
        try:
            # The expected response is the item with additional system properties, e.g. {"feat1": ..., "sys1": ...}
            # It's not possible to selectively retrieve features when using point reads (`client.read_item`).
            # However, point reads are recommended over queries (`client.query_items`) for performance and cost.
            # https://docs.microsoft.com/en-us/azure/cosmos-db/optimize-cost-reads-writes

            # As of azure-cosmos==4.2.0 (the minimum required version), `client.read_item` retries up to either of:
            # 30 seconds of timeout or 9 total attempts. Thus, no manual retry handling needs to be done.
            return self._container_client.read_item(
                item=FEATURE_STORE_SENTINEL_ID_VALUE, partition_key=cosmosdb_primary_key
            )
        except Exception as e:
            # Return None if the error was caused by read_item finding no result. Otherwise, re-raise the error.
            if is_read_item_not_found_error(e):
                return None
            _logger.warning(
                f"Encountered error reading from {self.online_table_name}:\n{e}"
            )
            raise e

    def _run_lookup_cosmosdb_query(
        self, feature_names: List[str], lookup_row: pd.core.series.Series
    ):
        """
        This helper function executes a single Cosmos DB query.
        """
        cosmosdb_lookup_row = self._pandas_to_cosmosdb(lookup_row)
        cosmosdb_primary_key = to_cosmosdb_primary_key(cosmosdb_lookup_row)
        if self.query_mode == QueryMode.PRIMARY_KEY_LOOKUP:
            feature_values = self._lookup_primary_key(cosmosdb_primary_key)
        else:
            raise ValueError(f"Unsupported query mode: {self.query_mode}")

        if not feature_values:
            _logger.warning(
                f"No feature values found in {self.online_table_name} for {cosmosdb_lookup_row}."
            )
            return np.full(len(feature_names), np.nan)

        # Return the result
        results = [feature_values.get(f, np.nan) for f in feature_names]
        return self._cosmosdb_to_pandas(results, feature_names)

    def _pandas_to_cosmosdb(self, row: pd.core.series.Series) -> List[Any]:
        """
        Converts the input Pandas row to the Cosmos DB online equivalent Python types.
        """
        return [
            self.primary_keys_to_type_converter[pk_name].to_online_store(pk_value)
            for pk_name, pk_value in row.items()
        ]

    def _cosmosdb_to_pandas(
        self, results: List[Any], feature_names: List[str]
    ) -> List[Any]:
        """
        Converts the online store retrieved item to Pandas compatible Python values for the given features.
        """
        feature_names_and_values = zip(feature_names, results)
        return [
            self.features_to_type_converter[feature_name].to_pandas(feature_value)
            for feature_name, feature_value in feature_names_and_values
        ]

    def shutdown(self) -> None:
        """
        Cleans up the store connection if it exists on the Cosmos DB online store.
        :return:
        """
        # Cosmos DB connections are stateless http connections and hence do not need an explicit
        # shutdown operation.
        pass
