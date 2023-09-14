"""
Description: To demonstrate collections in python.
Author: Donwin Lacdao
Date: September 13, 2023
Usage: CLick the play button
"""

# lists
monday = 10000.01
tuesday = 2000
#...etc..

daily_step_count = [10343, 9385, 7029, 10931, 5921]
employee_data = ["A123", 55596.01, 44, True]

list_of_lists = [["A", "B", "C"], [True, 12], 55] 

print(daily_step_count[2])
daily_step_count[4] = 9999
print(daily_step_count)

daily_step_count.append(10000)
daily_step_count.insert(3, 8888)
print(daily_step_count)

daily_step_count.remove(8888)
print(daily_step_count)

popped = daily_step_count.pop()
print(popped)
print(daily_step_count)


#[10343, 9385, 7029, 10931, 9999]
daily_step_count.sort()
print(daily_step_count)

daily_step_count.reverse()
print(daily_step_count)

ascending = sorted(daily_step_count)
print(ascending)
print(daily_step_count)

print(daily_step_count[2])

# slicing : splits a list
# start: default is position 0 
# stop: default at the end 
# step: default 1 step 
red_river_string = "RRC Polytechnic"
red_river_list = list(red_river_string)

print(red_river_list)
# ['R', 'R', 'C', ' ', 'P', 'o', 'l', 'y', 't', 'e', 'c', 'h', 'n', 'i', 'c']
print(red_river_list[2: 12: 2]) # C P l t c 

print(red_river_list[: 10: 1])

print(red_river_list[5: : 3]) # o t h c

print(red_river_list[-1])

#RRC Polytechnic
print(red_river_list[-1: -5: -1])


# Tuples
# ordered, immutable
# rounded, brackets 
provinces = ('BC', 'AB', 'MB', 'SK')
manitoba = ('mb')
print(type(provinces))
print(type(manitoba))
manitoba = ('mb',)
print(type(manitoba))

provinces = 'BC', 'AB', 'MB', 'SK'
print(type(provinces))

# provinces[2] = "Manitoba"

random_tuple = (1, 66, 2, 12, 32, -2, 54)

maximum = max(random_tuple)
print(maximum)

print(min(random_tuple))

print(sum(random_tuple))

name = "John"
tuple_name = tuple(name)
print(tuple_name, type(tuple_name))

list_of_numbers = [1, 2, 3]

tuple_of_numbers = tuple(list_of_numbers)


# Dictionaries 
# unordered
# mutable
# key, value pairs
# {}

fruit_dictionary = {'apples': 23, 'oranges': 10, 'bananas' : 59}

print(fruit_dictionary['oranges'])

fruit_dictionary['oranges'] = 100
print(fruit_dictionary['oranges'])

fruit_dictionary['pears'] = 12

print(fruit_dictionary)

fruit_dictionary['apple'] = 10

print(fruit_dictionary)


print(fruit_dictionary.keys())
print(fruit_dictionary.values())

# print(fruit_dictionary['orange'])

print(fruit_dictionary.get('oranges', 'does not exist'))

fruit_dictionary.pop('oranges')

print(fruit_dictionary)

fruit_dictionary.clear()
print(fruit_dictionary)

# set
# unordered 
# mutable
# values must be unique 
# {}

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# fives = {} <--- this would create an empty dictionary 
fives = set()

print(primes, type(primes))
print(fives, type(fives))

primes.add(29)
print(primes)

primes.add(2)
print(primes)

fives.add(5)
fives.add(10)

primes.remove(3)
#primes.remove(10)

primes.discard(11)
primes.discard(20)

print(primes)
fives.add(15)
fives.add(20)
# fives.add({25,30}) <-- can't do this

print(primes)   
print(fives)

# {2, 5, 7, 13, 17, 19, 23, 29}        
# {10, 20, 5, 15}

union_of_sets = primes.union(fives)
print(union_of_sets)

intersection_of_sets = primes.intersection(fives)
print(intersection_of_sets)

primes_difference = primes.difference(fives)
print(primes_difference)

fives_difference = fives.difference(primes)

print(fives_difference)

