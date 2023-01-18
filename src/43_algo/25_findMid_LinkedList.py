import math


def findMid(self, head):
    if head is None:
        return

    if head.next is None:
        return head.data

    curr_node = head
    nodes = []

    while curr_node is not None:
        nodes.append(curr_node.data)
        curr_node = curr_node.next

    # Even # elements
    if len(nodes) % 2 == 0:
        mid = int((len(nodes) / 2) + 1)
    else:
        mid = math.ceil(len(nodes) / 2)

    return nodes[mid - 1]


"""
# Here the fast node will reach ead first as its iterating twice the amount of nodes over slow
# Hence by the time fast reaches the end if the list, slow will be in the middle, whose results can be returned straight away
class Solution{
    public:
    /* Should return data of middle node. If linked list is empty, then  -1*/
    int getMiddle(Node *head)
    {
        // Your code here
        Node *slow=head;
        Node *fast=head;
        while(fast !=NULL && fast->next !=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow->data;
    }
};
"""
