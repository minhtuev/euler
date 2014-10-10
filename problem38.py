def is_pandigital(s):
	if len(s) != 9:
		return False
	for i in range(1, 10):
		if s.find(str(i)) == -1:
			return False
	return True

m = 0
base = -1
# note: this problem can be solved with pen and paper by simple consideration
# of the base number
for i in range(1, 40000):
	s = ''
	for j in range(1, 10):
		s += str(i*j)
		if len(s) == 9:
			break
	if len(s) == 9 and is_pandigital(s):
		if int(s) > m:
			m = int(s)
			base = i
			print base, m
