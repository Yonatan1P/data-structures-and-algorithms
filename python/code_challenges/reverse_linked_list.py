def reverseLinkedList(linkedlist):
    current = linkedlist.head
    old_previous = "Null"
    while current:
        print('old current:', current.value)
        old_next = current.next_node
        print('old next:', old_next.value)
        current.next_node = old_previous
        old_previous = current
        print('old previous:', old_previous.value)
        current = old_next
        print('new current:', current.value)
    linkedlist.head = current
    return linkedlist.head.value
