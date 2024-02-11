import unittest
from dsa.tree.bst import BSTree


class Testbs_tree(unittest.TestCase):
    def setUp(self) -> None:
        self.bs_tree = BSTree()
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
    

    def test_tree_order(self):
        self.assertTrue(True)
            


      

    
    



if __name__ == "__main__":
    unittest.main()
