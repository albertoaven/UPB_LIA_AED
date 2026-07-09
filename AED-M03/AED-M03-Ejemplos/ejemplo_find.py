def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x

# Bosque manual: 2 -> 1 -> 0 y 4 -> 3; 5 es singleton
parent = [0, 0, 1, 3, 3, 5]

print(find(parent, 2))  # representante de {0,1,2}
print(find(parent, 4))  # representante de {3,4}
print(find(parent, 5))  # singleton

assert find(parent, 2) == 0
assert find(parent, 4) == 3
assert find(parent, 5) == 5
print("OK")