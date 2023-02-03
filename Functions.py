# Function with no arguments
def my_function():
    print('Hello World! This is my function. :)')

# Function with arguments
def my_function_args(name, message):
    print('Hi my name is %s, %s' % (name, message))

# Function with return
def sum_two_nums(a, b):
    return a + b

# How to call a function
my_function() # prints Hello World! ...

# How to call a function with arguments
my_function_args('Jay', 'I love Python!') # prints Hi may name is Jay, I love Python!

# How to call a function with a return
x = sum_two_nums(2, 3) # x = 5
print(x) # prints 5

# Exercis
"""
In this exercise you'll use an existing function, and while adding your own to create a
fully functional program.

1. Add a function named list_benefits() that returns the following list of strings: "More 
organized code", "More readable code", "Easier code reuse", "Allowing programmers to
share and connect code together"

2. Add a function named build_sentence(info) which receives a single argument
containing a string and returns a sentence starting with the given string 
and ending with the string " is a benefit of functions!"

Run and see all the functions work together!
"""

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ['More organized code', 'More readable code', 'Easier code reuse', 
            'Allowing programmers to share and connect code together']

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
