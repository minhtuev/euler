import pprint

def main():
	f = open('p081_matrix.txt', 'r')
	A = []
	line = f.readline()
	while (line != ''):
		numbers = line.split(',')
		numbers = [int(n) for n in numbers]
		A.append(numbers)
		line = f.readline()
	f.close()

	n = len(A)
	R = []
	for i in range(n):
		R.append([0]*n)

	R[0][0] = A[0][0]
	for i in range(1, n):
		R[0][i] = R[0][i - 1] + A[0][i] 

	for i in range(1, n):
		for j in range(n):
			if j == 0:
				R[i][0] = A[i][0] + R[i - 1][0]
			else:
				R[i][j] = min(R[i - 1][j], R[i][j - 1]) + A[i][j]

	for i in range(n):
		print R[i]
	print R[n - 1][n  - 1]
main()