"""
Description: Module 02 Demonstration
Author: Donwin Lacdao
Date: September 12, 2023
Usage: Run using the play button in the IDE (Integrated Development Environment). 
"""

# This is an inline comment.


'''
This is a multi-line comment.
It spans over multiple lines.
'''


absolute_value = abs(-12)
print('absolute value:', absolute_value)
print('absolute_value:' + str(absolute_value))
print('absolute value:', abs(-12))

print("I am", '25', "years old!")
print("apples", "oranges", "bannanas", sep = "* ")

# Variables.
name = 'John'
age = 25
pi = 3.14159
number = 123
is_a_student = True 

print(type(name))
print(type(age))
print(type(pi))
print(type(number))
print(type(is_a_student))


# output: My name is John and I am 25 years old.
print(f"My name is {name} and I am {age} years old.")

# output: The value of pi is to two decimal places 3.14
print(f"The value of pi to two decimal places is {pi:.2f}.")

# output: The number is 00123
print(f"The number is {number:05}")

# output: Hello,          John
print(f"Hello, {name:>10}")