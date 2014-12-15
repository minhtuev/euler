def main():
	f = open('problem11.txt', 'r')
	A = []
	line = f.readline()
	while (line != ''):
		numbers = line.split(' ')
		numbers = [int(n) for n in numbers]
		print numbers
		A.append(numbers)
		line = f.readline()
	f.close()

	n = len(A)
	m = 4
	max_number = 0
	# going horizontally
	for row in A:
		product = 1
		for i in range(m):
			product *= row[i]
		max_number = max(max_number, product)
		for i in range(1, n - m):
			product = product * row[i+n-1]/row[i - 1]
			max_number = max(max_number, product)
	# going vertically
	for col in range(n):
		product = 1
		for i in range(m):
			product *= row[i][col]
		max_number = max(max_number, product)
		for row in range(1, n - m):
			product = product * A[row+n-1][col]/A[row - 1][col]
			max_number = max(max_number, product)




main()