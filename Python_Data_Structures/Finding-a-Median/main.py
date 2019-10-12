import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

def median(collection):
	sorted_list = sorted(collection)
	num_of_sales = len(sorted_list)
	half_slice = math.floor(num_of_sales/2)
	median = sorted_list[half_slice:(half_slice + 1)]
	return median


print(median(sale_prices))

