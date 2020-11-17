class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current_position = self.head
        while current_position:
            if current_position.value == value:
                return True
            current_position = current_position.next_node
        return False

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

    def insert_before(self, existing_value, insert_value):
        current_position = self.head
        if not current_position:
            return
        if current_position.value == existing_value:
            insert_node = Node(insert_value)
            insert_node.next_node = current_position
            self.head = insert_node
            return
        while current_position.next_node:
            if current_position.next_node.value == existing_value:
                break
            current_position = current_position.next_node
        if current_position.next_node.value == existing_value:
            insert_node = Node(insert_value)
            insert_node.next_node = current_position.next_node
            current_position.next_node = insert_node

    def insert_after(self, existing_value, insert_value):
        current_position = self.head
        if not current_position:
            return
        if current_position.value == existing_value:
            insert_node = Node(insert_value, current_position.next_node)
            current_position.next_node = insert_node
            return
        while current_position.next_node:
            if current_position.value == existing_value:
                break
            current_position = current_position.next_node
        if current_position.value == existing_value:
            insert_node = Node(insert_value, current_position.next_node)
            current_position.next_node = insert_node

    def count_from_end(self, reverse_index):
        current_position = self.head
        list_length = 0

        while current_position:
            list_length += 1
            current_position = current_position.next_node

        if reverse_index >= list_length or reverse_index < 0:
            return "Exception"

        current_position = self.head
        reverse_index +=1
        for i in range(0, list_length - reverse_index):
            current_position = current_position.next_node
            i += 1
        print(current_position.value)

        return current_position.value
