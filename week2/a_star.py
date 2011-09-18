#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../week1/')
from node import Node
sys.path.append('../')
from priority_dict import *

def search(root_node, goal):
  root_node.set_explored()
  nodes = priority_dict();
  nodes[root_node] = 0
  while len(nodes) > 0:
    print"Solmulista: " + ", ".join([str((k.value, v)) for k,v in nodes.items()])
    test_node = nodes.pop_smallest()
    print "Solmu: " + test_node.value
    if test_node.value == goal:
      return("Ratkaisu: ", test_node)
    test_node.set_explored()
    nodes = _add_a_star(test_node, nodes)
  return ("Ei ratkaisua", test_node)

def _add_a_star(popped_node, nodes):
  return_prioq = nodes
  for v, k in popped_node.neighbors:
    if not k.explored and is_smallest((v, k), return_prioq):
      k.set_reached(popped_node)
      return_prioq[k] = v
  return return_prioq

def is_smallest((estimate,node), node_estimate_list):
  print (node, estimate)
  if node in node_estimate_list:
    return estimate < node_estimate_list[node]
  return True

def print_route(last_node):
  tmp_list = []
  tmp_node = last_node
  while True:
    tmp_list.append(tmp_node)
    if tmp_node._reached_from is not None:
      tmp_node = tmp_node._reached_from
    else:
      break
  print [bar for bar in reversed([foo.value for foo in tmp_list])]
