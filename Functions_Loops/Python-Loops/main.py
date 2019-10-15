players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
  print(player)

players_two = {
	'2b': 'Altve',
	'3b': 'Bregman',
	'ss': 'Correa',
	'dh': 'Gattis'
}

for position, player in players_two.items():
  print('Position', position)
  print('Player Name', player)

# How to Loop Through the Characters of a Python String
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
	print(letter)

# Guide to looping over ranges
for num in range(1, 10):
	print(num)
for num in range(1, 11, 2):
	print(num)

# Guide to Continue and Break in Python Loops 
usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]
#					||: Continue :||: Break :||
for username in usernames:
	if username == 'cersei':
	# 	print(f'Sorry, {username}, you are not allowed')
	# 	continue
	# else:
	# 	print(f'{username} is allowed')
		print(f'{username} was found at index {usernames.index(username)}')
		break
	print(username)
#

# Overview of While Loops in Python 
nums = list(range(1, 100))
print(nums)

for num in nums:
	print(num)

while len(nums)>0:
	print(nums.pop())

def guessing_game():
	while True:
		print('What is your guess?')
		guess = input()

		if guess == '42':
			print('You correctly guessed it!')
			return False
		else:
			print(f'No, {guess} is not the answer, please try again\n')

guessing_game()

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
	new_customers.append(legacy_customer)
print(new_customers)
