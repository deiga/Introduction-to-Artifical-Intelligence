from collections import deque
from node import Node

def DFSearch(root_node, goal):
  root_node.set_explored()
  nodes = [root_node]
  while len(nodes) > 0:
    print"Solmulista: " + ", ".join([foo.value for foo in nodes])
    test_node = nodes.pop()
    print "Solmu: " + test_node.value
    if test_node.value == goal:
      return("Ratkaisu: ", test_node)
    test_node.set_explored()
    nodes = _addDFS(test_node, nodes)
  return ("Ei ratkaisua")

def _addDFS(popped_node, nodes):
  return_stack = nodes
  for node in sorted(popped_node.neighbors, reverse=True):
    if node.explored is False and node not in return_stack:
      node.set_reached(popped_node)
      return_stack.append(node)
  return return_stack

def BFSearch(root_node, goal):
  root_node.set_explored()
  nodes = deque([root_node])
  while len(nodes) > 0:
    print"Solmulista: " + ", ".join([foo.value for foo in nodes])
    test_node = nodes.popleft()
    print "Solmu: " + test_node.value
    if test_node.value == goal:
      return("Ratkaisu: ", test_node)
    test_node.set_explored()
    nodes = _addBFS(test_node, nodes)
  return ("Ei ratkaisua")

def _addBFS(popped_node, nodes):
  return_queue = nodes
  for node in sorted(popped_node.neighbors):
    if node.explored is False and node not in return_queue:
      node.set_reached(popped_node)
      return_queue.append(node)
  return return_queue

def print_route(last_node):
  tmp_list = []
  tmp_node = last_node
  while True:
    tmp_list.append(tmp_node)
    if tmp_node._reached_from is not None:
      tmp_node = tmp_node._reached_from
    else:
      break
  print sorted([foo.value for foo in tmp_list])
