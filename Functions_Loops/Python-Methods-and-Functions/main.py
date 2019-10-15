def color_changer(string):
	string = 'pink'
	return string

print(color_changer('blue'))

def full_name(first, last):
	print(f'{first} {last}')

full_name('adam', 'parker')

def auth(email, password):
	if email == 'adam@parker.com' and password == 'secret':
		print('authorized')
	else:
		print('Not authorized')

auth('adam@parker.com', 'secret')

def hundred(max_value):
	for num in range(1, max_value, 2):
		print(num)


# hundred(280)
