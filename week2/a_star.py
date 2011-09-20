#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../week1/')
from node import Node
sys.path.append('../')
from priority_dict import *
import math

path = []
goal_stop = None
SPEED = 100

def search(beginning, goal):
  global path, goal_stop
  goal_stop = goal
  node_list = priority_dict()
  node_list[beginning[0]] = beginning[1]
  while len(node_list) > 0:
    print"Solmulista: " + ", ".join([str((k, v)) for k,v in node_list.items()])
    node = node_list.smallest()
    time = node_list[node]
    print "Path: " + str(path)
    path.append((node.name, time))
    print "Solmu: " + node.name + ", " + str(time)
    node_list.pop_smallest()
    if node.name == goal_stop.name:
      return("Ratkaisu: ", node)
    node_list = _add_a_star(neighbors(node, time), node_list)
  return ("Ei ratkaisua", node)

def _add_a_star(neighs, nodes):
  global path
  return_prioq = nodes
  for stop, time in neighs:
    if stop.name not in [foo[0] for foo in path]:
      return_prioq[stop] = time
      if is_smallest(stop, time, return_prioq):
        path.append((stop, time))
  return return_prioq

def is_smallest(stop, time, node_estimate_list):
  if stop in node_estimate_list:
    return time < node_estimate_list[stop]
  return True

def neighbors(stop, time):
  neighbor_nodes = []
  for line in [trans[0] for trans in stop.transportations]:
    wait_time = calculate_wait_time(line,stop,time)
    next_stop = get_next_stop(line, stop)
    if next_stop is not None and next_stop.name not in [foo[0] for foo in path]:
      travel_time = calculate_travel_time(line, stop, next_stop)
      neighbor_nodes.append((next_stop, time+wait_time+travel_time))
  return neighbor_nodes

def calculate_wait_time(line_name, stop, time):
  next_time = [x[1] for x in stop.transportations if x[0] == line_name].pop()[1]
  while time > next_time:
    next_time += 10
  return time - next_time

def get_next_stop(line_name, stop):
  for neighbor in stop.neighbors:
    for trans_name, trans in neighbor.transportations:
      if trans_name == line_name and stop is not neighbor:
        return neighbor

def calculate_travel_time(line_name, prev_stop, next_stop):
  for trans_name, trans in prev_stop.transportations:
    if trans_name == line_name:
      prev_time = trans[1]
      break
  for trans_name, trans in next_stop.transportations:
    if trans_name == line_name:
      next_time = trans[1]
      break
  goal_time = calculate_time_to_goal(prev_stop)
  return (next_time + goal_time) - prev_time

def calculate_time_to_goal(current):
  print goal_stop
  distance = math.pow(math.fabs(current.x - goal_stop.x), 2) + math.pow(math.fabs(current.y - goal_stop.y), 2 )
  distance = math.sqrt(distance)
  return distance/SPEED

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
