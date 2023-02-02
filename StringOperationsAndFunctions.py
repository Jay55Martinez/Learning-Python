#Getting the length of a string len()
astring = 'Hello World!'
print(len(astring)) # prints 12

#Finding the first occurrence of a character 
print(astring.index('o')) # prints 4

#Countst the number of times that a character appears in the string
print(astring.count('l')) # prints 3

#Substring of the string
print(astring[3:7]) # prints lo W
print(astring[1:-7]) # prints ello
print(astring[1:7:3]) # prints eo

#Reverses the string
print(astring[::-1]) # prints !dlroW olleH

#Converts all of the characters to uppercase and lowercase
print(astring.upper()) # prints HELLO WORLD!
print(astring.lower()) # prints hello world!

#Determines if the start of the string starts or ends with the specified condition
print(astring.startswith("Hello")) # prints True
print(astring.endswith("blablabla")) # prints False

#Splits the string at the spaces " " putting it into a list
liststring = astring.split(" ")
print(liststring) # prints ['Hello', 'World!']

#Exercise
s = "Hey theraa! wht shou"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))