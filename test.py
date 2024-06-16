def road_to_cr (ii,years,i):
    i+=1
    if i==years:
        
        return ii*1.05*0.99-40
    ii=ii*1.05*0.99-40
    return road_to_cr (ii,years,i)
i=0
x=road_to_cr(6000,120,i)
print(x)