# m*(3m - 1) - n*(3n - 1) = k*(3k - 1)
# 3(m^2 - n^2) - (m - n) = 3(m-n)(m+n) - (m-n) = (m-n)(3(m+n)-1 )

def get_number(n):
	return n*(3*n - 1)/2

def is_pentagon(n, m = 0, dic = {}):
	P = get_number(m)
	while (n > P):
		m = m + 1
		P = get_number(m)
		dic[P] = True
	return n in dic

k = 2
D = -1
while (D == -1):
	index = k - 1 
	Pk = get_number(k)
	Pk1 = get_number(k+1)
	Pk0 = get_number(k-1)
	Pj = get_number(index)
	#print "k=", k
	while (index >= 1) and (Pj + Pk >= Pk1) and (Pk - Pj <= Pk0):
		if is_pentagon(Pk - Pj) and is_pentagon(Pk + Pj):
			D = Pk - Pj
			print Pk, Pj
			print "D=", D
			print "k=", k
			print "j=", index
			break
		index -= 1
		Pj = get_number(index)
	k += 1
