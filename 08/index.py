import heapq


# Алгоритм Дейкстры
def dijkstra_algoritm(graph, start):

    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Алгоритм Беллмана-Форда
def bellman_ford_algoritm(graph, start):
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v, graph[u][v]))

    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u, v, weight in edges:
            if (
                distances[u] != float("infinity")
                and distances[u] + weight < distances[v]
            ):
                distances[v] = distances[u] + weight

    for u, v, weight in edges:
        if distances[u] != float("infinity") and distances[u] + weight < distances[v]:
            raise ValueError("Граф содержит цикл отрицательного веса")

    return distances


# Алгоритм Джонсона
def johnson_algoritm(graph):
    new_graph = graph.copy()
    new_graph["S"] = {vertex: 0 for vertex in graph}

    try:
        h = bellman_ford_algoritm(new_graph, "S")
    except ValueError as e:
        return str(e)

    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v in graph[u]:
            reweighted_graph[u][v] = graph[u][v] + h[u] - h[v]

    distances = {}
    for u in graph:
        distances[u] = dijkstra_algoritm(reweighted_graph, u)

    for u in distances:
        for v in distances[u]:
            distances[u][v] = distances[u][v] + h[v] - h[u]

    return distances
