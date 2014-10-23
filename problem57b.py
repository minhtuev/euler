from fractions import Fraction

f1 = Fraction(1, 2)

count = 0

for i in range(1000):
	r = 1 + f1
	if len(str(r.numerator)) > len(str(r.denominator)):
		count += 1
		print r
	f1 = Fraction(1, 2 + f1)

print "total count:", count