def is_triangle(n, m = 0, dic = {}):
	if not(n in dic) and m*(m+1)/2 < n:
		while m*(m+1)/2 <= n:
			t = m*(m+1)/2
			dic[t] = True
			m += 1
	return n in dic

f = open('p042_words.txt')
s = f.readline()
count = 0
print ord('A')
for word in s.split(','):
	word = word[1:len(word) - 1]
	value = 0
	for c in word:
		value += ord(c) - 64
	if is_triangle(value):
		count += 1
		print word
f.close()

print "total count:", count