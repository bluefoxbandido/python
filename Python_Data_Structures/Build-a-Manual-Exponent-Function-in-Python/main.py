# import operator
from functools import reduce

# def exponent(base, power):
# 	counter = 0
# 	while counter < (power - 1):
# 		counter += 1
# 		base *= base
# 	return base
# print(exponent(9, 2))

# base_list = {}


# def exponent_calc(base, power):
# 	operators = {
# 		"*": operator.mul
# 	}
# 	counter = 0
# 	while counter < power:
# 		base_list[counter] = base
# 		counter += 1
# 		return base_list
	
# 	return reduce(lambda x, y: operators["*"](x, y), base_list)

# print(base_list)

# def manual_exponent(num, exp):
# 	counter = exp -1
# 	total = num
# 	while counter > 0:
# 		total *= num
# 		counter -= 1
# 	return total

# print(manual_exponent(2, 3))
# print(manual_exponent(10, 2))


def manual_exponent(num, exp):
	computed_list = [num] * exp
	def reducer_function(total, element):
		return total * element
	return reduce(reducer_function, computed_list)
print(manual_exponent(7, 3))
print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

def some_function(total, element):
	return total * element

