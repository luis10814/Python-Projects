def main():
	month = int(input("Enter a numeric month: "))
	day = int(input("Enter a numeric day: "))
	year = int(input("Enter a two digit year: "))
	
	if month * day == year:
		print("This is a magic date!")
	else:
		print("This is not a magic Date :(")


main()
