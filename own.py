import pandas as pd
import numpy as np
np.random.seed(0)
readings = np.random.randn(2205, 6000)
de = pd.DataFrame(readings)
#de your minutes dataframe
#ds dataframe created for seconds
def minute_to_second(de):
#mean function and conversion
    ds=[]
    for i,row in de.iterrows():
        second_list=[]
        for i in range(len(row)):
            if i%100==99:
                second_list.append(row[i-100:i])
        ds.append(second_list)
    return ds

ds=pd.DataFrame(minute_to_second(de))
print(ds)