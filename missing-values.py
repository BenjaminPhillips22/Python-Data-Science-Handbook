# %%

import numpy as np
import pandas as pd

# %%

a = np.array([1, None, 3])
b = np.array([1, np.nan, 3])

print(a.dtype)
print(b.dtype)

# %%

# use NaN. float or int types are
# faster than object types and
# have more functions you can apply

print(max(b))
try:
    print(max(a))
except:
    print('There was an error')


# %%

# Be careful of type casting when dealing
# with None and nan in pandas

c = pd.Series(range(4), dtype = int)
print(c)

c[0] = None
print(c)
print(c.dtype)

# None is changed to NaN and
# type is changed from int32 to float64

# %%

# There are some good tools for dealing with NAs

print(c.isnull())
print(c.notnull())
print(c.dropna()) # not inplace
print(c.dropna(inplace=True)) #inplace :)

# %%

c['a'] = np.nan
print(c)
print(c.fillna(10))

# %%

