# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player(Room):
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []
  def __str__(self):
    item_names = []
    for item in self.items:
      item_names.append(item.name)
    return f'\n{self.current_room}\n  Inventory:  {item_names}'