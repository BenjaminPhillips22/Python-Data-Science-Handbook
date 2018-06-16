# %%

import pandas as pd
import numpy as np
import seaborn as sns
titanic = sns.load_dataset('titanic')

# %%

df = titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()
print(df)

# %%

df = titanic.pivot_table('survived', index='sex', columns='class')
print(df)

# These produce the same dataframe
