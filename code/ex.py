import list_op, my_rand, naive
import sys, random

A = ["A","U","G","C"]
n = 100
N = 1000
name_stats = ["A", "n", "N", "mean_M", "max_M", "mean_minus", "mean_plus", "max_minus", "max_plus", 
                "mean_max_length_M", "max_max_length_M", "mean_sum_length_M", "max_sum_length_M"]

def rand_test(A, n, N, print_progression = True):
    mean_minus = 0.0
    mean_plus = 0.0
    max_minus = 0
    max_plus = 0
    mean_M = 0.0
    mean_max_length_M = 0.0
    mean_sum_length_M = 0.0
    max_M = 0
    max_max_length_M = 0
    max_sum_length_M = 0
    
    #thresholds to keep track of the computation progression
    thresholds = [5*i for i in range(1,22)]
    current_threshold_id = 0
    current_threshold = thresholds[current_threshold_id]
    for K in range(1, N+1):
        #choose w1 at random and obtain w2 with a random mutation
        w1 = my_rand.rand_word(n, A)
        i = random.randint(0, n-1)
        A2 = A.copy()
        A2.remove(w1[i])
        w2 = w1[:i] + random.choice(A2) + w1[i+1:]
        #compute M for both words
        M1 = naive.M(w1, A)
        M2 = naive.M(w2, A)
        #update stats
        minus, plus = list_op.difference(M1,M2)
        len_minus = len(minus)
        len_plus = len(plus)
        len_M1 = len(M1)
        max_length_M1 = list_op.max_length(M1)
        sum_length_M1 = list_op.sum_length(M1)

        mean_minus += len_minus
        mean_plus += len_plus
        max_minus = max(max_minus, len_minus)
        max_plus = max(max_plus, len_plus)
        mean_M += len_M1
        mean_max_length_M += max_length_M1
        mean_sum_length_M += sum_length_M1
        max_M = max(max_M, len_M1)
        max_max_length_M = max(max_max_length_M, max_length_M1)
        max_sum_length_M = max(max_sum_length_M, sum_length_M1)
        #update current "progression" threshold if necessary
        if print_progression:
            while K >= N * current_threshold // 100 and current_threshold <= 100:
                print("|{}%".format(current_threshold), end="")
                sys.stdout.flush()
                current_threshold_id += 1
                current_threshold = thresholds[current_threshold_id]
    if print_progression:
        print("")
    mean_minus /= N
    mean_plus /= N
    mean_M /= N
    mean_max_length_M /= N
    mean_sum_length_M /= N
    #store stats in a dictionary
    d = {}
    d["A"] = A
    d["n"] = n
    d["N"] = N
    d["mean_M"] = mean_M
    d["max_M"] = max_M
    d["mean_minus"] = mean_minus
    d["mean_plus"] = mean_plus
    d["max_minus"] = max_minus
    d["max_plus"] = max_plus
    d["mean_max_length_M"] = mean_max_length_M
    d["max_max_length_M"] = max_max_length_M
    d["mean_sum_length_M"] = mean_sum_length_M
    d["max_sum_length_M"] = max_sum_length_M
    return d

def print_stats_verbose(d, name_stats):
    for x in name_stats:
        print("{}: {}".format(x,d[x]))

def print_stats_line(d, name_stats):
    for x in name_stats:
        print("{}\t".format(d[x]), end="")
    print("")
    sys.stdout.flush()

def print_stats_by_line_up_to_(K, A, N, name_stats):
    for k in range(20, K+1):
        d = rand_test(A, k, N, False)
        print_stats_line(d, name_stats)

print_stats_by_line_up_to_(100, A, N, name_stats)


#print_stats_verbose(rand_test(A, n, N), name_stats)

"""
w1 = "acbcabcbc"
w2 = "acbccbcbc"
list_op.print_difference(naive.M(w1, A), naive.M(w2, A))
"""