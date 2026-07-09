from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
  key: int
  left: Optional["Node"] = None
  right: Optional["Node"] = None


class PreOrderIterator:
  def __init__(self, root):
    self._stack = [root] if root else []

  def __iter__(self):
    return self

  def __next__(self):
    if not self._stack:
      raise StopIteration

    node = self._stack.pop()

    # Primero derecha, luego izquierda.
    if node.right:
      self._stack.append(node.right)

    if node.left:
      self._stack.append(node.left)

    return node.key
  
class PostOrderIterator:
  def __init__(self, root):
    self._stack = []
    self.output = []

    if root:
      self._stack.append(root)

      while self._stack:
        node = self._stack.pop()
        self.output.append(node)

        if node.left:
          self._stack.append(node.left)

        if node.right:
          self._stack.append(node.right)

  def __iter__(self):
    return self

  def __next__(self):
    if not self.output:
      raise StopIteration

    return self.output.pop().key
  
if __name__ == "__main__":
  t = Node(4,
    Node(2,
      Node(1, Node(8), Node(9)),
      Node(3)),
    Node(6,
      Node(5),
      Node(7))
  )

assert list(PreOrderIterator(t)) == [4, 2, 1, 8, 9, 3, 6, 5, 7]
assert list(PostOrderIterator(t)) == [8, 9, 1, 3, 2, 5, 7, 6, 4]