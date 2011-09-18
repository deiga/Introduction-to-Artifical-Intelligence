#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import unittest
from a_node import A_Node
from a_star import *

class TestAStar(unittest.TestCase):

    def setUp(self):
      """docstring for setUp"""
      self.graph = A_Node("Frankfurt")
      b_node = A_Node("Wurzburg", [self.graph], [111])
      c_node = A_Node("Mannheim", [self.graph], [85])
      d_node = A_Node("Karlsruhe", [c_node], [67])
      f_node = A_Node("Stuttgart", [b_node, d_node], [140, 64])
      e_node = A_Node("Nurnberg", [c_node], [230])
      g_node = A_Node("Ulm", [b_node, d_node, e_node], [140, 64, 171])
      f_node = A_Node("Bayreuth", [e_node], [75])

    def test_a_star(self):
      print "A*: "
      result = search(self.graph, "Bayreuth")
      print result
      print_route(result[1])
      print

if __name__ == '__main__':
  unittest.main()
