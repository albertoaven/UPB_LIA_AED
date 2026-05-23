import heapq

class PriorityHeap:
  def __init__(self):
    self.heap = []
    self.counter = 0

  #insertar
  def insert(self, task, priority):
    heapq.heappush(self.heap, (priority, self.counter, task))

    self.counter += 1

  #extraer
  def pickmax(self):
    if(self.heap):
      priority, _, task = heapq.heappop(self.heap)

      return task, priority
    
    return None
  
  #ver_proxima
  def viewnext(self):
    if(self.heap):
      priority, _, task = self.heap[0]

      return task, priority
    
    return None
  
  def emptyheap(self):
    return len(self.heap) == 0
  
def main():  
  heap = PriorityHeap()

  heap.insert("Tarea A", 3)
  heap.insert("Tarea B", 5)
  heap.insert("Tarea C", 1)
  heap.insert("Tarea D", 5)

  print("Consulta:", heap.viewnext())

  while not heap.emptyheap():
      print("Extraído:", heap.pickmax())

main()