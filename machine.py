k = 3
for i in range(-1, k):
    u_1 = (1-0.8**(k-i))*6 + 0.8**(k-i) + sum([(1-0.8**l)*2 for l in range(1, 8-k)])
    u_0 = sum([(1-0.8**(l-i))*2 for l in range(k, 8)])
    print(u_1 - u_0)


def u_0(i, k):
    return sum([(1 - 0.8 ** (l - i)) * 2 for l in range(k, 8)])

def u_1(i, k):
    return (1 - 0.8 ** (k - i)) * 6 + 0.8 ** (k - i) + sum([(1 - 0.8 ** l) * 2 for l in range(1, 8 - k)])
