# Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
# Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)

def is_pandigital(s):
	for i in range(1, len(s) + 1):
		if s.find(str(i)) == -1:
			return False
	return True

def is_prime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0 :
			return False
	return True

m = -1
for n in range(123, 100000000):
	if is_pandigital(str(n)) and is_prime(n):
		m = n
		print m

print "largest:", m
