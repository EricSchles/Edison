#!/usr/bin/python

import sys
import random
import math
import string
import corpus
import garbageFill

def word_list(file_of_words):
    corpus_words =""
    fileObject = open((file_of_words), 'r', 0)
    for i in fileObject.read():
            corpus_words += i
    return corpus.clearHTML(corpus_words)


def freq_analysis(file_of_words):
    ascii_chars = string.ascii_lowercase + '.,?!()'
    total = 0.0
    numberOfLetters = {}
    freq_of_letters = {}
    for i in ascii_chars:
      numberOfLetters[i] = 0
    #print numberOfLetters
    for i in file_of_words:
      numberOfLetters[i] += 1
      total += 1
    #print numberOfLetters
    #for i in file_of_words:
    #    total += numberOfLetters[i]
    #print total
    for i in ascii_chars:
      freq_of_letters[i] = (numberOfLetters[i]/total)
    #print freq_of_letters
    return freq_of_letters

def badfreq_analysis(file_of_words):
  ascii_chars = string.ascii_lowercase + '.,?!()'
  total = 0
  numberOfLetters = {}
  freqOfLetters = {}
  for i in ascii_chars:
    numberOfLetters[i] = 0
  for i in file_of_words:
    numberOfLetters[i] += 1
    total += 1
  for i in ascii_chars:
    freqOfLetters[i] = (numberOfLetters[i] / total)
  return freqOfLetters


#Open a file
def opening(File):
    fileObject = open(File, 'r', 0)
    listOfChars = []
    for i in fileObject.read():
        listOfChars.append(i)
    print listOfChars


# num_file_char = len(listOfChars) * 1.5 * random.randint(200,500)



def generateOffSet(inputStr, corpusURL):
    inputStr = corpus.clearHTML(inputStr)
    #print(inputStr)
    offset = []
    NewList = []
    dict_of_characters = {}
    ascii_chars = string.ascii_lowercase + '.,?!()'
    x = 0
    freq = freq_analysis(corpus.callMe(corpusURL))
    #print(freq)
    for i in ascii_chars:
        dict_of_characters[x] = i
        x += 1
    #for ind,item in enumerate(listOfChars):
    #print inputStr
    for ind,item in enumerate(inputStr):
        #print item
        NewList.append(item)
        x = random.sample(xrange(140), random.randrange(2, 70, 1) )
        #print x
        offset.append(len(x))
        for i in x:
            #NewList.append(dict_of_characters[random.randint(0, 25)])
    		#NewList.append(garbageFill.generateGarbage(
          c = garbageFill.generateGarbage(freq);
          #print c
          NewList.append(c)
    return NewList,offset


def printToFile(file_of_words, NewList,offset):
    fileObject = open((file_of_words), 'w', 0)
    fileObject.write(NewList+"\n")
    fileObject.write(offset)	
