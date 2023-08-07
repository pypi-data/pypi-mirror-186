import os
from unittest import TestCase

import lightgbm as lgb
import numpy as np
import pandas as pd

# import tensorflow as tf
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier

from ..model_management import ModelEncodeError, ModelManagers, deserialize, serialize

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, "tests")


class TestSKLearnModelManager(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # read data
        data = pd.read_csv(f"{folder_path}/data/filled_na_train.csv").head(5)
        label = data["isFraud"].copy(deep=True)
        data = data.drop("isFraud", axis=1)
        # setup training params
        params = {
            "learning_rate": 0.2,
            "max_depth": 10,
            "min_samples_leaf": 24,
            "max_leaf_nodes": 496,
        }
        # train model
        cls._booster_skl = GradientBoostingClassifier(**params)
        cls._booster_skl.fit(data, label)
        cls.sample = data.iloc[[0]].to_numpy()

    def setUp(self) -> None:
        pass

    def test_serialize(self):
        serialize(self._booster_skl, ModelManagers.SKLEARN)
        self.assertRaises(ModelEncodeError, serialize, self._booster_skl, ModelManagers.XGBOOST)

    def test_deserialize(self):
        model_b = serialize(self._booster_skl, ModelManagers.SKLEARN)
        model = deserialize(model_b)
        self.assertTrue(
            np.allclose(
                model.predict_proba(self.sample), self._booster_skl.predict_proba(self.sample)
            )
        )


class TestXGBoostModelManager(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # read core
        data = pd.read_csv(f"{folder_path}/data/filled_na_train.csv").head(5)
        label = data["isFraud"].copy(deep=True)
        data = data.drop("isFraud", axis=1)
        cls.data = data
        # load to XGBoost format
        dtrain = xgb.DMatrix(data=data, label=label)
        # setup training params
        params = dict(max_depth=2, eta=1, objective="binary:logistic", nthread=4, eval_metric="auc")
        num_rounds = 5
        # train model
        cls._booster = xgb.train(params=params, dtrain=dtrain, num_boost_round=num_rounds)
        cls._booster_skl = xgb.XGBClassifier(objective="binary:logistic", use_label_encoder=False)
        cls._booster_skl.fit(data, label)
        cls.sample = data.iloc[[0]].to_numpy()

    def setUp(self) -> None:
        pass

    def test_save_learning_api(self):
        serialize(self._booster, ModelManagers.XGBOOST)

    def test_load_from_learning_api(self):
        model_str = serialize(self._booster, ModelManagers.XGBOOST)
        model = deserialize(model_str)

        # os.remove(new_file)
        # test that it executes as expected
        print(
            f"XGBoost from learning - Loaded: {model.inplace_predict(self.sample)} - Original: {self._booster.inplace_predict(self.sample)}"
        )
        self.assertTrue(
            np.allclose(
                model.inplace_predict(self.sample), self._booster.inplace_predict(self.sample)
            )
        )


class TestLightGBMModelManager(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # read data
        data = pd.read_csv(f"{folder_path}/data/filled_na_train.csv").head(5)
        label = data.pop("isFraud")
        # load to XGBoost format
        dtrain = lgb.Dataset(data=data, label=label, free_raw_data=True)
        # setup training params
        params = dict(max_depth=2, eta=1, objective="binary", num_threads=4, metric="auc")
        num_rounds = 5
        # train model
        cls._booster = lgb.train(params=params, train_set=dtrain, num_boost_round=num_rounds)
        cls._booster_skl = lgb.LGBMClassifier(objective="binary")
        cls._booster_skl.fit(data, label)
        cls.sample = data.iloc[[0]]

    def setUp(self) -> None:
        pass

    def test_save_learning_api(self):
        serialize(self._booster, ModelManagers.LIGHTGBM)

    def test_load_from_learning_api(self):
        model_b = serialize(self._booster, ModelManagers.LIGHTGBM)
        model = deserialize(model_b)
        self.assertTrue(np.allclose(model.predict(self.sample), self._booster.predict(self.sample)))
        # os.remove(temp)  # uncomment if not using FileManager


#     def test_save_sklearn_api(self):
#         temp = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
#         stored = self.manager.save_model(model=self._booster_skl, reference=temp)
#         self.assertTrue(os.path.exists(stored))
#         os.remove(stored)
#         # os.remove(temp)  # uncomment if not using FileManager
#
#     def test_load_from_sklearn_api(self):
#         temp = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
#         stored = self.manager.save_model(model=self._booster_skl, reference=temp)
#         model = self.manager.load_model(stored)
#         # os.remove(new_file)
#         # test that it executes as expected
#         print(
#             f"LGBM from SKL Loaded: {model.predict(self.sample)} - Original: {np.delete(self._booster_skl.predict_proba(self.sample), 0)}"
#         )
#         self.assertTrue(
#             np.allclose(
#                 model.predict(self.sample), np.delete(self._booster_skl.predict(self.sample), 0)
#             )
#         )
#         os.remove(stored)
#         # os.remove(temp)  # uncomment if not using FileManager


# class TestTensorflowModelManager(TestCase):
#     @staticmethod
#     def create_model(normalizer):
#
#         model = tf.keras.Sequential(
#             [
#                 normalizer,
#                 tf.keras.layers.Dense(512, activation="relu", input_shape=(111,)),
#                 tf.keras.layers.Dropout(0.2),
#                 tf.keras.layers.Dense(1),
#             ]
#         )
#
#         model.compile(
#             optimizer="adam",
#             loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
#         )
#
#         return model
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         # read core
#         data = pd.read_csv(f"{folder_path}/data/filled_na_train.csv").head(5)
#         label = data["isFraud"].copy(deep=True)
#         data = data.drop("isFraud", axis=1)
#         cls.data = data
#         cls.label = label
#
#         normalizer = tf.keras.layers.Normalization(axis=-1)
#         normalizer.adapt(data)
#
#         # define model
#         tf_model = cls.create_model(normalizer=normalizer)
#         # train model
#         tf_model.fit(data, label, epochs=5)
#         cls._tf_model = tf_model
#
#         cls.sample = data.iloc[[0]].to_numpy()
#
#     def setUp(self) -> None:
#         pass
#
#     def test_save(self):
#         serialize(self._tf_model, ModelManagers.TENSORFLOW)
#
#     def test_load(self):
#         model_str = serialize(self._tf_model, ModelManagers.TENSORFLOW)
#         model = deserialize(model_str)
#
#         loaded = model.predict(self.sample)
#         orig = self._tf_model.predict(self.sample)
#
#         # test that it executes as expected
#         print(f"Tensorflow from learning - Loaded: {loaded} - Original: {orig}")
#         self.assertTrue(np.allclose(loaded, orig))
