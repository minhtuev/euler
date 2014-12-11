from sort import PriorityQueue

def main():
	A = []
	f = open('p081_matrix.txt', 'r')
	line = f.readline()
	while (line != ''):
		numbers = line.split(',')
		numbers = [int(n) for n in numbers]
		A.append(numbers)
		print numbers
		line = f.readline()
	f.close()

	n = len(A)
	pq = PriorityQueue()
	dic = {}
	pq.push((0,0), A[0][0])
	destination = (n - 1, n - 1)
	(distance, positions) = pq.pop()
	dic[positions] = True
	while (positions != destination):
		(row, col) = positions
		print positions
		if row > 0 and not((row - 1, col) in dic):
			pq.push_or_update_min((row - 1, col), distance + A[row - 1][col])
		if col > 0 and not((row, col - 1) in dic):
			pq.push_or_update_min((row, col - 1), distance + A[row][col - 1])
		if row < n - 1 and not((row + 1, col) in dic):
			pq.push_or_update_min((row + 1, col), distance + A[row + 1][col])
		if col < n - 1 and not((row, col + 1) in dic):
			pq.push_or_update_min((row, col + 1), distance + A[row][col + 1])
		(distance, positions) = pq.pop()
		dic[positions] = True	
	print "distance:", distance

main()