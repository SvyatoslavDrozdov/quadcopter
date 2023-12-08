import numpy as np
from data import A, B, X_0
from solver import get_solution
import matplotlib.pyplot as plt


def U(t):
    def u_1(inner_t):
        return 0

    def u_2(inner_t):
        return 0

    def u_3(inner_t):
        return 0

    def u_4(inner_t):
        if inner_t <= 2 * np.pi:
            return np.sin(inner_t)
        else:
            return 0
        # return 0

    return np.array([u_1(t), u_2(t), u_3(t), u_4(t)])


max_time = 20
max_time_step = 1000
[time, X] = get_solution(X_0, A, B, U, max_time, max_time_step)
x = X[:, 6]
y = X[:, 8]
z = X[:, 10]

fi = X[:, 0]
theta = X[:, 2]

F_1 = X[:, 12]
F_2 = X[:, 13]
F_3 = X[:, 14]
F_4 = X[:, 15]

# plt.plot(time, F_1, label="F_1")
# plt.plot(time, F_2, label="F_2")
# plt.plot(time, F_3, label="F_3")
# plt.plot(time, F_4, label="F_4")

plt.plot(time, fi, label="φ")
plt.plot(time, theta, label="θ")

# plt.plot(time, x, label="x - coordinate")
# plt.plot(time, y, label="y - coordinate")
# plt.plot(time, z, label="z - coordinate")

plt.legend()
plt.grid()
plt.show()
