max_count = 0
max_p = -1
for p in range(9, 1001):
	count = 0
	for a in range(1, p/3 + 1):
		for b in range(a, (p - a)/2 + 1):
			c = p - a - b
			if c**2 == a**2 + b**2:
				count += 1
				print p, ":", a, b, c
	if count > max_count:
		max_count = count
		max_p = p

print max_count, max_p