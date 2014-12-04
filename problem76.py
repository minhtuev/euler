from utilities import memoize

@memoize
def count_sum(n, start_index = 1):
	print n, start_index
	if n == 1:
		return 1
	else:
		total_sum = 1 
		for index in range(start_index, n/2 + 1):
			total_sum += count_sum(n - index, index)
		return total_sum

def main():
	print count_sum(100) - 1

main()
