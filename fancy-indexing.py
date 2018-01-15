# fancy indexing

# %%

import numpy as np
import matplotlib.pyplot as plt

# %%

x = np.arange(10)
print(x)
print(x[-1])
print(x[:-1])
print(x[::-1])
print(x[::2])
print(x[1::2])

# %%

# the shape of the result reflects the shape
# of the index arrays rather than the shape
# of the array being indexed

x = np.arange(10)
y = np.array([[1, 2], [2, 3]])

print(x[y])

# %%

x = np.arange(10)
y = [0, 1, 2, 3, 9]
print(x)
x[y] += 1
print(x)

# %%

np.random.seed(42)
x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)

plt.hist(x, bins, histtype='step')
