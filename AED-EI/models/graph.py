import networkx as nx
import matplotlib.pyplot as plt

def create_graph(routes):
  grafo = {}

  for route_id, origen_id, destination_id, distance, time in routes:
    if origen_id not in grafo:
      grafo[origen_id] = {}

    grafo[origen_id][destination_id] = {
      "distance": distance,
      "time": time
    }

  return grafo

def draw_graph(graph):

  G = nx.DiGraph()

  for origin, neighbors in graph.items():

    for destination, data in neighbors.items():

      G.add_edge(
        origin,
        destination,
        weight=data["distance"]
      )

  plt.figure(figsize=(10, 8))

  pos = nx.spring_layout(
    G,
    seed=42
  )

  nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    arrows=True
  )

  labels = nx.get_edge_attributes(
    G,
    "weight"
  )

  nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
  )

  plt.title("Red de Ciudades")
  plt.show()