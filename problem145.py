from utilities import memoize

@memoize
def is_reversible(n):
	m = int(str(n)[::-1])
	if m < n:
		return is_reversible(m)
	else:
		if len(str(n)) != len(str(m)):
			return False
		s = n + m
		s = str(s)
		for ch in s:
			ch = int(ch)
			if ch % 2 == 0:
				return False
		return True

def main():
	count = 0
	for n in range(1, 1000000000 + 1):
		if is_reversible(n):
			print n
			count += 1
	print "count:", count

main()