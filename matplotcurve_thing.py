import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-3,5,100)
Y = lambda x: x**4 - 3*x**3 + x**2 - 3*x + 10

plt.plot(X, Y(X))
plt.show()
