class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        current_position = self.head
        all_values = ""
        while current_position:
            all_values += "{ "
            all_values += f"{current_position.value}"
            all_values += " } -> "
            current_position = current_position.next_node
        return all_values+"NULL"

    def append(self, value):
        current_position = self.head
        while current_position.next_node:
            current_position = current_position.next_node
        current_position.next_node = Node(value)

def zip_lists(first_list, second_list):
    absolute_head = first_list.head
    current_1 = first_list.head
    current_2 = second_list.head

    while current_1 and current_2:
        temp_1 = current_1.next_node
        temp_2 = current_2.next_node

        current_1.next_node = current_2
        current_2.next_node = temp_1

        current_1 = current_2.next_node
        current_2 = temp_2

    while current_1:
        first_list.append(current_1.value)
        current_1 = current_1.next_node

    while current_2:
        first_list.append(current_2.value)
        current_2 = current_2.next_node

    current_1 = absolute_head
    return first_list.__str__()
