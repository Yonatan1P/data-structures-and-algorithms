class Node:

  def __init__(self,value, next=None):
    self.value = value
    self.next = next
    self.read = 0

class Queue:

  def __init__(self, front=None, rear=None):
    self.front = front
    self.rear = rear

  def enqueue(self, value):
    node = Node(value)
    if not self.front:
      self.front = node
      self.rear = self.front
    else:
      self.rear.next = node
      self.rear = node

  def dequeue(self):
    if not self.front:
      return
    else:
      temp = self.front.value
      self.front = self.front.next
      return temp


class Edge:

  def __init__(self,end, weight=0):

    self.end = end
    self.weight = weight

class Graph:

  def __init__(self):
    self._adjacency_list = {}

  def add_vertex(self,value):
    vertex = Node(value)
    self._adjacency_list[vertex] = []
    return vertex

  def add_edge(self, start, end, weight=0):

    if not start in self._adjacency_list:
      raise Exception('start vertex not in graph')

    if not end in self._adjacency_list:
      raise Exception('end vertex not in graph')

    edge = Edge(end, weight)
    self._adjacency_list[start].append(edge)

  def breadth_first_traversal(self,start):
    output = ""
    queue = Queue()
    start.read = 1
    queue.enqueue(start)
    while queue.front:
      current = queue.dequeue()
      output += f"{current.value}"
      for edge in self._adjacency_list[current]:
        if not edge.end.read:
          edge.end.read = 1
          queue.enqueue(edge.end)
    return output
