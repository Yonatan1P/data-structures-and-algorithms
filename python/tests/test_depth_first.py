from challenges.depth_first.depth_first import depth_first
from challenges.graph.graph import Graph

def test_3_nodes():

    graph = Graph()
    n1 = graph.add_node('A')
    n2 = graph.add_node('B')
    n3 = graph.add_node('C')
    graph.add_edge(n1,n2)
    graph.add_edge(n1,n3)
    actual = depth_first(graph._adjacency_list, n1)
    expected = ['A','C', 'B']
    assert actual == expected

def test_cirlular_routes():

    graph = Graph()
    n1 = graph.add_node('A')
    n2 = graph.add_node('B')
    n3 = graph.add_node('C')
    graph.add_edge(n1,n2)
    graph.add_edge(n2,n3)
    graph.add_edge(n3,n1)
    actual = depth_first(graph._adjacency_list, n1)
    expected = ['A','B','C']
    assert actual == expected

def test_cirlular_routes():

    graph = Graph()
    n1 = graph.add_node('A')
    n2 = graph.add_node('B')
    n3 = graph.add_node('C')
    graph.add_edge(n1,n2)
    graph.add_edge(n2,n3)
    graph.add_edge(n3,n1)
    actual = depth_first(graph._adjacency_list, n1)
    expected = ['A','B','C']
    assert actual == expected
