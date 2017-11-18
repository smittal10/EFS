import csv
import operator
import json
import re
inverted_index={}
with open('/home/saloni/Downloads/DBLP-SIGWEB/concepts.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=row[1].lower()
		if key in inverted_index:
			inverted_index[key].append(int(row[0]))
		else:
			my_list=[]
			my_list.append(int(row[0]))
			inverted_index[key]=my_list
with open('/home/saloni/Downloads/DBLP-SIGWEB/author_tags.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=row[1].lower()
		if key in inverted_index:
			inverted_index[key].append(int(row[0]))
		else:
			my_list=[]
			my_list.append(int(row[0]))
			inverted_index[key]=my_list
def search_query(input_query,inverted_index):
	paper_id=[]
	author_id=[]
	# pattern = re.compile('[\W_]+')
	# word = pattern.sub(' ',input_query)
	pattern = re.compile(input_query)
	for key in inverted_index.keys():
		if (pattern.search(key)):
			for paper in inverted_index[key]:
				paper_id.append(paper)
	paper_id=set(paper_id)
	paper_id=list(paper_id)
	return paper_id
paper_authors={}
with open('/home/saloni/Downloads/DBLP-SIGWEB/paper_authors.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=int(row[0])
		if key in paper_authors:
			paper_authors[key].append(int(row[1]))
		else:
			my_list=[]
			my_list.append(int(row[1]))
			paper_authors[key]=my_list
display_info={}
with open('/home/saloni/Downloads/DBLP-SIGWEB/display_info.csv','rt') as obj:
	table = csv.reader(obj,delimiter=',')
	for row in table:
		key=int(row[0])
		my_list=[]
		my_list.append(row[1])
		my_list.append(row[2])
		my_list.append(row[3])
		my_list.append(row[4])
		my_list.append(row[5])
		my_list.append(row[6])
		display_info[key]=my_list
		
# with open('/home/saloni/Downloads/DBLP-SIGWEB/my_dict.json', 'r') as fp:
#     paper_authors = json.load(fp)
pr={}
with open('/home/saloni/Downloads/DBLP-SIGWEB/pagerank.json', 'r') as fp:
    pr = json.load(fp)
ppr={}
for key,value in pr.items():
	key=int(key)
	value=float(value)
	ppr[key]=value
pr=ppr
# i=0
# for key,value in pr.items():
# 	print(key)
# 	print(value)
# 	i=i+1
# 	if i==2:
# 		break

# print(pr)
query = input("Search here: ")
paper_list=search_query(query,inverted_index)
# print(paper_list)
if 1458194 in paper_list:
	print('hi')
author_ids=[]
for paper_id in paper_list:
	for author_id in paper_authors[paper_id]:
		author_ids.append(author_id)
author_ids=list(set(author_ids))
# print(author_ids)
if 81100097085 in author_ids:
	print("yo")

result=[]
for author_id in author_ids:
	if author_id in pr.keys():
		result.append((author_id,pr[author_id]))
# print(result)

final_res=sorted(result,key=lambda x:x[1],reverse=True)
i=0
for item in final_res:
	print(item)
	print("['Author_Name','Year_first','Year_last','Total_Publications','Citation_Count','Avg_cite']")
	print(display_info[item[0]])
	i=i+1
	if i==7:
		break









