import numpy as np
from numpy import pi
from matplotlib import pyplot as plt

x=np.linspace(0,2*pi,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()
