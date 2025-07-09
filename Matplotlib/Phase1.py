import matplotlib.pyplot as plt

import numpy as np

## Array1=np.array([1,6,8,9,10,3,2])
 ##Array2=np.array([3,4,5,7,8,10])
## You can also Have Array2 for y axis 
##plt.plot(Array1,Array2,marker='o')

##plt.xlabel("Simple Numbers")
##plt.ylabel("Simple Y axis Numbers ")
##plt.show()


## These Are the Parameters that you can Pass through the plotting things 
## marker|line|color
## o:r circle Dot color Means Red 
## Marker Size Means -------> 20 ms 
## Marker Color  ----___--> "mec" 
## LineStyle can dotted Dashed 
##you can also get for line Width

## Multiple Lines 
##plt.plot(Array1)
##plt.plot(Array2)

## Line Labels 
## Here you can Add Grid Lines ALong x axis and y axis like 
##plt.grid()

## Here you Can Set Multiple Plots These not Multiple Lines 
## plt.subplot(1,2,1)
##  First One Means nrows and 2nd Menas ncolumns third one Menas index 

## Scatter Plots Are Also Similar to the SubPlot Here You Can Plot The Graphs 
  ##  Here You Can Compare the Sizes Based on the Sizes like That s plt.scatter(x, y, s=sizes)

## Combine Color Size and Alpha 
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(100, size=(100))     # ✅ fixed typo here
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()




