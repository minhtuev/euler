L = []
dic = {}

for i in range(2, 100):
	r = i
	for prime in L:
		if r % prime == 0:
			count = 0
			while r % prime == 0:
				count += 1
				r = r / prime
			dic[prime] = max(dic[prime], count)
		if r == 1:
			break
	# r must be a prime
	if r > 1:
		L.append(r)
		dic[r] = 1
S = 1
for prime in L:
	print prime, dic[prime]
	S *= prime**dic[prime]

print S