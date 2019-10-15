def greeting(name = 'Guest'):
	print(f'Hi {name}')

greeting()

def some_function(collection = []):
	collection.append(1)
	return collection

print(some_function())

# Other part of program
print(some_function())

# How to Utilize Named Function Arguments in Python
def full_name(first, last):
	print(f'{first} {last}')
full_name(first = 'Adam', last = 'Parker')

def greeting(*args):
	print('Hi ' + ' '.join(args))


greeting('Adam', 'Parker')

# Lambda Functions in Python
"""
A tool used to wrap up functions. You can treat functionslike any other 
object. A lambda allows you to wrap up a process. 

"""
full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))