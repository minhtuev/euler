from utilities import memoize

def reverse_number(n):
	m = 0
	while n > 0:
		m = m*10 + n%10
		n = n / 10
	return m

@memoize
def is_reversible(n):
	if n % 10 == 0:
		return False
	m = reverse_number(n)
	if m < n:
		return is_reversible(m)
	s = n + m
	while s > 0:
		ch = s % 10
		if ch % 2 == 0:
			return False
		s = s / 10			
	return True

def main():
	count = 0
	n = 1
	while n < 1000000000:
		if is_reversible(n):
			count += 1
			print n, count
		n += 1
	print "count:", count

main()