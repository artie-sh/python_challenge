import urllib
import re

def character(input_string):
	result = ''
	for piece in input_string:	
		if piece in 'abcdefghijklmnopqrstuvwxyz':
			result += piece
	return result


source = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
strings = re.findall('[A-Z]{3}[a-z]{1}[A-Z]{3}', source)
#print character(strings[0])
print strings
