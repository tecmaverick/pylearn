class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        if head is None:
            return

        if head.next is None:
            return head

        current = head
        prev_node = None

        while (current is not None):
            next = current.next
            current.next = prev_node

            prev_node = current
            current = next

        return prev_node
