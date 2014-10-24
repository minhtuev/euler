from string import ascii_lowercase, ascii_letters
import enchant

ascii_numbers = '0123456789'
ascii_punctuations = "' ,."
ascii_possible = ascii_lowercase + ascii_numbers + ascii_punctuations

a = 10
b = 2
c= a ^ b
print c
print c ^ b

f = open('p059_cipher.txt')
s = f.readline()
print s
f.close()

d = enchant.Dict("en_US")

def decrypt(L, password):
	m = len(password)
	R = ""
	for index, v in enumerate(L):
		R += str(chr((v ^ ord(password[index % m]))))
	return R

L = [int(c) for c in s.split(',')]
for a in ascii_lowercase:
	if decrypt(L[:1], a)[0] in ascii_possible:
		for b in ascii_lowercase:
			for c in ascii_lowercase:
				password = a + b + c
				s = decrypt(L[:20], password)
				index = 1
				first_word = ''
				# use regex
				while s[index] in ascii_letters:
					first_word += s[index]
					index += 1
				if len(first_word) > 1 and d.check(first_word):
					print "first word:", first_word
					print password, s
print L