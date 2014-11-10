def is_square(n):
	if (int(n**0.5))**2 == n:
		return True
	return False

def find_minimum(D):
	L = []
	for x in range (1, D):
		if (x*x - 1) % D == 0:
			L.append(x)
	index = 0
	while (True):
		x = L[index]
		if (x*x - 1) % D == 0 and is_square((x*x - 1)/D) and x > 1:
			return x
		index += 1
		if index == len(L):
			L = [x + D for x in L]
			index = 0

max_D = -1
for D in range(2, 1001):
	print D
	if not is_square(D):
		m = find_minimum(D)
		if m > max_D:
			print "m=", m, ";D=", D
			max_D = m