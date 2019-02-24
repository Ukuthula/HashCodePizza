#%%
import numpy as np
import pandas as pd

#%%
example_param = pd.read_csv('data/example.in',sep=' ', header=None, nrows=1)
example = pd.read_csv('data/example.in',sep=' ', header=None, skiprows=1)
example = example[0].apply(lambda x: pd.Series(list(x)))
example[example == 'T'] = 0
example[example == 'M'] = 1
example = np.array(example, dtype=int)
exR = int(example_param[0])
exC = int(example_param[1])
exL = int(example_param[2])
exH = int(example_param[3])

#%%
print(exR, exC, exL, exH)

#%%
# saves
slices = []

#%%
int(np.sqrt(exH))

#%%
def generateSlices(R,C,L,H):
    '''
    This generates possible slices.
    '''
    slices = []

    sqrt = int(np.sqrt(H))

    print(sqrt)

    for row in range(0,R,sqrt):
        for col in range(0,C,sqrt):
            slices.append([(row,col),(min(row+sqrt-1,R-1), min(col+sqrt-1, C-1))])
            print(row,col)

    return slices

#%%
generateSlices(exR, exC, exL, exH)
