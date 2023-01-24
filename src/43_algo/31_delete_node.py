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




def deleteNode(curr_node):
    curr_node.data = curr_node.next.data
    curr_node.next = curr_node.next.next



data = populateNode("1 2 3 4")
deleteNode(data.next)

while data is not None:
    print(data.data)
    data = data.next