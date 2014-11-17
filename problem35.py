from numlib import is_prime, get_circular_number

checked = {}
count = 0
max_range = 1000000

for i in range(2, max_range + 1):
	if not(i in checked) and is_prime(i):
		L = get_circular_number(i)
		all_primes = True
		for n in L:
			if not(is_prime(n)):
				all_primes = False
			checked[n] = True

		if all_primes:
			count += len(L)
			print i

print "num circular prime:", count