#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../week1/')
from node import Node

class A_Node(Node):
  def __init__(self, value, parent = None, estimates = [0]):
    self.value = value
    self.explored = False
    self.neighbors = []
    self._reached_from = None
    if parent is not None:
      self._parent = parent
      for node, estimate in zip(self._parent, estimates):
        node.neighbors.append((estimate, self))
    else:
      self._parent = []

  def print_tree(self):
    print self
    for tpl in self.neighbors:
      tpl[0].print_tree()