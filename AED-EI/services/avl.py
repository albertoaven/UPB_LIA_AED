"""
Implementación de un Árbol AVL para almacenar e indexar
eventos utilizando su ID como clave de búsqueda.

Características:

- Inserción O(log n)
- Búsqueda O(log n)
- Auto-balanceo mediante rotaciones
- Rotación LL (Left Left)
- Rotación RR (Right Right)
- Rotación LR (Left Right)
- Rotación RL (Right Left)
"""

import time

class AVLNode:
  """
  Representa un nodo dentro del árbol AVL.

  Cada nodo almacena:

  - El evento completo.
  - El ID del evento.
  - Referencia al hijo izquierdo.
  - Referencia al hijo derecho.
  - Altura del nodo.
  """

  def __init__(self, event):
    # Evento almacenado
    self.event = event

    # Clave utilizada para ordenar el árbol
    self.key = event.id

    # Hijos
    self.left = None
    self.right = None

    # Altura inicial de una hoja
    self.height = 1

class AVLTree:
  """
  Implementación de un Árbol AVL.

  Un AVL es un Árbol Binario de Búsqueda
  que se mantiene balanceado automáticamente.
  """

  def __init__(self):
    # Raíz del árbol
    self.root = None

    self.insert_operations = 0
    self.search_operations = 0
    self.rotations = 0

  def get_height(self, node):
    """
    Devuelve la altura de un nodo.
    """

    if node is None:
      return 0

    return node.height

  def get_balance(self, node):
    """
    Calcula el factor de balance.

    altura(izquierdo) - altura(derecho)
    """

    if node is None:
      return 0

    return (
      self.get_height(node.left)
      - self.get_height(node.right)
    )

  def rotate_right(self, y):
    """
    Rotación simple hacia la derecha.

    Caso LL (Left Left).
    """

    self.rotations += 1

    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    y.height = (
      1 +
      max(
        self.get_height(y.left),
        self.get_height(y.right)
      )
    )

    x.height = (
      1 +
      max(
        self.get_height(x.left),
        self.get_height(x.right)
      )
    )

    return x

  def rotate_left(self, x):
    """
    Rotación simple hacia la izquierda.

    Caso RR (Right Right).
    """

    self.rotations += 1

    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    x.height = (
      1 +
      max(
        self.get_height(x.left),
        self.get_height(x.right)
      )
    )

    y.height = (
      1 +
      max(
        self.get_height(y.left),
        self.get_height(y.right)
      )
    )

    return y

  def insert(self, event):
    """
    Inserta un evento en el árbol.
    """

    self.insert_operations += 1

    self.root = self._insert(
      self.root,
      event
    )

  def _insert(self, node, event):
    """
    Inserción recursiva.

    1. Inserta como ABB.
    2. Actualiza alturas.
    3. Calcula balance.
    4. Realiza rotaciones.
    """

    if node is None:
      return AVLNode(event)

    if event.id < node.key:

      node.left = self._insert(
        node.left,
        event
      )

    elif event.id > node.key:

      node.right = self._insert(
        node.right,
        event
      )

    else:
      return node

    node.height = (
      1 +
      max(
        self.get_height(node.left),
        self.get_height(node.right)
      )
    )

    balance = self.get_balance(node)

    # Caso LL
    if (
      balance > 1 and
      event.id < node.left.key
    ):
      return self.rotate_right(node)

    # Caso RR
    if (
      balance < -1 and
      event.id > node.right.key
    ):
      return self.rotate_left(node)

    # Caso LR
    if (
      balance > 1 and
      event.id > node.left.key
    ):

      node.left = self.rotate_left(
        node.left
      )

      return self.rotate_right(node)

    # Caso RL
    if (
      balance < -1 and
      event.id < node.right.key
    ):

      node.right = self.rotate_right(
        node.right
      )

      return self.rotate_left(node)

    return node
  
  def print_tree(self):
    """
    Imprime visualmente el árbol AVL.

    Se utiliza para mostrar la estructura
    del árbol y verificar que las rotaciones
    están funcionando correctamente.
    """

    self._print_tree(
      self.root,
      "",
      True
    )

  def _print_tree(self,  node,  indent,  last):
    """
    Recorre el árbol recursivamente e imprime
    cada nodo mostrando su posición relativa.

    Args:
      node (AVLNode): Nodo actual.
      indent (str): Espacios de indentación.
      last (bool): Indica si es el último hijo.
    """

    if node is None:
      return

    print(indent, end="")

    if last:
      print("R----", end="")
      indent += "     "

    else:
      print("L----", end="")
      indent += "|    "

    print(node.key)

    self._print_tree(
      node.left,
      indent,
      False
    )

    self._print_tree(
      node.right,
      indent,
      True
    )

  def search(self, key):
    """
    Busca un evento dentro del árbol utilizando su ID.

    Args:
      key (int): ID a buscar.

    Returns:
      Event | None
    """

    start_time = time.perf_counter()

    self.search_operations += 1

    result = self._search(
          self.root,
          key
        )
    
    search_time = time.perf_counter() - start_time

    return result, search_time, self.search_operations

  def _search(self, node, key):
    """
    Búsqueda recursiva en el árbol AVL.

    Args:
      node (AVLNode): Nodo actual.
      key (int): ID buscado.

    Returns:
      Event | None
    """

    if node is None:
      return None

    if key == node.key:
      return node.event

    if key < node.key:

      return self._search(
        node.left,
        key
      )

    return self._search(
      node.right,
      key
    )

def build_event_avl(events):
  """
  Construye un árbol AVL a partir de una lista de eventos.
  """
  start_time = time.perf_counter()

  tree = AVLTree()

  for event in events:
    tree.insert(event)

  build_time = time.perf_counter() - start_time

  return tree, build_time