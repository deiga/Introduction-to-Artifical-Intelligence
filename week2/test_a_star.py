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
      e_node = A_Node("Nurnberg", [c_node, b_node], [230, 104])
      g_node = A_Node("Ulm", [b_node, f_node, e_node], [140, 107, 171])
      h_node = A_Node("Bayreuth", [e_node], [75])
      j_node = A_Node("Memmingen", [g_node], [55])
      k_node = A_Node("Munchen", [e_node, g_node, j_node], [170, 123, 115])
      i_node = A_Node("Passau", [e_node, k_node], [220,189])
      l_node = A_Node("Basel", [d_node], [191])
      n_node = A_Node("Zurich", [l_node, j_node], [85, 184])
      m_node = A_Node("Bern", [l_node, n_node], [91, 120])
      o_node = A_Node("Rosenheim", [k_node], [59])
      p_node = A_Node("Linz", [i_node], [102])
      q_node = A_Node("Salzburg", [o_node, p_node], [81, 126])
      r_node = A_Node("Innsbruck", [o_node], [93])
      s_node = A_Node("Landeck", [r_node], [73])

    def test_a_star(self):
      print "A*: "
      result = search(self.graph, "Salzburg")
      print result
      print_route(result[1])
      print

if __name__ == '__main__':
  unittest.main()
