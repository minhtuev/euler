dic = {}
L = []
partial_sum = []

def prime(n, dic = {}):
	if not(n in dic):
		for i in range(2, int(n**0.5) + 1):
			if n % i == 0:
				dic[n] = False
				return dic[n]
		dic[n] = True
	return dic[n]

i = 2
max_len = 1
while (i < 1000000):
	is_prime = True
	for u in L:
		if i % u == 0:
			is_prime = False
			break
	if is_prime:
		L.append(i)
		for index, sum_value in enumerate(partial_sum):
			partial_sum[index] = sum_value + i
			if (sum_value + i < 1000000) and (len(partial_sum) + 1 - index) > max_len and prime(sum_value + i):
				print max_len					
				print sum_value + i
				max_len = len(partial_sum) + 1 - index
		partial_sum.append(i)
	i += 1
