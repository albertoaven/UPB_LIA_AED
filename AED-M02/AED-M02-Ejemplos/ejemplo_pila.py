class Pila:
  def __init__(self):
    self.elementos = []

  def push(self, elemento):
    self.elementos.append(elemento)

  def pop(self):
    self.elementos.pop()

  def esta_vacia(self):
    return len(self.elementos) == 0