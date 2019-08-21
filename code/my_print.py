import ahocorasick_op, graph_build, graph_draw, graph_op, list_op, my_rand, naive
import sys, random, itertools
import tryalgo

def percent(a,b):
	if b != 0:
	    return a/b*100
	else:
		return 0

def connexity_test(A, m, n, frac, N, print_progression = False, line_print = False):
    AC_c = 0
    AC_sc = 0
    AC_empty = 0
    dB_c = 0
    dB_sc = 0
    dB_empty = 0
    h_c = 0
    h_empty = 0

    AC_c_and_dB_c = 0
    AC_c_and_not_dB_c = 0
    not_AC_c_and_not_dB_c = 0
    not_AC_c_and_dB_c = 0

    AC_sc_and_dB_sc = 0
    AC_sc_and_not_dB_sc = 0
    not_AC_sc_and_not_dB_sc = 0
    not_AC_sc_and_dB_sc = 0

    AC_c_and_h_c = 0
    AC_c_and_not_h_c = 0
    not_AC_c_and_not_h_c = 0
    not_AC_c_and_h_c = 0

    AC_sc_and_h_c = 0
    AC_sc_and_not_h_c = 0
    not_AC_sc_and_not_h_c = 0
    not_AC_sc_and_h_c = 0

    dB_c_and_h_c = 0
    dB_c_and_not_h_c = 0
    not_dB_c_and_not_h_c = 0
    not_dB_c_and_h_c = 0

    dB_sc_and_h_c = 0
    dB_sc_and_not_h_c = 0
    not_dB_sc_and_not_h_c = 0
    not_dB_sc_and_h_c = 0

    not_dB_c_and_h_empty = 0
    
    mean_AC = 0
    mean_dB = 0
    mean_h = 0

    mean_nb_cc_AC = 0
    mean_nb_cc_dB = 0
    mean_nb_cc_h = 0

    mean_max_len_cc_AC = 0
    mean_max_len_cc_dB = 0
    mean_max_len_cc_h = 0
	

    #thresholds to keep track of the computation progression
    thresholds = [5*i for i in range(1,22)]
    current_threshold_id = 0
    current_threshold = thresholds[current_threshold_id]
    for K in range(N):
        F = my_rand.rand_list_fraction(m, A, frac)
        G_AC = graph_build.acGraph_prime_n(A, F, n)
        G_dB = graph_build.deBruijn_n(A, F, n)
        #print(G_dB[0], G_dB[1])
        G_h = graph_build.hammmingGraph(A, F, n)
        
        nodes, _ = G_AC
        ccs = graph_op.connected_components(G_AC)
        mean_AC += len(nodes)
        mean_nb_cc_AC += len(ccs)
        mean_max_len_cc_AC += list_op.max_length(ccs)
        nodes, _ = G_dB
        ccs = graph_op.connected_components(G_dB)
        mean_dB += len(nodes)
        mean_nb_cc_dB += len(ccs)
        mean_max_len_cc_dB += list_op.max_length(ccs)
        nodes, _ = G_h
        ccs = graph_op.connected_components(G_h)
        mean_h += len(nodes)
        mean_nb_cc_h += len(ccs)
        mean_max_len_cc_h += list_op.max_length(ccs)


        AC_is_c = graph_op.is_connected(G_AC)
        AC_is_sc = graph_op.is_strongly_connected(G_AC)
        dB_is_c = graph_op.is_connected(G_dB)
        dB_is_sc = graph_op.is_strongly_connected(G_dB)
        h_is_c = graph_op.is_connected(G_h)
        if AC_is_c:
            AC_c += 1
        if AC_is_sc:
            AC_sc += 1
        if dB_is_c:
            dB_c += 1
        if dB_is_sc:
            dB_sc += 1
        if h_is_c:
            h_c += 1
        else:
            pass
            """
            nodes, edges = G_h
            cc = tryalgo.strongly_connected_components.tarjan(edges)
            if list_op.min_length(cc) > 2:
                print(K)
                print("F: {}".format(F))
                
                print("nodes: {}".format(nodes))
                print("#nodes: {}".format(len(nodes)))
                
                print("#components: {}".format(len(cc)))
                print("max size component: {}".format(list_op.max_length(cc)))
                graph_draw.draw_nx(graph_draw.listlist_to_nx(G_h))
            """
        if AC_is_c and dB_is_c:
            AC_c_and_dB_c += 1
        if AC_is_c and (not dB_is_c):
            AC_c_and_not_dB_c += 1
        if (not AC_is_c) and (not dB_is_c):
            not_AC_c_and_not_dB_c += 1
        if (not AC_is_c) and dB_is_c:
            not_AC_c_and_dB_c += 1
            #print_everything(A, F, n)
        
        if AC_is_sc and dB_is_sc:
            AC_sc_and_dB_sc += 1
        if AC_is_sc and (not dB_is_sc):
            AC_sc_and_not_dB_sc += 1
        if (not AC_is_sc) and (not dB_is_sc):
            not_AC_sc_and_not_dB_sc += 1
        if (not AC_is_sc) and dB_is_sc:
            not_AC_sc_and_dB_sc += 1
        
        if AC_is_c and h_is_c:
            AC_c_and_h_c += 1
        if AC_is_c and (not h_is_c):
            AC_c_and_not_h_c += 1
        if (not AC_is_c) and (not h_is_c):
            not_AC_c_and_not_h_c += 1
        if (not AC_is_c) and h_is_c:
            not_AC_c_and_h_c += 1
        
        if AC_is_sc and h_is_c:
            AC_sc_and_h_c += 1
        if AC_is_sc and (not h_is_c):
            AC_sc_and_not_h_c += 1
        if (not AC_is_sc) and (not h_is_c):
            not_AC_sc_and_not_h_c += 1
        if (not AC_is_sc) and h_is_c:
            not_AC_sc_and_h_c += 1
        
        if dB_is_c and h_is_c:
            dB_c_and_h_c += 1
        if dB_is_c and (not h_is_c):
            dB_c_and_not_h_c += 1
        if (not dB_is_c) and (not h_is_c):
            not_dB_c_and_not_h_c += 1
        if (not dB_is_c) and h_is_c:
            not_dB_c_and_h_c += 1
        
        if dB_is_sc and h_is_c:
            dB_sc_and_h_c += 1
        if dB_is_sc and (not h_is_c):
            dB_sc_and_not_h_c += 1
        if (not dB_is_sc) and (not h_is_c):
            not_dB_sc_and_not_h_c += 1
        if (not dB_is_sc) and h_is_c:
            not_dB_sc_and_h_c += 1
        
        nodes, _ = G_AC
        if nodes == []:
            AC_empty += 1

        nodes, _ = G_dB
        if nodes == []:
            dB_empty += 1

        nodes, _ = G_h
        if nodes == []:
            h_empty += 1
            if not dB_is_c:
                not_dB_c_and_h_empty += 1
        #update current "progression" threshold if necessary
        if print_progression:
            while K >= N * current_threshold // 100 and current_threshold <= 100:
                print("|{}%".format(current_threshold), end="")
                sys.stdout.flush()
                current_threshold_id += 1
                current_threshold = thresholds[current_threshold_id]
    mean_AC /= N
    mean_dB /= N
    mean_h /= N
    mean_nb_cc_AC /= N
    mean_nb_cc_dB /= N
    mean_nb_cc_h /= N
    mean_max_len_cc_AC /= N
    mean_max_len_cc_dB /= N
    mean_max_len_cc_h /= N
    if print_progression:
        print("")
    if line_print:
        print("{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}".format(A, m, n, frac, len(F), N,
            percent(AC_c, N), percent(dB_c, N), percent(h_c, N),
            percent(AC_sc, N), percent(dB_sc, N),
            percent(AC_empty, N), percent(dB_empty, N), percent(h_empty, N),
            percent(not_AC_c_and_not_h_c, N), #cases handled by theorem (with AC)
            percent(not_AC_c_and_not_h_c, max(N - h_c, 1)), #h-non connexity caught by theorem (with AC)
            percent(not_dB_c_and_not_h_c, N), #cases handled by theorem (with dB)
            percent(not_dB_c_and_not_h_c, max(N - h_c, 1)), #h-non connexity caught by theorem (with dB)
            percent(not_dB_c_and_h_c, max(N - dB_c, 1)), #counterexamples to theorem
            percent(AC_sc_and_dB_sc + not_AC_sc_and_not_dB_sc, N), #when both AC and dB have strong connexity at the same time
            percent(not_AC_c_and_dB_c, N), #counterexamples to: (not AC_c) => (not dB_c)
            mean_AC, mean_dB, mean_h, mean_nb_cc_AC, mean_nb_cc_dB, mean_nb_cc_h, mean_max_len_cc_AC, mean_max_len_cc_dB, mean_max_len_cc_h))

        sys.stdout.flush()
    else:
        print("A={}, m(F)={}, n={}, frac={}, |F|={}".format(A, m, n, frac, len(F)))
        print("dB_c: {}% ({}/{})".format(dB_c / N * 100, dB_c, N))
        print("dB_sc: {}% ({}/{})".format(dB_sc / N * 100, dB_sc, N))
        print("h_c: {}% ({}/{})".format(h_c / N * 100, h_c, N))
        print("h_empty: {}% ({}/{})".format(h_empty / N * 100, h_empty, N))
        print("Cases handled by theorem: {}% ({}/{})".format(not_dB_c_and_not_h_c / N * 100, not_dB_c_and_not_h_c, N))
        print("h-non connexity caught by theorem: {}% ({}/{})".format(not_dB_c_and_not_h_c / max(N - h_c, 1) * 100, not_dB_c_and_not_h_c, N - h_c))
        print("Counterexamples to theorem: {}% ({}/{})".format(not_dB_c_and_h_c / max(N - dB_c, 1) * 100, not_dB_c_and_h_c, N - dB_c))

