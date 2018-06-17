# %%

import pandas as pd

# %%

# got to be careful
d1 = pd.to_datetime('17-6-2018')
d2 = pd.to_datetime('6-17-2018')
print(d1)
print(d2)
# these are the same...

# %%

# this returns an error
d3 = pd.to_datetime('6-17-2018', format='%d/%m/%Y')
print(d3)

# %%

print(d1.strftime('%A'))