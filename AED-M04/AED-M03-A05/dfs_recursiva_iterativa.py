calls = 0

def dfs_recursive(tree, index=0, visited=None):
  global calls

  if visited is None:
    visited = []

  if index >= len(tree):
    return visited, calls

  calls += 1

  visited.append(tree[index])

  dfs_recursive(tree, 2 * index + 1, visited)
  dfs_recursive(tree, 2 * index + 2, visited)

  return visited, calls

def dfs_iterative(tree):
  global calls

  if not tree:
    return []

  visited = []
  stack = [0]

  while stack:
    calls += 1

    index = stack.pop()

    if index >= len(tree):
      continue

    visited.append(tree[index])

    right = 2 * index + 2
    left = 2 * index + 1

    if right < len(tree):
      stack.append(right)

    if left < len(tree):
      stack.append(left)

  return visited

def dfs(graph, node):
  print(node)

  for child in graph[node]:
    dfs(graph, child)

def dfs_memoizacion(graph, node, visited=None):
  if visited is None:
    visited = set()

  if node in visited:
    return

  visited.add(node)

  print(node)

  for child in graph[node]:
    dfs(graph, child, visited)

if __name__ == "__main__":
  calls = 0

  tree = [4, 2, 6, 1, 3, 5, 7, 8, 9]

  print("DFS recursive: ", dfs_recursive(tree))
  print("Llamadas:", calls)

  calls = 0

  print("DFS iterative: ", dfs_iterative(tree))
  print("Llamadas:", calls)  

  graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
  }

  dfs(graph, "C")
  dfs(graph, "C", None)