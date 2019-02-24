#%%
import numpy as np
import pandas as pd

#%%
example_param = pd.read_csv('data/example.in',sep=' ', header=None, nrows=1)
example = pd.read_csv('data/example.in',sep=' ', header=None, skiprows=1)
example = example[0].apply(lambda x: pd.Series(list(x)))

#%%
example_param

#%%
example

#%%
