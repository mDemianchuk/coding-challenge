from listnode import ListNode


def print_list(linked_list):
    while linked_list:
        print(linked_list.val, end=" ")
        linked_list = linked_list.next


def merge(linked_lists):
    merged = []

    # We can collect all nodes in O(n) time, where n is the number of elements
    for node in linked_lists:
        while node:
            merged.append(node.val)
            node = node.next

    # Sorts in O(n log n) time, which results in O(n + n log n), or just O(n log n) time complexity
    sorted_list = sorted(merged)
    # if the return type should be array
    # just return sorted_list

    # if the return type should be Node
    # we need to collect all elements again but this time into a linked list of type Node
    # this step adds O(n) time, but the resulting complexity still remains O (n log n)
    sorted_linked_list = ListNode()
    # so we still can have access to the first node
    head = sorted_linked_list

    for value in sorted_list:
        # Node (value) points to tail, which is None
        sorted_linked_list.next = ListNode(value)
        sorted_linked_list = sorted_linked_list.next

    # return the first node
    return head.next


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(6)

linked_list1 = ListNode(0)
linked_list1.next = node1
node1.next = node2
node2.next = node3

linked_list_2 = ListNode(1)
linked_list_2.next = node2
node2.next = node3
node3.next = node4

linked_list_3 = ListNode(-2)
linked_list_3.next = node3
node2.next = node4

result = merge([linked_list1, linked_list_2, linked_list_3])
print_list(result)
