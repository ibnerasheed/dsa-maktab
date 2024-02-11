from dsa.common.node import TreeNode


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

    def level_order(self, root):
        if root is None:
            return ""
        

        

    def __inorder(self, root):
        if root is None:
            return ""
        str = f"{self.__inorder(root.left)} {root.data}, {self.__inorder(root.right)}" 
        return str.strip()
    
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
        if data < root.data :
            if root.left is None :
                root.left = TreeNode(data, father=root)
            else :
                self.__insert(root.left, data)
        elif data >= root.data : 
            if root.right is None :
                root.right = TreeNode(data, father=root)
            else :
                self.__insert(root.right, data)
                


    def __str__(self):
        return self.inorder()    
    

        


        

