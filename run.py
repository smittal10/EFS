import csv
import networkx as nx
import json
import operator
import re
from my_inverted_index import display_results
query = input("Search here: ")
ls=display_results(query)
print(ls)
