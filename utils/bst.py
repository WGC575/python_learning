from typing import List
import node
from utils.node import Node

class BST:
    def __init__(self, root):
        self.root = None
    
    def iniTree(self, list: List[int]):
        if len(list) != 0:
            for v in list:
                self.push(v)
        else:
            print("Empty list.")


    def search(self, value)->int:
        return 
    
    def push(self, value: int):
        if self.root == None:
            self.root = Node(value, None)
        else:
            self.root