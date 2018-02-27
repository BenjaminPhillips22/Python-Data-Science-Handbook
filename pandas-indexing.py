# %%

import pandas as pd

# %%

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])

print('a' in data)
print(0.5 in data)  # False
print(list(data.items()))
print(data.keys())

# %%

# masking
print(data[(data > 0.3) & (data < 0.8)])

# %%

# loc and iloc
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])

# loc for explicit location
print(data.loc[1])

# iloc for implicit 'index' location
print(data.iloc[1])

# %%

s1 = [1, 2, 3, 4]
s2 = [3, 4, 5, 6]

df = pd.DataFrame(data={
    'col 1': s1,
    'col 2': s2,}
)

print(df.loc[df['col 2'] > 4, ['col 2']])
