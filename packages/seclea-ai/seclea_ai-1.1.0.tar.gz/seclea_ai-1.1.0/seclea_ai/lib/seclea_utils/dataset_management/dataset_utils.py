import pandas as pd
from pandas import DataFrame


def column_hash(dataset: DataFrame) -> int:
    """Invariant to ordering of columns/rows"""
    total = 0
    for col in dataset.columns:
        total += int(pd.util.hash_pandas_object(dataset[col]).sum())
    return total


def dataset_hash(dataset, project_id: str) -> str:
    return str(hash(column_hash(dataset) + hash(project_id)))


def get_dataset_project_hash(dataset, project) -> str:
    return str(hash(bytes(dataset)) + hash(project))


def get_dataset_hash(dataset) -> str:
    return str(hash(bytes(dataset)))


def get_project_hash(project) -> str:
    return str(hash(project))
