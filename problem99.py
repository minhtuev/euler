from math import log

def main():
	f = open('p099_base_exp.txt', 'r')
	max_value = 0
	max_line = 0
	line_number = 1

	line = f.readline()
	while (line != ''):
		numbers = line.split(',')
		base = float(numbers[0])
		expo = float(numbers[1])
		if (expo*log(base) > max_value):
			max_value = expo*log(base)
			max_line = line_number
			print base, expo, max_line
		line = f.readline()
		line_number += 1
	f.close()

main()


