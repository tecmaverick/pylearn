import array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class stack:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self._length = 0

    def _increment_counter(self):
        self._length += 1

    def _decrement_counter(self):
        self._length -= 1

    def push(self, data):
        if self.head_node is None:
            self.head_node = Node(data)
            self.tail_node = self.head_node
        else:
            new_node = Node(data)
            prev_node = self.tail_node
            prev_node.next = new_node

            self.tail_node = new_node
            new_node.prev = prev_node

        self._increment_counter()

    def peek(self):
        return self.tail_node

    def pop(self):
        if self.is_empty():
            return None

        if self.tail_node == self.head_node:
            curr_node = self.head_node
            self.head_node = None
        else:
            curr_node = self.tail_node
            self.tail_node = self.tail_node.prev
            self.tail_node.next = None

        self._decrement_counter()
        return curr_node

    def is_empty(self):
        return self.head_node is None

    def search(self, data):
        curr_node = self.head_node
        found = False

        while curr_node is not None:
            if curr_node.data == data:
                found = True
                break

            curr_node = curr_node.next
        return found

    def search(self, data):
        curr_node = self.head_node
        found = False

        while curr_node is not None:
            if curr_node.data == data:
                found = True
                break

            curr_node = curr_node.next
        return found

    def sort(self):
        cmp_node = self.head_node
        next_node = None

        stack_length = self._length - 1

        for i in range(stack_length, -1, -1):
            for j in range(i):
                print("iter")
                if next_node is None:
                    next_node = cmp_node.next
                else:
                    next_node = next_node.next

                if next_node is not None and cmp_node.data > next_node.data:
                    cmp_node.data, next_node.data  = next_node.data, cmp_node.data

            cmp_node = cmp_node.next
            next_node = None

    def clear(self):
        self.head_node = None


stk = stack()
stk.push(2)
stk.push(5)
stk.push(3)
stk.push(4)
stk.push(1)
print("3 exits in stack: {}".format(stk.search(-3)))
print(stk.peek().data)
stk.sort()
# stk.clear()

print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop())
