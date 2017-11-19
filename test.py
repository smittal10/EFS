import networkx as nx
g=nx.DiGraph()
g.add_edge(1,2,weight=2)
g.add_edge(2,3,weight=1)
# g.edges()
print(g.edges())

d={2:[3,4,5],3:[1]}
for i,j in d.items():
	print(len(j))
	for auth in j:
		print(auth)
