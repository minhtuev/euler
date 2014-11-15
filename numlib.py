def gcd(a, b, dic = {}):
	if not((a, b) in dic):
		if b % a == 0:
			dic[(a, b)] = a
		else:
			dic[(a, b)] = gcd(b % a, a)
	return dic[(a, b)]

def get_prime_factors(n, dic = {}):
	m = n
	if not(n in dic):
		L = []
		index = 2
		while (n > 1):
			if n % index == 0:
				L.append(index)
				while n % index == 0:
					n = n / index
				L.extend(get_prime_factors(n))
				n = 1
			index += 1
		dic[m] = L
	return dic[m]

def get_prime_factors_with_prime_list(n, primes, dic = {}):
	m = n
	if not(n in dic):
		L = []
		index = 0
		while (n > 1) and (index < len(primes)):
			if n % primes[index] == 0:
				L.append(primes[index])
				while n % primes[index] == 0:
					n = n / primes[index]
				L.extend(get_prime_factors(n))
				n = 1
				break
			index += 1
		if index == len(primes):
			L = [m]
		dic[m] = L
	return dic[m]