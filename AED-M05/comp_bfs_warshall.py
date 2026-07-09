# Ejemplo 7: Comparación aplicada - BFS por consulta vs Warshall (conteo de operaciones)

from collections import deque

def bfs_reachable_count_ops(adj, src, dst):
    # Devuelve (alcanzable, ops) donde ops cuenta inspecciones de vecinos
    q = deque([src])
    visited = {src}
    ops = 0

    while q:
        u = q.popleft()
        if u == dst:
            return True, ops
        for v in adj.get(u, []):
            ops += 1
            if v not in visited:
                visited.add(v)
                q.append(v)
    return False, ops

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
        R[i][i] = True
        for v in adj.get(u, []):
            R[i][idx[v]] = True
    return R, idx

def warshall_with_ops(R):
    n = len(R)
    reach = [row[:] for row in R]
    ops = 0  # cuenta evaluaciones básicas
    for k in range(n):
        for i in range(n):
            for j in range(n):
                ops += 1
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return reach, ops

if __name__ == "__main__":
    # Grafo dirigido moderado (n=8) y disperso
    adj = {
        0: [1, 2],
        1: [3],
        2: [3, 4],
        3: [5],
        4: [5, 6],
        5: [7],
        6: [7],
        7: []
    }

    queries = [(0, 7), (2, 7), (1, 6), (6, 0), (4, 7), (0, 6), (2, 5), (7, 0)]
    # Simular "muchas consultas" repitiendo el conjunto
    Q_small = queries
    Q_large = queries * 50  # 400 consultas

    # Estrategia 1: BFS por consulta
    def total_bfs_ops(Q):
        total = 0
        answers = []
        for (u, v) in Q:
            ok, ops = bfs_reachable_count_ops(adj, u, v)
            total += ops
            answers.append(ok)
        return total, answers

    bfs_ops_small, ans_small = total_bfs_ops(Q_small)
    bfs_ops_large, ans_large = total_bfs_ops(Q_large)

    # Estrategia 2: Warshall una vez + consultas O(1)
    nodes = nodes_sorted(adj)
    R0, idx = adjacency_to_bool_matrix(adj, nodes)
    reach, warshall_ops = warshall_with_ops(R0)

    def answer_with_warshall(Q):
        # costo de consulta ~ O(1); se cuenta 1 op por consulta para evidenciar escala
        ops = 0
        answers = []
        for (u, v) in Q:
            ops += 1
            answers.append(reach[idx[u]][idx[v]])
        return ops, answers

    w_ops_small, w_ans_small = answer_with_warshall(Q_small)
    w_ops_large, w_ans_large = answer_with_warshall(Q_large)

    print("BFS por consulta - ops (Q pequeño):", bfs_ops_small)
    print("BFS por consulta - ops (Q grande):", bfs_ops_large)
    print("Warshall preproc - ops:", warshall_ops)
    print("Warshall consultas - ops (Q pequeño):", w_ops_small)
    print("Warshall consultas - ops (Q grande):", w_ops_large)

    # Pruebas simples: ambas estrategias deben coincidir en respuestas
    assert ans_small == w_ans_small
    # Para el caso repetido, todas las respuestas deben coincidir en patrón
    assert ans_large == w_ans_large
