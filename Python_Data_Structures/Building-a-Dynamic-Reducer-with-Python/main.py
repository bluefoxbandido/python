import operator
from functools import reduce

# print('-----------------------MY SOLUTION')
# def dynamic_reducer(list_of_numbers, op):
# 	if op == "+":
# 		answer = reduce(lambda x, y: x+y, list_of_numbers)
# 	if op == "-":
# 		answer = reduce(lambda x, y: x-y, list_of_numbers)
# 	if op == "/":
# 		answer = reduce(lambda x, y: x/y, list_of_numbers)
# 	if op == "*":
# 		answer = reduce(lambda x, y: x*y, list_of_numbers)
# 	return answer

# # print(dynamic_reducer([1, 2, 3], "+")) # 6
# # print(dynamic_reducer([1, 2, 3], "-")) # -4

# print(dynamic_reducer([1, 2, 3], '+')) # 6
# print(dynamic_reducer([1, 2, 3], '-')) # -4
# print(dynamic_reducer([1, 2, 3], '*')) # 6
# print(dynamic_reducer([1, 2, 3], '/')) # 0.1666...

# #Instructor Solution
# print("\n")
# print('-----------------------INSTRUCTOR SOLUTION')


def dynamic_reducer(collection, symbol):
	operators = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.truediv
	}
	def reduce_helper(aggregate, iteration):
		for item in collection:
			aggregate = aggregate + iteration
			return aggregate
	return reduce(lambda aggregate, iteration: operators[symbol](aggregate, iteration), collection)
print(dynamic_reducer([1, 2, 3], '/'))



