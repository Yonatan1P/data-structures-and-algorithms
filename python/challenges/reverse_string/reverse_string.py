def reverse_string_array(string):
  output = ''
  letters = []
  for char in string:
    letters += [char]

  for i in range(len(letters)):
    reverse_index = len(letters) - (i + 1)
    output += f'{letters[reverse_index]}'
  return output

print(reverse_string_array('hello'))

class Node:

  def __init__(self, value, next=None):

    self.value = value
    self.next = next

class Stack:

  def __init__(self, top=None):
    self.top = top

  def add(self,value):
    node = Node(value, self.top)
    self.top = node

  def pop(self):
    popped = self.top.value
    self.top = self.top.next
    return popped

def reverse_string_stack(string):

  output = ''
  letters = Stack()
  for char in string:
    letters.add(char)

  while letters.top:
    output += letters.pop()
  return output

print(reverse_string_stack('hi, how are you doing today?'))

def reverse_string_recursive(string):

  if len(string) == 0:
    return string
  else:
    return reverse_string_recursive(string[1:]) + string[0]

print(reverse_string_recursive('hey, how it do?'))
