def triangle(n):
	return n*(n + 1)/2

def square(n):
	return n*n

def penta(n):
	return n*(3*n - 1)/2

def hexa(n):
	return n*(2*n - 1)

def hepta(n):
	return n*(5*n - 3)/2

def octa(n):
	return n*(3*n - 2)

def is_cyclic(u, v):
	u = str(u)
	v = str(v)
	if u[2:] == v[:2]:
		return True
	return False

def generate_list(f, max_value = 200):
	L = []
	for n in range(max_value):
		if f(n) < 10000:
			if f(n) >= 1000:
				L.append(f(n))
		else:
			break
	return L

L3 = generate_list(triangle)
#print L3
L4 = generate_list(square)
#print L4
L5 = generate_list(penta)
#print L5
L6 = generate_list(hexa)
#print L6
L7 = generate_list(hepta)
#print L7
L8 = generate_list(octa)
#print L8

L = [L3, L4, L5, L6, L7, L8]
check = [False]*6

def compute(current_index, num_list):
	prev = num_list[-1]
	if len(num_list) < 5:
		for index in range(6):
			if check[index] == False:
				check[index] = True
				for n in L[index]:
					if is_cyclic(prev, n) and not(n in num_list):
						num_list.append(n)
						compute(index, num_list)
						num_list.remove(n)
				check[index] = False
	else:
		for index in range(6):
			if check[index] == False:
				check[index] = True
				for n in L[index]:
					if not(n in num_list) and is_cyclic(prev, n) and is_cyclic(n, num_list[0]):
						num_list.append(n)
						print "the cyclic six are:", num_list
						print "the sum:", sum(num_list)
						num_list.remove(n)
				check[index] = False

check[0] = True
for n in L3:
	compute(0, [n])
