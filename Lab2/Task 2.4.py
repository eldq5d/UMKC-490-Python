# Using Numpy create random vector of size 15 and replace the maximum value by 100.

import numpy as np

a = np.random.random_integers(0, 200, (1, 15))
print(a)
M = a.max(None)
np.place(a, a == M, 100)
print(a)
