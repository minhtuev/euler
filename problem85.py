from utilities import memoize

@memoize
def count_square(w, h):
	if w == 1 and h == 1:
		return 1
	elif w == 1:
		return count_square(w, h - 1) + h
	elif h == 1:
		return count_square(w - 1, h) + w
	else:
		return count_square(w, h - 1) + count_square(w - 1, h ) + h*w - count_square(w - 1, h - 1)

# exist analytical solution = a(a+1)b(b+1)/4
def main():
	h = 1
	w = 1
	target = 2000000
	while count_square(w, h) < target:
		w += 1
	max_range = w
	max_number = 0
	for h in range(1, max_range):
		for w in range(1, max_range):
			if count_square(w, h) < target and count_square(w, h) > max_number:
				max_number = count_square(w, h)
				print max_number, w, h

main()