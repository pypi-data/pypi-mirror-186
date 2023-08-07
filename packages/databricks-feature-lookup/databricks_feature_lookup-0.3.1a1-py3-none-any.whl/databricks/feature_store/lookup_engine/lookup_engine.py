""" Defines the LookupEngine class, which is used to perform lookups on online stores. This class
differs from Publish in that its actions are read-only.
"""

import abc
import collections
import functools
import logging
from typing import List

import numpy as np
import pandas as pd

from databricks.feature_store.entities.online_feature_table import OnlineFeatureTable
from databricks.feature_store.entities.online_store_for_serving import (
    MySqlConf,
    SqlServerConf,
)


class LookupEngine(abc.ABC):
    @abc.abstractmethod
    def lookup_features(
        self, lookup_df: pd.DataFrame, feature_names: List[str]
    ) -> pd.DataFrame:
        raise NotImplementedError

    @abc.abstractmethod
    def shutdown(self) -> None:
        raise NotImplementedError
