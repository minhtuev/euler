def get_str(a, b, c, N):
	return str(a)+ " + (" + str(N) + "^0.5 + " + str(b) + ")/" + str(c) 

def is_perfect_square(N):
	n = int(N**0.5)
	if n**2 == N:
		return True
	return False

def get_notation(N):
	a0 = int(N**0.5)
	b0 = -a0
	c0 = 1
	L = [a0]
	T = []
	T2 = []
	while (True):
		f0 = c0/(N**0.5 + b0)
		a1 = int(f0)
		c1 = (N - b0**2)/c0
		b1 = abs(b0) - c1*a1
		if (a1, b1, c1) in T2:
			break
		T.append(a1)
		T2.append((a1, b1, c1))
		a0 = a1
		b0 = b1
		c0 = c1
	L.append(tuple(T))
	return L

max_number = 10000
count = 0 
for i in range(1, max_number + 1):
	if not(is_perfect_square(i)):
		L = get_notation(i)
		if len(L[1]) % 2 ==1 :
			count += 1
			print i
print "count:", count
