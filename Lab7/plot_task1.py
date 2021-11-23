import matplotlib.pyplot as plt
from numpy import *
import numpy as np


def f(t):
    return -t ** np.cos(5 * t)

t = np.arange(0, 10, 0.01)
y = f(t)

plt.plot(t, y, 'm')

plt.xlabel('t')
plt.ylabel('y')
plt.title('Y(x)=-x^cos(5*x), x=[0...10]')

plt.show()
