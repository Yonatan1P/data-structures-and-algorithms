class Vertex:

    def __init__(self, value):
        self.value = value

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self,value):

        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex

    def add_edge(self, start, end, weight=0):

        if start not in self._adjacency_list:
            raise KeyError("Start vertex not in Graph")

        if end not in self._adjacency_list:
            raise KeyError("End vertex not in Graph")

        edge = Edge(end, weight)
        self._adjacency_list[start].append(edge)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def size(self):
        return len(self._adjacency_list)

    def get_neighbors(self,vertex):
        return self._adjacency_list[vertex]
