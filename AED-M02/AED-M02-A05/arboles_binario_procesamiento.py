class Nodo:
  def __init__(self, valor):
      self.valor = valor
      self.izq = None
      self.der = None

def preorder(nodo):
  if nodo:
    print(nodo.valor, end=" ")
    preorder(nodo.izq)
    preorder(nodo.der)

def inorder(nodo):
  if nodo:
      inorder(nodo.izq)
      print(nodo.valor, end=" ")
      inorder(nodo.der)

def postorder(nodo):
  if nodo:
      postorder(nodo.izq)
      postorder(nodo.der)
      print(nodo.valor, end=" ")


def main():
  # Crear árbol
  raiz = Nodo(10)
  raiz.izq = Nodo(5)
  raiz.der = Nodo(15)
  raiz.izq.izq = Nodo(2)
  raiz.izq.der = Nodo(7)
  raiz.der.der = Nodo(20)

  # Recorridos
  print("Preorden:")
  preorder(raiz)

  print("\nInorden:")
  inorder(raiz)

  print("\nPostorden:")
  postorder(raiz)


main()