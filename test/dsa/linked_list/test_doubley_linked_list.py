import unittest
from dsa.linked_list.doubley_linked_list import DoubleyLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = DoubleyLinkedList()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_is_linkedList_empty(self):
        self.assertTrue(self.linked_list.empty())
        self.assertEqual(0, len(self.linked_list))
        self.assertEqual("[]", str(self.linked_list))

    
    def test_add_at_start(self):
        self.linked_list.add_at_start(7)
        self.assertEqual("[7]", str(self.linked_list))
        self.linked_list.add_at_start(8)
        self.assertEqual("[8, 7]", str(self.linked_list))
        self.linked_list.add_at_start(-2)
        self.assertEqual("[-2, 8, 7]", str(self.linked_list))
        self.assertFalse(self.linked_list.empty())
    
    def test_append(self):
        self.linked_list.append(3)
        self.assertEqual("[3]", str(self.linked_list))
        self.linked_list.append(6)
        self.assertEqual("[3, 6]", str(self.linked_list))
        self.linked_list.append(9)
        self.assertEqual("[3, 6, 9]", str(self.linked_list))
    
    def test_len(self):
        self.linked_list.append(10)
        self.linked_list.append(20)
        self.linked_list.append(30)
        self.assertEqual(3, len(self.linked_list))
    
    def test_delete_between_nodes(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.append(9)

        deletedElement = self.linked_list.delete(4)
        self.assertEqual(deletedElement, 4)
        self.assertEqual("[10, 7, 9]", str(self.linked_list))
    
    def test_delete_first_node(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.append(9)

        deletedElement = self.linked_list.delete(10)
        self.assertEqual(deletedElement, 10)
        self.assertEqual("[4, 7, 9]", str(self.linked_list))
   
    def test_delete_last_node(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.append(9)

        deletedElement = self.linked_list.delete(9)
        self.assertEqual(deletedElement, 9)
        self.assertEqual("[10, 4, 7]", str(self.linked_list))
    
    def test_delete_single_node_list(self):
        self.linked_list.append(7)

        deletedElement = self.linked_list.delete(7)
        self.assertEqual(deletedElement, 7)
        self.assertEqual("[]", str(self.linked_list))
        self.assertTrue(self.linked_list.empty())
        self.assertEqual(0, len(self.linked_list))
    
    def test_delete_should_raise_exception_when_data_not_found(self):
        with self.assertRaises(ValueError) as val:
            deleted_element = self.linked_list.delete(7)
        self.assertEqual("Data: 7 not found", str(val.exception))
    
    def test_search_should_return_location(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.append(9)

        location = self.linked_list.search(4)
        self.assertEqual(location, 2)
        location = self.linked_list.search(10)
        self.assertEqual(location, 1)
        location = self.linked_list.search(7)
        self.assertEqual(location, 3)
        location = self.linked_list.search(9)
        self.assertEqual(location, 4)
    
    def test_search_raise_exeception_data_not_found(self):
        with self.assertRaises(ValueError) as val:
            deleted_element = self.linked_list.search(7)
        self.assertEqual("Data: 7 not found", str(val.exception))
    @unittest.SkipTest
    def test_reverse(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.reverse()
        self.assertEqual("[7, 4, 10]", str(self.linked_list))
        
    
    def test_add_at_valid_location(self):
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        self.linked_list.append(9)

        self.linked_list.add_at_location(5, 50)
        self.assertEqual("[10, 4, 7, 9, 50]", str(self.linked_list))

        self.linked_list.add_at_location(3, 60)
        self.assertEqual("[10, 4, 60, 7, 9, 50]", str(self.linked_list))
        
    
    def test_add_at_invalid_location(self):
        with self.assertRaises(ValueError) as val:
            self.linked_list.add_at_location(10,60)
        self.assertEqual("Location: 10 not found", str(val.exception))
        
   
    def test_add_at_starting_location(self) : 
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        
        self.linked_list.add_at_location(1, 2)
        self.assertEqual("[2, 10, 4, 7]", str(self.linked_list)) 
       
    def test_add_at_last_location(self) : 
        self.linked_list.append(10)
        self.linked_list.append(4)
        self.linked_list.append(7)
        
        self.linked_list.add_at_location(4, 2)
        self.assertEqual("[10, 4, 7, 2]", str(self.linked_list))    

    # def test_concatenate(self):
    #     raise NotImplementedError


if __name__ == "__main__":
    unittest.main()
