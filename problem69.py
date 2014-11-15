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

def main():
	max_value = 0
	dic = {}
	primes = []
	for n in range(2, 1000001):
		L = get_prime_factors(n)
		dic[n] = Set()
		for f in L:
			dic[n].add(f)
		if float(n)/totient2(n, dic) > max_value:
			max_value = float(n) / totient2(n, dic)
			print n, totient2(n, dic), max_value

print get_prime_factors(1298)
print get_prime_factors(649)
main()
