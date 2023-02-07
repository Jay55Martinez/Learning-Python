# This is a test module that we will import into ModulesAndPackages.py to demonstrate how to use
# and creat modules
class Person:
    """Class represents a person with a given name, age, pronouns and a list of People that
    are their reletives"""
    def __init__(self, name: str, age: int, pronouns: str, relatives=None):
        self.name = name
        self.age = age
        self.pronouns = pronouns
        if relatives is None:
            self.relatives = []
        else:
            self.relatives = relatives
    
    #  The purpose of __repr__ is to provide a representation of the object that, when passed to the eval
    #  function, would create an object that is equal to the original. Like Java's equal statement
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, pronouns={self.pronouns}, relatives={[r.name for r in self.relatives]})"
    
    # adds a relative to the list of relatives
    def add_ralative(self, person):
        self.relatives.append(person)

    # prints all the names of the reletives. if list is empty prints 'no reletives'    
    def print_reletives(self):
        return [relative.name for relative in self.relatives]