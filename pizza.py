#%%
import numpy as np
import pandas as pd

#%%
def run( path_in, path_out ):
    data_param = pd.read_csv(path, sep=' ', header=None, nrows=1)
    data = pd.read_csv(path,sep=' ', header=None, skiprows=1)
    data = data[0].apply(lambda x: pd.Series(list(x)))
    data[data == 'T'] = 0
    data[data == 'M'] = 1
    data = np.array(data, dtype=int)
    dataR = int(data_param[0])
    dataC = int(data_param[1])
    dataL = int(data_param[2])
    dataH = int(data_param[3])


#%%
def generateSlices(R,C,L,H):
    '''
    This generates possible slices.
    '''
    slices = []

    sqrt = int(np.sqrt(H))

    for row in range(0,R,sqrt):
        for col in range(0,C,sqrt):
            slices.append([(row,col),(min(row+sqrt-1,R-1), min(col+sqrt-1, C-1))])

    return slices

#%%
def isSliceOK( coords , data ):
    #get number of ingredients
    cells = (coords[1][0] - coords[0][0] + 1) * (coords[1][1] - coords[0][1] + 1 )
    #mushrooms
    mush = 0
    for i in range( coords[0][0] , coords[1][0] + 1):
        for j in range( coords[0][1] , coords[1][1] + 1):
            mush += data[i][j]   
    return cells <= exH and mush >= exL and cells-mush >= exL 


#%%
def writeToFile(file_name, slices):
    slices = np.array(slices).reshape(len(slices),4)
    dataframe = pd.DataFrame(slices)
    dataframe.to_csv(file_name, header=[str(len(slices)),"","",""],sep=' ', index=False)
    

#%%
pd.DataFrame(np.array(ok).reshape(len(ok),4))

#%%
slices = generateSlices(exR, exC, exL, exH)
ok = []
for slize in slices:
    if isSliceOK(slize, example):
        ok.append(slize)

#%%
ok

#%%
writeToFile('out/example.in', ok)
