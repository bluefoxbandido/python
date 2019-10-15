# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# <= Less than
# <= Less than or equal to

username = 'jonsnow'

if username != 'jonsnow':
	print('Welcome')
else:
	print('You know nothing Jon Snow!')

user_list = ['Kristine', 'Tiffany']
second_list = ['Jordan', 'Brayden']

if user_list == second_list:
	print('They Match')
else:
	print('They don\'t match')

# How to Check if a Value is Included in a Python String or List
sentence = 'The quick brown fox jumped over the lazy dog'
word = 'quick'

if word in sentence:
	print('The word was found in the sentence')
else:
	print('The word was not found in the sentence')

nums = [1, 2, 3, 4]

if 3 in nums:
	print('The number was found')
else:
	print('The number was not found')

# Compound Conditionals 
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
	print('Access Permitted')
else: 
	print('You shall not pass!')
