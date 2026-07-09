# Ejemplo 6: Clausura transitiva con Warshall (matriz booleana) + conversión desde lista

def nodes_sorted(adj):
    nodes = set(adj.keys())
    for u in adj:
        for v in adj[u]:
            nodes.add(v)
    return sorted(nodes)

def adjacency_to_bool_matrix(adj, nodes):
    idx = {v: i for i, v in enumerate(nodes)}
    n = len(nodes)
    R = [[False] * n for _ in range(n)]
    for u in nodes:
        i = idx[u]
        # opcional: alcanzabilidad reflexiva (camino vacío)
        R[i][i] = True
        for v in adj.get(u, []):
            R[i][idx[v]] = True
    return R, idx

def warshall_transitive_closure(R):
    n = len(R)
    # Copia defensiva
    reach = [row[:] for row in R]
    for k in range(n):
        for i in range(n):
            if reach[i][k]:  # micro-optimización booleana
                for j in range(n):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach

def reachable(reach, idx, u, v):
    return reach[idx[u]][idx[v]]

if __name__ == "__main__":
    # Grafo dirigido
    adj = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": [],
        "E": ["A"]  # E alcanza A,B,C,D
    }

    nodes = nodes_sorted(adj)
    R0, idx = adjacency_to_bool_matrix(adj, nodes)
    reach = warshall_transitive_closure(R0)

    print("Nodos:", nodes)
    print("Alcanzabilidad A->D:", reachable(reach, idx, "A", "D"))
    print("Alcanzabilidad D->A:", reachable(reach, idx, "D", "A"))
    print("Alcanzabilidad E->D:", reachable(reach, idx, "E", "D"))
    print("Alcanzabilidad D->E:", reachable(reach, idx, "D", "E"))

    # Pruebas simples
    assert reachable(reach, idx, "A", "D") is True
    assert reachable(reach, idx, "D", "A") is False
    assert reachable(reach, idx, "E", "D") is True
    assert reachable(reach, idx, "A", "A") is True  # reflexiva por construcción
