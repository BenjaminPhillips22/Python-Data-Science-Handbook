# Computation on NumPy Arrays: Broadcasting

# %%

import numpy as np

# %%

a = np.arange(3)
b = np.arange(3).reshape((3, 1))
print(a)
print(b)
print(a + b)


# %%

# x and y have 1000 steps from 0 to 10
x = np.linspace(0, 10, 1000)
y = np.linspace(0, 10, 1000)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

%matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 10, 0, 10],
           cmap='viridis')
