lines = [line.strip() for line in open('problem8.txt')]
full_number = ''.join(lines)
print full_number

product =  1
m = 1
for index, c in enumerate(full_number):
	n = int(c)
	if index < 13:
		product *= n
		m = product
	else:
		prev_number = int(full_number[index - 13])
		if prev_number != 0:
			product = product / int(full_number[index - 13]) * n
		else:
			product = 1
			for counter in range(index - 12, index + 1):
				product *= int(full_number[counter])
		m =max (m, product)
print m
