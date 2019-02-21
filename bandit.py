import numpy as np

def p(m, n):
    return (m+1)/(m+n+2)

J = np.zeros([6, 6, 6])
U = np.zeros([6, 6, 6])

for m in range(6):
    for n in range(6):
        if m + n <= 5:
            if 0.6 > p(m, n): # choose A
                J[5, m, n] = 0.6
                U[5, m, n] = 1
            else:
                J[5, m, n] = p(m, n)
                U[5, m, n] = 2

for k in range(4, -1, -1):
    for m in range(6):
        for n in range(6):
            if m + n <= k:
                if  0.6 * (1+J[k+1, m, n]) + 0.4 * J[k+1, m, n] > \
                        p(m, n) * (1 + J[k+1, m+1, n]) + (1 - p(m, n)) * J[k+1, m, n+1]:  # choose A
                    J[k, m, n] = 0.6 * (1+J[k+1, m, n]) + 0.4 * J[k+1, m, n]
                    U[k, m, n] = 1
                else:
                    J[k, m, n] = p(m, n) * (1 + J[k+1, m+1, n]) + (1 - p(m, n)) * J[k+1, m, n+1]
                    U[k, m, n] = 2

for k in range(6):
    for m in range(6):
        for n in range(6):
            if m + n <= k and U[k,m,n] == 2:
                print(k, m, n, U[k, m, n])
