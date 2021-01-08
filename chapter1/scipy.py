import pandas as pd
import numpy as np
np.random.seed(1)
a = pd.Series(np.random.randint(size=5, low=1, high=10))
print(a, '\n')
print(a[0], '\n')
print(a[1: 3], '\n')
print(a[::2], '\n')
