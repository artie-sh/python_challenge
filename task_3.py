import urllib
import re

def character(input_string):
	result = ''
	for piece in input_string:	
		if piece in 'abcdefghijklmnopqrstuvwxyz':
			result += piece
	return result


source = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
strings = re.findall('<!--[\n%$@+{}_^#*()&!\]\[abcdefghijklmnopqrstuvwxyz]*-->', source)
print character(strings[0])
