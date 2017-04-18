

def multiplier(basis, power):
	result = 1
	for i in range(power):
		result *= basis

	return result


basis = raw_input("enter basis ")
power = raw_input("enter power ")

print 'result of %s to the power of %s equals %d' % (basis, power, multiplier(int(basis), int(power)))
