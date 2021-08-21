import numpy as np
import matplotlib.pyplot as plt


path = '/Regression/data.txt'
data = np.loadtxt(path)
plt.scatter(data[:, 0], data[:, 1])
plt.show()

