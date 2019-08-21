import list_op

def is_substring(u, w):
    """returns True iff u is a substring of w"""
    n = len(w)
    m = len(u)
    found_occurrence = False
    for i in range(n-m+1):
        found_mismatch = False
        for j in range(m):
            if u[j] != w[i+j]:
                found_mismatch = True
                break
        if not found_mismatch:
            found_occurrence = True
            break
    return found_occurrence

def is_substring_list(U, w):
    """returns True iff an element u of U is a substring of w"""
    for u in U:
        if is_substring(u, w):
            return True
    return False

def M(w, A):
    """returns M the minimal set of the forbidden substrings in w"""
    M = set()
    n = len(w)
    #add letters that do not appear in w
    A_w = A.copy()
    for l in A:
        if not is_substring(l, w):
            M.add(l)
            A_w.remove(l)
    for i in range(n):
        A_w_i = A_w.copy()
        if i < n - 1:
            A_w_i.remove(w[i+1])
        for l in A_w:
            u = w[i] + l
            j = i
            while is_substring(u, w) and j > 0:
                j -= 1
                u = w[j] + u
            if not is_substring(u, w):
                M.add(u)
    M = list(M)
    M = list_op.sort_by_length(M)
    return M
