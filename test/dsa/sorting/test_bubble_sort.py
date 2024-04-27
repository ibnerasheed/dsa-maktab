import unittest
from dsa.sorting.sorter import bubble_sort
from dsa.custom_obj import CustomObj



class Test_Sorters(unittest.TestCase):
    def test_bubble_sort_for_random_list(self):
        random_list = [67, 89, 56, 34, 90]
        expected_random_list = [34, 56, 67, 89, 90]

        self.assertEqual(expected_random_list, bubble_sort(random_list))


    def test_bubble_sort_for_sorted_list(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [8, 10, 45, 67, 77]
        self.assertEqual(expected_sorted_list, bubble_sort(sorted_list))


    def test_bubble_sort_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5]
        expected_reverse_sorted_list = [5, 15, 25, 35, 134]
        self.assertEqual(expected_reverse_sorted_list, bubble_sort(reverse_sorted_list))   
        
         

    def test_bubble_sort_if_interval_is_given(self):
        random_list = [67, 89, 56, 34, 90, 100, 22]
        excepted_list = [67, 34, 56, 89, 90, 100, 22]
        self.assertEqual(excepted_list, bubble_sort(random_list, 1, 4))

    def test_bubble_sort_for_sorted_list_if_interval_is_given(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [8, 10, 45, 67, 77]
        self.assertEqual(expected_sorted_list, bubble_sort(sorted_list, 1, 3)) 


    def test_bubble_sort_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5, 2]
        expected_reverse_sorted_list = [134, 15, 25, 35, 5, 2]
        self.assertEqual(expected_reverse_sorted_list, bubble_sort(reverse_sorted_list, 1, 4))     



    def test_bubble_sort_reverse_for_random_list(self):
        random_list = [67, 89, 56, 34, 90]
        expected_random_list = [90, 89, 67, 56, 34]

        self.assertEqual(expected_random_list, bubble_sort(random_list, reverse= True))


    def test_bubble_sort_reverse_for_sorted_list(self):
        sorted_list = [8, 10, 45, 67, 77]
        expected_sorted_list = [77, 67, 45, 10, 8]
        self.assertEqual(expected_sorted_list, bubble_sort(sorted_list, reverse = True))


    def test_bubble_sort_reverse_for_reverse_sorted_list(self):
        reverse_sorted_list = [134, 35, 25, 15, 5]
        expected_reverse_sorted_list = [134, 35, 25, 15, 5]
        self.assertEqual(expected_reverse_sorted_list, bubble_sort(reverse_sorted_list, reverse = True))    

    def test_bubble_sort_reverse_if_interval_is_given(self):
        random_list = [67, 89, 34, 56, 90, 100, 22]
        excepted_list = [67, 89, 56, 34, 90, 100, 22]
        self.assertEqual(excepted_list, bubble_sort(random_list, 1, 4, reverse = True))
        
    def test_bubble_sort_should_defualt_sort_collection_of_user_defined_objects(self):
        obj1 = CustomObj(1, "aalo")
        obj2 = CustomObj(7, "pyaaz")
        obj3 = CustomObj(11, "larbat")
        objects = [obj3, obj2, obj1]
        expected_sorted_objects = [obj1, obj2, obj3]
        self.assertEqual(expected_sorted_objects, bubble_sort(objects))


        

    def test_bubble_sort_should_sort_colection_of_user_defined_objects_on_given_key_functions(self):
        obj1 = CustomObj(1, "zuccini")
        obj2 = CustomObj(7, "mango")
        obj3 = CustomObj(11, "apple")
        objects = [obj1, obj2, obj3]
        expected_sorted_objects = [obj3, obj2, obj1]
        self.assertEqual(expected_sorted_objects, bubble_sort(objects, key = lambda obj : obj.value))

        

    def test_bubble_sort_should_stable_sort_colection_of_user_defined_objects(self):
        obj1 = CustomObj(1, "zuccini")
        obj2 = CustomObj(10, "mango")
        obj3 = CustomObj(11, "apple")
        obj4 = CustomObj(1, "orange")
        obj5 = CustomObj(7, "mango")
        
        objects = [obj2, obj3, obj1, obj5, obj4]
        expected_sorted_objects = [obj3, obj2, obj5, obj4, obj1]
        self.assertEqual(expected_sorted_objects, bubble_sort(objects, key = lambda obj : obj.value))

        


if __name__ == "__main__":
    unittest.main()





    
    
    


