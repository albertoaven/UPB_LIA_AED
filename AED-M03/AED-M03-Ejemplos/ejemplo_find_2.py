def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        parent[root_y] = root_x

# Inicialización
parent = [i for i in range(6)]

# Construcción del bosque
union(parent, 1, 2)
union(parent, 0, 1)
union(parent, 3, 4)

print(parent)  # [0, 0, 1, 3, 3, 5]

# Pruebas
print(find(parent, 2))  # 0
print(find(parent, 4))  # 3
print(find(parent, 5))  # 5