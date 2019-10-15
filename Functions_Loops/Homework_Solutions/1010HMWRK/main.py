"""
Homework!

1) Write a Python program to get the smallest number from a list.
    Example: [4, 6, 18, 3, 7]
    Result: 3

2) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    Example: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Result: ['Green', 'White', 'Black']

3) Write a Python program that accepts a comma separated STRING of words and prints them in alphabetical order.
    Example: "red, white, black, green"
    Expected Result : "black, green, red, white"
"""

# Solution 1
example = [4, 6, 18, 3, 7]

def smallest(collection):
	sorted_list = sorted(collection)
	return sorted_list[0]

print(smallest(example))
print(example)

#Solution 2
example2 = [4, 6, 18, 3, 7, 8]

def splicer_function(collection):
	del collection[5]
	del collection[4]
	del collection[0]
	return collection

print(splicer_function(example2))

example2 = [4, 6, 18, 3, 7, 8]
def pop_splice(collection):
	splice_copy = collection.copy()
	splice_copy.pop()
	splice_copy.pop()
	del splice_copy[0]
	return splice_copy
print(pop_splice(example2))


#Solution 3
example3 = "red,white,black,green"
def seperator(string):
	collection = string.split(',')
	collection.sort()
	sorted_string = ", ".join(collection)
	return sorted_string
	
print(seperator(example3))
