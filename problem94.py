def triangle_area(a, b, c):
	s = (a + b + c)/2.0
	return 	(s*(s - a)*(s - b)*(s - c))**0.5

def main():
	max_value = 10**9
	a = 3
	perimeter = 0
	while (3*a + 1) <= max_value:
		r = ((3*a + 1)*(a - 1))**0.5
		if (r.is_integer()):
			area = (a + 1)*r/4
			print a, a, a + 1, area
			perimeter += (3*a  + 1)
		a += 2
	print perimeter

main()