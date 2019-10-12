# __________________________________________________________________________________
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Overview				------------------------------------------------------------
players = {
	"SS": "Correa",
	"2B": "Altuve",
	"3B": "Bregman",
	"DH": "Gattis",
	"OF": "Springer",
}

second_base = players['2B']
designated_hitter = players['DH']
print(second_base)
print(designated_hitter)
#						--------------------------------

# Nested Collections 	--------------------------------
teams = {
	"astros": ["Altuve", "Correa", "Bregman"],
	"angels": ["Trout", "Pujols"],
	"yankees": ["judge", "stanton"]
}
print(teams['astros'][2])
astros = teams["astros"]
angels = teams["angels"]
yankees = teams["yankees"]

print(yankees)
#						--------------------------------

# How to Add Key:Value Pairs to Dictionaries -----------
teams['red sox'] = ['Price', 'Betts']
print(teams)
#						--------------------------------

# Guide to Using the get Function in Python Dictionaries to Configure Fallback Lookup Values
featured_team = teams.get('yankees', 'No featured team')
									# ^^^ ^^^ ^^^ ^^^
print(featured_team)

									# vvv vvv vvv vvv
"""
									if teams['mets']:
									...
									else
									...
"""
print('#						--------------------------------')
#						--------------------------------

# Guide to Python Dictionary View Objects --------------
player_names = list(players.copy().values())
print(players.keys())
print(players.items())
print('     ')
print(player_names)
print(teams)
print('          ')
team_groupings = list(teams.items())
print(team_groupings)

print(team_groupings)
print("------------")
print(team_groupings[1])
print("------------")
print(team_groupings[1][1])
print("------------")
print(team_groupings[1][1][1])
print("------------")
print(list(team_groupings)[1][1][0])
print("------------")
print(team_groupings[1][0][1][0])
"""
[
	"astros": ["Altuve", "Correa", "Bregman"],
	"angels": ["Trout", "Pujols"],
	"yankees": ["judge", "stanton"]
	'red sox': ['Price', 'Betts']
]
"""
#						--------------------------------

#						--------------------------------
# Overview of the Multiple Methods for Deleting Items ina Python Dictionary
# del teams['mets']

# print(teams.get('mets', 'No team found by that name'))
teams.pop('astros', 'No team found by that name')
print(teams)
#						--------------------------------

#Guide to Working with Lists of Nested Dictionaries
teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])
#						--------------------------------

# Weighted Lottery Function ----------------------------
print('Weighted Lottery Function')
import random
weights = {
	'winning': 1,
	'losing': 10
}
weighted_colors = {
	"red": 1,
	"blue": 2,
	"green": 3
}
# def weighted_lottery(collection):
# 	#Code goes here
# 	for weight in collection:
# 		collection_copy = []
# 		collection_copy.append((collection[weight]) * len(collection))
# 	generated_value = random.randint(0, len(collection_copy))

# 	return collection_copy[generated_value][0] #one random value
def weighted_lottery(collection):
	keys = list(collection.keys())
	random_seed = []
	
	for key in keys:
		for count in range(collection[key]):
			random_seed.append(key)
	
	random_value = random.choice(random_seed)
	
	return random_value

for count in range(11):
	print(weighted_lottery(weights))
print(weighted_lottery(weighted_colors))

# Instructor solution two
import numpy as np
def weighted_solution(weights):
	container_list = []
	for (name, weight) in weights.items():
	#	loop weight amount of times
		for _ in range(weight):
			container_list.append(name)
	return np.random.choice(container_list)
print(weighted_solution(weighted_colors))
#						--------------------------------

# Histogram Excercise	--------------------------------
companies = {
	"Google": 12,
	"Twitter": 8,
	"Facebook": 20,
	"Other": 4
}

def histogram(collection):
	keys = list(collection.keys())
	container = []
	for key in keys:
		container.append([key[0] + ': ' + '$'* collection[key]])
	return container
print(histogram(companies))
#						------------------------------------------------------------
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# __________________________________________________________________________________