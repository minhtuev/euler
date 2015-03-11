from utilities import memoize

@memoize
def is_pan_digital(s):
	if len(s) != 9:
		return False
	dic = {}
	for c in s:
		if c == '0':
			return False
		if c not in dic:
			dic[c] = 1
		else:
			return False
	return True

def fibonacci():
	a = 1
	b = 1
	yield (a, 1)
	yield (b, 2)
	n = a + b
	count = 3
	while (True):
		yield (n, count)
		a = b
		b = n
		n = a + b
		count +=1 

@memoize
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n*factorial(n - 1)

@memoize
def is_permutation(n, m):
	n = list(str(n))
	m = list(str(m))
	if len(n) != len(m):
		return False
	n.sort()
	m.sort()
	for index in range(len(n)):
		if n[index] != m[index]:
			return False
	return True

def get_circular_number(n):
	s = str(n)
	L = []
	for i in range(len(s)):
		if not(int(s) in L):
			L.append(int(s))
		s = s[-1] + s[0:len(s)-1]
	return L

@memoize
def is_prime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

@memoize
def gcd(a, b):
	if b % a == 0:
		return a
	else:
		return gcd(b % a, a)

@memoize
def get_prime_factors(n):
	m = n
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
	return L

@memoize
def get_prime_list(n):
	if n <= 1:
		return []
	elif n == 2:
		return [2]
	else:
		L = [2]
		counter = 3
		while (counter <= n):
			checked = True
			for a in L:
				if counter % a == 0:
					checked = False
					break
				if a**2 >= counter:
					break
			if (checked):
				L.append(counter)
			counter += 2
		return L

@memoize
def totient(n):
	m = n
	prime = 2
	result = 1
	while (n > 1):
		if n % prime == 0:
			result = 1 - 1.0/prime
			while (n % prime) == 0:
				n = n / prime
				result = result*prime
			if n > 1:
				result = result*totient(n)
				n = 1
		prime += 1
	return int(result)

@memoize
def is_square(n):
	m = int(n**0.5)
	if m**2 == n:
		return True
	return False

@memoize
def get_next_prime(n):
	m = n + 1
	while not(is_prime(m)):
		m +=1
	return m

@memoize
def get_digit_pow(base, exp, num_digits):
	base_10 = 10**num_digits
	if exp <= 1:
		return int(base**exp) % base_10
	else:
		result = get_digit_pow(base, exp/2, num_digits)**2 * (base**(exp % 2)) % base_10
		return result

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