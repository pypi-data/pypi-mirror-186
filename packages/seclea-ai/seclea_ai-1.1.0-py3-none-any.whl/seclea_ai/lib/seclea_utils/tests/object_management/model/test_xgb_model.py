import os

import pandas as pd
import xgboost as xgb

from unittest import TestCase

from sklearn import datasets

from ....object_management.enums import ApplicationType
from ....object_management.model.xgb_model import XGBoostModelManager

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, "model")
print(folder_path)


class TestXGBoostModelManager(TestCase):

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
        cls._bin_skl_model = xgb.XGBClassifier(**bin_params)
        cls._bin_skl_model.fit(bin_X, bin_y)
        bin_dset = xgb.DMatrix(
            data=bin_X,
            label=bin_y,
            enable_categorical=True,
        )

        cls._bin_xgb_model = xgb.train(params=dict(max_depth=2, eta=1, objective="binary:logistic", num_threads=1, metric="auc"),
                                       dtrain=bin_dset, num_boost_round=3)

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
        cls._multi_skl_model = xgb.XGBClassifier(**multi_params)
        cls._multi_skl_model.fit(multi_X, multi_y)
        multi_dset = xgb.DMatrix(
            data=multi_X,
            label=multi_y,
            enable_categorical=True,
        )
        cls._multi_xgb_model = xgb.train(params=dict(max_depth=2, eta=1, objective="multi:softmax", num_threads=1, num_class=3),
                                         dtrain=multi_dset, num_boost_round=3)

        # set up regression dataset
        reg_X, reg_y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

        # train model
        reg_params = {
            "learning_rate": 0.2,
            "max_depth": 10,
            "min_samples_leaf": 2,
            "max_leaf_nodes": 496,
        }
        cls._reg_skl_model = xgb.XGBRegressor(**reg_params)
        cls._reg_skl_model.fit(reg_X, reg_y)
        reg_dset = xgb.DMatrix(
            data=reg_X,
            label=reg_y,
            enable_categorical=True,
        )
        cls._reg_xgb_model = xgb.train(
            params=dict(max_depth=2, eta=1, objective="reg:absoluteerror", num_threads=1, metric="auc"),
            dtrain=reg_dset, num_boost_round=3)

    def test_get_params(self):
        # ARRANGE
        expected_ret_type = dict

        # ACT
        bin_skl_type = XGBoostModelManager.get_params(self._bin_skl_model)
        multi_skl_type = XGBoostModelManager.get_params(self._multi_skl_model)
        reg_skl_type = XGBoostModelManager.get_params(self._reg_skl_model)
        bin_lgb_type = XGBoostModelManager.get_params(self._bin_xgb_model)
        multi_lgb_type = XGBoostModelManager.get_params(self._multi_xgb_model)
        reg_lgb_type = XGBoostModelManager.get_params(self._reg_xgb_model)

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
        bin_skl_type = XGBoostModelManager.get_application_type(self._bin_skl_model)
        multi_skl_type = XGBoostModelManager.get_application_type(self._multi_skl_model)
        reg_skl_type = XGBoostModelManager.get_application_type(self._reg_skl_model)
        bin_lgb_type = XGBoostModelManager.get_application_type(self._bin_xgb_model)
        multi_lgb_type = XGBoostModelManager.get_application_type(self._multi_xgb_model)
        reg_lgb_type = XGBoostModelManager.get_application_type(self._reg_xgb_model)

        # ASSERT
        self.assertEqual(bin_skl_type, ApplicationType.BINARY_CLASSIFICATION)
        self.assertEqual(multi_skl_type, ApplicationType.MULTICLASS_CLASSIFICATION)
        self.assertEqual(reg_skl_type, ApplicationType.REGRESSION)
        self.assertEqual(bin_lgb_type, ApplicationType.BINARY_CLASSIFICATION)
        self.assertEqual(multi_lgb_type, ApplicationType.MULTICLASS_CLASSIFICATION)
        self.assertEqual(reg_lgb_type, ApplicationType.REGRESSION)
