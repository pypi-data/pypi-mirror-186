import uuid
from typing import Union
from abc import ABC


class Relationship:
    certainty: int
    target_hash: int
    target_column_name: str

    def __init__(self, certainty, target_file_hash, target_column_name):
        self.certainty = certainty
        self.target_hash = target_file_hash
        self.target_column_name = target_column_name


class ColMetadata(ABC):
    name: str
    col_type: str
    relationships: list[Relationship]

    def __init__(self, name: str, col_type: str, continuity: float):
        self.name = name
        self.col_type = col_type
        self.continuity = continuity
        self.relationships = []

    def get_attributes(self, stringify: bool):
        """Get the attributes of the column as a dictionary

        Returns: A dictionary of the column attributes
        """
        col_type = self.col_type if not stringify else str(self.col_type)
        return {
            "type": col_type,
            "continuity": self.continuity,
        }

    def add_relationship(self, certainty, target_id, target_column_name):
        self.relationships.append(Relationship(certainty, target_id, target_column_name))


class NumericColMetadata(ColMetadata):
    mean: Union[float, None]
    minimum: any
    maximum: any

    def __init__(self, name: str, col_type: str, continuity: float,
                 mean: Union[int, float, None], min_val, max_val):
        ColMetadata.__init__(self, name, col_type, continuity)
        self.mean = mean
        self.minimum = min_val
        self.maximum = max_val

    def get_attributes(self, stringify: bool):
        """Return the mean/min/max of the column for numeric columns

        Returns: A dictionary of the column attributes
        """
        col_type = self.col_type if not stringify else str(self.col_type)
        return {
            "type": col_type,
            "continuity": self.continuity,
            "mean": self.mean,
            "max": self.maximum,
            "min": self.minimum,
        }


class CategoricalColMetadata(ColMetadata):
    def __init__(self, name: str, col_type: str, continuity: float, columns=None):
        ColMetadata.__init__(self, name, col_type, continuity)


class CatalogueMetadata:
    item_id: uuid.UUID
    data_manifest: dict
    columns: dict[str:ColMetadata] = []
    tags: dict = {}

    def __init__(
            self,
            data_manifest: dict,
            item_id: uuid.UUID = None,
            columns: dict[str, ColMetadata] | None = None,
            tags: dict | None = None
    ):
        self.item_id = item_id
        self.data_manifest = data_manifest
        self.columns = columns or {}
        self.tags = tags or {}
