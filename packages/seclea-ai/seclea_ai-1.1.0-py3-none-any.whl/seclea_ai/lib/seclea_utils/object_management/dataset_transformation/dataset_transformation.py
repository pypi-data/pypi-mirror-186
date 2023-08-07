import pickle  # nosec
from typing import Any

from ..object_manager import DatasetTransformationManager
from ..utils import to_file, from_file


class GenericDatasetTransformationManager(DatasetTransformationManager):
    def save_object(self, obj: Any):
        to_file(pickle.dumps(obj), self.object_file_path, "wb+")

    def load_object(self) -> Any:
        """
        Loads a stored SKLearn model. As the model is stored with pickle and a certain version of SKLearn, there
        may be inconsistencies where different versions of SKLearn are used for pickling and unpickling.
        :return:
        """
        return pickle.loads(from_file(self.object_file_path, "rb"))  # nosec

    def hash_object(self, obj) -> int:
        return hash(str(obj))