def print_everything(A, F, n):
    print("F: {}".format(F))
    print("#motifs: {}".format(len(F)))

    G_AC_F_prime = graph_build.acGraph_prime(A, F)
    labels, edges = G_AC_F_prime
    print("AC_prime")
    print("#nodes: {}".format(len(labels)))
    print(labels)
    print(edges)
    graph_draw.draw_nx(graph_draw.listlist_to_nx(G_AC_F_prime))

    G = graph_build.deBruijn(A, F)
    nodes, edges = G
    print("dB")
    print("#nodes: {}".format(len(nodes)))
    print(nodes)
    print(edges)
    graph_draw.draw_nx(graph_draw.listlist_to_nx(G))

    G = graph_build.hammmingGraph(A, F, n)
    nodes, edges = G
    print("hamming")
    print("#nodes: {}".format(len(nodes)))
    #print(nodes)
    ccs = graph_op.strongly_connected_components(G)
    print("connected components: {}".format(len(ccs)))
    list_op.print_lengths(ccs)
    #print(ccs)
    graph_draw.draw_nx(graph_draw.listlist_to_nx(G))

def print_per_n_from(A, F, n_ini, draw=False):
    n = n_ini
    print("F: {}".format(F))
    print("#motifs: {}".format(len(F)))
    while True:
        G = graph_build.hammmingGraph(A, F, n)
        nodes, _ = G
        ccs = graph_op.strongly_connected_components(G)
        print("n: {}". format(n), end=" | ")
        print("#nodes: {}".format(len(nodes)), end=" | ")
        print("#ccs: {}".format(len(ccs)), end=" | ")
        list_op.print_lengths(ccs)
        if draw:
            graph_draw.draw_nx(graph_draw.listlist_to_nx(G))
        n += 1


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

