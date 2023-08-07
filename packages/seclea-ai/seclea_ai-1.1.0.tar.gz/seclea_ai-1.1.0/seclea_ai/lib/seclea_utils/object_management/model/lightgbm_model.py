import copy
from typing import Any, Dict

import lightgbm as lgb

from lightgbm import Booster

from ..enums import ApplicationType
from ..object_manager import ModelManager
from ..utils import from_file, to_file

try:
    import sklearn
    from sklearn.base import is_classifier, is_regressor
except ImportError:
    is_classifier = None
    is_regressor = None
    sklearn = None


class LightGBMModelManager(ModelManager):
    framework = "lightgbm"

    def save_object(self, obj: Any):
        self.metadata.update({self._model_name_key: obj.__class__.__name__})
        # TODO: review saving here, it seems strange to do it this way, bad smell...
        obj = getattr(obj, "booster_", obj)
        to_file(obj.model_to_string(), self.object_file_path)

    def load_object(self) -> Any:
        """
        :return: LightGBM.Booster model
        """

        model = getattr(lgb, self.metadata.get(self._model_name_key), None)
        if model is None:
            raise TypeError(f"lgb model not found: {self.metadata.get(self._model_name_key)}")
        return model(model_str=from_file(self.object_file_path))

    def hash_object(self, obj) -> int:
        return hash(str(obj))

    @staticmethod
    def _get_booster_params(model) -> Dict:
        return copy.deepcopy(model.params)

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
            return LightGBMModelManager._get_booster_params(model=model)
        # check if sklearn loaded correctly
        elif sklearn is not None:
            if issubclass(model.__class__, sklearn.base.BaseEstimator):
                return LightGBMModelManager._get_sklearn_params(model=model)
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
        objective_application = {
            ApplicationType.REGRESSION: {
                "regression",
                "regression_l2",
                "l2",
                "mean_squared_error",
                "mse",
                "l2_root",
                "root_mean_squared_error",
                "rmse",
                "regression_l1",
                "l1",
                "mean_absolute_error",
                "mae",
                "huber",
                "fair",
                "poisson",
                "quantile",
                "mape",
                "MAPE loss",
                "mean_absolute_percentage_error",
                "gamma",
                "tweedie",
            },
            ApplicationType.BINARY_CLASSIFICATION: {
                "binary",
                "cross_entropy",
                "xentropy",
                # "cross_entropy_lambda", TODO find out if these can be treated like binary class or not
                # "xentlambda"
            },
            ApplicationType.MULTICLASS_CLASSIFICATION: {
                "multiclass",
                "softmax",
                "multiclassova",
                "multiclass_ova",
                "ova",
                "ovr",
            }
        }
        objective_names = {"objective", "objective_type", "app", "application", "loss"}
        # incompatible_param_names = {"fobj"} TODO verify this on Booster object.

        objective = None
        for obj_name in objective_names:
            try:
                objective = model.params[obj_name]
            except KeyError:
                continue
        if objective is None:
            raise ValueError(
                f"Cannot find objective function in params. "
                f"Check model.params for one of {objective_names} and try again."
            )
        for application, objs in objective_application.items():
            if objective in objs:
                tmp = application
                return tmp
        raise ValueError(
            "Cannot autodetect objective function - you are probably using a custom objective. "
            "We currently don't support this, please try again with a standard objective function."
        )

    @staticmethod
    def get_application_type(model) -> ApplicationType:
        # check if Booster - NOTE using __class__.__name__ due to Tracked object interference with type()
        if model.__class__.__name__ == "Booster":
            return LightGBMModelManager._get_booster_application_type(model=model)
        # check if sklearn loaded correctly
        elif sklearn is not None:
            if issubclass(model.__class__, sklearn.base.BaseEstimator):
                return LightGBMModelManager._get_sklearn_application_type(model=model)
        raise ValueError(f"Model class {model.__class__.__name__} is not recognised "
                             f"or is an sklearn interface without sklearn installed.")

