import sys

class WordContainer(object):
  """docstring for WordContainer"""

  def __init__(self):
    self.ham = {}
    self.spam = {}

  def load_hamwords(self):
    """docstring for load_hamwords"""
    with open('hamwords.txt', 'r') as hamwords:
      for line in hamwords.readlines():
        vals = line.split()
        self.ham[vals[1]] = vals[0]

  def load_spamwords(self):
    """docstring for load_spamwords"""
    with open('spamwords.txt', 'r') as spamwords:
      for line in spamwords.readlines():
        vals = line.split()
        self.spam[vals[1]] = vals[0]

  def get_ham_p(hamword):
    occurrences = self.ham[hamword]
    return occurrences/len(self.ham)

  def get_spam_p(spamword):
    occurrences = self.spam[spamword]
    return occurrences/len(self.spam)