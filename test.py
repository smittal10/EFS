import networkx as nx
g=nx.DiGraph()
g.add_edge(1,2,weight=2)
g.add_edge(2,3,weight=1)
# g.edges()
print(g.edges())