import pytest
from challenges.graph.graph import Graph, Vertex, Edge

def test_add_nodes():
    graph = Graph()
    node = graph.add_node(5)
    actual = node.value
    expected = 5
    assert actual == expected

def test_add_node_returns_vertex():

    graph = Graph()

    vertex = graph.add_node("spam")

    assert isinstance(vertex, Vertex)


def test_add_node_return_has_correct_value():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected

def test_add_edge_sunny():

    graph = Graph()

    start = graph.add_node("start")

    end = graph.add_node("end")

    graph.add_edge(start, end)

    # no fail means a pass

    # can be more explicit if you like

    # try:
    #   graph.add_edge(start, end)
    # except KeyError:
    #   pytest.fail("KeyError should not be thrown")

def test_add_edge_with_weight():

    graph = Graph()

    start = graph.add_node("start")

    end = graph.add_node("end")

    weight = 10

    graph.add_edge(start, end, weight)


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():

    graph = Graph()

    graph.add_node("banana")

    graph.add_node("apple")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected

def test_get_neighbors_none():

    graph = Graph()

    banana = graph.add_node("banana")

    neighbors = graph.get_neighbors(banana)

    assert len(neighbors) == 0

def test_get_neighbors_returns_edges():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor = neighbors[0]

    assert isinstance(neighbor, Edge)

    assert neighbor.vertex.value == 'banana'


def test_get_neighbors_returns_edges_with_default_weight():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana)

    neighbors = graph.get_neighbors(apple)

    actual = neighbors[0].weight

    expected = 0

    assert actual == expected


def test_get_neighbors_returns_edges_with_custom_weight():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    neighbor_edge = neighbors[0]

    assert neighbor_edge.weight == 44


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size_one():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_size_two():

    graph = Graph()

    graph.add_node("spam")

    graph.add_node("bacon")

    expected = 2

    actual = graph.size()

    assert actual == expected
