from __future__ import annotations

from typing import Any, List, Dict

import numpy as np
import pandas as pd
from pandas import DataFrame

from ..object_manager import DatasetManager


class PandasDatasetManager(DatasetManager):

    framework = "pandas"

    def save_object(self, obj: pd.DataFrame):
        """
        @param obj:
        @return:
        """
        obj.to_csv(self.object_file_path, index=True)

    def load_object(self) -> Any:
        return pd.read_csv(self.object_file_path, index_col=self.metadata.get("index", 0))

    def hash_object(self, obj) -> int:
        return sum(int(pd.util.hash_pandas_object(obj[col]).sum()) for col in obj.columns)

    @staticmethod
    def _get_output_classes(col, dataset: DataFrame) -> int:
        """
        Computes the number of output classes - special value is -1 which indicates continuous (regression)
            NOTE: -1 will rely initially on user specification. This function is a fallback approximation that
            will treat numeric variables with unevenly spaced sorted unique values as continuous.
            eg. [0, 1, 2, 3] seems categorical like (with an equal distance between unique sorted values but
                [0, 2, 5, 6, 12] would be considered continuous/regression like and will return -1.
        :param col: output column to analyse
        :param dataset: DataFrame - the dataset.
        :return: int - The number of classes or -1 if continuous/regression target.
        :raises: AttributeError - if any of the listed outputs is not in dataset.columns.
        """
        uniques = dataset[col].unique()
        # do something to check if multiclass or regression.
        if len(uniques) > 2:
            # check type - if int or float need to check more
            if np.issubdtype(uniques.dtype, np.number):
                # check if gaps are the same when sorted - assume regression target if they are not.
                uniques = sorted(uniques)

                def diff(x):
                    v1, v2 = x
                    return v2 - v1
                gaps = list(map(lambda x: diff(x), zip(uniques, uniques[1:])))
                if not all(list(map(lambda x: x == gaps[0], gaps))):
                    return -1
        return len(uniques)

    @staticmethod
    def get_outputs_info(dataset: DataFrame, outputs: List, outputs_type: str) -> Dict:
        """
        Computes outputs_info dict from the outputs and the dataset.
        :param outputs: List The list of outputs eg. ["fraud_reported"] or [] if none.
        :param outputs_type: str or None - The user input about the outputs type. "regression" | "classification" | None
        :param dataset: DataFrame The full dataset. The outputs needs to be a subset of column_names.
        :return: Dict The outputs_info dict. Schema:
            output_info: {
                num_outputs: int the number of variables predicted (same as number of columns in output generally)
                outputs_classes: List[int] the number of classes. -1 indicates continuous ie. regression targets. [] if no outputs
            }
        :raises: AttributeError - if any of the listed outputs is not in dataset.columns.
        :raises KeyError - if the outputs_type is not one of the specified values.
        """

        output_classes = {
            "regression": lambda _: -1,
            "classification": lambda col: len(dataset[col].unique()),
            None: lambda col: PandasDatasetManager._get_output_classes(dataset=dataset, col=col),
        }

        if len(outputs) == 0:
            # no outputs indicated
            return {
                "num_outputs": 0,
                "outputs_classes": []
            }
        else:
            # more output columns
            return {
                "num_outputs": len(outputs),
                "outputs_classes": [output_classes[outputs_type](output) for output in outputs]
            }
