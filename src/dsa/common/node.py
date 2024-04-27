class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next   

class DoubleyNode:
    def __init__(self,data,previous=None,next=None):
        self.data = data
        self.next = next 
        self.previous = previous  

class TreeNode:
    def __init__(self, data, left=None, right=None, father=None):
        self.data = data
        self.left = left
        self.right = right
        self.father = father   

           
    

    
