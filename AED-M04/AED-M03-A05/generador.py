from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
  key: int
  left: Optional["Node"] = None
  right: Optional["Node"] = None

def postorder_list(root):
  if root is None:
    return []

  return (
    postorder_list(root.left)
    + postorder_list(root.right)
    + [root.key]
  )

def postorder_gen(root):
  if root is None:
    return

  yield from postorder_gen(root.left)
  yield from postorder_gen(root.right)
  yield root.key

if __name__ == "__main__":
  t = Node(
  4,
  Node(
    2,
    Node(1, Node(8), Node(9)),
    Node(3)
  ),
  Node(
    6,
    Node(5),
    Node(7)
  )
)
  
assert postorder_list(t) == list(postorder_gen(t))

print(postorder_list(t))
print(list(postorder_gen(t)))