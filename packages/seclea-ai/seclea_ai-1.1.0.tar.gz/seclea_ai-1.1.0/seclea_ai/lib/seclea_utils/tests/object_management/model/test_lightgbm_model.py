import lightgbm as lgb
import pandas as pd
from sklearn import datasets
import os

from ....object_management.enums import ApplicationType
from ....object_management.model.lightgbm_model import LightGBMModelManager

from unittest import TestCase

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, "model")
print(folder_path)


class TestLightGBMModelManager(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # set up binary dataset
        data = pd.read_csv(f"{folder_path}/../../data/filled_na_train.csv").head(10)
        bin_y = data["isFraud"].copy(deep=True)
        bin_X = data.drop("isFraud", axis=1)
        # setup training params
        bin_params = {
            "learning_rate": 0.2,
            "max_depth": 10,
            "min_samples_leaf": 2,
            "max_leaf_nodes": 496,
        }
        # train model
        cls._bin_skl_model = lgb.LGBMClassifier(**bin_params)
        cls._bin_skl_model.fit(bin_X, bin_y)
        bin_dset = lgb.Dataset(
            data=bin_X,
            label=bin_y,
            free_raw_data=True,
        )

        cls._bin_lgb_model = lgb.train(params=dict(max_depth=2, eta=1, objective="binary", num_threads=1, metric="auc"),
                                       train_set=bin_dset, num_boost_round=3)

        # set up multiclass dataset
        multi_X, multi_y = datasets.load_iris(return_X_y=True, as_frame=True)

        # train model
        multi_params = {
            "learning_rate": 0.2,
            "max_depth": 10,
            "min_samples_leaf": 2,
            "max_leaf_nodes": 496,
            "num_class": 3
        }
        cls._multi_skl_model = lgb.LGBMClassifier(**multi_params)
        cls._multi_skl_model.fit(multi_X, multi_y)
        multi_dset = lgb.Dataset(
            data=multi_X,
            label=multi_y,
            free_raw_data=True,
        )
        cls._multi_lgb_model = lgb.train(params=dict(max_depth=2, eta=1, objective="softmax", num_threads=1, num_class=3),
                                       train_set=multi_dset, num_boost_round=3)

        # set up regression dataset
        reg_X, reg_y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

        # train model
        reg_params = {
            "learning_rate": 0.2,
            "max_depth": 10,
            "min_samples_leaf": 2,
            "max_leaf_nodes": 496,
        }
        cls._reg_skl_model = lgb.LGBMRegressor(**reg_params)
        cls._reg_skl_model.fit(reg_X, reg_y)
        reg_dset = lgb.Dataset(
            data=reg_X,
            label=reg_y,
            free_raw_data=True,
        )
        cls._reg_lgb_model = lgb.train(
            params=dict(max_depth=2, eta=1, objective="regression", num_threads=1, metric="auc"),
            train_set=reg_dset, num_boost_round=3)

    def test_get_params(self):
        # ARRANGE
        expected_ret_type = dict

        # ACT
        bin_skl_type = LightGBMModelManager.get_params(self._bin_skl_model)
        multi_skl_type = LightGBMModelManager.get_params(self._multi_skl_model)
        reg_skl_type = LightGBMModelManager.get_params(self._reg_skl_model)
        bin_lgb_type = LightGBMModelManager.get_params(self._bin_lgb_model)
        multi_lgb_type = LightGBMModelManager.get_params(self._multi_lgb_model)
        reg_lgb_type = LightGBMModelManager.get_params(self._reg_lgb_model)

        # ASSERT
        self.assertEqual(type(bin_skl_type), expected_ret_type)
        self.assertEqual(type(multi_skl_type), expected_ret_type)
        self.assertEqual(type(reg_skl_type), expected_ret_type)
        self.assertEqual(type(bin_lgb_type), expected_ret_type)
        self.assertEqual(type(multi_lgb_type), expected_ret_type)
        self.assertEqual(type(reg_lgb_type), expected_ret_type)

    def test_get_application_type(self):
        # ARRANGE

        # ACT
        bin_skl_type = LightGBMModelManager.get_application_type(self._bin_skl_model)
        multi_skl_type = LightGBMModelManager.get_application_type(self._multi_skl_model)
        reg_skl_type = LightGBMModelManager.get_application_type(self._reg_skl_model)
        bin_lgb_type = LightGBMModelManager.get_application_type(self._bin_lgb_model)
        multi_lgb_type = LightGBMModelManager.get_application_type(self._multi_lgb_model)
        reg_lgb_type = LightGBMModelManager.get_application_type(self._reg_lgb_model)

        # ASSERT
        self.assertEqual(bin_skl_type, ApplicationType.BINARY_CLASSIFICATION)
        self.assertEqual(multi_skl_type, ApplicationType.MULTICLASS_CLASSIFICATION)
        self.assertEqual(reg_skl_type, ApplicationType.REGRESSION)
        self.assertEqual(bin_lgb_type, ApplicationType.BINARY_CLASSIFICATION)
        self.assertEqual(multi_lgb_type, ApplicationType.MULTICLASS_CLASSIFICATION)
        self.assertEqual(reg_lgb_type, ApplicationType.REGRESSION)
