import os.path
import unittest

from ...core.compression import get_compressor

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestOsCompression(unittest.TestCase):
    def setUp(self) -> None:
        self.comp = get_compressor()

    def test_compress_decompress_file(self):
        d_path, d_name = f"{base_dir}/data", "bee_movie.txt"
        o_path = os.path.join(d_path, d_name)
        orig_size = os.path.getsize(o_path)
        c_path, c_name = self.comp.compress(d_path, d_name)
        self.assertTrue(os.path.exists(os.path.join(c_path, c_name)))
        self.assertLess(
            os.path.getsize(os.path.join(c_path, c_name)),
            orig_size,
            "File post compression not smaller",
        )
        d_p, d_n = self.comp.decompress(c_path, c_name)
        self.assertEqual(
            os.path.getsize(os.path.join(d_p, d_n)),
            orig_size,
            "File post decompression not original size",
        )
        os.remove(os.path.join(c_path, c_name))

    def test_compress_decompress_dir(self):
        d_path, d_name = f"{base_dir}/data", "compress_example_dir"
        o_path = os.path.join(d_path, d_name)
        orig_size = os.path.getsize(os.path.join(o_path, "data")) + os.path.getsize(
            os.path.join(o_path, "object")
        )
        c_path, c_name = self.comp.compress(d_path, d_name)
        self.assertTrue(os.path.exists(os.path.join(c_path, c_name)))
        self.assertLess(
            os.path.getsize(os.path.join(c_path, c_name)),
            orig_size,
            "File post compression not smaller",
        )
        d_p, d_n = self.comp.decompress(c_path, c_name)
        d_path = os.path.join(d_p, d_n)
        d_size = os.path.getsize(os.path.join(d_path, "data")) + os.path.getsize(
            os.path.join(d_path, "object")
        )
        self.assertEqual(
            d_size,
            orig_size,
            "File post decompression not original size",
        )
        # os.remove(os.path.join(c_path, c_name))


if __name__ == "__main__":
    unittest.main()
