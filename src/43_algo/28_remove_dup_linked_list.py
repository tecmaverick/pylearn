# Function to remove duplicates from sorted linked list.


# ************************************************************************
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def removeDuplicates1(head):
    if head is None:
        return

    if head.next is None:
        return head

    curr_node = head
    prev_node = None

    dict = {}

    while curr_node is not None:
        if curr_node.data in dict:
            # while curr_node is not None and curr_node.data in dict:
            curr_node = curr_node.next

            prev_node.next = curr_node
        else:
            dict[curr_node.data] = curr_node.data

            prev_node = curr_node
            curr_node = curr_node.next

    return head


def removeDuplicates0(head):
    node = head

    while node and node.next:

        if node.data == node.next.data:

            node.next = node.next.next

        else:

            node = node.next

    return head


data = "2 2 3 7 10 13 18 18 20 20 27 28 30 32 33 35 40 40 40 40 41 42 45 53 54 57 57 61 66 66 68 68 69 71 40 40 77 79 81 82 84 87 87 87 90 93 95 96 98 98 98"
# data = "2 2 2 2"


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


# n1 = Node(2)
# n2 = Node(2);n1.next = n2
# n3 = Node(2);n2.next = n3
# n4 = Node(5);n3.next = n4

n = populateNode(data)
# res = removeDuplicates0(n)
res = removeDuplicates1(n)
while res is not None:
    print(res.data)
    res = res.next
