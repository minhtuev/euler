def is_prime(n, L):
	for u in L:
		if (n % u) == 0:
			return False
		if u**2 > n:
			break
	return True

L = [2]
n = 3

while len(L) < 10001:
	if is_prime(n, L):
		L.append(n)
		print n
	n += 2