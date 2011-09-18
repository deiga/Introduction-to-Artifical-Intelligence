
class Node(object):
  def __init__(self, stop, time):
    self.state = (stop, time)
    self.reached_from = None
    self.explored = False

  def stop(self):
    return self.state[0]

  def time(self):
    return self.state[1]

  def set_explored(self):
    self.explored = True