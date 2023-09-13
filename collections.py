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
