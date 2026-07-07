# ========== BFS ==========
# Complejidad temporal: O(V + E)
# Complejidad espacial: O(V)

from collections import deque


def bfs(graph, start):
  visited = set()
  queue = deque([start])
  order = []

  visited.add(start)

  while queue:
    current = queue.popleft()

    order.append(current)

    for neighbor in graph.get(current, {}):
      if neighbor not in visited:
        visited.add(neighbor)

        queue.append(neighbor)

  return order

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

  visited = set()

  queue = deque([start])

  # Guarda de dónde viene cada nodo
  parent = {
    start: None
  }

  visited.add(start)

  while queue:
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
    return []

  # Reconstruir camino
  path = []

  current = destination

  while current is not None:
    path.append(current)

    current = parent[current]

  path.reverse()

  return path