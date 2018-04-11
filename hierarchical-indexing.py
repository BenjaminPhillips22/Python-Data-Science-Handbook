# %%

import numpy as np
import pandas as pd

# %%

# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])

columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)*10 + 37


# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data

# %%

# need to access from the outside hierachy in

print(health_data)
print(health_data.loc[2013])
print(health_data['Bob'])
print(health_data['Bob']['HR'].loc[2013])
print(health_data['Bob']['HR'].loc[2013].loc[1])

# %%

# getting info

data_mean = health_data.mean(level='year')
print(data_mean)

# %%

# and of course, reindexing!


print(health_data)
print(health_data.reset_index())
print('-'*50)

# hmmm, can't figure out how to reset the column indexes
