#!/usr/bin/python

import random
import math
import string
import corpus

#Open a file



def word_list(file_of_words):
    corpus_words =""
    fileObject = open((file_of_words), 'r', 0)
    for i in fileObject.read():
            corpus_words += i
    return corpus.clearHTML(corpus_words)

print word_list('inputFile.txt')

def freq_analysis(file_of_words):
    ascii_chars = string.ascii_lowercase + '.,?!()'
    total = 0
    numberOfLetters = {}
    freq_of_letters = {}
    for i in ascii_chars:
        numberOfLetters[i] = 0
    for i in word_list(file_of_words):
        numberOfLetters[i] += 1
    for i in ascii_chars:
        total += numberOfLetters[i]
    for i in ascii_chars:
        freq_of_letters[i] = numberOfLetters[i]/total
    return freq_of_letters


#Open a file

fileObject = open("inputFile.txt", 'r', 0)

listOfChars = []
for i in fileObject.read():
    listOfChars.append(i)
print listOfChars


# num_file_char = len(listOfChars) * 1.5 * random.randint(200,500)
# math.floor(num_file_char)
# num_file_char = int(num_file_char)
# print num_file_char
# for y in xrange(num_file_char):
#     listOfChars.append(y)


offset = []


#this may need to change

NewList = []
dict_of_characters = {}
ascii_chars = string.ascii_lowercase + '.,?!()'
x = 0
for i in ascii_chars:
    dict_of_characters[x] = i
    x += 1

for ind,item in enumerate(listOfChars):
    NewList.append(item)
    x = random.sample(xrange(140), random.randrange(2, 70, 1) )
    offset.append(len(x))
    for i in x:
        NewList.append(dict_of_characters[random.randint(0, 25)])
