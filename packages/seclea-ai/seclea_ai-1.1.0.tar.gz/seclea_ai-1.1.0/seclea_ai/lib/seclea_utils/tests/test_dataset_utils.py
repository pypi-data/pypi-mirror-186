# This is inconsistent for each type of dataset we can have.
#
# class TestDatasetHashing(TestCase):
#     def setUp(self) -> None:
#         self.orig = pd.DataFrame(
#             [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]], columns=["a", "b", "c"]
#         )
#
#     def test_shuffle_rows(self):
#         shuf = self.orig.copy(deep=True)
#         shuf = shuf.reindex(np.random.permutation(len(shuf)))
#
#         self.assertEqual(
#             dataset_hash(self.orig, 1), dataset_hash(shuf, 1), "Row order affects hash"
#         )
#
#     def test_shuffle_columns(self):
#         shuf = self.orig.copy(deep=True)
#         shuf = shuf[[c for c in shuf if c not in ["c"]] + ["c"]]
#
#         self.assertEqual(
#             dataset_hash(self.orig, 1), dataset_hash(shuf, 1), "Column order affects hash"
#         )
#
#     def test_single_cell_change(self):
#         shuf = self.orig.copy(deep=True)
#         shuf.iat[0, 2] = 6
#         print(shuf)
#
#         self.assertNotEqual(
#             dataset_hash(self.orig, 1), dataset_hash(shuf, 1), "Row order affects hash"
#         )
