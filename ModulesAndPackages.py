# Modules example import the Person class from module.py
from module import Person

# example of importing the distance function from module.py
from module import distance

# example of importing all objects form module.py (redundent for example purpose)
from module import *

# using the imported module to define three people
mom = Person('Mom', 59, 'she/her', None)
dad = Person('Dad', 59, 'he/him', None)
jay = Person('Jay', 19, 'he/him', [mom, dad])

# Packages is like a module exept it can have other modules. It is a colection of modules

# main function 
def main():
    # we can now use methods defined inside the Person class
    jay.print_reletives()
    mom.add_relative(jay)
    dad.add_relative(jay)
    mom.print_reletives()
    m = distance(1, 3, 5, 6)
    print(m)

# What is the "__name__"? It is a special variable which gets its value depending on how 
# we execute the containing script.
# What is "__main__"? is the name of the environment where top-level code is run
if __name__ == "__main__":
    main()
    
# Exercise
# In this exercise, print an alphabetically sorted list of all the functions in the re module
# containing the word find.
import re

# dir(module) prints all the functions in the module
# help(module.funct) prints what the sepcific function does

# Your code goes here
find_member = []
for function in dir(re):
    if 'find' in function:
        find_member.append(function)
print(sorted(find_member))