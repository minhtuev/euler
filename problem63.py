count = 0
for n in range(1, 10):
	index = 1
	power = 1
	while (True):
		power = power * n
		if len(str(power)) == index:
			print n, index, power
			count += 1
		if power <= 10**(index - 1):
			break
		index += 1

print "total count:", count