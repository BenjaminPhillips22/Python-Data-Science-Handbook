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

df1 = make_df('ABC', range(3))
df2 = make_df('ADE', range(3))

# %%

print(pd.merge(df1, df2, ))

# %%

# joins on index
print(df1.set_index('A').join(df2.set_index('A')))
