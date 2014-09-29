s = 2
n = 600851475143
m = 1

while n > 1:
	if n % s == 0:
		m = s
		while n % s == 0:
			n = n / s
	s = s + 1
	
print m