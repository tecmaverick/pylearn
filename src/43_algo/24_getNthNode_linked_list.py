def getNthFromLast(head, n):
    if n <= 0 or head is None or (head.next is None and n > 1):
        return -1

    if head.next is None and n == 1:
        return head.data

    curr_node = head
    data = []

    while curr_node is not None:
        data.append(curr_node.data)
        curr_node = curr_node.next

    if n <= len(data):
        return data[-n]
    else:
        return -1