from numlib import get_next_prime, is_prime
from utilities import memoize

def compute_prime_sum(n, min_prime):
	if n <= 1:
		return 0
	elif n == 2:
		return 1
	else:
		prime = min_prime
		count = 0
		while (prime*2 <= n):
			count += compute_prime_sum(n - prime, prime)
			prime = get_next_prime(prime)
		if is_prime(n):
			count += 1
		return count

def main():
	n = 50
	m = compute_prime_sum(n, 2)
	while (m <= 5000):
		n += 1
		m = compute_prime_sum(n, 2)
	print n, m

main()