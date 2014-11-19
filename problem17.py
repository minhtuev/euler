from NumToWordsLib import numToWords
from string import ascii_lowercase

def count_letter(s):
	count = 0
	for char in s:
		if char in ascii_lowercase:
			count += 1
	return count

def main():
	count = 0
	for i in range(1, 1000 + 1):
		s = numToWords(i)
		print i, s
		count += count_letter(s)		
	print "count:", count

main()
print count_letter(numToWords(115))
print count_letter(numToWords(342))

