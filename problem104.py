from numlib import is_pan_digital, fibonacci

f = fibonacci()
(value, index) = f.next()

while (value < 100000000):
	(value, index) = f.next() 

s = str(value)
while is_pan_digital(s[:9]) == False or is_pan_digital(s[len(s)-9:]) == False:
	(value, index) = f.next()
	s = str(value)
	if index % 100 == 0:
		print index

print value, index