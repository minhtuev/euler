from utilities import memoize

@memoize
def digit_chain(n):
	if n == 1 or n == 89:
		return n
	else:
		next_number = 0
		m = n
		while n > 0:
			next_number += (n % 10)**2
			n /= 10
		n = m
		if next_number == 1 or next_number == 89:
			return next_number
		else:
			return digit_chain(next_number)

def main():
	max_range = 10000000
	count = 0
	for i in range(2, max_range + 1):
		if digit_chain(i) == 89:
			count += 1
			print i
	print "count:", count
main()