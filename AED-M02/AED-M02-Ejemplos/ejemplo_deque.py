from collections import deque

class Cola:
  def __init__(self):
    self.elementos = deque()

  def enqueue(self, elemento):
    self.elementos.append (elemento)

  def dequeue(self):
    if not self.esta_vacia():
      self.elementos.popleft()

  def esta_vacia(self):
    return len(self.elementos) == 0
  

def main():
  cola = Cola()

  cola.enqueue("Alberto")
  cola.enqueue("Keislene")
  cola.enqueue("Busqui")
  cola.enqueue("Tomás")

  
  cola.dequeue()

main()