from challenges.stacks_and_queues.stacks_and_queues import Stack

def depth_first(adjacency_list, root):

    temp = Stack()
    temp.push(root)
    output = []

    while temp.top:

        current = temp.pop()
        print(current)
        if current not in output:
            output += [current]
        for edge in adjacency_list[current]:
            if edge.vertex not in output:
                temp.push(edge.vertex)
    return [vertex.value for vertex in output]
