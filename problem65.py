from fractions import Fraction

def get_presentations(n):
	L = [2]
	count = 1
	for i in range(n -  1):
		if i % 3 == 1:
			L.append(2*count)
			count += 1
		else:
			L.append(1)
	return L

def compute_e(n):
	def compute(L):
		if len(L) == 1:
			return L[0]
		else:
			return L[0] + Fraction(1, compute(L[1:]))
	return compute(get_presentations(n))

n = 100
print get_presentations(n)
e = compute_e(n)
numerator = e.numerator
s = 0
while (numerator > 0):
	s += numerator % 10
	numerator = numerator / 10
print e
print s
