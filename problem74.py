from utilities import memoize
from numlib import factorial

@memoize
def compute_factorial_digits(n):
	L = str(n)
	sum_digits = 0
	for ch in L:
		sum_digits += factorial(int(ch))
	return sum_digits


def compute_loop(n):
	checked = {}
	count = 0
	while (True):
		checked[n] = True
		m = compute_factorial_digits(n)
		count += 1
		if m in checked:
			break
		n = m
	return count

def main():
	count = 0
	for n in range(1, 1000001):
		print n
		if compute_loop(n) == 60:
			count += 1
	print "count:", count

main()
