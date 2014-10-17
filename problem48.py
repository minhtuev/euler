const = 10000000000
def add(a, b):
	return (a + b) % const

def mul(a, b):
	return (a * b) % const

def pow(n, m):
	s = 1
	for i in range(m):
		s = mul(s, n)
	return s

s = 0
for i in range(1, 1001):
	s = add(s, pow(i, i))
print s