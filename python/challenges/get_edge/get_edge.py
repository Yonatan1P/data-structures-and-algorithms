def get_edges(graph, cities):
    cost = 0
    potential_cities = []
    potential_cities += [cities[0]]
    for node in graph._adjacency_list:
        if node.value in cities:
            for edge in graph._adjacency_list[node]:
                if edge.vertex.value in cities:
                    if edge.vertex.value not in potential_cities:
                        print(edge.vertex.value)
                        print('cost', edge.weight)
                        cost += edge.weight
                        potential_cities += [edge.vertex.value]
    print('potential cities', potential_cities)
    for city in cities:
        if city not in potential_cities:
            return False, '$0'
    return True, f'${cost}'

    # for city in cities:
    #     if city not in potential_cities:
    #         return False
    #     else:
    #         for flights in potential_flights:
    #             if flight.end.value

