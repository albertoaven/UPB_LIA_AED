from dataclasses import dataclass
from typing import Optional, Iterator, List

@dataclass
class Node:
  key: int
  left: Optional["Node"] = None
  right: Optional["Node"] = None

class InOrderIterator:
  def __init__(self, root: Optional[Node]):
    self._stack: List[Node] = []
    self._push_left(root)

  def _push_left(self, n: Optional[Node]):
    while n is not None:
      self._stack.append(n)
      n = n.left

  def __iter__(self) -> "InOrderIterator":
    return self
  
  def __next__(self) -> int:
    if not self._stack:
      raise StopIteration
    
    n = self._stack.pop()

    if n.right is not None:
      self._push_left(n.right)
    
    return n.key
  
if __name__ == "__main__":
  t = Node(4,
         Node(2, Node(1), Node(3)) ,
         Node(6, Node(5), Node(7)) 
      )
  
  it = InOrderIterator(t)
  out = list(it)

  assert out == [1, 2, 3, 4, 5, 6, 7]