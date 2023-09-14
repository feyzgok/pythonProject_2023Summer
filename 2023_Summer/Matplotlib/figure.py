import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y=[1,4,9,16]

fig,axes=plt.subplots()
axes[0].plot(x,x,color="red")
axes[1].plot(y,y,color='green')
plt.show()