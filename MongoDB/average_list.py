num_list = [1, 2, 3, 4, 5, 6]


def average_tool(collection):
    num_sum = 0
    for num in collection:
        num_sum += num
    dividend = len(collection)
    average = num_sum/dividend
    return average

print(average_tool(num_list))   

from functools import reduce
def average_reducer(collection):
    collection_total = reduce(lambda total, iterate : total + iterate, collection)
    average = collection_total / (len(collection))
    return average

print(average_reducer(num_list))