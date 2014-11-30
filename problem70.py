from numlib import is_permutation, totient, get_prime_factors, get_prime_list

def main():
	max_value = int(10**7)
	min_ratio = float(87109)/79180
	for n in range(2239261, max_value):
		factors = get_prime_factors(n)
		if len(factors) <= 2:
			v = totient(n)
			r = float(n)/v
			if r < min_ratio and is_permutation(n, v):
				min_ratio = r
				print n, v, r, get_prime_factors(n)

def main2():
	max_range = 333334
	max_value = 10000000
	prime_lists = get_prime_list(max_range)
	m = len(prime_lists)
	min_ratio = float(87109)/79180
	min_n = 87109
	print prime_lists
	for i in range(m - 1):
		for j in range(i + 1, m):
			p = prime_lists[i]
			q = prime_lists[j]
			n = p*q
			if n > max_value:
				break
			v = int(n*(1 - 1.0/p)*(1 - 1.0/q))
			r = float(n)/v
			print p, q
			if r < min_ratio and is_permutation(n, v):
				min_ratio = r
				min_n = n
				print n, v, r
	print min_ratio, min_n

def test():
	L = [20617, 45421, 69271, 75841, 162619, 176569,
			284029, 400399, 474883, 732031, 778669,
			783169, 1014109, 1288663, 1504051, 1514419,
			1924891, 1956103, 2006737, 2044501, 2094901, 2239261]
	for u in L:
		print u, totient(u), get_prime_factors(u)
87109
main2()
# test()
