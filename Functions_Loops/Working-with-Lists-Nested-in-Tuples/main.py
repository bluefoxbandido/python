post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])

# Guide to slices in Python Tuples
post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')
print(post[1::2])

# Three ways to Remove Elements from a Python Tuple

# # REmoving Elements from beginning
# post = post[1:]
# print(post)
# # Removing Elements from end
# post = post[:-1]
# print(post)

# Removing specific Element
post = list(post)
post.remove('published')
post = tuple(post)
print(post)

#How to use a Tuple as a Dictionary Key in Python
priority_index = {
	(1, 'premier'): [1, 34, 12],
	(1, 'mvp'): [84, 22, 24],
	(2, 'standard'): [93, 81, 3],
}
print(list(priority_index.keys()))

# Guide to Python's Zip FUnction
positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)
print(list(scoreboard))

# Introduction to the Python Set Data Structure
tags = {'python', 'coding',	'tutorials', 'coding'}

# print(tags)

#nope
# print(tags[0])
print(tags)
query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)

# Various Methods for Mergin Python Sets
tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# Merged Tags
merged_tags = tags_one | tags_two
print(merged_tags)

# tags in tags_one but not in tags_two 
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

# tags in two but not one
exclusive_to_tag_two = tags_two - tags_one
print(exclusive_to_tag_two)

# tags found in both
universal_tags = tags_one & tags_two
print(universal_tags)