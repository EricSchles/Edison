import math
import string
import sys
import csv

from sys import argv

script, in_put, in_key = argv

encrypted = open(in_put).read()
out = ''
i = 0
with open(in_key, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		for num in row:
			out += encrypted[i:i+1]
			i += int(num)

print out
