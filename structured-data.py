
# %%

import numpy as np

# %%

# compound data for structured arrays

data = np.zeros(3, dtype={
    'names':('name', 'age', 'weight'),
    'formats':('U10', 'i4', 'f8')
})

print(data)

data['name'] = ['Alice', 'Bob', 'Cathy']

print(data)