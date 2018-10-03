def main():
	maximum()


def maximum():
	num1 = int(input("Enter an integer: "))
	num2 = int(input("Enter another integer: "))
	
	if num1 > num2:
		print(num1, "is larger!")
	else:
		print num2, "is larger"

main()
