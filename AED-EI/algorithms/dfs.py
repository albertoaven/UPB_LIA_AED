# ========== DFS ==========
# Complejidad temporal: O(V + E)
# Complejidad espacial: O(V)

import time

def recursive_dfs(graph, start):
  visited = set()
  order = []

  def visit(node):
    visited.add(node)
    order.append(node)

    for neighbor in graph.get(node, []):
      if neighbor not in visited:
        visit(neighbor)

  visit(start)

  return order

def iterative_dfs(graph, start):
  visited = set()
  stack = [start]
  order = []

  while stack:
    current = stack.pop()

    if current in visited:
      continue

    visited.add(current)
    order.append(current)

    neighbors = graph.get(current, [])

    for neighbor in reversed(neighbors):
      if neighbor not in visited:
        stack.append(neighbor)

  return order

def recursive_dfs(graph, start):
  visited = set()

  order = []

  def visit(node):
    visited.add(node)

    order.append(node)

    for neighbor in graph.get(node, {}):
      if neighbor not in visited:
        visit(neighbor)

  visit(start)

  return order

def find_dfs(graph, start, destination):
  """
  Busca un camino entre start y destination
  utilizando DFS.

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
  stack = [start]
  parent = {
    start: None
  }

  while stack:
    operations += 1

    current = stack.pop()

    if current in visited:
      continue

    visited.add(current)

    # Llegamos al destino
    if current == destination:
      break

    for neighbor in graph.get(current, {}):
      operations += 1

      if neighbor not in visited:
        parent[neighbor] = current

        stack.append(neighbor)

  # No existe camino
  if destination not in parent:
    execution_time = (time.perf_counter() - start_time)

    return [], operations, execution_time

  # Reconstrucción del camino
  path = []

  current = destination

  while current is not None:
    operations += 1

    path.append(current)

    current = parent[current]

  path.reverse()

  execution_time = (time.perf_counter() - start_time)

  return path, operations, execution_time