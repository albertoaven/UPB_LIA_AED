# Representación de grafo dirigido con lista de adyacencia (dict: nodo -> list[vecinos]).
# Incluye nodos sin salidas e incluso nodos aislados.

from typing import Dict, List, Set, Iterable, Tuple, Any

Graph = Dict[Any, List[Any]]

def add_node(g: Graph, u: Any) -> None:
    """Asegura que el nodo exista en el diccionario, aunque no tenga salidas."""
    if u not in g:
        g[u] = []

def add_edge(g: Graph, u: Any, v: Any) -> None:
    """Agrega arista dirigida u->v y asegura la presencia de ambos nodos."""
    add_node(g, u)
    add_node(g, v)
    g[u].append(v)

def nodes(g: Graph) -> Set[Any]:
    """Devuelve el conjunto total de nodos, incluyendo los que aparecen solo como destino."""
    s = set(g.keys())
    for u, nbrs in g.items():
        for v in nbrs:
            s.add(v)
    return s

def edges(g: Graph) -> List[Tuple[Any, Any]]:
    """Lista de aristas dirigidas (u, v)."""
    out = []
    for u, nbrs in g.items():
        for v in nbrs:
            out.append((u, v))
    return out

# Pruebas simples
if __name__ == "__main__":
    g: Graph = {}

    # Dependencias: A -> B, A -> C, B -> D
    add_edge(g, "A", "B")
    add_edge(g, "A", "C")
    add_edge(g, "B", "D")

    # Nodo sin salidas (explícito): E existe pero no depende de nadie ni tiene dependientes
    add_node(g, "E")

    print("Adyacencias:", g)
    print("Nodos:", sorted(nodes(g)))
    print("Aristas:", edges(g))

    assert "E" in nodes(g)
    assert ("A", "B") in edges(g)
    assert g["D"] == []  # D aparece como destino; se asegura su presencia con lista vacía
