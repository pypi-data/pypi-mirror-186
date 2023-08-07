import json
from typing import Any, Dict

import tensorflow as tf

from ..enums import ApplicationType
from ..object_manager import ModelManager


# TODO see if we can improve the flow - will require rework of the flow for all models I think
class TensorflowModelManager(ModelManager):
    framework = "tensorflow"

    def save_object(self, obj: Any):
        # save to folder - SavedModel standard
        tf.keras.models.save_model(obj, self.object_file_path, save_format="tf")

    def load_object(self) -> Any:
        """
        Loads a stored XGBoost model. Note this will always return a Booster (LearningAPI model) even if the original
        model was an SKLearn model. This will impact the methods available on the returned model.
        :return: XGBoost.Booster model.
        """
        return tf.keras.models.load_model(self.object_file_path)

    def hash_object(self, obj) -> int:
        return hash(str(obj))

    @staticmethod
    def get_params(model) -> Dict:  # TODO check if this actually gets the parameter
        """
        Extracts the parameters of the model.
        :param model: The model
        """
        return json.loads(model.to_json())

    @staticmethod
    def get_application_type(model) -> ApplicationType:
        # we just need to know the output dimensionality of the model for binary|multiclass
        # TODO look up how regression works
        return ApplicationType.UNKNOWN
