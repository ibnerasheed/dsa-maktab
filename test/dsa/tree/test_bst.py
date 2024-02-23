import unittest
from dsa.tree.bst import BSTree


class Testbs_tree(unittest.TestCase):
    def setUp(self) -> None:
        self.bs_tree = BSTree(True)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def populate_tree_data(self):
        self.bs_tree.insert(100)
        self.bs_tree.insert(20)
        self.bs_tree.insert(200) 
        self.bs_tree.insert(10) 
        self.bs_tree.insert(30) 
        self.bs_tree.insert(150)  
        self.bs_tree.insert(300)

        
    
    def test_tree_is_empty(self):
        self.assertTrue(self.bs_tree.empty())
        self.assertEqual("[]", str(self.bs_tree))
        self.assertEqual("[]", self.bs_tree.inorder())
        self.assertEqual("[]", self.bs_tree.preorder())
        self.assertEqual("[]", self.bs_tree.postorder())
        self.assertEqual("[]", self.bs_tree.level_order())



    def test_insert_data_in_tree(self):
        self.bs_tree.insert(100)
        self.assertEqual("[100]", str(self.bs_tree))  
        self.bs_tree.insert(20)
        self.assertEqual("[20, 100]", str(self.bs_tree))  
        self.bs_tree.insert(200)
        self.assertEqual("[20, 100, 200]", str(self.bs_tree))  
        self.bs_tree.insert(10)
        self.assertEqual("[10, 20, 100, 200]", str(self.bs_tree))  
        self.bs_tree.insert(30)
        self.assertEqual("[10, 20, 30, 100, 200]", str(self.bs_tree))  
        self.bs_tree.insert(150)
        self.assertEqual("[10, 20, 30, 100, 150, 200]", str(self.bs_tree))  
        self.bs_tree.insert(300)
        self.assertEqual("[10, 20, 30, 100, 150, 200, 300]", str(self.bs_tree))  

    def test_inorder_traversal(self):
        self.populate_tree_data()
        self.assertEqual("[10, 20, 30, 100, 150, 200, 300]", self.bs_tree.inorder()) 

    def test_preorder_traversal(self):
        self.populate_tree_data()
        self.assertEqual("[100, 20, 10, 30, 200, 150, 300]", self.bs_tree.preorder()) 

    def test_postorder_traversal(self):
        self.populate_tree_data()
        self.assertEqual("[10, 30, 20, 150, 300, 200, 100]", self.bs_tree.postorder())   

    def test_level_order_traversal(self):
        self.populate_tree_data()  
        self.assertEqual("[100, 20, 200, 10, 30, 150, 300]", self.bs_tree.level_order())   
    
    def test_search_should_return_true_if_search_key_is_present(self):
        self.populate_tree_data()
        self.assertTrue(self.bs_tree.search(100))
   
    def test_search_should_return_false_if_search_key_is_not_present(self):
        self.populate_tree_data()
        self.assertFalse(self.bs_tree.search(500))   

    def test_delete_node_when_it_has_no_child(self):
        self.populate_tree_data()
        self.bs_tree.delete(10)
        self.assertEqual("[20, 30, 100, 150, 200, 300]", str(self.bs_tree))  
        self.bs_tree.delete(300)
        self.assertEqual("[20, 30, 100, 150, 200]", str(self.bs_tree)) 
        self.bs_tree.delete(30)
        self.bs_tree.delete(150)
        self.assertEqual("[20, 100, 200]", str(self.bs_tree)) 
        self.bs_tree.delete(20)
        self.bs_tree.delete(200)
        self.assertEqual("[100]", str(self.bs_tree)) 
         

    def test_delete_root_node_when_it_has_no_child(self): 
        self.bs_tree.insert(100)
        self.bs_tree.delete(100)
        self.assertEqual("[]", str(self.bs_tree))

    def test_delete_should_throw_exception_when_data_is_not_present(self):
        self.populate_tree_data()
        with self.assertRaises(ValueError) as val:
            self.bs_tree.delete(678)
        self.assertEqual("Data: 678 not found", str(val.exception))

    def test_delete_node_when_it_has_only_right_child(self):
        self.bs_tree.insert(100)
        self.bs_tree.insert(20)
        self.bs_tree.insert(200)
        self.bs_tree.insert(30)
        self.bs_tree.delete(20)
        self.assertEqual("[30, 100, 200]", str(self.bs_tree))
        
    def test_delete_node_when_it_has_only_left_child(self):
        self.bs_tree.insert(100)
        self.bs_tree.insert(20)
        self.bs_tree.insert(200)
        self.bs_tree.insert(10)
        self.bs_tree.delete(20)
        self.assertEqual("[10, 100, 200]", str(self.bs_tree))
        
    def test_delete_root_node_when_it_has_only_right_child(self):
        self.bs_tree.insert(100)
        self.bs_tree.insert(200)
        self.bs_tree.delete(100)
        self.assertEqual("[200]", str(self.bs_tree))

    def test_delete_root_node_when_it_has_only_left_child(self):
        self.bs_tree.insert(100)
        self.bs_tree.insert(20)
        self.bs_tree.delete(100)
        self.assertEqual("[20]", str(self.bs_tree))

    def test_delete_node_when_it_has_both_child(self):  
        self.populate_tree_data()
        self.bs_tree.delete(200)
        self.assertEqual("[20, 30, 100, 150, 300]", str(self.bs_tree)) 


    def test_delete_root_node_when_it_has_both_child(self):  
        pass
      



       

if __name__ == "__main__":
    unittest.main()
