# "for" loop
primes = [2, 3, 5, 7]
for prime in primes: # prime is the current element in the iteration 
    print(prime)

# using "range" and "xrange"
# Prints out the numbers 0, 1, 2, 3, 4
for x in range(5):
    if x == 4: # note range -1 is the last iteration
        print(x)
        break
    print(x, end = ", ")

# Prints out 3, 4
for x in range(3, 5):
    if x == 4: 
        print(x)
        break
    print(x, end = ", ")

# Prints out 3, 5, 7, 9
for x in range(3, 10, 2): # iterates by 2 
    if x == 9:
        print(x)
        break
    print(x, end = ", ")
    
# "while" loop
count = 0
while count < 5:
    print(count) 
    count += 1 # adds 1 to the current value of count

# "break" and "continue" statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Pints out only odd numbers
print('example only print odd numbers')
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
    
# "else" clause for loops
# when the clause in the loop fails the "else" is then executed
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('count value reached %d' % count)
    
# example of the else statement not being executed
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print('this will not be printed')

# Exercise
# Loop through and print out all even numbers from the numbers list 
# in the same order they are received. Don't print any numbers that 
# come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        print()
        break
    if number % 2 == 0:
        print(number, end= " ")