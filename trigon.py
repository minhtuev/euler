# https://projecteuler.net/problem=68
L = range(1, 7)
dic = {}
count = 0
for value in L:
	dic[value] = False
for A in L:
	dic[A] = True
	for B in L:
		if dic[B] == True:
			continue
		dic[B] = True
		for C in L:
			if dic[C] == True:
				continue
			dic[C] = True
			for D in L:
				if (D > A) and (D < B + A):
					if dic[D] == True:
						continue
					dic[D] = True
					E = A + B - D
					if E in L and E < A + C:
						dic[E] = True
						F = A + C - E
						if F in L and dic[F] == False and F > A:
							print A, B, C, D, C, E, F, E, B, "sum:", A + B + C
							count += 1
						dic[E] = False
					dic[D] = False
			dic[C] = False
		dic[B] = False
	dic[A] = False
print "num solution:", count