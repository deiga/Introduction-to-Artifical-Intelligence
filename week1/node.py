class Node(object):
  """docstring for Node"""
  value = None
  explored = False
  parent = None
  reached_from = None

  def __init__(self, value, parent = None):
    super(Node, self).__init__()
    self.value = value
    self.parent = parent

  def explored(self):
    """docstring for explored"""
    self.explored = True

  def set_reached(self, from_node):
    """docstring for set_reached"""
    self.reached_from = from_node