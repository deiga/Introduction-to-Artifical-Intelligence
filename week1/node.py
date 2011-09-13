class Node(object):
  """docstring for Node"""
  def __init__(self, value, parent = None):
    self.value = value
    self.explored = False
    self.neighbors = []
    self._reached_from = None
    if parent is not None:
      self._parent = parent
      for node in self._parent:
        node.neighbors.append(self)
    else:
      self._parent = []

  def set_explored(self):
    """docstring for explored"""
    self.explored = True

  def set_reached(self, from_node):
    """docstring for set_reached"""
    self.reached_from = from_node

  def parent(self):
    if len(self._parent) == 0:
      return None
    ret_string = "("
    for node in self._parent:
      ret_string = ret_string + node.value + ", "
    return ret_string[:-2] + ")"

  def reached_from(self):
    if self._reached_from is None:
      return None
    return self._reached_from.value

  def print_tree(self):
    print self
    for node in self.neighbors:
      node.print_tree()

  def __repr__(self):
    return "(%s, %s, %s, %s, %s)" %(self.value, self.explored, self.parent(), self.reached_from(), len(self.neighbors))

  def __str__(self):
    return self.__repr__()