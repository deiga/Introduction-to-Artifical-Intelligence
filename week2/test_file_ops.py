#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import unittest
from file_ops import File_ops

class Test_file_ops(unittest.TestCase):

    def setUp(self):
      self.file_ops = File_ops()

    def test_stop_length(self):
      self.assertEqual(len(self.file_ops.stops), 26)
      print self.file_ops.stops
      print

    def test_trans_length(self):
      self.assertEqual(len(self.file_ops.transportations), 12)
      print self.file_ops.transportations
      print

    def test_stop_trans(self):
      for stop in self.file_ops.stops:
        for trans in stop.transportations:
          print trans
      print

    def test_stop_neighs(self):
      for stop in self.file_ops.stops:
        print stop.neighbors
      print

if __name__ == '__main__':
  unittest.main()