def find_all_non_c_aux(A, words, len_words, n, current_F, i, rem, verbose):
	if rem == 0:
		#print(current_F)
		G_h = graph_build.hammmingGraph(A, current_F, n)
		if not graph_op.is_connected(G_h):
			#print(current_F)
			if verbose:
				G_AC_F_prime = graph_build.acGraph_prime(A, current_F)
				labels, edges = G_AC_F_prime
				print("AC_prime")
				print("#nodes: {}".format(len(labels)))
				print(labels)
				print(edges)
				graph_draw.draw_nx(graph_draw.listlist_to_nx(G_AC_F_prime))
				print("hamming")
				nodes, _ = G_h
				ccs = graph_op.strongly_connected_components(G_h)
				print("n: {}". format(n), end=" | ")
				print("#nodes: {}".format(len(nodes)), end=" | ")
				print("#ccs: {}".format(len(ccs)), end=" | ")
				list_op.print_lengths(ccs)
				#graph_draw.draw_nx(graph_draw.listlist_to_nx(G_h))
			G_AC = graph_build.acGraph_prime(A, current_F)
			if not graph_op.is_connected(G_AC):
				return (1, 1)
			else:
				return (0, 1)
		else:
			return (0, 0)
	else:
		K = 0 ; N = 0
		for j in range(i+1, len_words - rem + 1):
			new_F = [u for u in current_F]
			new_F.append(words[j])
			(new_K, new_N) = find_all_non_c_aux(A, words, len_words, n, new_F, j, rem-1, verbose)
			K += new_K
			N += new_N
		return (K, N)
		

def find_all_non_c(A, n, m, k, verbose = False):
	letters = "".join(A)
	words = []
	for li in itertools.product(letters, repeat=m):
		u = "".join(li)
		words.append(u)
	len_words = len(words)
	K, N = find_all_non_c_aux(A, words, len_words, n, [], -1, k, verbose)
	print(K, N, percent(K,N))
	