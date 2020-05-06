import pandas as pd
import numpy as np
from null_eval.null_eval import assess_NA

from pandas import DataFrame

df = DataFrame({'a':[1, 3, 4], 'b': [6, np.nan, 3]})
print(df.head())
print(assess_NA(df))    

df_2 = DataFrame({'a': [3, np.nan, 4, 6, np.nan, 5, 3],
'b':[np.nan, np.nan, 4, 6, np.nan, 5, np.nan],
'c':[np.nan, np.nan, np.nan, np.nan, np.nan, 5, np.nan],
'd':[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

print(df_2.head())
print(assess_NA(df_2))