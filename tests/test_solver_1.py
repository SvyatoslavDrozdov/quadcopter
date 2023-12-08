import numpy as np
import matplotlib.pyplot as plt

from solver import get_solution

omega_squared = 2
A = np.array([[0, 1], [-omega_squared, 0]])
B = np.array([0, 1])
X_0 = np.array([0.5, 0])


def F(t):
    return 2 + 0 * t


max_time = 10
max_time_step = 10000
[time, X] = get_solution(X_0, A, B, F, max_time, max_time_step)

Y = X[:, 0]
plt.plot(time, Y)
plt.grid()
plt.show()
