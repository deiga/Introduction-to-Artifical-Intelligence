
class Stop(object):

  def __init__(self, number, name, x, y):
    self.number = number
    self.x = x
    self.y = y
    self.name = name
    self.transportations = []
    self.neighbors = []

  def __repr__(self):
    return str((self.number, self.x, self.y, self.name, len(self.transportations), len(self.neighbors)))

  def __str__(self):
    return self.__repr__()