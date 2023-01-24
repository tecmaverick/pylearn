class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    @property
    def right_node(self):
        return self.right

    @right_node.setter
    def right_node(self, node):
        self.right = node

    @property
    def left_node(self):
        return self.left

    @left_node.setter
    def left_node(self, node):
        self.left = node

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
    def root(self):
        return self._root_node

    @root.setter
    def root(self, node):
        self._root_node = node

    def insert(self, data):
        if self._root_node is None:
            self._root_node = Node(data)
        else:
            self._root_node.insert(data)

    def search(self, root, search_val):
        if root is None:
            return

        if search_val == root.data:
            return root
        elif search_val > root.data:
            return self.search(root.right, search_val)
        elif search_val < root.data:
            return self.search(root.left, search_val)



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
result = t.search(t.root, "k")
print(result)
