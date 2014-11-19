from numlib import is_prime

def get_concat_numbers(u, v):
	p1 = int(str(u) + str(v))
	p2 = int(str(v) + str(u))
	return (p1, p2)

def is_pair(u, v, dic = {}):
	key = (min(u, v), max(u, v))
	if not(key in dic):
		(p1, p2) = get_concat_numbers(u, v)
		if is_prime(p1) and is_prime(p2):
			dic[key] = True
		else:
			dic[key] = False
	return dic[key]

def is_pairs(pairs, u):
	for v in pairs:
		if not(is_pair(u, v)):
			return False
	return True

def main():
	L = [3, 7]
	R = {3:[(3,7)], 7:[]}
	n = 11
	while (True):
		if (is_prime(n)):
			print n
			for u in L:
				if is_pair(u, n):
					temp = [(u, n)]
					for pairs in R[u]:
						if not(n in pairs) and is_pairs(pairs, n):
							new_pairs = pairs + (n,)
							if len(new_pairs) == 5:
								print new_pairs
								print sum(new_pairs)
								return
							temp.append(new_pairs)
					R[u].extend(temp)
			R[n] = []
			L.append(n)
		n += 2

main()

