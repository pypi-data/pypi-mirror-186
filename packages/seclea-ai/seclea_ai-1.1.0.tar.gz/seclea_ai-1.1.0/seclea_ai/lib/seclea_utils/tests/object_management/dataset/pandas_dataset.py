from unittest import TestCase

import pandas as pd

from seclea_ai.lib.seclea_utils.object_management.dataset.pandas_dataset import PandasDatasetManager


class TestPandasDatasetManager(TestCase):

    def setUp(self) -> None:
        self.dataset = pd.DataFrame(
            {"col1": [0, 1, 2, 3, 4, 5], "col2": [1, 2, 3, 4, 5, 6], "col3": [2, 3, 4, 5, 6, 7], "col4": [3, 4, 5, 6, 7, 8]}
        )
        self.class_outputs_type = "classification"
        self.reg_outputs_type = "regression"
        self.none_outputs_type = None

    def test_get_outputs_info(self):
        # ARRANGE
        outputs = ["col1"]
        expected_class_output = {
            "num_outputs": 1,
            "outputs_classes": [
                6
            ]
        }
        expected_reg_output = {
            "num_outputs": 1,
            "outputs_classes": [
                -1
            ]
        }
        expected_none_output = {
            "num_outputs": 1,
            "outputs_classes": [
                6
            ]
        }

        # ACT
        class_output = PandasDatasetManager.get_outputs_info(
            self.dataset,
            outputs=outputs,
            outputs_type=self.class_outputs_type
        )
        reg_output = PandasDatasetManager.get_outputs_info(
            self.dataset,
            outputs=outputs,
            outputs_type=self.reg_outputs_type
        )
        none_output = PandasDatasetManager.get_outputs_info(
            self.dataset,
            outputs=outputs,
            outputs_type=self.none_outputs_type
        )

        # ASSERT
        self.assertEqual(expected_class_output, class_output, "Classification outputs didn't match")
        self.assertEqual(reg_output, expected_reg_output, "Regression outputs didn't match")
        self.assertEqual(none_output, expected_none_output, "None outputs didn't match")
