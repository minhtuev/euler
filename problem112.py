def is_increasing(n):
	s = str(n)
	s = [int(ch) for ch in s]
	for i in range(len(s) - 1):
		if s[i] > s[i + 1]:
			return False
	return True

def is_decreasing(n):
	s = str(n)
	s = [int(ch) for ch in s]
	for i in range(len(s) - 1):
		if s[i] < s[i + 1]:
			return False
	return True

def is_bouncy(n):
	return not(is_increasing(n) or is_decreasing(n))

def main():
	n = 1
	num_boucy = 0
	while (float(num_boucy)/n < 0.99):
		n += 1
		if is_bouncy(n):
			num_boucy += 1
		print n, num_boucy

main()