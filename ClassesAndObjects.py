# Objects: encapsulation of variables and and functions in a single entity
class MyClass:
    variable = 'something'
    
    def function(self):
        print('This is a message inside the class.') 

# assigning objects
my_object_x = MyClass()
my_object_y = MyClass()

my_object_y.variable = 'something different' # changes the field of the object

# accessing object variables
print(my_object_x.variable)
print(my_object_y.variable)

# accessing object functions
my_object_x.function()

# "__init__()" function is used for assigning values in the class
class NumberHolder:
    
    def __init__(self, number):
        self.number = number
        
    def getnumber(self):
        return self.number
        
numberholder = NumberHolder(3)
value = numberholder.getnumber()
print(value)

# Exercise
"""
We have a class defined for vehicles. Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be
a blue van named Jump worth $10,000.00.
"""

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = 'Fer'
car1.color = 'red'
car1.value = 60000.0
car2 = Vehicle()
car2.name = 'Jump'
car2.color = 'blue'
car2.value = 10000.0
# test code
print(car1.description())
print(car2.description())