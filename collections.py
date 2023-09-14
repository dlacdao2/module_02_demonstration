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