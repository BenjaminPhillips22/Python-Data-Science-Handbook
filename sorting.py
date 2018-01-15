# sorting

# %%

import numpy as np

# %%

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a[:-1])
print(a[1:])
print(a[::-1])

# bogosort, prehaps the worst sorting
# algorithm that works


def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x


print(bogosort(a[::-1]))

# %%

b = np.array([2, 4, 3, 1, 0])

# different sort types are available
# {'quicksort', 'mergesort', 'heapsort'}

# sort without modifying inpurt
print(np.sort(b))
print(b)

# sort in-place
b.sort()
print(b)

# cool function argsort
# return the indices of the sorted elements
c = np.array([0, 20, 11, 3])
print(c)
print(np.argsort(c))
