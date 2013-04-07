import random

#A function that takes a dictionary of letter/frequency pairs and returns a letter distributed according to those frequencies
def generateGarbage(freqs):
  sum = 0.0
  d = random.random()
  #for c in 'abcdefghijklmnopqrstuvwxyz,.!?()':
  for c in freqs.keys():
    #print(c)
    sum += freqs[c]
    if (sum >= d):
    return c
