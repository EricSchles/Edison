#!/usr/bin/python

import sys
import random
import math
import string
import corpus


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
    for i in file_of_words:
        numberOfLetters[i] += 1
    for i in ascii_chars:
        total += numberOfLetters[i]
    for i in ascii_chars:
        freq_of_letters[i] = (numberOfLetters[i]/total)
    return freq_of_letters

#Post fix corpus freq
def post_padding_fix(inputlist, corpus_freq, input_freq, offset, epsilon):
    #get list of chars not meeting freq
    ascii_chars = string.ascii_lowercase + '.,?!()'
    length = len(inputlist)
    fix_chars_above = {}
    fix_chars_below = {}
    for i in ascii_chars:
        diff = corpus_freq[i] - input_freq[i]
        if (diff > epsilon):
            fix_chars_above[i] = int(diff * length)
        elif (diff < -epsilon):
            fix_chars_below[i] = int(diff * length)

    #organize a list of lists for mutable parts of padding
    total = 2
    slices_offset = [[]*2]*len(offset)
    for ind, item in enumerate(offset):
        slices_offset[ind][1] = total
        slices_offset[ind][2] = total + item
        total += 1
    #creating an index to keep track of below changes
    index_of_below = {}
    for key in fix_chars_below:
        x = 0
        index_of_below[x] = key
        x += 1
    random_key = random.randrange(0, len(fix_chars_below))
    random_key = index_of_below[random_key]
    #replacing the aboves with belows
    while(fix_chars_below)
    while (fix_chars_below[random_key] < (epsilon * length))
        which_slice = random.randrange(0, len(offset))
        letter_in_slice = random.randrange(slices_offset[which_slice][1], slices_offset[which_slice][2])
        if inputlist[letter_in_slice] in fix_chars_above
            inputList[letter_in_slice] = fix_chars_below[random_key]
            fix_chars_above[inputlist[letter_in_slice]] -= 1
            if (fix_chars_above[inputlist[letter_in_slice]] < epsilon * length):
                del fix_chars_above[[inputlist[letter_in_slice]]]
            fix_chars_below[random_key] += 1
            if (fix_chars_below[random_key] > -epsilon * length)
                del fix_chars_below[random_key]
                index_of_below = {}
                for key in fix_chars_below:
                    x = 0
                    index_of_below[x] = key
                    x += 1
                random_key = random.randrange(0, len(fix_chars_below))
                random_key = index_of_below[random_key]


    #make this more efficient later by removing below chars
    #how many times do we want to run this before we do freq analysis?










#Open a file
def opening(File):
    fileObject = open(File, 'r', 0)
    listOfChars = []
    for i in fileObject.read():
        listOfChars.append(i)
    print listOfChars


# num_file_char = len(listOfChars) * 1.5 * random.randint(200,500)



def generateOffSet( ):
    """returns NewList and Offset, respectively"""
    offset = []
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
            NewList.append(dict_of_characters[random.randint(0, 31)])
        return NewList,offset


def printToFile(file_of_words, NewList,offset):
    fileObject = open((file_of_words), 'w', 0)
    fileObject.write(NewList+"\n")
    fileObject.write(offset)

opening( sys.argv[1] ) #reads first file
#freq_analysis( word_list(sys.argv[1]) )
NEW,off = generateOffSet() #new and offset
printToFile(sys.argv[2],NEW,off)


