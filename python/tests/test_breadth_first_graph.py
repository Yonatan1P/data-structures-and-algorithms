from challenges.breadth_first_graph.breadth_first_graph import Graph, Node
def test_breadth_first_graph_happy():
    graph = Graph()
    vertex1 = graph.add_vertex("Hi")
    vertex2 = graph.add_vertex("my")
    vertex3 = graph.add_vertex("name")
    vertex4 = graph.add_vertex("is")
    vertex5 = graph.add_vertex("Yoni")
    vertex6 = graph.add_vertex("!")
    graph.add_edge(vertex1,vertex2)
    graph.add_edge(vertex1,vertex3)
    graph.add_edge(vertex2,vertex3)
    graph.add_edge(vertex3,vertex4)
    graph.add_edge(vertex4,vertex3)
    graph.add_edge(vertex4,vertex5)
    graph.add_edge(vertex5,vertex6)
    actual = graph.breadth_first_traversal(vertex1)
    expected = "HimynameisYoni!"
    assert actual == expected

def test_breadth_first_graph_with_loop():
    graph = Graph()
    vertex1 = graph.add_vertex("Hi")
    vertex2 = graph.add_vertex("my")
    vertex3 = graph.add_vertex("name")
    vertex4 = graph.add_vertex("is")
    vertex5 = graph.add_vertex("Yoni")
    vertex6 = graph.add_vertex("!")
    graph.add_edge(vertex1,vertex2)
    graph.add_edge(vertex1,vertex3)
    graph.add_edge(vertex2,vertex3)
    graph.add_edge(vertex3,vertex4)
    graph.add_edge(vertex4,vertex3)
    graph.add_edge(vertex4,vertex5)
    graph.add_edge(vertex5,vertex6)
    graph.add_edge(vertex6,vertex1)
    actual = graph.breadth_first_traversal(vertex1)
    expected = "HimynameisYoni!"
    assert actual == expected

def test_breadth_first_graph_no_edges():
    graph = Graph()
    vertex1 = graph.add_vertex("Hi")
    vertex2 = graph.add_vertex("my")
    vertex3 = graph.add_vertex("name")
    vertex4 = graph.add_vertex("is")
    vertex5 = graph.add_vertex("Yoni")
    vertex6 = graph.add_vertex("!")
    actual = graph.breadth_first_traversal(vertex1)
    expected = "Hi"
    assert actual == expected


