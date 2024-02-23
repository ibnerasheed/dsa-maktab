from dsa.common.node import TreeNode
from dsa.queue.dynamic_queue import DynamicQueue
from dsa.queue.static_queue import FixedSizeQueue


class BSTree:
    def __init__(self, is_recursive_strategy = True):
        self.__head = None

        if is_recursive_strategy:
            self.__tree_algo = self.__RecursiveTreeAlgorithms()
        else:
            self.__tree_algo = self.__IterativeTreeAlgorithms()

    def empty(self):
        return not self.__head
    
    def insert(self, data):
        if self.empty() :
            self.__head = TreeNode(data)
        else:
            self.__tree_algo.insert(self.__head, data)

    def inorder(self):
        return f"[{self.__tree_algo.inorder(self.__head)[:-1]}]"

    def preorder(self):
        return f"[{self.__tree_algo.preorder(self.__head)[:-1]}]"

    def postorder(self):
        return f"[{self.__tree_algo.postorder(self.__head)[:-1]}]"   

    def level_order(self):
        if self.empty():
            return "[]"

        result = ""
        
        queue = DynamicQueue()
        queue.enqueue(self.__head)

        while not queue.empty():
            node = queue.dequeue()
            result+=f"{node.data}, "

            if node.left:
                queue.enqueue(node.left)
            
            if node.right:
                queue.enqueue(node.right)
        return f"[{result[:-2]}]"
        
    def search(self, data):
        return self.__tree_algo.search(self.__head, data)  


    def delete(self, data):
        self.__head = self.__tree_algo.delete(self.__head, data)    
    
    
            


            
            

    def __str__(self):
        return self.inorder()
    

    
    class TreeAlgorithms:
        def search(self, root, data):
            pass

        def inorder(self, root):
            pass

        def preorder(self, root):
            pass

        def insert(self, root, data) : 
            pass

        def delete(self, root, data): 
            pass
            
    
    class __RecursiveTreeAlgorithms(TreeAlgorithms):
        def search(self, root, data):
            if root is None:
                return False
            elif root.data == data:
                return True
            elif root.data > data:
                return self.search(root.right, data)
            else:
                return self.search(root.left, data)
        
        def inorder(self, root):
            if root is None:
                return ""
            str = f"{self.inorder(root.left)} {root.data}, {self.inorder(root.right)}" 
            return str.strip()    

        def preorder(self, root):
            if root is None:
                return ""
            left_tree = self.preorder(root.left)
            right_tree = self.preorder(root.right)
            str = f"{root.data}, {left_tree} {right_tree}" 
            return str.strip()
    
        def postorder(self, root):
            if root is None:
                return ""
            str = f"{self.postorder(root.left)} {self.postorder(root.right)} {root.data}," 
            return str.strip()

        def insert(self, root, data) : 
            if data < root.data and root.left is None :
                root.left = TreeNode(data, father=root)
            elif data < root.data and root.left is not None :
                self.insert(root.left, data)
            elif root.right is None: 
                root.right = TreeNode(data, father=root)
            else:
                self.insert(root.right, data)


        def delete(self, node, data):
            if node is None :
                raise ValueError(f"Data: {data} not found")

            if data < node.data: 
                node.left = self.delete(node.left, data)
            elif data > node.data:
                node.right = self.delete(node.right, data)
            else: 
                if node.left is None:
                    return node.right   
                if node.right is None:
                    return node.left
                if node.left is None and node.right is None:
                    return None
            
            return node
                       
        def is_right_child(self, node):
            return node.father.right == node

    class __IterativeTreeAlgorithms(TreeAlgorithms):
        def search(self, root, data):
            while root is not None:
                if root.data == data:
                    return True
                elif root.data > data:
                    root = root.right
                else:
                    root = root.left
            return False