import array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.root_node = None
        self._length = 0

    def _increment_counter(self):
        self._length += 1

    def _decrement_counter(self):
        self._length -= 1

    def push(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            new_node = Node(data)
            curr_node = self.root_node

            while curr_node is not None:
                # This means we had reached the end node in linked list
                if curr_node.next is None:
                    curr_node.next = new_node
                    self._increment_counter()
                    break

                curr_node = curr_node.next

    def pop(self):
        if self.is_empty():
            return None

        prev_node = None
        curr_node = self.root_node

        while curr_node is not None:

            # Logic to check for curr_node is root_node
            if curr_node.next is None and self.root_node == curr_node:
                self.root_node = None
                break

            elif curr_node.next is None:
                prev_node.next = None
                break

            prev_node = curr_node
            curr_node = curr_node.next

        self._decrement_counter()
        return curr_node

    def is_empty(self):
        return self.root_node is None

    def search(self, data):
        curr_node = self.root_node
        found = False

        while curr_node is not None:
            if curr_node.data == data:
                found = True
                break

            curr_node = curr_node.next
        return found

    def search(self, data):
        curr_node = self.root_node
        found = False

        while curr_node is not None:
            if curr_node.data == data:
                found = True
                break

            curr_node = curr_node.next
        return found

    def sort(self):
        curr_node = self.root_node
        prev_node = None
        counter = self._length
        sort_counter = 0

        while True:
            print("iter")
            if prev_node is not None and curr_node.data > prev_node.data:
                prev_node.data, curr_node.data = curr_node.data, prev_node.data

            prev_node = curr_node
            curr_node = curr_node.next
            sort_counter += 1

            if sort_counter >= counter:
                curr_node = self.root_node
                prev_node = None
                counter -=1
                sort_counter = 0

            if counter <=1:
                break



    def clear(self):
        self.root_node = None


stk = stack()
stk.push(2)
stk.push(5)
stk.push(3)
stk.push(4)
stk.push(1)
print("3 exits in stack: {}".format(stk.search(-3)))
stk.sort()
# stk.clear()

print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop().data)
print(stk.pop())