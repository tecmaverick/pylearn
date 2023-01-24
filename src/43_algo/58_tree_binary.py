class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data > data:
            if self.right is None: self.right = Node(data)
            else: self.right.insert(data)
        elif self.data < data:
            if self.left is None: self.left = Node(data)
            else: self.left.insert(data)
        else:
            print("data already present" + str(data))


class MyBinaryTree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data)


t = MyBinaryTree()
t.insert(10)
t.insert(5)
t.insert(11)
t.insert(12)
t.insert(6)
a = 1
