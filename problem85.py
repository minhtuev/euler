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
		return count_square(w, h - 1) + count_square(w - 1, h ) - count_square(w - 1, h - 1) + 2

print count_square(3, 2)