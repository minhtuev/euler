from numlib import is_prime, is_permutation

def main():
	for a in range(1000, 10000):
		if is_prime(a):
			for b in range(a + 1, 10000):
				c = b + (b - a)
				if (c < 10000) and is_permutation(a, b) and is_permutation(b, c) and is_prime(b) and is_prime(c):
					print a, b, c

main()