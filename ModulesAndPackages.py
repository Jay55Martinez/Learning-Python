# Modules example import module.py
from module import Person

# using the imported module to define three people
mom = Person('Mom', 59, 'she/her', None)
dad = Person('Dad', 59, 'he/him', None)
jay = Person('Jay', 19, 'he/him', [mom, dad])

# main function 
def main():
    # we can now use methods defined inside the Person class
    jay.print_reletives()
    mom.add_relative(jay)
    dad.add_relative(jay)
    mom.print_reletives()

# What is the "__name__"? It is a special variable which gets its value depending on how 
# we execute the containing script.
# What is "__main__"? is the name of the environment where top-level code is run
if __name__ == "__main__":
    main()