def preorder_list(tree, i=0):
  if i >= len(tree) or tree[i] is None:
    return []

  return (
    [tree[i]]
    + preorder_list(tree, 2 * i + 1)
    + preorder_list(tree, 2 * i + 2)
  )


def inorder_list(tree, i=0):
  if i >= len(tree) or tree[i] is None:
    return []

  return (
    inorder_list(tree, 2 * i + 1)
    + [tree[i]]
    + inorder_list(tree, 2 * i + 2)
  )


def postorder_list(tree, i=0):
  if i >= len(tree) or tree[i] is None:
    return []

  return (
    postorder_list(tree, 2 * i + 1)
    + postorder_list(tree, 2 * i + 2)
    + [tree[i]]
  )

node = [4, 2, 6, 1, 3, 5, 7, 8, 9]

pre = preorder_list(node)
ino = inorder_list(node)
post = postorder_list(node)

print(pre)
print(ino)
print(post)

assert pre == [4, 2, 1, 8, 9, 3, 6, 5, 7]
assert ino == [8, 1, 9, 2, 3, 4, 5, 6, 7]
assert post == [8, 9, 1, 3, 2, 5, 7, 6, 4]

print("Todos los tests pasaron.")