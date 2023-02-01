#Integer Example
myint = 21
print(myint)
one = 1 
two = 2
three = one + two
print(three)

#Float Example
myfloat = 7.1
print(myfloat)
myfloat = float(90)
print(myfloat)

#String Example
mystring = 'hello'
print(mystring)
helloworld = mystring + ' world'
print(helloworld)

#Assignments can be done to multiple objects in one line
a,b = 3, 6
print(a + b)
number, word = 5, 'five'
# this will not work:
# print(number + word)

#Exercise
if mystring == 'hello':
    print("String: %s " % mystring)
if myfloat == 7.1:
    print('Float %f' % myfloat)
if myint != 0:
    print('%i != 0' % myint)
