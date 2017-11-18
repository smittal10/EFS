import csv
import networkx as nx
import json
import matplotlib.pyplot as plt
my_dict={}
with open('DBLP-SIGWEB/paper_authors.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=int(row[0])
		if key in my_dict:
			my_dict[key].append(int(row[1]))
		else:
			my_list=[]
			my_list.append(int(row[1]))
			my_dict[key]=my_list
# with open('DBLP-SIGWEB/my_dict.json', 'w') as fp:
#     json.dump(my_dict, fp)

co_author={}
for paper,authors in my_dict.items():
	if len(authors)==1:
		break
	ls = authors;
	for author in authors:
		ls.remove(author)
		for assoc_auth in ls:
			if author in co_author:
				if assoc_auth in co_author[author]:
					co_author[author][assoc_auth] += 1
				else:
					co_author[author][assoc_auth]=1
			else:
				temp={}
				temp[assoc_auth]=1
				co_author[author]=temp;
# with open('DBLP-SIGWEB/co_authors.json', 'w') as fp:
#     json.dump(co_author, fp)
seed_scores={}
with open('DBLP-SIGWEB/authors_info.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=int(row[0])
		seed_scores[key] = float(row[1])
# with open('DBLP-SIGWEB/seed_scores.json', 'w') as fp:
#     json.dump(seed_scores, fp)		


G=nx.DiGraph();
for author,assocs in co_author.items():
	for author2,edge in assocs.items():
		G.add_edge(author,author2,weight=edge)
# print(G.edges(data=True))
# pos=nx.spring_layout(G)

# nx.draw(G,pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.savefig('DBLP-SIGWEB/graph2.png')
pr = nx.pagerank(G,personalization=seed_scores,max_iter=50)

with open('DBLP-SIGWEB/pagerank.json', 'w') as fp:
    json.dump(pr, fp)

i=0
for key,value in pr.items():
	print(key)
	print(value)
	i=i+1
	if i==10:
		break






