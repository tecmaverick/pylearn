'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    # Function to remove a loop in the linked list.

    def removeLoop(self, head):
        if head is None or head.next is None:
            return 0

        curr_node = head
        data_key = {}
        duplicate_found = 0

        while curr_node.next is not None:
            curr_node_id = id(curr_node)
            if curr_node_id not in data_key:
                data_key[curr_node_id] = 0
            else:
                # link found
                data_key[curr_node_id] += 1
                prev_node.next = None
                duplicate_found = 1
                break

            prev_node = curr_node
            curr_node = curr_node.next

        return duplicate_found


    def detectLoop(self, head):
        if head is None or head.next is None:
            return False

        curr_node = head
        data_key = {}
        duplicate_found = False

        while curr_node.next is not None:
            curr_node_id = id(curr_node)
            if curr_node_id not in data_key:
                data_key[curr_node_id] = 0
            else:
                # link found
                data_key[curr_node_id] += 1
                duplicate_found = True
                break

            prev_node = curr_node
            curr_node = curr_node.next

        return duplicate_found

