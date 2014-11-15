from numlib import gcd

def totient(n):
	count = 0
	for i in range(1, n):
		if gcd(i, n) == 1:
			count += 1
	return count

def main():
	max_value = 0
	for n in range(2, 1000001):
		if float(n)/totient(n) > max_value:
			max_value = float(n)/totient(n)
			print n, totient(n), max_value

main()
