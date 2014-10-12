def digit(n, s = '', m = 0):
	while (n > len(s)):
		m += 1
		s += str(m)
	return int(s[n - 1])

print digit(1)*digit(10)*digit(100)*digit(1000)*digit(10000)*digit(100000)*digit(1000000)