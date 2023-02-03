# basic logic
x = 2
print(x == 2) # True
print(x == 3) # False
print(x >= 1) # True
print(x < 89) # True

# boolean operators "and" "or"
name = 'Jay'
age = 19
if name == 'Jay' and age == 19:
    print('%s is %d' % (name, age))
if name == 'James' or name == 'Jay':
    print('Your name is Jay or James')

# "in" operator checks to see if specified object is in an interble object container
if name in ['Jay', 'Bill']:
    print('Your name is Jay or Bill')

# if else statements
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# "is" operator checks if the object is the same instance
a = 1
b = 1
c = a
print(a == b) # True
print(a is b) # True
print(a is c) # True 

x = [1,2,3]
y = [1,2,3]
z = x
print(x == y) # True
print(x is y) # False
print(x is z) # True because z is an instance of x

# "not" operator
print(not False) # True
print(not (2 < 3)) # False

# Exercise
# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array: # true if the list/array is not empty
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number: # true if second_number equals 0
    print("6")