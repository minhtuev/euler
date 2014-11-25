from numlib import gcd, get_prime_factors
from sets import Set

def totient1(n):
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

# ideas: phi(n) = n*product((1 - 1/p_i))
# n/phi(n) = 1/[product(1 - 1/p_i)] => max
# product(1 - 1/p_i) => min => 1/p_i must be maximized => p_i must be minimized
def main():
	max_value = 0
	dic = {}
	primes = []
	for n in range(2, 1000001):
		if float(n)/totient(n) > max_value:
			max_value = float(n) / totient(n)
			print n, totient(n), max_value

print get_prime_factors(1298)
print get_prime_factors(649)
# main()
print get_prime_factors(510510)