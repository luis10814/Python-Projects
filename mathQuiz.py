import random

def main():
	quiz()
	
def quiz():
	num1 = random.randint(0, 500)
	num2 = random.randint(0, 500)
	answer = num1 + num2
	
	print "What is ", num1, "+", num2
	
	gAnswer = int(input())
	
	if gAnswer == answer:
		print("Correct!")
	else:
		print("Wrong!")
	
main()
