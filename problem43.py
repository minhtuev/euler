def generate_permutations(s):
	if len(s) == 1:
		return [s]

	L = []
	for index in range(len(s)):
		r = list(s)
		c = r[0]
		r[0] = r[index]
		r[index] = c
		r = ''.join(r)
		for p in generate_permutations(r[1:]):
			L.append(r[0] + p)
	return L

s = 0
for n in generate_permutations('0123456789'):
	m = []
	for i in range(1, 8):
		m.append(int(n[i:i+3]))
	d = [2, 3, 5, 7, 11, 13, 17]
	has_property = True
	for i in range(len(m)):
		if m[i] % d[i] != 0:
			has_property = False
			break
	if has_property:
		print n
		s += int(n)

print "total sum:", s