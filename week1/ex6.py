from collections import deque
from node import Node

def DFSearch(root_node, goal):
  """docstring for DFSearch"""
  root_node.set_explored()
  nodes = [root_node]
  while len(nodes) > 0:
    test_node = nodes.pop()
    print test_node
    if test_node.value == goal:
      return("Ratkaisu: ", test_node)
    test_node.set_explored()
    nodes = _addDFS(test_node, nodes)
  return ("Ei raktaisua")

def _addDFS(popped_node, nodes):
  return_stack = nodes
  for node in popped_node.neighbors:
    if node.explored is False and node not in return_stack:
      return_stack.append(node)
  return return_stack

def BFSearch(root_node, goal):
  root_node.set_explored()
  nodes = deque([root_node])
  while len(nodes) > 0:
    test_node = nodes.popleft()
    print test_node
    if test_node.value == goal:
      return("Ratkaisu: ", test_node)
    test_node.set_explored()
    nodes = _addBFS(test_node, nodes)
  return ("Ei raktaisua")

def _addBFS(popped_node, nodes):
  return_queue = nodes
  for node in popped_node.neighbors:
    if node.explored is False and node not in return_queue:
      return_queue.append(node)
  return return_queue