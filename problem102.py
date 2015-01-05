
# adapted from here
# http://stackoverflow.com/questions/2049582/how-to-determine-a-point-in-a-triangle

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

def sign(p1, p2, p3):
	return float(p1.x - p3.x)*(p2.y - p3.y) - (p2.x - p3.x)*(p1.y - p3.y)

def point_in_triangle(pt, v1, v2, v3):
	b1 = sign(pt, v1, v2) < 0
	b2 = sign(pt, v2, v3) < 0
	b3 = sign(pt, v3, v1) < 0
	return ((b1 == b2) and (b2 == b3))

def main():
	f =  open('p102_triangles.txt', 'r')
	lines = f.readlines()
	lines = [line.strip() for line in lines]
	lines = [[int(n) for n in line.split(',')] for line in lines]
	count = 0
	origin = Point(0, 0)
	for line in lines:
		(u1, u2, v1, v2, w1, w2) = line
		p1 = Point(u1, u2)
		p2 = Point(v1, v2)
		p3 = Point(w1, w2)
		if point_in_triangle(origin, p1, p2, p3):
			count += 1
	f.close()
	print "count:", count

main()