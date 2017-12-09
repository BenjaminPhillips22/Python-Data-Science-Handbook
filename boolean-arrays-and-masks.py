# boolean arrays and masks

# %%

import numpy as np

# %%

if True and True:
    print("must be True")

if True & True:
    print("must still be True")

x = np.array([True, False]) & np.array([True, True])
print(x)
try:
    y = np.array([True, False]) and np.array([True, True])
except:
    print("This didn't work because 'and' is not bit-wise")

# %%

# np.count_nonzero can be used to count the number of True

x = np.arange(10)
print(np.count_nonzero(x % 2))

# %%

# don't forget to use brackets when you have multiple conditions

print((x > 3) & (x < 7))

# there is also np.bitwise_and (and the other comparison operations)

print(np.bitwise_and(x > 3, x < 7))
