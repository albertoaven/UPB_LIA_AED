# ========== DFS ==========
# Complejidad temporal: O(V + E)
# Complejidad espacial: O(V)

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

  visited = set()
  stack = [start]
  parent = {
    start: None
  }

  while stack:
    current = stack.pop()

    if current in visited:
      continue

    visited.add(current)

    # Llegamos al destino
    if current == destination:
      break

    for neighbor in graph.get(current, {}):
      if neighbor not in visited:
        parent[neighbor] = current

        stack.append(neighbor)

  # No existe camino
  if destination not in parent:
    return []

  # Reconstrucción del camino
  path = []

  current = destination

  while current is not None:
    path.append(current)

    current = parent[current]

  path.reverse()

  return path