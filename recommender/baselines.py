import pandas as pd
import networkx as nx
import random

from eval import tests

# Top k
# Random k
# MixedTR k
# Bottom k
# PopB k

def argmax(iterable):
    return max(enumerate(iterable), key=lambda x: x[1])[0]

def maxRel(curr,feasible_set,V):
	# relevance: v[cur][f \in F]
	# print('in maxRel: ')
	# print(feasible_set)
	
	maxRel = V[int(curr)][int(feasible_set[0])]
	maxRelItem = int(feasible_set[0])
	for item in feasible_set:
		if V[int(curr)][int(item)] > maxRel:
			maxRel = V[int(curr)][int(item)]
			maxRelItem = int(item)
	
	return maxRelItem

def calc_relevance(G):
	# consider all_simple_paths w. cutoff 2 (mutual friends)
	# add a base randomness (sample this from Twitter relevance dist)
	# normalise b/w (0,1)
	# return 2D matrix (NxN)

	nodes = nx.nodes(G)
	#print(len(nodes))
	rel = [[None] * len(nodes) for i in range(len(nodes))]
	mutual_counts = []
	
	for node1 in nodes:
		for node2 in nodes:
			n1 = [user for user in nx.all_neighbors(G, node1)]
			n2 = [user for user in nx.all_neighbors(G, node2)]
			mutual_counts.append(len(set(n1).intersection(n2)))
	c = 0
	maxlen = max(mutual_counts)		
	
	for node1 in nodes:
		for node2 in nodes:
			#print(f"({node1},{node2})")
			rel[int(node1)][int(node2)] = ((mutual_counts[c]/maxlen) + random.random())/2.0
			c = c + 1
			
	return rel

def topk(G,rel,k):
	nodes = nx.nodes(G)
	#print(nodes)
	alloc = [None] * len(nodes)
	
	for node in nodes:
		feasible_set = list(range(0, len(nodes)))
		feasible_set.remove(int(node)) # remove self node
		neighours = [user for user in nx.all_neighbors(G, node)] 
		feasible_set = list(set(feasible_set) - set(neighours)) # remove neighbours
		temp_alloc = []
		for rep in range(k):
			selected = maxRel(node,feasible_set,rel)
			temp_alloc.append(selected)
			feasible_set.remove(int(selected))
		
		alloc[int(node)] = temp_alloc # top k allocation
	
	return alloc

def maxRel_adj(curr,feasible_set,V,expose):
	# relevance: v[cur][f \in F]
	# print('in maxRel: ')
	# print(feasible_set)
	
	maxRel = 0.5*V[int(curr)][int(feasible_set[0])] + 0.5 - 0.5*(expose[int(feasible_set[0])]/(1+sum(expose)))
	maxRelItem = int(feasible_set[0])
	for item in feasible_set:
		if (0.5*V[int(curr)][int(item)] + 0.5 - 0.5*expose[int(item)]/(1+sum(expose))) > maxRel:
			maxRel = 0.5*V[int(curr)][int(item)] + 0.5 - 0.5*expose[int(item)]/(1+sum(expose))
			maxRelItem = int(item)
	
	return maxRelItem

def popBk(G,rel,k):
	nodes = nx.nodes(G)
	#print(nodes)
	expose = [0] * len(nodes)
	alloc = [None] * len(nodes)
	
	for node in nodes:
		feasible_set = list(range(0, len(nodes)))
		feasible_set.remove(int(node)) # remove self node
		neighours = [user for user in nx.all_neighbors(G, node)] 
		feasible_set = list(set(feasible_set) - set(neighours)) # remove neighbours
		temp_alloc = []
		for rep in range(k):
			selected = maxRel_adj(node,feasible_set,rel,expose)
			expose[selected] = expose[selected] + 1
			temp_alloc.append(selected)
			feasible_set.remove(int(selected))
		
		alloc[int(node)] = temp_alloc 
	
	return alloc

def randomk(G,rel,k):
	nodes = nx.nodes(G)
	#print(nodes)
	alloc = [None] * len(nodes)
	
	for node in nodes:
		feasible_set = list(range(0, len(nodes)))
		feasible_set.remove(int(node)) # remove self node
		neighours = [int(user) for user in nx.all_neighbors(G, node)] 
		feasible_set = list(set(feasible_set) - set(neighours)) # remove neighbours
		alloc[int(node)] = random.sample(feasible_set, k) # random allocation
	
	return alloc

def minExpose(curr,feasible_set,expose):
	
	#print(f'default minrel is {minRel}')
	minExposeItem = feasible_set[0]
	minExpose = expose[minExposeItem]
	for item in feasible_set:
		#print(f'current Exposeevance b/w {int(curr)} and {int(item)} is {V[int(curr)][int(item)]}')
		if expose[item] <= minExpose:
			#print(f'condition was TRUE -===')
			minExpose = expose[item]
			minExposeItem = item
	
	return minExposeItem

