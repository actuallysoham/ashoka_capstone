import pandas as pd

def fairRec(U,G,k,V):
	'''
	U: Set of users
	G: G[u] is the list of users followed by u in U
	k: Recommendation set size
	V: Relevance scores; V[u][p] is relevance of p for u
	'''
	A = [None]*len(U) # initial allocation set
	U_ord = sorted(U)
	F = dict()
	print('hello')
	for u in U_ord:
		F[u] = U - set(u) # remove a

	#print(F['a'])
	#print(F['b'])
	#print(F['c'])

	alpha = 1
	l = alpha * k
	S = [l for  u in U_ord]
	T = l * len(U)
	# call roundRobin(len(U_ord), T, V, U_ord, F)

def roundRobin(m,T,V,S,F):
	B = [None]*len(U)
	x = m
	r = 0
	while(True):
		r = r + 1
		for i in range(0,m):
			#argmax_i()
		if T == 0:
			break
		# exit condition 2: if max feasibility set is 0


def main():
	U = {'a','b','c'}
	fairRec(U,'none',5,'none')

main()