from word_container import WordContainer
import math

wc = WordContainer()

def spamicity(msg):
  """docstring for spamicity"""
  logOdds = math.log(0.5/0.5)
  for word in msg.split():
    logOdds = logOdds + math.log(wc.get_spam_p(word)/wc.get_ham_p(word))
  return math.exp(logOdds)

mesg = "SPECIAL OFFER : VIAGRA on SALE at $1.38 !!! \nCompare the best online pharmacies to buy Viagra. Order Viagra online with huge discount. Multiple benefits include FREE shipping, Reorder discounts, Bonus pills"
print spamicity(mesg)


mesg = "Hi Timo Sand, \nHere is a new event for stuff in your tracker. Check out your upcoming events calendar to see them all. \nOCTOBER 2011 \nSaturday 22 \nKemopetrol at Virgin Oil Co., Helsinki, Finland \nBuy tickets"
print spamicity(mesg)


mesg = "Prepare for amazing winnings at Kings Spin \n\nhttp://www.spinlotcasino.com/?id1b6e583627f73f89d21ef87a88a6a6c24093141fc36380a4e0"
print spamicity(mesg)