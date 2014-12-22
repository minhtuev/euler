import re

def match(string):
	prog = re.compile("1\d2\d3\d4\d5\d6\d7\d8\d9")
	result = prog.match(string)
	return result is not None

def main():
	n = int(10203040506070809**0.5) + 2
	incre = 4
	while not(match(str(n**2))):
		n += incre
		if incre == 4:
			incre = 6
		else:
			incre = 4
	print n, (n)**2

main()