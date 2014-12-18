from numlib import get_digit_pow
def main():
	base = 2
	exp = 7830457
	num_digits = 10
	base_10 = 10**num_digits
	print (28433*get_digit_pow(base, exp, num_digits) + 1) % base_10

main()