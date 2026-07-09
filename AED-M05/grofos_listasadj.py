class UndirectedGraphAdjList:
  def __init__(self):
    self.adj = {}

  def add_vertex(self, u):
    if u not in self.adj:
      self.adj[u] = []

  def add_edge(self, u, v):
    self.add_vertex(u)
    self.add_vertex(v)

    if v not in self.adj[u]:
      self.adj[u].append(v)

    if u not in self.adj[v]:
      self.adj[v].append(u)

  def remove_edge(self, u, v):
    if u in self.adj and v in self.adj[u]:
      self.adj[u].remove(v)

    if v in self.adj and u in self.adj[v]:
      self.adj[v].remove(u)

  def neighbors(self, u):
    return list(self.adj.get(u, []))

if __name__ == "__main__":
  g = UndirectedGraphAdjList()

  g.add_vertex("A")
  g.add_edge("A", "B")
  g.add_edge("A", "C")
  g.add_edge("A", "B")

  print("Vecinos de A: ", g.neighbors("A"))
  assert sorted(g.neighbors("A")) == ["B", "C"]
  assert "A" in g.neighbors("B")

  g.remove_edge("A", "B")

  print("Tras eliminar A-B, vecinos de A: ", g.neighbors("A"))
  assert "B" not in g.neighbors("A")
  assert "A" not in g.neighbors("B")