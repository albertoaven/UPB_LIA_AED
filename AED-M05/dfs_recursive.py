# Ejemplo 2: DFS recursiva (lista de adyacencia) con conjunto de visitados y orden de visita

def dfs_recursive(adj, start):
    visited = set()
    order = []

    def visit(u):
        visited.add(u)
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visit(v)

    visit(start)
    return order, visited

if __name__ == "__main__":
    # Grafo dirigido con orden de vecinos controlado
    adj = {
        0: [1, 2],
        1: [3],
        2: [3, 4],
        3: [5],
        4: [],
        5: []
    }

    order, reached = dfs_recursive(adj, 0)
    print("Orden DFS recursiva:", order)
    print("Alcanzables:", reached)

    # Pruebas simples (deterministas por el orden de listas)
    assert reached == {0, 1, 2, 3, 4, 5}
    assert order == [0, 1, 3, 5, 2, 4]
