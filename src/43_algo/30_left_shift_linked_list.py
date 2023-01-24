# def rotate(self, head, k):
#     if head == None or k <= 0:
#         return head
#
#     curr_node = head
#     nodes_to_shit = []
#     counter = 0
#     new_head = None
#
#     while curr_node is not None:
#         if counter < k:
#             nodes_to_shit.append(curr_node)
#
#         if counter == k:
#             new_head = curr_node
#
#         if curr_node.next is None:
#             # Remove the last node in the shifted section to None, which will be new tail node
#             nodes_to_shit[-1].next = None
#
#             # Set the current tail node reference to the start of shifted nodes
#             curr_node.next = nodes_to_shit[0]
#             break
#
#         curr_node = curr_node.next
#         counter += 1
#
#     return new_head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def populateNode(data):
    head = None
    prev = None
    data = data.split()
    for idx, itm in enumerate(data):
        n = Node(itm)
        if head is None:
            head = n

        if prev:
            prev.next = n

        prev = n
    return head


def rotate(head, k):
    if head is None or k <= 0:
        return head

    curr_node = head
    nodes_to_shift = []
    counter = 0
    new_head = None

    while curr_node is not None:
        if counter < k:
            nodes_to_shift.append(curr_node)

        if counter == k:
            new_head = curr_node

        # if the nodes to reverse is same as length of linkedlist, then return as is
        if counter == (k-1) and curr_node.next is None:
            return head

        if curr_node.next is None:
            # Remove the last node in the shifted section to None, which will be new tail node
            nodes_to_shift[-1].next = None

            # Set the current tail node reference to the start of shifted nodes
            curr_node.next = nodes_to_shift[0]
            break

        curr_node = curr_node.next
        counter += 1

    return new_head


data = populateNode("1 2 3 4")
result = rotate(data, 4)

while result is not None:
    print(result.data)
    result = result.next
