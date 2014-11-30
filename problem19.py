from datetime import date, timedelta

def main():
	d = date(1900, 1, 1)
	count = 0
	for year in range(1901, 2001):
		for month in range(1, 13):
			d2 = date(year, month, 1)
			t = (d2 - d)
			if t.days % 7 == 6:
				count +=1 
				print d2

	print "count:", count

main()