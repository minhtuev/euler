from fractions import Fraction
from numlib import gcd

def main():
	min_fraction = Fraction(1, 3)
	max_fraction = Fraction(1, 2)

	count = 0
	for d in range(4, 12000 + 1):
		for n in range(max(d/3 - 1, 1), d/2 + 1):
			f = Fraction(n, d)
			if gcd(n, d) == 1 and min_fraction < f and max_fraction > f:
				count += 1

	print "count:", count

main()
