
# %%

import numpy as np
import pandas as pd
import seaborn as sns

# %%

planets = sns.load_dataset('planets')
print(planets.shape)
print(planets.head())

# %%

print(planets.mean())
print(planets.median())

# %%

print(planets.describe())

# %%

print(planets.head())
print(planets.groupby('year')['mass'].mean().sort_values())

# %%



