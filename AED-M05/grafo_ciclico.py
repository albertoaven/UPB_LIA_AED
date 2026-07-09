from typing import Dict, List, Any, Set

Graph = Dict[Any, List[Any]]

def all_nodes(g: Graph) -> Set[Any]:
    s = set(g.keys())
    for u in g:
        for v in g[u]:
            s.add(v)
    return s

def has_cycle_dfs(g: Graph) -> bool:
    """
    Detecta ciclo dirigido usando DFS con estados:
    0 = no visitado, 1 = en proceso, 2 = finalizado.
    """
    state = {u: 0 for u in all_nodes(g)}

    def dfs(u: Any) -> bool:
        state[u] = 1  # en proceso
        for v in g.get(u, []):
            if state[v] == 1:
                return True  # back edge => ciclo
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2  # finalizado
        return False

    for u in list(state.keys()):
        if state[u] == 0:
            if dfs(u):
                return True
    return False

# Pruebas simples
if __name__ == "__main__":
    # Caso acíclico: A->B, A->C, B->D
    dag: Graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    assert has_cycle_dfs(dag) is False
    print("DAG: ciclo =", has_cycle_dfs(dag))

    # Caso cíclico: A->B, B->C, C->A
    cyc: Graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert has_cycle_dfs(cyc) is True
    print("Cíclico: ciclo =", has_cycle_dfs(cyc))
