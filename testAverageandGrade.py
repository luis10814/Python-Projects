def main():
	
	test1 = int(input("Enter test score 1: "))
	test2 = int(input("Enter test score 2: "))
	test3 = int(input("Enter test score 3: "))
	test4 = int(input("Enter test score 4: "))
	test5 = int(input("Enter test score 5: "))
	
	calc_average(test1, test2, test3, test4, test5)
	
def calc_average(t1, t2, t3, t4, t5):
	
	average = t1 + t2 + t3 + t4 + t5
	average = average / 5
	
	determine_grade(average)
	
def determine_grade(x):
	
	if x < 60:
		print("F")
	elif x > 59 and x < 70:
		print("D")
	elif x > 69 and x < 80:
		print("C")
	elif x > 79 and x < 90:
		print("B")
	elif x > 89 and x < 100:
		print("A")
		
main()
