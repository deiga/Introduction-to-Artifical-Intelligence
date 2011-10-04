from word_container import WordContainer
import Math

wc = new WordContainer()

def spamicity(msg):
  """docstring for spamicity"""
  logOdds = Math.log(0.5/0.5)
  for word in msg.split():
    logOdds = logOdds + Math.log(wc.get_spam_p(word)/wc.get_ham_p(word))
  return Math.exp(logOdds)
#  SPAMICITY(Viesti, P):
#  ￼￼￼logOdds = log(P.Spam / P.noSpam) // P.Spam + P.noSpam = 1
#     for each Sana in Viesti
#       logOdds = logOdds + log(P.Sana_Spam(Sana) / P.Sana_noSpam(Sana))
#      return(exp(logOdds))
