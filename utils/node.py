class Node:
    def __init__(self, value: int, left, right, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def addLeft(self, node_target, node_source):
        node_target.left = node_source

    def addRight(self, node_target, node_source):
        node_target.right = node_source

