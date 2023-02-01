#Example of lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist) #[1, 2, 3]
print(*mylist) #1 2 3

# prints
# 1
# 2
# 3
# the whole list using for loop
for x in mylist:
    print(x)
    
#prints 1, 2, 3 using for loop
for x in range(3):
    if x < len(mylist) - 1:
        print('%i' % mylist[x] + ',', end=' ')
    else:
        print(mylist[x])

#list with different object types
list2 = [4, 'string', 7.1]
print(list2) #[4, 'string', 7.1]
print(*list2) #4 string 7.1