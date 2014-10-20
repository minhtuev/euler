L = [1, 2, 1]
n = 2

max_level = 100
count = 0
while (n < max_level):
	T = [1]
	for index in range(len(L) - 1):
		s = L[index] + L[index + 1]
		if (s > 1000000):
			s = 1000000
			count += 1
		T.append(s)
	T.append(1)
	L = T
	print T
	n += 1
print "total count:", count