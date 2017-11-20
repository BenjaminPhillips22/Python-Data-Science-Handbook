# Computation on NumPy Arrays: Universal Functions

# %%

# scipy also has functions in the special submodule

import numpy as np
from scipy import special

# Gamma functions (generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))

# %%

# for large arrays, specifying the output array
# will prevent a temporary array from being created

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

# %%

# Aggregates
x = np.arange(1, 6)
print(x)

# multiply all the elements
print(np.multiply.reduce(x))

# store intermediate results as all the elements are multiplied
print(np.add.accumulate(x))

# pretty much these... (but good to know for other things)
#  (np.sum, np.prod, np.cumsum, np.cumprod)

# %%

# outer product

print(np.multiply.outer(x, x))
