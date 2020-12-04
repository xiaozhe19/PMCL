
import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(0, 10, 0.1)
 
y = (4*x**2-16*x+16)/(x**2+1)
 
plt.title("一元一次函数")
plt.plot(x, y)
 
plt.show()
