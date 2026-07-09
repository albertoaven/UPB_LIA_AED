# Ejemplo 4: BFS con deque y distancias mínimas (grafo no ponderado)

from collections import deque

def bfs_distances(adj, start):
    dist = {start: 0}
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj.get(u, []):
            if v not in dist:  # equivale a "no visitado"
                dist[v] = dist[u] + 1
                q.append(v)

    return dist

if __name__ == "__main__":
    # Grafo no ponderado (dirigido para ejemplificar; la propiedad de capas se mantiene)
    adj = {
        "s": ["a", "b"],
        "a": ["c"],
        "b": ["c", "d"],
        "c": ["e"],
        "d": ["e"],
        "e": []
    }

    dist = bfs_distances(adj, "s")
    print("Distancias desde s:", dist)

    # Pruebas simples: distancias mínimas en cantidad de aristas
    assert dist["s"] == 0
    assert dist["a"] == 1 and dist["b"] == 1
    assert dist["c"] == 2
    assert dist["d"] == 2
    assert dist["e"] == 3
