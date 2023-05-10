import networkx as nx
import os
import pandas as pd

# make set of all users
# order set
# add all nodes to graph
# add pairwise edges
# export as gexf, viz in gephi

all_users = set()

r1 = os.listdir('following/')
for filename in r1:
	df = pd.read_excel('following/'+str(filename))
	followings = list(df['username'])
	all_users.update(followings)

r1 = [name[:-5] for name in r1]
all_users.update(r1)
print(len(all_users))
all_users_ord = list(all_users)

G = nx.Graph()
G.add_nodes_from(range(len(all_users_ord)))
#G.add_edge(1,2)

for filename in r1:
	df = pd.read_excel('following/'+str(filename)+'.xlsx')
	followings = list(df['username'])
	for following in followings:
		G.add_edge(all_users_ord.index(filename),all_users_ord.index(following))

remove = [node for node, degree in G.degree() if degree < 5]
#G.remove_nodes_from(remove)
print(G)
nx.write_gexf(G, "synth/ashoka_large.gexf")
nx.write_edgelist(G,'synth/ashoka_large.csv', data=False)