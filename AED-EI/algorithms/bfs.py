# ========== BFS ==========
# Complejidad temporal: O(V + E)
# Complejidad espacial: O(V)

import time

from collections import deque


def bfs(graph, start):
  start_time = time.perf_counter()
  operations = 0

  visited = set()
  queue = deque([start])
  order = []

  visited.add(start)

  while queue:
    operations += 1

    current = queue.popleft()

    order.append(current)

    for neighbor in graph.get(current, {}):
      if neighbor not in visited:
        visited.add(neighbor)

        queue.append(neighbor)

  execution_time = (time.perf_counter() - start_time)

  return order, operations, execution_time

def find_bfs(graph, start, destination):
  """
  Busca el camino más corto en cantidad de saltos
  entre start y destination utilizando BFS.

  Args:
    graph: Grafo representado como lista de adyacencia.
    start: Nodo origen.
    destination: Nodo destino.

  Returns:
    list: Camino encontrado o lista vacía.
  """
  start_time = time.perf_counter()
  operations = 0

  visited = set()

  queue = deque([start])

  # Guarda de dónde viene cada nodo
  parent = {
    start: None
  }

  visited.add(start)

  while queue:
    operations += 1

    current = queue.popleft()

    # Llegamos al destino
    if current == destination:
      break

    for neighbor in graph.get(current, {}):
      if neighbor not in visited:
        visited.add(neighbor)

        parent[neighbor] = current

        queue.append(neighbor)

  # No existe camino
  if destination not in parent:
    execution_time = (time.perf_counter() - start_time)

    return [], operations, execution_time

  # Reconstruir camino
  path = []

  current = destination

  while current is not None:
    operations += 1

    path.append(current)

    current = parent[current]

  path.reverse()

  execution_time = (time.perf_counter() - start_time)

  return path, operations, execution_time