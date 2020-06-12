class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def on_take(self):
    print(f'You have taken the {self.name}!\n{self.description}')
  def on_drop(self):
    print(f'You have dropped the {self.name}.')

key = Item('key', 'This key opens locked doors.')