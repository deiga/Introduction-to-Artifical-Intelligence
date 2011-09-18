#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../week1/')
from node import Node
sys.path.append('../')
from priority_dict import *

def search(beginning, goal):
  node_list = priority_dict();
  node = Node(beginning[0], beginning[1])
  node_list[node] = 0
  while len(node_list) > 0:
    print"Solmulista: " + ", ".join([str((k.state, v)) for k,v in node_list.items()])
    node = node_list.pop_smallest()
    print "Solmu: " + node.state[0].name + ", " + str(node.state[1])
    if node.state[0].name == goal:
      return("Ratkaisu: ", node)
    node.set_explored()
    node_list = _add_a_star(node, node_list)
  return ("Ei ratkaisua", node)

def _add_a_star(popped_node, nodes):
  return_prioq = nodes
  for v, k in popped_node.neighbors:
    if is_smallest((v, k), return_prioq):
      k.set_reached(popped_node)
    if not k.explored and is_smallest((v, k), return_prioq):
      return_prioq[k] = v
  return return_prioq

def is_smallest((estimate,node), node_estimate_list):
  if node in node_estimate_list:
    return estimate < node_estimate_list[node]
  return True

def neighbors(node):
  neighbor_nodes = []
  stop = node.stop()
  time = node.time()
  for line in [trans[0] for trans in node.transportations]:
    wait_time = calculate_wait_time(line,stop,time)
    next_stop =
    pass

def calculate_wait_time(line_name, stop, time):
  next_line = [x[1] for x in stop.transportations if x[0] == line_name].pop()
  next_time = next_time[1]
  return time - next_time if next_time < time else 60 - time + next_time

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
