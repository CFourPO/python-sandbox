import numpy as np

# Example
print("Example 1: Calculate BMI\n")
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print('Numpy Height: %s' % np_height)
print('Numpy Weight: %s' % np_weight)

bmi = np_weight / np_height ** 2
print('BMI: %s' % bmi)

print(bmi > 23)
print(bmi[bmi > 23])

# Example
print("Example 2: Weight to Height Ratios\n")
h = [2, 3, 4]
w = [4, 6, 8]
np_h = np.array(h)
np_w = np.array(w)

w_to_h = np_w / np_h

print(w_to_h)

# Example
print("Example 3: Weight Conversion kg to lbs\n")
"""
First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds.
"""
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_kg = np.array(weight_kg)
np_weight_lb = np_weight_kg * 2.2

print(np_weight_lb)
