import ahocorasick_op, graph_build, graph_draw, graph_op, list_op, my_rand, naive
import sys, random
import tryalgo

import my_print

A = ["A","C","U"]
n = 10
N = 1000
name_stats = ["A", "n", "N", "mean_M", "max_M", "mean_minus", "mean_plus", "max_minus", "max_plus", 
                "mean_max_length_M", "max_max_length_M", "mean_sum_length_M", "max_sum_length_M"]

#F = ["ACA", "CAAA", "AAC"]

#2 simple cycles
#F = ["AAAA", "CCCC", "AACC", "CCAA", "ACAC", "CACA", "ACCA", "CAAC"]

#A'_F connected but DB_F is not
#F = ["AACC", "ACAA", "ACAC", "CAA"]
#F = ["AACC", "ACAA", "ACAC", "CAA", "AAAA"]

#Disconnecting DB_F with few forbidden motifs
#F = ["AAAC", "CAAC", "CACC", "ACCA", "CCCA"]

#stabilizes at n=24
#F = ['CACACC', 'CCCAAA', 'CCCCCC', 'CAACAC', 'CCACCC', 'ACACCC', 'ACCACA', 'ACACCA', 'AACCCA', 'AAACCC', 'AACCAC', 'ACAACA', 'CCCAAC', 'AACCAA', 'AACAAA', 'AACAAC', 'ACCACC', 'CCACAC', 'CAAAAC', 'CCCACC', 'ACAACC', 'AACACA', 'ACCAAA', 'AAAAAA', 'CAAACA']

#stabilizes at n=11
#F = ['CAAAAC', 'ACAAAC', 'ACACAA', 'AACACA', 'CAACAC', 'CAAACA', 'ACAACC', 'CACCCC', 'CCACCA', 'AAAACC', 'ACACCA', 'CCCCAC', 'ACAACA', 'AACCAA', 'CCACAA', 'CCCAAC', 'AACAAA', 'ACACCC', 'ACAAAA', 'ACCACA', 'AACCCA', 'AAAAAC', 'AAAAAA', 'CACAAC', 'CCAACC', 'CAAACC', 'ACCCCA', 'ACCCCC', 'CACACA', 'CCAAAC', 'CCAAAA', 'ACCACC', 'AAAACA', 'AACCAC', 'CCCCAA', 'AAACCA', 'CAACCA', 'CAAAAA']

#few motifs (0.2), #ccs increases with n (one big component, many much smaller components)
#F = ['CAACCC', 'CCCCCA', 'CAACAC', 'CACAAA', 'CAAACA', 'CACACA', 'ACAACA', 'AAAAAC', 'AAACAA', 'CCACCA', 'AAAACA', 'CCACAA']

#F = ["CAAAA", "AAAAC"]

#F = ["AAA", "CAA", "ACAA", "ACACAA"]

#2 cycles, #ccs increases, all ccs are tiny
#F = ["CC", "AAA"]
#F = ["AAA", "CAC"]

#F = ["ACAC", "CCC"]

#"barely" connected
#F = ['CACA', 'ACCA', 'CCCA', 'ACAC', 'CACC', 'CAAA']

#few motifs, 3 "big" ccs
#F = ['AAAA', 'ACCA', 'CCCC']

#m = list_op.max_length(F)

"""
m = 5
F = my_rand.rand_list_fraction(m, A, .5)
"""
"""
m = list_op.max_length(F)
my_print.print_everything(A, F, 10)
my_print.print_per_n_from(A, F, m)
"""

"""
for i in range(1, 33):
    my_print.find_all_non_c(A, 10, 5, i, verbose=False)
"""

#my_print.connexity_test(A, 3, 8, .05, 100, line_print=True, print_progression=True)



for num in range(1,100):
    my_print.connexity_test(A, 5, 10, num / 100, 100, line_print=True)
    #my_print.connexity_test(A, 5, 10, num / 33, 1000, line_print=True)




#my_print.connexity_test(A, 4, 9, .2, 1)


"""
#Test rand_list_fraction
F = my_rand.rand_list_fraction(5, A, .2)
print("F")
print(len(F))
print(F)
"""

#F = ['CACCA', 'AAACA', 'CAAAC', 'ACAAA', 'AAAAA', 'ACCCC', 'ACACA', 'CCAAC', 'ACACC', 'ACCAA', 'ACCCA', 'CCCAC', 'AACAA', 'ACAAC', 'AACAC', 'AAAAC']

#F = ['ACCAA', 'CCCAC', 'AAACA', 'CAAAC', 'CACAC', 'CCACA', 'ACCCA', 'ACACA', 'CCCCC', 'CACCC', 'ACAAC', 'AAAAA', 'ACACC', 'ACCAC', 'AACCC', 'CAAAA']

#F = ['CCAAA', 'AAACC', 'CAACA', 'ACCAC', 'AACCA', 'AACAA', 'CCCAC', 'CAAAA', 'ACAAC', 'ACAAA', 'CACAC', 'CCCCC', 'CCCCA', 'AACCC', 'AACAC', 'CAACC']
"""
#Test hammingGraph
G = graph_build.hammmingGraph(A, F, n)
nodes, edges = G
print("G")
print(len(nodes))
print(nodes)
graph_draw.draw_nx(graph_draw.listlist_to_nx(G))

#Test deBruijn
G = graph_build.deBruijn_inf(A, F)
nodes, edges = G
print("dB")
print(nodes)
print(edges)
graph_draw.draw_nx(graph_draw.listlist_to_nx(G))
"""
"""
#Test Aho-Corasick automaton
#w = "AACACCACCACCACAAAAAACCCCCCACACACACCACCCCACACA"
AC = ahocorasick_op.build_auto(F)
nodes, edges, failure_links = AC.dump()
print(nodes)
print(edges)
print(failure_links)
"""

#my_print.print_stats_by_line_up_to_(100, A, N, name_stats)


#my_print.print_stats_verbose(rand_test(A, n, N), name_stats)

"""
w1 = "acbcabcbc"
w2 = "acbccbcbc"
list_op.print_difference(naive.M(w1, A), naive.M(w2, A))
"""