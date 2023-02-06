# Dictionary is like a java map
phonebook = {}
phonebook['Jay'] = 1234567890
phonebook['Jack'] = 6718383909
phonebook['Bill'] = 2932733889
print(phonebook) # prints {'Jay': 1234567890, 'Jack': 6718383909, 'Bill': 2932733889}

# Alternative way to initialize a dictionary
cars_in_stock = {'ford': 2, 'subaru': 5, 'toyota': 1}
print(cars_in_stock) # prints {'ford': 2, 'subaru': 5, 'toyota': 1}

# Iterating over dictionaries
for name, number in phonebook.items():
    print('Phone number of %s is %d' % (name, number))
    
# Removing a value
del phonebook['Bill'] # removes Bill and his number from dictionary
print(phonebook) # {'Jay': 1234567890, 'Jack': 6718383909}

# alternative way to remove
phonebook.pop('Jay')
print(phonebook) # {'Jack': 6718383909}

# Exercise
"""
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
"""
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  