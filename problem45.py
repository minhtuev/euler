def is_pentagonal(n, m = 0, dic = {}):
	P = m*(3*m -1)/2
	while (n > P):
		m = m + 1
		P = m*(3*m -1)/2
		dic[P] = True
	return n in dic

def is_hexagonal(n, m = 0, dic = {}):
	P = m*(2*m -1)
	while (n > P):
		m = m + 1
		P = m*(2*m -1)
		dic[P] = True
	return n in dic

n = 286
T = n*(n+1)/2
while not(is_pentagonal(T) and is_hexagonal(T)):
	n += 1
	T = n*(n+1)/2
print "T=", T
print "n=", n	