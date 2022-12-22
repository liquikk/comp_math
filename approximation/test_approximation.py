import unittest
import approximation as app


class tester(unittest.TestCase):
    def test_least_squares_method_1(self):
        data_ay = [[2, 4], [3, 9]]
        answer = 2.69
        self.assertEqual(round(app.least_squares_method(data_ay)[0], 2), answer)

    def test_least_squares_method_2(self):
        data = [[2, 3, 7], [3, 3, 7], [4, 7, 3]]
        answer = [4.68, -2.06]
        self.assertEqual([round(item, 2) for item in app.least_squares_method(data)], answer)

    def test_linear_approximation(self):
        data_xy = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
        x = [2, 3]
        answer = [[2, 2.65], [3, 3.63]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in app.linear_approximation(data_xy, x)], answer)

    def test_polinomial_approximation(self):
        coesf = [0.48, -4.8, 13.96, -7.64]
        x = [1, 3, 5]
        answer = [[1, 2.0], [3, 4.0], [5, 2.16]]
        self.assertEqual([[round(item[0], 2), round(item[1], 2)] for item in app.polinomial_approximation(coesf, x)], answer)

if __name__ == '__main__':
    unittest.main()