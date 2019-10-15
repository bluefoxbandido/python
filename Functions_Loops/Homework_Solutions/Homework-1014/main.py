"""
Homework!

	Create a small guessing game in python! This game will be inside of a function. When the function is called, pass in a number that must be guessed. A user can then input guesses into the console, and the game will tell them if they are right or wrong. Keep the function going until they guess correctly.

		Requirements:
			- Functions
			- Looping
			- Conditionals

"""

def guessing_game(number_choice):
	while True:
		print('Choose a number')
		guess = input()

		if guess == number_choice:
			print('Correct')
			break
		else:
			print('No, {guess} is incorrect')
guessing_game("42")