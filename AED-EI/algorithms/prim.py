# ========== PRIM ==========
# Complejidad temporal: O(E log V)
# Complejidad espacial: O(V + E)

import heapq
import time

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
  start_time = time.perf_counter()
  evaluated_edges = 0
  selected_edges = 0

  visited = set()

  mst = []

  priority_queue = []

  visited.add(start)

  # Cargamos las aristas del nodo inicial

  for neighbor, data in graph[start].items():
    evaluated_edges += 1

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

    selected_edges += 1

    # Agregar nuevas aristas candidatas

    for neighbor, data in \
      graph.get(destination, {}).items():
      evaluated_edges += 1

      if neighbor not in visited:
        heapq.heappush(
          priority_queue,
          (
            data["distance"],
            destination,
            neighbor
          )
        )

  execution_time = time.perf_counter() - start_time

  return mst, evaluated_edges, selected_edges, execution_time