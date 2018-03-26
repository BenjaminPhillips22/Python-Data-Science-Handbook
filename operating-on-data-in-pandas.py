# %%

import numpy as np
import pandas as pd

# %%

rng = np.random.RandomState(43)
print(rng.randint(0, 10, 4))

# %%

df = pd.DataFrame(rng.randint(0, 10, 3),
                  columns=['A'])

a = df.divide(2)
print(a)

# %%

print(a.mod(2))

# %%

print(a + a)
