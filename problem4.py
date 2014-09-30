from math import log10

def get_nearest_10(n):
	return 10**(int(log10(n)))

def is_palindromic(n):
	m = get_nearest_10(n)
	while (m >= 10):
		a = n / m
		b = n % 10
		if (a != b):
			return False
		n = (n % m) / 10
		m = m / 100
	return True	

def is_pan(s):
	for i in range(len(s) / 2):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True

def find_largest_palindromic():
	b = 999
	m = -1
	p = None
	# find all ordered pairs where a <= b
	while (b > 99):
		a = b
		while (a > 99):
			if is_palindromic(a*b) and a*b > m:
				m = a*b
				p = (a, b)
			a = a - 1
		b = b -1
		# early stopping condition
		if b*b < m :
			return p, m

print find_largest_palindromic()
