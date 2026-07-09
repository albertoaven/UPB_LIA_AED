# Ejemplo 1 (parámetros del grafo): |V|, |E| y densidad aproximada

def graph_basic_stats(vertices, edges, directed=False):
    """
    vertices: iterable de vértices
    edges: iterable de pares (u, v)
    directed: True si el grafo es dirigido
    """
    V = set(vertices)
    E = list(edges)

    n = len(V)
    m = len(E)

    # Densidad aproximada:
    # - Dirigido: máximo n*(n-1) sin bucles
    # - No dirigido: máximo n*(n-1)/2 sin multiaristas ni bucles
    if n <= 1:
        density = 0.0
    else:
        if directed:
            max_edges = n * (n - 1)
        else:
            max_edges = n * (n - 1) / 2
        density = m / max_edges if max_edges else 0.0

    return n, m, density

# Pruebas simples
verts = ["A", "B", "C", "D", "E", "F"]
edges_undirected = [("A", "B"), ("A", "C"), ("C", "D"), ("C", "E"), ("C", "F")]
n, m, d = graph_basic_stats(verts, edges_undirected, directed=False)

print("No dirigido:", n, m, round(d, 3))
assert n == 4 and m == 3
assert 0.0 < d < 1.0

edges_directed = [("A", "B"), ("B", "A"), ("A", "C")]
n2, m2, d2 = graph_basic_stats(verts, edges_directed, directed=True)
print("Dirigido:", n2, m2, round(d2, 3))
assert n2 == 4 and m2 == 3