class WeigtedDigraphAdjMap:
  def __init__(self):
    self.adj = {}

  def add_vertex(self, u):
    if u not in self.adj:
      self.adj[u] = {}

  def add_edge(self, u, v, w):
    self.add_vertex(u)
    self.add_vertex(v)
    self.adj[u][v] = w

  def weight(self, u, v):
    return self.adj.get(u, {}).get(v, None)
  
  def neighbors(self, u):
    return list(self.adj.get(u, {}).keys())