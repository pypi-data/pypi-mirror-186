from __future__ import annotations

from typing import Any

import tensorflow as tf

from ..object_manager import DatasetManager


class TensorflowDatasetManager(DatasetManager):

    framework = "tensorflow"

    def save_object(self, obj: tf.data.Dataset):
        tf.data.experimental.save(
            obj, self.object_file_path, compression=self.metadata.get("compression", "NONE")
        )

    def load_object(self) -> Any:
        return tf.data.experimental.load(
            self.object_file_path,
            compression=self.metadata.get("compression", "NONE"),
        )

    def hash_object(self, obj) -> int:
        return hash(obj)

    def get_outputs_info(self):
        raise NotImplementedError("Dataset info detection is currently not supported for Tensorflow datasets.")
