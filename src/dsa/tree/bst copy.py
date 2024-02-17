from dsa.common.node import TreeNode
from dsa.queue.dynamic_queue import DynamicQueue
from dsa.queue.static_queue import FixedSizeQueue


class BSTree:
    def __init__(self):
        self.__head = None

    def empty(self):
        return not self.__head
    
    def insert(self, data):
        if self.empty() :
            self.__head = TreeNode(data)
        else:
            self.__insert(self.__head, data)

    def inorder(self):
        return f"[{self.__inorder(self.__head)[:-1]}]"

    def preorder(self):
        return f"[{self.__preorder(self.__head)[:-1]}]"

    def postorder(self):
        return f"[{self.__postorder(self.__head)[:-1]}]"   

    def level_order(self):
        if self.empty():
            return ""

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
        return self.__search(self.__head, data)
    
    def __search(self, root, data):
        if root is None:
            return False
        elif root.data == data:
            return True
        elif root.data > data:
            return self.__search(root.right, data)
        else:
            return self.__search(root.left, data)
        
    # def __search(self, root, data):
    #     while root is not None:
    #         if root.data == data:
    #             return True
    #         elif root.data > data:
    #             root = root.right
    #         else:
    #             root = root.left
    #     return False        

                

    def __inorder(self, root):
        if root is None:
            return ""
        str = f"{self.__inorder(root.left)} {root.data}, {self.__inorder(root.right)}" 
        return str.strip()
    
    # def __inorder(self, root):
    #     result = ""
    #     temp = root

    #     while temp:
    #         if temp.left is None:
    #             result += f"{temp.data}, "
    #             temp = temp.right
    #         else:
    #             father= temp.left
                
    #             while father.right is not None and father.right != temp:
    #                 father= father.right

            
    #             if father.right is None:
    #                 father.right = temp
    #                 temp = temp.left
    #             else:
                
    #                 father.right = None
    #                 result += f"{temp.data}, "
    #                 temp = temp.right

    #     return result.rstrip(", ")


    def __preorder(self, root):
        if root is None:
            return ""
        left_tree = self.__preorder(root.left)
        right_tree = self.__preorder(root.right)
        str = f"{root.data}, {left_tree} {right_tree}" 
        return str.strip()
    
    def __postorder(self, root):
        if root is None:
            return ""
        str = f"{self.__postorder(root.left)} {self.__postorder(root.right)} {root.data}," 
        return str.strip()


    def __insert(self, root, data) : 
        if data < root.data and root.left is None :
            root.left = TreeNode(data, father=root)
        elif data < root.data and root.left is not None :
            self.__insert(root.left, data)
        elif root.right is None: 
            root.right = TreeNode(data, father=root)
        else:
            self.__insert(root.right, data)
                


    def __str__(self):
        return self.inorder()    
    

        


        

