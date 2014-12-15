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
		for col in range(m):
			product *= row[col]
		max_number = max(max_number, product)
		for col in range(1, n - m):
			if row[col - 1] != 0:
				product = product * row[col+m-1]/row[col - 1]
			else:
				product = 1
				for new_col in range(col, col+m):
					product *= row[new_col]
			max_number = max(max_number, product)

	# going vertically
	for col in range(n):
		product = 1
		for row in range(m):
			product *= A[row][col]
		max_number = max(max_number, product)
		for row in range(1, n - m):
			if A[row - 1][col] != 0:
				product = product * A[row+m-1][col]/A[row - 1][col]
			else:
				product = 1
				for new_row in range(row, row+m):
					product *= A[new_row][col]
			max_number = max(max_number, product)

	# going diagonally in one direction
	for row in range(0, n - m):
		for col in range(0, n - m):
			product = 1
			for index in range(m):
				product *= A[row + index][col + index]
			max_number = max(max_number, product)

	# going diagonally in the other direction
	for row in range(m - 1, n):
		for col in range(m - 1, n):
			product = 1
			for index in range(m):
				product *= A[row - index][col - index]
			max_number = max(max_number, product)

	print "max number", max_number

main()