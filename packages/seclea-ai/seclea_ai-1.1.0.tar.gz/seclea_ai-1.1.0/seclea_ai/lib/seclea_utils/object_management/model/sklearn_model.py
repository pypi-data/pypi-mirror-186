import pickle  # nosec
from typing import Any, Dict
import joblib

from ..enums import ApplicationType
from ..object_manager import ModelManager
from ..utils import from_file
from sklearn.base import is_classifier, is_regressor


class SKLearnModelManager(ModelManager):
    framework = "sklearn"

    def save_object(self, obj: Any):
        joblib.dump(obj, self.object_file_path)

    def load_object(self) -> Any:
        """
        Loads a stored SKLearn model. As the model is stored with pickle and a certain version of SKLearn, there
        may be inconsistencies where different versions of SKLearn are used for pickling and unpickling.
        :return:
        """
        try:
            return joblib.load(self.object_file_path)
        except Exception:
            # fallback on pickle for old files
            return pickle.loads(from_file(self.object_file_path, "rb"))  # nosec

    def hash_object(self, obj) -> int:
        return hash(str(obj))

    @staticmethod
    def get_params(model) -> Dict:
        """
        Extracts the parameters of the model.
        :param model: The model
        """

        return model.get_params()

    @staticmethod
    def get_application_type(model) -> ApplicationType:
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
