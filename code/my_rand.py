import random
import ahocorasick
import ahocorasick_op as ac_op

def rand_word(n, A):
    L = [random.choice(A) for _ in range(n)]
    w = ""
    for i in range(n-1, -1, -1):
        w = L[i] + w
    return w

def rand_list_fraction(n, A, frac):
    len_A = len(A)
    threshold = int(frac * pow(len_A, n))
    w_1 = rand_word(n, A)
    l = [w_1]
    len_l = 1
    AC_l = ahocorasick.Automaton()
    AC_l.add_word(w_1, w_1)
    AC_l.make_automaton()
    while len_l < threshold:
        w = rand_word(n, A)
        if not ac_op.is_substring(AC_l, w):
            AC_l.add_word(w, w)
            AC_l.make_automaton()
            l.append(w)
            len_l += 1
    return l

