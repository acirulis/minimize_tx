import numpy as np
import scipy.optimize


def get_const_mat(N):
    ones = np.ones(N - 1)
    eye = np.eye(N - 1) * -1
    block = np.vstack((ones, eye))
    A = block.copy()
    for i in range(1, N):
        block[[i - 1, i]] = block[[i, i - 1]]  # swap rows
        A = np.hstack((A, block))
    return A


def vec_2_mat(x_opt, N):
    M = np.zeros((N, N))
    k = 0
    for i in range(0, N):
        for j in range(0, N):
            if j != i:
                M[j, i] = x_opt[k]
                k += 1
    return M


balances = [-10, -3, -3, 6, 5, 5, -8, 8]
balances = [-10, -3, -3, -8, 8, 6, 5, 5]
# balances = [-3, -3, 1, 5]
# balances = sorted(balances, key=abs)

# balances.sort()
print(balances)
N = len(balances)
K = N * (N - 1)

cm = get_const_mat(N)

# cm2 = [
#     [1, 1, 1, 1, 1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0],
#     [-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0],
#     [0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0],
#     [0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0],
#     [0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, -1],
#     [0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 1, 1, 1, 1, 1]
# ]

c = np.ones(K)
lb = np.zeros(K)

# print(cm)

x_opt = scipy.optimize.linprog(c, A_eq=cm, b_eq=balances, method='revised simplex')
result = vec_2_mat(x_opt.x, N)
print(result)
# set_const_mat();
# var
# k = members.length * (members.length - 1);
# var
# c = ones(k);
# var
# lb = zeros(k);
# var
# x_opt = lp(c, [], [], A_mat, balances, lb, []);
# var
# A = vec_2_mat(x_opt);
