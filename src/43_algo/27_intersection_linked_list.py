def intersetPoint(head1, head2):
    if head1 is None or head2 is None:
        return -1

    if head1.next == head2:
        return head2.data

    if head2.next == head1:
        return head1.data

    curr_node1 = head1
    curr_node2 = head2

    dict = {}

    while (curr_node1 is not None or curr_node2 is not None):

        if curr_node1 is not None:
            curr_node1 = curr_node1.next

            if curr_node1 not in dict:
                dict[curr_node1] = 1
            else:
                return curr_node1.data

        if curr_node2 is not None:
            curr_node2 = curr_node2.next

            if curr_node2 not in dict:
                dict[curr_node2] = 1
            else:
                return curr_node2.data

    return -1