def fact(n, dic = {1:1, 0:1}):
	if not(n in dic):
		dic[n] = n*fact(n - 1) 
	return dic[n]

total_sum = 0
for i in range(3, 9999999):
	s = 0
	n = i
	while n > 0:
		d = n % 10
		s += fact(d)
		n = n / 10
	if s == i:
		print s
		total_sum += i

print "total sum:", total_sum