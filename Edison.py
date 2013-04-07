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
        	corpus_words.append(i.lower)
	return corpus.clearHTML(corpus_words)

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

fileObject = open("file.txt", 'r', 0)

listOfChars = []
for i in fileObject.read():
	listOfChars.append(i)
print listOfChars


num_file_char = len(listOfChars) * 1.5 * random.randint(200,500)
math.floor(num_file_char)
num_file_char = int(num_file_char)
print num_file_char
for y in xrange(num_file_char):
	listOfChars.append(y)


offset = []
#generates offsets
for l in listOfChars:
	x = random.randrange(0,15,1)
	offset.append(x)
print len(offset) == len(listOfChars)

#this may need to change

NewList = []
dict_of_characters = {}

x = 0
for i in string.ascii_lowercase:
	dict_of_characters[x] = i
	x += 1

for ind,item in enumerate(listOfChars):
	NewList.append(item)
	x = random.sample(offset, random.randrange(2, 75, 1) )
	offset.append(len(x))
	for i in x:
		NewList.append(dict_of_character[random.randint(0, 25)])