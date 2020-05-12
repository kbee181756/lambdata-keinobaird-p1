import pandas as pd
import numpy as np
#from null_evalor.null_eval import assess_NA
from null_evalor.refactor import Nullers
from pandas import DataFrame

df = DataFrame({'a': [1, 3, 4], 'b': [6, np.nan, 3]})
print(df.head())
print(Nullers.assess_NA(df))

df_2 = DataFrame({'a': [3, np.nan, 4, 6, np.nan, 5, 3],
                  'b': [np.nan, np.nan, 4, 6, np.nan, 5, np.nan],
                  'c': [np.nan, np.nan, np.nan, np.nan, np.nan, 5, np.nan],
                  'd': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

print(df_2.head())
print(Nullers.assess_NA(df_2))

df_3 = DataFrame({'a': [3, np.nan, 4, 6, np.nan, np.nan, 3],
                  'b': [np.nan, np.nan, 4, 6, np.nan, 5, np.nan],
                  'c': [np.nan, np.nan, np.nan, np.nan, np.nan, 5, np.nan],
                  'd': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

print(df_3.head())
print(Nullers.assess_NA(df_3))
