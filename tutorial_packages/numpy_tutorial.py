import numpy as np

# Create 2 new lists height and weight
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


"""
First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds. Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds.
"""
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weight_kg = np.array(weight_kg)
np_weight_lb = np_weight_kg * 2.2

print(np_weight_lb)
