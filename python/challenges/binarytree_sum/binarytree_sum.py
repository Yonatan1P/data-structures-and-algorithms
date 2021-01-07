from challenges.stacks_and_queues.stacks_and_queues import Queue

def totalUsage(binarytree):
    if type(binarytree.root.value) == int:
	    output = 0
    elif type(binarytree.root.value) == str:
        output = ''

    if not binarytree.root:
        return output
    root = binarytree.root

    temp_queue = Queue()
    temp_queue.enqueue(root)

    while temp_queue.front:
        current_node = temp_queue.dequeue()
        output += current_node.value
        if current_node.left:
            temp_queue.enqueue(current_node.left)
        if current_node.right:
            temp_queue.enqueue(current_node.right)
    return output
