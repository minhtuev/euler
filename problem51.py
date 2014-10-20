prime_list = [2]
n = 3
dic = {}

def get_digit_positions(n1, n2):
	n1 = str(n1)
	n2 = str(n2)
	if len(n1) != len(n2):
		return None
	L = []
	for index in range(len(n1)):
		if n1[index] != n2[index]:
			L.append(index)
	return tuple(L)

def same_digit(n, L):
	n = str(n)
	for index in L:
		if n[index] != n[L[0]]:
			return False
	return True

num_prime = 8
has_found = False
dic = {}
dic[2] = {}
check = {}
finger = 0
while (not has_found):
	is_prime = True
	for prime in prime_list:
		if n % prime == 0:
			is_prime = False
			break
		if prime**2 >= n:
			break
	if is_prime:
		check[n] = {}
		dic[n] = {}
		i = finger
		while (i < len(prime_list)):
			prime = prime_list[i]
			positions = get_digit_positions(n, prime)
			if positions != None and not(positions in check):
				if same_digit(prime, positions) and same_digit(n, positions):
					dic[prime][positions] = dic[prime].get(positions, 1) + 1
					check[n][positions] = 1
					if dic[prime][positions] == num_prime:
						print "the smallest prime found with the desired property is:", prime
						has_found = True
						break
				elif positions == None:
					# all the positions before should be invalid. do not consider anymore.
					finger = i + 1
			i += 1
		# adding to the growing prime list
		prime_list.append(n)
		print n
	n += 1