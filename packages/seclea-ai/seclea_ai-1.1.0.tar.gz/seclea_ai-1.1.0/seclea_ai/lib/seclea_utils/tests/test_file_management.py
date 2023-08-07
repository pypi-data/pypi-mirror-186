import os.path
import unittest
from tempfile import TemporaryDirectory

import tensorflow as tf

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder_path = os.path.join(base_dir, "tests")


class TestEncodeDecode(unittest.TestCase):
    def setUp(self) -> None:
        # setup file structure

        model: tf.keras.Sequential = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(512, activation="relu", input_shape=(111,)),
                tf.keras.layers.Dropout(0.2),
                tf.keras.layers.Dense(4),
            ]
        )

        # TODO find multiclass classification loss and metrics etc.
        model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
        )

        self.root = TemporaryDirectory()
        tf.keras.models.save_model(model, self.root.name, save_format="tf")

    # TODO: This  test was removed for instability reasons.
    # def test_dir_to_file_to_dir(self):
    #
    #     a = self.root.name
    #     with CustomNamedTemporaryFile() as temp:
    #         with open(temp.name, "wb") as write_f:
    #             encode_dir_to_file(PurePath(self.root.name), file=write_f)
    #         with open(temp.name, "rb") as read_f:
    #             b = decode_file_to_dir(read_f)
    #
    #     comparer = filecmp.dircmp(a, b)
    #     print(comparer.report())
    #
    #     # keeping this in as this is a primary use case that must work - error here means we have issues.
    #     tf.keras.models.load_model(b)
    #
    #     self.assertEqual(
    #         comparer.diff_files,
    #         [],
    #         "Some files are different after decoding...",
    #     )
    #     shutil.rmtree(b)
    #


if __name__ == "__main__":
    unittest.main()
