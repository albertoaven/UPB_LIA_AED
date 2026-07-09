# Ejemplo 3: DFS iterativa con pila (comparación con DFS recursiva)

def dfs_recursive(adj, start):
    visited = set()
    order = []

    def visit(u):
        visited.add(u)
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visit(v)

    visit(start)
    return order, visited

def dfs_iterative(adj, start):
    visited = set()
    order = []
    stack = [start]

    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)

        # Para aproximar el mismo comportamiento que la recursión,
        # se apilan vecinos en orden inverso (LIFO).
        for v in reversed(adj.get(u, [])):
            if v not in visited:
                stack.append(v)

    return order, visited

def dfs_recursive_reach(adj, start):
    visited = set()
    def visit(u):
        visited.add(u)
        for v in adj.get(u, []):
            if v not in visited:
                visit(v)
    visit(start)
    return visited

if __name__ == "__main__":
  adj = {
    0: [1, 2],
    1: [3],
    2: [4, 5],
    3: [6],
    4: [7],
    5: [],
    6: [8, 9],
    7: [],
    8: [10],
    9: [11],
    10: [12, 13],
    11: [],
    12: [14],
    13: [15],
    14: [],
    15: [16, 17],
    16: [],
    17: [18],
    18: [19, 20],
    19: [],
    20: [21],
    21: [22],
    22: [23],
    23: [24, 25],
    24: [],
    25: [26],
    26: [27],
    27: [28],
    28: [],
    29: [30],
    30: [31],
    31: [],
    32: [33],
    33: [34],
    34: [],
    35: [36],
    36: [37],
    37: [],
    38: [39],
    39: [],
    40: [41],
    41: [],
    42: [43],
    43: [],
    44: [45],
    45: [],
    46: [47],
    47: [],
    48: [49],
    49: []
  }

  order_it, reached_it = dfs_iterative(adj, 0)
  order_rec, reached_it_1 = dfs_recursive(adj, 0)
  reached_rec = dfs_recursive_reach(adj, 0)

  print("Orden DFS iterativa:", order_it)
  print("Orden DFS recursiva:", order_rec)
  print("Alcanzables (iterativa):", reached_it)
  print("Alcanzables (recursiva):", reached_rec)

  # Pruebas simples: misma alcanzabilidad, orden no necesariamente idéntico
  assert reached_it == reached_rec
  #assert reached_it == {0, 1, 2, 3, 4, 5}