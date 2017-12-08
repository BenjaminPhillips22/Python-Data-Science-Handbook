# Computation on NumPy Arrays: Aggregates


# %%

import numpy as np

# %%

# a neat tool to estimate the time taken
x = np.arange(1e6)
%timeit sum(x)
%timeit np.sum(x)

# np.sum is an order of magnitude faster

# %%

x = np.arange(10)
print(sum(x))
print(x)
print(x.sum())
print(x)

# %%

# numpy has NaN safe functions

x = np.array([1, 2, 3, np.NaN, 4, 5])
print(x.sum())
print(np.nansum(x))
