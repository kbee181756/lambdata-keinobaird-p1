import pandas as pd
import numpy as np

from pandas import DataFrame

df = DataFrame({'a':[1, 3, 4], 'b': [6, 4, 3]})
print(df.head())

import null_eval

print(assess_NA(df))