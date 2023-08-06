# %%
"""Test how custom functions work with sklearn package."""
import numpy as np
from AGONS_nano.Custom_Transformers import RowStandardScaler, RowMinMaxScaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#Generate random data
x = np.array([[1,2,3], [6,5,4], [8,7,9]])

#Compare RowStandardScaler to normal StandardScaler
rws = RowStandardScaler()
ss = StandardScaler()

print("Showing output of RowStandardScaler: {}".format(rws.fit_transform(x)))
print("Showing output of StandardScaler: {}".format(ss.fit_transform(x)))

#Compare RowMinMaxScaler to normal MinMaxScaler
rms = RowMinMaxScaler()
ms = MinMaxScaler()

print("Showing output of RowStandardScaler: {}".format(rms.fit_transform(x)))
print("Showing output of StandardScaler: {}".format(ms.fit_transform(x)))
