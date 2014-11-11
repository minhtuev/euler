def is_square(n):
	if (int(n**0.5))**2 == n:
		return True
	return False

def find_minimum(D):
	y = 1
	while (True):
		if is_square(1 + D*y**2):
			return (1+D*y**2)**0.5
		y += 1

max_D = -1
for D in range(2, 1001):
	print D
	if not is_square(D):
		m = find_minimum(D)
		if m > max_D:
			print "m=", m, ";D=", D
			max_D = m