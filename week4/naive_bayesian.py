# !/usr/bin/python
# This Python file uses the following encoding: utf-8 #

from word_container import WordContainer
import math

def spamicity(msg, wc):
  """docstring for spamicity"""
  logOdds = math.log(0.5/0.5)
  for word in msg.lower().split():
    logOdds = logOdds + math.log(wc.get_spam_p(word)/wc.get_ham_p(word))
  return math.exp(logOdds)
