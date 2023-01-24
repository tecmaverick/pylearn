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

    def post_order_traverse(self, root, lst=[]):
        if root is None:
            return

        self.post_order_traverse(root.left, lst)
        self.post_order_traverse(root.right, lst)
        lst.append(root.data)




# ***********************************
# t = MyTree()
# f = Node("F")
# b = Node("B")
# a = Node("A")
# d = Node("D")
# c = Node("C")
# e = Node("E")
# g = Node("G")
# i = Node("I")
# h = Node("H")
# k = Node("K")
# j = Node("J")
#
# g.left_node = c
# g.right_node = i
# c.left_node = b
# c.right_node = e
# b.left_node = a
# e.left_node = d
# e.right_node = f
# i.left_node = h
# i.right_node = j
# j.right_node = k

# lst = []
# t.root = g
# t.post_order_traverse(t.root, lst)
# print(' '.join([str(x) for x in lst]))

# ***********************************

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
t.post_order_traverse(t.root, lst)
print(' '.join([str(x) for x in lst]))

# ***********************************
# t = MyTree()
# f = Node("F")
# b = Node("B")
# a = Node("A")
# d = Node("D")
# c = Node("C")
# e = Node("E")
# g = Node("G")
# i = Node("I")
# h = Node("H")
#
# f.right_node = g
# f.left_node = b
# b.left_node = a
# b.right_node = d
# d.left_node = c
# d.right_node = e
# g.right_node = i
# i.left_node = h
#
#
# lst = []
# t.root = g
# t.post_order_traverse(t.root, lst)
# print(' '.join([str(x) for x in lst]))
