import pandas as pd
import numpy as np


def assess_NA(data):
    null_sum = data.isnull().sum()
    total = null_sum.sort_values(ascending=False)
    percent = (((null_sum / len(data.index)) * 100).round(2)
               ).sort_values(ascending=False)
    df_NA = pd.concat([total, percent], axis=1, keys=[
        'Number of NA', 'Percent NA'])
    df_NA = df_NA[(df_NA.T != 0).any()]
    return df_NA

def null_check(data):
    null_sum = data.isnull().sum()
    total = null_sum.sort_values(ascending=True)
    percent = (((null_sum/len(data.index)) *100).round(2)
              ).sort_values(ascending=True)
    df_NA1 = pd.concat([total, percent], axis=1, keys=[
        'Number of NA-1', 'Percent NA-1'])
    df_NA1 = df_NA1[(df_NA1.T !=0).any()]
    return df_NA1

if __name__ == "__main__":
    data = assess_NA(data)
    print(data, assess_NA(data))

    data = null_check(data)
    print(data, null_check(data))