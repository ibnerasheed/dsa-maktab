import unittest
from dsa.sorting.sorter import bubble_sort



class Test_Sorters(unittest.TestCase):
    
    
    def test_bubble_sort(self):
        self.random_list = [67, 89, 56, 34, 90]
        self.expected_random_list = [34, 56, 67, 89, 90]

        self.sorted_list = [8, 10, 45, 67, 77]
        self.expected_sorted_list = [8, 10, 45, 67, 77]

        self.reverse_sorted_list = [134, 35, 25, 15, 5]
        self.expected_reverse_sorted_list = [5, 15, 25, 35, 134]

        self.assertEqual(self.expected_random_list, bubble_sort(self.random_list))
        self.assertEqual(self.expected_sorted_list, bubble_sort(self.sorted_list))
        self.assertEqual(self.expected_reverse_sorted_list, bubble_sort(self.reverse_sorted_list))



if __name__ == "__main__":
    unittest.main()





    
    
    


