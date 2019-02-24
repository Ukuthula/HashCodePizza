#%%
import numpy as np
import pandas as pd

#%%
example_param = pd.read_csv('data/example.in',sep=' ', header=None, nrows=1)
example = pd.read_csv('data/example.in',sep=' ', header=None, skiprows=1)
example = example[0].apply(lambda x: pd.Series(list(x)))
example[example == 'T'] = 0
example[example == 'M'] = 1
example = np.array(example)
exR = int(example_param[0])
exC = int(example_param[1])
exL = int(example_param[2])
exH = int(example_param[3])
slices = []


#%%
print(exR, exC, exL, exH)

#%%
print(example)

#%%
def isSliceOK( coords ):
    #get number of ingredients
    cells = (coords[1][0] - coords[0][0] + 1) * (coords[1][1] - coords[0][1] + 1 )
    #mushrooms
    mush = 0
    for i in range( coords[0][0] , coords[1][0] + 1):
        for j in range( coords[0][1] , coords[1][1] + 1):
            mush += example[j][i]   
    return cells <= exH and mush >= exL and cells-mush >= exL 

    




