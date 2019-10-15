# num_list = range(1, 11)

# # for num in num_list: 
# # 	cubed_nums.append(num ** 3)
# cubed_nums = [num**3 for num in num_list]

# even_numbers = []

# for num in num_list:
# 	if num % 2 == 0:
# 		even_numbers.append(num)

# even_numbers = [num for num in num_list if num % 2 == 0]
# print(list(num_list))
# print(even_numbers)

"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1> Greeting </h1>
"""
def heading_generator():
	print('Enter Title')
	title = input() 

	print('Enter Heading Type')
	heading_type = input()
	print(f'<h{heading_type}> {title}</h{heading_type}>')

heading_generator()
