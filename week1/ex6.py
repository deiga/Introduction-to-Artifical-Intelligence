import unittest
from node import Node
from bfs_dfs import *

class TestNode(unittest.TestCase):

    def setUp(self):
      """docstring for setUp"""
      self.graph = Node("A")
      b_node = Node("B", [self.graph])
      c_node = Node("C", [self.graph])
      d_node = Node("D", [self.graph])
      f_node = Node("F", [c_node, d_node])
      e_node = Node("E", [f_node])

    def test_DFS(self):
      print "DFS: "
      result = DFSearch(self.graph, "F")
      print result
      print_route(result[1])
      print

    def test_BFS(self):
      print "BFS: "
      result = BFSearch(self.graph, "F")
      print result
      print_route(result[1])
      print

if __name__ == '__main__':
  unittest.main()
