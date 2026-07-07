# ========== PRIM ==========
# Complejidad temporal: O(E log V)
# Complejidad espacial: O(V + E)

import heapq

def prim(graph, start):
  """
  Algoritmo de Prim.

  Construye un Árbol de Expansión Mínima (MST)
  partiendo desde un vértice inicial.

  Args:
    graph: Lista de adyacencia.
    start: Nodo inicial.

  Returns:
    list: Lista de aristas seleccionadas.
  """

  visited = set()

  mst = []

  priority_queue = []

  visited.add(start)

  # Cargamos las aristas del nodo inicial

  for neighbor, data in graph[start].items():
    heapq.heappush(
      priority_queue,
      (
        data["distance"],
        start,
        neighbor
      )
    )

  while priority_queue:
    weight, origin, destination = \
      heapq.heappop(priority_queue)

    # Evita ciclos

    if destination in visited:
      continue

    visited.add(destination)

    mst.append(
      (
        origin,
        destination,
        weight
      )
    )

    # Agregar nuevas aristas candidatas

    for neighbor, data in \
      graph.get(destination, {}).items():

      if neighbor not in visited:
        heapq.heappush(
          priority_queue,
          (
            data["distance"],
            destination,
            neighbor
          )
        )

  return mst