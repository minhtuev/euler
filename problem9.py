n = 1000
for a in range(1, n):
	for b in range(a, n - a + 1):
		c = n - a - b
		if c >= b and (a**2 + b**2 == c**2):
			print a, b, c
			print a*b*c

# the problem can also be solved algebraically:
# a^2 + b^2 = c^2
# let say c = m^2 + n^2, b = m^2 - n^2, a = 2mn
# and a + b + c = 1000