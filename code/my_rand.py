import random

def rand_word(n, A):
    L = [random.choice(A) for _ in range(n)]
    w = ""
    for i in range(n-1, -1, -1):
        w = L[i] + w
    return w