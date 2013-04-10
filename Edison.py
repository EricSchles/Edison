#!/usr/bin/python

import sys
import random
import math
import string
import corpus
import decrypt


def word_list(file_of_words):
    corpus_words =""
    fileObject = open((file_of_words), 'r', 0)
    for i in fileObject.read():
            corpus_words += i
    return corpus.clearHTML(corpus_words)


def freq_analysis(file_of_words):
    ''' hello'''
    ascii_chars = string.ascii_lowercase + '.,?!()'
    total = 0.0
    numberOfLetters = {}
    freq_of_letters = {}
    for i in ascii_chars:
        numberOfLetters[i] = 0
    for i in file_of_words:
        numberOfLetters[i] += 1
        total += 1
    for i in ascii_chars:
        freq_of_letters[i] = (numberOfLetters[i]/total)
    return freq_of_letters


def final_freq(freq_of_corpus, freq_of_input_text, PaddedEmptyList, inputLIST):
    '''takes freq of corpus and input text, outputs freq number to use in padding'''
    ascii_chars = string.ascii_lowercase + '.,?!()'
    for i in ascii_chars:
        freq_of_corpus[i] = freq_of_corpus[i] * len(PaddedEmptyList) - freq_of_input_text[i] * len(inputList)
    return freq_of_corpus[i]

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

opening( sys.argv[1] ) #reads first file
freq_analysis( word_list(sys.argv[1]) )
NEW,off = generateOffSet() #new and offset
printToFile(sys.argv[2],NEW,off)


"""
Todo:

inputting false positive letter choices
to make it unclear what is actually plaintext 
and ciphertext


"""
