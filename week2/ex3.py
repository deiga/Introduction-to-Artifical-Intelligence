#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import unittest
from file_ops import File_ops
from a_star import *

class TestAStar(unittest.TestCase):

    def setUp(self):
      self.file_ops = File_ops()

    def test_search(self):
      for stop in self.file_ops.stops:
        if stop.name == 'Töölöntori':
          goal = stop
          break
      result = search((self.file_ops.stops[0], 0), goal)
      print result

if __name__ == '__main__':
  unittest.main()
