from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import networkx as nx
import matplotlib.pyplot as plt
Graph={}
levels=3
#limit=""
list_of_nodes=["Machine Learning"]
def id_extractor(search_string):
    #print(type(wikipedia.search(search_string)))
    query = wikipedia.search(search_string)[0]
    #print(query)
    new_string = ""
    for i in query:
        if i == " ":
            new_string = new_string + '_'
        else:
            new_string = new_string + i
    #print("New string")
    print("Searching for {}".format(new_string))

    res = requests.get("https://en.wikipedia.org/wiki/"+new_string)
    soup = bs(res.text, "html.parser")
    wikidata = []
    for link in soup.find_all("a"):
        url = link.get("href", "")
        if "//www.wikidata.org/" in url:
            wikidata.append(url)
            #print(url)
    #print(wikidata)

    #count = 0
    wikidata_id  = ""
    for i in wikidata[0]:
        if i == 'Q' or i == '1' or i == '2' or i =='0' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            wikidata_id = wikidata_id + i
    res = requests.get(wikidata[0])
    soup = bs(res.text, "html.parser")
    #print(soup)
    node=""
    for hit in soup.findAll(attrs={'class' : 'wikibase-title-label'}):
        node= hit.text
    return wikidata_id,node


def result_gen_children(prop,id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    q="""
    SELECT ?item ?itemLabel 
    WHERE
    {
        ?item wdt:P361?/wdt:P279? wd:Q245652 .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    } 
    """
    q=re.sub(r"Q245652",id,q)
    #q=re.sub(r"P361",prop,q)
    
    sparql.setQuery(q)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

    
def result_gen_parent(prop,id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    q="""
    SELECT ?item ?itemLabel
    WHERE
    {
        wd:Q245652 wdt:P361?/wdt:P279? ?item   .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    } 
    """
    q=re.sub(r"Q245652",id,q)
    sparql.setQuery(q)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def chilldren(node,id,level):
    if level==levels:
        return
    
    results = result_gen_children("P361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])
    
    if node not in Graph.keys():
        Graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemLabel.value"] ) :
            print(y)
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            if y not in Graph[node]:
                Graph[node].append(y)
            if y not in Graph:
                chilldren(y,x,level+1)

def parent(node,id,level):
    if level==levels:
        return

    results = result_gen_parent("P361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])
    
    if node not in Graph.keys():
        Graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemLabel.value"] ) :
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            print(y)
            if y not in Graph:
                Graph[y]=[]
                Graph[y].append(node)
                parent(y,x,level+1)
            else:
                Graph[y].append(node)

def Graph_gen():
    for node in list_of_nodes:
        id,node=id_extractor(node)
        chilldren(node,id,0)
        parent(node,id,0)
        

Graph_gen()
for x in Graph:
    Graph[x]=list(dict.fromkeys(Graph[x]))

print("***************")
#print(G)
source = []
target = []
for x in Graph:
    for y in Graph[x]:
        if x!=y:
            source.append(x)
            target.append(y)
kg_df = pd.DataFrame({'source':source, 'target':target})


G=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.DiGraph())
#temp=nx.find_cycle(G)
#print(temp)
#G=nx.transitive_reduction(G)
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
# # Spectral
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=nx.spectral_layout(G))
plt.title("spectral")
plt.show()
