import pandas as pd
import numpy as np

def assess_NA(data):
  null_sum = data.isnull().sum()
  total = null_sum.sort_values(ascending=False)
  percent = (((null_sum / len(data.index))*100).round(2) ).sort_values(ascending=False)
  df_NA = pd.concat([total, percent], axis=1, keys=['Number of NA', 'Percent NA'])
  df_NA = df_NA[(df_NA.T !=0).any()]
  return df_NA


if __name__ == "__main__":
    data = assess_NA(data) 
    print(data, assess_NA(data))