def sum_digits(n):
	n = str(n)
	s = sum([ord(c) for c in n]) - 48*len(n)
	return s

max_sum = 0
for a in range(2, 100):
	n = 1
	for i in range(100):
		n *= a
		if sum_digits(n) > max_sum:
			print n
			print a, i + 1
			max_sum = sum_digits(n)

print "max sum:", max_sum