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

