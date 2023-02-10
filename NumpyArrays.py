import numpy as np
# Numpy Arrays is a alternative to Python lists. Some benfits of numpy arrays is
# that they are fast and easy to work with

# Create 2 new lists with heights and weights
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [85.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# making height and weight lists numpy
np_height = np.array(height)
np_weight = np.array(weight)

# print out the type of np_height
print(type(np_height))

# Element-wise calculations can take all the heights and weights and calculate the bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# Subsetting

# Prints boolean responce for each element
print(bmi > 23)

# Prints only those observations above 26
print(bmi[bmi > 26])

# Exercise
"""
First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights
from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your
conversion. Lastly, print the resulting array of weights in pounds.
"""

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)