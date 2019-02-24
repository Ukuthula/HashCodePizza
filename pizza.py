#%%
import numpy as np
import pandas as pd

#%%
example_param = pd.read_csv('data/example.in',sep=' ', header=None, nrows=1)
example = pd.read_csv('data/example.in',sep=' ', header=None, skiprows=1)
example = example[0].apply(lambda x: pd.Series(list(x)))
exR = int(example_param[0])
exC = int(example_param[1])
exL = int(example_param[2])
exH = int(example_param[3])
slices = []


#%%
print(exR, exC, exL, exH)

#%%
example[0][0]

#%%

