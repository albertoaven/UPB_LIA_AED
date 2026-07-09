def find_shortest_path(tree, target):
  path = []

  def backtrack(index):
    # Si el índice está fuera del árbol, no hay camino.
    if index >= len(tree):
      return False

    # Se agrega el nodo actual al camino.
    path.append(tree[index])

    # Si encontramos el objetivo, terminamos.
    if tree[index] == target:
      return True

    left = 2 * index + 1
    right = 2 * index + 2

    # Buscar primero en el subárbol izquierdo y luego en el derecho.
    if backtrack(left) or backtrack(right):
      return True

    # Backtracking:
    # El objetivo no está en esta rama, por lo que
    # eliminamos el nodo antes de volver.
    path.pop()
    return False

  if backtrack(0):
    return path

  return None

if __name__ == "__main__":
  node = [4, 2, 6, 1, 3, 5, 7, 8, 9]

  print(find_shortest_path(node, 5))