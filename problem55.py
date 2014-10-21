# can be 
def is_palindromic(n):
	n = str(n)
	for i in range(len(n)/2):
		if n[i] != n[len(n) - 1 - i]:
			return False
	return True

def reverse(n):
	n = str(n)[::-1]
	return int(n)

# use caching and recursive definition
def calculate(n, dic = {}, step = 0):
	if not(n in dic):
		m = n + reverse(n)
		if is_palindromic(m):
			dic[n] = 1
		elif step <= 50:
			dic[n] = 1 + calculate(m, step = step + 1)
		else:
			dic[n] = float("inf")
		dic[reverse(n)] = dic[n]
	return dic[n]

count = 0
for i in range(1, 10001):
	if calculate(i) == float("inf"):
		print i
		count += 1
print "number of lychel nums:", count