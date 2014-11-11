f = open('problem66.txt', 'r')

line = f.readline()
max_number = -1
while (True):
	line = f.readline()
	if line == '':
		break
	else:
		L = line.split(' ')
		L = [int(x) for x in L]
		if L[1] > max_number:
			max_number = L[1]
			print L

f.close()