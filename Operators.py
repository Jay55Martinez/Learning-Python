#Addition (+), Subtraction (-), Multiplication (*), Division (/)
number = 4 + 2 / 2 * 4
print(number)

#Remainder (%)
remainder = 10%3
print(remainder)

#Power (**)
squared = 3  ** 2
cubed = 3 ** 3
if squared == 9 and cubed == 27:
    print(str(squared) + ' and ' + str(cubed))

#(*) with strings duplicates the string by x
string = 'hello'
hello3times = string * 3
print(hello3times)

#(+) and (*) with lists
#(+) appends the lists
#(*) appends the same list to the end x times
mylist = [1, 5, 6, 8]
mylist2 = [4, 0, -1, -3]
print(mylist + mylist2)# [1, 5, 6, 8, 4, 0, -1, -3]
print(mylist * 2)# [1, 5, 6, 8, 1, 5, 6, 8]

#Exercise
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")