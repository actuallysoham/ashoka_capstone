import pandas as pd
import networkx as nx
import math
import numpy as np

def testGini(alloc):
	'''
	alloc : Allocation
	'''
	comb = []

	for i in alloc:
		comb.extend(i)

	comb = np.array(comb)

	total = 0
	for i, xi in enumerate(comb[:-1], 1):
		total = total + np.sum(np.abs(xi - comb[i:]))

	return total / (len(comb)**2 * np.mean(comb))

def testSatisfaction(alloc,G,E = 1):
	'''
	alloc : Allocation
	G : Graph
	E : Minimum exposure
	'''
	nodes = nx.nodes(G)
	comb = []

	for i in alloc:
		comb.extend(i)

	#for node in nodes:
		#print(f"count of node {node}: {comb.count(int(node))}")

	freq = {}
	for node in nodes:
		freq[node] = comb.count(int(node))

	vals = freq.values()
	val_above_threshold = [v for v in vals if v >= E]
	frac = len(val_above_threshold)/len(vals)
	#print(frac)
	return frac

def testInequality(alloc,G,k):
	'''
	alloc : Allocation
	G : Graph
	k : Recommendation set size
	'''
	nodes = nx.nodes(G)
	comb = []

	for i in alloc:
		comb.extend(i)

	ineq = 0
	for node in nodes:
		#exposure = max(comb.count(int(node)),1) # dealing with exposure = 0 case here
		exposure = comb.count(int(node))
		x = (exposure+1)/((len(nodes) * k)+1)
		#print(x)
		z = x * math.log(x,len(nodes))
		ineq = ineq + z
	
	ineq = -1 * ineq
	return ineq

def calcUtility(n,alloc, V):
	util = 0
	for item in alloc:
		util += V[int(n)][int(item)]
	return util

def testEnvy(alloc,G,V):
	'''
	alloc : Allocation
	G : Graph
	V : Relavence scores
	'''
	nodes = nx.nodes(G)
	mean_envy = 0

	for node1 in nodes:
		envy_sum = 0
		for node2 in nodes:
			if node1 != node2:
				n1_util = calcUtility(node1,alloc[int(node1)],V) 
				n2_util = calcUtility(node2,alloc[int(node2)],V) 
				envy = max((n1_util - n2_util),0)
				envy_sum += envy
		mean_envy += envy_sum/(len(nodes) - 1)

	return (mean_envy/len(nodes))

def testDummy(alloc, G):
	print("It's testing!")
	nodes = nx.nodes(G)
	comb = []

	for i in alloc:
		comb.extend(i)

	#print(comb)

	for node in nodes:
		print(f"count of node {node}: {comb.count(int(node))}")


def testLoss(alloc,top_alloc,G):
	'''
	alloc : Allocation
	G : Graph
	k : Recommendation set size
	'''
	nodes = nx.nodes(G)
	comb = []
	top_comb = []

	for i,j in zip(alloc,top_alloc):
		comb.extend(i)
		top_comb.extend(j)

	loss = 0
	for node in nodes:
		curr_loss = max((1 + top_comb.count(int(node)) - comb.count(int(node)))/(1+top_comb.count(int(node))),0)
		loss = loss + curr_loss
	
	loss = loss/ len(nodes)
	return loss

