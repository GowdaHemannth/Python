import matplotlib.pyplot as plt

import numpy as np

Array1=np.array([1,6,8,9,10,3,2])
Array2=np.array([3,4,5,7,8,10])
## You can also Have Array2 for y axis 
plt.plot(Array1,marker='o')
plt.plot(Array2)
plt.xlabel("Simple Numbers")
plt.ylabel("Simple Y axis Numbers ")
plt.show()


## These Are the Parameters that you can Pass through the plotting things 
## marker|line|color
## o:r circle Dot color Means Red 
## Marker Size Means -------> 20 ms 
## Marker Color  ----___--> "mec" 
## LineStyle can dotted Dashed 
##you can also get for line Width

## Multiple Lines 

