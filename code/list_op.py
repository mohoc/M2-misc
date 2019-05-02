def max_length(L):
    max_val = 0
    for x in L:
        x_len = len(x)
        if x_len > max_val:
            max_val = x_len
    return max_val

def sort_by_length(L):
    n = max_length(L)
    L_prime = [[] for _ in range(n+1)]
    for x in L:
        x_len = len(x)
        L_prime[x_len].append(x)
    L_new = []
    for i in range(n+1):
        L_prime[i].sort()
        for x in L_prime[i]:
            L_new.append(x)
    return L_new

def difference(L1, L2):
    minus = []
    plus = []
    for x in L1:
        if not x in L2:
            minus.append(x)
    for x in L2:
        if not x in L1:
            plus.append(x)
    return (minus, plus)

def print_difference(L1,L2):
    minus, plus = difference(L1, L2)
    print("-: {} {}".format(len(minus), minus))
    print("+: {} {}".format(len(plus), plus))

def sum_length(L):
    S = 0
    for x in L:
        S += len(x)
    return S
