# %%

import numpy as np
import pandas as pd

# %%


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)


# %%

df = make_df('ABC', range(3))
df

# %%

# array concatenation
x = [1, 2, 3]
print(np.concatenate([x, x]))

# %%

# Series concatenation
# notice the repeated indices
y = pd.Series(['A', 'B'])
z = pd.Series(['C', 'D'])
print(pd.concat([y, z]))

# %%

# DataFrame concatenation

df1 = make_df('AB', [1, 2])
print(pd.concat([df1, df1]))
print(pd.concat([df1, df1], axis=1))

# %%

# There is also the append function
df1.append(df1)
