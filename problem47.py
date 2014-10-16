def count_prime_factors(n, dic = {1:1}):
	if not(n in dic):
		i = 2
		s = 0
		while (n > 1):
			if n % i == 0:
				s += 1
				while (n % i) == 0:
					n = n / i
			i += 1
		dic[n] = s
	return dic[n]

n = 210
while not(count_prime_factors(n) == 4 and count_prime_factors(n+1) == 4 and count_prime_factors(n+2) == 4 and count_prime_factors(n+3)==4):
	n += 1
print "n=", n