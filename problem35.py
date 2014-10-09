def get_circular_number(n):
	s = str(n)
	L = []
	for i in range(len(s)):
		L.append(int(s))
		s = s[-1] + s[0:len(s)-1]
	return L

def is_prime(n, L = [2], dic = {1:False, 2:True}):
	if not(n in dic):
		for u in L:
			if (n % u) == 0:
				dic[n] = False
				return False
			if u**2 > n:
				break
		L.append(n)
		dic[n] = True
	return dic[n]

def is_prime2(n):
	for i in range(2, n):
		if n % i == 0:
			return False
		if i**2 >= n:
			break
	return True

circlar_prime = {}
count = 0

for i in range(2, 1000000):
	print "at:", i
	if not(i in circlar_prime) and is_prime2(i):
		L = get_circular_number(i)
		all_primes = True
		for n in L:
			if not(is_prime(n)):
				all_primes = False
				break
		if all_primes:
			for n in L:
				circlar_prime[n] = True
				count += 1
				print n

print len(circlar_prime)
print count