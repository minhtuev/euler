a = 1
b = 2
n = 3
c = a + b
s = 2
while c <= 4000000:
	print c, n
	if c % 2 == 0:
		s = s + c
	a = b
	b = c
	c = a + b
	n = n + 1
print s