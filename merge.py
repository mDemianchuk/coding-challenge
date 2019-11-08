from node import Node


def print_list(linked_list):
    while linked_list:
        print(linked_list.value, end=" ")
        linked_list = linked_list.next_node


def merge(linked_lists):
    merged = []

    # We can collect all nodes in O(n) time, where n is the number of elements
    for node in linked_lists:
        while node:
            merged.append(node.value)
            node = node.next_node

    # Sorts in O(n log n) time, which results in O(n + n log n), or just O(n log n) time complexity
    sorted_list = sorted(merged)
    # if the return type should be array
    # just return sorted_list

    # if the return type should be Node
    # we need to collect all elements again but this time into a linked list of type Node
    # this step adds O(n) time, but the resulting complexity still remains O (n log n)
    sorted_linked_list = Node()
    # so we still can have access to the first node
    head = sorted_linked_list

    for value in sorted_list:
        # Node (value) points to tail, which is None
        sorted_linked_list.next_node = Node(value)
        sorted_linked_list = sorted_linked_list.next_node

    # return the first node
    return head.next_node


node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
node4 = Node(6)

linked_list1 = Node(0)
linked_list1.next_node = node1
node1.next_node = node2
node2.next_node = node3

linked_list_2 = Node(1)
linked_list_2.next_node = node2
node2.next_node = node3
node3.next_node = node4

linked_list_3 = Node(-2)
linked_list_3.next_node = node3
node2.next_node = node4

result = merge([linked_list1, linked_list_2, linked_list_3])
print_list(result)
