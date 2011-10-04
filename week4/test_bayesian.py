#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import unittest
from naive_bayesian import *
from word_container import *

class Test_file_ops(unittest.TestCase):

    def setUp(self):
      self.wc = WordContainer()

    # def test_given_spam(self):
    #       mesg = "SPECIAL OFFER : VIAGRA on SALE at $1.38 !!! \nCompare the best online pharmacies to buy Viagra. Order Viagra online with huge discount. Multiple benefits include FREE shipping, Reorder discounts, Bonus pills"
    #       print spamicity(mesg, self.wc)
    #
    #     def test_given_ham(self):
    #       mesg = "Hi Timo Sand, \nHere is a new event for stuff in your tracker. Check out your upcoming events calendar to see them all. \nOCTOBER 2011 \nSaturday 22 \nKemopetrol at Virgin Oil Co., Helsinki, Finland \nBuy tickets"
    #       print spamicity(mesg, self.wc)
    #
    #     def test_other_spam(self):
    #       mesg = "Prepare for amazing winnings at Kings Spin \n\nhttp://www.spinlotcasino.com/?id1b6e583627f73f89d21ef87a88a6a6c24093141fc36380a4e0"
    #       print spamicity(mesg, self.wc)

    def test_ham_words(self):
      print "Ham length: ", len(self.wc.ham)
      self.assertEqual(self.wc.get_ham_p("from"), 17259/828009)

if __name__ == '__main__':
  unittest.main()
