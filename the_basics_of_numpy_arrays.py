
# %%

import numpy as np

# %%

np.random.seed(0)

x = np.random.randint(10, size=(3, 4, 5)) 
print(x.ndim)
print(x.itemsize)
print(x.nbytes)
