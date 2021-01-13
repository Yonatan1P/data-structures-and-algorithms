from challenges.get_edge.get_edge import get_edges
from challenges.graph.graph import Graph

def test_happy_path():
    graph = Graph()

    n1 = graph.add_node('Pandora')
    n2 = graph.add_node('Metroville')
    n3 = graph.add_node('Arendelle')
    n4 = graph.add_node('Monstropolis')
    n5 = graph.add_node('Naboo')
    n6 = graph.add_node('Narnia')

    graph.add_edge(n1,n2,82)
    graph.add_edge(n1,n3,150)
    graph.add_edge(n2,n3,99)
    graph.add_edge(n2,n4,105)
    graph.add_edge(n2,n5,26)
    graph.add_edge(n2,n6,37)
    graph.add_edge(n3,n4,42)
    graph.add_edge(n4,n5,73)
    graph.add_edge(n5,n6,250)

    graph.add_edge(n2,n1,82)
    graph.add_edge(n3,n1,150)
    graph.add_edge(n3,n2,99)
    graph.add_edge(n4,n2,105)
    graph.add_edge(n5,n2,26)
    graph.add_edge(n6,n2,37)
    graph.add_edge(n4,n3,42)
    graph.add_edge(n5,n4,73)
    graph.add_edge(n6,n5,250)

    actual = get_edges(graph, ["Metroville", "Pandora"])
    expected = True, "$82"
    assert actual == expected

def test_3_destinations():
    graph = Graph()

    n1 = graph.add_node('Pandora')
    n2 = graph.add_node('Metroville')
    n3 = graph.add_node('Arendelle')
    n4 = graph.add_node('Monstropolis')
    n5 = graph.add_node('Naboo')
    n6 = graph.add_node('Narnia')

    graph.add_edge(n1,n2,82)
    graph.add_edge(n1,n3,150)
    graph.add_edge(n2,n3,99)
    graph.add_edge(n2,n4,105)
    graph.add_edge(n2,n5,26)
    graph.add_edge(n2,n6,37)
    graph.add_edge(n3,n4,42)
    graph.add_edge(n4,n5,73)
    graph.add_edge(n5,n6,250)

    graph.add_edge(n2,n1,82)
    graph.add_edge(n3,n1,150)
    graph.add_edge(n3,n2,99)
    graph.add_edge(n4,n2,105)
    graph.add_edge(n5,n2,26)
    graph.add_edge(n6,n2,37)
    graph.add_edge(n4,n3,42)
    graph.add_edge(n5,n4,73)
    graph.add_edge(n6,n5,250)

    actual = get_edges(graph, ['Arendelle', 'Monstropolis', 'Naboo'])
    expected = True, '$115'
    assert actual == expected

def test_falsy():
    graph = Graph()

    n1 = graph.add_node('Pandora')
    n2 = graph.add_node('Metroville')
    n3 = graph.add_node('Arendelle')
    n4 = graph.add_node('Monstropolis')
    n5 = graph.add_node('Naboo')
    n6 = graph.add_node('Narnia')

    graph.add_edge(n1,n2,82)
    graph.add_edge(n1,n3,150)
    graph.add_edge(n2,n3,99)
    graph.add_edge(n2,n4,105)
    graph.add_edge(n2,n5,26)
    graph.add_edge(n2,n6,37)
    graph.add_edge(n3,n4,42)
    graph.add_edge(n4,n5,73)
    graph.add_edge(n5,n6,250)

    graph.add_edge(n2,n1,82)
    graph.add_edge(n3,n1,150)
    graph.add_edge(n3,n2,99)
    graph.add_edge(n4,n2,105)
    graph.add_edge(n5,n2,26)
    graph.add_edge(n6,n2,37)
    graph.add_edge(n4,n3,42)
    graph.add_edge(n5,n4,73)
    graph.add_edge(n6,n5,250)

    actual = get_edges(graph, ['Pandora', 'Naboo'])
    expected = False, '$0'
    assert actual == expected

def test_3_falsy():
    graph = Graph()

    n1 = graph.add_node('Pandora')
    n2 = graph.add_node('Metroville')
    n3 = graph.add_node('Arendelle')
    n4 = graph.add_node('Monstropolis')
    n5 = graph.add_node('Naboo')
    n6 = graph.add_node('Narnia')

    graph.add_edge(n1,n2,82)
    graph.add_edge(n1,n3,150)
    graph.add_edge(n2,n3,99)
    graph.add_edge(n2,n4,105)
    graph.add_edge(n2,n5,26)
    graph.add_edge(n2,n6,37)
    graph.add_edge(n3,n4,42)
    graph.add_edge(n4,n5,73)
    graph.add_edge(n5,n6,250)

    graph.add_edge(n2,n1,82)
    graph.add_edge(n3,n1,150)
    graph.add_edge(n3,n2,99)
    graph.add_edge(n4,n2,105)
    graph.add_edge(n5,n2,26)
    graph.add_edge(n6,n2,37)
    graph.add_edge(n4,n3,42)
    graph.add_edge(n5,n4,73)
    graph.add_edge(n6,n5,250)

    actual = get_edges(graph, ['Narnia', 'Arendelle', 'Naboo'])
    expected = False, '$0'
    assert actual == expected
