from numlib import is_permutation, totient

def main():
	max_value = int(10**7)
	min_ratio = float(87109)/79180
	for n in range(2, max_value):
		v = totient(n)
		r = float(n)/v
		if r < min_ratio and is_permutation(n, v):
			min_ratio = r
			print n, v, r

main()
