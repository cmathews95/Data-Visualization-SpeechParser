# Data-Visualization-SpeechParser
(Python) Parses 2016 Presidential Nominee Speeches and gives counts of the different words used.

bernie_speech.txt:  Partial HTML of website I pulled speech from

bs.txt:		    After parsing/removing remaining html tags

removehtmltags.txt: Contains Script used to remove HTML tags. Need to
		    modify to work on any html page.

SpeechParser.py:    Parses through txt file and creates a dictionary of 
		    words used in speech & number of times used, creates
		    a file named with the second argument and pretty
		    prints the dictionary with word/word count into this
		    file.