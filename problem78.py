from utilities import memoize

@memoize
def count_sum(n, start_index = 1):
	if n == 1:
		return 1
	else:
		total_sum = 1 
		for index in range(start_index, n/2 + 1):
			total_sum += count_sum(n - index, index)
		return total_sum

def main():
	n = 5
	m = count_sum(n)
	while (m % 1000000 != 0):
		n += 1
		m = count_sum(n)
		if m % 10 == 0:
			print n, m

main()
