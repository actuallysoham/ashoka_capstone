import networkx as nx

er = nx.erdos_renyi_graph(200,0.075, directed = True)
ws = nx.watts_strogatz_graph(200,35,0.25)
ba = nx.barabasi_albert_graph(200,15)

#print(er)
#print(ws)
#print(ba)

nx.write_gexf(er, "synth/er_200.gexf")
nx.write_gexf(ws, "synth/ws_200.gexf")
nx.write_gexf(ba, "synth/ba_200.gexf")
nx.write_edgelist(er,'synth/er_200.csv', data=False)
nx.write_edgelist(ws,'synth/ws_200.csv', data=False)
nx.write_edgelist(ba,'synth/ba_200.csv', data=False)

# relevance can be number of mutuals -> can be calculate from edges directly