from numlib import get_proper_divisor

def get_amicable_numbers(number, max_value = 10**6):
	L = [number]
	next_number = sum(get_proper_divisor(number))
	while next_number not in L  and next_number <= max_value:
		L.append(next_number)
		next_number = sum(get_proper_divisor(next_number))
	return (next_number, L)


def main():
	max_value = 10**6
	dic = {}
	min_number = None
	max_length = 0

	for number in range(1, max_value+1):
		if number not in dic:
			(next_number, L) = get_amicable_numbers(number, max_value)
			if next_number == number:
				for value in L:
					dic[value] = True				
				if len(L) == max_length:
					min_number = min(min_number, min(L))
				elif len(L) > max_length :
					min_number = min(L)
					max_length = len(L)
					print number, min_number, max_length, L
					print "---"

main()