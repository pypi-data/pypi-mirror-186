from unittest import TestCase

from ..model_management import ModelEncodeError, ModelManagers, serialize


class Test(TestCase):
    def test_get_model_manager_framework_not_installed_exception(self):
        self.assertRaises(ModelEncodeError, serialize, "random model", ModelManagers.NOT_IMPORTED)

    def test_get_model_manager_sklearn_installed(self):
        self.assertIsNotNone(
            ModelManagers.SKLEARN.value,
            msg="Failed to instantiate framework",
        )

    def test_get_model_manager_xgboost_installed(self):
        self.assertIsNotNone(
            ModelManagers.XGBOOST.value,
            msg="Failed to instantiate framework",
        )

    def test_get_model_manager_lightgbm_installed(self):
        self.assertIsNotNone(
            ModelManagers.LIGHTGBM.value,
            msg="Failed to instantiate framework",
        )

    def test_get_model_manager_tensorflow_installed(self):
        self.assertIsNotNone(
            ModelManagers.TENSORFLOW.value,
            msg="Failed to instantiate framework",
        )
