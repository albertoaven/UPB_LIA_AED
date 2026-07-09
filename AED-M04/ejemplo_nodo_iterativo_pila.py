from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
  key: int
  left: Optional["Node"] = None
  right: Optional["Node"] = None

def preorder_iterative(root: Optional[Node]) -> List[int]:
  if root is None:
    return []
  
  out: List[int] = []
  stack: List[Node] = [root]

  while stack:
    n = stack.pop()
    out.append(n.key)

    if n.right is not None:
      stack.append(n.right)

    if n.left is not None:
      stack.append(n.left)

  return out

def inorder_iterative(root: Optional[Node]) -> List[int]:
    out = []
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        out.append(current.key)

        current = current.right

    return out

def postorder_iterative(root: Optional[Node]) -> List[int]:
  if root is None:
      return []

  stack1 = [root]
  stack2 = []
  out = []

  while stack1:
      node = stack1.pop()
      stack2.append(node)

      if node.left:
          stack1.append(node.left)

      if node.right:
          stack1.append(node.right)

  while stack2:
      out.append(stack2.pop().key)

  return out

if __name__ == "__main__":
  t = Node(4,
           Node(2, Node(1, Node(8), Node(9)), Node(3)),
           Node(6, Node(5), Node(7))
      )

  pre = preorder_iterative(t)
  ino = inorder_iterative(t)
  post = postorder_iterative(t)

  print(pre)
  print(ino)
  print(post)

  assert pre == [4, 2, 1, 8, 9, 3, 6, 5, 7]
  assert ino == [8, 1, 9, 2, 3, 4, 5, 6, 7]
  assert post == [8, 9, 1, 3, 2, 5, 7, 6, 4]

  print("Todos los tests pasaron.")