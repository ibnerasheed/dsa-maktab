import unittest
from dsa.sorting.sorter import selection_sort
class Test_Sorters(unittest.TestCase):
    def test_selection_sort_for_random_list(self):
        random_list = [67, 89, 56, 34, 90]
        expected_random_list = [34, 56, 67, 89, 90]

        self.assertEqual(expected_random_list, selection_sort(random_list))


    def test_selection_sort_for_sorted_list(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [8, 10, 45, 67, 77]
        self.assertEqual(expected_sorted_list, selection_sort(sorted_list))


    def test_selection_sort_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5]
        expected_reverse_sorted_list = [5, 15, 25, 35, 134]
        self.assertEqual(expected_reverse_sorted_list, selection_sort(reverse_sorted_list))    

    def test_selection_sort_if_interval_is_given(self):
        random_list = [67, 89, 56, 34, 90, 100, 22]
        excepted_list = [67, 34, 56, 89, 90, 100, 22]
        self.assertEqual(excepted_list, selection_sort(random_list, 1, 4))

    def test_selection_sort_for_sorted_list_if_interval_is_given(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [8, 10, 45, 67, 77]
        self.assertEqual(expected_sorted_list, selection_sort(sorted_list, 1, 3)) 


    def test_selection_sort_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5, 2]
        expected_reverse_sorted_list = [134, 15, 25, 35, 5, 2]
        self.assertEqual(expected_reverse_sorted_list, selection_sort(reverse_sorted_list, 1, 4))        



    def test_selection_sort_reverse_for_random_list(self):
        random_list = [67, 89, 56, 34, 90]
        expected_random_list = [90, 89, 67, 56, 34]
        self.assertEqual(expected_random_list, selection_sort(random_list, reverse= True))


    def test_selection_sort_reverse_for_sorted_list(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [77, 67, 45, 10, 8]
        self.assertEqual(expected_sorted_list, selection_sort(sorted_list, reverse = True))


    def test_selection_sort_reverse_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5]
        expected_reverse_sorted_list = [134, 35, 25, 15, 5]
        self.assertEqual(expected_reverse_sorted_list, selection_sort(reverse_sorted_list, reverse = True))    

    def test_selection_sort_reverse_if_interval_is_given(self):
        random_list = [67, 89, 34, 56, 90, 100, 22]
        excepted_list = [67, 89, 56, 34, 90, 100, 22]
        self.assertEqual(excepted_list, selection_sort(random_list, 1, 4, reverse = True))
        



if __name__ == "__main__":
    unittest.main()





    
    
    


