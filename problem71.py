from fractions import Fraction

def main():
	desired_value = Fraction(3, 7)
	max_range = 1000000
	max_fraction = Fraction(2, 5)
	for denominator in range(5, max_range + 1):
		numerator = int(desired_value*denominator)
		while Fraction(numerator, denominator) < desired_value:
			numerator += 1
		numerator -= 1
		if Fraction(numerator, denominator) > max_fraction:
			max_fraction = Fraction(numerator, denominator)
			print max_fraction, float(max_fraction)

main()