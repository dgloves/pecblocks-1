import numpy as np
import pandas as pd
import os
import zipfile
import h5py
import math

'''adds each group to a list of Pandas dataframes'''
def read_hdf5_file(filename, cols, n_skip=0, n_dec=1):
  pdata=[]
#  print (cols)
  with h5py.File(filename, 'r') as f:
    for grp_name, grp in f.items():
#      print ('Reading', grp_name, 'for a dataframe')
      vals = []
      ncols = len (cols)
      nrows = grp[cols[0]].len()
      ndfrows = int(math.ceil(nrows/n_dec))
#      print ('hdf5 ary', nrows, ndfrows, ncols)
      ary = np.zeros (shape=(ndfrows, ncols))
      j = 0
      for col in cols:
        x = np.zeros(nrows)
        grp[col].read_direct (x)
        ary[:,j] = x[::n_dec]
        j += 1
      df = pd.DataFrame (data=ary[n_skip:,:], columns=cols)
      pdata.append(df)
  return pdata

def read_csv_files(path, pattern=".csv"):
  if zipfile.is_zipfile (path):
    zf = zipfile.ZipFile (path)
    pdata =[]
    for zn in zf.namelist():
      pdata0 = pd.read_csv (zf.open(zn),sep=',',header=0,on_bad_lines='skip')
      if pdata0.shape[0] >0:
        pdata += [pdata0.copy()]
    return pd.concat(pdata)
  else:
    files = [fn for fn in os.listdir(path) if pattern in fn]; 
    # files = np.sort(files)
    if len(files)>0:
      pdata =[]
      for i in range(len(files)):
        pdata0 = pd.read_csv(os.path.join(path,files[i]),sep=',',header=0,on_bad_lines='skip')
        if pdata0.shape[0] >0:
          pdata += [pdata0.copy()]  
      return pd.concat(pdata)


