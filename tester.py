import pandas as pd
import numpy as np
from null_eval.null_eval import assess_NA

from pandas import DataFrame

df = DataFrame({'a':[1, 3, 4], 'b': [6, 4, 3]})
print(df.head())
print(assess_NA(df))