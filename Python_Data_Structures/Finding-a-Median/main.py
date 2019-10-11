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
	median_object = sale_prices[math.ceil((len(sorted_list))/2)]
	return median_object

print(median(sale_prices))
