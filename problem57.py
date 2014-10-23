def gcd(n, m):
	if m % n == 0: return n
	else: return gcd(m % n, n)

class Fraction(object):
	def __init__(self, a = 1, b = 1):
		self.a = a
		self.b = b

	def numerator(self):
		return self.a

	def denominator(self):
		return self.b

	def simplify(self):
		d = gcd(min(abs(self.a), abs(self.b)), max(abs(self.a), abs(self.b)))
		self.a /= d
		self.b /= d

	def __add__(self, other):
		if type(other).__name__ != Fraction.__name__:
			other = int(other)
			other = Fraction(other, 1)
		result = Fraction(self.a*other.b + other.a*self.b, self.b*other.b)
		result.simplify()
		return result

	def __sub__(self, other):
		if type(other).__name__ != Fraction.__name__:
			other = int(other)
			other = Fraction(other, 1)
		result = Fraction(self.a*other.b - other.a*self.b, self.b*other.b)
		result.simplify()
		return result

	def __rsub__(self, other):
		return Fraction(int(other), 1) - self

	def __radd__(self, other):
		return self + other

	def __str__(self):
		return str(self.a) + "/" + str(self.b)

f1 = Fraction(1, 3)
f2 = Fraction(1, 12)
print f2 - 1
print gcd(20, 95)
