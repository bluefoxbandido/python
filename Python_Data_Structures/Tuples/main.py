"""
List: []
Dictionary: {}
Tuple: ()

Tuples are immutable
"""
post = ('Python Basics', 'Intro Guide to Python', 'Some Cool Python Content')

title, sub_heading, content = post

# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

print(id(post))
post = post + ('published',)
print(id(post))

title, sub_heading, content, status = post
print(title)
print(sub_heading)
print(content)
print(status)