from numlib import is_prime

def get_digit_positions(n1, n2):
	n1 = str(n1)
	n2 = str(n2)
	if len(n1) != len(n2):
		return []
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

def main():
	num_prime = 8
	dic = {}
	prime_list = []
	n = 2
	while (True):
		if is_prime(n):
			check = {}
			temp = []
			for prime in prime_list:
				positions = get_digit_positions(prime, n)
				if len(positions) > 0 and not(positions in check) and same_digit(n, positions) and same_digit(prime, positions):
					dic[prime][positions] = dic[prime].get(positions, [])
					dic[prime][positions].append(n)
					if len(dic[prime][positions]) + 1 == num_prime:
						print prime, dic[prime][positions], positions
						return
					check[positions] = True
				# prunning the search space
				if len(str(prime)) != len(str(n)):
					del dic[prime]
				else:
					temp.append(prime)
			dic[n] = {}
			prime_list = temp
			# adding to the growing prime list
			prime_list.append(n)
			print n, prime_list[0]
		n += 1

main()