# Speech Parser - read speech transcript & create data
#			 	  struct of [words used & instances]
# Christie Mathews 2/27/2016
# mathews.christie@gmail.com

import sys
from pprint import pprint
version_msg = "speech-parser 1.0"
usage_msg = "usage: python SpeechParser.py [speech_fileName] [results_fileName]"

# Checks if String has any Numbers in it
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
# Checks Number of times WORD appears in speech
def instances(inputString):
	print "Occurrences in speech of " + inputString + ": "
	string = inputString.lower()
	if string in SPEECH_DICT:
		return SPEECH_DICT[string]
	else:
		return 0

# Check for proper arguments
if len(sys.argv) == 3:
	speech_fileName  = sys.argv[1]
	results_fileName = sys.argv[2]
else:
	print usage_msg

# Word Separators: ' ' '.' ',' '"'
separators_set = set([' ', '.' , ',', '"'])
SPEECH_DICT = {}
try:
    f = open(speech_fileName)
    for line in f:
    	for word in line.split():
    		if hasNumbers(word):
    			continue
    		word = (word.replace(" ", "")).lower()
    		word = word.replace(".", "")
    		word = word.replace(",", "")
    		word = word.replace("\"", "")
    		word = word.replace("-", "")

    		# Add Word to Dict. or increment count
    		if word in SPEECH_DICT:
    			SPEECH_DICT[word] += 1
    		else:
    			SPEECH_DICT[word] = 1
except IOError as e:
	print "I/O error({0}): {1}".format(e.errno, e.strerror)

# print SPEECH_DICT
with open(results_fileName, 'wt') as out:
    pprint(SPEECH_DICT, stream=out)
