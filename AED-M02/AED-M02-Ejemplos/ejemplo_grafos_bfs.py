from collections import deque

grafo = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"],
}

def bfs(grafo, inicio):
  visitados = set()
  cola = deque([inicio])
  visitados.add(inicio)

  orden = []

  while cola:
    actual = cola.popleft()
    orden.append(actual)

    for vecino in grafo.get(actual, []):
      if vecino not in visitados:
        visitados.add(vecino)
        cola.append(vecino)

  return orden

def bfs_distancias(grafo, inicio):
  dist = { inicio: 0 }
  cola = deque([inicio])

  while cola:
    actual = cola.popleft()

    for vecino in grafo.get(actual, []):
      if vecino not in dist:
        dist[vecino] = dist[actual] + 1
        cola.append(vecino)

  return dist

def dfs_recursivo(grafo, inicio):
  visitados = set()
  orden = []

  def visitar(nodo):
    visitados.add(nodo)
    orden.append(nodo)

    for vecino in grafo.get(nodo, []):
      if vecino not in visitados:
        visitar(vecino)

  visitar(inicio)

  return orden

def dfs_iterativo(grafo, inicio):
  visitados = set()
  pila = [inicio]
  orden = []

  while pila:
    actual = pila.pop()

    if actual in visitados:
      continue

    visitados.add(actual)
    orden.append(actual)

    vecinos = grafo.get(actual, [])

    # Se hace el reversed para que se mantenga el orden establecido.
    # Sin reversed se procesaría A -> D -> C -> B
    # Con el reversed se procesa A -> B -> C -> D
    # Recordar que se trabaja con una PILA (LIFO)

    for v in reversed(vecinos): 
      if v not in visitados:
        pila.append(v)

  return orden

print("BFS desde A:", bfs(grafo, "A"))
print("Distancias desde A:", bfs_distancias(grafo, "A"))
print("DFS recursivo desde A:", dfs_recursivo(grafo, "A"))
print("DFS iterativo desde A:", dfs_iterativo(grafo, "A"))