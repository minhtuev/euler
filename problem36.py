n = bin(20)
print n

def get_binary(n):
	return bin(n)[2:]

def is_palindromic(s):
	for i in range(len(s)/2 + 1):
		if s[i] != s[len(s) - 1 -i]:
			return False
	return True

sum_numbers = 0

for i in range(1, 1000000):
	if is_palindromic(str(i)) and is_palindromic(get_binary(i)):
		print i
		sum_numbers += i

print "sum:", sum_numbers