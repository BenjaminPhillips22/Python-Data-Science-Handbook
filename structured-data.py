
# %%

import numpy as np

# %%

# compound data for structured arrays

data = np.zeros(3, dtype={
    'names': ('name', 'age', 'weight'),
    'formats': ('U10', 'i4', 'f8')
})

print(data)

data['name'] = ['Alice', 'Bob', 'Cathy']
data['age'] = [100, 99, 98]
data['weight'] = [10.3, 55.3, 100/3]

print(data)

# %%

# get all names
print(data['name'])

# get all of Alice's details
print(data[0])