import numpy as np
import pandas as pd
X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
print(X)
df = pd.DataFrame(X, columns=['a', 'b'])
print(df)
# Compare this snippet from test.py: