def get_ordered_tuple(n):
	L = []
	while n > 0:
		L.append(n % 10)
		n = n / 10
	L.sort()
	return tuple(L)

dic = {}
n = 300
desired_value = 5

while (True):
	triple = n**3
	key = get_ordered_tuple(triple)
	dic[key] = dic.get(key, [])
	dic[key].append(n)
	if len(dic[key]) == desired_value:
		print dic[key]
		print [u**3 for u in dic[key]]
		break
	n += 1
