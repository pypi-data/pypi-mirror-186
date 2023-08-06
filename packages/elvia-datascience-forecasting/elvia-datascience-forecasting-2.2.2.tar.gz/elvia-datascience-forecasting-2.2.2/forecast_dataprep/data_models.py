from dataclasses import dataclass
from enum import Enum
import json
import re
from typing import List, Optional, Union

import pandas as pd


### Abstractions to represent (a list of) either meteringpoints or substations
class ModelTargetLevel(Enum):

    METERING_POINT = 1
    SUBSTATION = 2


class ModelTargetList:

    def __init__(self,
                 identifiers: Optional[List[Union[str, int]]] = None,
                 allow_duplicates: bool = False) -> None:

        self.identifiers: list = []
        self.allow_duplicates = allow_duplicates

        if identifiers:
            for i in identifiers:
                self.put(i)

    def put(self, identifier: Union[int, str]) -> None:
        level = self.get_type(identifier)
        if level is None:
            raise ValueError('The identifier does not look right')
        if level == ModelTargetLevel.METERING_POINT:
            self._add_if_match_existing(int(identifier))
        if level == ModelTargetLevel.SUBSTATION:
            self._add_if_match_existing(str(identifier).upper())

    def _add_if_match_existing(self, identifier):
        if not self.identifiers or self.get_type(identifier) == self.get_type(
                self.identifiers[0]):
            if self.allow_duplicates or identifier not in set(
                    self.identifiers):
                self.identifiers.append(identifier)
            else:
                raise ValueError('Duplicates not allowed')
        else:
            raise ValueError(
                'Model targets must all be either substation or meteringpoint')

    @staticmethod
    def get_type(identifier: Union[str, int]) -> Optional[ModelTargetLevel]:
        if isinstance(
                identifier, int
        ) and identifier > 707057500014300000 and identifier < 707057500087400700:
            return ModelTargetLevel.METERING_POINT
        elif isinstance(identifier, str) and re.fullmatch(
                r"7070575000[\d]{8}", identifier):
            return ModelTargetLevel.METERING_POINT
        elif isinstance(identifier, str) and re.fullmatch(
                r"T[0-9A-Z\-]+", identifier.upper()):
            return ModelTargetLevel.SUBSTATION
        return None

    @property
    def level(self) -> Optional[ModelTargetLevel]:
        return self.get_type(self.identifiers[0]) if self.identifiers else None

    @staticmethod
    def from_json(target_model_list: str) -> 'ModelTargetList':
        return ModelTargetList(json.loads(target_model_list))

    def to_json(self) -> str:
        return json.dumps(self.identifiers)


### Dataframe groupings


@dataclass
class EnrichmentFeaturesBundle:
    """
    Dataframes used in the enrichment stage
    """
    weekly_average: pd.DataFrame
    school_holidays: pd.DataFrame
    national_holidays: pd.DataFrame
    prices: pd.DataFrame


@dataclass
class Dataframes:
    """
    This class is a convenient encapsulation of diverse dataframes
    """
    hourly_consumption: pd.DataFrame
    ingested: EnrichmentFeaturesBundle


@dataclass
class IngestmentOutput:
    """
    Dataframes that result from the ingestion process
    """
    ingested_hourly_data: pd.DataFrame
    ingested_metadata: pd.DataFrame
    enrichment_features: EnrichmentFeaturesBundle
