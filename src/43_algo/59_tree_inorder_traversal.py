class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            print("data already present" + str(data))


class MyTree:
    def __init__(self):
        self._root_node = None

    @property
    def root_node(self):
        return self._root_node

    def insert(self, data):
        if self._root_node is None:
            self._root_node = Node(data)
        else:
            self.root_node.insert(data)

    def inorder_traverse(self, root, lst=[]):
        if root is None:
            return

        self.inorder_traverse(root.left, lst)
        lst.insert(0, root.data)
        self.inorder_traverse(root.right, lst)


t = MyTree()
t.insert("g")
t.insert("c")
t.insert("b")
t.insert("a")
t.insert("e")
t.insert("d")
t.insert("f")
t.insert("i")
t.insert("h")
t.insert("j")
t.insert("k")

lst = []
t.inorder_traverse(t.root_node, lst)
print(' '.join(lst))


