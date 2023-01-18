# class node:
#     def __init__(self, data=None):
#         self._data = data
#         self._next_node = None
#
#     @property
#     def data(self):
#         return self._data
#
#     def __repr__(self):
#         return self._data
#
#
# class linked_list:
#     def __init__(self):
#         self._head_node = None
#         self._length = 0
#
#     def __len__(self):
#         return self._length
#
#     def __repr__(self):
#
#         if self._head_node is None:
#             return ""
#
#         curr_node = self._head_node
#         values = []
#
#         while True:
#             values.append(str(curr_node.data))
#             if curr_node._next_node is not None:
#                 curr_node = curr_node._next_node
#             else:
#                 break
#
#         return " -> ".join(values)
#
#     def _get_tail_node(self):
#         if self._head_node is None:
#             return None
#
#         curr_node = self._head_node
#
#         while True:
#             if curr_node._next_node is not None:
#                 curr_node = curr_node._next_node
#             else:
#                 return curr_node
#
#     def append(self,data):
#         self._length +=1
#
#         if self._head_node is None:
#             self._head_node = node(data)
#         else:
#             tail_node = self._get_tail_node()
#             tail_node._next_node = node(data)
#
#     def pop(self):
#         if self._head_node is None:
#             return
#
#         curr_node = self._head_node
#         prev_node = None
#
#         while True:
#             if curr_node._next_node is not None:
#                 prev_node = curr_node
#                 curr_node = curr_node._next_node
#             else:
#                 if prev_node is not None:
#                     prev_node._next_node = None
#                     self._length -= 1
#                 break
#
#
# ll = linked_list()
# # ll.append(1)
# ll.append(2)
# ll.append(3)
# print(ll)
# print("Len: {}".format(len(ll)))
#
# ll.pop() # Value 3
# print("Len after removing value '3': {}".format(len(ll)))
#
# ll.append(5)
# print(ll)
# print("Len: {}".format(len(ll)))

# ************************************************************************************************************************
# More optimized implementation of LinkedList
# append O(1) as opposed to O(n)
# len O(1) as opposed to O(n)
# pop O(n)
# ************************************************************************************************************************
class node:
    def __init__(self, data=None):
        self._data = data
        self._next_node = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __repr__(self):
        return str(self._data)


class linked_list:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):

        if self._head_node is None:
            return ""

        curr_node = self._head_node
        values = []

        while True:
            values.append(str(curr_node.data))
            if curr_node._next_node is not None:
                curr_node = curr_node._next_node
            else:
                break

        return " -> ".join(values)

    def __iter__(self):
        curr_node = self._head_node

        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node._next_node

    def _get_tail_node(self):
        if self._head_node is None:
            return None
        else:
            return self._tail_node

    def append(self, data):
        self._length += 1

        if self._head_node is None:
            self._head_node = node(data)
            self._tail_node = self._head_node
        else:
            tail_node = self._get_tail_node()
            tail_node._next_node = node(data)
            self._tail_node = tail_node._next_node

    # remove the last element
    def pop(self):
        if self._head_node is None:
            return

        curr_node = self._head_node

        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node._next_node

            if curr_node._next_node is None:
                self._tail_node = prev_node
                prev_node._next_node = None
                self._length -= 1
                break

    def get(self, index):
        if self._head_node is None:
            return

        if index > self._length or index < 0:
            return

        counter = 0
        curr_node = self._head_node

        while curr_node is not None:
            if counter == index:
                return curr_node.data
            else:
                curr_node = curr_node._next_node
                counter += 1

    def set(self, index, value):
        if self._head_node is None:
            return

        if index > self._length or index < 0:
            return

        counter = 0
        curr_node = self._head_node

        while curr_node is not None:
            if counter == index:
                curr_node.data = value
                break
            else:
                curr_node = curr_node._next_node
                counter += 1

ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)
print("Len: {}".format(len(ll)))

print("Popping last element")
ll.pop()  # Value 3
print("Len after popping: {}".format(len(ll)))

print("Popping last element")
ll.append(5)
print(ll)
print("Len: {}".format(len(ll)))

# Get item by index
print("Node @ 2: {}".format(ll.get(0)))

# Set item by index
print(ll.set(2,10))
print(ll)

for l in ll:
    print("Item:{}".format(l))
