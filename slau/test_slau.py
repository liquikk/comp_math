import unittest
import slau as sl

class tester(unittest.TestCase):

    def test_slau_gj_1(self):
        mat = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
        keys = [15, -9, 5]
        answer = [-7.0, -2.0, 2.0]
        self.assertEqual(sl.slau_gj(mat, keys), answer)

    def test_slau_gj_2(self):
        mat = [[4, -2], [6, 1]]
        keys = [22, 45]
        answer = [7.0, 3.0]
        self.assertEqual(sl.slau_gj(mat, keys), answer)

    def test_slau_gj_type_errors(self):
        mat = [[3, -2], [5, 4]]
        keys = [[6], [32]]

        wrong_mat_1 = [['2', 3], [2, 4]]
        wrong_mat_2 = [[3, 45], '23, 22']

        wrong_keys_1 = [2, '3']
        wrong_keys_2 = "2, 3"

        with self.assertRaises(TypeError):
            sl.slau_gj(mat, wrong_keys_1)
        with self.assertRaises(TypeError):
            sl.slau_gj(mat, wrong_keys_2)
        with self.assertRaises(TypeError):
            sl.slau_gj(wrong_mat_1, keys)
        with self.assertRaises(TypeError):
            sl.slau_gj(wrong_mat_2, keys)

    def test_slau_gj_size_errors(self):
        mat = [[3, -2], [5, 4]]
        keys = [[6], [32]]

        wrong_mat_1 = [[2, 3, 3], [3, 5, 6]]

        wrong_keys_1 = [2, 3, 4]
        wrong_keys_2 = []

        with self.assertRaises(ValueError):
            sl.slau_gj(mat, wrong_keys_1)
        with self.assertRaises(ValueError):
            sl.slau_gj(mat, wrong_keys_2)
        with self.assertRaises(ValueError):
            sl.slau_gj(wrong_mat_1, keys)



    # def test_slau_inv_mat_1(self):
    #     mat = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
    #     keys = [15, -9, 5]
    #     answer = [-7.0, -2.0, 2.0]
    #     self.assertEqual(sl.slau_inv_mat(mat, keys), answer)

    # def test_slau_inv_mat_2(self):
    #     mat = [[4, -2], [6, 1]]
    #     keys = [[22], [45]]
    #     answer = [[7.0], [3.0]]
    #     self.assertEqual(sl.slau_inv_mat(mat, keys), answer)

    # def test_slau_inv_mat_type_errors(self):
    #     mat = [[3, -2], [5, 4]]
    #     keys = [[6], [32]]

    #     wrong_mat_1 = [['2', 3], [2, 4]]
    #     wrong_mat_2 = [[3, 45], '23, 22']

    #     wrong_keys_1 = [2, '3']
    #     wrong_keys_2 = "2, 3"

    #     with self.assertRaises(TypeError):
    #         sl.slau_inv_mat(mat, wrong_keys_1)
    #     with self.assertRaises(TypeError):
    #         sl.slau_inv_mat(mat, wrong_keys_2)
    #     with self.assertRaises(TypeError):
    #         sl.slau_inv_mat(wrong_mat_1, keys)
    #     with self.assertRaises(TypeError):
    #         sl.slau_inv_mat(wrong_mat_2, keys)

    # def test_slau_inv_mat_size_errors(self):
    #     mat = [[3, -2], [5, 4]]
    #     keys = [[6], [32]]

    #     wrong_mat_1 = [[2, 3, 3], [3, 5, 6]]

    #     wrong_keys_1 = [2, 3, 4]
    #     wrong_keys_2 = []

    #     with self.assertRaises(ValueError):
    #         sl.slau_inv_mat(mat, wrong_keys_1)
    #     with self.assertRaises(ValueError):
    #         sl.slau_inv_mat(mat, wrong_keys_2)
    #     with self.assertRaises(ValueError):
    #         sl.slau_inv_mat(wrong_mat_1, keys)

if __name__ == '__main__':
    unittest.main()