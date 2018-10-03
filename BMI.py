def main():
	weight = float(input("Enter your weight pounds: "))
	height = float(input("Enter your height in inches: "))
	
	bmi = weight * 703 / (height * height)
	print(bmi)
	
main()
