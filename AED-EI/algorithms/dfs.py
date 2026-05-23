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