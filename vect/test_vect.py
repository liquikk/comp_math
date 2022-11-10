import vect as v
import unittest


class tester(unittest.TestCase):

    def test_sum(self):
        a = [1, 2, 3, 4]
        answer = [2, 3, 4, 5]
        self.assertEqual(v.sum_vect(a, 1), answer)

    def test_sub(self):
        a = [1, 2, 3, 4]
        answer = [0, 1, 2, 3]
        self.assertEqual(v.subtraction(a, 1), answer)
    
    def test_mlt(self):
        a = [1, 2, 3, 0]
        answer = [2, 4, 6, 0]
        self.assertEqual(v.mlt(a, 2), answer)

    def test_div(self):
        a = [10, 22, 35, 0]
        answer = [5, 11, 17.5, 0]
        self.assertEqual(v.div(a, 2), answer)

    def test_scal_pr(self):
        a = [1, 2, 3, 4]
        b = [5, 2, 3, 1]
        self.assertEqual(v.scal_pr(a, b), 22)

    def test_cos(self):
        a = [1, 0, 0]
        b = [0, 1, 1]
        self.assertEqual(v.cos(a, b), 0)

    def test_sum_errors(self):
        a = [1, 2, 3]
        wrong_v1 = ['1', 2, 3]
        wrong_v2 = [True, 2, 3, 0]
        wrong_v3 = [[1, 2], [3, 4]]
        wrong_v4 = [1, 2, 3, 0, 12]

        with self.assertRaises(TypeError):
            v.sum_vect(a, wrong_v1)
        with self.assertRaises(TypeError):
            v.sum_vect(a, wrong_v2)
        with self.assertRaises(TypeError):
            v.sum_vect(a, wrong_v3)
        with self.assertRaises(TypeError):
            v.sum_vect(a, '1')
        with self.assertRaises(ValueError):
            v.sum_vect(a, wrong_v4)

    def test_sub_errors(self):
        a = [1, 2, 3]
        wrong_v1 = ['1', 2, 3]
        wrong_v2 = [True, 2, 3, 0]
        wrong_v3 = [[1, 2], [3, 4]]
        wrong_v4 = [1, 2, 3, 0, 12]

        with self.assertRaises(TypeError):
            v.subtraction(a, wrong_v1)
        with self.assertRaises(TypeError):
            v.subtraction(a, wrong_v2)
        with self.assertRaises(TypeError):
            v.subtraction(a, wrong_v3)
        with self.assertRaises(TypeError):
            v.subtraction(a, '1')
        with self.assertRaises(ValueError):
            v.subtraction(a, wrong_v4)

    def test_div_errors(self):
        a = [1, 2, 3]
        wrong_v1 = ['1', 2, 3]
        wrong_v2 = [True, 2, 3, 0]
        wrong_v3 = [[1, 2], [3, 4]]
        wrong_v4 = [1, 2, 3, 0, 12]

        with self.assertRaises(TypeError):
            v.div(a, wrong_v1)
        with self.assertRaises(TypeError):
            v.div(a, wrong_v2)
        with self.assertRaises(TypeError):
            v.div(a, wrong_v3)
        with self.assertRaises(TypeError):
            v.div(a, '1')
        with self.assertRaises(ValueError):
            v.div(a, wrong_v4)

    def test_mlt_errors(self):
        a = [1, 2, 3]
        wrong_v1 = ['1', 2, 3]
        wrong_v2 = [True, 2, 3, 0]
        wrong_v3 = [[1, 2], [3, 4]]
        wrong_v4 = [1, 2, 3, 0, 12]

        with self.assertRaises(TypeError):
            v.mlt(a, wrong_v1)
        with self.assertRaises(TypeError):
            v.mlt(a, wrong_v2)
        with self.assertRaises(TypeError):
            v.mlt(a, wrong_v3)
        with self.assertRaises(TypeError):
            v.mlt(a, '1')
        with self.assertRaises(ValueError):
            v.mlt(a, wrong_v4)
        
    def test_cos_error(self):
        a = [1, 2]
        b = [1, 2, 3]
        with self.assertRaises(ValueError):
            v.cos(a, b)

if __name__ == '__main__':
    unittest.main()
