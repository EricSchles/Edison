import random
import math

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

#A function that takes in a string (our message padded with space for padding, and the desired frequencies in the output (dictionary of char/int pairs)
# and returns pad
def generateFrequentGarbage(pad, freqDict):
  arr = []
  #print freqDict
  leng = len(pad)
  #print pad
  #print leng
  totLen = 0
  idx = 0
  for k in freqDict.keys():
    #print k
    #print freqDict[k]
    #print leng
    #Currently math.ceil, since otherwise round-off (often) results in less
    # of each number than we need and we run out of letters to use before we have filled the message
    arr.append(int(math.ceil(freqDict[k]*leng)))
    totLen += int(math.ceil(freqDict[k]*leng))
    #print int(freqDict[k]*leng)
    idx += 1
  #print freqDict
  #print arr
  print totLen
  print len(pad)
  for i in range(0,len(pad)):
    #print i
    #print pad[i]
    if(pad[i] == '\n'):
      j = pickFrequentGarbage(arr, totLen)
      #print " "
      pad[i] = freqDict.keys()[j]
      #print(freqDict.keys()[j])
      #print arr
      arr[j] = arr[j] - 1
      totLen = totLen - 1
      #print arr
      #print ""
  return pad

#Deal with randomly picking from the letters we have left
def pickFrequentGarbage(numLeftArr, totalNumLeft):
  #print numLeftArr
  d = random.randrange(totalNumLeft)
  #print d
  sum = 0
  idx = 0
  while idx < len(numLeftArr):
    sum += numLeftArr[idx]
    #print sum
    if(sum >= d):
      return idx
    idx += 1
  # idx - 1 since the loop will add one after running through everything
  return idx - 1