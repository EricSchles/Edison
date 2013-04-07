import urllib
import json
from bs4 import BeautifulSoup

#Pass in the url of the site from which you want your corpus
def encode(url):
  s = 'http://api.embed.ly/1/extract?key=5ed486a7c46945c2bda8c508de408955&url={0}&format=json&words={1}'.format(urllib.quote_plus(url), 50000)
  return s

#Make the actual URL call to the API
def makeCall(encodedUrl):
  feed = urllib.urlopen(encodedUrl)
  return feed.read()

#Pass in the JSON result from encode, get out the words in the description field
def getWords(jsonObj):
	#sIdx = jsonObj.find("\"description\":") + 16
  sIdx = jsonObj.find("\"content\":") + 11
	#Do I know for a fact that safe always comes after description?
	#Do I have any evidence it ever comes after content? Dumbass
	####eIdx = jsonObj.find("\"safe\": ") - 3
  eIdx = jsonObj.find("\", \"", sIdx);
  result = jsonObj[sIdx:eIdx]
  return result

#Remove all html tags
def clearHTML(content):
  soup = BeautifulSoup(content)
  lines = soup.prettify()
  end = ''
	#print(lines)
	#print()
	#print(type(lines))
  curInTag = False
  lastSpace = False
  lastSlash = False
  for s in lines:
    #print s
    if s == '<':
      curInTag = True
    elif s == '>':
      curInTag = False
    elif s == '\\':
      lastSlash = True
    elif not curInTag:
      if not lastSlash:
        if s.isalpha():
          end += s.lower()
          lastSpace = False
				#if s == ' ' and not lastSpace:
				#	end += s
				#	lastSpace = True
        elif s == '.':
          end += '.'
        elif s == ',':
          end += ','
        elif s == '?':
          end += '?'
        elif s == '!':
          end += '!'
        elif s == '(':
          end += '('
        elif s == ')':
          end += ')'
				#Dashes currently ommited, change based on non-sleep-deprived choice
				#elif s == '-':
				#	end += '-'
      else:
        lastSlash = False
  return end
	
#Put it all together
def callMe(url):
  return clearHTML(getWords(makeCall(encode(url))))
