# project euler, problem 46

def is_prime(n, dic = {1:False}):
	if n not in dic:
		dic[n] = True
		for i in range(2, int(n**0.5)+1):
			if (n % i) == 0:
				dic[n] = False
				break
	return dic[n]

def goldbach():
	n = 35
	while (True):
		n += 2
		if is_prime(n) == False:
			m = n - 2
			while (m > 1):
				if is_prime(m):
					k = (n - m)/2
					u = int(k**0.5)
					if u*u == k:
						print n, m
						break
				m = m - 2
			if m == 1:
				print "goldbach fails for:", n
				break
goldbach()


