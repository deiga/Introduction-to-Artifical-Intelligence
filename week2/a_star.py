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
  node_list[node.stop()] = node.time()
  while len(node_list) > 0:
    print"Solmulista: " + ", ".join([str((k, v)) for k,v in node_list.items()])
    node = node_list.smallest()
    print "Solmu: " + node.name + ", " + str(node_list[node])
    node_list.pop_smallest()
    if node.name == goal:
      return("Ratkaisu: ", node)
    node.set_explored()
    node_list = _add_a_star(node, node_list)
  return ("Ei ratkaisua", node)

def _add_a_star(popped_node, nodes):
  return_prioq = nodes
  neighbors = neighbors(popped_node)
  for node in neighbors:
    if is_smallest(node.stop(), node.time(), return_prioq):
      node.set_reached(popped_node)
    if not node.explored:
      return_prioq[node.stop()] = node.time()
  return return_prioq

def is_smallest(stop, time, node_estimate_list):
  if stop in node_estimate_list:
    return time < node_estimate_list[stop]
  return True

def neighbors(node):
  neighbor_nodes = []
  stop = node.stop()
  time = node.time()
  for line in [trans[0] for trans in node.transportations]:
    wait_time = calculate_wait_time(line,stop,time)
    next_stop = get_next_stop(line, stop)
    if next_stop is not None:
      travel_time = calculate_travel_time(line, stop, next_stop)
      neighbor_nodes.append(Node(next_stop, time+wait_time+travel_time))
  return neighbor_nodes

def calculate_wait_time(line_name, stop, time):
  next_time = [x[1] for x in stop.transportations if x[0] == line_name].pop()[1]
  while time > next_time:
    next_time + 10
  return time - next_time

def get_next_stop(line_name, stop):
  next_stop = [[bar.name for bar in foo.transportations if bar.name == line_name] for foo in stop.neighbors].pop()
  return next_stop

def calculate_travel_time(line_name, prev_stop, next_stop):
  prev_time = [x[1] for x in prev_stop.transportations if x[0] == line_name].pop()[1]
  next_time = [x[1] for x in next_stop.transportations if x[0] == line_name].pop()[1]
  return next_time - prev_time

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
