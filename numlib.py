def gcd(a, b, dic = {}):
	if not((a, b) in dic):
		if b % a == 0:
			dic[(a, b)] = a
		else:
			dic[(a, b)] = gcd(b % a, a)
	return dic[(a, b)]