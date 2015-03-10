from numlib import get_prime_list
max_value = 50*10**6
max_prime = int(max_value**0.5)
prime_list = get_prime_list(max_prime)
dic = {}
for a in prime_list:
	S = a**2
	for b in prime_list:
		S2 = S + b**3
		if S2 >= max_value:
			break
		for c in prime_list:
			S3 = S2 + c**4
			if S3 >= max_value:
				break
			if S3 not in dic:
				dic[S3] = True
				print a, b, c, S3
print len(dic), len(prime_list), max_prime