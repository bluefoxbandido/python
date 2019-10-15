"""
Homework!
"""
"""
1) Write a Python program to count the number of characters (character frequency) in a string.
    Example: "google.com"
    Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
def char_count_one(string):
	container = {}
	for char in string:
		if char in container:
			container[char] += 1
		else:
			container[char] = 1
	return container

print(char_count_one('google.com'))

from collections import Counter
def char_count_two(string):
	container = Counter(string)
	return container

print(char_count_two('the quick brown fox jumped over the lazy dog'))

def char_count_three(string):
	container = {}
	for chars in string:
		container[chars] = container.get(chars, 0) + 1
	return container

print(char_count_three('i really hope this one works'))

"""
2) Write a Python program to sum all the values in a dictionary.
    Example: {"google": 12, "facebook": 20, "twitter": 8, "other": 4}
    Result: 44
"""
def value_sum(collection):
	keys = list(collection.keys())
	value_total = 0
	for key in keys:
		value_total += collection[key]
	return value_total

example = {"google": 12, "facebook": 20, "twitter": 8, "other": 4}
print(value_sum(example))

"""
3) Write a python program that takes an integer and squares every digit.
    Example: 2345
    Result: 491625
"""
def digit_rooter(original_number):
	digit_string_list = []
	digit_string_list.extend(str(original_number))
	digit_product_list = []
	for digit in digit_string_list:
		digit_product_list.append((int(digit)**2))
	string_product = ''
	for digit in digit_product_list:
		string_product += str(digit)
	return string_product
print(digit_rooter(2345))

# container = []
# container.extend(str(2345))
# print(container)

# num_convert = int(container[0])
# print(num_convert)
# test_run = '2'
# print(int(test_run))