def bottomk(G,rel,k):
	nodes = nx.nodes(G)
	expose = [0] * len(nodes)
	alloc = [None] * len(nodes)
	
	for node in nodes:
		feasible_set = list(range(0, len(nodes)))
		feasible_set.remove(int(node)) # remove self node
		neighours = [user for user in nx.all_neighbors(G, node)] 
		feasible_set = list(set(feasible_set) - set(neighours)) # remove neighbours
		temp_alloc = []
		#print(f'current node is {node}')
		#print()
		for rep in range(k):
			selected = minExpose(node,feasible_set,expose)
			expose[selected] = expose[selected] + 1
			#print(f"selected is {selected}")
			temp_alloc.append(selected)
			feasible_set = list(set(feasible_set) - set([int(selected)]))
			#print(f"feasbility set is {feasible_set}")
		
		alloc[int(node)] = temp_alloc # top k allocation
	
	return alloc

# =====================
# Fair Rec Algo
# =====================

def fairRec(G,V,k):
	'''
	G: Graph
	k: Recommendation set size
	V: Relevance scores; V[u][p] is relevance of p for u
	'''
	nodes = nx.nodes(G)
	A = [None]*len(nodes) # initial allocation set
	F = [None]*len(nodes) # initial feasblity sets
	#print('hello')
	for node in nodes:
		feasible_set = list(range(0, len(nodes)))
		feasible_set.remove(int(node)) # remove self node
		neighours = [int(user) for user in nx.all_neighbors(G, node)] 
		feasible_set = list(set(feasible_set) - set(neighours)) # remove neighbours
		F[int(node)] = feasible_set

	alpha = 1
	l = alpha * k
	S = [l for  node in nodes]
	T = l * len(nodes)

	n_ord = [int(node) for node in nodes]
	B = roundRobin(G,S,T,V,n_ord,F)
	return B

def maxRelevance(curr,feasible_set,S,V):
	# relevance: v[cur][f \in F]
	# print('in maxRel: ')
	
	#print(feasible_set)

	empty_users = []
	for i in range(len(S)):
		if S[i] <= 0:
			empty_users.append(i)

	feasible_set = list(set(feasible_set) - set(empty_users))
	if len(feasible_set) == 0:
		return -1
	else:
		#print(feasible_set)
		#print(f'len of f-set is :{len(feasible_set)}')
		maxRel = V[int(curr)][int(feasible_set[0])]
		maxRelItem = int(feasible_set[0])
		for item in feasible_set:
			if V[int(curr)][int(item)] > maxRel:
				maxRel = V[int(curr)][int(item)]
				maxRelItem = int(item)
		
		return maxRelItem


def roundRobin(G,S,T,V,n_ord,F):
	B = [None]*len(nx.nodes(G))
	x = len(nx.nodes(G))
	r = 0
	exitWhile = False
	
	while exitWhile == False:
		r = r + 1
		for i in range(0,len(nx.nodes(G))):
			
			if len(F[n_ord[i]]) == 0:
				x = i - 1
				#print(f'=== exiting on p = 0 condition ====')
				exitWhile = True
				break

			p = maxRelevance(n_ord[i],F[n_ord[i]],S,V)
			#print(p)
			if p == -1:
				x = i - 1
				#print(f'=== exiting on p = 0 condition ====')
				exitWhile = True
				break

			if B[n_ord[i]] is None: B[n_ord[i]] = [p]
			else: B[n_ord[i]].append(p)

			F[n_ord[i]].remove(p)
			S[p] = S[p] - 1
			#print(S)
			T = T - 1
			if T == 0:
				x = i
				#print(f'=== exiting on T = 0 condition ====')
				exitWhile = True
				break

	return B

# =====================

#print(argmax([3,2,5,4,3,9,2,9]))

test_er = nx.read_edgelist('../datasets/synth/ws_200.csv')
print(test_er)

'''
curr_labels = sorted(test_er)
simp_ind = 0
mapping = dict()
for lab in curr_labels:
	mapping[lab] = simp_ind
	simp_ind = simp_ind + 1

test_er = nx.relabel_nodes(test_er, mapping)
'''

relevance_scores  = calc_relevance(test_er)
eval_scores = []
#alloc = topk(test_er,relevance_scores,3)
#res = tests.testGini(alloc)
#print(res)

#alloc = popBk(test_er,relevance_scores,3)
#alloc2 = topk(test_er,relevance_scores,3)
#print(alloc)
#print(alloc2)
#res = tests.testDummy(alloc,test_er)
#res = tests.testDummy(alloc2,test_er)


test_runs = 20

for k in range(1,test_runs):
	#print(f'at iteration {k}')
	#top_alloc = topk(test_er,relevance_scores,k)
	alloc = popBk(test_er,relevance_scores,k)
	#res = tests.testGini(alloc)
	#res = tests.testInequality(alloc, test_er, k)
	#res = tests.testLoss(alloc, top_alloc, test_er)
	#res = tests.testSatisfaction(alloc, test_er, k)
	res = tests.testEnvy(alloc, test_er, relevance_scores)
	eval_scores.append(res)

#print(eval_scores)
#print(f_eval_scores)



for k_print in range(0,test_runs-1):
	print(f"({k_print+1},{eval_scores[k_print]})", end='')


