import random

def main():
	num = random.randint(0,100)
	
	choice = "Y"
	
	
	while choice == "Y" or choice == "y":
		guess = int(input("Guess A number 1 - 100: "))
	
		if guess == num:
			print("You guessed right!")
		
		elif guess < num:
			print("To low!")
		elif guess > num:
			print("To high")
		
		
		choice = raw_input("Guess again? (Y/N) ")
	
	
main()
