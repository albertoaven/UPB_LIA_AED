from datetime import datetime

class Event:
  def __init__(self, id, timestamp, category, priority, description, origin, destination, status):
    self.id = id
    self.timestamp = timestamp
    self.category = category
    self.priority = priority
    self.description = description
    self.origin = origin
    self.destination = destination
    self.age = self.calculate_age()
    self.status = status
  
  def calculate_age(self):
    now = datetime.now()
    return now - self.timestamp