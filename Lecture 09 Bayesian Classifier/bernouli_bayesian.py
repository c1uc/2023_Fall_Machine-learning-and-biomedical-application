import numpy as np

Xp = np.array([
    [1, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 1]
])

Xs = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 0]
])

x = np.array([1, 0, 0, 1, 1, 1, 1, 0])

Pp = np.sum(Xp, axis=0) / np.sum(Xp)
print(Pp, sum(Pp))

Ps = np.sum(Xs, axis=0) / np.sum(Xs)
print(Ps, sum(Ps))

Px_p = np.prod(np.power(Pp, x) * np.power(1 - Pp, 1 - x))
Px_s = np.prod(np.power(Ps, x) * np.power(1 - Ps, 1 - x))
print(Px_p, Px_s)

C_p = Xp.shape[0]
C_s = Xs.shape[0]
print(C_p, C_s)

Pp_x = Px_p * C_p / (Px_p * C_p + Px_s * C_s)
Ps_x = Px_s * C_s / (Px_p * C_p + Px_s * C_s)
print(Pp_x, Ps_x)
