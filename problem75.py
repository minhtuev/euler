from numlib import is_square

def main():
	max_range = 500000	
	dic = {}
	checked = {}
	max_L = max_range*3
	for a in range(1, max_range + 1):
		b = a + 1
		c2 = a*a + b*b
		c = int(c2**0.5)
		while (b <= max_range) and (a + b + c <= max_L):
			if not ((a, b) in checked):
				if c2 == c*c:
					s = a + b + c
					k = 1
					while (s*k <= max_L):
						dic[s*k] = dic.get(s*k, 0)  + 1
						checked[(a*k, b*k)] = True
						print a*k, b*k, (s - a - b)*k
						k +=1
			b += 2
			c2 = a*a + b*b
			c = int(c2**0.5)
			

	count = 0
	for key in dic:
		if dic[key] == 1:
			count += 1
	print "count:", count

main()