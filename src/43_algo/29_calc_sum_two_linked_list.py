class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def create_ll(self, data):
        head = None
        prev = None
        data = [x for x in str(data)]

        for itm in data:
            n = Node(itm)
            if head is None:
                head = n

            if prev:
                prev.next = n

            prev = n

        return head

    def getSumLinkList(self, head):

        if head is None:
            return

        curr_node = head
        result = ""

        while (curr_node is not None):
            result += str(curr_node.data)
            curr_node = curr_node.next

        return result

    # Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        if first and second:
            f = self.getSumLinkList(first)
            s = self.getSumLinkList(second)
            sum = int(f) + int(s)
            return self.create_ll(sum)
        else:
            return