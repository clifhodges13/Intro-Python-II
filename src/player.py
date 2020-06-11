# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player(Room):
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
  def __str__(self):
    return f'\n{self.current_room}'