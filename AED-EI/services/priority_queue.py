import heapq

class PriorityHeap:
  def __init__(self):
    self.heap = []
    self.counter = 0

  # Insertar un elemento
  def insert(self, element, priority):
    heapq.heappush(self.heap, (priority, self.counter, element))

    self.counter += 1

  # Quitar un elemento
  def pickmax(self):
    if(self.heap):
      priority, _, element = heapq.heappop(self.heap)

      return element, priority
    
    return None
  
  # Ver el próximo elemento
  def viewnext(self):
    if(self.heap):
      priority, _, element = self.heap[0]

      return element, priority
    
    return None
  
  def emptyheap(self):
    return len(self.heap) == 0