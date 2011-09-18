#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import glob
from stop import Stop

class File_ops(object):

  def __init__(self):
    self.stops = self.parse_stops()
    self.transportations = self.parse_transportation()
    self.populate_stops()

  def parse_stops(self):
    stops = []
    with open('data/pysakit.txt', 'r') as stops_file:
      for line in stops_file.readlines():
        line.strip()
        if line == "": continue
        number, y, x, name = line.split(" ")
        number = int(number)
        y = int(y)
        x = int(x)
        name = name[:-1] if '\n' in name else name
        stops.append(Stop(number, name, x, y))
    return stops

  def parse_transportation(self):
    transportations = {}
    for trans_file_name in glob.glob('data/linja*.txt'):
      with open(trans_file_name, 'r') as trans_file:
        line_name = self._parse_line(trans_file_name)
        for line in trans_file.readlines():
          line.strip()
          if line == "": continue
          stop_number, estimate = line.split(" ")
          stop_number = int(stop_number)
          estimate = int(estimate)
          trans = (stop_number, estimate)
          if line_name in transportations:
            transportations[line_name].append(trans)
          else:
            transportations[line_name] = [trans]
    return transportations

  def populate_stops(self):
    for line_name, trans_list in self.transportations.items():
      for i, trans in enumerate(trans_list[:-1]):
        if trans not in self.stops[trans[0]-1].transportations:
          self.stops[trans[0]-1].transportations.append((line_name, trans))
        prev = self.stops[trans[0]-1]
        next = self.stops[trans_list[i+1][0]-1]
        if next not in prev.neighbors:
          prev.neighbors.append(next)


  def _parse_line(self, filename):
    return filename.split("/")[1].split(".")[0][5:]
