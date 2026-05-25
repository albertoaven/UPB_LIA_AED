from collections import deque

def bfs(graph, start, key):
  visited = set()
  queue = deque([start])
  visited.add(start)

  order = []

  while queue:
    current = queue.popleft()
    order.append(current)

    for neighbor in graph.get(current, []):
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

  return order