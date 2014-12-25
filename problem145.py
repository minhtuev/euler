from utilities import memoize

def reverse_number(n):
	m = 0
	while n > 0:
		m = m*10 + n%10
		n = n / 10
	return m

def is_reversible(n):
	m = reverse_number(n)
	if n % 10 == 0:
		return False
	s = n + m
	while s > 0:
		ch = s % 10
		if ch % 2 == 0:
			return False
		s = s / 10			
	return True

def main():
	count = 0
	for n in range(1, 1000000000 + 1):
		if is_reversible(n):
			print n
			count += 1
	print "count:", count

main()