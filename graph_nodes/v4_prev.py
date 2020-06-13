from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import networkx as nx
import matplotlib.pyplot as plt
Graph={}
levels=1
#limit=""
labels = {}
appeared = {}
cncpt_ls  = []
list_of_nodes=[]



def get_nodes():
    openfile=open("nodes.txt","r")
    t=openfile.readlines()
    for x in t:
        #print(x)
        x=x.encode("utf-8")
        x=re.sub(r"/[A-Z][A-Z][A-Z]*","",x)
        x=re.sub(r"/"," ",x)
        x=re.sub(r"\n","",x)
        list_of_nodes.append(x)



def id_extractor(search_string):
    #print(type(wikipedia.search(search_string)))
    query=""
    try:
        query = wikipedia.search(search_string)[0]
    except :
        return "-1","-1"

    #print(query)
    new_string = ""
    for i in query:
        if i == " ":
            new_string = new_string + '_'
        else:
            new_string = new_string + i
    #print("New string")
    print("****************************************************************************")
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

    count = 0
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
    return wikidata_id.encode("utf-8"),node.encode("utf-8")


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
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            print(y)
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            if y not in Graph[node]:
                if y!=node:
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
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            print(y)
            if y not in Graph:
                Graph[y]=[]
                if y!=node:
                    Graph[y].append(node)
                parent(y,x,level+1)
            else:
                if y!=node:
                    Graph[y].append(node)



def save_graph(filename):
    open(filename, 'w').close()
    fout=open(filename,"w")
    for x in Graph:
        #x=x.encode("utf-8")
        fout.write(x)
        fout.write("\n")
        for y in Graph[x]:
            #y=y.encode("utf-8")
            fout.write(y)
            fout.write("\n")
        fout.write("-1\n")
    fout.close()


def load_graph():
    fin=open("gr2.txt","r")
    lines=fin.readlines()
    is_key=True
    for x in lines:
        x=x.strip()
        if is_key:
            key=x
            is_key=False
            Graph[key]=[]
        else:
            if(x=="-1"):
                is_key=True
            else:
                Graph[key].append(x)

#Not Tested Yet
def reduce_graph():
    flag=True
    while flag:
        print("$")
        to_delete=[]
        flag=False
        for x in Graph:
            if x not in list_of_nodes:
                if len(Graph[x])==0:
                    to_delete.append(x)
        for x in to_delete:
            Graph.pop(x)
            for y in Graph:
                if x in Graph[y]:
                    Graph[y].remove(x)
                    flag=True




def Graph_gen():
    load_graph()
    for node in list_of_nodes:
        save_graph("prev_gr2.txt")
        id,node=id_extractor(node)
        if id!="-1":
            if node not in Graph:
                chilldren(node,id,0)
                parent(node,id,0)
                #print(Graph)
                save_graph("gr2.txt")

def add_concept(main_concept):
    f = open("cncp.txt","a")
    f.write(main_concept)
    f.write("\n")
    f.close()

    f = open("cncp.txt","r")
    for x in f :
        x = x.replace('\n','')
        print('x',x)
        cncpt_ls.append(x)
        print(x)

def label_w(i,H):
    templist = []
    for j in cncpt_ls:
        ##is there a path between i and j
       print("source:",i)
       print("target",j)
       if nx.has_path(H,i,j):
           if nx.shortest_path_length(H,i,j)>2:
              templist.append(j)
              print("found match,adding")
    labels[i] = templist

get_nodes()
list_of_nodes=list(dict.fromkeys(list_of_nodes))

##Graph_gen()
load_graph()
for x in Graph:
    Graph[x]=list(dict.fromkeys(Graph[x]))
count=0


print("***************")
source = []
target = []
for x in Graph:
    for y in Graph[x]:
        if x!=y:
            source.append(x)
            target.append(y)
##print("here")
kg_df = pd.DataFrame({'source':source, 'target':target})
##print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.DiGraph())
print(len(G))
##for searching convert into directed Graph
H = G.to_undirected()
print(kg_df)

'''node labelling process'''
# Load nodes
# Generate Graph
# Label nodes
mn_cncpt = "artificial intelligence"
subject = "computer science"
H.add_edge(mn_cncpt,subject)
##also save grph here

'''main concept '''
add_concept(mn_cncpt)
print("mn_cncpt list",cncpt_ls)
##after this step cncpt list is updated and mn_cncpt is also added to the list to get the ans
'''Now go to each node and then label it '''
for i in  H.nodes():
    label_w(i,H) ## label and write into the file
    if len(appeared[i]) == 0:
        appeared[i].append(mn_cncpt)

##what concept do you require
concept = "machine learning"
for i in labels[concept]:
    print(i)##maybe also print the predecessor of i
for i in appeared[concept]:
    print(i)##maybe also print the predecessor of i

print("done")
