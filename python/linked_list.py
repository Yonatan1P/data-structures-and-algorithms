class Node:

    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node

class LinkedList():

    def __init__(self):
        self.head=None

    def insert(self,value):
        self.head=Node(value,self.head)

    def includes(self,value):
        current_position=self.head
        while current_position:
            if current_position.value==value:
                return True
            current_position=current_position.next_node
        return False

    def __str__(self):
        current_position=self.head
        all_values=""
        while current_position:
            all_values+="{ " + "{value}".format(value=current_position.value) + " } -> "
            current_position=current_position.next_node
        return all_values+"NULL"

    def append(self,value):
        current_position=self.head
        while current_position.next_node:
            current_position=current_position.next_node
        current_position.next_node=Node(value)
