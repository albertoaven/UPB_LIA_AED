import math

class WeightedGraph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_node(self, u):
        if u not in self.adj:
            self.adj[u] = []

    def add_edge(self, u, v, w):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def nodes(self):
        return list(self.adj.keys())

    def neighbors(self, u):
        return self.adj.get(u, [])

def dijkstra_naive(g, source):
    dist = {v: math.inf for v in g.nodes()}
    dist[source] = 0
    visited = set()

    while len(visited) < len(g.nodes()):
        # Selección lineal del no visitado con menor distancia
        u = None
        best = math.inf
        for v in g.nodes():
            if v not in visited and dist[v] < best:
                best = dist[v]
                u = v

        if u is None:  # nodos restantes inalcanzables
            break

        visited.add(u)

        # Relajación
        for v, w in g.neighbors(u):
            if v in visited:
                continue
            cand = dist[u] + w
            if cand < dist[v]:
                dist[v] = cand

    return dist

# Pruebas simples
g = WeightedGraph(directed=False)
g.add_edge("A", "B", 3)
g.add_edge("A", "C", 1)
g.add_edge("C", "B", 1)
g.add_edge("B", "D", 2)
g.add_edge("C", "D", 5)

dist = dijkstra_naive(g, "A")
print("Distancias desde A (naive):", dist)

assert dist["A"] == 0
assert dist["C"] == 1
assert dist["B"] == 2  # A->C->B = 1+1
assert dist["D"] == 4  # A->C->B->D = 1+1+2
