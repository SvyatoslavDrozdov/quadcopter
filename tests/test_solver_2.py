import numpy as np
import matplotlib.pyplot as plt
from solver import get_solution

omega_squared = 2
A = np.array([[0, 1], [-omega_squared, 0]])
B = np.array([[1, 0], [0, 2]])
X_0 = np.array([0, 0])


def U(t):
    y_1 = np.sin(t + 1) / (t + 1)
    y_2 = 1
    return np.array([y_1, y_2])


max_time = 10
max_time_step = 1000
[time, X] = get_solution(X_0, A, B, U, max_time, max_time_step)

Y = X[:, 0]
plt.plot(time, Y)
plt.grid()
plt.show()
