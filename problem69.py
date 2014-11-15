from numlib import gcd, get_prime_factors
from sets import Set

def totient(n):
	count = 0
	for i in range(1, n):
		if gcd(i, n) == 1:
			count += 1
	return count

# this requires another approach to the problem
# maybe i need to compute the prime factor set of each number
# and then quickly find the intersection between two prime sets using Set datastructur

def totient2(n, dic):
	count = 0
	for i in range(2, n):
		if len(dic[n].intersection(dic[i])) == 0:
			count += 1
	return count + 1

def totient3(n):
	L = get_prime_factors(n)
	count = float(n)
	for f in L:
		count = count*(1 - 1.0/f)
	return count

def totient4(n, dic = {}):
	m = n
	if not(n in dic):
		index = 2
		dic[m] = 1
		while (n > 1):
			if n % index == 0:
				dic[m] = 1 - 1.0/index
				while (n % index) == 0:
					n = n / index
					dic[m] = dic[m]*index
				if n > 1:
					dic[m] = dic[m]*totient4(n)
					n = 1
			index += 1
	return dic[m]

# ideas: phi(n) = n*product((1 - 1/p_i))
# n/phi(n) = 1/[product(1 - 1/p_i)] => max
# product(1 - 1/p_i) => min => 1/p_i must be maximized => p_i must be minimized
def main():
	max_value = 0
	dic = {}
	primes = []
	for n in range(2, 1000001):
		if float(n)/totient4(n) > max_value:
			max_value = float(n) / totient4(n)
			print n, totient4(n), max_value

print get_prime_factors(1298)
print get_prime_factors(649)
# main()
print get_prime_factors(510510)