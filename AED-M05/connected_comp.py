# Ejemplo 5: Componentes conexas en grafo no dirigido (DFS iterativa)

def connected_components_undirected(adj):
    visited = set()
    components = []

    for start in adj.keys():
        if start in visited:
            continue

        comp = set()
        stack = [start]
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            comp.add(u)
            for v in adj.get(u, []):
                if v not in visited:
                    stack.append(v)

        components.append(comp)

    return components

if __name__ == "__main__":
    # Grafo no dirigido: se listan vecinos en ambos sentidos
    adj = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3],
        5: []  # nodo aislado
    }

    comps = connected_components_undirected(adj)
    print("Componentes:", comps)

    # Normalizar tamaños para prueba
    sizes = sorted(len(c) for c in comps)
    print("Tamaños:", sizes)

    # Pruebas simples: {0,1,2}, {3,4}, {5}
    assert sizes == [1, 2, 3]
    assert any(c == {0, 1, 2} for c in comps)
    assert any(c == {3, 4} for c in comps)
    assert any(c == {5} for c in comps)
