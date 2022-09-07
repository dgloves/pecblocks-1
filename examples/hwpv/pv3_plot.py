import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_hdf ('pv3_server.hdf5')
print (df)
#df['Vs'] = np.abs(df['Vs'])
#df['Vc'] = np.abs(df['Vc'])
#df['Is'] = np.abs(df['Is'])
#df['Ic'] = np.abs(df['Ic'])
#print (df)

#df.plot(x='t', y=['Vdc', 'Idc'], backend='matplotlib', subplots=True)
df.plot(x='t', y=['G', 'T', 'Md', 'Mq', 'Fc', 'Ctl', 'Vrms', 'GVrms', 'Vdc', 'Idc', 'Id', 'Iq'], 
        layout=(3, 4), figsize=(16,10), subplots=True)

plt.show()
