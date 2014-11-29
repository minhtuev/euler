from numlib import totient

def main():
	# max_range = 8
	max_range = 1000000
	num_fractions = 0

	for d in range(2, max_range + 1):
		num_fractions += totient(d)

	print "num fractions:", num_fractions

main()