import unittest
from node import Node
from collections import deque

class TestNode(unittest.TestCase):

    def setUp(self):
      """docstring for setUp"""
      pass

    def test_node_queue(self):
      """docstring for test_node_qeue"""
      queue = deque()
      queue.append(Node("1st"))
      queue.append(Node("2nd"))
      queue.append(Node("3rd"))
      self.assertEqual(queue.popleft().value, Node("1st").value)
      self.assertEqual(queue.popleft().value, Node("2nd").value)
      self.assertEqual(queue.popleft().value, Node("3rd").value)

    def test_node_stack(self):
      """docstring for test_node_stack"""
      stack = []
      stack.append(Node("1st"))
      stack.append(Node("2nd"))
      stack.append(Node("3rd"))
      self.assertEqual(stack.pop().value, Node("3rd").value)
      self.assertEqual(stack.pop().value, Node("2nd").value)
      self.assertEqual(stack.pop().value, Node("1st").value)

if __name__ == '__main__':
  unittest.main()
