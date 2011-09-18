#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import glob

def parse_stops():
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
      stops.append((number, (x, y), name))
  return stops

def parse_transportation():
  transportations = []
  for trans_file_name in glob.glob('data/linja*.txt'):
    with open(trans_file_name, 'r') as trans_file:
      line_name = parse_line(trans_file_name)
      for line in trans_file.readlines():
        line.strip()
        if line == "": continue
        number, estimate = line.split(" ")
        number = int(number)
        estimate = int(number)
        transportations.append((line_name, number, estimate))
  return transportations


def parse_line(filename):
  return filename.split("/")[1].split(".")[0][5:]

print parse_stops()
print parse_transportation()