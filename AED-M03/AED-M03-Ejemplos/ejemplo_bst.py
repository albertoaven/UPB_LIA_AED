class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

def insert(root, key):
  if root is None:
    return Node(key)
  elif key < root.key:
    root.left = insert(root.left, key)
  elif key > root.key:
    root.right = insert(root.right, key)
  
  return root

def search(root, key, comparisons):
  if root is None:
    return False 

  if root.key == key:
    return True

  comparisons += 1

  if root.key > key:  
    return search(root.left, key, comparisons), comparisons
  else:
    return search(root.right, key, comparisons), comparisons

def minimum(node):
  current = node

  while current.left is not None:
    current = current.left

  return current

def deleteNode(root, key):
  if root is None:
    return root
  
  if key < root.key:
    root.left = deleteNode(root.left, key)
  elif key > root.key:
    root.rigth = deleteNode(root.right, key)
  else:
    if root.left is None:
      return root.right
    
    if root.right is None:
      return root.left
    
    sucessor = minimum(root.right)
    root.key = sucessor.key
    root.right = deleteNode(root.right, sucessor.key)
  
  return root

def print_tree(node, level=0, prefix="Root: "):
  if node is not None:
    print(" " * (level * 4) + prefix + str(node.key))
    
    if node.left or node.right:
      print_tree(node.left, level + 1, "L--- ")
      print_tree(node.right, level + 1, "R--- ")

values = [50, 30, 70, 20, 40, 60, 80]

root = None

for value in values:
  root = insert(root, value)

print_tree(root, level=0, prefix= "Root: ")

result, comparisons = search(root, 60, 0)

if result:
  print(f"El valor 60 está en el árbol. Encontrado después de {comparisons} comparaciones.")
else:
  print(f"El valor 60 no está en el árbol")

deleteNode(root, 70)

print(f"Se eliminó el valor 70. El nuevo árbol es:")
print_tree(root, level=0, prefix="Root: ")