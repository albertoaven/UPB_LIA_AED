import heapq

def dijkstra(graph, start):
    distances = {n: float('inf') for n in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        dist, actual = heapq.heappop(pq)

        for vecino, datos in graph[actual].items():
            nueva = dist + datos["distance"]

            if nueva < distances[vecino]:
                distances[vecino] = nueva
                heapq.heappush(pq, (nueva, vecino))

    return distances