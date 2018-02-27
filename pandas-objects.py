# pandas objects

# %%

import numpy as np
import pandas as pd

# %%

# Make a Series with a Dict
x = pd.Series({'a': 3,
               'b': 6,
               'c': 9})

print(x['a':'c'])

# %%

# a dataframe can a Dict of Series
df = pd.DataFrame({'col 1': x,
                   'col 2': x})

df
# %%

# or a Dict of lists/np arrays
df = pd.DataFrame({'col 1': ['e', 'f', 'g'],
                   'col 2': np.array([2, 4, 6])})

print(df)
print(df.columns)
print(df.index)
