class Event:
  def __init__(self, id, timestamp, category, priority, description, origin, destination):
    self.id = id
    self.timestamp = timestamp
    self.category = category
    self.priority = priority
    self.description = description
    self.origin = origin
    self.destination = destination