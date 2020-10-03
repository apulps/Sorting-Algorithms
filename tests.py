import unittest
from bubble_sort import bubble_sort
from bucket_sort import bucket_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from radix_sort import radix_sort
from selection_sort import selection_sort


class TestSortingAlgorithms(unittest.TestCase):

    def test_bubble_sort(self):
        """
        Test that it can sort a list of numbers with the bubble algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = bubble_sort(data)
        self.assertEqual(output, expected)

    def test_bucket_sort(self):
        """
        Test that it can sort a list of numbers (range from 0.0 to 1.0) with the bucket algorithm.
        """
        data = [0.511, 0.712, 0.233, 0.231, 0.91, 0.1, 0.29, 0.457, 0.899]
        expected = [0.1, 0.231, 0.233, 0.29, 0.457, 0.511, 0.712, 0.899, 0.91]
        output = bucket_sort(data)
        self.assertEqual(output, expected)

    def test_heap_sort(self):
        """
        Test that it can sort a list of numbers with the heap algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = heap_sort(data)
        self.assertEqual(output, expected)

    def test_insertion_sort(self):
        """
        Test that it can sort a list of numbers with the insertion algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = insertion_sort(data)
        self.assertEqual(output, expected)

    def test_merge_sort(self):
        """
        Test that it can sort a list of numbers with the merge algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = merge_sort(data)
        self.assertEqual(output, expected)

    def test_quick_sort(self):
        """
        Test that it can sort a list of numbers with the quick algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = quick_sort(data, 0, len(data) - 1)
        self.assertEqual(output, expected)

    def test_radix_sort(self):
        """
        Test that it can sort a list of numbers with the radix algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = radix_sort(data)
        self.assertEqual(output, expected)

    def test_selection_sort(self):
        """
        Test that it can sort a list of numbers with the selection algorithm.
        """
        data = [4, 78, 2, 33, 0, 99, 86, 4, 21, 3]
        expected = [0, 2, 3, 4, 4, 21, 33, 78, 86, 99]
        output = selection_sort(data)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
