import json
from typing import Any, Dict

import xgboost as xgb
from xgboost import Booster

from ..enums import ApplicationType
from ..object_manager import ModelManager

try:
    import sklearn
    from sklearn.base import is_classifier, is_regressor
except ImportError:
    is_classifier = None
    is_regressor = None
    sklearn = None


class XGBoostModelManager(ModelManager):

    framework = "xgboost"

    def save_object(self, obj: xgb.Booster):
        # save to temp file then use manager to store.
        self.metadata.update({self._model_name_key: obj.__class__.__name__})
        obj.save_model(self.object_file_path)

    def load_object(self) -> Any:
        """
        Loads a stored XGBoost model. Note this will always return a Booster (LearningAPI model) even if the original
        model was an SKLearn model. This will impact the methods available on the returned model.
        :param reference:
        :return: XGBoost.Booster model.
        """
        # TODO need to be careful about customer usage - ie. do they use the best iteration for their model or not....
        model_name = self.metadata.get(self._model_name_key)
        model = getattr(xgb, model_name, None)
        if model is None:
            raise TypeError(f"Cannot load xgboost model: {model_name} - not found")
        model = model()
        model.load_model(self.object_file_path)
        return model

    def hash_object(self, obj) -> int:
        return hash(str(obj))

    @staticmethod
    def _get_booster_params(model) -> Dict:
        return json.loads(model.save_config())

    @staticmethod
    def _get_sklearn_params(model) -> Dict:
        return model.get_params()

    @staticmethod
    def get_params(model) -> Dict:
        """
        Extracts the parameters of the model.
        :param model: The model
        """
        if model.__class__.__name__ == "Booster":
            return XGBoostModelManager._get_booster_params(model=model)
        # check if sklearn loaded correctly
        elif sklearn is not None:
            if issubclass(model.__class__, sklearn.base.BaseEstimator):
                return XGBoostModelManager._get_sklearn_params(model=model)
        raise ValueError(f"Model class {model.__class__.__name__} is not recognised "
                         f"or is an sklearn interface without sklearn installed.")

    @staticmethod
    def _get_sklearn_application_type(model) -> ApplicationType:
        # we assume that scikit learn is loaded
        # see https://github.com/microsoft/LightGBM/blob/master/python-package/lightgbm/sklearn.py#L493
        if is_classifier(model):
            try:
                if model.n_classes_ == 2:
                    return ApplicationType.BINARY_CLASSIFICATION
                elif model.n_classes_ > 2:
                    return ApplicationType.MULTICLASS_CLASSIFICATION
                else:
                    raise ValueError(f"Found unexpected number of classes {model.n_classes_}")
            # no n_classes_ attribute we can only say it's a classifier.
            except AttributeError:
                return ApplicationType.CLASSIFICATION
        elif is_regressor(model):
            return ApplicationType.REGRESSION
        else:
            raise ValueError("We currently don't support applications other than classification and regression. "
                             "Support for other model types will be added in the future")

    @staticmethod
    def _get_booster_application_type(model: Booster) -> ApplicationType:
        params = XGBoostModelManager.get_params(model=model)
        objective = params["learner"]["objective"]["name"]
        if "binary" in objective:
            return ApplicationType.BINARY_CLASSIFICATION
        elif "multi" in objective:
            return ApplicationType.MULTICLASS_CLASSIFICATION
        elif "reg" in objective:
            return ApplicationType.REGRESSION
        else:
            raise ValueError(f"We currently only support Classification and Regression objective functions. "
                             f"Current objective function is {objective}")

    @staticmethod
    def get_application_type(model) -> ApplicationType:
        if model.__class__.__name__ == "Booster":
            return XGBoostModelManager._get_booster_application_type(model=model)
        elif sklearn is not None:
            if issubclass(model.__class__, sklearn.base.BaseEstimator):
                return XGBoostModelManager._get_sklearn_application_type(model=model)
        else:
            raise ValueError(f"Model class {model.__class__.__name__} is not recognised "
                             f"or is an sklearn interface without sklearn installed.")

