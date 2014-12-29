def main():
	f =  open('p079_keylog.txt', 'r')
	lines = f.readlines()
	lines = [line.strip() for line in lines]
	f.close()

	for line in lines:
		

main()