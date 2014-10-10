count = 0

# notice the recursive definition, we can prove that 
# there are no more than 11 such numbers.

def is_prime(n, L = [2], dic = {1:False, 2:True}):
	if not(n in dic):
		for u in L:
			if (n % u) == 0:
				dic[n] = False
				return False
			if u**2 > n:
				break
		L.append(n)
		dic[n] = True
	return dic[n]

for i in range(2, 11):
	print i, is_prime(i)

def left_truncatable(n):
	s = str(n)
	for i in range(len(s)):
		m = int(s[i:])
		if not(is_prime(m)):
			return False
	return True

def right_truncatable(n):
	while (n > 0):
		if not(is_prime(n)):
			return False
		n = n / 10
	return True

count = 0
n = 11
total_sum = 0
while (count < 11):
	if is_prime(n) and right_truncatable(n) and left_truncatable(n):
		print "truncatable prime:", n
		count += 1
		total_sum += n
	n += 1
print "total sum:", total_sum