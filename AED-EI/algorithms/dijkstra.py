# ========== Dijkstra ==========
# Complejidad temporal: O((V + E) log V)
# Complejidad espacial: O(V)

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

import heapq


def find_path_dijkstra(graph,  start,  destination):
  """
  Encuentra el camino mínimo entre
  start y destination utilizando Dijkstra.

  Args:
    graph: Grafo representado mediante lista
      de adyacencia.
    start: Nodo origen.
    destination: Nodo destino.

  Returns:
    tuple:
      (
        distancia_total,
        camino
      )

      Si no existe camino:

      (
        float("inf"),
        []
      )
  """

  distances = {
    node: float("inf")
    for node in graph
  }

  distances[start] = 0

  previous = {}

  priority_queue = [
    (0, start)
  ]

  while priority_queue:
    current_distance, current = \
      heapq.heappop(
        priority_queue
      )

    if current == destination:
      break

    for neighbor, data in \
      graph.get(current, {}).items():

      new_distance = (
        current_distance
        + data["distance"]
      )

      if (
        new_distance
        < distances.get(
            neighbor,
            float("inf")
          )
      ):

        distances[neighbor] = \
          new_distance

        previous[neighbor] = \
          current

        heapq.heappush(
          priority_queue,
          (
            new_distance,
            neighbor
          )
        )

  # No existe camino

  if (
    destination != start
    and destination not in previous
  ):
    return (
      float("inf"),
      []
    )

  # Reconstrucción del camino

  path = []

  current = destination

  while current != start:

    path.append(current)

    current = previous[current]

  path.append(start)

  path.reverse()

  return (
    distances[destination],
    path
  )