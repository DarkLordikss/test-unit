import unittest
from main import Solution


class TestSolutionInputOk(unittest.TestCase):
    def test_true_array_casual_case(self):
        self.assertEqual(Solution.can_partition([1, 5, 11, 5]), True)
        self.assertEqual(Solution.can_partition([1, 2, 3, 4, 5, 6, 7]), True)
        self.assertEqual(Solution.can_partition([100, 100, 100, 100]), True)
        self.assertEqual(Solution.can_partition([1, 1]), True)

    def test_false_array_casual_case(self):
        self.assertEqual(Solution.can_partition([1, 2, 3, 5]), False)
        self.assertEqual(Solution.can_partition([1, 2, 3, 4, 5, 6]), False)
        self.assertEqual(Solution.can_partition([100, 100, 100]), False)
        self.assertEqual(Solution.can_partition([1]), False)

    def test_false_array_single_element_case(self):
        self.assertEqual(Solution.can_partition([5]), False)
        self.assertEqual(Solution.can_partition([1]), False)
        self.assertEqual(Solution.can_partition([100]), False)


class TestSolutionInputBad(unittest.TestCase):
    def test_typeerror_not_list_case(self):
        with self.assertRaises(TypeError):
            Solution.can_partition('test')

    def test_typeerror_not_list_of_nums_case(self):
        with self.assertRaises(TypeError):
            Solution.can_partition([1, 'a', 3])

    def test_keyerror_big_nums_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([101, 101])

    def test_keyerror_big_list_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([1] * 10 ** 100)

    def test_keyerror_array_empty_list_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([])

    def test_keyerror_array_below_one_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([0, 0])

    def test_typeerror_array_float_nums_case(self):
        with self.assertRaises(KeyError):
            Solution.can_partition([2.1, 3.9, 6])
