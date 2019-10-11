"""
Complete the following coding exercises:

1) Write a Python program to calculate the length of a string.
    Example: "Coding"
    Result: 6
"""
string = 'string'
value = len(string)
print(value)

def county_tool_two(string):
	value = string.index(string[-1]) + 1
	return value
print(value)

"""

2) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
    Example: "Python"
    Result: "Pyon"
"""
string = 'string'
segment = string[:2]

def splicer(string):
	first = string[:2]
	second = string[-2:]
	spliced_product = first + second
	return spliced_product

test_run = 'the random string'
print(splicer(test_run))

"""

3) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$'
    Example: "restart"
    Result: "$esta$t"

"""
# string = 'string'
# print(string[0])

# def money_changer(collection):
# 	change_key = string[0]
# 	for char in collection:
# 		product = ''
# 		if char == change_key:
# 			product += '$'
# 		else:
# 			product += char
# 	return product
# print('below')
# guess = 'string'
# print(money_changer(guess))

def string_changer(string_to_change, new_char):
	first_char = string_to_change[0]
	return string_to_change.replace(first_char, new_char)
print(string_changer("restart", "$"))


