# This prints out 'hello, Jay!'
name = 'Jay'
print('hello, %s!' % name)

# This prints out 'Jay is 19 years old'
age = 19
print('%s is %d years old' % (name, age))

# Prints a lists content 'A list: [1, 2, 3]'
mylist = [1, 2, 3]
print('A list: %s' % mylist)

# Prints float to 4 decimal places
float = 21.8319289129812
print('%.4f' % float)

#Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."

#print 'Hello John Doe. Your current balance is $53.44.
print(format_string % data)