import numpy as np
import matplotlib.pyplot as plt
from solver import get_solution

A = np.array([[0, 1, -2], [1, 1, 0], [-1, 0, 1]])
B = np.array([[1, 0, - 1], [0, -1, 0], [0, 0, 2]])
X_0 = np.array([0, 0, 0])


def U(t):
    def u_1(inner_t):
        return 1

    def u_2(inner_t):
        return 1

    def u_3(inner_t):
        if inner_t <= 2 * np.pi:
            return np.sin(inner_t)
        else:
            return 0

    return np.array([u_1(t), u_2(t), u_3(t)])


max_time = 1
max_time_step = 10000
[time, X] = get_solution(X_0, A, B, U, max_time, max_time_step)

Y_1 = X[:, 0]
Y_2 = X[:, 1]
Y_3 = X[:, 2]
# plt.plot(time, Y_1, label="X_1")
# plt.plot(time, Y_2, label="X_2")
plt.plot(time, Y_3, label="X_3")
plt.grid()
plt.legend()
plt.show()
