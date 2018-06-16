# %%

import pandas as pd

# %%

data = ['peter', 'Paul', 'MARY', 'gUIDO', None]
[print(s.capitalize()) for s in data]

# but it will return an error for None

# %%

# so we can use the pandas function

print(pd.Series(data).str.capitalize())

# %%

print(pd.Series(data).str.capitalize().str.startswith('P'))

# %%

# There are a lot of cool methods.
# https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html
