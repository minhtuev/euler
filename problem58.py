from utilities import memoize
from pprint import PrettyPrinter
from numlib import is_prime

@memoize
def build_square(n):
	if n % 2 == 0:
		return [[]]
	elif n == 1:
		return [[1]]
	else:
		A = build_square(n - 2)
		# dimension of the smaller square
		n2 = len(A)
		m = n2**2 + 1
		for i in range(n2):
			row = A[n2 - 1 - i]
			row.append(m)
			m += 1
		first_row = range(m, m + n)
		first_row.reverse()
		m = m + n
		for row in A:
			row.insert(0, m)
			m += 1
		last_row = range(m, m + n)
		A.insert(0, first_row)
		A.append(last_row)
		return A

def main():
	side = 1
	counter = 2
	result = 1
	num_prime = 0
	diagonal = [1, 1, 1, 1]
	while (result > 0.1):
		side += 2
		for i in range(4):
			diagonal[i] = diagonal[i] + counter + 2*i
			if is_prime(diagonal[i]):
				num_prime += 1
		counter += 2*4
		result = float(num_prime)/(side*2 - 1)
		print result, side, num_prime 
main()