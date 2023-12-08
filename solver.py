import numpy as np


def get_solution(X_0, A, B, U, max_time, max_time_step):
    """
    This function solves differential equation of the form dX/dt = AX + BU,
    where A and B are known matrix and U is the vector of known functions.
    :return:
    """
    X = np.array([X_0])
    tau = max_time / max_time_step
    time = [0]
    E = np.eye(len(A))
    V = np.linalg.inv(2 * E - tau * A)
    W = np.dot(V, (2 * E + tau * A))
    for time_step in range(max_time_step + 1):
        X_next = np.dot(W, X[time_step]) + 2 * tau * np.dot(V, np.dot(B, U(time[time_step] + tau / 2)))
        time.append(tau * time_step)
        X = np.vstack((X, X_next))

    return [time, X]
