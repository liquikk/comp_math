import mclaurin as mcl
import unittest

class tester(unittest.TestCase):
    def test_t_r_exp(self):
        n = 7
        x = 2
        answer = 7.3809523809523805
        self.assertEqual(mcl.mclaurin_exp(n, x), answer)

    def test_t_r_sin(self):
        n = 7
        x = 2
        answer = 0.9092974264614476
        self.assertEqual(mcl.mclaurin_sin(n, x), answer)

    def test_t_r_cos(self):
        n = 6
        x = 3
        answer = -0.9899396306818181
        self.assertEqual(mcl.mclaurin_cos(n, x), answer)

    def test_t_r_arcsin(self):
        n = 3
        x = 1
        answer = 1.286309523809524
        self.assertEqual(mcl.mclaurin_arcsin(n, x), answer)

    def test_t_r_arccos(self):
        n = 3
        x = 1
        answer = 0.28448680298537266
        self.assertEqual(mcl.mclaurin_arccos(n, x), answer)

if __name__ == '__main__':
    unittest.main()