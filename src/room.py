# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []
  def __str__(self):
    if len(self.items) > 0:
      item_names = []
      for item in self.items:
        item_names.append(item.name)
      return f'{self.name}\n{self.description}\n  Room Items: {item_names}'
    else:
      return f'{self.name}\n{self.description}\n  Room Items: []'