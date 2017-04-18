def positioner(letter):
	index = 0
	for piece in 'abcdefghijklmnopqrstuvwxyz':
		if letter == piece:
			return index
		index += 1
			

def translator(input_string):
	result = ''
	alphabet = 'abcdefghijklmnopqrstuvwxyzab'
	for item in input_string:
		if item in alphabet:
			increment = alphabet[positioner(item) + 2]
		else:
			increment = item
		result += increment

	return result



raw_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."



print translator(raw_input('enter text to translate '))



