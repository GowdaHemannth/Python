from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
## Here the Below codeused for travessing the boundary SVM 
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC

##Load the Daatset 
Cancer=load_breast_cancer()
x=Cancer.data[:,:2] ## 
y=Cancer.target

## Build the model=
SVM=SVC(kernel='rbf',gamma=0.5,c=1.0)
SVM.fit(x,y)

## Plot the Decision Boundary
DecisionBoundaryDisplay.from_estimator(
    SVM, ## MODLE TYPE
    x,  ## DATASET LIKE SELECT ONLY 2 COLUMNS 
     response_method="predict",
        cmap=plt.cm.Spectral,
        alpha=0.8,
        xlabel=Cancer.feature_names[0],
        ylabel=Cancer.feature_names[1],
)

## Noew for Plotting think these or tk these 
plt.scatter(x[:,0],x[:,1],c=y,s=20,edgecolors='k')
plt.show()