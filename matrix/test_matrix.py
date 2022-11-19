import matrix as m
import unittest

class tester(unittest.TestCase):
   
    def test_add_matrices(self):
        a = [[1, 2], [3, 4], [5, 6]]
        b = [[1, 2], [3, 4], [5, 6]]
        ans = [[2, 4], [6, 8], [10, 12]]
        self.assertEqual(m.add(a, b), ans)

    def test_transposition(self):
        a=[[1,2],[1,2],[1,2]]
        ans=[[1,1,1],[2,2,2]]
        self.assertEqual(m.transposition(a),ans)

    def test_mlt_scal(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scal = 3
        ans = [[3, 6], [9, 12], [15, 18]]
        self.assertEqual(m.mlt(a, scal), ans)

    def test_mlt_matrices(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        b = [[1, 2], [1, 2], [3, 4]]
        ans = [[12, 18],[27, 42],[42, 66],[57, 90]]
        self.assertEqual(m.mlt(a, b), ans)

    def test_div(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scalar = 1/2
        ans = [[0.5, 1.0], [1.5, 2.0], [2.5, 3.0]]
        self.assertEqual(m.mlt(a, scalar), ans)

    def test_sub_matrices(self):
        a = [[1, 2], [3, 4], [5, 6]]
        b = [[2, 3], [4, 5], [6, 7]]
        ans = [[-1, -1], [-1, -1], [-1, -1]]
        self.assertEqual(m.sub(a, b), ans)
    
    def test_add_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        default = [[1, 2], [3, 4], [5, 6]]
        scal = 2
        row1 = 0
        row2 = 1
        ans = [[7, 10], [3, 4], [5, 6]]
        self.assertEqual(m.add_rows(a, row1, row2, scal), ans)
        self.assertEqual(a, default)

    def test_mlt_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        scal = 2
        row_num = 0
        ans = [[2, 4], [3, 4], [5, 6]]
        self.assertEqual(m.mlt_row(a, row_num, scal), ans)

    def test_change_rows(self):
        a = [[1, 2], [3, 4], [5, 6]]
        row1 = 0
        row2 = 1
        ans = [[3, 4], [1, 2], [5, 6]]
        self.assertEqual(m.change_rows(a, row1, row2, True), ans)
        m.change_rows(a, row1, row2)
        self.assertEqual(a, ans)

if __name__ == '__main__':
    unittest.main()