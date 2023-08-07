import pandas as pd
from sklearn import datasets
import os

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from ....object_management.enums import ApplicationType
from ....object_management.model.lightgbm_model import LightGBMModelManager

from unittest import TestCase

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, "model")
print(folder_path)


class TestSKLearnModelManager(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # set up binary dataset
        data = pd.read_csv(f"{folder_path}/../../data/filled_na_train.csv").head(10)
        bin_y = data["isFraud"].copy(deep=True)
        bin_X = data.drop("isFraud", axis=1)
        # setup training params

        # train model
        cls._bin_skl_model = RandomForestClassifier(random_state=42)
        cls._bin_skl_model.fit(bin_X, bin_y)

        # set up multiclass dataset
        multi_X, multi_y = datasets.load_iris(return_X_y=True, as_frame=True)

        # train model
        cls._multi_skl_model = RandomForestClassifier(random_state=42)
        cls._multi_skl_model.fit(multi_X, multi_y)

        # set up regression dataset
        reg_X, reg_y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

        # train model
        cls._reg_skl_model = RandomForestRegressor(random_state=42)
        cls._reg_skl_model.fit(reg_X, reg_y)

    def test_get_params(self):
        # ARRANGE
        expected_ret_type = dict

        # ACT
        bin_skl_type = LightGBMModelManager.get_params(self._bin_skl_model)
        multi_skl_type = LightGBMModelManager.get_params(self._multi_skl_model)
        reg_skl_type = LightGBMModelManager.get_params(self._reg_skl_model)

        # ASSERT
        self.assertEqual(type(bin_skl_type), expected_ret_type)
        self.assertEqual(type(multi_skl_type), expected_ret_type)
        self.assertEqual(type(reg_skl_type), expected_ret_type)

    def test_get_application_type(self):
        # ARRANGE

        # ACT
        bin_skl_type = LightGBMModelManager.get_application_type(self._bin_skl_model)
        multi_skl_type = LightGBMModelManager.get_application_type(self._multi_skl_model)
        reg_skl_type = LightGBMModelManager.get_application_type(self._reg_skl_model)

        # ASSERT
        self.assertEqual(bin_skl_type, ApplicationType.BINARY_CLASSIFICATION)
        self.assertEqual(multi_skl_type, ApplicationType.MULTICLASS_CLASSIFICATION)
        self.assertEqual(reg_skl_type, ApplicationType.REGRESSION)
