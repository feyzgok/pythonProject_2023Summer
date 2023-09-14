#matrix
import numpy as np

matrixArr=np.array([20,30])
print(matrixArr)

myList=([10,20,30],[20,30,40],[40,50,60])
myMatrixArr2=np.array(myList)
print(myMatrixArr2)

print(myMatrixArr2[[0,2]])#fancy index
