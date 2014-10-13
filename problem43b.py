def is_pandigital(n):
	if len(n) == 1:
		return True

	for index in range(len(n) - 1):
		if n[index+1:].find(n[index]) != -1:
			return False
	return True

divisors = [2, 3, 5, 7, 11, 13, 17]
L = []
for d in divisors:
	S = []
	for s in range(10, 1000):
		if (s % d == 0):
			m = str(s)
			if len(m) == 2:
				m = '0' + m
			if is_pandigital(m):
				S.append(m)
	print S
	L.append(S)

numbers = []
def build_strings(L, index = 0, s = ''):
	if index == len(L):
		if is_pandigital(s):
			numbers.append(s)
		return

	if s == '':
		for n in L[index]:
			build_strings(L, index + 1, n)
	else:
		for n in L[index]:
			if s[len(s)-2:len(s)] == n[0:2]:
				build_strings(L, index + 1, s + n[2])

build_strings(L)
total_sum = 0
for number in numbers:
	for c in range(10):
		if number.find(str(c)) == -1:
			m = int(str(c) + number)
			print m
			total_sum += m
print total_sum

