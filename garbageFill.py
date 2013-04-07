import random

#A function that takes a dictionary of letter/frequency pairs and returns a letter distributed according to those frequencies
def generateGarbage(freqs):
  sum = 0.0
  d = random.random()
  #print d
  #for c in 'abcdefghijklmnopqrstuvwxyz,.!?()':
  c = ' '
  for c in freqs.keys():
    #print(c)
    #print freqs[c]
    sum += freqs[c]
    #print sum
    if (sum >= d):
      #print c
      return c
  #print 'Got through'
  return c
