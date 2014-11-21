from numlib import is_prime
from utilities import memoize

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

@memoize
def count_recurring_digits(n):
	n = str(n)
	max_digit_counts = 0
	dic = {}
	for char in n:
		dic[char] = dic.get(char, 0) + 1
		max_digit_counts = max(max_digit_counts, dic[char])
	return max_digit_counts
	
def main():
	num_prime = 8
	dic = {}
	prime_list = []
	# we only care about numbers with 3 recurring digits
	# we don't have to check the primes with two or four recurring digits.
	# if we form 8 different numbers with them, at least once the sum of the digits (and the whole number) is divisible by three.
	n = 101
	while (True):
		if count_recurring_digits(n) >= 3 and is_prime(n):
			check = {}
			temp = []
			for prime in prime_list:
				positions = get_digit_positions(prime, n)
				if len(positions) == 3 and not(positions in check) and same_digit(n, positions) and same_digit(prime, positions):
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
	
		n += 2

main()