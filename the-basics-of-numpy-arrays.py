
# %%

import numpy as np

# %%

np.random.seed(0)

x = np.random.randint(10, size=(3, 4, 5))
print(x.ndim)
print(x.itemsize)
print(x.nbytes)

# %%

# slices of lists, both are shallow copies
a = [1, 2, 3]
b = a
b[0] = 9
print(a)
b[1:] = [10, 11]
print(a)

# %%

# slices of np arrays are also shallow copies
c = np.array([1, 2, 3])
d = c
d[0] = 9
print(c)
d[1:] = [10, 11]
print(c)

# use .copy() to create deep copies
e = np.array([1, 2, 3])
f = e.copy()
f[0] = 9
print(e)

# %%

# reshape
print(np.array(list(range(1, 10))).reshape((3, 3)))
