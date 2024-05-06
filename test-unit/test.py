import unittest
from main import Solution


class TestSolutionInputOk(unittest.TestCase):
    def test_true_array_casual_case(self):
        self.assertEqual(Solution.can_partition([1, 5, 11, 5]), True)
        self.assertEqual(Solution.can_partition([1, 2, 3, 4, 5, 6, 7]), True)

    def test_false_array_casual_case(self):
        self.assertEqual(Solution.can_partition([1, 2, 3, 5]), False)
        self.assertEqual(Solution.can_partition([1, 2, 3, 4, 5, 6]), False)

    def test_false_array_empty_list_case(self):
        self.assertEqual(Solution.can_partition([]), False)

    def test_true_array_single_element_case(self):
        self.assertEqual(Solution.can_partition([0]), True)

    def test_false_array_single_element_case(self):
        self.assertEqual(Solution.can_partition([5]), False)

    def test_true_array_big_nums_case(self):
        self.assertEqual(Solution.can_partition([10**100, 10**100, 2*10**100]), True)
        self.assertEqual(Solution.can_partition([10**6, 10**7, 10**8]), False)

    def test_false_array_big_nums_case(self):
        self.assertEqual(Solution.can_partition([10**600, 10**700, 10**800]), False)

    def test_true_array_negative_nums_case(self):
        self.assertEqual(Solution.can_partition([-1, -5, 5, 11]), True)

    def test_false_array_negative_nums_case(self):
        self.assertEqual(Solution.can_partition([-1, -2, -3, -4, -5, -6]), False)

    def test_true_array_zeros_case(self):
        self.assertEqual(Solution.can_partition([0, 0]), True)

    def test_true_array_float_nums_case(self):
        self.assertEqual(Solution.can_partition([2.1, 3.9, 6]), True)

    def test_false_array_float_nums_case(self):
        self.assertEqual(Solution.can_partition([1.23, 23, 2.3]), False)


class TestSolutionInputBad(unittest.TestCase):
    def test_typeerror_not_list_case(self):
        with self.assertRaises(TypeError):
            Solution.can_partition('test')

    def test_typeerror_not_list_of_nums_case(self):
        with self.assertRaises(TypeError):
            Solution.can_partition([1, 'a', 3])

    def test_keyerror_big_nums_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([1] * 10 ** 100)

    def test_keyerror_big_list_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([1] * 10 ** 100)
