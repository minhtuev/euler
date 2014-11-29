from numlib import is_permutation, totient, get_prime_factors

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

def test():
	L = [20617, 45421, 69271, 75841, 162619, 176569,
			284029, 400399, 474883, 732031, 778669,
			783169, 1014109, 1288663, 1504051, 1514419,
			1924891, 1956103, 2006737, 2044501, 2094901, 2239261]
	for u in L:
		print u, totient(u), get_prime_factors(u)

main()
# test()
