import math

# This is a test module that we will import into ModulesAndPackages.py to demonstrate how to use
# and create modules
class Person:
    """Class represents a person
    . . .
    Attributes
    ----------
    name : str
        the name of the person
    age : int
        the age of the person
    pronouns : str
        the pronouns the person identifies with
    relatives : list of Person
        list of all relatives to the person
    . . .
    Methods
    -------
    add_relatives(other)
        adds a person to list of relatives. Throws an error if passed a object
        that is not a Person
    print_relatives()
        prints the names of all the relatives for the Person
    
    """
    def __init__(self, name: str, age: int, pronouns: str, relatives: list):
        self.name = name
        self.age = age
        self.pronouns = pronouns
        if relatives is None:
            self.relatives = []
        else:
            for people in relatives:
                if not (isinstance(people, Person)):
                    raise TypeError('The list of relatives contains a object that is not a Person')
            self.relatives = relatives
    
    #  The purpose of __repr__ is to provide a representation of the object that, when passed to the eval
    #  function, would create an object that is equal to the original. Like Java's equal statement
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, pronouns={self.pronouns}, relatives={[r.name for r in self.relatives]})"
    
    # adds a relative to the list of relatives
    def add_relative(self, person):
        if not (isinstance(person, Person)):
            raise TypeError("not given a Person as a parameter")
        self.relatives.append(person)

    # prints all the names of the reletives. if list is empty prints 'no reletives'    
    def print_reletives(self):
        print("%s's relatives are: " % self.name, end="")
        print([relative.name for relative in self.relatives])

# returns the distance between two points
def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)